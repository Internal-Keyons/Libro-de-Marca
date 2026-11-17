"""Capítulo 18 · Digital (área Aplicaciones): la identidad visual de Keyons en pantalla.

Uso:  python tools/digital.py
Escribe aplicaciones/digital.html y los ítems del capítulo 18 en js/nav-data.js; registra los niveles (tools/normativa.py).
Después: python tools/normas.py · python tools/niveles.py --aplicar · python tools/biblioteca.py

Propuesta de texto del 2026-11-17, pendiente de aprobación de Keylin (ella pidió que Claude redacte y ella apruebe).
Solo texto y componentes del libro: sin maquetas de interfaz hasta que exista la hoja de componentes aprobada (CLAUDE.md).
Lo que ya regula otra norma se cita con enlace (R17): los tipos de producto son de Personalización (PER-001 a PER-004),
los grados de presencia de Estela son de EST-005, su voz y trato de EST-003 y EST-004, el color en pantalla de COL-012.
Cada sección abre con título, una sola entrada y su composición (R22).
"""
import html
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normativa import N, registrar   # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
esc = lambda t: html.escape(t, quote=False)
I = '        '


def P(*ps, cls=''):
    c = f' class="{cls}"' if cls else ''
    return ''.join(f'<p{c}>{p}</p>' for p in ps)


def lead(t): return f'{I}<p class="ed__lead">{t}</p>'
def prosa(*ps): return f'{I}<div class="prosa">{P(*ps)}</div>'
def sub(t): return f'{I}<h3 class="ed__sub">{esc(t)}</h3>'
def stack(filas): return f'{I}<div class="ed__stack">' + ''.join(f'<div><span class="paren">({esc(k)})</span>{P(*ps)}</div>' for k, ps in filas) + '</div>'
def matriz(etq, cols, filas):
    """Tabla editorial del libro (.matrix): una fila por situación y una columna por condición"""
    head = ('<div class="matrix__row matrix__head" role="row"><span class="matrix__k" role="columnheader"></span>'
            + ''.join(f'<span class="matrix__lvl" role="columnheader">{esc(t)}<small>{esc(s)}</small></span>' for t, s in cols) + '</div>')
    rows = ''.join(f'<div class="matrix__row" role="row"><span class="matrix__k" role="rowheader">{esc(k)}</span>'
                   + ''.join(f'<span class="matrix__v" role="cell">{esc(v)}</span>' for v in vs) + '</div>' for k, vs in filas)
    return f'{I}<div class="matrix" role="table" aria-label="{esc(etq)}">{head}{rows}</div>'


_NORMAS = {v['id']: (k, v['t']) for k, v in json.load(io.open(os.path.join(ROOT, 'data', 'normas.json'), encoding='utf-8')).items()}
def xref(nid, texto=None):
    ruta, t = _NORMAS[nid]
    return f'<a class="xref" href="../{ruta}" title="{nid}">{esc(texto or t)}</a>'


def seccion(sid, num, corto, titular, partes):
    return (f'\n    <!-- {num} · {corto} -->\n    <section class="ed" id="{sid}">\n      <div class="ed__label"><span>{num}</span><span>{esc(corto)}</span></div>\n      <div>\n'
            f'{I}<h2 class="ed__title">{esc(titular)}</h2>\n' + '\n'.join(partes) + '\n      </div>\n    </section>\n')


C18 = [
    ('sobriedad', '18.1', 'Sobriedad viva', 'La identidad se reconoce en la estructura', [
        lead('En una interfaz de uso frecuente, Keyons se expresa con <strong>tipografía, estructura, espacio y color funcional</strong>, al servicio de la tarea.'),
        stack([('Prioridad', [N('Cada superficie operativa debe priorizar claridad, navegación, jerarquía y concentración.', 'debe')]),
               ('Recursos de identidad', ['La tipografía oficial, la retícula, el espacio y unos pocos detalles visuales hacen reconocible la experiencia.',
                                          'La marca se reconoce sin fotografías, texturas ni degradados en cada pantalla.']),
               ('Color', [f'El color en pantalla sigue la norma {xref("KYN-MRK-COL-012")}: cada color comunica una función.']),
               ('Detalles', [N('Los detalles expresivos deberían ser pocos y precisos: una ventana de cielo en un encabezado, un acento de color o una transición breve.', 'deberia')])]),
        sub('Ejemplo de aplicación'),
        lead('Un tablero de un producto SaaS de Keyons, descrito por <strong>lo que hace reconocible la marca</strong> en cada zona.'),
        stack([('Encabezado', ['Logotipo, navegación principal y búsqueda sobre Blanco Keyons, con el texto en Azul Noche.']),
               ('Indicadores', ['Cifras en Plus Jakarta Sans con cifras tabulares, y gráficos con la paleta de datos y sus leyendas.']),
               ('Acción principal', ['Una sola acción destacada por vista, en el color de acción del sistema.']),
               ('Momento vivo', ['La bienvenida al iniciar la semana muestra un cielo de mediodía detrás del saludo; el resto de la vista conserva la sobriedad.'])]),
    ]),
    ('momentos', '18.2', 'Momentos vivos', 'La intensidad sube cuando ayuda a comprender', [
        lead('Algunas experiencias admiten <strong>mayor libertad gráfica</strong>: bienvenidas, presentaciones de producto, descubrimientos y relatos.'),
        matriz('Cuándo sube la intensidad y cuándo se contiene, según el momento',
               [('Sube la intensidad', 'Los recursos expresivos ganan protagonismo'), ('Se contiene', 'Tipografía, espacio y color funcional')],
               [('Bienvenida', ['En la primera entrada o al comenzar un ciclo de trabajo.', 'Cuando la persona vuelve a una tarea en curso.']),
                ('Introducción a un producto', ['Al presentar qué hace y para quién.', 'Cuando la persona ya lo conoce y busca una función.']),
                ('Descubrimiento', ['Al revelar una capacidad nueva, una sola vez.', 'Cuando el aviso se repite o interrumpe una tarea.']),
                ('Presentación de capacidades', ['En una página o un recorrido dedicados.', 'Dentro de un flujo de trabajo.']),
                ('Estado vacío', ['Cuando orienta el primer paso de un espacio nuevo.', 'Cuando falta un dato o una búsqueda queda sin resultados.']),
                ('Experiencia narrativa', ['En relatos, informes editoriales y aperturas.', 'Cuando el relato acompaña datos que se comparan.'])]),
        prosa(N('Cada recurso expresivo en pantalla debe ayudar a comprender, orientar o comunicar.', 'debe'),
              N('Un momento vivo no debe competir con una acción importante ni convertir una pantalla de trabajo en una pieza publicitaria.', 'no-debe')),
    ]),
    ('producto', '18.3', 'Según el producto', 'Cada producto muestra la marca que le corresponde', [
        lead('La identidad visible cambia con el <strong>modelo de cada producto</strong>; la calidad de la experiencia es la misma en los tres.'),
        stack([('Keyons Product Default', [f'Usa la identidad predeterminada de Keyons, con el acento del cliente en las zonas que define {xref("KYN-MRK-PER-002")}.']),
               ('Producto personalizado', [f'La interfaz adopta la marca contratante; la firma Keyons queda en la construcción, según {xref("KYN-MRK-PER-003")}.']),
               ('Proyecto sin firma', [f'La solución prescinde de logotipos y colores Keyons, como define {xref("KYN-MRK-PER-004")}. Su calidad se reconoce en la claridad, la coherencia y la resolución de la experiencia.'])]),
    ]),
    ('estela', '18.4', 'Estela en pantalla', 'La presencia de Estela cambia con el contexto', [
        lead(f'Estela aparece en pantalla con <strong>distintos grados de presencia</strong>, según {xref("KYN-MRK-EST-005")}; su voz y su trato son los de {xref("KYN-MRK-EST-003")}.'),
        matriz('Presencia visual de Estela según el contexto',
               [('Presencia', 'Cómo se ve Estela'), ('Ejemplo', 'Dónde ocurre')],
               [('Experiencia dedicada', ['Protagonista: su identidad visual ocupa la composición.', 'La presentación de Estela o su bienvenida.']),
                ('Asistencia contextual', ['Discreta: una señal pequeña junto a la tarea.', 'Una sugerencia al completar un informe.']),
                ('Capacidad de IA', ['Sin figura: la función se presenta por lo que hace.', 'Un resumen automático o la clasificación de documentos.']),
                ('Producto de cliente', ['Sin la identidad pública de Keyons.', 'Un asistente con el nombre y la marca del cliente.'])]),
        prosa(N('Una capacidad de IA puede presentarse sin representar a Estela.', 'puede'),
              N('En un producto de cliente, Estela no debe mostrarse con la identidad pública de Keyons.', 'no-debe')),
    ]),
]


def pagina(secciones):
    S = ''.join(seccion(*x) for x in secciones)
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Digital · Aplicaciones · Manual de marca · Keyons</title>
<link rel="icon" href="../assets/logos/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/libro.css">
<link rel="stylesheet" href="../css/marca.css">
</head>
<body class="is-area" data-root=".." data-area="aplicaciones" data-page="aplicaciones/digital.html">
<!-- Generado por tools/digital.py: el texto se cambia ahí -->

<header id="topbar"></header>

<div class="doc">
  <aside class="side" id="side" aria-label="Capítulos de Aplicaciones"></aside>

  <main class="content chapter">
    <nav class="crumbs" aria-label="Ruta">
      <a href="../inicio.html">Inicio</a>
      <svg viewBox="0 0 16 16" aria-hidden="true"><path d="m6 3.5 4.5 4.5L6 12.5"/></svg>
      <a href="index.html">Aplicaciones</a>
      <svg viewBox="0 0 16 16" aria-hidden="true"><path d="m6 3.5 4.5 4.5L6 12.5"/></svg>
      <span>18 Digital</span>
    </nav>

    <section class="portal portal--salmon portal--atardecer" aria-label="18 Digital">
      <div class="portal__arcs" aria-hidden="true"></div>
      <div class="portal__txt">
        <span class="kicker">Capítulo 18 · Aplicaciones</span>
        <h1 class="t-display">Digital</h1>
        <p>La identidad de Keyons en pantalla: sobria, con momentos vivos.</p>
      </div>
    </section>
{S}
    <nav id="pager" aria-label="Paginación"></nav>
  </main>
</div>

<script src="../js/nav-data.js"></script>
<script src="../js/libro.js"></script>
</body>
</html>
'''


io.open(os.path.join(ROOT, 'aplicaciones', 'digital.html'), 'w', encoding='utf-8', newline='\n').write(pagina(C18))

# Índice: los ítems de 18 enlazan a sus secciones; «Íconos de aplicación» sigue por definir
nav = os.path.join(ROOT, 'js', 'nav-data.js')
s = io.open(nav, encoding='utf-8').read()
its = ', '.join(f"{{ t: '{corto}', s: 'b', href: 'aplicaciones/digital.html#{sid}' }}" for sid, num, corto, *_ in C18) + ", { t: 'Íconos de aplicación' }"
s, n = re.subn(r"(\{ n: '18', k: 'digital',[^\n]*?)s: '[pbv]'(, d: '[^']*', items: \[)\n.*?\] \},",
               lambda m: m.group(1) + "s: 'b'" + m.group(2) + '\n        ' + its + ' ] },', s, count=1, flags=re.S)
assert n == 1, 'capítulo 18 no encontrado en nav-data.js'
io.open(nav, 'w', encoding='utf-8', newline='\n').write(s)
print('ok · 18:', len(C18), 'secciones')

registrar('aplicaciones/digital.html')
