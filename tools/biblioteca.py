"""Registro único de los libros de la Biblioteca Keyons y su buscador común.

Uso:  python tools/biblioteca.py
      (después de tools/normas.py y tools/sistema_diseno.py; antes de tools/gobierno.py)

Fuente única: data/libros.json (nombre oficial, nombre corto, trama, ruta, acceso, estado editorial y prefijo).
Escribe:
- js/libro.js              el bloque LIBROS (con su presentación: documental o editorial) entre /* libros:inicio */ y /* libros:fin */ (selector y buscador)
- index.html               las seis filas de la portada entre <!-- libros:inicio --> y <!-- libros:fin --> (la portada funciona sin JS)
- data/gobierno.json       la tabla de prefijos por libro que muestra la Guía
- js/busqueda-indice.js    el índice del buscador: áreas, secciones y normas de los libros con acceso abierto

Acceso y estado son dos datos distintos: un libro puede abrirse («acceso»: «abierto») y estar en construcción.
Permisos: hoy la Biblioteca no tiene control de acceso, todo lo publicado es público. El índice reúne solo los libros
con acceso abierto. Un libro restringido necesitará un índice filtrado en el servidor (docs/BUSQUEDA_Y_PERMISOS.md).
"""
import html
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = json.load(io.open(os.path.join(ROOT, 'data', 'libros.json'), encoding='utf-8'))
ESTADOS = D['estados']
LIBROS = D['libros']
NAVS = {'marca': 'js/nav-data.js', 'sistema-diseno': 'js/nav-sistema-diseno.js'}   # mapa de navegación de cada libro abierto


def leer(p):
    return io.open(os.path.join(ROOT, p), encoding='utf-8').read()


def escribir(p, s):
    io.open(os.path.join(ROOT, p), 'w', encoding='utf-8', newline='\n').write(s)


def entre(s, a, b, nuevo, archivo):
    i, j = s.find(a), s.find(b)
    if i < 0 or j < 0:
        sys.exit(f'{archivo}: faltan las marcas {a} … {b}')
    return s[:i + len(a)] + nuevo + s[j:]


def js_str(t):
    return t.replace('\\', '\\\\').replace("'", "\\'")


def nodo(archivo, var):
    """Lee una variable global de un archivo JS del libro con Node (los mapas son JS, no JSON)."""
    code = f"global.window=global;require({json.dumps(os.path.join(ROOT, archivo))});process.stdout.write(JSON.stringify(window.{var}||null))"
    out = subprocess.run(['node', '-e', code], capture_output=True, text=True, encoding='utf-8')
    if out.returncode:
        sys.exit(f'{archivo}: {out.stderr.strip()}')
    return json.loads(out.stdout)


# ── 1 · Bloque LIBROS en js/libro.js ──
filas = []
for b in LIBROS:
    abierto = b['acceso'] == 'abierto'
    filas.append(f"    {{ id: '{b['id']}', t: '{js_str(b['nombre'])}', c: '{js_str(b['corto'])}', tr: '{b['trama']}', "
                 + (f"h: '{b['ruta']}', on: true, " if abierto else '')
                 + f"e: '{b['estado']}', el: '{js_str(ESTADOS[b['estado']])}', p: '{b.get('presentacion', 'documental')}' }}")
bloque = '\n  const LIBROS = [\n' + ',\n'.join(filas) + ',\n  ];\n  '
s = leer('js/libro.js')
escribir('js/libro.js', entre(s, '/* libros:inicio */', '/* libros:fin */', bloque, 'js/libro.js'))

# ── 2 · Filas de la portada (index.html) ──
CHECK = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5 6.2 12 13 4.5"/></svg>'
GO = '<span class="row__go" aria-hidden="true"><svg viewBox="0 0 16 16"><path d="M3 8h10M9.2 4.2 13 8l-3.8 3.8"/></svg></span>'
li = []
for n, b in enumerate(LIBROS, 1):
    e = html.escape
    lab = ESTADOS[b['estado']]
    badge = f'<span class="badge badge--on">{CHECK}{lab}</span>' if b['estado'] == 'disponible' else f'<span class="badge badge--off">{lab}</span>'
    t = f'<span class="row__t">{e(b["nombre"])}</span>'
    texto = f'<span>{t}<span class="row__d">{e(b["desc"])}</span></span>' if b['desc'] else t
    if b['acceso'] == 'abierto':
        li.append(f'      <li><a class="row" href="{b["ruta"]}"><span class="row__n">{n:02d}</span>{texto}{badge}{GO}</a></li>')
    else:
        # Un libro en preparación no se abre. Si tiene descripción, recibe foco para mostrarla con el teclado, como al pasar el cursor.
        foco = ' tabindex="0"' if b['desc'] else ''
        li.append(f'      <li><div class="row row--off"{foco} aria-disabled="true"><span class="row__n">{n:02d}</span>{texto}{badge}</div></li>')
s = leer('index.html')
escribir('index.html', entre(s, '<!-- libros:inicio -->', '<!-- libros:fin -->', '\n' + '\n'.join(li) + '\n      ', 'index.html'))

# ── 3 · Prefijos de la Guía (data/gobierno.json) ──
G = json.load(io.open(os.path.join(ROOT, 'data', 'gobierno.json'), encoding='utf-8'))
pref = [{'k': b['prefijo'], 't': b['nombre'], 'estado': b['prefijo_estado']} for b in LIBROS if b['prefijo']]
sin = [b['nombre'] for b in LIBROS if not b['prefijo']]
if sin:
    pref.append({'k': 'Por asignar', 't': ' · '.join(sin), 'estado': ESTADOS['preparacion']})
G['identificadores']['prefijos'] = pref
escribir('data/gobierno.json', json.dumps(G, ensure_ascii=False, indent=2) + '\n')

# ── 4 · Índice del buscador (js/busqueda-indice.js) ──
items = []
def anclas(ruta):
    p = os.path.join(ROOT, ruta)
    return set(re.findall(r'\sid="([^"]+)"', io.open(p, encoding='utf-8').read())) if os.path.exists(p) else set()

for b in LIBROS:
    if b['acceso'] != 'abierto':
        continue
    items.append({'t': b['nombre'], 'h': b['ruta'], 'b': b['id'], 'p': ESTADOS[b['estado']], 's': 'v'})
    nav = nodo(NAVS[b['id']], 'KEYONS_NAV') or []
    area = 'Módulo' if b['id'] == 'sistema-diseno' else 'Área'
    for a in nav:
        items.append({'t': a.get('full') or a['t'], 'h': a.get('href'), 'b': b['id'], 'p': area, 's': 'b'})
        for c in a['ch']:
            sub = ''
            for it in c['items']:
                if it.get('sub'):
                    sub = it['sub']
                    continue
                if it.get('grp'):
                    continue
                h = it.get('href')
                if h and '#' in h:   # solo anclas que existen: nada de resultados que llevan a la nada
                    pg, an = h.split('#', 1)
                    if an not in anclas(pg):
                        h = None
                items.append({'t': it['t'], 'h': h, 'b': b['id'], 'p': ' · '.join(x for x in [a['t'], c['n'] + ' ' + c['t'], sub] if x), 's': it.get('s', 'p')})

# Normas de Marca (registro de tools/normas.py)
for o in nodo('js/secciones.js', 'KEYONS_NORMAS') or []:
    if o.get('e') == 'descontinuada':
        continue
    corto = o['id'].replace('KYN-MRK-', '')
    items.append({'t': o['t'], 'h': o['h'], 'b': 'marca', 's': 'v' if o.get('e') == 'vigente' else 'b', 'n': 1,
                  'p': o['id'] + (' · integrada en ' + o['en'] if o.get('en') else '') + (' · ' + o['a'][-1] if o.get('a') else ''),
                  'k': ' '.join([o['id'], corto, o.get('n', '')] + (o.get('a') or []))})

# Normas heredadas que cita el Sistema de Diseño (KYN-PRD-UIX, sin cambios de ID)
SD = json.load(io.open(os.path.join(ROOT, 'data', 'sistema-diseno.json'), encoding='utf-8'))
for m in SD['modulos']:
    for c in m['capitulos']:
        for sc in c['subcapitulos']:
            if not sc.get('norma'):
                continue
            pg = f"sistema-diseno/{m['slug']}/{c['slug']}.html"
            an = 's-' + sc['n'].replace('.', '-')
            items.append({'t': sc['t'], 'h': pg + '#' + an if an in anclas(pg) else None, 'b': 'sistema-diseno', 'n': 1,
                          's': {'vigente': 'v', 'borrador': 'b'}.get(sc['estado'], 'p'), 'p': sc['norma'] + ' · ' + c['st'], 'k': sc['norma']})

libros = {b['id']: b['nombre'] for b in LIBROS}
escribir('js/busqueda-indice.js',
         '/* Índice del buscador de la Biblioteca. Generado por tools/biblioteca.py: no se edita a mano.\n'
         '   Reúne solo los libros con acceso abierto (data/libros.json). b: libro · p: ruta de lectura · s: estado · n: norma · k: claves. */\n'
         'window.KEYONS_BUSQUEDA = ' + json.dumps({'libros': libros, 'items': items}, ensure_ascii=False, separators=(',', ':')) + ';\n')

print(f'{len(LIBROS)} libros · {sum(1 for b in LIBROS if b["acceso"] == "abierto")} abiertos · {len(items)} entradas en el buscador')
