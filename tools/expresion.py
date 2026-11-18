"""Área Expresión de marca · introducción, capítulo 16 Corporativo y capítulo 17 Expresivo.

Uso:  python tools/expresion.py
Texto: Keylin, 2026-11-13. Escribe modos/corporativo.html y modos/expresivo.html, y los ítems del índice de los capítulos 16 y 17 en js/nav-data.js.

Segunda ronda (2026-11-13): los capítulos 16 y 17 se reescribieron en forma directa (pendientes de aprobación de Keylin);
la introducción del área conserva su texto.
Tercera ronda (2026-11-13): la página del área queda con su título, una entrada breve y los accesos a los capítulos;
su contenido pasa a 16.4 Intensidad (lo que permanece y varía, el continuo) y a 17.1 Principios (estructura y expresión).
Cada sección abre como el resto del libro (reglas-visuales R22): título, una sola entrada y la composición principal.
Diagramación con los componentes del libro:
- base: título, entrada (.ed__lead), filas con rótulo (.ed__stack), cierre (.ed__close);
- creativa donde ayuda a leer: tarjetas con viñeta (.pgrid + .pgrid__v) para principios, preguntas y recursos; la comparación
  en tres columnas (.tri3) y el espectro (.espectro) en Intensidad; la paleta en fila (.paleta5) en Editorial.
Cuarta ronda (2026-11-17): 16.4 con la línea de intensidad (.espectro con marcas y flecha), la tabla «Lo que permanece
y lo que varía» (.matrix), las cuatro preguntas reales con íconos oficiales (.pgrid--ico, tools/iconos_oficiales.py) y
«Los niveles pueden convivir»; 17.1 con íconos; 16.5 cita con enlace lo que ya regulan TYP, ESP y DAT.
Quinta ronda (2026-11-17): 16.4 vuelve a la imagen 1 (barra Azul Cielo lisa, tres nombres y Propósito, Recursos, Color y
Piezas) y abre con «La identidad permanece. La intensidad cambia.», que deja la página del área; las cuatro preguntas
van numeradas como CMP-004; 16.1 con íconos del catálogo aprobado.
Sexta ronda (2026-11-17): marcadores según reglas-visuales R26 (16.1 y 17.1 con viñetas, 17.5 con íconos, 16.4 con números);
16.4 sin barra ni nombres sueltos, solo las tres columnas.
Cada párrafo normativo se marca con N(texto, nivel) (tools/normativa.py); después: python tools/niveles.py --aplicar
"""
import html
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normativa import N, registrar   # noqa: E402
from iconos_oficiales import icono   # noqa: E402
import json   # noqa: E402

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
    """Tarjetas numeradas (como CMP-004): (título, párrafos) o (título, párrafos, orientación en Azul Noche)"""
    return (f'{I}<div class="pgrid{" pgrid--2" if dos else ""}">' + ''.join(
        f'<div><span class="pgrid__n">{k:02d}</span><p class="pgrid__t">{esc(it[0])}</p>{P(*it[1], cls="pgrid__d")}'
        + (f'<p class="pgrid__d pgrid__o">{it[2]}</p>' if len(it) > 2 and it[2] else '') + '</div>' for k, it in enumerate(items, 1)) + '</div>')
def cierre(*ps): return f'{I}<div class="ed__close">{P(*ps)}</div>'
C_ = 'M10 0a10 10 0 1 0 0 20a10 10 0 1 0 0-20ZM7.76 6h4.48A1.76 1.76 0 0 1 14 7.76v4.48A1.76 1.76 0 0 1 12.24 14H7.76A1.76 1.76 0 0 1 6 12.24V7.76A1.76 1.76 0 0 1 7.76 6Z'
Q_ = 'M1.1 1.1h17.8v17.8H1.1ZM10 5.55a4.45 4.45 0 1 0 0 8.9a4.45 4.45 0 1 0 0-8.9Z'
def vin(k): return f'<svg viewBox="0 0 20 20" aria-hidden="true"><path fill="currentColor" fill-rule="evenodd" d="{C_ if k % 2 == 0 else Q_}"/></svg>'
def pgrid_v(items):
    """Tarjetas con viñeta (círculo y cuadrado alternados). Con un número impar, la última fila conserva su posición vacía (R23)."""
    vacia = '<div class="pgrid__vacia" aria-hidden="true"></div>' if len(items) % 2 else ''
    return (f'{I}<div class="pgrid pgrid--2">' + ''.join(
        f'<div><span class="pgrid__v">{vin(k)}</span><p class="pgrid__t">{esc(t)}</p>{P(*ps, cls="pgrid__d")}</div>' for k, (t, ps) in enumerate(items)) + vacia + '</div>')
def pgrid_i(items):
    """Tarjetas con ícono oficial (capítulo 26) en lugar de viñeta: (ícono, título, párrafos, orientación o None).
    La orientación cierra la tarjeta en Azul Noche. Con un número impar, la posición vacía de R23."""
    vacia = '<div class="pgrid__vacia" aria-hidden="true"></div>' if len(items) % 2 else ''
    return (f'{I}<div class="pgrid pgrid--2 pgrid--ico">' + ''.join(
        f'<div><span class="pgrid__ic">{icono(ic)}</span><p class="pgrid__t">{esc(t)}</p>{P(*ps, cls="pgrid__d")}'
        + (f'<p class="pgrid__d pgrid__o">{o}</p>' if o else '') + '</div>' for ic, t, ps, o in items) + vacia + '</div>')
def matriz(etq, cols, filas):
    """Tabla editorial del libro (.matrix): una fila por tema y una columna por condición, alineadas"""
    head = ('<div class="matrix__row matrix__head" role="row"><span class="matrix__k" role="columnheader"></span>'
            + ''.join(f'<span class="matrix__lvl" role="columnheader">{esc(t)}<small>{esc(s)}</small></span>' for t, s in cols) + '</div>')
    rows = ''.join(f'<div class="matrix__row" role="row"><span class="matrix__k" role="rowheader">{esc(k)}</span>'
                   + ''.join(f'<span class="matrix__v" role="cell">{esc(v)}</span>' for v in vs) + '</div>' for k, vs in filas)
    return f'{I}<div class="matrix" role="table" aria-label="{esc(etq)}">{head}{rows}</div>'
_NORMAS = None
def xref(nid, texto=None):
    """Referencia a otra norma dentro del texto (R17), con el enlace editorial del libro (R06)"""
    global _NORMAS
    if _NORMAS is None:
        _NORMAS = {v['id']: (k, v['t']) for k, v in json.load(io.open(os.path.join(ROOT, 'data', 'normas.json'), encoding='utf-8')).items()}
    ruta, t = _NORMAS[nid]
    return f'<a class="xref" href="../{ruta}" title="{nid}">{esc(texto or t)}</a>'
def tri3(cols):
    """Comparación en tres columnas: cada columna con su nombre y las mismas filas, alineadas entre columnas"""
    return (f'{I}<div class="tri3">' + ''.join(f'<div><p class="tri3__t">{esc(t)}</p>' + ''.join(f'<div class="tri3__c"><span class="tri3__k">{esc(k)}</span><p>{esc(v)}</p></div>' for k, v in filas) + '</div>'
                                              for t, filas in cols) + '</div>')


def seccion(sid, num, corto, titular, partes):
    return (f'\n    <!-- {num} · {corto} -->\n    <section class="ed" id="{sid}">\n      <div class="ed__label"><span>{num}</span><span>{esc(corto)}</span></div>\n      <div>\n'
            f'{I}<h2 class="ed__title">{esc(titular)}</h2>\n' + '\n'.join(partes) + '\n      </div>\n    </section>\n')


# ───────────── 16.4 · Espectro de la imagen 1 (Keylin, 2026-11-17) ─────────────
# Solo la comparación en tres columnas: la barra y los nombres salieron (Keylin, 2026-11-17); cada columna lleva su nombre
TRI = tri3([('Formal', [('Propósito', 'Informar con exactitud.'), ('Recursos', 'Tipografía, retícula y espacio, con acentos puntuales.'),
                        ('Color', 'Blanco Keyons y Azul Noche, con Azul Cielo para orientar.'), ('Piezas', 'Contratos, políticas, certificaciones e informes técnicos.')]),
            ('Corporativo Editorial', [('Propósito', 'Explicar y convencer.'), ('Recursos', 'Fotografía protagonista, titulares grandes y atmósferas.'),
                                       ('Color', 'Los cinco colores oficiales, cada uno en su función.'), ('Piezas', 'Presentaciones, informes ejecutivos, propuestas y memorias.')]),
            ('Expresivo', [('Propósito', 'Inspirar y construir una experiencia.'), ('Recursos', 'Composición experimental, cielos, texturas y movimiento.'),
                           ('Color', 'Cielos, degradados o monocromía, según la atmósfera.'), ('Piezas', 'Campañas, piezas narrativas y aperturas editoriales.')])])

# ───────────── Capítulo 16 · Corporativo ─────────────
PALETA = (f'{I}<ul class="paleta5" aria-label="Los cinco colores oficiales">'
          + ''.join(f'<li><i style="background:var({v})"></i><b>{n}</b><span>{d}</span></li>' for v, n, d in [
              ('--k-blanco', 'Blanco Keyons', 'Estructura y contraste'), ('--k-noche', 'Azul Noche', 'Estructura y contraste'),
              ('--k-cielo', 'Azul Cielo', 'Reconocimiento y acento'), ('--k-salmon', 'Salmón Tierra', 'Expresión según el contexto'),
              ('--k-atardecer', 'Salmón Atardecer', 'Variante para composiciones oscuras')]) + '</ul>')
C16 = [
    ('principios', '16.1', 'Principios', 'Claridad con carácter', [
        lead('La expresión corporativa de Keyons combina <strong>claridad, confianza y personalidad</strong> mediante una composición precisa y un uso deliberado del espacio.'),
        pgrid_v([('La claridad dirige', [N('Cada pieza debe dejar claro qué información importa más y en qué orden se lee.', 'debe'), 'La tipografía, el espacio y la retícula resuelven la jerarquía antes que cualquier recurso decorativo.']),
                 ('La sobriedad es una elección', [N('La expresión corporativa puede usar todos los recursos de la identidad Keyons.', 'puede'), 'Cada pieza elige los que su función necesita, con precisión y equilibrio.']),
                 ('El carácter nace de la composición', ['Keyons se reconoce por la relación entre tipografía, proporción, imagen, color y espacio, sin repetir un motivo gráfico.']),
                 ('La función marca la intensidad', ['Un aviso legal, una propuesta comercial y una memoria corporativa comparten identidad y varían en ritmo, recursos e intensidad.'])]),
    ]),
    ('formal', '16.2', 'Formal', 'Precisión que transmite confianza', [
        lead('Formal es la referencia <strong>más contenida</strong> del sistema: sirve cuando importan la exactitud, la lectura prolongada o las consecuencias institucionales de la información.'),
        stack([('Color', [N('La composición formal debería partir de fondos claros, texto de alto contraste, Azul Noche y Blanco Keyons, con Azul Cielo para orientar y acentuar.', 'deberia'),
                          N('Otros colores oficiales pueden sumarse cuando hay una razón de comunicación y se conserva la legibilidad.', 'puede')]),
               ('Tipografía y jerarquía', [N('Los títulos deben permitir localizar el contenido de un vistazo, y los párrafos, mantener una medida cómoda.', 'debe'),
                                           N('La tipografía expresiva puede aparecer en portadas y aperturas.', 'puede')]),
               ('Composición', [N('Retículas regulares y márgenes generosos sostienen la lectura. Cada elemento gráfico debe cumplir una función: organizar, separar, destacar o contextualizar.', 'debe')]),
               ('Dónde se usa', ['Contratos, políticas, documentos regulatorios, certificaciones, comunicaciones oficiales e informes técnicos. Un informe también admite el tratamiento editorial cuando el contenido y la audiencia lo permiten.'])]),
    ]),
    ('editorial', '16.3', 'Editorial', 'El rigor también puede ser memorable', [
        lead('Corporativo Editorial suma <strong>libertad compositiva</strong> sin perder precisión: fotografía protagonista, titulares de mayor escala y un uso más amplio del color.'),
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
    ('intensidad', '16.4', 'Intensidad', 'La identidad permanece. La intensidad cambia.', [
        # Apertura: la intro del área Expresión pasa aquí (Keylin, 2026-11-17)
        lead('Keyons tiene <strong>una sola identidad visual</strong>. Su expresión cambia según lo que necesita comunicar, las personas a quienes se dirige y el entorno en el que aparece.'),
        TRI,
        sub('Lo que permanece y lo que varía'),
        lead('La identidad Keyons no cambia entre los niveles de expresión. Lo que cambia es <strong>la manera de combinar sus recursos</strong> y el protagonismo que adquieren.'),
        matriz('Lo que permanece y lo que varía entre los niveles de expresión',
               [('Lo que permanece', 'Los tres niveles comparten las mismas bases'), ('Lo que varía', 'Cada nivel puede modificar')],
               [('Tipografía', ['Familias oficiales y principios de jerarquía.', 'Escala, contraste, alineación y protagonismo.']),
                ('Color', ['Paleta corporativa, funciones cromáticas y criterios de contraste.', 'Proporción, intensidad, fondos y presencia de acentos.']),
                ('Composición', ['Retícula, equilibrio, claridad y geometría de marca.', 'Simetría, asimetría, espacios y ritmo.']),
                ('Recursos', ['Criterios de calidad, originalidad y pertinencia visual.', 'Fotografía, cielos, ilustración, texturas y movimiento.'])]),
        prosa(N('La pieza debe conservar una relación reconocible con Keyons, aunque su apariencia cambie considerablemente.', 'debe'),
              N('La intensidad debería responder al contenido y al contexto, no a una cantidad predeterminada de recursos.', 'deberia')),
        sub('Cuatro preguntas para decidir'),
        lead(N('Antes de establecer la intensidad visual de una pieza, el diseñador debería responder estas cuatro preguntas.', 'deberia')),
        pgrid([('¿Qué debe lograr la pieza?', ['Informar, explicar, persuadir o generar impacto.'], 'El objetivo define qué debe destacar.'),
               ('¿Quién la utilizará?', ['Nivel de conocimiento y necesidad de detalle.'], 'La audiencia define el nivel de claridad requerido.'),
               ('¿Dónde se usará?', ['Documento, presentación, digital o interactivo.'], 'El contexto define el margen de experimentación.'),
               ('¿Qué tan compleja es la información?', ['Datos, instrucciones, cifras o narrativa visual.'], 'La complejidad define los recursos visuales necesarios.')]),
        sub('Los niveles pueden convivir'),
        lead('Una propuesta comercial puede abrir con una portada expresiva, desarrollar su argumento mediante composiciones editoriales y cerrar con condiciones formales.'),
        prosa(N('Los cambios de intensidad pueden ocurrir dentro de una misma pieza.', 'puede'),
              N('Sus transiciones deben conservar continuidad tipográfica, cromática y compositiva.', 'debe')),
        stack([('Intensidad y densidad', [N('La intensidad mide el protagonismo de los recursos de identidad; la densidad, la cantidad y organización de la información. Cada una debe regularse por separado.', 'debe')])]),
    ]),
    ('documentos', '16.5', 'Documentos', 'El documento como expresión de marca', [
        lead('Un documento Keyons es <strong>una herramienta clara y confiable</strong> con identidad propia: la estructura da continuidad y la intensidad cambia la presentación, nunca la información.'),
        stack([('Formato', [N('El formato debe responder al destino del documento: impresión, lectura digital, distribución o edición.', 'debe')]),
               # Auditoría del 2026-11-17: lo que ya regula otra norma se cita con enlace (R17) y aquí queda solo lo propio del documento
               ('Márgenes y retícula', [N(f'Columnas, márgenes y medianiles siguen la norma {xref("KYN-MRK-ESP-004")}. En un documento, sus posiciones deben repetirse de una página a otra.', 'debe')]),
               ('Tipografía', [f'La jerarquía de títulos, cuerpo, notas y cifras sigue la norma {xref("KYN-MRK-TYP-002")}, y cada familia se usa según {xref("KYN-MRK-TYP-006")}.']),
               ('Portada', [N('La portada debe mostrar el título, el emisor y los datos de identificación. Su intensidad, formal o editorial, depende del contenido y la audiencia.', 'debe')]),
               ('Encabezado y pie', [N('Encabezado y pie deberían llevar solo la información recurrente útil: identidad, título breve, versión o página.', 'deberia')]),
               ('Títulos y numeración', [N('La jerarquía debe distinguir capítulos, secciones y apartados sin depender solo del tamaño o del color. La numeración se usa cuando facilita referencias o auditorías.', 'debe')]),
               ('Tablas y cifras', [N(f'Las cifras deben mostrar sus unidades y alinearse según {xref("KYN-MRK-TYP-006")}. El color ayuda a leer, pero nunca es la única diferencia.', 'debe')]),
               ('Gráficos', [N(f'Los gráficos deben seguir las {xref("KYN-MRK-DAT-001", "normas de datos y visualización")} de Keyons, fuente única de sus paletas.', 'debe')]),
               ('Notas y citas', [N('Notas y referencias deben encontrarse con facilidad, sin competir con el texto principal.', 'debe')]),
               ('Firmas', [N('Cada bloque de firma debe mostrar quién firma, con qué función y bajo qué procedimiento. La firma visual y la firma con validez jurídica son elementos distintos.', 'debe')]),
               ('Sellos', [N('Sellos y marcas de agua deben corresponder a una certificación o aprobación real y conservar la legibilidad.', 'debe')])]),
        cierre('Una pieza corporativa Keyons no necesita elegir entre rigor y personalidad.', 'Su calidad está en saber cuánto protagonismo dar a cada uno.'),
    ]),
]

C17 = [
    ('principios', '17.1', 'Principios', 'Libertad con intención', [
        lead('La expresión de Keyons puede ser <strong>intensa, sensible y memorable</strong> sin perder claridad: su fuerza nace de la relación entre forma, contenido y emoción.'),
        pgrid_v([('Una identidad que permite explorar', [N('La experimentación debe conservar una relación visible con la tipografía, el color, la geometría y la composición de Keyons.', 'debe')]),
                 ('La intensidad no es saturación', [N('Cada composición debe elegir un protagonista y los elementos que lo acompañan.', 'debe'), 'Reunir todos los recursos a la vez genera competencia visual.']),
                 ('La emoción tiene una función', [N('Cada recurso expresivo debe transmitir una idea, una atmósfera o una experiencia ligada al contenido.', 'debe')]),
                 ('La claridad permanece', [N('La información esencial debe seguir siendo fácil de encontrar, con contraste y jerarquía suficientes.', 'debe')])]),
        sub('Estructura y expresión'),
        lead('Keyons combina la disciplina de una <strong>estructura clara</strong> con la libertad de una expresión visual propia.'),
        stack([('La metáfora 60/40', ['La relación 60/40 describe ese equilibrio: una base estructural sólida que sostiene una capa expresiva con personalidad, sin ser una proporción técnica ni un reparto por porcentajes.']),
               ('Minimalismo y maximalismo', ['Son recursos que pueden convivir dentro de una misma pieza. Una fotografía intensa puede ocupar una composición muy sencilla; una página casi monocromática puede lograr gran expresividad con escala, ritmo y espacio.'])]),
        cierre('La intensidad no se mide por la cantidad de elementos, sino por la fuerza y la pertinencia de las decisiones visuales.'),
    ]),
    ('composicion', '17.2', 'Composición', 'Una retícula que permite explorar', [
        lead('La retícula es <strong>una herramienta</strong>, no una plantilla: admite simetría, asimetría controlada o una organización editorial experimental.'),
        stack([('Protagonista', [N('Cada composición debería tener un centro de atención reconocible: una fotografía, una frase, una cifra o una relación espacial.', 'deberia')]),
               ('Espacio', ['El espacio libre crea contraste, pausa y expectativa. Pocos elementos bien elegidos suelen recordarse más que muchos.']),
               ('Asimetría', [N('La asimetría puede generar movimiento o tensión, siempre con un equilibrio perceptible.', 'puede')]),
               ('Composición propia', [N('Cada pieza debe tener decisiones visuales propias de su contenido. Cambiar solo la foto y el título de una composición genérica tampoco es dirección creativa.', 'debe')])]),
    ]),
    ('tipografia', '17.3', 'Tipografía', 'La letra también expresa', [
        lead('La tipografía <strong>también narra</strong>: escala, peso, alineación y ritmo construyen personalidad con las familias oficiales.'),
        stack([('Dónde se expresa', [N('Los tratamientos expresivos deberían concentrarse en títulos, aperturas y mensajes breves.', 'deberia')]),
               ('Lectura continua', [N('Los textos de lectura continua deben mantener legibilidad, contraste y espaciado adecuados.', 'debe')]),
               ('Tipografía como firma', [N('Tipografía y diagramación pueden bastar para que una pieza se reconozca como Keyons, sin otros recursos.', 'puede')])]),
    ]),
    ('color', '17.4', 'Color y cielos', 'El color construye atmósfera', [
        lead('El sistema cromático permite <strong>piezas contenidas e intensas</strong>; una pieza monocromática también puede ser expresiva.'),
        stack([('Cielos', [N('Los cielos deben responder a la intención de la pieza y a sus normas de construcción. Su función es atmosférica: categorías, resultados y estados usan otros colores.', 'debe')]),
               ('Degradados', [N('Los degradados deben verse como transiciones naturales, sin cortes ni saltos que afecten el contraste del texto.', 'debe'),
                               N('Su posición, extensión y dirección pueden adaptarse a cada soporte.', 'puede')]),
               ('Color con propósito', [N('El color expresivo, el color de datos y el color semántico deben mantenerse separados. Un color de marca nunca indica por sí solo éxito, advertencia o error.', 'debe')])]),
    ]),
    ('recursos', '17.5', 'Recursos', 'Cada recurso con un propósito', [
        lead('Cada recurso entra <strong>cuando ayuda a comunicar</strong>, y la decisión siempre es humana.'),
        pgrid_i([('camara', 'Fotografía', [N('La fotografía puede asumir el protagonismo de una composición.', 'puede'), N('Su selección debe responder a una intención narrativa, con calidad, autenticidad y pertinencia.', 'debe')], None),
                 ('formas', 'Ilustración e imágenes sintéticas', [N('Su dirección artística debe partir de criterio humano, originalidad y respeto de derechos.', 'debe'), N('Una imagen sintética no debe presentarse como fotografía documental de un hecho real.', 'no-debe')], None),
                 ('capas', 'Texturas y tramas', [N('Las texturas deben ceder ante textos, cifras y elementos esenciales: si compiten, se reducen o se retiran.', 'debe')], None),
                 ('flecha-giro', 'Movimiento', [N('El contenido debe comprenderse sin la animación, y el movimiento, respetar las preferencias de accesibilidad.', 'debe')], None),
                 ('perfil', 'Firma humana', ['La expresión Keyons nace de decisiones deliberadas: selección, composición, edición y evaluación.', 'La tecnología amplía las posibilidades; el criterio decide cuáles usar.'], None)]),
    ]),
    ('limites', '17.6', 'Límites', 'La libertad no elimina la responsabilidad', [
        lead(N('Toda pieza expresiva debe conservar contraste, accesibilidad, comprensión y reconocimiento de marca.', 'debe')),
        stack([('Información primero', ['La intensidad visual nunca justifica ocultar información o dificultar una acción.']),
               ('Recursos opcionales', ['Fotografía, texturas, cielos, degradados y movimiento son opcionales. Las proporciones de color sirven como punto de partida; la calidad se juzga por el resultado y el contexto.']),
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

# La página del área queda sin intro, como las demás áreas (Keylin, 2026-11-17)
p = os.path.join(ROOT, 'modos', 'index.html')
s = io.open(p, encoding='utf-8').read()
s = re.sub(r'\n[ \t]*<template id="area-intro">.*?</template>', '', s, flags=re.S)   # quita exactamente lo que se insertó
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
