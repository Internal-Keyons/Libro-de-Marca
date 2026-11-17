"""Íconos oficiales para los generadores de capítulos.

Fuente única: el catálogo del capítulo 26 (recursos/iconos.html, lo escribe tools/iconos.py).
icono('brujula') devuelve el SVG del catálogo tal cual: lienzo 32, trazo 2,5, color currentColor.
Si el nombre no existe en el catálogo, el generador se detiene: un ícono que falta se diseña, no se improvisa.
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CAT = None


def catalogo():
    global _CAT
    if _CAT is None:
        s = io.open(os.path.join(ROOT, 'recursos', 'iconos.html'), encoding='utf-8').read()
        _CAT = {m.group(1): m.group(2) for m in re.finditer(r'<button class="ict"[^>]*\bdata-n="([^"]+)"[^>]*>(<svg class="ic".*?</svg>)', s, re.S)}
    return _CAT


def icono(nombre):
    c = catalogo()
    if nombre not in c:
        raise SystemExit(f'El ícono «{nombre}» no está en el catálogo oficial (recursos/iconos.html)')
    return c[nombre]
