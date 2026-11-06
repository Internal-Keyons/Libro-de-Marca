"""Gobierno normativo de la Biblioteca Keyons.

Lee la fuente común (data/gobierno.json), el registro de normas (data/normas.json) y el texto aprobado de cada
sección (data/referencia-contenido.json) y genera, desde esa misma fuente:

- data/autoridad.json            dimensiones de cada norma: estado, versión, ámbito, aprobación, excepciones, relacionadas.
                                  Conserva los valores ya aprobados; solo completa los que faltan.
- data/clasificacion-propuesta.json  inventario y clasificación propuesta de cada requisito (DEBE, NO DEBE, DEBERÍA, PUEDE).
                                  No modifica ningún texto. Queda pendiente de aprobación humana.
- docs/CLASIFICACION_NORMATIVA.md    reporte de la clasificación, ambigüedades, duplicaciones y contradicciones.
- js/autoridad.js                 estado y versión para la web (rótulo discreto de cada norma).
- guia/index.html                Guía de la Biblioteca: cómo leer las normas, rutas, referencias y aprobaciones.
- recursos/gobierno.html         redirección de compatibilidad hacia la Guía.
- ia/gobierno.json                la misma información para agentes de IA.

Uso:  python tools/gobierno.py
"""
import io, json, os, re, html
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda p: json.load(io.open(os.path.join(ROOT, p), encoding='utf-8'))
def W(p, s):
    p = os.path.join(ROOT, p); os.makedirs(os.path.dirname(p), exist_ok=True)
    io.open(p, 'w', encoding='utf-8', newline='\n').write(s)

G = J('data/gobierno.json')
REG = J('data/normas.json')
REG = REG.get('normas', REG)
TXT = J('data/referencia-contenido.json')['secciones']
AUT_P = 'data/autoridad.json'
AUT = J(AUT_P)['normas'] if os.path.exists(os.path.join(ROOT, AUT_P)) else {}

COMUN = {'vigente': 'vigente', 'borrador': 'en-revision', 'pendiente': 'en-revision', 'revision': 'en-revision',
         'estructura': 'en-revision', 'descontinuada': 'descontinuada', 'integrada': 'descontinuada'}
ETQ = {'vigente': 'Vigente', 'en-revision': 'En revisión', 'descontinuada': 'Descontinuada'}

# ── Ámbito propuesto según el área de la norma ──
IDENT = ['identidad', 'web', 'internas', 'saas']
AMB = {'ADN': IDENT + ['servicios'], 'CON': IDENT, 'DIS': IDENT + ['servicios'], 'VOZ': IDENT + ['servicios'],
       'LOG': IDENT, 'COL': IDENT, 'TYP': IDENT, 'ESP': IDENT, 'ILU': IDENT, 'ICO': IDENT, 'ICN': IDENT, 'DAT': IDENT,
       'CMP': IDENT, 'GAL': ['identidad', 'web'], 'TEX': ['identidad', 'web'], 'PLA': ['identidad', 'web'], 'REF': ['identidad', 'web'],
       'PRE': ['identidad', 'servicios'], 'PER': ['saas', 'personalizados', 'cliente'],
       'VIS': IDENT}
CALIDAD = {'KYN-MRK-VIS-007', 'KYN-MRK-VIS-008', 'KYN-MRK-VIS-011'}   # calidad y experiencia: aplican también a productos de clientes

# ── Clasificación de requisitos por expresión ──
R = [
    ('NO DEBE', r'\b(no (se )?deben?|nunca|no se (utiliza|utilizan|usa|usan|permite|admite|aplica|introduce|introducen|suman|publica)|no utilizar|no aplicar|no introducir|no convertir|prohibid[oa]s?|evitar)\b'),
    ('DEBERÍA', r'\b(debería|deberían|se recomienda|conviene|preferente(mente)?|se prefiere[n]?|preferimos|idealmente|recomendad[oa]s?)\b'),
    ('DEBE', r'\b(debe|deben|siempre|obligatori[oa]|se exige|requiere[n]?|deberá[n]?)\b'),
    ('PUEDE', r'\b(puede|pueden|podrá[n]?|se permite[n]?|opcional(mente)?)\b'),
]
IMPERATIVO = r'^(Utilizar|Aplicar|Comprobar|Mantener|Conservar|Seleccionar|Ajustar|Verificar|Incorporar|Evaluar|Adoptar|Citar|Incluir)\b'

def frases(t):
    t = re.sub(r'\s+', ' ', t)
    return [f.strip() for f in re.split(r'(?<=[.;:!?])\s+(?=[A-ZÁÉÍÓÚÑ¿«(])', t) if len(f.strip()) > 18]

def clasificar(f):
    lv = [k for k, rx in R if re.search(rx, f, re.I)]
    imp = re.match(IMPERATIVO, f)
    if 'NO DEBE' in lv and 'DEBE' in lv:
        lv.remove('DEBE')
    if not lv and imp:
        return 'DEBE', ['imperativo en infinitivo: se interpreta como DEBE']
    if not lv:
        return None, []
    amb = ['varias expresiones normativas en la misma frase'] if len(lv) > 1 else []
    if lv[0] == 'DEBE' and re.search(r'\bsiempre\b', f, re.I) and not re.search(r'\bdeben?\b', f, re.I):
        amb.append('«siempre» sin verbo normativo')
    return lv[0], amb

inv, ambig, sent_idx = [], [], defaultdict(list)
for h, v in sorted(REG.items(), key=lambda x: x[1]['id']):
    nid = v['id']
    sec = TXT.get(h, {})
    texto = sec.get('texto', '')
    reqs = []
    for i, f in enumerate(frases(texto), 1):
        nivel, notas = clasificar(f)
        norm = re.sub(r'[^a-záéíóúñ ]', '', f.lower())
        if len(norm) > 50:
            sent_idx[norm].append(nid)
        if not nivel:
            continue
        rid = f'{nid}.{len(reqs) + 1}'
        reqs.append({'ref': rid, 'nivel': nivel, 'texto': f, **({'revisar': notas} if notas else {})})
        if notas:
            ambig.append((rid, nivel, notas, f))
    area = nid.split('-')[2]
    ambito = sorted(set(AMB.get(area, IDENT) + (['personalizados', 'cliente'] if nid in CALIDAD else [])), key=[a['k'] for a in G['ambitos']].index)
    inv.append({'id': nid, 'titulo': v['t'], 'estado': v['estado'], 'fuente': h, 'ambito_propuesto': ambito, 'requisitos': reqs})

dups = {k: sorted(set(v)) for k, v in sent_idx.items() if len(set(v)) > 1}
CONTRA = [
    ('KYN-MRK-TYP-004', 'El kicker se especifica en TASA Orbiter 500, 14 px, +8 %; el código lo aplica en Plus Jakarta Sans 700, 12 a 13 px, +2 %.'),
    ('KYN-MRK-TYP-002', 'El estándar de tracking (8.8) fija 0em para títulos en Plus Jakarta Sans; los títulos de sección del libro usan −3 %.'),
    ('KYN-MRK-TYP-002', 'El estándar fija −3 % de 52 a 79 px y −5 % desde 80 px para TASA Orbiter; el display del libro usa −4 %.'),
    ('KYN-MRK-ILU-003', 'Divisor de 1 px en Gris Bruma y divisor fuerte en Azul Noche al 16 %; el libro usa Azul Cielo 100 y 200, y barras de 4 px en tablas.'),
    ('KYN-MRK-ILU-007', 'El texto fija Azul Cielo y trazos uniformes para las tramas; desde la ronda 15 se muestran en Azul Noche con trazo a mano.'),
    ('KYN-MRK-ICO-005', 'Los íconos de la marca salen del catálogo; las flechas de navegación del libro son íconos de 1,6 px fuera del catálogo.'),
    ('KYN-MRK-ESP-004', 'La retícula fija contenido hasta 1520 px; el libro usa un documento de 1600 px.'),
]

# ── Dimensiones por norma: se conservan los valores aprobados ──
out = {}
for n in inv:
    prev = AUT.get(n['id'], {})
    est = n['estado']
    out[n['id']] = {
        'titulo': n['titulo'],
        'estado': COMUN.get(est, 'en-revision'), 'estado_documental': est,
        'version': prev.get('version') or ('1.0' if est == 'vigente' else '0.1'),
        'ambito': prev.get('ambito', []),
        'responsable': prev.get('responsable'), 'fecha_aprobacion': prev.get('fecha_aprobacion'),
        'excepciones': prev.get('excepciones', []),
        'relacionadas': sorted(set(re.findall(r'KYN-[A-Z]{3}-[A-Z]{3}-\d{3}', TXT.get(n['fuente'], {}).get('texto', ''))) - {n['id']}),
    }
W(AUT_P, json.dumps({'nota': 'Generado por tools/gobierno.py. Ámbito, responsable, fecha y excepciones se completan solo con valores aprobados.', 'normas': out}, ensure_ascii=False, indent=1) + '\n')

cnt = Counter(r['nivel'] for n in inv for r in n['requisitos'])
W('data/clasificacion-propuesta.json', json.dumps({
    'estado': 'Propuesta pendiente de aprobación humana', 'regla': G['regla_ia'],
    'resumen': {'normas': len(inv), 'requisitos': sum(cnt.values()), 'por_nivel': cnt, 'ambiguedades': len(ambig), 'duplicaciones': len(dups)},
    'normas': inv, 'duplicaciones': [{'texto_normalizado': k, 'normas': v} for k, v in dups.items()],
    'contradicciones': [{'norma': a, 'detalle': b} for a, b in CONTRA]}, ensure_ascii=False, indent=1) + '\n')

# ── Reporte ──
L = ['# Clasificación normativa propuesta', '',
     f'**Estado:** propuesta pendiente de aprobación humana. {G["regla_ia"]}', '',
     '**Método:** se recorrió el texto aprobado de cada norma (data/referencia-contenido.json) y se clasificó cada frase según sus expresiones normativas. No se modificó ningún texto. Cada requisito recibe una referencia interna (por ejemplo, `KYN-MRK-COL-004.2`) que conserva el ID principal.', '',
     '## Resumen', '', '| Dato | Valor |', '|---|---|',
     f'| Normas inventariadas | {len(inv)} |', f'| Requisitos detectados | {sum(cnt.values())} |'] + \
    [f'| {k} | {cnt.get(k, 0)} |' for k in ['DEBE', 'NO DEBE', 'DEBERÍA', 'PUEDE']] + \
    [f'| Requisitos con ambigüedad | {len(ambig)} |', f'| Frases duplicadas entre normas | {len(dups)} |', f'| Contradicciones con el código | {len(CONTRA)} |', '',
     '## Ámbitos propuestos', '', 'Se asignaron por área de la norma. Ninguno está aprobado; `data/autoridad.json` los registra vacíos hasta su aprobación.', '',
     '| Área | Ámbitos propuestos |', '|---|---|'] + \
    [f'| {a} | {", ".join(next(x["t"] for x in G["ambitos"] if x["k"] == k) for k in v)} |' for a, v in sorted(AMB.items())] + \
    ['', 'Las normas de calidad y experiencia ' + ', '.join(sorted(CALIDAD)) + ' suman Productos personalizados y Productos con identidad del cliente.', '',
     '## Contradicciones entre normas y código', '', '| Norma | Detalle |', '|---|---|'] + [f'| {a} | {b} |' for a, b in CONTRA] + \
    ['', '## Ambigüedades por revisar', '', '| Referencia | Nivel propuesto | Motivo | Frase |', '|---|---|---|---|'] + \
    [f'| {r} | {lv} | {"; ".join(n)} | {f[:160]}{"…" if len(f) > 160 else ""} |' for r, lv, n, f in ambig] + \
    ['', '## Frases repetidas en varias normas', ''] + ([f'- {", ".join(v)}: «{k[:120]}…»' for k, v in dups.items()] or ['Ninguna.']) + \
    ['', '## Requisitos por norma', '', '| Norma | DEBE | NO DEBE | DEBERÍA | PUEDE |', '|---|---|---|---|---|'] + \
    [f'| {n["id"]} | ' + ' | '.join(str(sum(1 for r in n['requisitos'] if r['nivel'] == k)) for k in ['DEBE', 'NO DEBE', 'DEBERÍA', 'PUEDE']) + ' |' for n in inv] + ['']
W('docs/CLASIFICACION_NORMATIVA.md', '\n'.join(L))

# ── Web: estado y versión, discretos, desde la misma fuente ──
W('js/autoridad.js', '/* Generado por tools/gobierno.py desde data/autoridad.json. No se edita a mano. */\nwindow.KEYONS_AUT = '
  + json.dumps({k: [ETQ[v['estado']], v['version']] for k, v in out.items()}, ensure_ascii=False) + ';\n')

# ── IA ──
W('ia/gobierno.json', json.dumps({'gobierno': G, 'normas': out,
                                  'clasificacion_propuesta': {'estado': 'Pendiente de aprobación humana', 'archivo': '/data/clasificacion-propuesta.json'}},
                                 ensure_ascii=False, indent=1) + '\n')

# ── Página: recursos/gobierno.html ──
e = html.escape
def stack(rows, v=False):
    return f'        <div class="ed__stack{" ed__stack--v" if v else ""}">\n' + ''.join(f'          <div><span class="paren">({e(k)})</span><p>{d}</p></div>\n' for k, d in rows) + '        </div>\n'
def sec(sid, num, lab, title, body):
    return f'''    <section class="ed" id="{sid}">
      <div class="ed__label"><span>{num}</span><span>{lab}</span></div>
      <div>
        <h2 class="ed__title">{title}</h2>
{body}      </div>
    </section>

'''
def lis(xs, v=False):
    # Viñetas solo para elementos breves (ESP-005): si alguno pasa de dos líneas, la lista se presenta en filas
    if max(len(x) for x in xs) > 160:
        return '        <ul class="gov__rows">' + ''.join(f'<li>{e(x)}</li>' for x in xs) + '</ul>\n'
    return f'        <ul class="gov__list{" gov__list--v" if v else ""}">' + ''.join(f'<li>{e(x)}</li>' for x in xs) + '</ul>\n'
def link(t, h):
    return f'<a class="xref" href="../{h}">{e(t)}</a>'

S = ''
S += sec('normas', '01', 'Cómo leer las normas', 'Autoridad, vigencia y ámbito',
         '        <p class="ed__lead">Las normas de los seis libros distinguen <strong>requisitos, recomendaciones y opciones</strong> con los mismos términos.</p>\n'
         + '        <dl class="gov__lv">' + ''.join(f'<div><dt>{e(n["k"])}</dt><dd>{e(n["d"])}</dd></div>' for n in G['niveles']) + '</dl>\n'
         + lis(G['niveles_uso'])
         + '        <h3 class="ed__sub">Vigencia</h3>\n' + stack([(x['t'], e(x['d'])) for x in G['estados']], v=True)
         + '        <h3 class="ed__sub">Estados del proceso que se conservan</h3>\n'
         + stack([(x['t'], e(x['d']) + f' Equivale a {e(x["equivale"])}.') for x in G['estados_adicionales']], v=True)
         + f'        <p class="ed__more">{e(G["regla_ia"])}</p>\n'
         + '        <h3 class="ed__sub">Ámbitos de aplicación</h3>\n'
         + '        <ul class="gov__amb">' + ''.join(f'<li>{e(a["t"])}</li>' for a in G['ambitos']) + '</ul>\n' + lis(G['ambitos_criterio'])
         + '        <h3 class="ed__sub">Dimensiones de cada norma</h3>\n' + lis(G['dimensiones']))
ROUTES = ''
for r in G['rutas']:
    steps = ''.join(f'<li><span class="gov__route-i">{i:02d}</span>{link(t, h)}</li>' for i, (t, h) in enumerate(r['pasos'], 1))
    notes = ''.join(f'<p class="gov__route-n">{e(x)}</p>' for x in r.get('reglas', []))
    ROUTES += (f'        <div class="gov__route"><div class="gov__route-h"><span class="gov__route-k">{r["k"]}</span><h3 class="gov__route-t">{e(r["t"])}</h3><p class="gov__route-p">{e(r["para"])}</p></div>\n'
               f'          <ol class="gov__route-s">{steps}</ol>{notes}</div>\n')
S += sec('rutas', '02', 'Rutas de lectura', 'Cinco rutas, según quién consulta',
         '        <p class="ed__lead">Cada ruta tiene <strong>un propósito, un orden de consulta</strong> y enlaces directos al contenido que existe hoy.</p>\n'
         + ROUTES + lis(G['rutas_criterio']))
S += sec('referencias', '03', 'Referencias y versiones', 'Un ID permanente para citar',
         f'        <p class="ed__lead">Formato común: <strong>{e(G["identificadores"]["formato"])}</strong>.</p>\n'
         + lis(G['identificadores']['reglas'])
         + '        <div class="matrix" role="table" aria-label="Prefijos por libro"><div class="matrix__row matrix__head" role="row"><span class="matrix__k" role="columnheader">(Prefijo)</span><span class="matrix__lvl" role="columnheader">Libro</span><span class="matrix__lvl" role="columnheader">Estado</span></div>'
         + ''.join(f'<div class="matrix__row" role="row"><span class="matrix__k" role="rowheader">{e(p["k"])}</span><span class="matrix__v" role="cell">{e(p["t"])}</span><span class="matrix__v" role="cell">{e(p["estado"])}</span></div>' for p in G['identificadores']['prefijos']) + '</div>\n'
         + '        <h3 class="ed__sub">Citación</h3>\n' + stack([(c['k'], e(c['d'])) for c in G['citacion']], v=True)
         + f'        <p class="ed__more">{e(G["citacion_nota"])}</p>\n'
         + '        <h3 class="ed__sub">Versionado y trazabilidad</h3>\n' + lis(G['versionado'], v=True))
S += sec('gobierno', '04', 'Gobierno y aprobaciones', 'Quién aprueba y cómo se exceptúa',
         f'        <p class="ed__lead">{e(G["autoridad"]["texto"])}</p>\n'
         + stack([('Estado actual', e(G['autoridad'].get('actual', G['autoridad']['estado']))), ('Propuesta', e(G['autoridad']['propuesta']))])
         + '        <h3 class="ed__sub">Procedimiento de excepción</h3>\n'
         + '        <ol class="gov__steps">' + ''.join(f'<li>{e(x)}</li>' for x in G['excepciones']['pasos']) + '</ol>\n'
         + f'        <p class="ed__more">{e(G["excepciones"]["nota"])}</p>\n'
         + '        <h3 class="ed__sub">Permisos de consulta</h3>\n'
         + f'        <div class="gov__perm"><div class="gov__perm-k"><span class="gov__perm-l">Estado</span><span class="gov__perm-v"><span class="dot dot--borrador"></span>{e(G["permisos"]["estado"])}</span></div><p class="gov__perm-t">{e(G["permisos"]["texto"])}</p></div>\n')

STATE = f'{e(G["estado"])} · versión {e(G["version"])}'
PAGE = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Guía de la Biblioteca · Keyons</title>
<meta name="description" content="Cómo leer las normas de la Biblioteca Keyons: autoridad, vigencia, ámbitos, rutas de lectura, referencias y aprobaciones.">
<link rel="icon" href="../assets/logos/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/libro.css">
</head>
<body class="is-guia" data-root=".." data-page="guia/index.html">
<!-- Generado por tools/gobierno.py desde data/gobierno.json. No se edita a mano.
     Guía y gobierno: recurso común de la Biblioteca, no un séptimo libro. -->

<header id="topbar"></header>

<div class="doc doc--solo">
  <main class="content chapter">
    <nav class="crumbs" aria-label="Ruta"><a href="../index.html">Biblioteca Keyons</a>
      <svg viewBox="0 0 16 16" aria-hidden="true"><path d="m6 3.5 4.5 4.5L6 12.5"/></svg><span>Guía de la Biblioteca</span></nav>

    <header class="guia__h">
      <span class="kicker">Biblioteca Keyons · Guía de Gobernanza</span>
      <h1 class="guia__t">Guía de la Biblioteca</h1>
      <p class="guia__l">Las convenciones comunes a los seis libros: cómo leer cada norma, por dónde empezar, cómo citarla y quién la aprueba.</p>
      <p class="gov__state"><span class="dot dot--borrador"></span>@STATE@</p>
    </header>

@S@  </main>
</div>

<script>window.KEYONS_BOOK = { id: 'biblioteca', home: 'guia/index.html', menuLabel: 'Guía de la Biblioteca' }; window.KEYONS_NAV = [];</script>
<script src="../js/libro.js"></script>
</body>
</html>
'''.replace('@STATE@', STATE).replace('@S@', S)
W('guia/index.html', PAGE)

# Compatibilidad: la ubicación anterior en Recursos lleva a la Guía, con su apartado
W('recursos/gobierno.html', '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Guía de la Biblioteca · Keyons</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="../guia/index.html">
<script>
  /* El gobierno normativo pasó a la Guía de la Biblioteca. Se conservan los enlaces anteriores. */
  var m = { autoridad: 'normas', vigencia: 'normas', ambitos: 'normas', rutas: 'rutas', citacion: 'referencias', aprobacion: 'gobierno' };
  var h = location.hash.slice(1);
  location.replace('../guia/index.html' + (m[h] ? '#' + m[h] : ''));
</script>
<meta http-equiv="refresh" content="0; url=../guia/index.html">
</head>
<body><p>El gobierno normativo está en la <a href="../guia/index.html">Guía de la Biblioteca</a>.</p></body>
</html>
''')
print(f'{len(inv)} normas · {sum(cnt.values())} requisitos ({dict(cnt)}) · {len(ambig)} ambigüedades · {len(dups)} duplicaciones · {len(CONTRA)} contradicciones')
