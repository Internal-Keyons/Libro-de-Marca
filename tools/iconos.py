"""Íconos de interfaz: del PDF del diseñador al catálogo (recursos/iconos.html).

Uso:  python tools/iconos.py "C:/ruta/Iconos pagina web.pdf"

Cada página del PDF es un ícono. El script toma solo los de SPECS, los lleva a la
retícula de 10.1 (lienzo 32, área viva 28, trazo 2,5, terminaciones rectas, uniones
en ángulo) y los agrega al catálogo. Los que necesitaron ajuste quedan marcados
con el punto Salmón (is-rev) hasta que se aprueben.
También escribe _tmp/iconos/revision.html: original junto al ajustado.
"""
import base64
import math
import os
import re
import sys

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = sys.argv[1] if len(sys.argv) > 1 else r'C:\Users\a120s\Downloads\Iconos pagina  web.pdf'
W = 2.5          # trazo de la familia
CHECK = [(8.81, 16.83), (13.45, 21.47), (22.53, 11.04)]   # el check del ícono check (40)
CIRC = 11.14     # radio del círculo guía en los íconos sólidos (eje del trazo)

# num de página: (nombre, categoría, operación, nota de ajuste o None si entra tal cual)
SPECS = {
    8: ('flecha-derecha-solido', 'nav', 'solid', None),
    9: ('flecha-abajo-solido', 'nav', 'solid', None),
    53: ('flecha-arriba-solido', 'nav', 'solid', None),
    54: ('flecha-izquierda-solido', 'nav', 'solid', None),
    59: ('flecha-abajo-izquierda-solido', 'nav', 'solid-std', 'El círculo medía 24,4 px; ahora es el mismo de los demás sólidos, dibujado con cuatro curvas, y la flecha quedó centrada.'),
    105: ('flecha-abajo-derecha-solido', 'nav', 'solid-std', 'El círculo medía 24,4 px; ahora es el mismo de los demás sólidos, dibujado con cuatro curvas, y la flecha quedó centrada.'),
    10: ('inicio', 'nav', ('fit', 28, 28), 'Los aleros salían del área viva (1,4 a 30,6 px); se redujo al 95 %.'),
    36: ('check-solido', 'acc', 'solid-check', 'El check es el mismo del ícono check, en el mismo tamaño y con las mismas uniones. El círculo tenía trazo de 2,58.'),
    39: ('mas-solido', 'acc', 'solid', None),
    42: ('cerrar-solido', 'acc', 'solid', None),
    68: ('menos-solido', 'acc', 'solid', None),
    79: ('ajustes', 'acc', None, 'Las perillas tenían un contorno de 1 px; ahora son rellenas, mismo tamaño.'),
    17: ('nube-descarga', 'acc', 'cloud-down', 'Venía en lienzo ancho de 43 px; la nube se llevó a 26 × 20 px. La flecha es la de la familia (flecha-abajo), en el tamaño que ya usan carpeta-descarga y documento-descarga.'),
    44: ('circulo-solido', 'est', 'solid', None),
    47: ('sector', 'est', 'sector', 'Las líneas medían 2,35 y estaban corridas 1,2 px del centro; se centraron con trazo de 2,5.'),
    #15: ('interruptor-solido', 'est', 'toggle-solid', 'Lienzo ancho de 43 px y trazo de 2,38; quedó en 23 px de ancho con trazo de 2,5.'),
    #16: ('interruptor', 'est', 'toggle', 'Lienzo ancho de 43 px y trazo de 2,38; quedó en 23 px de ancho con trazo de 2,5.'),
    120: ('ayuda', 'est', None, None),
    123: ('advertencia', 'est', None, None),
    122: ('chat-texto', 'com', None, None),
    61: ('lista', 'edi', 'list', 'Medía 25,4 px de ancho y quedó en 22. Los puntos tenían un contorno de 0,96 px; ahora son rellenos, mismo tamaño.'),
    62: ('lista-cuadros', 'edi', 'list-sq', 'Medía 25,4 px de ancho y quedó en 22. Las líneas tenían terminación redonda y pasaron a recta; los cuadros perdieron su contorno de 0,96 px.'),
    121: ('capas-agregar', 'edi', None, None),
    70: ('dividir-solido', 'dat', 'solid', None),
    14: ('nube', 'obj', ('fit', 26, 20), 'Venía en lienzo ancho de 43 px; se llevó al rectángulo de 26 × 20 px.'),
    18: ('fuego', 'obj', None, 'La llama interior tenía un contorno de 0,48 px; quedó solo el relleno. Las puntas llevan corte recto (unión biselada), como en el original.'),
    27: ('calendario', 'obj', 'calendar', 'Medía 25,2 px de ancho y quedó en 22. Conserva el 31, convertido en trazado.'),
    29: ('estrella', 'obj', 'star', 'Tamaño original. Su grosor real era 2,8; el hueco se recalculó para dar 2,5 exactos.'),
    34: ('edificio', 'obj', 'building', 'Medía 26,8 px de ancho y quedó en 23. Trazo de 2,56; pasó a 2,5. La puerta es la misma de inicio: 5,2 px de ancho y esquinas de 0,75.'),
    #124: ('portapapeles-lista', 'arc', 'clip-list', 'Los checks tenían trazo de 1,5 px: a 2,5 tres filas no caben, quedaron dos filas con el check de la familia. El contorno tenía terminaciones redondas.'),
}

# Íconos cuyas puntas van cortadas en recto, como en el original
BISEL = {18}

# Íconos que vienen de otro PDF: num → (archivo, página)
SRC = {124: (r'C:\Users\a120s\Downloads\Icono.pdf', 1)}

# Fuera del catálogo y por qué (se informa, no se dibuja)
FUERA = {
    20: 'cohete: familia ilustrativa', 26: 'varita: familia ilustrativa', 28: 'flor: familia ilustrativa',
    32: 'caja con estrella: familia ilustrativa', 35: 'planta: familia ilustrativa',
    30: 'corazón de píxeles: otro estilo de dibujo', 33: 'balanza: eliminada',
    15: 'interruptor sólido: eliminado, no se lee como parte de la familia', 16: 'interruptor: eliminado, no se lee como parte de la familia',
    124: 'portapapeles con lista (Icono.pdf): eliminado',
    50: 'SOON: es texto, va como etiqueta de interfaz', 51: 'NEW: es texto, va como etiqueta de interfaz',
    82: 'traducir: son letras', 95: 'igual a chat (89)', 108: 'igual a carpeta (100)',
}

# Orden dentro de cada categoría: familias juntas, el contorno antes que el relleno
ORDEN = {
    'nav': 'flecha-derecha flecha-izquierda flecha-arriba flecha-abajo flecha-diagonal flecha-derecha-larga chevron-derecha flecha-giro deshacer '
           'flecha-derecha-solido flecha-izquierda-solido flecha-arriba-solido flecha-abajo-solido flecha-abajo-izquierda-solido flecha-abajo-derecha-solido '
           'inicio navegar entrar salir abrir-externo contraer',
    'acc': 'mas mas-solido menos menos-solido check check-solido cerrar cerrar-solido mas-opciones buscar ajustes descargar nube-descarga duplicar marcador enviar',
    'est': 'informacion ayuda advertencia verificado circulo circulo-solido sector progreso-25 mitad progreso-50 interruptor interruptor-solido '
           'alarma alarma-agregar alarma-quitar alarma-check',
    'com': 'correo arroba chat chat-texto chat-agregar chat-check chat-alerta chat-cerrar chat-notificacion cita microfono microfono-apagado',
    'arc': 'carpeta carpeta-agregar carpeta-check carpeta-buscar carpeta-descarga carpeta-bloqueada portapapeles portapapeles-lista portapapeles-check '
           'portapapeles-descarga documento documento-texto documento-agregar documento-check documento-buscar documento-descarga documento-favorito clip',
    'edi': 'formas seleccion capas capas-agregar lista lista-cuadros',
    'dat': 'tendencia porcentaje igual diferente dividir dividir-solido',
    'obj': 'favorito-circulo estrella fuego asterisco brujula globo nube calendario camara movil edificio cono',
}


def n(v):
    s = f'{v:.2f}'.rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def pt(p):
    return (p.x, p.y) if hasattr(p, 'x') else p


def path_d(items, T, close=False):
    out, cur, start = [], None, None
    for it in items:
        k = it[0]
        if k == 're':
            r = it[1]
            a = [T((r.x0, r.y0)), T((r.x1, r.y0)), T((r.x1, r.y1)), T((r.x0, r.y1))]
            out.append('M%s %sL%s %sL%s %sL%s %sZ' % tuple(n(c) for p in a for c in p))
            cur = None
            continue
        if k == 'qu':
            q = it[1]
            a = [T(pt(q.ul)), T(pt(q.ur)), T(pt(q.lr)), T(pt(q.ll))]
            out.append('M%s %sL%s %sL%s %sL%s %sZ' % tuple(n(c) for p in a for c in p))
            cur = None
            continue
        ps = [T(pt(p)) for p in it[1:]]
        if cur is None or abs(cur[0] - ps[0][0]) > .01 or abs(cur[1] - ps[0][1]) > .01:
            if same(cur, start) and out:
                out.append('Z')                         # el trazo vuelve a su inicio: se cierra y la esquina se une en ángulo
            out.append('M%s %s' % (n(ps[0][0]), n(ps[0][1])))
            start = ps[0]
        if k == 'l':
            out.append('L%s %s' % (n(ps[1][0]), n(ps[1][1])))
        else:
            out.append('C' + ' '.join('%s %s' % (n(x), n(y)) for x, y in ps[1:]))
        cur = ps[-1]
    if (close or same(cur, start)) and out and out[-1] != 'Z':
        out.append('Z')
    return ''.join(out)


def same(a, b):
    return a is not None and b is not None and abs(a[0] - b[0]) < .02 and abs(a[1] - b[1]) < .02


def poly_d(pts):
    return 'M' + 'L'.join('%s %s' % (n(x), n(y)) for x, y in pts) + 'Z'


def circ_d(cx, cy, r):
    k = r * .5523
    return ('M%s %sC%s %s %s %s %s %sC%s %s %s %s %s %sC%s %s %s %s %s %sC%s %s %s %s %s %sZ' % tuple(n(v) for v in (
        cx + r, cy, cx + r, cy + k, cx + k, cy + r, cx, cy + r,
        cx - k, cy + r, cx - r, cy + k, cx - r, cy,
        cx - r, cy - k, cx - k, cy - r, cx, cy - r,
        cx + k, cy - r, cx + r, cy - k, cx + r, cy)))


def stroke(d, cap='square'):
    return (f'<path d="{d}" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="{cap}" '
            f'stroke-linejoin="miter" stroke-miterlimit="4" pathLength="1"/>')


def fill(d, eo=False):
    return f'<path d="{d}" fill="currentColor"{" fill-rule=\"evenodd\"" if eo else ""}/>'


# --- geometría auxiliar -------------------------------------------------------

def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def add(a, b): return (a[0] + b[0], a[1] + b[1])
def mul(a, k): return (a[0] * k, a[1] * k)
def unit(a):
    L = math.hypot(*a)
    return (a[0] / L, a[1] / L)
def nrm(u): return (-u[1], u[0])


def meet(p, u, q, v):
    """Intersección de las rectas p+t·u y q+s·v."""
    den = u[0] * v[1] - u[1] * v[0]
    if abs(den) < 1e-9:
        return p
    t = ((q[0] - p[0]) * v[1] - (q[1] - p[1]) * v[0]) / den
    return add(p, mul(u, t))


def outline(pts, cap):
    """Contorno de una polilínea de trazo W: terminaciones rectas, uniones en ángulo."""
    h = W / 2
    P = list(pts)
    if cap == 'square':
        P[0] = add(P[0], mul(unit(sub(P[0], P[1])), h))
        P[-1] = add(P[-1], mul(unit(sub(P[-1], P[-2])), h))
    U = [unit(sub(P[i + 1], P[i])) for i in range(len(P) - 1)]
    L, R = [], []
    for side, acc in ((1, L), (-1, R)):
        acc.append(add(P[0], mul(nrm(U[0]), h * side)))
        for i in range(1, len(P) - 1):
            a = add(P[i], mul(nrm(U[i - 1]), h * side))
            b = add(P[i], mul(nrm(U[i]), h * side))
            acc.append(meet(a, U[i - 1], b, U[i]))
        acc.append(add(P[-1], mul(nrm(U[-1]), h * side)))
    return L + R[::-1]


def outline_round(pts, cap):
    """Como outline, pero con la unión redonda del ícono check."""
    h = W / 2
    P = list(pts)
    if cap == 'square':
        P[0] = add(P[0], mul(unit(sub(P[0], P[1])), h))
        P[-1] = add(P[-1], mul(unit(sub(P[-1], P[-2])), h))
    U = [unit(sub(P[i + 1], P[i])) for i in range(len(P) - 1)]
    sides = {}
    for side in (1, -1):
        seq = [(add(P[0], mul(nrm(U[0]), h * side)), None)]
        for i in range(1, len(P) - 1):
            a = add(P[i], mul(nrm(U[i - 1]), h * side))
            b = add(P[i], mul(nrm(U[i]), h * side))
            turn = U[i - 1][0] * U[i][1] - U[i - 1][1] * U[i][0]
            if turn * side < 0:                         # lado exterior del giro: arco
                seq += [(a, None), (b, P[i])]
            else:
                seq.append((meet(a, U[i - 1], b, U[i]), None))
        seq.append((add(P[-1], mul(nrm(U[-1]), h * side)), None))
        sides[side] = seq
    L, R = sides[1], sides[-1]
    Rr = [(R[k][0], R[k + 1][1] if k + 1 < len(R) else None) for k in range(len(R) - 1, -1, -1)]
    seq = L + Rr
    out = 'M%s %s' % (n(seq[0][0][0]), n(seq[0][0][1]))
    prev = seq[0][0]
    for p, c in seq[1:]:
        if c is None:
            out += 'L%s %s' % (n(p[0]), n(p[1]))
        else:
            a, b = sub(prev, c), sub(p, c)
            sw = 1 if a[0] * b[1] - a[1] * b[0] > 0 else 0
            out += 'A%s %s 0 0 %d %s %s' % (n(h), n(h), sw, n(p[0]), n(p[1]))
        prev = p
    return out + 'Z'


def cross(l1, l2, cap):
    """Contorno de dos trazos que se cruzan (más, cerrar) como una sola figura."""
    h = W / 2
    o = meet(l1[0], unit(sub(l1[1], l1[0])), l2[0], unit(sub(l2[1], l2[0])))
    arms = []
    for e in (l1[0], l1[1], l2[0], l2[1]):
        u = unit(sub(e, o))
        arms.append((math.atan2(u[1], u[0]), e, u))
    arms.sort()
    out = []
    for i, (_, e, u) in enumerate(arms):
        e2 = add(e, mul(u, h)) if cap == 'square' else e
        nn = nrm(u)
        out += [sub(e2, mul(nn, h)), add(e2, mul(nn, h))]
        _, _, v = arms[(i + 1) % 4]
        out.append(meet(add(o, mul(nn, h)), u, sub(o, mul(nrm(v), h)), v))
    return out


def is_circle(d):
    r = d['rect']
    its = [it for it in d['items'] if not (it[0] == 'l' and pt(it[1]) == pt(it[2]))]   # sin rectas de largo cero
    return all(it[0] == 'c' for it in its) and len(its) >= 4 and abs(r.width - r.height) < .3


def cap_of(d):
    c = d.get('lineCap') or (0,)
    return 'butt' if c[0] == 0 else 'square'


def white(c):
    return c is not None and min(c) > .9


def lines_of(d):
    """Polilíneas (listas de puntos) de un dibujo hecho solo de rectas."""
    out, cur = [], None
    for it in d['items']:
        if it[0] != 'l':
            return None
        a, b = pt(it[1]), pt(it[2])
        if cur and abs(cur[-1][0] - a[0]) < .01 and abs(cur[-1][1] - a[1]) < .01:
            cur.append(b)
        else:
            cur = [a, b]
            out.append(cur)
    return out


# --- construcción ----------------------------------------------------------------

def build_solid(page, std, check=False):
    ds = page.get_drawings()
    ring = next(d for d in ds if d['type'] == 'fs' and is_circle(d) and not white(d.get('fill')))
    r = ring['rect']
    cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
    rad = (r.width / 2 if not std else CIRC) + W / 2
    dx, dy = (0, 0)
    if std:                                             # la flecha, centrada en el círculo
        fs = [d['rect'] for d in ds if d['type'] == 'f' and white(d.get('fill'))]
        dx = 16 - (min(r.x0 for r in fs) + max(r.x1 for r in fs)) / 2
        dy = 16 - (min(r.y0 for r in fs) + max(r.y1 for r in fs)) / 2
    T = lambda p: (p[0] + dx, p[1] + dy)
    if std:
        cx, cy = 16, 16
    parts = [circ_d(cx, cy, rad)]
    wl = []
    for d in ds:
        if d is ring:
            continue
        if d['type'] == 'f' and white(d.get('fill')):
            parts.append(path_d(d['items'], T, True))
        elif d['type'] == 's' and white(d.get('color')):
            for pl in lines_of(d):
                wl.append(([T(p) for p in pl], cap_of(d)))
    if check:
        parts.append(outline_round(CHECK, 'square'))
    elif len(wl) == 2 and all(len(p) == 2 for p, _ in wl):
        parts.append(poly_d(cross(wl[0][0], wl[1][0], wl[0][1])))
    else:
        parts += [poly_d(outline(p, c)) for p, c in wl]
    return [fill(''.join(parts), eo=True)]


def bbox(ds, T):
    xs, ys = [], []
    for d in ds:
        r = d['rect']
        e = W / 2 if 's' in d['type'] and (d.get('width') or 0) > 2 else 0
        for x, y in ((r.x0, r.y0), (r.x1, r.y1)):
            X, Y = T((x, y))
            xs += [X - e, X + e]
            ys += [Y - e, Y + e]
    return min(xs), min(ys), max(xs), max(ys)


def fit_T(ds, bw, bh):
    """Escala y centra el dibujo en una caja de bw × bh; el trazo no escala."""
    r0 = [d['rect'] for d in ds]
    cx = (min(r.x0 for r in r0) + max(r.x1 for r in r0)) / 2
    cy = (min(r.y0 for r in r0) + max(r.y1 for r in r0)) / 2
    lo, hi = .3, 1.0
    for _ in range(40):
        s = (lo + hi) / 2
        x0, y0, x1, y1 = bbox(ds, lambda p: ((p[0] - cx) * s, (p[1] - cy) * s))
        if x1 - x0 <= bw and y1 - y0 <= bh:
            lo = s
        else:
            hi = s
    s = lo
    x0, y0, x1, y1 = bbox(ds, lambda p: ((p[0] - cx) * s, (p[1] - cy) * s))
    ox, oy = 16 - (x0 + x1) / 2, 16 - (y0 + y1) / 2
    return lambda p: ((p[0] - cx) * s + ox, (p[1] - cy) * s + oy), s


def build_generic(ds, T):
    out = []
    for d in ds:
        t, w = d['type'], d.get('width') or 0
        r = d['rect']
        if t == 'f' and (r.width < .05 or r.height < .05):
            continue                                    # relleno vacío de una línea
        if t == 's' or (t == 'fs' and w >= 2 and lines_of(d) and (r.width < .05 or r.height < .05)):
            out.append(stroke(path_d(d['items'], T, d.get('closePath')), cap_of(d)))
        elif t == 'f':
            out.append(fill(path_d(d['items'], T, True)))
        elif t == 'fs':
            if is_circle(d):                            # perilla o punto: relleno del mismo tamaño
                (x0, y0), (x1, y1) = T((r.x0, r.y0)), T((r.x1, r.y1))
                out.append(fill(circ_d((x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2 + w / 2)))
            elif d['items'][0][0] == 're':
                (x0, y0), (x1, y1) = T((r.x0 - w / 2, r.y0 - w / 2)), T((r.x1 + w / 2, r.y1 + w / 2))
                out.append(fill(poly_d([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])))
            else:
                out.append(fill(path_d(d['items'], T, True)))
    return out


def build_toggle(solid, ancho=23):
    s = (ancho - W) / 30.2
    H = 17 * s
    R = H / 2
    x0, x1 = 16 - (ancho - W) / 2, 16 + (ancho - W) / 2
    kr = R - W / 2 - 1.11 * s                          # perilla: el mismo aire que el original, a escala
    if solid:
        Ro = R + W / 2
        pill = 'M%s %sH%sA%s %s 0 0 1 %s %sH%sA%s %s 0 0 1 %s %sZ' % (
            n(x0 - W / 2 + Ro), n(16 - Ro), n(x1 + W / 2 - Ro), n(Ro), n(Ro), n(x1 + W / 2 - Ro), n(16 + Ro),
            n(x0 - W / 2 + Ro), n(Ro), n(Ro), n(x0 - W / 2 + Ro), n(16 - Ro))
        return [fill(pill + circ_d(x0 + R, 16, kr), eo=True)]
    pill = 'M%s %sH%sA%s %s 0 0 1 %s %sH%sA%s %s 0 0 1 %s %sZ' % (
        n(x0 + R), n(16 - R), n(x1 - R), n(R), n(R), n(x1 - R), n(16 + R), n(x0 + R), n(R), n(R), n(x0 + R), n(16 - R))
    return [stroke(pill), fill(circ_d(x1 - R, 16, kr))]


def build_cloud_down(page, doc):
    ds = [d for d in page.get_drawings() if d['type'] == 's']
    arrow = next(d for d in doc[101].get_drawings() if d['type'] == 'f')   # flecha de carpeta-descarga
    ar = arrow['rect']
    for k in range(400):
        s = .76 - k * .001
        cx, cy = 21.48, 14.7
        T0 = lambda p: ((p[0] - cx) * s, (p[1] - cy) * s)
        top = T0((0, 17.39))[1]                         # la flecha arranca donde arrancaba la original
        A0 = lambda p: (p[0] - (ar.x0 + ar.x1) / 2, p[1] - ar.y0 + top)
        x0, y0, x1, y1 = bbox(ds, T0)
        (ax0, ay0), (ax1, ay1) = A0((ar.x0, ar.y0)), A0((ar.x1, ar.y1))
        X0, Y0, X1, Y1 = min(x0, ax0), min(y0, ay0), max(x1, ax1), max(y1, ay1)
        if X1 - X0 <= 26 and Y1 - Y0 <= 20:
            break
    ox, oy = 16 - (X0 + X1) / 2, 16 - (Y0 + Y1) / 2
    T = lambda p: (T0(p)[0] + ox, T0(p)[1] + oy)
    A = lambda p: (A0(p)[0] + ox, A0(p)[1] + oy)
    out = [stroke(path_d(d['items'], T), 'butt') for d in ds]
    out.append(fill(path_d(arrow['items'], A, True)))
    return out


def build_list(page, squares, ancho=22):
    ds = page.get_drawings()
    rows = sorted({round(d['rect'].y0, 1) for d in ds if d['type'] in ('s', 'fs') and d['rect'].height < .05})
    b = 2.42 + .96                                      # punto o cuadro, con su antiguo contorno incluido
    x0 = 16 - ancho / 2
    out = []
    for y in rows:
        out.append(stroke('M%s %sL%s %s' % (n(x0 + b + 2.25 + W / 2), n(y), n(x0 + ancho - W / 2), n(y))))
        if squares:
            out.append(fill(poly_d([(x0, y - b / 2), (x0 + b, y - b / 2), (x0 + b, y + b / 2), (x0, y + b / 2)])))
        else:
            out.append(fill(circ_d(x0 + b / 2, y, b / 2)))
    return out


def glyphs(page, T):
    """El texto de la página (el 31 del calendario) convertido en trazado."""
    svg = page.get_svg_image(text_as_path=True)
    defs = dict(re.findall(r'<path id="([^"]+)" d="([^"]+)"', svg))
    out = ''
    for ref, a, b, c, d, e, f in re.findall(r'<use[^>]*xlink:href="#([^"]+)" transform="matrix\(([^,]+),([^,]+),([^,]+),([^,]+),([^,]+),([^)]+)\)"', svg):
        a, b, c, d, e, f = map(float, (a, b, c, d, e, f))
        G = lambda x, y: T((a * x + c * y + e, b * x + d * y + f))
        tok = re.findall(r'[A-Za-z]|-?\d*\.?\d+(?:e-?\d+)?', defs[ref])
        i, cmd, x, y = 0, None, 0.0, 0.0
        while i < len(tok):
            if tok[i].isalpha():
                cmd = tok[i]
                i += 1
                if cmd == 'Z':
                    out += 'Z'
                    continue
            if cmd in ('M', 'L'):
                x, y = float(tok[i]), float(tok[i + 1]); i += 2
                out += cmd + '%s %s' % tuple(n(v) for v in G(x, y))
            elif cmd == 'H':
                x = float(tok[i]); i += 1
                out += 'L%s %s' % tuple(n(v) for v in G(x, y))
            elif cmd == 'V':
                y = float(tok[i]); i += 1
                out += 'L%s %s' % tuple(n(v) for v in G(x, y))
            elif cmd == 'C':
                ps = [(float(tok[i + k]), float(tok[i + k + 1])) for k in (0, 2, 4)]; i += 6
                x, y = ps[-1]
                out += 'C' + ' '.join('%s %s' % tuple(n(v) for v in G(*q)) for q in ps)
            else:
                i += 1
    return out


def build_building(page):
    ds = page.get_drawings()
    T, s = fit_T(ds, 23, 28)
    out = []
    for d in ds:
        if any(it[0] == 'c' for it in d['items']):     # el cuerpo con la puerta: puerta de inicio
            x0, x1, y0, yb = 8.95, 23.05, 4.84, 27.14
            hw, r, top = 2.6 / s, .75 / s, 21.65
            dl, dr = 16 - hw, 16 + hw
            pts = 'M%s %sL%s %sL%s %sL%s %sL%s %sL%s %sL%s %sC%s %s %s %s %s %sL%s %sC%s %s %s %s %s %sL%s %sZ'
            P = [(dr, yb), (x1, yb), (x1, y0), (x0, y0), (x0, yb), (dl, yb), (dl, top + r),
                 (dl, top + r * .45), (dl + r * .45, top), (dl + r, top), (dr - r, top),
                 (dr - r * .45, top), (dr, top + r * .45), (dr, top + r), (dr, yb)]
            out.append(stroke(pts % tuple(n(v) for q in P for v in T(q)), 'butt'))
        else:
            out.append(stroke(path_d(d['items'], T, d.get('closePath')), cap_of(d)))
    return out


def build_clip_list(page):
    ds = page.get_drawings()
    out = []
    for d in ds:
        if d['type'] == 'f':
            out.append(fill(path_d(d['items'], lambda p: p, True)))
        elif d['type'] == 's' and (d.get('width') or 0) > 2.4 and d['rect'].height > 1:
            out.append(stroke(path_d(d['items'], lambda p: p), 'square'))
    k = .38
    for y in (14.3, 21.3):
        out.append(stroke('M10.4 %sL14 %s' % (n(y), n(y)), 'butt'))
        p = [(16 + (x - 8.81) * k, y + .24 + (yy - 16.83) * k) for x, yy in CHECK]
        out.append(stroke(poly_d(p)[:-1], 'square').replace('stroke-linejoin="miter"', 'stroke-linejoin="round"'))
    return out


def build_star(page):
    d = next(x for x in page.get_drawings() if x['type'] == 'f')
    P = [pt(it[1]) for it in d['items']]
    k = 1
    c = ((min(p[0] for p in P) + max(p[0] for p in P)) / 2, (min(p[1] for p in P) + max(p[1] for p in P)) / 2)
    P = [(16 + (p[0] - c[0]) * k, 16 + (p[1] - c[1]) * k) for p in P]
    area = sum(P[i][0] * P[(i + 1) % len(P)][1] - P[(i + 1) % len(P)][0] * P[i][1] for i in range(len(P))) / 2
    inward = 1 if area > 0 else -1
    edges = []
    L = sorted(math.hypot(*sub(P[(i + 1) % len(P)], P[i])) for i in range(len(P)))
    corte = L[-10]                                      # las diez aristas largas; los biseles de las puntas no
    for i in range(len(P)):
        a, b = P[i], P[(i + 1) % len(P)]
        if math.hypot(*sub(b, a)) >= corte:
            u = unit(sub(b, a))
            edges.append((add(a, mul(nrm(u), W * inward)), u))
    hole = [meet(edges[i][0], edges[i][1], edges[(i + 1) % len(edges)][0], edges[(i + 1) % len(edges)][1]) for i in range(len(edges))]
    return [fill(poly_d(P) + poly_d(hole), eo=True)]


def build_sector(page):
    c = next(d for d in page.get_drawings() if d['type'] == 's' and is_circle(d))
    I = lambda p: p
    return [stroke(path_d(c['items'], I), 'butt'), stroke('M16 %sL16 16L%s 16' % (n(c['rect'].y0), n(c['rect'].x1)), 'butt')]


def build(doc, num):
    name, cat, op, note = SPECS[num]
    page = pymupdf.open(SRC[num][0])[SRC[num][1] - 1] if num in SRC else doc[num - 1]
    ds = page.get_drawings()
    if op in ('solid', 'solid-std', 'solid-check'):
        els = build_solid(page, op == 'solid-std', op == 'solid-check')
    elif op in ('list', 'list-sq'):
        els = build_list(page, op == 'list-sq')
    elif op == 'calendar':
        T, _ = fit_T(ds, 22, 28)
        els = build_generic(ds, T) + [fill(glyphs(page, T))]
    elif op == 'building':
        els = build_building(page)
    elif op == 'clip-list':
        els = build_clip_list(page)
    elif op == 'toggle' or op == 'toggle-solid':
        els = build_toggle(op == 'toggle-solid')
    elif op == 'cloud-down':
        els = build_cloud_down(page, doc)
    elif op == 'star':
        els = build_star(page)
    elif op == 'sector':
        els = build_sector(page)
    elif isinstance(op, tuple):
        T, _ = fit_T(ds, op[1], op[2])
        els = build_generic(ds, T)
    else:
        els = build_generic(ds, lambda p: p)
    if num in BISEL:
        els = [e.replace('stroke-linejoin="miter"', 'stroke-linejoin="bevel"') for e in els]
    return '<svg class="ic" viewBox="0 0 32 32" aria-hidden="true">' + ''.join(els) + '</svg>'


# --- verificación: lo dibujado cabe en el área viva --------------------------------

def check(svg):
    import numpy as np
    s = svg.replace('class="ic"', 'xmlns="http://www.w3.org/2000/svg" width="32" height="32"').replace('currentColor', '#000')
    pg = pymupdf.open(stream=s.encode(), filetype='svg')[0]
    pix = pg.get_pixmap(matrix=pymupdf.Matrix(8, 8), alpha=False, colorspace=pymupdf.csGRAY)
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width) < 128
    ys, xs = np.nonzero(a)
    return xs.min() / 8, ys.min() / 8, (xs.max() + 1) / 8, (ys.max() + 1) / 8


def main():
    doc = pymupdf.open(PDF)
    svgs = {num: build(doc, num) for num in SPECS}
    for num, svg in svgs.items():
        b = check(svg)
        flag = '' if b[0] >= 1.9 and b[1] >= 1.9 and b[2] <= 30.1 and b[3] <= 30.1 else '  FUERA DEL ÁREA VIVA'
        print(f'{num:>4} {SPECS[num][0]:<30} {b[0]:5.2f} {b[1]:5.2f} {b[2]:5.2f} {b[3]:5.2f}{flag}')

    # Catálogo
    P = os.path.join(ROOT, 'recursos', 'iconos.html')
    s = open(P, encoding='utf-8').read()
    g0 = s.index('<div class="icat__grid">') + len('<div class="icat__grid">')
    g1 = s.index('</div>', g0)
    grid = s[g0:g1]
    heads = re.findall(r'<p class="icat__h" data-cat="(\w+)">([^<]*)<span>\d+</span></p>', grid)
    tiles = re.findall(r'<button class="ict[^"]*" type="button" data-n="([^"]+)" data-cat="(\w+)" data-num="(\d+)".*?</button>', grid, re.S)
    raw = {m.group(3): m.group(0) for m in re.finditer(r'<button class="ict[^"]*" type="button" data-n="([^"]+)" data-cat="(\w+)" data-num="(\d+)".*?</button>', grid, re.S)}
    groups = {c: [raw[num] for _, cc, num in tiles if cc == c and int(num) not in SPECS and int(num) not in FUERA] for c, _ in heads}
    for num in sorted(SPECS):
        name, cat, op, note = SPECS[num]
        cls = 'ict is-rev' if note else 'ict'
        t = (f'<button class="{cls}" type="button" data-n="{name}" data-cat="{cat}" data-num="{num}" title="{name}">'
             f'{svgs[num]}<span>{name}</span></button>')
        g = groups[cat]
        base = name[:-len('-solido')] if name.endswith('-solido') else None
        k = next((i for i, x in enumerate(g) if base and f'data-n="{base}"' in x), None)
        if k is None:
            g.append(t)
        else:
            j = k + 1
            while j < len(g) and '-solido"' in g[j]:
                j += 1
            g.insert(j, t)
    for c in groups:
        rank = {nm: i for i, nm in enumerate(ORDEN.get(c, '').split())}
        groups[c].sort(key=lambda t: rank.get(re.search(r'data-n="([^"]+)"', t).group(1), 999))
    new = ''.join(f'<p class="icat__h" data-cat="{c}">{lab}<span>{len(groups[c])}</span></p>' + ''.join(groups[c]) for c, lab in heads)
    total = sum(len(v) for v in groups.values())
    s = s[:g0] + new + s[g1:]
    s = re.sub(r'<span class="icat__count">\d+ íconos</span>', f'<span class="icat__count">{total} íconos</span>', s)
    if 'class="icat__rev"' not in s:
        s = s.replace('<p class="icat__file"></p>', '<p class="icat__file"></p>\n              <p class="icat__rev" hidden>Ajustado a la retícula · pendiente de revisión</p>')
    open(P, 'w', encoding='utf-8').write(s)
    print('catálogo:', total, 'íconos')

    # Hoja de revisión: original del PDF junto al ajustado
    rows = []
    for num in sorted(SPECS, key=lambda k: (SPECS[k][3] is None, k)):
        name, cat, op, note = SPECS[num]
        if not note:
            continue
        srcp = pymupdf.open(SRC[num][0])[SRC[num][1] - 1] if num in SRC else doc[num - 1]
        pix = srcp.get_pixmap(matrix=pymupdf.Matrix(4, 4), alpha=True)
        png = base64.b64encode(pix.tobytes('png')).decode()
        wide = srcp.rect.width > 33
        rows.append(f'<div class="r"><div class="c"><img src="data:image/png;base64,{png}" style="height:128px;width:auto" alt=""></div>'
                    f'<div class="c g">{svgs[num].replace("class=\"ic\"", "class=\"ic\" width=\"128\" height=\"128\"")}</div>'
                    f'<div class="t"><b>{num} · {name}</b><p>{note}</p>{"<small>Original en lienzo ancho de 43 × 32 px</small>" if wide else ""}</div></div>')
    out = ['<!doctype html><html lang="es"><meta charset="utf-8"><title>Íconos ajustados</title><style>',
           'body{margin:0;padding:40px;font:15px/1.5 "Plus Jakarta Sans",system-ui,sans-serif;color:#10122A;background:#F4F4F4}',
           'h1{font-size:24px;font-weight:500;margin:0 0 6px}.s{color:#6B6D7E;margin:0 0 32px}',
           '.r{display:grid;grid-template-columns:auto 160px 1fr;gap:24px;align-items:center;padding:16px 0;border-top:1px solid #E0E1E5}',
           '.c{min-width:160px;height:160px;display:grid;place-items:center;background:#fff}',
           '.g{background:#fff linear-gradient(#729BDD33,#729BDD33) 16px 16px/128px 128px no-repeat;background-image:linear-gradient(#fff,#fff),linear-gradient(#729BDD55,#729BDD55);background-size:112px 112px,128px 128px;background-position:24px 24px,16px 16px;background-repeat:no-repeat}',
           '.t p{margin:4px 0 0;max-width:56ch}.t small{color:#6B6D7E}',
           '.k{display:flex;gap:24px;margin:0 0 24px;font-size:13px;color:#6B6D7E}</style>',
           '<h1>Íconos ajustados a la retícula</h1><p class="s">Izquierda: original del PDF. Centro: ajustado; el marco celeste es el margen de 2 px y lo blanco es el área viva de 28 × 28.</p>',
           ''.join(rows), '<h2 style="font-size:18px;font-weight:500;margin:40px 0 8px">Fuera del catálogo</h2><ul>',
           ''.join(f'<li>{k} · {v}</li>' for k, v in sorted(FUERA.items())), '</ul></html>']
    R = os.path.join(ROOT, '_tmp', 'iconos', 'revision.html')
    os.makedirs(os.path.dirname(R), exist_ok=True)
    open(R, 'w', encoding='utf-8').write(''.join(out))
    print('revisión:', R)


if __name__ == '__main__':
    main()
