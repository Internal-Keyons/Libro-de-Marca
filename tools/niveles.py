"""Fuerza normativa de las declaraciones del Libro de Marca: DEBE / NO DEBE / DEBERÍA / PUEDE.

Uso:  python tools/niveles.py            lista los candidatos y escribe docs/niveles/candidatos.json
      python tools/niveles.py --aplicar  aplica en las páginas las decisiones «aplicada» de docs/niveles/niveles.json

Regla (reglas-visuales R16, 2026-11-12, para todos los libros):
- La palabra del nivel va dentro de la redacción, natural y en mayúscula: «Los gradientes DEBEN construirse en casa».
- El ícono oficial (cuadrado de 8 px, .nvl--fin) va al final del párrafo, unido a la última palabra, nunca junto a la palabra del nivel.
- Caso A: una norma con su explicación, un ícono al final del párrafo. Caso B: varias normas, un párrafo por norma.
- Caso C: el texto descriptivo no lleva ícono.

Clasificación (decide una persona, no el script):
- El script solo propone candidatos: frases de una sección normativa con un verbo modal o una marca de obligación.
- docs/niveles/niveles.json (interno, no se publica) guarda la decisión de cada candidato: «aplicada» (norma confirmada con verbo modal explícito),
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
DEC = os.path.join(ROOT, 'docs', 'niveles', 'niveles.json')   # registro interno de trabajo: no se publica
CAND = os.path.join(ROOT, 'docs', 'niveles', 'candidatos.json')

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


WJ = '\u2060'   # unión de palabra: el ícono nunca queda solo al comienzo de una línea
ICONO_RX = re.compile(r'(?:\u2060|&#8288;)?<span class="nvl nvl--fin"[^>]*><i class="nvl__m[^"]*" aria-hidden="true"></i></span>')


COLA_RX = re.compile(r'<span class="nvl-cola">(.*?)</span>(?=</(?:p|li|dd)>)', re.S)


def limpiar(src):
    """Quita todos los íconos de nivel y su envoltura: la operación se repite desde cero y nunca duplica."""
    src = ICONO_RX.sub('', src)
    return COLA_RX.sub(lambda m: m.group(1), src)


def con_icono(t, nivel):
    """El final del párrafo y su ícono van juntos en una sola pieza (.nvl-cola): siguen unidos aunque el párrafo
    sea una retícula o una fila flexible, y la unión de palabra impide que el ícono empiece una línea."""
    i = t.rfind('>') + 1
    if t[i:].strip():                                       # el párrafo termina en texto
        return t[:i] + f'<span class="nvl-cola">{t[i:]}{WJ}{icono(nivel)}</span>'
    m = re.search(r'<(\w+)\b[^>]*>[^<]*</\1>$', t)          # termina en un elemento corto, por ejemplo <strong>
    if m:
        return t[:m.start()] + f'<span class="nvl-cola">{m.group(0)}{WJ}{icono(nivel)}</span>'
    return t + WJ + icono(nivel)


def profundidad(html):
    """Etiquetas en línea abiertas al final de un fragmento: un párrafo solo se separa donde no hay ninguna abierta."""
    d = 0
    for m in re.finditer(r'<(/?)(strong|b|em|span|a|i)\b[^>]*>', html):
        d += -1 if m.group(1) else 1
    return d


def aplicar():
    """Regla de niveles (reglas-visuales R16):
    - Caso A · una sola norma en el párrafo, con o sin explicación: un ícono al final del párrafo completo.
    - Caso B · varias normas independientes en un párrafo: se separan en párrafos, cada uno con su ícono al final.
      La explicación que sigue a una norma queda con ella; lo que va antes de la primera, también con la primera.
    - Caso C · texto descriptivo: sin ícono.
    Cada declaración se busca por su texto (no por posición), así que la operación se puede repetir sin cambios nuevos."""
    D = json.load(io.open(DEC, encoding='utf-8'))['declaraciones']
    por_pagina = {}
    for d in D:
        if d['estado'] == 'aplicada':
            por_pagina.setdefault(d['fuente'].split('#')[0], []).append(d)
    hechas, separados, fallos = 0, 0, []
    for pg, ds in por_pagina.items():
        ruta = os.path.join(ROOT, pg)
        src = limpiar(io.open(ruta, encoding='utf-8').read())
        # La palabra del nivel en mayúscula dentro de su frase (idempotente)
        grupos = {}
        for d in ds:
            an = d['fuente'].split('#')[1]
            ms = re.search(r'<section class="[^"]*\bed\b[^"]*" id="%s">(.*?)</section>' % re.escape(an), src, re.S)
            if not ms:
                fallos.append((d['id'], d['frase'][:60], 'sin sección')); continue
            hallado = None
            for b in re.finditer(r'<(p|li|dd)\b[^>]*>(.*?)</\1>', ms.group(1), re.S):
                plano, pos = mapa(b.group(2))
                if d['frase'].lower() in plano.lower():
                    hallado = (ms.start(1) + b.start(), ms.start(1) + b.end()); break
            if not hallado:
                fallos.append((d['id'], d['frase'][:60], 'frase no encontrada')); continue
            grupos.setdefault(hallado, []).append(d)
        # De atrás hacia adelante, para que las posiciones anteriores no cambien
        for (a0, a1), dd in sorted(grupos.items(), key=lambda x: -x[0][0]):
            bloque = src[a0:a1]
            m = re.match(r'(<(p|li|dd)\b[^>]*>)(.*?)(</\2>)$', bloque, re.S)
            abre, tag, inner, cierra = m.group(1), m.group(2), m.group(3), m.group(4)
            plano, pos = mapa(inner)
            for d in dd:   # mayúscula
                k = plano.lower().find(d['frase'].lower())
                w = re.search(PALABRA[d['nivel']], d['frase'], re.I)
                if w:
                    for g in range(1, (w.lastindex or 0) + 1):
                        if w.group(g):
                            p0 = pos[k + w.start(g)]; p1 = pos[k + w.end(g) - 1] + 1
                            inner = inner[:p0] + inner[p0:p1].upper() + inner[p1:]
            dd.sort(key=lambda d: plano.lower().find(d['frase'].lower()))
            if len(dd) == 1:   # Caso A
                partes = [(inner.rstrip(), dd[0])]
            else:              # Caso B
                cortes = [pos[plano.lower().find(d['frase'].lower())] for d in dd[1:]]
                if any(profundidad(inner[:c]) for c in cortes) or tag != 'p':
                    fallos.append((dd[0]['id'], dd[0]['frase'][:60], 'no se puede separar sin romper el formato: revisar a mano'))
                    partes = [(inner.rstrip(), dd[-1])]
                else:
                    lims = [0] + cortes + [len(inner)]
                    partes = [(inner[lims[n]:lims[n + 1]].strip(), dd[n]) for n in range(len(dd))]
                    separados += 1
            sangria = re.search(r'\n([ \t]*)$', src[:a0])
            sep = '\n' + (sangria.group(1) if sangria else '')
            nuevo = sep.join(f'{abre}{con_icono(t, d["nivel"])}{cierra}' for t, d in partes)
            src = src[:a0] + nuevo + src[a1:]
            hechas += len(partes)
        io.open(ruta, 'w', encoding='utf-8', newline='\n').write(src)
    print(f'{hechas} párrafos con su nivel · {separados} párrafos separados en varias normas · {len(fallos)} sin aplicar')
    for f in fallos:
        print('  ', f)


if __name__ == '__main__' and '--aplicar' in sys.argv:
    aplicar()
elif __name__ == '__main__':
    c = candidatos()
    io.open(CAND, 'w', encoding='utf-8', newline='\n').write(json.dumps(c, ensure_ascii=False, indent=1) + '\n')
    print(f'{len(c)} candidatos en {len({x["id"] for x in c})} normas · docs/niveles/candidatos.json')
