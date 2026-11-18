"""Sistema de Diseño · piezas comunes de los capítulos redactados (tools/sd_capitulos.py las usa con los módulos tools/sd/m*.py).

Criterios: Guía de la Biblioteca 05, bloques «Sistema de diagramación» y «Composición normativa según el contenido»
(fuente única; aquí no se copian). Cada norma abre con rótulo, titular directo y una entrada que aclara su función. Después,
su composición principal según el contenido: requisito central con sus filas (req + stack), dimensiones que integran cada
requisito con su decisión (dims), tabla (matriz) o secuencia (pasos). Los apartados complementarios van solo cuando hacen
falta (detalle). La verificación es parte de la norma (verif) y se presenta según su función (ver): breve, técnica, agrupada
en la validación del capítulo o como referencia. Las verificaciones se escriben solo aquí; data/sd-normas.json las recibe al
generar. Los requisitos son textos de Keylin; lo demás es propuesta en borrador.
"""
import html
import io
import re
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from normativa import N, MARCADAS, plano as _np  # noqa: E402,F401  (los módulos lo importan desde aquí)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(ROOT, 'data', 'sd-normas.json')
REG = json.load(io.open(REGISTRO, encoding='utf-8'))
NORMAS = {n['id']: n for n in REG['normas']}
CONSTRUIDAS = {}   # id → metadatos de las normas escritas en esta corrida
VALIDADOS = set()   # capítulos con su sección «Validación del capítulo»
# Etiqueta corta del menú lateral (Guía 05 · Sistema de diagramación): completa y en un renglón; el nombre largo queda en la página
CORTOS = {
    'KYN-SDI-PEX-002': 'Claridad primero', 'KYN-SDI-PEX-003': 'Complejidad', 'KYN-SDI-PEX-005': 'Previsibilidad',
    'KYN-SDI-PEX-006': 'Contexto previo', 'KYN-SDI-PEX-018': 'Reconocer', 'KYN-SDI-PEX-007': 'Personas reales',
    'KYN-SDI-PEX-009': 'Frecuencia de uso', 'KYN-SDI-PEX-010': 'Decisiones', 'KYN-SDI-PEX-011': 'Prisma',
    'KYN-SDI-PEX-013': 'Resultados', 'KYN-SDI-PEX-014': 'Evidencia', 'KYN-SDI-ARQ-001': 'Organización',
    'KYN-SDI-ARQ-002': 'Nombres', 'KYN-SDI-ARQ-004': 'Detalle a pedido', 'KYN-SDI-ARQ-008': 'Controles',
    'KYN-SDI-ARQ-009': 'Adaptación', 'KYN-SDI-ARQ-017': 'Acceso directo', 'KYN-SDI-ARQ-012': 'Pertinencia',
    'KYN-SDI-ARQ-013': 'Resultados claros', 'KYN-SDI-ARQ-016': 'Permisos',
}
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
def dims(filas):
    """Dimensiones integradas (Guía 05 · Composición normativa): cada fila reúne el requisito de su dimensión, con su nivel (N),
    y su decisión de aplicación, sin repetirse en otra composición: (rótulo, [requisito, decisión, …]).
    Requisito y decisión van en el color principal de lectura (Guía 05 · Color del texto): los distinguen el orden, el nivel
    al final del requisito y el párrafo propio, no el color."""
    return stack(filas)
def matriz(etq, cols, filas, kh=False):
    """Tabla del libro (.matrix): (rótulo de fila, [celdas]). Las celdas admiten código y enlaces; con kh, también el rótulo."""
    head = ('<div class="matrix__row matrix__head" role="row"><span class="matrix__k" role="columnheader"></span>'
            + ''.join(f'<span class="matrix__lvl" role="columnheader">{esc(t)}<small>{esc(s)}</small></span>' for t, s in cols) + '</div>')
    rows = ''.join(f'<div class="matrix__row" role="row"><span class="matrix__k" role="rowheader">{k if kh else esc(k)}</span>'
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
MAS_DET = '<svg class="det__mas" viewBox="0 0 16 16" aria-hidden="true"><path class="v" d="M8 3v10" stroke="currentColor" stroke-width="1.5"/><path d="M3 8h10" stroke="currentColor" stroke-width="1.5"/></svg>'
def detalle(items):
    """Detalle plegable simple (Guía 05 · Sistema de diagramación): un bloque secundario por tema
    (verificación, entregable, notas técnicas, evidencia, excepciones): (rótulo, [(rótulo, texto)]).
    details y summary son el control; el + es decorativo; ninguno se abre solo y varios pueden quedar abiertos."""
    out = ''.join(f'<details class="det"><summary>{esc(t)}{MAS_DET}</summary>'
                  f'<div class="det__c"><dl>' + ''.join(f'<div><dt class="promise__k">{esc(r)}</dt><dd>{x}</dd></div>' for r, x in filas) + '</dl></div></details>'
                  for t, filas in items)
    return f'{I}<div class="dets">{out}</div>'
def serie(items):
    """Serie desplegable (R27, modelo ADN-006): varios ítems comparables o recorribles, sin número: (título, [(rótulo, texto)])"""
    out = ''.join(f'<details class="promise"><summary><span class="promise__t">{esc(t)}</span>{MAS}</summary>'
                  f'<div class="promise__body"><dl>' + ''.join(f'<div><dt class="promise__k">{esc(r)}</dt><dd>{x}</dd></div>' for r, x in filas) + '</dl></div></details>'
                  for t, filas in items)
    return f'{I}<div class="promises">{out}</div>'
def c(t): return f'<code>{esc(t)}</code>'
def cap(href, t): return f'<a class="xref" href="{href}">{esc(t)}</a>'


def ancla(capn, k):
    return 's-' + capn.replace('.', '-') + f'-{k:02d}'


VER = ('breve', 'tecnica', 'grupo', 'referencia')


def _verif_html(ver, verif, ref):
    """La verificación según su función (Guía 05 · Composición normativa): cada prueba es (rótulo, condición, resultado esperado)."""
    if ver == 'grupo':
        return ''
    if ver == 'referencia':
        return f'{I}<p class="ed__more"><span class="ed__more-k">Verificación</span>{ref}</p>'
    if ver == 'breve':
        return (f'{I}<div class="ed__more"><span class="ed__more-k">Verificación</span>'
                + ''.join(f'<p>{cnd} Resultado esperado: {res}</p>' for _, cnd, res in verif) + '</div>')
    return detalle([('Verificación', [(r, f'{cnd} Resultado esperado: {res}') for r, cnd, res in verif])])


def _relaciones(rel, texto):
    """Dependencias de una norma: las de rel=[…] y las que el texto enlaza (R, M y L). Formas: KYN-SDI-…, KYN-MRK-… y SD-NN
    (un capítulo del Sistema de Diseño). La fuente es el módulo; el registro las recibe al generar."""
    s = set(rel) | set(re.findall(r'⟦R:([A-Z0-9-]+)\|', texto)) | set(re.findall(r'title="(KYN-MRK-[A-Z]+-\d+)"', texto))
    for slug in re.findall(r'href="\.\./[a-z-]+/([a-z0-9-]+)\.html"', texto):
        if slug in _SLUG:
            s.add('SD-' + _SLUG[slug][0])
    return sorted(s)


def relacion_valida(r):
    return r in CONSTRUIDAS or (r.startswith('KYN-MRK-') and r in _MRK) or (r.startswith('SD-') and r[3:] in CAPS)


def norma(nid, nombre, capitulo, slug_mod, slug_cap, k, titular, entrada, partes, origen=(), responsabilidad='', cita='', corto=None,
          verif=(), ver='breve', ref='', rel=()):
    """Una norma emitida en borrador. Registra su ruta, su titular y su verificación para data/sd-normas.json.
    verif: [(rótulo, condición, resultado esperado)]; ver: breve, tecnica, grupo o referencia (ref: el texto que remite).
    rel: dependencias normativas que no llevan enlace en la página (Guía 05 · Referencias). El registro las recibe junto con
    las referencias R() del texto: aquí está la fuente; data/sd-normas.json («relaciones») se genera y no se edita."""
    if ver not in VER:
        raise SystemExit(f'{nid}: presentación de la verificación desconocida «{ver}»')
    if not verif or any(len(v) != 3 or not v[1] or not v[2] for v in verif):
        raise SystemExit(f'{nid}: cada norma lleva su verificación con condición y resultado esperado')
    if ver == 'referencia' and not ref:
        raise SystemExit(f'{nid}: la verificación por referencia necesita el texto que remite')
    an = ancla(capitulo, k)
    previo = NORMAS.get(nid)
    if previo and previo.get('ruta') and not previo['ruta'].startswith(f'sistema-diseno/{slug_mod}/{slug_cap}.html#'):
        raise SystemExit(f'{nid} ya está emitido en otro capítulo')
    if nid in CONSTRUIDAS:
        raise SystemExit(f'{nid} se usa dos veces')
    CONSTRUIDAS[nid] = dict(id=nid, nombre=nombre, corto=corto or CORTOS.get(nid, nombre), slug=slug_cap, ruta=f'sistema-diseno/{slug_mod}/{slug_cap}.html#{an}', origen=list(origen),
                            responsabilidad=responsabilidad, cita=cita, titular=titular, ancla=an,
                            verificacion=[dict(rotulo=r, condicion=plano(cnd), resultado=plano(res)) for r, cnd, res in verif], presentacion=ver,
                            _verif=list(verif),
                            relaciones=_relaciones(rel, ''.join(partes) + ref))
    partes = list(partes) + ([_verif_html(ver, verif, ref)] if ver != 'grupo' else [])
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


def numeradas(items, cols=3):
    """Retícula con número (R26: secuencia o enumeración útil), como CMP-004: (título, párrafos)"""
    m = {2: ' pgrid--2', 3: '', 4: ' pgrid--4'}[cols]
    return (f'{I}<div class="pgrid{m}">' + ''.join(
        f'<div><span class="pgrid__n">{k:02d}</span><p class="pgrid__t">{esc(t)}</p>{P(*ps, cls="pgrid__d")}</div>' for k, (t, ps) in enumerate(items, 1)) + '</div>')


_MRK = {v['id']: (k, v['t']) for k, v in json.load(io.open(os.path.join(ROOT, 'data', 'normas.json'), encoding='utf-8')).items()}


def M(nid, texto=None):
    """Enlace a una norma del Libro de Marca desde una página de capítulo del Sistema de Diseño (se cita, no se copia)"""
    ruta, t = _MRK[nid]
    return f'<a class="xref" href="../../{ruta}" title="{nid}">{esc(texto or t)}</a>'


def plano(t):
    """Texto sin etiquetas ni marcas de referencia, para el registro"""
    t = re.sub(r'⟦R:([A-Z0-9-]+)\|([^⟧]*)⟧', lambda m: m.group(2) or (CONSTRUIDAS.get(m.group(1), {}).get('nombre') or m.group(1)), t)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', t))).strip()


def R(nid, texto=''):
    """Referencia directa a otra norma del Sistema de Diseño. tools/sd_capitulos.py la resuelve cuando todas las normas
    están escritas: enlace a su ancla, con su nombre y, si está en otro capítulo, el capítulo. Una norma sin destino detiene
    la generación: la oración se redacta sin la referencia (Guía 05 · Composición normativa)."""
    return f'⟦R:{nid}|{texto}⟧'


_SLUG = {s: (num, mod, st) for num, (mod, s, st) in CAPS.items()}


def resolver(t, slug_actual):
    def un(m):
        nid, texto = m.group(1), m.group(2)
        b = CONSTRUIDAS.get(nid)
        if not b:
            raise SystemExit(f'Referencia sin destino: {nid} (en {slug_actual})')
        num, mod, st = _SLUG[b['slug']]
        if b['slug'] == slug_actual:
            return f'<a class="xref" href="#{b["ancla"]}">{esc(texto or b["nombre"])}</a>'
        return (f'<a class="xref" href="../{mod}/{b["slug"]}.html#{b["ancla"]}">{esc(texto or b["nombre"])}</a>'
                + ('' if texto else f', en {num} {esc(st)}'))
    return re.sub(r'⟦R:([A-Z0-9-]+)\|([^⟧]*)⟧', un, t)


def may(t):
    """Una celda con una oración independiente empieza con mayúscula (Guía 05 · Celdas y resultados). El código, las cifras
    y los nombres que ya empiezan con mayúscula quedan como están."""
    return t[:1].upper() + t[1:] if t[:1].islower() else t


def validacion(capn, slug_cap, entrada):
    """Validación del capítulo: la verificación del capítulo y las pruebas que conviene consultar juntas (ver='grupo').
    Tabla solo cuando reúne tres pruebas o más; si no, filas. El rótulo de cada fila nombra la norma sin enlace
    (Guía 05 · Referencias): la norma está en la misma página y el menú lleva a ella; con dos pruebas, se suma su rótulo."""
    VALIDADOS.add(slug_cap)
    pr = [(b, v) for b in CONSTRUIDAS.values() if b['slug'] == slug_cap and b['presentacion'] == 'grupo' for v in b['_verif']]
    cuenta = {}
    for b, _ in pr:
        cuenta[b['id']] = cuenta.get(b['id'], 0) + 1
    def rot(b, r): return b['corto'] + (f' · {r}' if cuenta[b['id']] > 1 else '')
    partes = []
    if len(pr) >= 3:
        partes.append(matriz('Pruebas del capítulo', [('Qué se comprueba', 'Condición'), ('Qué se espera', 'Resultado')],
                             [(rot(b, r), [cnd, may(res)]) for b, (r, cnd, res) in pr]))
    elif pr:
        partes.append(f'{I}<div class="ed__stack">' + ''.join(
            f'<div><span class="paren">({esc(rot(b, r))})</span><p>{cnd} Resultado esperado: {res}</p></div>' for b, (r, cnd, res) in pr) + '</div>')
    return seccion('validacion', _SLUG[slug_cap][0], 'Validación', 'Validación del capítulo', entrada, partes)
