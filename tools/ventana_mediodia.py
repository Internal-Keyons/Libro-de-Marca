"""Uso: python tools/ventana_mediodia.py  → assets/img/ventanas/ventana-mediodia.webp

La ventana de Mediodía con el mismo estilo de las otras cuatro (600 × 800): un degradado suave y difuso con grano fino,
sin destellos. De arriba abajo, la escala Azul Cielo de tokens.css: 500, 400, 300, 200 y 100, con manchas amplias
y desenfocadas que le dan la variación natural de un cielo despejado.
"""
import os
import random

from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 600, 800
hx = lambda h: tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))
# Escala Azul Cielo (css/tokens.css): 500, 400, 300, 200 y 100, tan claros como las otras ventanas
PARADAS = [(0.0, hx('#729BDD')), (0.35, hx('#8FAFE2')), (0.65, hx('#ACC3E7')), (0.85, hx('#C6D5EC')), (1.0, hx('#E0E7F1'))]


def color(t):
    for (a, ca), (b, cb) in zip(PARADAS, PARADAS[1:]):
        if t <= b:
            k = (t - a) / (b - a)
            return tuple(round(ca[i] + (cb[i] - ca[i]) * k) for i in range(3))
    return PARADAS[-1][1]


base = Image.new('RGB', (W, H))
d = ImageDraw.Draw(base)
for y in range(H):
    d.line([(0, y), (W, y)], fill=color(y / (H - 1)))

# Manchas amplias y desenfocadas: más claras abajo a la derecha, más profundas arriba a la izquierda
capa = Image.new('RGBA', (W, H), (0, 0, 0, 0))
dc = ImageDraw.Draw(capa)
for cx, cy, r, c, a in [(520, 690, 330, '#E0E7F1', 120), (90, 120, 300, '#688DCB', 60), (420, 260, 260, '#9DB9E5', 60), (120, 560, 280, '#B9CCEA', 70)]:
    dc.ellipse([cx - r, cy - r, cx + r, cy + r], fill=hx(c) + (a,))
capa = capa.filter(ImageFilter.GaussianBlur(120))
img = Image.alpha_composite(base.convert('RGBA'), capa).convert('RGB')

# Grano fino, como en las otras ventanas
random.seed(7)
ruido = Image.effect_noise((W, H), 18).convert('L')
grano = Image.merge('RGB', (ruido, ruido, ruido))
img = Image.blend(img, Image.composite(img, grano, Image.new('L', (W, H), 236)), 0.5)

img.save(os.path.join(ROOT, 'assets', 'img', 'ventanas', 'ventana-mediodia.webp'), quality=88)
print('ok · assets/img/ventanas/ventana-mediodia.webp')
