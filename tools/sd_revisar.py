"""Control editorial del Sistema de Diseño (solo lectura; nunca reescribe texto).

Uso:  python tools/sd_revisar.py          (después de generar el libro)

Criterio: Guía 05, «Composición normativa según el contenido». Separa dos niveles:
- ERROR: problemas comprobables. La entrega exige cero.
- REVISAR: posibles problemas editoriales para revisión humana, uno por uno. Ningún comienzo de titular está prohibido:
  el aviso pregunta si el titular identifica la responsabilidad de la norma. Un aviso se conserva con su motivo en
  tools/sd/revision-justificada.json ({"tipo:clave": {"motivo": "...", "fecha": "AAAA-MM-DD"}}).
"""
import difflib
import html
import io
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = json.load(io.open(os.path.join(ROOT, 'data', 'sd-normas.json'), encoding='utf-8'))
JUST_P = os.path.join(ROOT, 'tools', 'sd', 'revision-justificada.json')
JUST = json.load(io.open(JUST_P, encoding='utf-8')) if os.path.exists(JUST_P) else {}
COD = r'(?<![A-Z]-)(?<!KYN-SDI-)\b(?:PEX|ARQ|FUI|CPE|PAT|ACC|CNT|DAV|IAE|SPR|MOV|GOB)-\d{3}\b'

err, rev = [], []


def plano(t):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t))).replace('⁠', '').strip()


def sim(a, b):
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()


def aviso(tipo, clave, texto):
    k = f'{tipo}:{clave}'
    if k in JUST:
        return
    rev.append(f'REVISAR {tipo:<12} {clave}: {texto}')


# Páginas generadas: secciones por ancla
paginas = {}
for n in REG['normas']:
    if n['estado'] == 'reservado' or not n.get('ruta'):
        continue
    pg = n['ruta'].split('#')[0]
    if pg not in paginas:
        t = io.open(os.path.join(ROOT, pg), encoding='utf-8').read()
        paginas[pg] = (t, dict(re.findall(r'<section class="ed" id="([^"]+)">(.*?)</section>', t, re.S)))

normas = [n for n in REG['normas'] if n['estado'] != 'reservado']
reqs = {}   # id → [requisitos en texto plano]
pres = defaultdict(list)   # página → presentaciones de verificación
for n in normas:
    nid = n['id']
    pg, an = n['ruta'].split('#')
    t, secs = paginas[pg]
    sec = secs.get(an)
    if sec is None:
        err.append(f'ERROR   ancla        {nid}: falta la sección #{an} en {pg}')
        continue
    h2 = re.search(r'<h2 class="ed__title">(.*?)</h2>', sec, re.S)
    if not h2 or plano(h2.group(1)) != n.get('titular'):
        err.append(f'ERROR   registro     {nid}: el titular de la página no coincide con data/sd-normas.json')
    v = n.get('verificacion') or []
    if not v or any(not x.get('condicion') or not x.get('resultado') for x in v):
        err.append(f'ERROR   verificación {nid}: sin condición y resultado esperado')
    p = n.get('presentacion_verificacion')
    pres[pg].append(p)
    det_ver = re.search(r'<details class="det"><summary>Verificación', sec)
    if det_ver and p != 'tecnica':
        err.append(f'ERROR   verificación {nid}: plegable «Verificación» en una norma «{p}»')
    if p in ('breve', 'tecnica'):
        for x in v:
            if plano(x['condicion'])[:40] not in plano(sec):
                err.append(f'ERROR   registro     {nid}: la verificación del registro no está en la página')
    if p == 'grupo':
        val = secs.get('validacion', '')
        for x in v:
            if plano(x['condicion'])[:40] not in plano(val):
                err.append(f'ERROR   registro     {nid}: la prueba agrupada no está en «Validación del capítulo»')
    # Requisitos (párrafos con nivel) y repeticiones dentro de la norma
    rq = [plano(x) for x in re.findall(r'<p[^>]*>((?:(?!</p>).)*?nvl--fin(?:(?!</p>).)*)</p>', sec, re.S)]
    reqs[nid] = rq
    otros = [plano(x) for x in re.findall(r'<(?:p|dd|span class="matrix__v"[^>]*)[^>]*>((?:(?!</p>|</dd>|</span>).)*)', sec, re.S)]
    for r in rq:
        for o in otros:
            if o and o != r and len(o) > 30:
                s = sim(r, o)
                if s >= 0.9:
                    err.append(f'ERROR   repetición   {nid}: un requisito se repite en otra fila: «{o[:70]}…»')
                elif s >= 0.7:
                    aviso('repetición', nid, f'una fila se parece a un requisito ({s:.2f}): «{o[:70]}…»')
    for x in v:
        for r in rq:
            s = sim(x['condicion'] + ' ' + x['resultado'], r)
            if s >= 0.6:
                aviso('verificación', nid, f'la verificación se parece al requisito ({s:.2f})')
    # Referencias
    if '⟦R:' in sec:
        err.append(f'ERROR   referencia   {nid}: referencia sin resolver')
    visible = plano(re.sub(r'<span class="ed__code"[^>]*>.*?</span>', '', sec))
    for m in re.findall(COD, visible):
        err.append(f'ERROR   referencia   {nid}: código suelto sin enlace «{m}»')
    # Titulares para revisión humana
    tit = n.get('titular', '')
    if re.search(r'\b(se|es|son|dice|tiene|sabe|puede|deja|sigue|llega|muestra|encuentra)\b', tit, re.I):
        aviso('titular', nid, f'«{tit}» tiene forma de frase: ¿identifica la responsabilidad de la norma?')
    if 'Casos límite' in sec:
        aviso('casos límite', nid, 'confirmar que son situaciones excepcionales, no habituales')

# Requisitos idénticos o parecidos entre normas
todos = [(nid, r) for nid, rs in reqs.items() for r in rs]
for i, (a, ra) in enumerate(todos):
    for b, rb in todos[i + 1:]:
        if a == b:
            continue
        if ra == rb:
            err.append(f'ERROR   duplicación  {a} y {b}: el mismo requisito palabra por palabra')
        elif sim(ra, rb) >= 0.75:
            aviso('duplicación', f'{a}+{b}', f'requisitos parecidos ({sim(ra, rb):.2f})')

# Una sola forma de verificación en un capítulo de tres normas o más
for pg, ps in pres.items():
    if len(ps) >= 3 and len(set(ps)) == 1:
        aviso('composición', pg.split('/')[-1], f'las {len(ps)} normas usan la misma verificación «{ps[0]}»: ¿es consistencia justificada?')

# Guía 05 · Celdas y resultados: una oración independiente en una celda empieza con mayúscula (salvo código o cifras)
for pg, (t, secs) in paginas.items():
    for celda in re.findall(r'<span class="matrix__v" role="cell">(.*?)</span>(?=<span class="matrix__v"|</div>)', t, re.S):
        p = plano(celda)
        if p[:1].islower() and p.endswith('.') and not celda.lstrip().startswith('<code'):
            err.append(f'ERROR   celda        {pg.split("/")[-1]}: oración en minúscula «{p[:60]}…»')
    # Guía 05 · Referencias: el rótulo de una prueba del capítulo nombra la norma sin enlace
    val = secs.get('validacion', '')
    if re.search(r'<span class="matrix__k" role="rowheader"><a ', val):
        err.append(f'ERROR   validación   {pg.split("/")[-1]}: el rótulo de una prueba lleva enlace')

ids = {n['id'] for n in REG['normas']}
for n in normas:
    # Relaciones del registro con destino
    for r in n.get('relaciones', []):
        if r not in ids:
            err.append(f'ERROR   relación     {n["id"]}: la relación {r} no tiene destino')
    # Resultados que describen un juicio en lugar de un hecho observable (revisión humana)
    for v in n.get('verificacion', []):
        if re.search(r'\b(correctamente|adecuad\w*|apropiad\w*|claramente|bien|se entiende|es claro|es fácil)\b', v['resultado'], re.I):
            aviso('resultado', f'{n["id"]}:{v["rotulo"]}', f'¿describe un hecho observable? «{v["resultado"]}»')
    # Densidad de enlaces visibles (revisión humana, sin máximo fijo)
    pg, an = n['ruta'].split('#')
    k = paginas[pg][1].get(an, '').count('class="xref"')
    if k >= 4:
        aviso('enlaces', n['id'], f'{k} enlaces visibles: ¿cada uno conduce a una especificación necesaria?')

# Códigos conservados respecto del último commit
try:
    prev = json.loads(subprocess.run(['git', 'show', 'HEAD:data/sd-normas.json'], cwd=ROOT, capture_output=True, encoding='utf-8').stdout)
    ahora = {n['id'] for n in REG['normas']}
    for n in prev['normas']:
        if n['id'] not in ahora:
            err.append(f'ERROR   código       {n["id"]}: estaba en el último commit y falta')
        elif n.get('ruta') and n['ruta'].split('#')[1] != next(x for x in REG['normas'] if x['id'] == n['id'])['ruta'].split('#')[1]:
            err.append(f'ERROR   ancla        {n["id"]}: cambió su ancla')
except Exception as e:   # sin git: se omite
    print('Sin comparación con el último commit:', e)

for x in err:
    print(x)
for x in rev:
    print(x)
print(f'\n{len(normas)} normas · {len(err)} errores · {len(rev)} para revisión humana · {len(JUST)} avisos justificados')
sys.exit(1 if err else 0)
