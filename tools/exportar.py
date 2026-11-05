"""Tres formas de leer el Manual de Marca Keyons, generadas desde una misma fuente.

Uso:  python tools/exportar.py [--pdf]

La fuente son las páginas del libro (HTML), js/nav-data.js y data/normas.json. Este script no escribe
contenido: lo lee y lo publica en otros formatos, sin resumir ni reescribir.

- ia/libro-de-marca.md       el libro completo en Markdown, en el orden del índice
- ia/capitulos/*.md          un archivo por capítulo
- ia/normas/*.md             un archivo por norma con ID
- ia/indice.json             áreas, capítulos y normas con estado, versión, rutas y referencias
- ia/tokens.json             los tokens de css/tokens.css en formato Design Tokens (DTCG 2025.10)
- llms.txt                   la puerta de entrada para herramientas de IA
- documental/index.html      la versión íntegra para leer, imprimir o guardar como PDF
- documental/libro-de-marca-keyons.pdf   con --pdf, impreso con Edge o Chrome sin interfaz

Solo usa la biblioteca estándar de Python y Node (que normas.py ya usa para leer nav-data.js).
"""
import datetime
import html
import json
import os
import pathlib
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normas import ROOT, nav  # noqa: E402

IA = os.path.join(ROOT, 'ia')
DOC = os.path.join(ROOT, 'documental')
STATUS = {'v': 'vigente', 'b': 'borrador', 'p': 'por definir'}
PERMISOS = 'por definir; se asignarán con la Biblioteca Keyons'

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
INLINE = {'a', 'abbr', 'b', 'br', 'code', 'em', 'i', 'kbd', 'mark', 'q', 's', 'small', 'span', 'strong', 'sub', 'sup', 'time', 'u', 'label'}
SKIP_TAGS = {'script', 'style', 'template', 'header', 'aside', 'nav', 'input', 'select', 'textarea', 'noscript', 'head'}
# Piezas de interfaz o decoración que no son contenido
SKIP_CLASS = {'portal__arcs', 'hero__clouds', 'hero__glass', 'crumbs', 'btn-icon', 'fpop', 'kidx__bar', 'icat__bar', 'tester__bar'}
SKIP_CLASS_RE = re.compile(r'__(count|nav|dl|q|hint|chips|toggle)\b')


# ─── Árbol HTML mínimo ───
class Node:
    __slots__ = ('tag', 'attrs', 'kids', 'parent')

    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.kids, self.parent = tag, dict(attrs), [], parent

    def cls(self):
        return (self.attrs.get('class') or '').split()

    def has(self, c):
        return c in self.cls()

    def find_all(self, pred):
        for k in self.kids:
            if isinstance(k, Node):
                if pred(k):
                    yield k
                yield from k.find_all(pred)

    def find(self, pred):
        return next(self.find_all(pred), None)

    def text(self):
        return ''.join(k if isinstance(k, str) else (' ' if k.tag == 'br' else k.text()) for k in self.kids)


class Tree(HTMLParser):
    def __init__(self, src):
        super().__init__(convert_charrefs=True)
        self.root = Node('#root', {}, None)
        self.cur = self.root
        self.feed(src)

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.kids.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.kids.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.kids.append(data)


def ws(s):
    return re.sub(r'\s+', ' ', s.replace('\xa0', ' '))


def joinp(parts):
    """Une piezas de texto. Dos elementos pegados (un rótulo y su texto, dos celdas) se separan con « · »."""
    out, prev_el = '', False
    for el, t in parts:
        if not t:
            continue
        if (el or prev_el) and out and re.match(r'[\w*(«¿¡]', t):
            if re.search(r'[\w*)»]$', out):
                out += ' · '
            elif re.search(r'[.?!:;]$', out):
                out += ' '
        out += t
        prev_el = el
    return out


def plain(n):
    """Texto de un elemento, con separación entre sus piezas."""
    return ws(joinp((isinstance(k, Node), ws(k) if isinstance(k, str) else plain(k)) for k in n.kids)).strip()


# ─── Conversión a bloques ───
# Un bloque es (tipo, datos): h (nivel, texto) · p (texto) · lines [textos] · ul/ol [textos]
# · table [filas] · res (texto de recurso visual) · meta [(clave, valor)]
class Page:
    def __init__(self, path, normas):
        self.path = path
        self.dir = posixpath.dirname(path)
        self.normas = normas
        self.tree = Tree(open(os.path.join(ROOT, path), encoding='utf-8').read()).root
        # Nombre de cada pestaña, por el id del panel o por el valor data-* que comparten
        self.tabs = {}
        for t in self.tree.find_all(lambda n: n.attrs.get('role') == 'tab'):
            name = ws(t.text()).strip()
            keys = [t.attrs.get('aria-controls')] + [v for k, v in t.attrs.items() if k.startswith('data-') and v and not v.replace('.', '').isdigit()]
            for k in keys:
                if k:
                    self.tabs.setdefault(k, name)

    def tab_name(self, n):
        a = n.attrs
        for k in [a.get('id')] + [v for x, v in a.items() if x.startswith('data-')]:
            if k and k in self.tabs:
                return self.tabs[k]
        return None

    def url(self, ref):
        """Ruta del sitio desde la raíz, para enlaces y recursos."""
        if not ref or ref.startswith(('http:', 'https:', 'mailto:', 'tel:', 'data:')):
            return ref
        if ref.startswith('#'):
            return '/' + self.path + ref
        return '/' + posixpath.normpath(posixpath.join(self.dir, ref))

    # Elementos
    def skip(self, n):
        if n.tag in SKIP_TAGS or n.attrs.get('id') == 'pager' or 'aria-live' in n.attrs:
            return True
        # Los botones son controles, salvo los que llevan contenido: descripciones, viñetas, imágenes, íconos y marcas
        if n.tag == 'button' and not any(x in n.attrs for x in ('data-d', 'data-vf', 'data-cred', 'data-cap')) and not n.has('ict') \
                and not n.find(lambda x: x.tag == 'svg' and x.attrs.get('role') == 'img'):
            return True
        c = n.cls()
        return any(x in SKIP_CLASS or SKIP_CLASS_RE.search(x) for x in c)

    def is_block(self, n):
        if not isinstance(n, Node) or self.skip(n):
            return False
        if n.tag in ('svg', 'img'):
            return self.visual(n) is not None
        if n.tag not in INLINE or any(x in n.attrs for x in ('data-cap', 'data-cred', 'data-tip')):
            return True
        return any(self.is_block(k) for k in n.kids)

    def visual(self, n):
        """Texto de recurso visual de un elemento, o None si es decoración."""
        a = n.attrs
        label = a.get('aria-label') or a.get('alt') or a.get('title') or ''
        if n.tag == 'img':
            return f'Imagen: {self.url(a.get("src", ""))}' + (f' · «{label}»' if label else '')
        if n.tag == 'svg':
            fig = n.parent and (n.parent.tag == 'figure' or any('fig' in c or 'stage' in c or c == 'orient' for c in n.parent.cls()))
            if a.get('role') != 'img' and not fig:
                return None
            texts = [ws(t.text()).strip() for t in n.find_all(lambda x: x.tag == 'text')]
            tips = [g.attrs['data-tip'].replace('|', ': ') for g in n.find_all(lambda x: 'data-tip' in x.attrs)]
            s = 'Gráfico SVG en línea' if a.get('role') == 'img' else 'Ilustración SVG en línea'
            if label:
                s += f' · «{label}»'
            uses = [u.attrs.get('href') for u in n.find_all(lambda x: x.tag == 'use')]
            if uses:
                s += ' · Símbolo: ' + ', '.join(sorted(set(uses)))
            if texts:
                s += ' · Textos: ' + ' / '.join(t for t in texts if t)
            if tips:
                s += ' · Al pasar el cursor: ' + ' / '.join(tips)
            return s
        return None

    def bg(self, n):
        out = []
        st = n.attrs.get('style') or ''
        for u in re.findall(r'url\(([^)]+)\)', st):
            out.append(self.url(u.strip('\'"')))
        if n.attrs.get('data-src'):
            out.append(self.url(n.attrs['data-src']))
        return out

    # Texto en línea
    def inl(self, n):
        if isinstance(n, str):
            return ws(n)
        if self.skip(n) or n.attrs.get('aria-hidden') == 'true' or n.tag in ('svg', 'img'):
            return ''
        if n.tag == 'br':
            return ' '
        inner = joinp((isinstance(k, Node), self.inl(k)) for k in n.kids)
        core = inner.strip()
        if not core:
            return inner if inner.isspace() else ''
        lead, trail = inner[:len(inner) - len(inner.lstrip())], inner[len(inner.rstrip()):]
        if n.tag in ('strong', 'b') or n.has('paren'):
            return f'{lead}**{core}**{trail}'
        if n.tag == 'em' or (n.tag == 'i' and core):
            return f'{lead}*{core}*{trail}'
        if n.tag == 'code':
            return f'{lead}`{core}`{trail}'
        if n.tag == 'a' and n.attrs.get('href') and n.attrs['href'] != '#':
            return f'{lead}[{core}]({self.url(n.attrs["href"])}){trail}'
        return inner

    def line(self, n):
        return re.sub(r'\*\*\s*\*\*', '', re.sub(r' +', ' ', self.inl(n))).strip()

    # Bloques
    def blocks(self, n, lvl):
        out, buf = [], []

        def flush():
            t = re.sub(r' +', ' ', joinp(buf)).strip()
            if t:
                out.append(('p', t))
            buf.clear()

        for k in n.kids:
            if isinstance(k, str):
                buf.append((False, ws(k)))
                continue
            if self.skip(k):
                continue
            if not self.is_block(k) and k.attrs.get('aria-hidden') != 'true':
                buf.append((True, self.inl(k)))
                if k.tag == 'span' and k.has('paren'):
                    buf.append((False, ' '))
                continue
            flush()
            out += self.block(k, lvl)
        flush()
        return out

    def leafy(self, n):
        """Un grupo pequeño de piezas de texto: se lee como un solo bloque de líneas."""
        kids = [k for k in n.kids if isinstance(k, Node) and not self.skip(k) and k.attrs.get('aria-hidden') != 'true']
        if len(kids) < 2 or any(isinstance(k, str) and k.strip() for k in n.kids):
            return None
        for k in kids:
            if k.tag in ('ul', 'ol', 'dl', 'table', 'figure', 'details', 'section', 'svg', 'img', 'button', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6') \
                    or k.attrs.get('role') in ('table', 'img', 'tabpanel'):
                return None
            if any(self.is_block(g) for g in k.kids) or self.bg(k):
                return None
        lines = [self.line(k) for k in kids]
        return [x for x in lines if x] or None

    def block(self, n, lvl):
        a, c = n.attrs, n.cls()
        if a.get('aria-hidden') == 'true':
            imgs = [self.url(i.attrs.get('src', '')) for i in n.find_all(lambda x: x.tag == 'img')]
            if imgs:
                return [('res', 'Imágenes de ejemplo: ' + ', '.join(imgs))]
            if n.tag != 'svg' and n.text().strip():
                return [('res', 'Muestra visual: ' + plain(n))]
            if n.tag in ('div', 'figure') and c:
                return [('res', f'Demostración visual (clase `{c[0]}`)')]
            return []
        if n.tag in ('svg', 'img'):
            v = self.visual(n)
            return [('res', v)] if v else []
        res = []
        if a.get('role') == 'img':
            res.append(('res', 'Figura: «' + (a.get('aria-label') or '') + '»' + ''.join(f' · {u}' for u in self.bg(n))))
        elif self.bg(n):
            res.append(('res', 'Imagen de fondo: ' + ', '.join(self.bg(n))))
        if 'data-cap' in a or 'data-cred' in a:
            res.append(('res', ' · '.join(x for x in (a.get('data-cap'), a.get('data-cred')) if x)))

        if n.tag == 'section' and n.find(lambda x: x.has('ed__label')) and a.get('id'):
            return res + self.section(n, lvl)
        if n.has('portal'):
            return res + self.portal(n, lvl)
        if n.tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            t = self.line(n)
            if not t:
                return res
            depth = max(lvl, lvl + int(n.tag[1]) - 2)
            return res + ([('h', depth, t)] if depth <= 6 else [('p', f'**{t}**')])
        if n.tag in ('ul', 'ol'):
            items = [self.flat(li) for li in n.kids if isinstance(li, Node) and li.tag == 'li']
            return res + [(n.tag, [i for i in items if i])]
        if n.tag == 'table' or a.get('role') == 'table':
            return res + self.table(n)
        if n.tag == 'details':
            s = n.find(lambda x: x.tag == 'summary')
            out = res + ([('p', '**' + self.line(s) + '**')] if s else [])
            body = Node('div', {}, n)
            body.kids = [k for k in n.kids if k is not s]
            return out + self.blocks(body, lvl)
        if n.has('ict'):
            return res + [('ul', [f'Ícono `{a.get("data-n")}`' + (' · ajustado a la retícula, pendiente de revisión' if n.has('is-rev') else '')])]
        if n.has('vdemo__s'):
            return res + [('res', 'Ejemplo dibujado: ' + plain(n) if plain(n) else 'Ejemplo dibujado')]
        if n.tag == 'button' and 'data-vf' in a:
            return res + [('res', f'Viñeta {self.line(n)}: SVG en línea que se copia con el color elegido')]
        if n.tag == 'button' and 'data-d' in a:
            w = a.get('data-w') or self.line(n)
            return res + [('ul', [f'**{w}**: {a["data-d"]}'])]
        if a.get('role') == 'tabpanel' and self.tab_name(n):
            return res + [('p', f'**{self.tab_name(n)}**')] + self.blocks(n, lvl)
        if n.tag == 'dl':
            items, dt = [], None
            for k in n.find_all(lambda x: x.tag in ('dt', 'dd')):
                if k.tag == 'dt':
                    dt = self.line(k)
                else:
                    items.append(f'**{dt}**: {self.line(k)}' if dt else self.line(k))
                    dt = None
            return res + [('ul', items)]
        lf = self.leafy(n)
        if lf:
            return res + ([('lines', lf)] if len(lf) > 1 else [('p', lf[0])])
        inner = self.blocks(n, lvl)
        tips = [] if n.tag == 'svg' else [x.attrs['data-tip'] for x in [n] if 'data-tip' in x.attrs]
        return res + inner + [('res', 'Al pasar el cursor: ' + t.replace('|', ': ')) for t in tips]

    def flat(self, li):
        parts = []
        for k in li.kids:
            if isinstance(k, str):
                parts.append((False, ws(k)))
            elif not self.skip(k):
                parts.append((True, self.inl(k) if not self.is_block(k) else self.flat(k)))
        return re.sub(r' +', ' ', joinp(parts)).strip()

    def table(self, n):
        rows = []
        if n.tag == 'table':
            for tr in n.find_all(lambda x: x.tag == 'tr'):
                rows.append([self.flat(td) for td in tr.kids if isinstance(td, Node) and td.tag in ('td', 'th')])
        else:
            for r in n.find_all(lambda x: x.attrs.get('role') == 'row'):
                kids = [k for k in r.kids if isinstance(k, Node)]
                cells = [k for k in kids if k.attrs.get('role') in ('cell', 'columnheader', 'rowheader', 'gridcell')] or kids
                rows.append([self.flat(k) for k in cells])
        rows = [r for r in rows if any(r)]
        return [('table', rows)] if rows else []

    def section(self, n, lvl):
        lab = n.find(lambda x: x.has('ed__label'))
        spans = [ws(s.text()).strip() for s in lab.kids if isinstance(s, Node)]
        num, name = (spans + ['', ''])[:2]
        key = f'{self.path}#{n.attrs["id"]}'
        nor = self.normas.get(key)
        head = f'{nor["id"]} · {num} {name}' if nor else f'{num} {name}'
        meta = [('Número', num)]
        if nor:
            meta += [('ID', nor['id']), ('Estado', nor['estado'])]
        meta.append(('Fuente', '/' + key))
        body = Node('div', {}, n)
        body.kids = [k for k in n.kids if k is not lab]
        inner = self.blocks(body, lvl + 1)
        sec = {'key': key, 'num': num, 'name': name, 'norma': nor, 'blocks': inner}
        self.sections.append(sec)
        return [('h', lvl, head), ('meta', meta)] + inner

    def portal(self, n, lvl):
        k = n.find(lambda x: x.has('kicker'))
        h = n.find(lambda x: x.tag == 'h1')
        ps = [self.line(p) for p in n.find_all(lambda x: x.tag == 'p')]
        out = [('h', lvl, self.line(h) if h else '')]
        meta = [('Fuente', '/' + self.path)]
        if k:
            meta.insert(0, ('Rótulo', self.line(k)))
        out.append(('meta', meta))
        out += [('p', p) for p in ps if p]
        out += [('res', 'Imagen de fondo: ' + ', '.join(self.bg(n)))] if self.bg(n) else []
        return out

    def content(self, lvl):
        """Bloques de la página: el encabezado (portal o héroe) y sus secciones."""
        self.sections = []
        main = self.tree.find(lambda x: x.tag == 'main')
        return self.blocks(main, lvl)


# ─── Salidas ───
def merge(blocks):
    """Junta listas seguidas: varios botones con descripción forman una sola lista."""
    out = []
    for b in blocks:
        if out and b[0] == 'ul' and out[-1][0] == 'ul':
            out[-1] = ('ul', out[-1][1] + b[1])
        else:
            out.append(b)
    return out


def md(blocks):
    out = []
    for b in merge(blocks):
        t = b[0]
        if t == 'h':
            out.append('#' * b[1] + ' ' + b[2])
        elif t == 'p':
            out.append(b[1])
        elif t == 'lines':
            out.append('\n'.join(b[1]))
        elif t in ('ul', 'ol'):
            out.append('\n'.join(('- ' if t == 'ul' else f'{i}. ') + x for i, x in enumerate(b[1], 1)))
        elif t == 'table':
            w = max(len(r) for r in b[1])
            rows = [r + [''] * (w - len(r)) for r in b[1]]
            esc = lambda s: s.replace('|', '\\|')
            out.append('\n'.join(['| ' + ' | '.join(esc(c) for c in rows[0]) + ' |', '|' + '---|' * w]
                                 + ['| ' + ' | '.join(esc(c) for c in r) + ' |' for r in rows[1:]]))
        elif t == 'res':
            out.append('> Recurso visual: ' + b[1])
        elif t == 'meta':
            out.append(' · '.join(f'{k}: `{v}`' if k in ('Fuente', 'ID', 'Ruta') else f'{k}: {v}' for k, v in b[1]))
    return '\n\n'.join(out)


def inline_html(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s


def to_html(blocks):
    out = []
    for b in merge(blocks):
        t = b[0]
        if t == 'h':
            out.append(f'<h{b[1]}>{inline_html(b[2])}</h{b[1]}>')
        elif t == 'p':
            out.append(f'<p>{inline_html(b[1])}</p>')
        elif t == 'lines':
            out.append('<p class="lines">' + '<br>'.join(inline_html(x) for x in b[1]) + '</p>')
        elif t in ('ul', 'ol'):
            out.append(f'<{t}>' + ''.join(f'<li>{inline_html(x)}</li>' for x in b[1]) + f'</{t}>')
        elif t == 'table':
            head, *rows = b[1]
            out.append('<table><thead><tr>' + ''.join(f'<th>{inline_html(c)}</th>' for c in head) + '</tr></thead><tbody>'
                       + ''.join('<tr>' + ''.join(f'<td>{inline_html(c)}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table>')
        elif t == 'res':
            out.append(f'<p class="res">Recurso visual · {inline_html(b[1])}</p>')
        elif t == 'meta':
            out.append('<p class="meta">' + ' · '.join(f'{k}: {html.escape(v)}' for k, v in b[1]) + '</p>')
    return '\n'.join(out)


def front(d):
    def val(v):
        if isinstance(v, list):
            return '[' + ', '.join(json.dumps(x, ensure_ascii=False) for x in v) + ']'
        return json.dumps(v, ensure_ascii=False)
    return '---\n' + ''.join(f'{k}: {val(v)}\n' for k, v in d.items()) + '---\n\n'


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


IDRE = re.compile(r'KYN-MRK-[A-Z]{2,4}-\d{3}')


def refs(blocks):
    return sorted(set(IDRE.findall(md(blocks))))


# ─── Tokens en formato DTCG ───
def tokens():
    src = open(os.path.join(ROOT, 'css', 'tokens.css'), encoding='utf-8').read()
    body = src[src.index(':root{'):]
    body = body[:body.index('\n}')]
    layer, groups, skipped = 'primitivos', {'primitivos': {}, 'semanticos': {}, 'componentes': {}}, []
    names = {}
    for line in body.split('\n'):
        if '2 · SEMÁNTICOS' in line:
            layer = 'semanticos'
        elif '3 · COMPONENTES' in line:
            layer = 'componentes'
        com = re.search(r'/\*\s*(.+?)\s*\*/\s*$', line)
        decls = re.findall(r'--([\w-]+):([^;]+);', line)
        for name, v in decls:
            names[name] = layer
            tok = conv(v.strip(), names)
            if tok is None:
                skipped.append(name)
                continue
            if com and len(decls) == 1:
                tok['$description'] = com.group(1)
            groups[layer][name] = tok
    groups['$description'] = ('Tokens de css/tokens.css en formato del Design Tokens Community Group (2025.10). '
                              'Tres capas: primitivos, semánticos y componentes. Los productos leen semánticos y componentes.')
    return groups, skipped


def conv(v, names):
    m = re.fullmatch(r'var\(--([\w-]+)\)', v)
    if m and m.group(1) in names:
        return {'$value': '{' + names[m.group(1)] + '.' + m.group(1) + '}'}
    m = re.fullmatch(r'#([0-9A-Fa-f]{6})', v)
    if m:
        h = m.group(1)
        return {'$type': 'color', '$value': {'colorSpace': 'srgb', 'components': [round(int(h[i:i + 2], 16) / 255, 4) for i in (0, 2, 4)], 'hex': '#' + h.upper()}}
    m = re.fullmatch(r'rgba\((\d+),(\d+),(\d+),([\d.]+)\)', v.replace(' ', ''))
    if m:
        r, g, b, al = m.groups()
        return {'$type': 'color', '$value': {'colorSpace': 'srgb', 'components': [round(int(x) / 255, 4) for x in (r, g, b)], 'alpha': float(al),
                                             'hex': '#%02X%02X%02X' % (int(r), int(g), int(b))}}
    m = re.fullmatch(r'(-?[\d.]+)px', v)
    if m:
        return {'$type': 'dimension', '$value': {'value': float(m.group(1)) if '.' in m.group(1) else int(m.group(1)), 'unit': 'px'}}
    m = re.fullmatch(r'([\d.]+)ms', v)
    if m:
        return {'$type': 'duration', '$value': {'value': int(m.group(1)), 'unit': 'ms'}}
    m = re.fullmatch(r'cubic-bezier\(([^)]+)\)', v)
    if m:
        return {'$type': 'cubicBezier', '$value': [float(x) for x in m.group(1).split(',')]}
    if re.search(r"'[^']+'", v) and ',' in v:
        return {'$type': 'fontFamily', '$value': [x.strip().strip("'") for x in v.split(',')]}
    return None


# ─── Libro ───
def main():
    today = datetime.date.today().isoformat()
    inicio = open(os.path.join(ROOT, 'inicio.html'), encoding='utf-8').read()
    version = re.search(r'<meta name="keyons:version" content="([\d.]+)">', inicio).group(1)
    reg = json.load(open(os.path.join(ROOT, 'data', 'normas.json'), encoding='utf-8'))
    areas = nav()

    for d in (os.path.join(IA, 'capitulos'), os.path.join(IA, 'normas')):
        shutil.rmtree(d, ignore_errors=True)

    base = {'manual': 'Libro de Marca Keyons', 'version': version, 'fecha': today, 'permisos': PERMISOS}
    full = [('h', 1, 'Libro de Marca Keyons'),
            ('meta', [('Versión', version), ('Fecha de exportación', today), ('Fuente', '/inicio.html'), ('Permisos', PERMISOS)]),
            ('p', 'Exportación íntegra generada desde las páginas del libro con tools/exportar.py. Conserva la redacción y el orden '
                  'del índice. Cada sección indica su ruta de origen; los recursos visuales se citan con su ruta o su descripción.')]
    home = Page('inicio.html', reg)
    full += [('h', 2, 'Presentación')] + home.content(3)

    index = {**base, 'areas': [], 'normas': []}
    norm_rows = {}
    for ai, a in enumerate(areas, 1):
        ah = [('h', 2, f'Área {ai:02d} · {a.get("full") or a["t"]}'),
              ('meta', [('Color', a['colorName']), ('Fuente', '/' + a['href'])]),
              ('p', a['d'])]
        full += ah
        arow = {'id': a['id'], 'titulo': a.get('full') or a['t'], 'descripcion': a['d'], 'color': a['colorName'], 'ruta': '/' + a['href'], 'capitulos': []}
        for c in a['ch']:
            pages = []
            for it in c['items']:
                h = it.get('href', '').split('#')[0]
                if h and h not in pages:
                    pages.append(h)
            items = []
            for it in c['items']:
                if 'sub' in it or 'grp' in it:
                    items.append(f'**{it.get("sub") or it.get("grp")}**')
                    continue
                s = f'{it["t"]} · {STATUS.get(it.get("s"), "por definir")}'
                items.append(s + (f' · `/{it["href"]}`' if it.get('href') else ''))
            title = f'Capítulo {c["n"]} · {c["t"]}'
            meta = [('Estado', STATUS[c['s']]), ('Clave', c['k'])] + [('Ruta', '/' + p) for p in pages]
            if c.get('was'):
                meta.append(('Número anterior', ', '.join([c['was']] if isinstance(c['was'], str) else c['was'])))

            def chapter(l):
                out = [('h', l, title), ('meta', meta), ('p', c['d']), ('p', '**Contenido del capítulo**'), ('ul', items)]
                secs = []
                for p in pages:
                    pg = Page(p, reg)
                    out += pg.content(l + 1)
                    secs += pg.sections
                if not pages:
                    out.append(('p', '*Capítulo sin página: solo existe su índice en el libro.*'))
                return out, secs

            blocks, secs = chapter(3)
            full += blocks
            cblocks, _ = chapter(1)
            slug = f'{c["n"]}-{c["k"]}'
            cref = refs(cblocks)
            write(os.path.join(IA, 'capitulos', slug + '.md'),
                  front({**base, 'capitulo': c['n'], 'titulo': c['t'], 'area': a.get('full') or a['t'], 'estado': STATUS[c['s']],
                         'rutas': ['/' + p for p in pages], 'normas': [s['norma']['id'] for s in secs if s['norma']], 'referencias': cref})
                  + md(cblocks) + '\n')
            arow['capitulos'].append({'n': c['n'], 'clave': c['k'], 'titulo': c['t'], 'estado': STATUS[c['s']], 'descripcion': c['d'],
                                      'rutas': ['/' + p for p in pages], 'markdown': f'/ia/capitulos/{slug}.md',
                                      'normas': [s['norma']['id'] for s in secs if s['norma']]})
            for s in secs:
                nor = s['norma']
                if not nor:
                    continue
                r = [x for x in refs(s['blocks']) if x != nor['id']]
                norm_rows[nor['id']] = {'id': nor['id'], 'titulo': nor['t'], 'numero': s['num'], 'rotulo': s['name'], 'estado': nor['estado'],
                                        'capitulo': c['n'], 'area': a['id'], 'fuente': '/' + s['key'],
                                        'markdown': f'/ia/normas/{nor["id"]}.md', 'referencias': r}
                nb = [('h', 1, f'{nor["id"]} · {s["name"]}'),
                      ('meta', [('Número', s['num']), ('Estado', nor['estado']), ('Capítulo', f'{c["n"]} {c["t"]}'), ('Fuente', '/' + s['key'])])] + s['blocks']
                norm_rows[nor['id']]['_md'] = (front({**base, 'id': nor['id'], 'titulo': nor['t'], 'numero': s['num'], 'estado': nor['estado'],
                                                     'capitulo': f'{c["n"]} {c["t"]}', 'area': a.get('full') or a['t'], 'fuente': '/' + s['key'],
                                                     'referencias': r}), nb)
        index['areas'].append(arow)

    # Normas registradas: las que no tienen sección (descontinuadas) quedan en el índice con su estado
    for h, v in reg.items():
        if v['id'] not in norm_rows:
            norm_rows[v['id']] = {'id': v['id'], 'titulo': v['t'], 'numero': v['n'], 'estado': v['estado'], 'fuente': '/' + h, 'referencias': []}
    cited = {}
    for r in norm_rows.values():
        for x in r['referencias']:
            cited.setdefault(x, []).append(r['id'])
    for nid, r in sorted(norm_rows.items()):
        r['citada_por'] = sorted(cited.get(nid, []))
        if '_md' in r:
            fm, nb = r.pop('_md')
            fm = fm.replace('---\n\n', f'citada_por: {json.dumps(r["citada_por"], ensure_ascii=False)}\n---\n\n', 1) if fm.endswith('---\n\n') else fm
            write(os.path.join(IA, 'normas', nid + '.md'), fm + md(nb) + '\n')
        index['normas'].append(r)

    write(os.path.join(IA, 'libro-de-marca.md'), front(base) + md(full) + '\n')
    write(os.path.join(IA, 'indice.json'), json.dumps(index, ensure_ascii=False, indent=1) + '\n')
    tk, skipped = tokens()
    write(os.path.join(IA, 'tokens.json'), json.dumps(tk, ensure_ascii=False, indent=1) + '\n')

    caps = [c for a in index['areas'] for c in a['capitulos']]
    write(os.path.join(ROOT, 'llms.txt'), '\n'.join([
        '# Libro de Marca Keyons', '',
        f'> Manual de identidad y expresión visual de Keyons. Versión {version}, exportada el {today}. '
        'Cada norma tiene un ID permanente KYN-MRK-XXX-### y un estado: vigente, borrador o descontinuada.', '',
        'Escrito una vez en el libro (HTML) y publicado en tres formas: lectura visual, documental y estructurada. '
        f'Permisos: {PERMISOS}.', '',
        '## Antes de consultar', '',
        '- [Convenciones de autoridad normativa](/ia/gobierno.json): niveles DEBE, NO DEBE, DEBERÍA y PUEDE; estados de vigencia; ámbitos; aprobación, excepciones y citación. Una clasificación propuesta por IA no tiene vigencia sin aprobación humana.',
        '- [Rutas de lectura y convenciones en la web](/recursos/gobierno.html)', '',
        '## Libro completo', '',
        '- [Libro completo en Markdown](/ia/libro-de-marca.md)',
        '- [Índice de áreas, capítulos y normas](/ia/indice.json): estado, versión, rutas y referencias cruzadas',
        '- [Tokens de diseño](/ia/tokens.json): formato Design Tokens Community Group', '',
        '## Capítulos', ''] + [f'- [{c["n"]} {c["titulo"]}]({c["markdown"]}): {c["descripcion"]}' for c in caps] + [
        '', '## Normas', '', 'Un archivo por norma en /ia/normas/<ID>.md; la lista completa está en el índice.', '']))

    # Lectura documental
    toc = ''.join(f'<li><a href="#{b[2].split(" · ")[0].replace(" ", "-")}">{html.escape(b[2])}</a></li>' for b in full if b[0] == 'h' and b[1] == 2)
    body = to_html(full[3:])
    body = re.sub(r'<h2>([^<]+)</h2>', lambda m: f'<h2 id="{html.unescape(m.group(1)).split(" · ")[0].replace(" ", "-")}">{m.group(1)}</h2>', body)
    tpl = open(os.path.join(ROOT, 'tools', 'documental.html'), encoding='utf-8').read()
    write(os.path.join(DOC, 'index.html'), tpl.replace('{{VERSION}}', version).replace('{{FECHA}}', today).replace('{{TOC}}', toc).replace('{{BODY}}', body))

    print(f'{len(caps)} capítulos · {sum(1 for r in norm_rows.values() if "markdown" in r)} normas con archivo · '
          f'{len(norm_rows)} en el índice · tokens sin formato DTCG: {", ".join(skipped) or "ninguno"}')
    if '--pdf' in sys.argv:
        pdf()


def pdf():
    for exe in (r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe', r'C:\Program Files\Google\Chrome\Application\chrome.exe',
                shutil.which('msedge') or '', shutil.which('google-chrome') or '', shutil.which('chromium') or ''):
        if exe and os.path.exists(exe):
            out = os.path.join(DOC, 'libro-de-marca-keyons.pdf')
            src = pathlib.Path(DOC, 'index.html').as_uri()
            # Un perfil propio evita que el navegador ya abierto reciba la orden y no imprima
            with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as prof:
                subprocess.run([exe, '--headless', '--disable-gpu', '--no-pdf-header-footer', '--virtual-time-budget=15000',
                                f'--user-data-dir={prof}', f'--print-to-pdf={out}', src], capture_output=True, timeout=300)
            if os.path.exists(out):
                print('PDF:', os.path.relpath(out, ROOT), f'{os.path.getsize(out) // 1024} KB')
            else:
                print('El navegador no generó el PDF: se obtiene imprimiendo documental/index.html')
            return
    print('No se encontró Edge ni Chrome: el PDF se obtiene imprimiendo documental/index.html')


if __name__ == '__main__':
    main()
