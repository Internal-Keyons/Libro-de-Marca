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

Biblioteca (errores, salida 1), en los dos libros abiertos (Marca y Sistema de Diseño):
- IDs de norma duplicados: en data/normas.json, en data/sistema-diseno.json o entre los dos.
- Enlaces del índice de cada libro (js/nav-data.js, js/nav-sistema-diseno.js) a páginas o anclas que no existen.
- Referencias KYN-MRK en las páginas del Sistema de Diseño a normas que no están en el registro.
- Normas KYN-PRD-UIX citadas por el Sistema de Diseño sin su archivo en ia/normas.
- Un ID KYN-SDI emitido en el contenido sin estar registrado (el prefijo está reservado, sin emitir).
- Bloques «Normas relacionadas» o «Relacionado» (CLAUDE.md: la referencia va dentro del texto).
- Cada norma redactada del Sistema de Diseño con su estructura: rótulo con ID, titular, entrada y filas con nivel.
- Los seis libros con su nombre oficial (data/libros.json) en la portada, el selector, la Guía y la tabla de tramas.
- Estilos independientes: cada libro carga solo su hoja; libro.css sin reglas de un libro; sistema-diseno.css acotado.
"""
import datetime
import hashlib
import io
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


def biblioteca():
    """Revisión de la Biblioteca: IDs, anclas, referencias, estructura y nombres. Devuelve la lista de errores."""
    import glob
    err = []
    lee = lambda p: io.open(os.path.join(ROOT, p), encoding='utf-8').read() if os.path.exists(os.path.join(ROOT, p)) else None
    ids_mrk = [v['id'] for v in json.load(io.open(os.path.join(ROOT, 'data', 'normas.json'), encoding='utf-8')).values()]
    SD = json.load(io.open(os.path.join(ROOT, 'data', 'sistema-diseno.json'), encoding='utf-8'))
    ids_sd = [sc['norma'] for m in SD['modulos'] for c in m['capitulos'] for sc in c['subcapitulos'] if sc.get('norma')]
    for nombre, ids in (('data/normas.json', ids_mrk), ('data/sistema-diseno.json', ids_sd)):
        for x in sorted({i for i in ids if ids.count(i) > 1}):
            err.append(f'ID DOBLE {x}: aparece más de una vez en {nombre}')
    for x in sorted(set(ids_mrk) & set(ids_sd)):
        err.append(f'ID DOBLE {x}: está en el registro de Marca y en el del Sistema de Diseño')
    for x in sorted(set(ids_sd)):
        if not os.path.exists(os.path.join(ROOT, 'ia', 'normas', x + '.md')):
            err.append(f'SIN NORMA {x}: el Sistema de Diseño la cita y no está en ia/normas')
    # Anclas de los dos índices
    def ids_de(p):
        t = lee(p)
        return None if t is None else set(re.findall(r'\sid="([^"]+)"', t))
    for archivo in ('js/nav-data.js', 'js/nav-sistema-diseno.js'):
        for h in sorted(set(re.findall(r"href: '([^']+)'", lee(archivo)))):
            pg, _, an = h.partition('#')
            hay = ids_de(pg)
            if hay is None:
                err.append(f'ENLACE  {archivo}: {h} lleva a una página que no existe')
            elif an and an not in hay:
                err.append(f'ANCLA   {archivo}: {h} lleva a un ancla que no existe')
    # Referencias y bloques prohibidos en las páginas del Sistema de Diseño
    for p in sorted(glob.glob(os.path.join(ROOT, 'sistema-diseno', '**', '*.html'), recursive=True)):
        t = io.open(p, encoding='utf-8').read()
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        for x in sorted(set(re.findall(r'KYN-MRK-[A-Z]{3}-\d{3}', t)) - set(ids_mrk)):
            err.append(f'REFERENCIA {rel}: cita {x}, que no está en data/normas.json')
        for x in sorted(set(re.findall(r'KYN-SDI-[A-Z]{3}-\d{3}', t))):
            err.append(f'SDI     {rel}: {x} aparece emitido; KYN-SDI está reservado y sin emitir')
    for p in sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)):
        if any(x in p for x in ('_tmp', 'propuestas', 'Libro de marcar', '_lab', 'documental')):
            continue
        t = io.open(p, encoding='utf-8').read()
        if re.search(r'<h[1-4][^>]*>\s*(Normas relacionadas|Relacionado)\s*</h[1-4]>', t):
            err.append(f'BLOQUE  {os.path.relpath(p, ROOT)}: tiene un bloque «Normas relacionadas» o «Relacionado»')
    # Estructura de cada norma redactada del Sistema de Diseño
    for p in sorted(glob.glob(os.path.join(ROOT, 'data', 'sd-capitulos', '*.html'))):
        t = io.open(p, encoding='utf-8').read()
        for sec in re.findall(r'<section class="ed" id="[^"]+">.*?</section>', t, re.S):
            sid = re.search(r'id="([^"]+)"', sec).group(1)
            if 'ed__code' not in sec:
                continue   # sección sin ID: contenido de lectura, no norma
            falta = [k for k, rx in (('rótulo con ID', r'class="ed__code"'), ('titular', r'class="ed__title"'),
                                     ('entrada', r'class="ed__lead"'), ('filas con nivel', r'data-lvl="(debe|deberia|puede)"')) if not re.search(rx, sec)]
            if falta:
                err.append(f'NORMA   {os.path.basename(p)}#{sid}: le falta {", ".join(falta)}')
    # Estilos independientes por libro (docs/ARQUITECTURA_BIBLIOTECA.md)
    for p in sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)):
        if any(x in p for x in ('_tmp', 'propuestas', 'Libro de marcar', '_lab', 'documental')):
            continue
        t = io.open(p, encoding='utf-8').read()
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        if 'js/nav-data.js' in t and 'sistema-diseno.css' in t:
            err.append(f'ESTILOS {rel}: una página del Libro de Marca carga la hoja del Sistema de Diseño')
        if 'nav-sistema-diseno.js' in t and 'css/marca.css' in t:
            err.append(f'ESTILOS {rel}: una página del Sistema de Diseño carga la hoja del Libro de Marca')
        if 'nav-sistema-diseno.js' in t and 'sistema-diseno.css' not in t:
            err.append(f'ESTILOS {rel}: una página del Sistema de Diseño no carga su hoja propia')
    if re.search(r'\[data-libro="(?!biblioteca)', re.sub(r'/\*.*?\*/', '', lee('css/libro.css'), flags=re.S)):
        err.append('ESTILOS css/libro.css: tiene reglas de un libro concreto; van en la hoja de ese libro')
    css = re.sub(r'/\*.*?\*/', '', lee('css/sistema-diseno.css'), flags=re.S)
    for sel in re.findall(r'([^{};]+)\{', css):
        for x in sel.split(','):
            x = x.strip()
            if x and not x.startswith('@') and not re.search(r'\.sd[a-z]*[-_]|\.sdn|html\[data-libro="sistema-diseno"\]', x):
                err.append(f'ESTILOS css/sistema-diseno.css: «{x}» no está acotado al Sistema de Diseño')
    # Nombres oficiales de los seis libros
    L = json.load(io.open(os.path.join(ROOT, 'data', 'libros.json'), encoding='utf-8'))['libros']
    for p in ('index.html', 'js/libro.js', 'guia/index.html', 'fundamentos/elementos/graficos.html'):
        t = lee(p) or ''
        for b in L:
            if p == 'guia/index.html' and not b.get('prefijo'):
                continue   # la Guía agrupa los libros sin prefijo en una sola fila
            if b['nombre'] not in t:
                err.append(f'NOMBRE  {p}: falta «{b["nombre"]}», el nombre oficial de data/libros.json')
    return err


def auditoria():
    """Auditoría para Polaris: niveles por declaración, referencias, metadatos, índice y exportaciones.
    Devuelve (errores, avisos). Los avisos informan sin detener: metadatos sin designar, exportaciones desactualizadas a propósito."""
    import glob
    err, av = [], []
    lee = lambda p: io.open(os.path.join(ROOT, p), encoding='utf-8').read() if os.path.exists(os.path.join(ROOT, p)) else ''
    N = json.load(io.open(os.path.join(ROOT, 'data', 'normas.json'), encoding='utf-8'))
    ids = {v['id'] for v in N.values()}
    PAL = {'debe': r'\bDEBE[N]?\b', 'deberia': r'\bDEBERÍA[N]?\b', 'puede': r'\bPUEDE[N]?\b'}
    paginas = [p for p in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)
               if not any(x in p for x in ('_tmp', 'propuestas', 'Libro de marcar', '_lab', 'documental', os.sep + 'tools' + os.sep))]
    sin_icono = 0
    for p in paginas:
        t = io.open(p, encoding='utf-8').read()
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        # 1 · Cada ícono de nivel corresponde a la palabra de su declaración (la frase que termina en el ícono)
        for m in re.finditer(r'<span class="nvl nvl--fin" data-lvl="(\w+)"([^>]*)>', t):
            lvl, attrs = m.group(1), m.group(2)
            antes = re.sub(r'<[^>]+>', '', t[max(0, m.start() - 600):m.start()])
            frase = re.split(r'(?<=[.;!?])\s+|<', antes)[-1] if antes else ''
            frase = re.split(r'(?<=[.;!?:])\s+(?=[A-ZÁÉÍÓÚÑ¿«(])', antes.strip())[-1]
            if lvl not in PAL:
                err.append(f'NIVEL   {rel}: ícono con nivel desconocido «{lvl}»')
            elif not re.search(PAL[lvl], frase):
                err.append(f'NIVEL   {rel}: el ícono «{lvl}» no tiene su palabra en mayúscula en la declaración «…{frase[-70:]}»')
            if 'aria-label="Nivel:' not in attrs:
                err.append(f'NIVEL   {rel}: ícono de nivel sin alternativa accesible')
        # Una palabra de nivel en mayúscula sin ícono en su declaración (en el texto del libro, no en ejemplos de «No hacer»)
        plano = re.sub(r'<span class="nvl nvl--fin"[^>]*>', '¶', t)
        plano = re.sub(r'<[^>]+>', ' ', plano)
        plano = re.sub(r'([.;!?])\s*¶', r'¶', plano)   # el ícono va después del punto final de su declaración
        if rel in ('inicio.html', 'guia/index.html', 'sistema-diseno/index.html'):
            plano = ''   # leyendas que explican los niveles: no son declaraciones
        for f in re.split(r'(?<=[.;!?])\s+', plano):
            if re.search(r'\b(DEBE[N]?|DEBERÍA[N]?|PUEDE[N]?)\b', f) and '¶' not in f and 'KYN-' not in f:
                sin_icono += 1
        # 2 · Referencias a normas que no se resuelven (se informan, nunca se borran)
        if not rel.startswith(('sistema-diseno/', 'data/')):
            for x in sorted(set(re.findall(r'KYN-MRK-[A-Z]{3}-\d{3}', t)) - ids):
                av.append(f'REFERENCIA {rel}: cita {x}, que no está en el registro (se conserva; revisar)')
    if sin_icono:
        av.append(f'NIVEL   {sin_icono} frases con DEBE/DEBERÍA/PUEDE en mayúscula sin ícono en su declaración (revisar con tools/niveles.py)')
    # 3 · Metadatos esenciales: se informan los que faltan, no se inventan
    A = json.load(io.open(os.path.join(ROOT, 'data', 'autoridad.json'), encoding='utf-8'))['normas']
    for campo, nombre in (('ambito', 'ámbito'), ('responsable', 'responsable'), ('fecha_aprobacion', 'fecha de aprobación')):
        n = sum(1 for v in A.values() if not v.get(campo))
        if n:
            av.append(f'METADATO {nombre}: vacío en {n} de {len(A)} normas (pendiente de designar; no se completa sin aprobación)')
    for v in N.values():
        if v['id'] not in A:
            av.append(f'METADATO {v["id"]}: sin ficha en data/autoridad.json (correr tools/gobierno.py)')
    # 4 · Índice y contenido: cada sección con rótulo debería estar en el índice del libro
    nav = lee('js/nav-data.js')
    fuera = [h for h in N if h not in nav and N[h]['estado'] in ('vigente', 'borrador')]
    if fuera:
        av.append(f'ÍNDICE  {len(fuera)} normas sin entrada propia en js/nav-data.js (subsecciones): ' + ', '.join(N[h]['id'] for h in fuera[:8]) + (' …' if len(fuera) > 8 else ''))
    # 5 · Exportaciones (no se regeneran en esta ronda): se informa la diferencia
    ia = {os.path.basename(x)[:-3] for x in glob.glob(os.path.join(ROOT, 'ia', 'normas', 'KYN-MRK-*.md'))}
    faltan = sorted(ids - ia)
    if faltan:
        av.append(f'EXPORTACIÓN {len(faltan)} normas sin archivo en ia/normas: ' + ', '.join(faltan))
    md = lee('ia/libro-de-marca.md')
    if md:
        f2 = sorted(i for i in ids if i not in md)
        if f2:
            av.append(f'EXPORTACIÓN {len(f2)} normas ausentes de ia/libro-de-marca.md: ' + ', '.join(f2))
    return err, av


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

    errores, avisos = biblioteca(), []
    e2, auditados = auditoria()
    errores += e2
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
    for x in auditados:
        print('AVISO  ', x)
    print(f'{len(cur)} secciones · {len(errores)} errores · {len(avisos)} cambios por aprobar')
    sys.exit(1 if errores else 0)


if __name__ == '__main__':
    main()
