"""Sistema de Diseño · capítulos redactados con normas propias (KYN-SDI).

Uso:  python tools/sd_capitulos.py
Después: python tools/niveles.py --aplicar  ·  python tools/sistema_diseno.py  ·  python tools/biblioteca.py

El contenido vive en un archivo por módulo (tools/sd/m01_experiencia.py, tools/sd/m02_arquitectura.py, …); las piezas
comunes, en tools/sd/base.py. Este archivo:
- escribe data/sd-capitulos/<capítulo>.html (las secciones que tools/sistema_diseno.py pega en cada página);
- actualiza data/sistema-diseno.json: los subcapítulos de cada capítulo redactado pasan a ser sus normas;
- actualiza data/sd-normas.json, fuente única de los códigos: lo construido queda «borrador»; lo demás conserva su estado;
- escribe propuestas/matriz-normativa-sd-01-06.md desde el registro.

Criterios: Guía 05 «Implementación editorial de capítulos», reglas-visuales R22, R26 y R27, y las indicaciones de Keylin
del 2026-11-17 (lectura principal breve, detalle en el acordeón único, verificación ejecutable, sin maquetas).
Todo es borrador: un capítulo con contenido no es un capítulo terminado; su cobertura está en propuestas/sd-entregas/.
"""
import importlib
import io
import json
import os
import pkgutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding='utf-8')
from normativa import registrar   # noqa: E402
import sd   # noqa: E402
from sd import base   # noqa: E402

ROOT = base.ROOT


def modulos():
    out = []
    for m in sorted(pkgutil.iter_modules(sd.__path__), key=lambda x: x.name):
        if m.name.startswith('m'):
            out += importlib.import_module('sd.' + m.name).CAPITULOS
    return out


def matriz_md(reg):
    filas = ['| Código | Cap. | Nombre corto | Estado | Textos de origen | Responsabilidad | Se cita en lugar de repetirse |', '| --- | --- | --- | --- | --- | --- | --- |']
    for n in sorted(reg['normas'], key=lambda n: (n['capitulo'], n['id'])):
        filas.append(f"| {n['id']} | {n['capitulo']} | {n['nombre']} | {n['estado']} | {' · '.join(n['origen'])} | {n['responsabilidad']} | {n['cita'] or '—'} |")
    return ('# Matriz normativa del Sistema de Diseño\n\n'
            'Generada por `tools/sd_capitulos.py` desde `data/sd-normas.json` (fuente única de los códigos). No se edita a mano.\n\n'
            '- **borrador:** código emitido, con página y en el buscador. Es contenido en revisión, no un capítulo terminado.\n'
            '- **reservado:** número apartado para un capítulo pendiente. Sin página, sin buscador y sin estado vigente ni implementado.\n'
            '- Un código corresponde a una responsabilidad normativa diferenciable. Los textos que expresaban la misma obligación se unieron, también entre capítulos.\n'
            '- Las normas UIX conservan su ID y son material de referencia. Su destino está en `propuestas/auditoria-uix-2026-11-17.md`.\n'
            '- La cobertura de cada capítulo (desarrollado, parcial, pendiente, requiere aprobación) está en `propuestas/sd-entregas/`.\n\n'
            + '\n'.join(filas) + '\n')


def main():
    caps = modulos()
    sd_json = json.load(io.open(os.path.join(ROOT, 'data', 'sistema-diseno.json'), encoding='utf-8'))
    num_de = {c['slug']: c['num'] for m in sd_json['modulos'] for c in m['capitulos']}
    reg = base.REG
    por_id = {n['id']: n for n in reg['normas']}
    for nid, b in base.CONSTRUIDAS.items():
        n = por_id.get(nid)
        if n is None:
            n = dict(id=nid, capitulo=num_de[b['slug']], nombre='', estado='', ruta=None, origen=[], responsabilidad='', cita='')
            reg['normas'].append(n); por_id[nid] = n
        n.update(nombre=b['nombre'], estado='borrador', ruta=b['ruta'], origen=b['origen'] or n['origen'],
                 responsabilidad=b['responsabilidad'] or n['responsabilidad'], cita=b['cita'] or n['cita'])
    # El registro se escribe antes de clasificar los niveles: tools/niveles.py lee de él las secciones de cada norma
    io.open(base.REGISTRO, 'w', encoding='utf-8', newline='\n').write(json.dumps(reg, ensure_ascii=False, indent=1) + '\n')
    for mod, capn, slug, secs, dc in caps:
        dst = os.path.join(ROOT, 'data', 'sd-capitulos', slug + '.html')
        io.open(dst, 'w', encoding='utf-8', newline='\n').write(
            f'    <!-- Capítulo {num_de[slug]} · generado por tools/sd_capitulos.py (tools/sd/). No se edita a mano. Borrador. -->' + ''.join(secs))
        m = next(x for x in sd_json['modulos'] if x['n'] == mod)
        cp = next(x for x in m['capitulos'] if x['n'] == capn)
        nums = sorted((n for n in reg['normas'] if n['estado'] != 'reservado' and n['ruta'] and n['ruta'].split('#')[0].endswith('/' + slug + '.html')),
                      key=lambda n: n['ruta'])
        cp['subcapitulos'] = [{'n': n['ruta'].split('#s-')[1].replace('-', '.'), 't': n['nombre'], 'estado': n['estado'], 'st': n['nombre'], 'norma': n['id']} for n in nums]
        cp['estado'] = 'borrador'
        cp['dc'] = dc
        if m['estado'] in ('estructura', 'pendiente'):
            m['estado'] = 'borrador'
        registrar(os.path.relpath(dst, ROOT).replace(os.sep, '/'))
    io.open(os.path.join(ROOT, 'data', 'sistema-diseno.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(sd_json, ensure_ascii=False, indent=1) + '\n')
    io.open(os.path.join(ROOT, 'propuestas', 'matriz-normativa-sd-01-06.md'), 'w', encoding='utf-8', newline='\n').write(matriz_md(reg))
    print('ok ·', len(caps), 'capítulos ·', len(base.CONSTRUIDAS), 'normas en borrador')


if __name__ == '__main__':
    main()
