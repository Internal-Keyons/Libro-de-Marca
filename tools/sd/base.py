"""Sistema de Diseño · piezas comunes de los capítulos redactados (tools/sd_capitulos.py las usa con los módulos tools/sd/m*.py).

Cada norma abre como el resto de la Biblioteca: rótulo (ID y nombre corto), titular, una entrada breve y los requisitos
en filas con nivel (.sdn). La lectura principal muestra el requisito y sus decisiones esenciales; los detalles técnicos,
los casos límite y la verificación completa van en el acordeón único (reglas-visuales R27, modelo ADN-006).
Componentes del libro, elegidos por el contenido: filas rotuladas (.ed__stack), tabla (.matrix), secuencia (.steps),
correcto e incorrecto (.redline) y acordeón (.promises). Los requisitos son textos de Keylin; lo demás es propuesta en borrador.
"""
import html
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from normativa import N  # noqa: E402,F401  (los módulos lo importan desde aquí)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(ROOT, 'data', 'sd-normas.json')
REG = json.load(io.open(REGISTRO, encoding='utf-8'))
NORMAS = {n['id']: n for n in REG['normas']}
CONSTRUIDAS = {}   # id → metadatos de las normas escritas en esta corrida
esc = lambda t: html.escape(t, quote=False)
I = '        '


def P(*ps, cls=''):
    c = f' class="{cls}"' if cls else ''
    return ''.join(f'<p{c}>{p}</p>' for p in ps)


def sub(t): return f'{I}<h3 class="ed__sub">{esc(t)}</h3>'
def prosa(*ps): return f'{I}<div class="prosa">{P(*ps)}</div>'
def req(*ps):
    """Requisitos con su nivel, en filas (modelo del capítulo 01). Cada uno, un párrafo (Caso B)."""
    return f'{I}<div class="sdn">' + ''.join(f'<div class="sdn__r"><p class="sdn__t">{p}</p></div>' for p in ps) + '</div>'
def stack(filas): return f'{I}<div class="ed__stack">' + ''.join(f'<div><span class="paren">({esc(k)})</span>{P(*ps)}</div>' for k, ps in filas) + '</div>'
def matriz(etq, cols, filas):
    """Tabla del libro (.matrix): (rótulo de fila, [celdas]). Las celdas admiten código y enlaces."""
    head = ('<div class="matrix__row matrix__head" role="row"><span class="matrix__k" role="columnheader"></span>'
            + ''.join(f'<span class="matrix__lvl" role="columnheader">{esc(t)}<small>{esc(s)}</small></span>' for t, s in cols) + '</div>')
    rows = ''.join(f'<div class="matrix__row" role="row"><span class="matrix__k" role="rowheader">{esc(k)}</span>'
                   + ''.join(f'<span class="matrix__v" role="cell">{v}</span>' for v in vs) + '</div>' for k, vs in filas)
    return f'{I}<div class="matrix" role="table" aria-label="{esc(etq)}">{head}{rows}</div>'
def pasos(items):
    """Secuencia (.steps): (título, descripción, rótulo, criterio)"""
    return (f'{I}<div class="steps">' + ''.join(
        f'<div class="step"><span class="step__n">{k:02d}</span><div><p class="step__t">{esc(t)}</p><p class="step__d">{d}</p></div>'
        f'<div class="step__c"><span class="paren">({esc(r)})</span><p>{c}</p></div></div>' for k, (t, d, r, c) in enumerate(items, 1)) + '</div>')
def contraste(items):
    """Correcto e incorrecto (.redline): lo que se corrige y la forma correcta"""
    return f'{I}<div class="redline">' + ''.join(f'<div class="redline__i"><p class="redline__no">{n}</p><p class="redline__yes">{s}</p></div>' for n, s in items) + '</div>'
MAS = '<span class="btn-icon" aria-hidden="true"><svg viewBox="0 0 16 16"><path class="v" d="M8 3v10"/><path d="M3 8h10"/></svg></span>'
def detalle(items):
    """Acordeón único (R27): (título, [(rótulo, texto)]). details y summary son el control; el + es decorativo.
    Ninguno se abre solo y varios pueden quedar abiertos."""
    out = ''.join(f'<details class="promise"><summary><span class="promise__n">{k:02d}</span><span class="promise__t">{esc(t)}</span>{MAS}</summary>'
                  f'<div class="promise__body"><dl>' + ''.join(f'<div><dt class="promise__k">{esc(r)}</dt><dd>{x}</dd></div>' for r, x in filas) + '</dl></div></details>'
                  for k, (t, filas) in enumerate(items, 1))
    return f'{I}<div class="promises">{out}</div>'
def c(t): return f'<code>{esc(t)}</code>'
def cap(href, t): return f'<a class="xref" href="{href}">{esc(t)}</a>'


def ancla(capn, k):
    return 's-' + capn.replace('.', '-') + f'-{k:02d}'


def norma(nid, nombre, capitulo, slug_mod, slug_cap, k, titular, entrada, partes, origen=(), responsabilidad='', cita=''):
    """Una norma emitida en borrador. Registra su ruta y sus metadatos para data/sd-normas.json."""
    an = ancla(capitulo, k)
    previo = NORMAS.get(nid)
    if previo and previo.get('ruta') and not previo['ruta'].startswith(f'sistema-diseno/{slug_mod}/{slug_cap}.html#'):
        raise SystemExit(f'{nid} ya está emitido en otro capítulo')
    if nid in CONSTRUIDAS:
        raise SystemExit(f'{nid} se usa dos veces')
    CONSTRUIDAS[nid] = dict(id=nid, nombre=nombre, slug=slug_cap, ruta=f'sistema-diseno/{slug_mod}/{slug_cap}.html#{an}', origen=list(origen),
                            responsabilidad=responsabilidad, cita=cita)
    return (f'\n    <!-- {nid} · {nombre} -->\n    <section class="ed" id="{an}">\n'
            f'      <div class="ed__label sdn-label"><span class="ed__code" data-copy="{nid}" data-copy-msg="ID copiado · {nid}" title="Copiar el ID de esta norma">{nid}</span><span>{esc(nombre)}</span></div>\n'
            f'      <div>\n{I}<h2 class="ed__title">{esc(titular)}</h2>\n{I}<p class="ed__lead">{entrada}</p>\n' + '\n'.join(partes) + '\n      </div>\n    </section>\n')


def seccion(sid, num, corto, titular, entrada, partes):
    """Sección de lectura sin ID de norma (por ejemplo, el ejemplo de aplicación del capítulo)."""
    return (f'\n    <!-- {corto} -->\n    <section class="ed" id="{sid}">\n      <div class="ed__label"><span>{num}</span><span>{esc(corto)}</span></div>\n'
            f'      <div>\n{I}<h2 class="ed__title">{esc(titular)}</h2>\n{I}<p class="ed__lead">{entrada}</p>\n' + '\n'.join(partes) + '\n      </div>\n    </section>\n')


SD = json.load(io.open(os.path.join(ROOT, 'data', 'sistema-diseno.json'), encoding='utf-8'))
CAPS = {c['num']: (m['slug'], c['slug'], c['st']) for m in SD['modulos'] for c in m['capitulos']}


def L(num, texto=None):
    """Enlace a otro capítulo del Sistema de Diseño por su número visible (01 a 45), desde una página de capítulo."""
    mod, slug, st = CAPS[num]
    return cap(f'../{mod}/{slug}.html', texto or f'{num} {st}')
