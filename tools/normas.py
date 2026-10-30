"""Registro de normas del Manual de Marca Keyons.

Uso:  python tools/normas.py

Lee las secciones de cada página (rótulo .ed__label: número y título), actualiza data/normas.json
y escribe js/secciones.js (KEYONS_SECS, KEYONS_CAPS y KEYONS_NORMAS) para el libro.

Reglas (recursos/referencia.html, 39.1):
- Un ID emitido nunca cambia, no se borra ni se reutiliza. Este script jamás regenera el registro desde cero.
- Si una página cambia su numeración, el ID se conserva y solo se actualiza el número visible («n»).
- Una sección nueva recibe ID únicamente si está en NUEVAS: emitir un ID es una decisión, no un efecto del script.
- Si una sección registrada ya no existe, el script avisa y no la borra: se marca [DESCONTINUADA] a mano.
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
    'marca/principios.html#calidad': ('KYN-MRK-DIS-006', 'Calidad sin firma visible'),
    # 11 · Criterio visual y antipatrones (aprobadas conceptualmente 2026-10-29; antes «KYN-VIS-###» provisional)
    **{f'fundamentos/criterio/antipatrones.html#vis-{i:03d}': (f'KYN-MRK-VIS-{i:03d}', t) for i, t in enumerate([
        'Kicker decorativo', 'Tracking indiscriminado', 'Jerarquía visual repetitiva', 'Tarjetas innecesarias',
        'Gradientes ornamentales', 'Geometría genérica', 'Acentos tipográficos repetidos', 'Iconografía de relleno',
        'Saturación de microelementos', 'Simetría automática', 'Movimiento ornamental', 'Contraste insuficiente',
        'Lenguaje genérico', 'Maximalismo uniforme', 'Originalidad a costa de orientación', 'Composición no intercambiable'], 1)},
    # 10 · Composiciones (2026-10-30)
    'fundamentos/composicion/editorial.html#decidir': ('KYN-MRK-CMP-001', 'Decidir la composición'),
    'fundamentos/composicion/editorial.html#simetria': ('KYN-MRK-CMP-002', 'Orden y experimentación'),
    'fundamentos/composicion/editorial.html#reticulas': ('KYN-MRK-CMP-003', 'Retículas editoriales'),
    'fundamentos/composicion/editorial.html#ritmo': ('KYN-MRK-CMP-004', 'Ritmo visual'),
    # 08 · Tipografía y 12 · Elementos gráficos (2026-10-30)
    'fundamentos/tipografia/sistema.html#funcion': ('KYN-MRK-TYP-007', 'Uso por función'),
    'fundamentos/elementos/graficos.html#profundidad': ('KYN-MRK-ILU-009', 'Profundidad atmosférica'),
}

# Cambios de título o estado de normas ya emitidas (el ID nunca cambia)
CAMBIOS = {
    'KYN-MRK-DIS-002': {'t': 'Identidad, experiencia y sistema: roles definidos'},
    'KYN-MRK-DIS-003': {'t': 'Diseño: calma y expresión'},
    'KYN-MRK-DIS-004': {'t': 'Intensidad según contexto'},
    'KYN-MRK-DIS-005': {'t': 'Claridad antes que complejidad'},
    # 2026-10-30: sale de Principios de diseño; el ID queda reservado
    'KYN-MRK-DIS-006': {'estado': 'descontinuada'},
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
    ids = {v['id'] for v in reg.values()}
    for h, v in reg.items():
        v.update(CAMBIOS.get(v['id'], {}))
        if h in secs:
            v['n'] = secs[h][0]
        elif v['estado'] != 'descontinuada':
            print('AVISO: la norma', v['id'], 'ya no tiene sección en', h, '(no se borra)')
    for h, (nid, t) in NUEVAS.items():
        if h in reg:
            continue
        if nid in ids:
            sys.exit(f'{nid} ya existe en el registro: un ID nunca se reutiliza')
        if h not in secs:
            sys.exit(f'{nid}: no existe la sección {h}')
        reg[h] = {'estado': 'vigente', 'id': nid, 'n': secs[h][0], 't': t}
        ids.add(nid)

    with open(REG, 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(reg, ensure_ascii=False, indent=1, sort_keys=True) + '\n')

    secs_js = {n: h for h, (n, _) in sorted(secs.items(), key=lambda x: num_key(x[1][0]))}
    normas = sorted(({'id': v['id'], 'n': v['n'], 't': v['t'], 'h': h, 'e': v['estado']} for h, v in reg.items()), key=lambda o: o['id'])
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('window.KEYONS_SECS = ' + json.dumps(secs_js, ensure_ascii=False) + ';\n')
        f.write('window.KEYONS_CAPS = ' + json.dumps(caps, ensure_ascii=False) + ';\n')
        f.write('window.KEYONS_NORMAS = ' + json.dumps(normas, ensure_ascii=False) + ';\n')
    print(f'{len(reg)} normas en el registro · {len(secs)} secciones · {len(caps)} capítulos con página')


if __name__ == '__main__':
    main()
