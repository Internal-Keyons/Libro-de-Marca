"""Fuerza normativa de las declaraciones del Libro de Marca: DEBE / NO DEBE / DEBERÍA / PUEDE.

Uso:  python tools/niveles.py            lista los candidatos y escribe data/niveles-candidatos.json
      python tools/niveles.py --aplicar  aplica en las páginas las decisiones «aplicada» de data/niveles.json

Regla (reglas-visuales R16, 2026-11-12, para todos los libros):
- La palabra del nivel va dentro de la redacción, natural y en mayúscula: «Los gradientes DEBEN construirse en casa».
- El ícono oficial (cuadrado de 8 px, .nvl) va al final de la declaración, nunca junto a la palabra.
- Una declaración = un nivel. Un párrafo con dos fuerzas se separa o queda pendiente.

Clasificación (decide una persona, no el script):
- El script solo propone candidatos: frases de una sección normativa con un verbo modal o una marca de obligación.
- data/niveles.json guarda la decisión de cada candidato: «aplicada» (norma confirmada con verbo modal explícito),
  «no-normativa» (descripción, historia o ejemplo) o «pendiente» (normativa pero ambigua o sin verbo: decide Keylin).
- «Siempre» y «nunca» nunca se convierten solos en DEBE o NO DEBE.
"""
import html as H
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = json.load(io.open(os.path.join(ROOT, 'data', 'normas.json'), encoding='utf-8'))
DEC = os.path.join(ROOT, 'data', 'niveles.json')
CAND = os.path.join(ROOT, 'data', 'niveles-candidatos.json')

MODAL = re.compile(r'\b(no\s+(?:se\s+)?deben?|deben?|deberían?|pueden?|podrán?|se\s+permiten?|se\s+recomienda|nunca|siempre|jamás|obligatori[oa]s?|prohibid[oa]s?)\b', re.I)
BLOQUE = re.compile(r'<(p|li|dd|td|figcaption|span class="pgrid__d"|p class="[^"]*")[^>]*>(.*?)</(?:p|li|dd|td|figcaption|span)>', re.S)


def texto(s):
    return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', '', s))).strip()


def secciones(src):
    out = {}
    for m in re.finditer(r'<section class="[^"]*\bed\b[^"]*" id="([^"]+)">(.*?)</section>', src, re.S):
        out[m.group(1)] = m.group(2)
    return out


def candidatos():
    paginas = {}
    for h, v in REG.items():
        if v['estado'] not in ('vigente', 'borrador'):
            continue
        pg, an = h.split('#')
        paginas.setdefault(pg, []).append((an, v))
    out = []
    for pg, ss in sorted(paginas.items()):
        src = io.open(os.path.join(ROOT, pg), encoding='utf-8').read()
        sec = secciones(src)
        for an, v in ss:
            cuerpo = sec.get(an, '')
            for k, m in enumerate(re.finditer(r'<(p|li|dd)\b[^>]*>(.*?)</\1>', cuerpo, re.S)):
                t = texto(m.group(2))
                if len(t) < 12:
                    continue
                for f in re.split(r'(?<=[.;!?])\s+(?=[A-ZÁÉÍÓÚÑ¿«(])', t):
                    w = MODAL.findall(f)
                    if w:
                        out.append({'id': v['id'], 'estado': v['estado'], 'fuente': f'{pg}#{an}', 'bloque': k, 'frase': f,
                                    'marcas': sorted({x.lower() for x in w})})
    return out


ETQ = {'debe': 'Debe', 'no-debe': 'No debe', 'deberia': 'Debería', 'puede': 'Puede'}
MARCA = {'debe': 'debe', 'no-debe': 'debe', 'deberia': 'deberia', 'puede': 'puede'}   # «No debe» usa la marca de Debe
PALABRA = {'debe': r'\b(deben?)\b', 'no-debe': r'\b(?:(no)\s+)?(?:se\s+)?(deben?)\b', 'deberia': r'\b(deberían?)\b', 'puede': r'\b(pueden?)\b'}


def icono(nivel):
    return (f'<span class="nvl nvl--fin" data-lvl="{MARCA[nivel]}" role="img" aria-label="Nivel: {ETQ[nivel]}">'
            f'<i class="nvl__m nvl__m--{MARCA[nivel]}" aria-hidden="true"></i></span>')


def mapa(inner):
    """Texto visible del bloque (espacios colapsados) y, para cada carácter, su posición en el HTML."""
    txt, pos, i = [], [], 0
    while i < len(inner):
        ch = inner[i]
        if ch == '<':
            i = inner.index('>', i) + 1
            continue
        if ch == '&' and ';' in inner[i:i + 10]:
            j = inner.index(';', i)
            for c in H.unescape(inner[i:j + 1]):
                if c.isspace():   # &nbsp; cuenta como espacio, igual que en el texto extraído
                    if txt and txt[-1] != ' ':
                        txt.append(' '); pos.append(i)
                    continue
                txt.append(c); pos.append(i)
            i = j + 1
            continue
        if ch.isspace():
            if txt and txt[-1] != ' ':
                txt.append(' '); pos.append(i)
            i += 1
            continue
        txt.append(ch); pos.append(i)
        i += 1
    return ''.join(txt), pos


def aplicar():
    D = json.load(io.open(DEC, encoding='utf-8'))['declaraciones']
    hechas, fallos = 0, []
    por_pagina = {}
    for d in D:
        if d['estado'] == 'aplicada':
            por_pagina.setdefault(d['fuente'].split('#')[0], []).append(d)
    for pg, ds in por_pagina.items():
        ruta = os.path.join(ROOT, pg)
        src = io.open(ruta, encoding='utf-8').read()
        for d in ds:
            an = d['fuente'].split('#')[1]
            ms = re.search(r'<section class="[^"]*\bed\b[^"]*" id="%s">(.*?)</section>' % re.escape(an), src, re.S)
            bs = list(re.finditer(r'<(p|li|dd)\b[^>]*>(.*?)</\1>', ms.group(1), re.S)) if ms else []
            if d['bloque'] >= len(bs):
                fallos.append((d['id'], d['frase'][:60], 'sin bloque')); continue
            b = bs[d['bloque']]
            ini = ms.start(1) + b.start(2)
            inner = b.group(2)
            plano, pos = mapa(inner)
            plano_s = plano.strip(); off = len(plano) - len(plano.lstrip())
            k = plano_s.lower().find(d['frase'].lower())   # sin distinguir mayúsculas: una frase ya aplicada se reconoce
            if k < 0:
                fallos.append((d['id'], d['frase'][:60], 'frase no encontrada')); continue
            k += off
            fin = k + len(d['frase'])
            if 'nvl--fin' in inner[pos[fin - 1]:pos[fin - 1] + 160]:
                continue   # ya aplicada
            nuevo = inner
            # 1 · El ícono al final de la declaración, después de las etiquetas que la cierran
            corte = pos[fin - 1] + 1
            while True:
                m = re.match(r'</(strong|b|em|span|a)>', nuevo[corte:])
                if not m:
                    break
                corte += m.end()
            nuevo = nuevo[:corte] + icono(d['nivel']) + nuevo[corte:]
            # 2 · La palabra del nivel en mayúscula, dentro de la frase
            m = re.search(PALABRA[d['nivel']], d['frase'], re.I)
            if m:
                for g in range(1, (m.lastindex or 0) + 1):
                    if m.group(g) is None:
                        continue
                    a0 = pos[k + m.start(g)]; a1 = pos[k + m.end(g) - 1] + 1
                    nuevo = nuevo[:a0] + nuevo[a0:a1].upper() + nuevo[a1:]
            src = src[:ini] + nuevo + src[ini + len(inner):]
            hechas += 1
        io.open(ruta, 'w', encoding='utf-8', newline='\n').write(src)
    print(f'{hechas} declaraciones con su nivel · {len(fallos)} sin aplicar')
    for f in fallos:
        print('  ', f)


if __name__ == '__main__' and '--aplicar' in sys.argv:
    aplicar()
elif __name__ == '__main__':
    c = candidatos()
    io.open(CAND, 'w', encoding='utf-8', newline='\n').write(json.dumps(c, ensure_ascii=False, indent=1) + '\n')
    print(f'{len(c)} candidatos en {len({x["id"] for x in c})} normas · data/niveles-candidatos.json')
