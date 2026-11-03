"""Protege la redacción de las normas: detecta cambios, pérdidas y reversiones antes de guardar o publicar.

Uso:
  python tools/verificar.py                     compara el libro con la referencia aprobada
  python tools/verificar.py --aprobar "nota"    registra la redacción actual como aprobada (con la nota)
  python tools/verificar.py --historial         siembra la referencia con todas las versiones del historial de Git

La referencia (data/referencia-contenido.json) se genera desde las páginas: no se edita a mano ni es una
segunda fuente. Guarda, por cada sección del libro, su ID, estado, ruta y la huella de cada redacción aprobada.

Errores (salida 1):
- Una norma registrada en data/normas.json sin su sección en el libro.
- Una sección cuyo texto volvió a una redacción anterior a la aprobada: una reversión.
Avisos (salida 0): secciones nuevas o con redacción cambiada, que esperan aprobación.
"""
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exportar import Tree, ws  # noqa: E402
from normas import ROOT, nav  # noqa: E402

REF = os.path.join(ROOT, 'data', 'referencia-contenido.json')


def pages():
    out = []
    for a in nav():
        for c in a['ch']:
            for it in c['items']:
                h = it.get('href', '').split('#')[0]
                if h and h not in out:
                    out.append(h)
    return out


def sections(src):
    """Texto normalizado de cada sección: lo visible y lo que vive en atributos (descripciones, glosarios)."""
    out = {}
    for sec in Tree(src).root.find_all(lambda n: n.tag == 'section' and n.has('ed') and 'id' in n.attrs):
        extra = ' '.join(n.attrs.get(k, '') for n in sec.find_all(lambda n: True) for k in ('data-d', 'data-w', 'data-tip', 'data-cap'))
        # Sin el número de sección: renumerar un capítulo no es cambiar su redacción
        t = re.sub(r'^\s*\d+(?:\.\d+)*', '', ws(sec.text()))
        out[sec.attrs['id']] = re.sub(r'\s+', ' ', t + ' ' + extra).strip()
    return out


def huella(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


def actual():
    reg = json.load(open(os.path.join(ROOT, 'data', 'normas.json'), encoding='utf-8'))
    out = {}
    for p in pages():
        for sid, t in sections(open(os.path.join(ROOT, p), encoding='utf-8').read()).items():
            k = f'{p}#{sid}'
            n = reg.get(k, {})
            out[k] = {'id': n.get('id'), 'estado': n.get('estado', 'sin ID'), 'texto': t, 'huella': huella(t)}
    return out, reg


def cargar():
    if os.path.exists(REF):
        return json.load(open(REF, encoding='utf-8'))
    return {'nota': 'Generado por tools/verificar.py. No se edita a mano.', 'secciones': {}}


def guardar(ref):
    with open(REF, 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(ref, ensure_ascii=False, indent=1, sort_keys=True) + '\n')


def registrar(ref, cur, nota, fecha):
    for k, v in cur.items():
        e = ref['secciones'].setdefault(k, {'versiones': []})
        e.update({'id': v['id'], 'estado': v['estado'], 'texto': v['texto']})
        if not e['versiones'] or e['versiones'][-1]['huella'] != v['huella']:
            e['versiones'].append({'huella': v['huella'], 'aprobada': fecha, 'nota': nota})


def historial(ref):
    """Siembra la referencia con cada versión de cada sección en los commits de main, en orden."""
    commits = subprocess.check_output(['git', 'log', '--reverse', '--format=%h %ad', '--date=short'], cwd=ROOT, encoding='utf-8').split('\n')
    for line in filter(None, commits):
        c, d = line.split()
        for p in pages():
            r = subprocess.run(['git', 'show', f'{c}:{p}'], cwd=ROOT, capture_output=True)
            if r.returncode:
                continue
            for sid, t in sections(r.stdout.decode('utf-8')).items():
                e = ref['secciones'].setdefault(f'{p}#{sid}', {'versiones': []})
                h = huella(t)
                if not e['versiones'] or e['versiones'][-1]['huella'] != h:
                    e['versiones'].append({'huella': h, 'aprobada': d, 'nota': f'commit {c}'})


def main():
    ref = cargar()
    cur, reg = actual()
    hoy = datetime.date.today().isoformat()
    if '--historial' in sys.argv:
        historial(ref)
        registrar(ref, cur, 'estado del libro al sembrar la referencia', hoy)
        guardar(ref)
        print(f'Referencia sembrada: {len(ref["secciones"])} secciones')
        return
    if '--aprobar' in sys.argv:
        i = sys.argv.index('--aprobar')
        nota = sys.argv[i + 1] if len(sys.argv) > i + 1 else 'aprobado'
        registrar(ref, cur, nota, hoy)
        guardar(ref)
        print(f'Aprobado: {nota}')
        return

    errores, avisos = [], []
    for h, n in reg.items():
        if n['estado'] not in ('descontinuada', 'integrada') and h not in cur:
            errores.append(f'FALTA   {n["id"]} ({h}): la norma no tiene sección en el libro')
    for k, v in cur.items():
        e = ref['secciones'].get(k)
        nombre = v['id'] or k
        if not e:
            avisos.append(f'NUEVA   {nombre}: sección sin aprobar')
            continue
        hs = [x['huella'] for x in e['versiones']]
        if v['huella'] == hs[-1]:
            continue
        if v['huella'] in hs[:-1]:
            j = hs.index(v['huella'])
            errores.append(f'REVERSIÓN {nombre}: volvió a la redacción del {e["versiones"][j]["aprobada"]} ({e["versiones"][j]["nota"]}); '
                           f'la aprobada es del {e["versiones"][-1]["aprobada"]}')
        else:
            avisos.append(f'CAMBIO  {nombre}: redacción distinta de la aprobada el {e["versiones"][-1]["aprobada"]}')
    for x in errores + avisos:
        print(x)
    print(f'{len(cur)} secciones · {len(errores)} errores · {len(avisos)} cambios por aprobar')
    sys.exit(1 if errores else 0)


if __name__ == '__main__':
    main()
