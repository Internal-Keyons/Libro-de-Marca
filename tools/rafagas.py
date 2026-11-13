"""Ráfagas de color (KYN-MRK-ILU-006): genera las seis formas y las inserta en la página.

Uso:
  python tools/rafagas.py                 genera las seis y actualiza fundamentos/elementos/graficos.html
  python tools/rafagas.py --hoja ruta.png solo escribe una hoja de contacto, sin tocar la página
  python tools/rafagas.py --escala .5     resolución de trabajo (1 es la final)

Cada ráfaga es una o varias cintas. Una cinta es una curva con dos anchos, uno a cada lado, porque el
borde de una ráfaga no es simétrico. El perfil es gaussiano y se recorta con un umbral suave: el
interior queda lleno y el borde se disuelve sin perder la forma.
El color sigue a la cinta: avanza a lo largo de la curva y cambia de un borde al otro, mezclado en OKLab.
Por eso la forma se lee también desde adentro.

En reposo la ráfaga queda quieta: la página no lleva cauce ni flujo (pedido de Keylin, 2026-11-11).
El grano no va en la imagen: lo pone el shader de js/keyons-rafaga.js, quieto en pantalla.
"""
import argparse
import base64
import io
import os
import re

import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGINA = os.path.join(ROOT, 'fundamentos', 'elementos', 'graficos.html')
W, H = 472, 904  # cartel completo
ANCHO = .8      # de los anchos anotados (borde visible) a la desviación de la campana
CAUCE = 8        # el cauce es 1/8 de la imagen

# Colores de la marca (tokens.css)
NOCHE, PROFUNDO, CIELO, MEDIO, CLARO = '#10122A', '#3D6BAF', '#729BDD', '#8FB4DC', '#C4DBF0'
LAVANDA, SALMON, ATARDECER, ROSA = '#B2BFE5', '#CE635D', '#E99D9E', '#C4658B'
NARANJA, AMBAR, AMARILLO, CREMA, VERDE, ORO = '#E87838', '#F5A742', '#FFCE86', '#FFEBB1', '#D5E0D2', '#FFCE49'
GRIS, NOCHE2, VIOLETA = '#8B8C92', '#324269', '#7D81B9'


def lin(c):
    c = np.asarray(c, dtype=np.float32)
    return np.where(c <= .04045, c / 12.92, ((c + .055) / 1.055) ** 2.4)


def gam(c):
    c = np.clip(c, 0, 1)
    return np.where(c <= .0031308, c * 12.92, 1.055 * c ** (1 / 2.4) - .055)


M1 = np.array([[.4122214708, .5363325363, .0514459929], [.2119034982, .6806995451, .1073969566], [.0883024619, .2817188376, .6299787005]], np.float32)
M2 = np.array([[.2104542553, .793617785, -.0040720468], [1.9779984951, -2.428592205, .4505937099], [.0259040371, .7827717662, -.808675766]], np.float32)
M1I, M2I = np.linalg.inv(M1), np.linalg.inv(M2)


def oklab(rgb):
    return (M2 @ np.cbrt(M1 @ lin(rgb)[..., None]))[..., 0]


def srgb(lab):
    return gam(M1I @ ((M2I @ lab[..., None]) ** 3))[..., 0]


def col(h):
    return oklab(np.array([int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)], np.float32))


def catmull(p, n):
    """Curva suave que pasa por todos los puntos; interpola también los anchos."""
    p = np.array(p, np.float32)
    q = np.vstack([2 * p[0] - p[1], p, 2 * p[-1] - p[-2]])
    seg = len(p) - 1
    u = np.linspace(0, seg, n, dtype=np.float32)
    i = np.minimum(u.astype(int), seg - 1)
    t = (u - i)[:, None]
    a, b, c, d = q[i], q[i + 1], q[i + 2], q[i + 3]
    return .5 * (2 * b + (c - a) * t + (2 * a - 5 * b + 4 * c - d) * t * t + (3 * b - a - 3 * c + d) * t ** 3)


def ruido(rng, w, h, celda):
    """Ruido suave de baja frecuencia para que el borde no parezca dibujado con compás."""
    g = rng.standard_normal((int(h / celda) + 3, int(w / celda) + 3)).astype(np.float32)
    g = np.array(Image.fromarray(g, 'F').resize((w, h), Image.BICUBIC), np.float32)
    return g / max(float(np.abs(g).max()), 1e-6)


def suave(a, lo, hi):
    t = np.clip((a - lo) / (hi - lo), 0, 1)
    return t * t * (3 - 2 * t)


def tabla(colores, n=256):
    """Tabla de color (a lo largo, a lo ancho). Cada parada: (s, borde, medio, centro) o (s, b1, m1, centro, m2, b2)."""
    fil = []
    for p in colores:
        c = p[1:]
        if len(c) == 3:
            c = (c[0], c[1], c[2], c[1], c[0])
        fil.append(np.stack([col(x) for x in c]))
    fil = np.stack(fil)
    s = [p[0] for p in colores]
    u = np.linspace(0, 1, n)
    return np.stack([np.stack([np.interp(u, s, fil[:, k, d]) for d in range(3)], 1) for k in range(5)], 1).astype(np.float32)


def leer(t, s, m):
    """Lee la tabla con s (0-1) y m (-1 a 1), interpolando en los dos sentidos."""
    i = np.clip(s, 0, 1) * (t.shape[0] - 1)
    j = (np.clip(m, -1, 1) + 1) * 2
    i0, j0 = np.minimum(i.astype(int), t.shape[0] - 2), np.minimum(j.astype(int), 3)
    fi, fj = (i - i0)[..., None], (j - j0)[..., None]
    return (t[i0, j0] * (1 - fi) + t[i0 + 1, j0] * fi) * (1 - fj) + (t[i0, j0 + 1] * (1 - fi) + t[i0 + 1, j0 + 1] * fi) * fj


def cinta(xx, yy, esc, c, ancho):
    """Devuelve (alfa, color OKLab, tangente x, tangente y, s, densidad) de una cinta."""
    n = c.get('n', 300)
    sp = catmull([(list(p) + [1.])[:5] for p in c['puntos']], n)
    P, su, sd, pe = sp[:, :2], np.maximum(sp[:, 2], 1) * ancho, np.maximum(sp[:, 3], 1) * ancho, np.clip(sp[:, 4], 0, None)
    T = np.gradient(P, axis=0)
    ds = np.maximum(np.hypot(T[:, 0], T[:, 1]), 1e-3)
    T = T / ds[:, None]
    s = np.cumsum(ds)
    s = (s - s[0]) / max(float(s[-1] - s[0]), 1e-3)
    pe = pe * np.clip(s / .06, 0, 1) ** .5 * np.clip((1 - s) / .06, 0, 1) ** .5
    h, w = xx.shape
    A, S, M, TX, TY = [np.zeros_like(xx) for _ in range(5)]
    for i in range(n):
        r = 3.8 * max(su[i], sd[i]) + 24
        x0, x1 = max(int((P[i, 0] - r) * esc), 0), min(int((P[i, 0] + r) * esc) + 1, w)
        y0, y1 = max(int((P[i, 1] - r) * esc), 0), min(int((P[i, 1] + r) * esc) + 1, h)
        if x0 >= x1 or y0 >= y1:
            continue
        dx, dy = xx[y0:y1, x0:x1] - P[i, 0], yy[y0:y1, x0:x1] - P[i, 1]
        a, b = dx * T[i, 0] + dy * T[i, 1], dy * T[i, 0] - dx * T[i, 1]
        sa = max(c.get('largo', .9) * .5 * (su[i] + sd[i]), 3)
        lado = np.where(b > 0, sd[i], su[i])
        g = pe[i] * (ds[i] / (sa * 2.5066)) * np.exp(-.5 * (a * a / (sa * sa) + b * b / (lado * lado)))
        A[y0:y1, x0:x1] += g
        S[y0:y1, x0:x1] += g * s[i]
        M[y0:y1, x0:x1] += g * (b / (lado * 1.7))
        TX[y0:y1, x0:x1] += g * T[i, 0]
        TY[y0:y1, x0:x1] += g * T[i, 1]
    q = np.maximum(A, 1e-6)
    S, M, TX, TY = S / q, M / q, TX / q, TY / q
    lo, hi = c.get('borde', (.14, .6))
    alfa = suave(A, lo, hi) * c.get('opacidad', 1.)
    return alfa, leer(tabla(c['colores']), S, M), TX, TY, S, A


def esfera(xx, yy, c):
    """Esfera: borde circular nítido y color radial descentrado, que le da volumen."""
    bx, by, rad = c['esfera']
    fx, fy = c.get('foco', (bx - rad * .22, by - rad * .26))
    r = np.hypot(xx - bx, yy - by)
    d = c.get('difumino', 34)
    alfa = 1 - suave(r, rad - d, rad + d)
    u = np.clip(np.hypot(xx - fx, yy - fy) / (rad * 1.28), 0, 1)
    pasos = c['colores']
    lab = np.stack([np.interp(u, [p[0] for p in pasos], [col(p[1])[k] for p in pasos]) for k in range(3)], -1).astype(np.float32)
    q = np.maximum(r, 1e-3)
    return alfa.astype(np.float32), lab, -(yy - by) / q, (xx - bx) / q, np.full_like(r, .5), alfa.astype(np.float32)   # recorrido fijo: sin anillos de brillo


def espiral(cx, cy, r0, vueltas, w0, w1, n=36, inicio=3.7):
    """Puntos de una espiral que entra hacia el centro, para Giro."""
    pts = []
    for i in range(n):
        t = i / (n - 1)
        th = inicio - t * vueltas * 6.2832
        r = r0 * (1 - t) ** .82 + 8
        w = w0 + (w1 - w0) * t
        pts.append((cx + r * np.cos(th), cy + r * np.sin(th) * 1.04, w, w, 1.))
    # La forma completa queda centrada en (cx, cy), no el punto donde nace la espiral
    x0, x1 = min(q[0] - q[2] for q in pts), max(q[0] + q[2] for q in pts)
    y0, y1 = min(q[1] - q[2] for q in pts), max(q[1] + q[2] for q in pts)
    dx, dy = cx - (x0 + x1) / 2, cy - (y0 + y1) / 2
    return [(q[0] + dx, q[1] + dy, q[2], q[3], q[4]) for q in pts]


# Coordenadas sobre 472 × 904. Puntos de una cinta: (x, y, ancho izquierdo, ancho derecho, peso), mirando hacia donde avanza.
RAFAGAS = [
    {'n': 'Flujo', 'seed': 11, 'fase': 'Mediodía', 'dots': [CIELO, MEDIO, CLARO], 'warp': 10, 'capas': [
        dict(puntos=[(-170, 306, 178, 172), (40, 298, 176, 182), (170, 346, 170, 170), (300, 440, 164, 160), (430, 500, 160, 156), (660, 548, 160, 156)],
             colores=[(0, CLARO, MEDIO, CIELO), (1, CLARO, MEDIO, CIELO)], borde=(.015, 1.)),
    ]},
    {'n': 'Estela', 'seed': 22, 'dots': ['#ACC3E7', CIELO, '#496192'], 'warp': 2, 'ancho': .94, 'capas': [
        dict(puntos=[(-130, -110, 16, 16, 0.6), (40, 60, 30, 30, 0.8), (165, 205, 48, 48), (250, 300, 62, 62), (215, 395, 70, 70), (300, 500, 74, 74), (360, 610, 66, 66), (325, 700, 50, 50), (420, 830, 30, 30, 0.8), (600, 1030, 16, 16, 0.6)],
             colores=[(0, '#C6D5EC', '#C6D5EC', '#C6D5EC'), (1, '#C6D5EC', '#C6D5EC', '#C6D5EC')], borde=(.04, .9), opacidad=.5, largo=1.),
        dict(puntos=[(-130, -110, 6, 6), (40, 60, 12, 12), (165, 205, 22, 22), (250, 300, 32, 32), (215, 395, 40, 40), (300, 500, 44, 44), (360, 610, 38, 38), (325, 700, 26, 26), (420, 830, 12, 12), (600, 1030, 6, 6)],
             colores=[(0, '#C6D5EC', '#ACC3E7', '#8FAFE2'), (.5, '#ACC3E7', '#8FAFE2', CIELO), (1, '#C6D5EC', '#ACC3E7', '#8FAFE2')], borde=(.06, .8), largo=1.),
    ]},
    {'n': 'Pulso', 'seed': 33, 'fase': 'Atardecer', 'dots': [ATARDECER, SALMON], 'warp': 1, 'capas': [
        dict(esfera=(236, 410, 176), colores=[(0, ATARDECER), (.46, ATARDECER), (1, SALMON)]),
    ]},
    # Corriente (2026-11-13): tonos claros de la escala Azul Cielo; el oficial #729BDD es el más oscuro
    {'n': 'Corriente', 'seed': 44, 'dots': ['#C6D5EC', '#8FAFE2', CIELO], 'warp': 4, 'ancho': .95, 'capas': [
        dict(puntos=[(120, -100, 96, 98), (130, 80, 88, 102), (165, 210, 80, 94), (235, 320, 74, 92), (306, 392, 56, 80), (352, 446, 40, 62), (340, 512, 42, 56), (272, 566, 50, 58), (206, 628, 54, 56), (206, 706, 52, 52), (262, 796, 52, 52), (342, 906, 54, 54), (410, 1040, 56, 56)],
             colores=[(0, '#C6D5EC', '#ACC3E7', '#ACC3E7', '#C6D5EC', '#E0E7F1'), (.18, '#C6D5EC', '#ACC3E7', '#ACC3E7', '#C6D5EC', '#E0E7F1'), (.33, '#C6D5EC', '#ACC3E7', '#ACC3E7', '#ACC3E7', '#C6D5EC'),
                      (.42, CIELO, '#8FAFE2', '#ACC3E7', '#C6D5EC', '#C6D5EC'), (.49, CIELO, CIELO, '#8FAFE2', '#ACC3E7', '#C6D5EC'), (.6, CIELO, '#8FAFE2', '#8FAFE2', '#C6D5EC', '#ACC3E7'), (.72, '#8FAFE2', '#C6D5EC', '#ACC3E7', '#ACC3E7', '#C6D5EC'), (1, '#C6D5EC', '#ACC3E7', '#ACC3E7', '#ACC3E7', '#C6D5EC')]),
    ]},
    {'n': 'Giro', 'seed': 55, 'dots': [LAVANDA, '#FED8B5', AMARILLO], 'warp': 2, 'capas': [
        dict(puntos=espiral(236, 452, 186, 1.56, 54, 32), colores=[(0, CREMA, AMARILLO, AMARILLO), (1, CREMA, AMARILLO, AMARILLO)], borde=(.05, .75), opacidad=.62),
        dict(puntos=espiral(236, 452, 186, 1.56, 32, 18), colores=[(0, LAVANDA, LAVANDA, CIELO), (.4, LAVANDA, CIELO, CIELO), (.75, LAVANDA, CIELO, PROFUNDO), (1, CIELO, PROFUNDO, PROFUNDO)]),
    ]},
    {'n': 'Ola', 'seed': 66, 'dots': [NOCHE, NOCHE2, GRIS], 'warp': 5, 'capas': [
        dict(puntos=[(286, -80, 112, 122), (276, 80, 122, 122), (222, 240, 110, 104), (234, 350, 92, 92), (286, 470, 76, 82), (304, 550, 74, 78), (262, 650, 60, 62), (266, 770, 26, 26, .6)],
             colores=[(0, GRIS, GRIS, GRIS), (.72, GRIS, GRIS, GRIS), (1, CREMA, CREMA, GRIS)], borde=(.02, 1.), opacidad=.46),
        dict(puntos=[(286, -80, 74, 84), (286, 80, 80, 80), (216, 240, 66, 62), (226, 340, 56, 52), (282, 460, 44, 44), (318, 530, 42, 38), (264, 628, 36, 34), (258, 740, 18, 18, .8), (300, 880, 9, 9, .45)],
             colores=[(0, GRIS, NOCHE2, NOCHE), (.3, GRIS, NOCHE2, NOCHE), (.46, GRIS, NOCHE2, NOCHE2), (.6, GRIS, GRIS, NOCHE2), (.72, GRIS, NOCHE2, NOCHE), (.84, GRIS, GRIS, NOCHE2), (1, CREMA, GRIS, GRIS)], borde=(.05, .7)),
    ]},
]


def componer(r, escala):
    """Devuelve la ráfaga como RGBA de 8 bits (alfa directo) y deja su cauce en r['_cauce']."""
    w, h = int(W * escala), int(H * escala)
    y, x = np.mgrid[0:h, 0:w].astype(np.float32)
    rng = np.random.default_rng(r['seed'])
    amp = r['warp']
    xx = x / escala + amp * ruido(rng, w, h, 110 * escala)
    yy = y / escala + amp * ruido(rng, w, h, 110 * escala)
    alfa = np.zeros((h, w), np.float32)
    lab = np.zeros((h, w, 3), np.float32)
    cx, cy, cs, cp = [np.zeros((h, w), np.float32) for _ in range(4)]
    for c in r['capas']:
        a, l, tx, ty, s, A = esfera(xx, yy, c) if 'esfera' in c else cinta(xx, yy, escala, c, ANCHO * r.get('ancho', 1))
        lab = lab * (1 - a[..., None]) + l * a[..., None]
        alfa = alfa + a * (1 - alfa)
        p = np.clip(A / .08, 0, 1)
        cx += tx * p * (a + .02)
        cy += ty * p * (a + .02)
        cs += s * (a + .02)
        cp += a + .02
    lab = lab / np.maximum(alfa, 1e-4)[..., None]
    out = np.dstack([srgb(lab), alfa])
    mag = np.maximum(cp, 1e-4)
    f = np.dstack([.5 + .5 * np.clip(cx / mag, -1, 1), .5 - .5 * np.clip(cy / mag, -1, 1), np.clip(cs / mag, 0, 1)])   # y hacia arriba
    r['_cauce'] = Image.fromarray((f * 255 + .5).astype(np.uint8), 'RGB').resize((W // CAUCE, H // CAUCE), Image.BILINEAR)
    return (np.clip(out, 0, 1) * 255 + .5).astype(np.uint8)


def puntear(rgba, rng):
    """Vista de la hoja de contacto: el mismo punteado que hace el shader."""
    a = rgba[..., 3].astype(np.float32) / 255
    g = rng.random(a.shape, np.float32)
    s = np.clip((a - g) / .5 + .5, 0, 1) * np.clip(a / .06, 0, 1)
    a2 = a + (s - a) * .2
    fondo = np.array([244, 244, 244], np.float32)
    return (rgba[..., :3] * a2[..., None] + fondo * (1 - a2[..., None])).astype(np.uint8)


def svg(r, webp):
    d = base64.b64encode(webp).decode()
    i = r['n'].lower()
    return ('<svg viewBox="0 0 472 904" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
            f'<defs><filter id="rg-{i}" filterUnits="userSpaceOnUse" x="0" y="0" width="472" height="904">'
            '<feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="2" seed="7"/>'
            '<feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  1.9 0 0 0 -.25"/>'
            '<feComposite in="SourceGraphic" operator="arithmetic" k1=".82" k2=".34"/></filter></defs>'
            f'<image filter="url(#rg-{i})" width="472" height="904" preserveAspectRatio="none" href="data:image/webp;base64,{d}"/></svg>')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hoja')
    ap.add_argument('--escala', type=float, default=1.)
    a = ap.parse_args()
    imgs = {r['n']: componer(r, a.escala) for r in RAFAGAS}
    if a.hoja:
        rng = np.random.default_rng(1)
        w, h = int(W * a.escala), int(H * a.escala)
        sh = Image.new('RGB', (3 * (w + 8), 2 * (h + 8)), 'white')
        for k, r in enumerate(RAFAGAS):
            sh.paste(Image.fromarray(puntear(imgs[r['n']], rng)), ((k % 3) * (w + 8), (k // 3) * (h + 8)))
        sh.save(a.hoja)
        return
    src = open(PAGINA, encoding='utf-8').read()
    figs = re.findall(r'<figure class="rfp".*?</figure>', src, re.S)
    if len(figs) != len(RAFAGAS):
        raise SystemExit(f'Se esperaban {len(RAFAGAS)} ráfagas y hay {len(figs)}')
    por = {re.search(r'rfp__t">([^<]+)<', f).group(1): f for f in figs}
    nuevas = []
    for k, r in enumerate(RAFAGAS, 1):
        b = io.BytesIO()
        Image.fromarray(imgs[r['n']], 'RGBA').save(b, 'WEBP', quality=90, alpha_quality=95, method=6)
        f = por[r['n']]
        f = re.sub(r'<svg.*?</svg>', lambda m: svg(r, b.getvalue()), f, count=1, flags=re.S)
        if r.get('fase'):
            f = re.sub(r'(rfp__t">[^<]+<small>)[^<]*', lambda m: m.group(1) + r['fase'], f, count=1)
        f = re.sub(r'rfp__n">\(\d+/06\)', f'rfp__n">({k:02d}/06)', f)
        f = re.sub(r'(rfp__dots">).*?(</span>)', lambda m: m.group(1) + ''.join(f'<i style="background:{x}"></i>' for x in r['dots']) + m.group(2), f, count=1, flags=re.S)
        f = re.sub(r'<figure class="rfp"[^>]*>', '<figure class="rfp" data-rfp>', f, count=1)
        nuevas.append(f)
    ini, fin = src.index(figs[0]), src.index(figs[-1]) + len(figs[-1])
    src = src[:ini] + ''.join(nuevas) + src[fin:]
    open(PAGINA, 'w', encoding='utf-8', newline='\n').write(src)
    print('Rafagas actualizadas:', ', '.join(r['n'] for r in RAFAGAS))


if __name__ == '__main__':
    main()
