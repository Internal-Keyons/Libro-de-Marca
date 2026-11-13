"""Área Expresión de marca · introducción, capítulo 16 Corporativo y capítulo 17 Expresivo.

Uso:  python tools/expresion.py
Texto: Keylin, 2026-11-13. Escribe la introducción en modos/index.html (<template id="area-intro">),
modos/corporativo.html y modos/expresivo.html, y los ítems del índice de los capítulos 16 y 17 en js/nav-data.js.

Segunda ronda (2026-11-13): los capítulos 16 y 17 se reescribieron en forma directa (pendientes de aprobación de Keylin);
la introducción del área conserva su texto.
Cada sección sigue la entrada en niveles (reglas-visuales R22): título, entrada, apoyo breve y después el desarrollo.
Diagramación con los componentes del libro:
- base: título, entrada (.ed__lead), apoyo (.ed__apoyo), filas con rótulo (.ed__stack), cierre (.ed__close);
- creativa donde ayuda a leer: tarjetas con viñeta (.pgrid + .pgrid__v) para principios, preguntas y recursos; la comparación
  en tres columnas (.tri3) en Intensidad; el espectro (.espectro) en la introducción; la paleta en fila (.paleta5) en Editorial.
Cada párrafo normativo se marca con N(texto, nivel) (tools/normativa.py); después: python tools/niveles.py --aplicar
"""
import html
import io
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
def pgrid(items, dos=True):
    return (f'{I}<div class="pgrid{" pgrid--2" if dos else ""}">' + ''.join(
        f'<div><span class="pgrid__n">{k:02d}</span><p class="pgrid__t">{esc(t)}</p>{P(*ps, cls="pgrid__d")}</div>' for k, (t, ps) in enumerate(items, 1)) + '</div>')
def cierre(*ps): return f'{I}<div class="ed__close">{P(*ps)}</div>'
def apoyo(t): return f'{I}<p class="ed__apoyo">{t}</p>'
C_ = 'M10 0a10 10 0 1 0 0 20a10 10 0 1 0 0-20ZM7.76 6h4.48A1.76 1.76 0 0 1 14 7.76v4.48A1.76 1.76 0 0 1 12.24 14H7.76A1.76 1.76 0 0 1 6 12.24V7.76A1.76 1.76 0 0 1 7.76 6Z'
Q_ = 'M1.1 1.1h17.8v17.8H1.1ZM10 5.55a4.45 4.45 0 1 0 0 8.9a4.45 4.45 0 1 0 0-8.9Z'
def vin(k): return f'<svg viewBox="0 0 20 20" aria-hidden="true"><path fill="currentColor" fill-rule="evenodd" d="{C_ if k % 2 == 0 else Q_}"/></svg>'
def pgrid_v(items):
    """Tarjetas con viñeta (círculo y cuadrado alternados) en lugar de número"""
    return (f'{I}<div class="pgrid pgrid--2">' + ''.join(
        f'<div><span class="pgrid__v">{vin(k)}</span><p class="pgrid__t">{esc(t)}</p>{P(*ps, cls="pgrid__d")}</div>' for k, (t, ps) in enumerate(items)) + '</div>')
def tri3(cols):
    """Comparación en tres columnas: cada columna con su nombre y las mismas filas, alineadas entre columnas"""
    return (f'{I}<div class="tri3">' + ''.join(f'<div><p class="tri3__t">{esc(t)}</p>' + ''.join(f'<div class="tri3__c"><span class="tri3__k">{esc(k)}</span><p>{esc(v)}</p></div>' for k, v in filas) + '</div>'
                                              for t, filas in cols) + '</div>')


def seccion(sid, num, corto, titular, partes):
    return (f'\n    <!-- {num} · {corto} -->\n    <section class="ed" id="{sid}">\n      <div class="ed__label"><span>{num}</span><span>{esc(corto)}</span></div>\n      <div>\n'
            f'{I}<h2 class="ed__title">{esc(titular)}</h2>\n' + '\n'.join(partes) + '\n      </div>\n    </section>\n')


# ───────────── Introducción del área ─────────────
ESPECTRO = (f'{I}<div class="espectro" role="img" aria-label="Espectro continuo de intensidad: Formal, Corporativo Editorial y Expresivo">'
            '<span class="espectro__barra" aria-hidden="true"></span>'
            '<span class="espectro__k">Formal</span><span class="espectro__k">Corporativo Editorial</span><span class="espectro__k">Expresivo</span></div>')
# El titular de la página del área ya es «Una identidad. Distintas intensidades.»: la sección abre con su frase de cierre
INTRO = (seccion('espectro', 'Intro', 'Expresión de marca', 'La identidad permanece. La intensidad cambia.', [
    lead('Keyons tiene una sola identidad visual. Su expresión cambia según lo que necesita comunicar, las personas a quienes se dirige y el entorno en el que aparece.'),
    prosa('Una propuesta institucional puede ser sobria y precisa. Una publicación editorial puede combinar fotografía, color y composiciones inesperadas. Una campaña puede llevar esa libertad todavía más lejos. Las tres pertenecen a la misma marca.',
          'La diferencia no está en utilizar sistemas visuales separados, sino en regular la intensidad con la que se manifiestan sus recursos.'),
    pgrid([('Lo que permanece', ['La tipografía, el sistema cromático, la geometría, los criterios de composición y los principios de claridad constituyen una base compartida. Su aplicación puede variar, pero debe conservar una relación reconocible con la identidad Keyons.',
                                 'La coherencia no exige repetir una misma distribución, un mismo degradado o una misma cantidad de color. Se construye mediante decisiones que responden a una gramática visual común.']),
           ('Lo que varía', ['Pueden cambiar el protagonismo de la fotografía, la intensidad cromática, la escala tipográfica, el ritmo, la presencia de texturas, el movimiento y la libertad de composición.',
                             'Estas variaciones responden al propósito de cada pieza. No se utilizan recursos expresivos para demostrar creatividad, sino porque ayudan a comunicar una idea, construir una atmósfera o generar una experiencia memorable.'])]),
    sub('Un continuo de expresión'),
    lead('Formal, Corporativo Editorial y Expresivo son tres referencias dentro de un mismo continuo.'),
    ESPECTRO,
    prosa('No constituyen estilos cerrados ni categorías excluyentes. Una pieza puede situarse entre dos niveles, adoptar características de ambos o modificar su intensidad entre secciones.',
          'La elección depende de cuatro preguntas: qué se comunica, a quién se dirige, dónde aparecerá y cuánta libertad visual permite su función.'),
    sub('Estructura y expresión'),
    prosa('Keyons combina la disciplina de una estructura clara con la libertad de una expresión visual propia.',
          'La relación 60/40 puede utilizarse como metáfora de ese equilibrio: una base estructural suficientemente sólida para sostener una capa expresiva con personalidad.',
          'No representa una proporción técnica ni obliga a distribuir una composición mediante porcentajes.',
          'El minimalismo y el maximalismo no son identidades opuestas. Son recursos que pueden convivir dentro de una misma pieza. Una fotografía intensa puede ocupar una composición extremadamente sencilla; una página casi monocromática puede conseguir gran expresividad mediante escala, ritmo y espacio.'),
    cierre('La intensidad no se mide por la cantidad de elementos, sino por la fuerza y la pertinencia de las decisiones visuales.'),
]))

# ───────────── Capítulo 16 · Corporativo ─────────────
PALETA = (f'{I}<ul class="paleta5" aria-label="Los cinco colores oficiales">'
          + ''.join(f'<li><i style="background:var({v})"></i><b>{n}</b><span>{d}</span></li>' for v, n, d in [
              ('--k-blanco', 'Blanco Keyons', 'Estructura y contraste'), ('--k-noche', 'Azul Noche', 'Estructura y contraste'),
              ('--k-cielo', 'Azul Cielo', 'Reconocimiento y acento'), ('--k-salmon', 'Salmón Tierra', 'Expresión según el contexto'),
              ('--k-atardecer', 'Salmón Atardecer', 'Variante para composiciones oscuras')]) + '</ul>')
TRI = tri3([('Formal', [('Propósito', 'Informar con exactitud.'), ('Recursos', 'Tipografía, retícula y espacio, con acentos puntuales.'),
                        ('Color', 'Blanco Keyons y Azul Noche, con Azul Cielo para orientar.'), ('Piezas', 'Contratos, políticas, certificaciones e informes técnicos.')]),
            ('Corporativo Editorial', [('Propósito', 'Explicar y convencer.'), ('Recursos', 'Fotografía protagonista, titulares grandes y atmósferas.'),
                                       ('Color', 'Los cinco colores oficiales, cada uno en su función.'), ('Piezas', 'Presentaciones, informes ejecutivos, propuestas y memorias.')]),
            ('Expresivo', [('Propósito', 'Inspirar y construir una experiencia.'), ('Recursos', 'Composición experimental, cielos, texturas y movimiento.'),
                           ('Color', 'Cielos, degradados o monocromía, según la atmósfera.'), ('Piezas', 'Campañas, piezas narrativas y aperturas editoriales.')])])
C16 = [
    ('principios', '16.1', 'Principios', 'Claridad con carácter', [
        lead('La expresión corporativa comunica <strong>profesionalismo, confianza y criterio</strong>.'),
        apoyo('Se apoya en una composición clara, una jerarquía reconocible y un uso deliberado del espacio.'),
        prosa('Abarca dos referencias de intensidad, Formal y Corporativo Editorial, que comparten fundamentos y se combinan según el contenido.'),
        pgrid_v([('La claridad dirige', [N('Cada pieza debe dejar claro qué información importa más y en qué orden se lee.', 'debe'), 'La tipografía, el espacio y la retícula resuelven la jerarquía antes que cualquier recurso decorativo.']),
                 ('La sobriedad es una elección', [N('La expresión corporativa puede usar todos los recursos de la identidad Keyons.', 'puede'), 'Cada pieza elige los que su función necesita, con precisión y equilibrio.']),
                 ('El carácter nace de la composición', ['Keyons se reconoce por la relación entre tipografía, proporción, imagen, color y espacio, sin repetir un motivo gráfico.']),
                 ('La función marca la intensidad', ['Un aviso legal, una propuesta comercial y una memoria corporativa comparten identidad y varían en ritmo, recursos e intensidad.'])]),
    ]),
    ('formal', '16.2', 'Formal', 'Precisión que transmite confianza', [
        lead('Formal es la referencia <strong>más contenida</strong> del sistema.'),
        apoyo('Sirve cuando importan la exactitud, la lectura prolongada o las consecuencias institucionales de la información.'),
        stack([('Color', [N('La composición formal debería partir de fondos claros, texto de alto contraste, Azul Noche y Blanco Keyons, con Azul Cielo para orientar y acentuar.', 'deberia'),
                          N('Otros colores oficiales pueden sumarse cuando hay una razón de comunicación y se conserva la legibilidad.', 'puede')]),
               ('Tipografía y jerarquía', [N('Los títulos deben permitir localizar el contenido de un vistazo, y los párrafos, mantener una medida cómoda.', 'debe'),
                                           N('La tipografía expresiva puede aparecer en portadas y aperturas.', 'puede')]),
               ('Composición', [N('Retículas regulares y márgenes generosos sostienen la lectura. Cada elemento gráfico debe cumplir una función: organizar, separar, destacar o contextualizar.', 'debe')]),
               ('Dónde se usa', ['Contratos, políticas, documentos regulatorios, certificaciones, comunicaciones oficiales e informes técnicos. Un informe también admite el tratamiento editorial cuando el contenido y la audiencia lo permiten.'])]),
    ]),
    ('editorial', '16.3', 'Editorial', 'El rigor también puede ser memorable', [
        lead('Corporativo Editorial suma <strong>libertad compositiva</strong> sin perder precisión.'),
        apoyo('Admite fotografía protagonista, titulares de mayor escala y un uso más amplio del color.'),
        stack([('Dónde se usa', ['Presentaciones corporativas, informes ejecutivos, publicaciones de marca, propuestas y memorias.']),
               ('Composición y ritmo', [N('La retícula sigue siendo la base y admite variaciones de escala, alineación y ocupación. Cada cambio de ritmo debe facilitar la lectura.', 'debe')]),
               ('Espacio', [N('Los espacios blancos tienen valor compositivo y no deben llenarse solo para equilibrar la cantidad de contenido.', 'no-debe')])]),
        sub('Los cinco colores'),
        prosa(N('Corporativo Editorial puede usar los cinco colores oficiales, cada uno en su función.', 'puede')),
        PALETA,
        prosa(N('La pieza debe conservar jerarquía, equilibrio y contraste suficiente, aunque el color tenga gran presencia.', 'debe'),
              N('Salmón Atardecer debe reservarse para composiciones oscuras.', 'debe')),
        stack([('Fotografía y atmósfera', [N('Cada fotografía debe aportar significado, contexto o una perspectiva reconocible.', 'debe'),
                                           N('Cielos, degradados y texturas pueden acompañarla cuando construyen una atmósfera.', 'puede')]),
               ('Reconocimiento', [N('Una pieza editorial debe reconocerse como Keyons por su tipografía, su diagramación y sus proporciones, sin depender del logotipo.', 'debe')])]),
    ]),
    ('intensidad', '16.4', 'Intensidad', 'Elegir cuánto expresar', [
        lead('La intensidad <strong>se ajusta durante el diseño</strong>, según la función de la pieza.'),
        apoyo('La precisión y la lectura extensa piden menos competencia visual. Una visión o un proyecto admiten más fotografía, color y composición.'),
        TRI,
        sub('Cuatro preguntas para decidir'),
        pgrid_v([('Propósito', ['Informar, explicar, convencer, documentar o inspirar.']), ('Audiencia', ['Conocimientos, expectativas y necesidades de lectura.']),
                 ('Canal', ['Documento, pantalla, presentación, publicación o soporte físico.']), ('Contenido', ['Volumen, complejidad, importancia y sensibilidad de la información.'])]),
        stack([('Una pieza, varias intensidades', [N('Una propuesta puede abrir con una portada de alto impacto, argumentar en páginas editoriales y cerrar con condiciones formales.', 'puede'),
                                                   N('Las transiciones deben conservar continuidad tipográfica, cromática y compositiva.', 'debe')]),
               ('Intensidad y densidad', [N('La intensidad mide el protagonismo de los recursos de identidad; la densidad, la cantidad y organización de la información. Cada una debe regularse por separado.', 'debe')])]),
    ]),
    ('documentos', '16.5', 'Documentos', 'El documento como expresión de marca', [
        lead('Un documento Keyons es <strong>una herramienta clara y confiable</strong> con identidad propia.'),
        apoyo('La estructura da continuidad. La intensidad cambia la presentación, nunca la información.'),
        stack([('Formato', [N('El formato debe responder al destino del documento: impresión, lectura digital, distribución o edición.', 'debe')]),
               ('Márgenes y retícula', [N('Márgenes y retícula deben tomarse de las especificaciones de cada formato y repetir sus posiciones de una página a otra.', 'debe')]),
               ('Tipografía', [N('Títulos, cuerpo, notas y cifras deben usar el sistema tipográfico oficial, con relaciones constantes de tamaño, peso e interlineado.', 'debe')]),
               ('Portada', [N('La portada debe mostrar el título, el emisor y los datos de identificación. Su intensidad, formal o editorial, depende del contenido y la audiencia.', 'debe')]),
               ('Encabezado y pie', [N('Encabezado y pie deberían llevar solo la información recurrente útil: identidad, título breve, versión o página.', 'deberia')]),
               ('Títulos y numeración', [N('La jerarquía debe distinguir capítulos, secciones y apartados sin depender solo del tamaño o del color. La numeración se usa cuando facilita referencias o auditorías.', 'debe')]),
               ('Tablas y cifras', [N('Las cifras deben alinearse de forma constante y mostrar sus unidades. El color ayuda a leer, pero nunca es la única diferencia.', 'debe')]),
               ('Gráficos', [N('Los gráficos deben seguir las <a href="../fundamentos/datos/graficos.html">normas de datos y visualización</a> de Keyons, fuente única de sus paletas.', 'debe')]),
               ('Notas y citas', [N('Notas y referencias deben encontrarse con facilidad, sin competir con el texto principal.', 'debe')]),
               ('Firmas', [N('Cada bloque de firma debe mostrar quién firma, con qué función y bajo qué procedimiento. La firma visual y la firma con validez jurídica son elementos distintos.', 'debe')]),
               ('Sellos', [N('Sellos y marcas de agua deben corresponder a una certificación o aprobación real y conservar la legibilidad.', 'debe')])]),
        cierre('Una pieza corporativa Keyons no necesita elegir entre rigor y personalidad.', 'Su calidad está en saber cuánto protagonismo dar a cada uno.'),
    ]),
]

C17 = [
    ('principios', '17.1', 'Principios', 'Libertad con intención', [
        lead('La expresión de Keyons puede ser <strong>intensa, sensible y memorable</strong> sin perder claridad.'),
        apoyo('Su fuerza nace de la relación entre forma, contenido y emoción, más que de la cantidad de recursos.'),
        pgrid_v([('Una identidad que permite explorar', [N('La experimentación debe conservar una relación visible con la tipografía, el color, la geometría y la composición de Keyons.', 'debe')]),
                 ('La intensidad no es saturación', [N('Cada composición debe elegir un protagonista y los elementos que lo acompañan.', 'debe'), 'Reunir todos los recursos a la vez genera competencia visual.']),
                 ('La emoción tiene una función', [N('Cada recurso expresivo debe transmitir una idea, una atmósfera o una experiencia ligada al contenido.', 'debe')]),
                 ('La claridad permanece', [N('La información esencial debe seguir siendo fácil de encontrar, con contraste y jerarquía suficientes.', 'debe')])]),
    ]),
    ('composicion', '17.2', 'Composición', 'Una retícula que permite explorar', [
        lead('La retícula es <strong>una herramienta</strong>, no una plantilla.'),
        apoyo('Admite simetría, asimetría controlada o una organización editorial experimental.'),
        stack([('Protagonista', [N('Cada composición debería tener un centro de atención reconocible: una fotografía, una frase, una cifra o una relación espacial.', 'deberia')]),
               ('Espacio', ['El espacio libre crea contraste, pausa y expectativa. Pocos elementos bien elegidos suelen recordarse más que muchos.']),
               ('Asimetría', [N('La asimetría puede generar movimiento o tensión, siempre con un equilibrio perceptible.', 'puede')]),
               ('Composición propia', [N('Cada pieza debe tener decisiones visuales propias de su contenido. Cambiar solo la foto y el título de una composición genérica tampoco es dirección creativa.', 'debe')])]),
    ]),
    ('tipografia', '17.3', 'Tipografía', 'La letra también expresa', [
        lead('La tipografía <strong>también narra</strong>.'),
        apoyo('Escala, peso, alineación y ritmo construyen personalidad con las familias oficiales.'),
        stack([('Dónde se expresa', [N('Los tratamientos expresivos deberían concentrarse en títulos, aperturas y mensajes breves.', 'deberia')]),
               ('Lectura continua', [N('Los textos de lectura continua deben mantener legibilidad, contraste y espaciado adecuados.', 'debe')]),
               ('Tipografía como firma', [N('Tipografía y diagramación pueden bastar para que una pieza se reconozca como Keyons, sin otros recursos.', 'puede')])]),
    ]),
    ('color', '17.4', 'Color y cielos', 'El color construye atmósfera', [
        lead('El sistema cromático permite <strong>piezas contenidas e intensas</strong>.'),
        apoyo('La intensidad no exige toda la paleta: una pieza monocromática también puede ser expresiva.'),
        stack([('Cielos', [N('Los cielos deben responder a la intención de la pieza y a sus normas de construcción. Su función es atmosférica: categorías, resultados y estados usan otros colores.', 'debe')]),
               ('Degradados', [N('Los degradados deben verse como transiciones naturales, sin cortes ni saltos que afecten el contraste del texto.', 'debe'),
                               N('Su posición, extensión y dirección pueden adaptarse a cada soporte.', 'puede')]),
               ('Color con propósito', [N('El color expresivo, el color de datos y el color semántico deben mantenerse separados. Un color de marca nunca indica por sí solo éxito, advertencia o error.', 'debe')])]),
    ]),
    ('recursos', '17.5', 'Recursos', 'Cada recurso con un propósito', [
        lead('Cada recurso entra <strong>cuando ayuda a comunicar</strong>.'),
        apoyo('Fotografía, ilustración, texturas y movimiento suman carácter; la decisión siempre es humana.'),
        pgrid_v([('Fotografía', [N('La fotografía puede asumir el protagonismo de una composición.', 'puede'), N('Su selección debe responder a una intención narrativa, con calidad, autenticidad y pertinencia.', 'debe')]),
                 ('Ilustración e imágenes sintéticas', [N('Su dirección artística debe partir de criterio humano, originalidad y respeto de derechos.', 'debe'), N('Una imagen sintética no debe presentarse como fotografía documental de un hecho real.', 'no-debe')]),
                 ('Texturas y tramas', [N('Las texturas deben ceder ante textos, cifras y elementos esenciales: si compiten, se reducen o se retiran.', 'debe')]),
                 ('Movimiento', [N('El contenido debe comprenderse sin la animación, y el movimiento, respetar las preferencias de accesibilidad.', 'debe')]),
                 ('Firma humana', ['La expresión Keyons nace de decisiones deliberadas: selección, composición, edición y evaluación.', 'La tecnología amplía las posibilidades; el criterio decide cuáles usar.'])]),
    ]),
    ('limites', '17.6', 'Límites', 'La libertad no elimina la responsabilidad', [
        lead(N('Toda pieza expresiva debe conservar contraste, accesibilidad, comprensión y reconocimiento de marca.', 'debe')),
        apoyo('La intensidad visual nunca justifica ocultar información o dificultar una acción.'),
        stack([('Recursos opcionales', ['Fotografía, texturas, cielos, degradados y movimiento son opcionales. Las proporciones de color sirven como punto de partida; la calidad se juzga por el resultado y el contexto.']),
               ('Expresión propia', [N('Las decisiones gráficas deben ser propias de Keyons. Sumar tendencias y efectos de moda tampoco sustituye una dirección creativa.', 'debe')]),
               ('Cada contexto', [N('Una campaña puede ser muy experimental; un formulario de uso frecuente pide estabilidad y previsibilidad.', 'puede')])]),
        cierre('Keyons no necesita verse siempre igual para ser reconocible.', 'La creatividad no consiste en añadir más. Consiste en encontrar la forma que mejor comunica lo que importa.'),
    ]),
]


def pagina(archivo, n, titulo, portal, secciones):
    S = ''.join(seccion(*x) for x in secciones)
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titulo} · Expresión · Manual de marca · Keyons</title>
<link rel="icon" href="../assets/logos/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/libro.css">
<link rel="stylesheet" href="../css/marca.css">
</head>
<body class="is-area" data-root=".." data-area="modos" data-page="modos/{archivo}">
<!-- Generado por tools/expresion.py: el texto se cambia ahí -->

<header id="topbar"></header>

<div class="doc">
  <aside class="side" id="side" aria-label="Capítulos de Expresión"></aside>

  <main class="content chapter">
    <nav class="crumbs" aria-label="Ruta">
      <a href="../inicio.html">Inicio</a>
      <svg viewBox="0 0 16 16" aria-hidden="true"><path d="m6 3.5 4.5 4.5L6 12.5"/></svg>
      <a href="index.html">Expresión</a>
      <svg viewBox="0 0 16 16" aria-hidden="true"><path d="m6 3.5 4.5 4.5L6 12.5"/></svg>
      <span>{n} {titulo}</span>
    </nav>

    <section class="portal portal--salmon" aria-label="{n} · {titulo}">
      <div class="portal__arcs" aria-hidden="true"></div>
      <div class="portal__txt">
        <span class="kicker">Capítulo {n} · Expresión</span>
        <h1 class="t-display">{titulo}</h1>
        <p>{portal}</p>
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


def escribir(p, s):
    io.open(os.path.join(ROOT, p), 'w', encoding='utf-8', newline='\n').write(s)


escribir('modos/corporativo.html', pagina('corporativo.html', '16', 'Corporativo', 'Claridad con carácter.', C16))
escribir('modos/expresivo.html', pagina('expresivo.html', '17', 'Expresivo', 'Libertad con intención.', C17))

# Introducción del área en modos/index.html
p = os.path.join(ROOT, 'modos', 'index.html')
s = io.open(p, encoding='utf-8').read()
s = re.sub(r'\n?<template id="area-intro">.*?</template>\n?', '\n', s, flags=re.S)
s = s.replace('<div id="area-page"></div>', '<div id="area-page"></div>\n    <template id="area-intro">' + INTRO + '    </template>', 1)
io.open(p, 'w', encoding='utf-8', newline='\n').write(s)

# Índice: los ítems de 16 y 17 enlazan a sus secciones
nav = os.path.join(ROOT, 'js', 'nav-data.js')
s = io.open(nav, encoding='utf-8').read()
def items(archivo, secs):
    return ', '.join(f"{{ t: '{corto}', s: 'b', href: 'modos/{archivo}#{sid}' }}" for sid, num, corto, *_ in secs)
s = re.sub(r"(\{ n: '16', k: 'corporativo',[^\n]*?)s: '[pbv]'(, d: '[^']*', items: \[)\n.*?\] \},",
           lambda m: m.group(1) + "s: 'b'" + m.group(2) + '\n        ' + items('corporativo.html', C16) + ' ] },', s, count=1, flags=re.S)
s = re.sub(r"(\{ n: '17', k: 'expresivo',[^\n]*?)s: '[pbv]'(, d: '[^']*', items: \[)\n.*?\] \}",
           lambda m: m.group(1) + "s: 'b'" + m.group(2) + '\n        ' + items('expresivo.html', C17) + ' ] }', s, count=1, flags=re.S)
io.open(nav, 'w', encoding='utf-8', newline='\n').write(s)
print('ok · 16:', len(C16), 'secciones · 17:', len(C17), 'secciones')

registrar('modos/corporativo.html')
registrar('modos/expresivo.html')
