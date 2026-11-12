"""Registro de normas del Manual de Marca Keyons.

Uso:  python tools/normas.py

Lee las secciones de cada página (rótulo .ed__label: número y título), actualiza data/normas.json
y escribe js/secciones.js (KEYONS_SECS, KEYONS_CAPS y KEYONS_NORMAS) para el libro.

Reglas (recursos/referencia.html, 39.1):
- Un ID emitido nunca cambia, no se borra ni se reutiliza desde que se publique la versión 1. Este script jamás regenera el registro desde cero.
  (Ronda 20, antes de la versión 1: se borraron las nomenclaturas integradas y descontinuadas y cada familia se renumeró sin huecos.)
- Si una página cambia su numeración, el ID se conserva y solo se actualiza el número visible («n»).
- Una sección nueva recibe ID únicamente si está en NUEVAS: emitir un ID es una decisión, no un efecto del script.
- Si una sección registrada ya no existe, el script avisa y no la borra: se marca [DESCONTINUADA] a mano.
- TRASLADOS mueve una norma a otra página sin cambiar su ID; la ruta anterior queda como alias y redirige.
- INTEGRADAS marca una norma cuyo contenido ya vive en otra («integrada en»): conserva su ID y apunta a la norma que la contiene.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, 'data', 'normas.json')
OUT = os.path.join(ROOT, 'js', 'secciones.js')

# Normas nuevas aprobadas: ruta#ancla → (ID, título). Una vez emitidas, quedan en el registro para siempre.
NUEVAS = {
    # 03 · Principios de diseño (aprobados 2026-10-29)
    'marca/principios.html#criterio': ('KYN-MRK-DIS-001', 'Diseñar con identidad, construir con criterio'),
    'marca/principios.html#capas': ('KYN-MRK-DIS-002', 'Identidad, experiencia y sistema'),
    'marca/principios.html#calma': ('KYN-MRK-DIS-003', 'Calma estructural y expresión visual'),
    'marca/principios.html#contexto': ('KYN-MRK-DIS-004', 'Expresividad contextual'),
    'marca/principios.html#comprension': ('KYN-MRK-DIS-005', 'Comprensión antes que complejidad'),
    # 11 · Criterio visual y antipatrones (aprobadas conceptualmente 2026-10-29; antes «KYN-VIS-###» provisional)
    **{f'fundamentos/criterio/antipatrones.html#vis-{i:03d}': (f'KYN-MRK-VIS-{i:03d}', t) for i, t in enumerate([
        'Jerarquía visual repetitiva', 'Tarjetas innecesarias', 'Geometría genérica', 'Iconografía de relleno',
        'Saturación de microelementos', 'Simetría automática', 'Movimiento ornamental', 'Contraste insuficiente',
        'Lenguaje genérico', 'Maximalismo uniforme', 'Originalidad a costa de orientación', 'Composición no intercambiable'], 1) if i not in (7, 11)},
    # 10 · Composiciones (2026-10-30)
    'fundamentos/composicion/editorial.html#decidir': ('KYN-MRK-CMP-001', 'Decidir la composición'),
    'fundamentos/composicion/editorial.html#simetria': ('KYN-MRK-CMP-002', 'Orden y experimentación'),
    'fundamentos/composicion/editorial.html#reticulas': ('KYN-MRK-CMP-003', 'Retículas editoriales'),
    'fundamentos/composicion/editorial.html#ritmo': ('KYN-MRK-CMP-004', 'Ritmo visual'),
    # 08 · Tipografía y 12 · Elementos gráficos (2026-10-30)
    'fundamentos/tipografia/sistema.html#funcion': ('KYN-MRK-TYP-006', 'Uso por función'),
    'fundamentos/elementos/graficos.html#profundidad': ('KYN-MRK-ILU-009', 'Profundidad atmosférica'),
    # 29 · Recursos técnicos (2026-11-06)
    'recursos/tecnicos.html#tecnicos': ('KYN-MRK-TEC-001', 'Recursos técnicos'),
    # 05 · Estela (2026-11-11, en borrador): una norma por sección, desde capitulo-05-estela.md
    'marca/estela.html#quien': ('KYN-MRK-EST-001', 'Quién es Estela', 'borrador'),
    # 06 · Isotipo (2026-11-12, en borrador): favicon, Apple Touch Icon e íconos PWA
    'fundamentos/identidad/isotipo.html#aplicaciones': ('KYN-MRK-LOG-011', 'Aplicaciones digitales', 'borrador'),
    # 21 · Redes y campañas (2026-11-12, en borrador): archivo de campañas aprobadas
    'aplicaciones/campanas.html#archivo': ('KYN-MRK-RED-001', 'Archivo de campañas', 'borrador'),
}

# Traslados (2026-11, consolidación de Fundamentos): ruta anterior → ruta vigente
TRASLADOS = {
    'fundamentos/forma/espacio.html#reticula': 'fundamentos/composicion/editorial.html#reticula',
    'fundamentos/forma/espacio.html#densidad': 'fundamentos/composicion/editorial.html#densidad',
    'fundamentos/forma/espacio.html#diagramas': 'fundamentos/composicion/editorial.html#diagramas',
    'fundamentos/criterio/antipatrones.html#vis-001': 'fundamentos/composicion/editorial.html#vis-001',
    'fundamentos/criterio/antipatrones.html#vis-002': 'fundamentos/composicion/editorial.html#vis-002',
    'fundamentos/criterio/antipatrones.html#vis-003': 'fundamentos/forma/espacio.html#vis-003',
    'fundamentos/criterio/antipatrones.html#vis-004': 'fundamentos/iconografia/iconos.html#vis-004',
    'fundamentos/criterio/antipatrones.html#vis-005': 'fundamentos/composicion/editorial.html#vis-005',
    'fundamentos/criterio/antipatrones.html#vis-006': 'fundamentos/composicion/editorial.html#vis-006',
    'fundamentos/criterio/antipatrones.html#vis-008': 'fundamentos/color/paleta-base.html#vis-008',
    'fundamentos/criterio/antipatrones.html#vis-009': 'marca/vocabulario.html#vis-009',
    'fundamentos/criterio/antipatrones.html#vis-010': 'fundamentos/composicion/editorial.html#vis-010',
    'fundamentos/criterio/antipatrones.html#vis-012': 'fundamentos/composicion/editorial.html#vis-012',
}

# Normas cuyo contenido quedó integrado en otra: ID → ID de la norma que lo contiene
INTEGRADAS = {}
# Ancla real donde vive el contenido integrado
ANCLA_INTEGRADA = {}

# Cambios de título o estado de normas ya emitidas (el ID nunca cambia)
CAMBIOS = {
    'KYN-MRK-DIS-002': {'t': 'Identidad, experiencia y sistema: roles definidos'},
    'KYN-MRK-DIS-003': {'t': 'Diseño: calma y expresión'},
    'KYN-MRK-DIS-004': {'t': 'Intensidad según contexto'},
    'KYN-MRK-DIS-005': {'t': 'Claridad antes que complejidad'},
    # 2026-11 · consolidación de Fundamentos: títulos de materia
    'KYN-MRK-ESP-001': {'t': 'Lenguaje geométrico Keyons'},
    'KYN-MRK-ESP-002': {'t': 'Sistema de radios y curvaturas'},
    'KYN-MRK-ESP-003': {'t': 'Sistema de espaciado'},
    'KYN-MRK-CMP-001': {'t': 'Componer según el contenido'},
    'KYN-MRK-CMP-002': {'t': 'Simetría y asimetría'},
    'KYN-MRK-CMP-004': {'t': 'Ritmo y equilibrio visual'},
    'KYN-MRK-ESP-005': {'t': 'Jerarquía y densidad de información'},
    'KYN-MRK-TYP-001': {'t': 'Familias tipográficas'},
    'KYN-MRK-TYP-003': {'t': 'Probador tipográfico'},
    'KYN-MRK-TYP-004': {'t': 'Etiquetas de contexto'},
    'KYN-MRK-TYP-005': {'t': 'Criterios de aplicación'},
    'KYN-MRK-ILU-001': {'t': 'Viñetas y marcadores gráficos'},
    'KYN-MRK-ILU-002': {'t': 'Recursos de énfasis visual'},
    'KYN-MRK-ILU-003': {'t': 'Líneas, guías y medidas'},
    'KYN-MRK-ILU-004': {'t': 'Transparencia y superposición'},
    'KYN-MRK-ILU-009': {'t': 'Luz y profundidad'},
    'KYN-MRK-ILU-006': {'t': 'Ráfagas de color'},
    'KYN-MRK-ILU-007': {'t': 'Tramas y texturas'},
    'KYN-MRK-ILU-008': {'t': 'Fotografía e imágenes'},
}


def nav():
    js = "global.window={};require(process.argv[1]);console.log(JSON.stringify(window.KEYONS_NAV))"
    return json.loads(subprocess.check_output(['node', '-e', js, os.path.join(ROOT, 'js', 'nav-data.js')], encoding='utf-8'))


def num_key(n):
    return [int(x) for x in n.split('.')]


def main():
    areas = nav()
    caps, pages = {}, []
    for a in areas:
        for c in a['ch']:
            hrefs = [it['href'].split('#')[0] for it in c['items'] if it.get('href')]
            if hrefs:
                caps[str(int(c['n']))] = hrefs[0]
            pages += [h for h in hrefs if h not in pages]

    secs = {}   # ruta#ancla → (número, título del rótulo)
    for p in pages:
        s = open(os.path.join(ROOT, p), encoding='utf-8').read()
        for m in re.finditer(r'<section class="ed(?: [^"]*)?" id="([^"]+)">\s*<div class="ed__label"><span>([\d.]+)</span><span>([^<]+)</span>', s):
            secs[f'{p}#{m.group(1)}'] = (m.group(2), m.group(3))

    reg = json.load(open(REG, encoding='utf-8'))
    for old, new in TRASLADOS.items():
        if old in reg and new not in reg:
            v = reg.pop(old)
            v.setdefault('antes', [])
            if old not in v['antes']:
                v['antes'].append(old)
            reg[new] = v
    ids = {v['id'] for v in reg.values()}
    byid = {v['id']: v for v in reg.values()}
    for h, v in reg.items():
        cam = CAMBIOS.get(v['id'], {})
        v.update(cam)
        if v['id'] in INTEGRADAS:
            v['estado'] = 'integrada'
            v['en'] = INTEGRADAS[v['id']]
        if h in secs:
            v['n'] = secs[h][0]
        elif v['estado'] == 'integrada':
            v['n'] = byid[v['en']]['n']
        elif v['estado'] != 'descontinuada':
            print('AVISO: la norma', v['id'], 'ya no tiene sección en', h, '(no se borra)')
    movidas = {old for v in reg.values() for old in v.get('antes', [])}
    for h, (nid, t, *est) in NUEVAS.items():
        if h in reg or h in movidas:
            continue
        if nid in ids:
            sys.exit(f'{nid} ya existe en el registro: un ID nunca se reutiliza')
        if h not in secs:
            sys.exit(f'{nid}: no existe la sección {h}')
        reg[h] = {'estado': est[0] if est else 'vigente', 'id': nid, 'n': secs[h][0], 't': t}
        ids.add(nid)

    with open(REG, 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(reg, ensure_ascii=False, indent=1, sort_keys=True) + '\n')

    secs_js = {n: h for h, (n, _) in sorted(secs.items(), key=lambda x: num_key(x[1][0]))}
    titulos = {}   # título editorial interior de cada sección, para el buscador
    for p in pages:
        s = open(os.path.join(ROOT, p), encoding='utf-8').read()
        for m in re.finditer(r'<section class="ed(?: [^"]*)?" id="([^"]+)">\s*<div class="ed__label">.*?<h2 class="ed__title">(.*?)</h2>', s, re.S):
            titulos[f'{p}#{m.group(1)}'] = re.sub(r'<[^>]+>', ' ', m.group(2)).replace('&nbsp;', ' ').split()
    def fila(h, v):
        o = {'id': v['id'], 'n': v['n'], 't': v['t'], 'h': ANCLA_INTEGRADA.get(v['id'], h), 'e': v['estado']}
        if v.get('en'):
            o['en'] = v['en']
        extra = v.get('alias', []) + [' '.join(titulos[h])] if h in titulos else v.get('alias', [])
        if extra:
            o['a'] = extra
        return o
    normas = sorted((fila(h, v) for h, v in reg.items()), key=lambda o: o['id'])
    alias = {old: (ANCLA_INTEGRADA.get(v['id'], h)) for h, v in reg.items() for old in v.get('antes', [])}
    alias.update({h: ANCLA_INTEGRADA[v['id']] for h, v in reg.items() if v['id'] in ANCLA_INTEGRADA and h != ANCLA_INTEGRADA[v['id']]})
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('window.KEYONS_SECS = ' + json.dumps(secs_js, ensure_ascii=False) + ';\n')
        f.write('window.KEYONS_CAPS = ' + json.dumps(caps, ensure_ascii=False) + ';\n')
        f.write('window.KEYONS_NORMAS = ' + json.dumps(normas, ensure_ascii=False) + ';\n')
        f.write('window.KEYONS_ALIAS = ' + json.dumps(alias, ensure_ascii=False) + ';\n')
    print(f'{len(reg)} normas en el registro · {len(secs)} secciones · {len(caps)} capítulos con página')


if __name__ == '__main__':
    main()
