"""Clasificación normativa de los capítulos generados (reglas-visuales R16, leyenda normativa).

Los generadores (tools/estela.py, tools/expresion.py) marcan cada párrafo normativo con N(texto, nivel):
el nivel lo decide quien redacta, por el significado de la norma, nunca por las palabras que aparecen.
registrar(pagina) escribe esas decisiones en docs/niveles/niveles.json:
- la frase del párrafo marcado que lleva la palabra del nivel queda «aplicada» con su nivel;
- toda otra frase candidata de la página queda «no-normativa» (explicación, ejemplo o descripción).
Después, `python tools/niveles.py --aplicar` pone la palabra en mayúscula y el ícono al final del párrafo.
"""
import html as H
import importlib.util
import io
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEC = os.path.join(ROOT, 'docs', 'niveles', 'niveles.json')
MARCADAS = []   # (texto plano del párrafo, nivel)
PALABRA = {'debe': r'\bdeben?\b', 'no-debe': r'\bno\s+(?:se\s+)?deben?\b', 'deberia': r'\bdeberían?\b', 'puede': r'\bpueden?\b'}


def plano(t):
    return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', '', t))).replace('⁠', '').strip()


def N(texto, nivel):
    """Marca un párrafo como norma de nivel debe, no-debe, deberia o puede; devuelve el texto sin cambios."""
    t = plano(texto)
    if not re.search(PALABRA[nivel], t, re.I):
        raise SystemExit(f'Párrafo marcado «{nivel}» sin su palabra: {t[:80]}')
    MARCADAS.append((t, nivel))
    return texto


def registrar(pagina):
    spec = importlib.util.spec_from_file_location('niveles', os.path.join(ROOT, 'tools', 'niveles.py'))
    nv = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nv)
    cands = [c for c in nv.candidatos() if c['fuente'].startswith(pagina + '#')]
    D = json.load(io.open(DEC, encoding='utf-8'))
    D['declaraciones'] = [d for d in D['declaraciones'] if not d['fuente'].startswith(pagina + '#')]
    usadas, aplicadas = set(), 0
    for c in cands:
        f = c['frase'].replace('⁠', '')
        nivel = None
        for k, (t, nv_) in enumerate(MARCADAS):
            if f.lower() in t.lower() and re.search(PALABRA[nv_], f, re.I) and k not in usadas:
                nivel = nv_; usadas.add(k); break
        d = {'id': c['id'], 'fuente': c['fuente'], 'bloque': c['bloque'], 'frase': f}
        if nivel:
            d.update(estado='aplicada', nivel=nivel, motivo='Norma con su nivel, clasificada al redactar (tools/normativa.py).'); aplicadas += 1
        else:
            d.update(estado='no-normativa', motivo='Explicación, ejemplo o descripción.')
        D['declaraciones'].append(d)
    texto_pag = plano(io.open(os.path.join(ROOT, pagina), encoding='utf-8').read()).lower()
    faltan = [t for k, (t, _) in enumerate(MARCADAS) if k not in usadas and t.lower() in texto_pag]
    io.open(DEC, 'w', encoding='utf-8', newline='\n').write(json.dumps(D, ensure_ascii=False, indent=1) + '\n')
    print(f'{pagina}: {aplicadas} normas con nivel · {len(cands) - aplicadas} frases descriptivas')
    for t in faltan:
        print('   SIN REGISTRAR:', t[:90])
