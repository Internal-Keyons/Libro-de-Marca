"""Genera el Sistema de Diseño desde su arquitectura documental.

Uso: python tools/sistema_diseno.py

Fuente única: data/sistema-diseno.json (módulos, capítulos y subcapítulos, con estado y nombre corto).
El libro usa los mismos componentes que el Libro de Marca: cada módulo es un área.
Escribe:
- js/nav-sistema-diseno.js           índice para js/libro.js (tarjetas, menú, lateral, buscador, paginador, páginas de área)
- sistema-diseno/<módulo>.html       página de área del módulo (generada en el navegador) y normas de Marca que aplica
- sistema-diseno/<módulo>/<cap>.html página de capítulo con sus subcapítulos

La portada (sistema-diseno/index.html) y la plantilla se editan a mano.
Los números (01.02.03) son ubicación documental; no son códigos de norma.
"""
import html
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normas import ROOT  # noqa: E402

DATA = os.path.join(ROOT, 'data', 'sistema-diseno.json')
OUT = os.path.join(ROOT, 'sistema-diseno')

# Mismo ciclo de color que las áreas del Libro de Marca
COLORES = ['noche', 'cielo', 'salmon', 'atardecer']
PORTAL = {'noche': 'portal', 'cielo': 'portal portal--cielo', 'salmon': 'portal portal--salmon', 'atardecer': 'portal portal--salmon portal--atardecer'}
NOMBRE_COLOR = {'noche': 'Azul Noche', 'cielo': 'Azul Cielo', 'salmon': 'Salmón Tierra', 'atardecer': 'Salmón Atardecer'}
ESTADO = {'vigente': 'v', 'borrador': 'b', 'pendiente': 'p', 'estructura': 'e', 'revision': 'r', 'descontinuado': 'd'}
TEXTO = {'v': 'Vigente', 'b': 'Borrador', 'p': 'Contenido pendiente', 'e': 'Estructura definida', 'r': 'En revisión', 'd': 'Descontinuado'}
CLASE = {'v': 'vigente', 'b': 'borrador', 'p': 'pendiente', 'e': 'estructura', 'r': 'revision', 'd': 'descontinuado'}

CHEV = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="m6 3.5 4.5 4.5L6 12.5"/></svg>'


def e(t):
    return html.escape(t, quote=True)


def js(t):
    return t.replace('\\', '\\\\').replace("'", "\\'")


def ancla(n):
    return 's-' + n.replace('.', '-')


def head(title, root):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)} · Sistema de Diseño · Keyons</title>
<meta name="keyons:libro" content="sistema-diseno">
<meta name="keyons:version" content="0.1">
<link rel="icon" href="{root}/assets/logos/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}/css/tokens.css">
<link rel="stylesheet" href="{root}/css/libro.css">
<link rel="stylesheet" href="{root}/css/sistema-diseno.css">
</head>
'''


def foot(root):
    return f'''<script src="{root}/js/nav-sistema-diseno.js"></script>
<script src="{root}/js/libro.js"></script>
</body>
</html>
'''


def dot(k):
    return f'<span class="dot dot--{CLASE[k]}" title="{TEXTO[k]}" aria-label="{TEXTO[k]}"></span>'


def nav(d):
    """Doce áreas (una por módulo); cada capítulo lista sus subcapítulos como secciones de su página."""
    areas = []
    for i, m in enumerate(d['modulos']):
        color = COLORES[i % 4]
        caps = []
        for c in m['capitulos']:
            items = ',\n          '.join(
                f"{{ n: '{s['n']}', t: '{js(s['t'])}', st: '{js(s['st'])}', s: '{ESTADO[s['estado']]}', href: 'sistema-diseno/{m['slug']}/{c['slug']}.html#{ancla(s['n'])}' }}"
                for s in c['subcapitulos'])
            caps.append(f"      {{ n: '{c['n']}', k: '{c['n'].replace('.', '-')}', t: '{js(c['st'])}', full: '{js(c['t'])}', s: '{ESTADO[c['estado']]}', items: [\n          {items} ] }}")
        areas.append(f'''  {{
    id: '{m['k'].lower()}', k: '{m['k']}', t: '{js(m['st'])}', full: '{js(m['t'])}', href: 'sistema-diseno/{m['slug']}.html', color: '{color}', colorName: '{NOMBRE_COLOR[color]}',
    cd: '{js(m['dc'])}',
    d: '{js(m['d'])}',
    ch: [
{(',' + chr(10)).join(caps)}
    ]
  }}''')
    return '''/* ═══════════════════════════════════════════════════════════════
   KEYONS · MAPA DEL SISTEMA DE DISEÑO
   Generado por tools/sistema_diseno.py desde data/sistema-diseno.json.
   No se edita a mano: se cambia el JSON y se vuelve a generar.
   Cada módulo es un área, como en el Libro de Marca: t es el nombre corto
   (menú, tarjeta, lateral) y full el título completo (página de área).
   Los números son ubicación documental; los códigos de norma van aparte.
   ═══════════════════════════════════════════════════════════════ */
window.KEYONS_BOOK = {
  id: 'sistema-diseno',
  home: 'sistema-diseno/index.html',
  menuLabel: 'Módulos del Sistema de Diseño',
  alt: [['Libro de Marca', 'inicio.html', 'right'], ['Plantilla de norma', 'sistema-diseno/plantilla.html', 'code']],
  status: { p: 'Contenido pendiente' },
  legend: ['e', 'p', 'b', 'r', 'v', 'd'],
  words: { ch: 'Capítulos', pg: 'Subcapítulos', pgs: 'subcapítulos' },
  cardShort: true,
  areaFull: true
};

window.KEYONS_NAV = [
''' + ',\n'.join(areas) + '''
];
'''


def modulo(i, m, reg):
    refs = []
    for r in m['marca']:
        if isinstance(r, list):
            h, num, t = r
            lab = 'Capítulo'
        else:
            h, t, num = reg['KYN-MRK-' + r]
            lab = 'KYN-MRK-' + r
        refs.append(f'          <a class="kidx__r" href="../{h}"><b>{lab}</b><span class="kidx__n">{num}</span><span class="kidx__t">{e(t)}</span></a>')
    nota = f'\n        <p class="ed__more">{e(m["nota"])}</p>' if m.get('nota') else ''
    return head(m['t'], '..') + f'''<body class="is-area" data-root=".." data-area="{m['k'].lower()}" data-page="sistema-diseno/{m['slug']}.html">

<header id="topbar"></header>

<div class="doc">
  <aside class="side" id="side" aria-label="Capítulos de {e(m['st'])}"></aside>
  <main class="content">
    <nav class="crumbs" aria-label="Ruta"><a href="index.html">Sistema de Diseño</a>
      {CHEV}<span>{e(m['st'])}</span></nav>
    <!-- Contenido generado desde js/nav-sistema-diseno.js, igual que las áreas del Libro de Marca -->
    <div id="area-page"></div>

    <!-- Relación con el Libro de Marca: se cita, no se duplica -->
    <section class="ed" id="marca">
      <div class="ed__label"><span>{m['n']}</span><span>Libro de Marca</span></div>
      <div>
        <h2 class="ed__title">Normas de marca que aplica</h2>
        <p class="ed__lead">La fuente oficial de cada una es el <strong>Libro de Marca</strong>. Este módulo las aplica en la interfaz sin duplicarlas.</p>{nota}
        <div class="kidx__list sd-refs">
{chr(10).join(refs)}
        </div>
      </div>
    </section>

    <nav id="pager" aria-label="Paginación"></nav>
  </main>
</div>

''' + foot('..')


def capitulo(i, m, c):
    color = COLORES[i % 4]
    k = ESTADO[c['estado']]
    filas = '\n'.join(f'          <div class="kidx__r sd-sub" id="{ancla(s["n"])}"><b>{s["n"]}</b><span class="kidx__t">{e(s["t"])}</span>'
                      f'<span class="sd-st">{dot(ESTADO[s["estado"]])}{TEXTO[ESTADO[s["estado"]]]}</span></div>' for s in c['subcapitulos'])
    return head(c['t'], '../..') + f'''<body class="is-area" data-root="../.." data-area="{m['k'].lower()}" data-page="sistema-diseno/{m['slug']}/{c['slug']}.html">

<header id="topbar"></header>

<div class="doc">
  <aside class="side" id="side" aria-label="Capítulos de {e(m['st'])}"></aside>

  <main class="content chapter">
    <nav class="crumbs" aria-label="Ruta">
      <a href="../index.html">Sistema de Diseño</a>
      {CHEV}
      <a href="../{m['slug']}.html">{e(m['st'])}</a>
      {CHEV}
      <span>{c['n']} {e(c['st'])}</span>
    </nav>

    <section class="{PORTAL[color]}" aria-label="Capítulo {c['n']} · {e(c['t'])}">
      <div class="portal__arcs" aria-hidden="true"></div>
      <div class="portal__txt">
        <span class="kicker">Capítulo {c['n']} · {e(m['st'])}</span>
        <h1 class="t-display">{e(c['t'])}</h1>
        <p>{TEXTO[k]}. Sus {len(c['subcapitulos'])} subcapítulos todavía no tienen normas aprobadas.</p>
      </div>
    </section>

    <!-- Subcapítulos: cada uno reunirá sus normas. Generado por tools/sistema_diseno.py -->
    <section class="ed" id="subcapitulos">
      <div class="ed__label"><span>{c['n']}</span><span>Subcapítulos</span></div>
      <div>
        <h2 class="ed__title">Subcapítulos</h2>
        <p class="ed__lead">Cada subcapítulo reunirá sus <strong>reglas, ejemplos y especificaciones</strong>. Cada norma llevará un código permanente, independiente de esta numeración.</p>
        <div class="kidx__list sd-refs">
{filas}
        </div>
      </div>
    </section>

    <nav id="pager" aria-label="Paginación"></nav>
  </main>
</div>

''' + foot('../..')


def main():
    d = json.load(io.open(DATA, encoding='utf-8'))
    reg = {v['id']: (h, v['t'], v['n']) for h, v in json.load(io.open(os.path.join(ROOT, 'data', 'normas.json'), encoding='utf-8')).items() if v['estado'] == 'vigente'}
    io.open(os.path.join(ROOT, 'js', 'nav-sistema-diseno.js'), 'w', encoding='utf-8', newline='\n').write(nav(d))
    paginas = 0
    for i, m in enumerate(d['modulos']):
        io.open(os.path.join(OUT, m['slug'] + '.html'), 'w', encoding='utf-8', newline='\n').write(modulo(i, m, reg))
        os.makedirs(os.path.join(OUT, m['slug']), exist_ok=True)
        for c in m['capitulos']:
            io.open(os.path.join(OUT, m['slug'], c['slug'] + '.html'), 'w', encoding='utf-8', newline='\n').write(capitulo(i, m, c))
            paginas += 1
    nc = sum(len(m['capitulos']) for m in d['modulos'])
    ns = sum(len(c['subcapitulos']) for m in d['modulos'] for c in m['capitulos'])
    print(f'{len(d["modulos"])} módulos · {nc} capítulos · {ns} subcapítulos · {paginas} páginas de capítulo')


if __name__ == '__main__':
    main()
