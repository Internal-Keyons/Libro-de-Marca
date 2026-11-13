"""Área Expresión de marca · introducción, capítulo 16 Corporativo y capítulo 17 Expresivo.

Uso:  python tools/expresion.py
Texto: Keylin, 2026-11-13. Escribe la introducción en modos/index.html (<template id="area-intro">),
modos/corporativo.html y modos/expresivo.html, y los ítems del índice de los capítulos 16 y 17 en js/nav-data.js.

Diagramación con los componentes del libro:
- base: título, entrada (.ed__lead), lectura continua (.prosa), filas con rótulo (.ed__stack), cierre (.ed__close);
- creativa donde ayuda a leer: tarjetas numeradas (.pgrid) para principios, preguntas y recursos; el espectro de intensidad
  (.espectro) en la introducción; la paleta corporativa en fila (.paleta5) en Editorial.
"""
import html
import io
import os
import re

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
C16 = [
    ('principios', '16.1', 'Principios', 'Claridad con carácter', [
        lead('La expresión corporativa de Keyons comunica profesionalismo, confianza y criterio. Se apoya en una composición clara, una jerarquía reconocible y un uso deliberado del espacio.'),
        prosa('Su sobriedad no implica ausencia de personalidad. La identidad puede manifestarse mediante una decisión tipográfica, una fotografía, un acento cromático o una composición editorial bien resuelta.',
              'Dentro de este capítulo conviven dos referencias de intensidad: Formal y Corporativo Editorial. Ambas comparten los mismos fundamentos visuales y pueden combinarse según las necesidades del contenido.'),
        pgrid([('La claridad dirige', ['Cada pieza debe establecer qué información tiene mayor importancia y cómo debe recorrerla quien la recibe.', 'La composición ordena el contenido antes de incorporar recursos decorativos. La tipografía, el espacio y la retícula deben resolver la jerarquía incluso cuando la pieza no utiliza fotografías ni elementos expresivos.']),
               ('La sobriedad es una elección, no una restricción', ['La expresión corporativa puede utilizar los recursos completos de la identidad Keyons.', 'Su selección debe responder a la función de cada pieza. Una composición contenida puede requerir pocos recursos; otra puede beneficiarse de una fotografía de gran formato o una presencia cromática más marcada.', 'Lo importante es conservar precisión, equilibrio y reconocimiento de marca.']),
               ('El carácter nace de la composición', ['Keyons no necesita repetir un motivo gráfico para que todas sus piezas se reconozcan.', 'La relación entre tipografía, proporciones, imágenes, color y espacio debe generar continuidad sin convertir la identidad en una plantilla intercambiable.']),
               ('La función determina la intensidad', ['Una comunicación legal, una propuesta comercial y una memoria corporativa no requieren necesariamente el mismo tratamiento visual.', 'Comparten identidad, pero pueden variar en ritmo, recursos e intensidad según el tipo de información y las expectativas de lectura.'])]),
    ]),
    ('formal', '16.2', 'Formal', 'Precisión que transmite confianza', [
        lead('Formal es la referencia más contenida del sistema de expresión.'),
        prosa('Está especialmente indicada para comunicaciones donde predominan la exactitud, la trazabilidad documental, la lectura prolongada o las consecuencias institucionales de la información.',
              'Su composición debería priorizar fondos claros, texto de alto contraste, una retícula estable y recursos gráficos discretos.',
              'El blanco y el Azul Noche constituyen una base especialmente apropiada. Azul Cielo puede utilizarse para identificar, orientar o establecer acentos. Otros colores oficiales también pueden incorporarse cuando exista una razón de comunicación y se mantenga la legibilidad.',
              'Esta preferencia no prohíbe los recursos cromáticos de Keyons. Define una dirección visual recomendada.'),
        stack([('Tipografía y jerarquía', ['La tipografía conduce la lectura mediante diferencias claras de tamaño, peso, posición y espacio.', 'Los títulos deben permitir localizar rápidamente el contenido. Los párrafos mantienen una medida cómoda, interlineado suficiente y una secuencia de lectura predecible.', 'La expresividad tipográfica puede aparecer en portadas o aperturas, sin comprometer la comprensión del documento.']),
               ('Composición', ['Las retículas regulares y los márgenes generosos favorecen la lectura y la estabilidad visual.', 'La simetría es apropiada cuando refuerza la formalidad. La asimetría controlada también puede utilizarse si conserva equilibrio y continuidad.', 'Los elementos gráficos deben cumplir una función identificable: organizar, separar, destacar o contextualizar.']),
               ('Aplicación', ['Formal resulta especialmente útil en contratos, políticas, documentos regulatorios, certificaciones, comunicaciones oficiales e informes que requieren lectura técnica o administrativa.', 'No es una categoría obligatoria por tipo de archivo. Un informe también puede adoptar tratamiento editorial cuando el contenido y la audiencia lo permiten.'])]),
    ]),
    ('editorial', '16.3', 'Editorial', 'El rigor también puede ser memorable', [
        lead('Corporativo Editorial amplía la libertad compositiva sin abandonar la precisión.'),
        prosa('Combina la claridad institucional con una dirección visual más reconocible. Puede utilizar fotografía protagonista, titulares de mayor escala, relaciones espaciales menos convencionales y un uso más amplio del color.',
              'Es una referencia apropiada para presentaciones corporativas, informes ejecutivos, publicaciones de marca, propuestas, memorias y comunicaciones cuyo contenido se beneficia de una lectura editorial.'),
        stack([('Composición y ritmo', ['La retícula continúa siendo el fundamento, pero permite variaciones de escala, alineación y ocupación del espacio.', 'Una página puede contener una sola idea protagonista. Otra puede organizar varias capas de información mediante bloques, fotografía y contrastes tipográficos.', 'El cambio de ritmo debe facilitar la lectura, no interrumpirla.', 'Los espacios blancos tienen valor compositivo. No deben llenarse únicamente para equilibrar visualmente la cantidad de contenido.'])]),
        sub('El color corporativo completo'),
        prosa('Corporativo Editorial puede utilizar los cinco colores oficiales de la identidad, respetando sus funciones y condiciones de uso: Blanco Keyons, Azul Noche, Azul Cielo, Salmón Tierra y Salmón Atardecer.',
              'Esto no significa que todos deban aparecer en cada pieza ni que tengan la misma función.'),
        PALETA,
        prosa('Blanco Keyons y Azul Noche sostienen la estructura y el contraste. Azul Cielo aporta reconocimiento y acento. Salmón Tierra y Salmón Atardecer enriquecen la expresión según el contexto y las combinaciones definidas por el sistema cromático.',
              'El uso de Salmón Atardecer debe respetar especialmente su función como variante para composiciones oscuras.',
              'La composición puede utilizar varios de estos colores, incluso con gran presencia visual, siempre que conserve jerarquía, equilibrio y contraste suficiente.'),
        stack([('Fotografía y atmósfera', ['Las fotografías deben aportar significado, contexto o una perspectiva reconocible.', 'Pueden ocupar una página completa, convivir con grandes espacios vacíos o integrarse mediante recortes y composiciones editoriales.', 'Los cielos, degradados y texturas pueden acompañar las imágenes cuando ayudan a construir una atmósfera.', 'No deben utilizarse como una obligación estética ni sustituir la claridad del mensaje.']),
               ('Reconocimiento de marca', ['Una pieza editorial debe poder reconocerse como Keyons a través de su tipografía, diagramación, proporciones y decisiones visuales, sin depender exclusivamente del logotipo.', 'La coherencia se alcanza por la relación entre los elementos, no por repetir siempre el mismo recurso.'])]),
    ]),
    ('intensidad', '16.4', 'Intensidad', 'Elegir cuánto expresar', [
        lead('La intensidad corporativa no se selecciona mediante una etiqueta fija. Se ajusta durante el diseño de acuerdo con la función de la pieza.'),
        prosa('Cuando el contenido exige precisión, estabilidad o lectura extensa, conviene reducir la competencia visual.',
              'Cuando la intención es explicar una visión, presentar un proyecto o construir una narrativa, puede aumentar el protagonismo de la fotografía, el color y la composición.',
              'La decisión debe considerar:'),
        pgrid([('Propósito', ['Informar, explicar, convencer, documentar o inspirar.']), ('Audiencia', ['Conocimientos, expectativas y necesidades de lectura.']),
               ('Canal', ['Documento, pantalla, presentación, publicación o soporte físico.']), ('Contenido', ['Volumen, complejidad, importancia y sensibilidad de la información.'])]),
        stack([('Una misma pieza puede variar', ['Una propuesta comercial puede comenzar con una portada de alto impacto, desarrollar su argumento mediante páginas editoriales y cerrar con condiciones formales de composición contenida.', 'No necesita escoger un único nivel para toda su extensión.', 'Las transiciones deben conservar continuidad tipográfica, cromática y compositiva.']),
               ('Intensidad y densidad son diferentes', ['Una composición puede ser intensa y contener muy poca información.', 'También puede presentar numerosos datos sin ser visualmente expresiva.', 'La intensidad describe el protagonismo de los recursos de identidad. La densidad describe la concentración y organización de información.', 'Ambas dimensiones deben regularse por separado.'])]),
    ]),
    ('documentos', '16.5', 'Documentos', 'El documento como expresión de marca', [
        lead('Los documentos Keyons deben funcionar como herramientas claras y confiables, sin renunciar a su identidad visual.'),
        prosa('La estructura documental establece continuidad entre diferentes usos. El nivel expresivo modifica la presentación sin alterar la integridad de la información.'),
        stack([('Formatos', ['Se utiliza el formato que mejor responda al destino del documento: impresión, lectura digital, distribución o edición.', 'La elección debe considerar compatibilidad, facilidad de consulta, exportación y conservación.', 'No se crean formatos nuevos únicamente para diferenciarlos visualmente.']),
               ('Márgenes y retícula', ['Los márgenes proporcionan protección al contenido y espacio para la lectura.', 'La retícula debe facilitar la alineación de títulos, párrafos, tablas, imágenes y referencias.', 'En documentos extensos, la repetición de posiciones permite reconocer la estructura de una página a otra.', 'Los valores exactos se toman de las especificaciones de formato correspondientes; no se improvisan para cada archivo.']),
               ('Tipografía', ['Se utiliza el sistema tipográfico oficial de Keyons.', 'Los estilos de título, subtítulo, cuerpo, nota y cifra mantienen relaciones consistentes de tamaño, peso e interlineado.', 'La tipografía no debe reemplazarse por fuentes decorativas para simular una expresión más creativa.']),
               ('Portada', ['La portada identifica el documento y establece su jerarquía principal.', 'Debe mostrar con claridad el título, el emisor y los datos de identificación necesarios.', 'Puede ser formal o editorial. El uso de fotografía, composición asimétrica o recursos cromáticos depende del contenido y la audiencia.']),
               ('Encabezado y pie', ['Estos elementos contienen información recurrente útil, como identidad, título abreviado, versión o paginación.', 'Deben mantener una presencia discreta y consistente.', 'No es necesario repetir todos los metadatos en cada página cuando no aportan valor a la consulta.']),
               ('Títulos y numeración', ['La jerarquía permite identificar capítulos, secciones y apartados sin depender únicamente del tamaño o del color.', 'La numeración se utiliza cuando facilita referencias, auditoría o navegación.', 'Los documentos editoriales pueden emplear encabezados más libres si su organización sigue siendo comprensible.']),
               ('Tablas y cifras', ['Las tablas priorizan la comparación y la precisión.', 'Los números deben alinearse de manera consistente, mantener unidades visibles y permitir distinguir encabezados, valores, totales y notas.', 'El color puede ayudar a interpretar, pero no debe ser la única forma de diferenciar información.']),
               ('Gráficos', ['Los gráficos se seleccionan según el tipo de relación que deben comunicar.', 'Se utilizan las <a href="../fundamentos/datos/graficos.html">normas de datos y visualización de Keyons</a> como fuente única para las paletas categóricas, secuenciales y divergentes.', 'Las decisiones gráficas deben favorecer lectura, comparación y exactitud antes que decoración.']),
               ('Notas y citas', ['Las notas, fuentes y referencias deben ser fáciles de localizar sin competir con el contenido principal.', 'Los sistemas de citación siguen las exigencias del documento y su contexto.', 'La identidad visual puede definir su presentación, pero no modificar el sentido ni la integridad de las referencias.']),
               ('Firmas', ['Los bloques de firma deben mostrar claramente quién interviene, su función y el dato que corresponda al procedimiento.', 'El diseño no puede crear ambigüedad sobre autoría, aprobación o responsabilidad.', 'La firma visual y la firma con validez jurídica son elementos distintos.']),
               ('Sellos', ['Los sellos, marcas de agua y otros indicadores documentales se utilizan cuando cumplen una función de identificación, clasificación o control.', 'No deben presentarse como certificaciones o aprobaciones si no existe el respaldo correspondiente.', 'Su presencia debe conservar la legibilidad del documento.'])]),
        cierre('Una pieza corporativa Keyons no necesita elegir entre rigor y personalidad. Su calidad está en saber cuánto protagonismo dar a cada uno.',
               'El contenido determina la estructura. El criterio determina la expresión.'),
    ]),
]

# ───────────── Capítulo 17 · Expresivo ─────────────
C17 = [
    ('principios', '17.1', 'Principios', 'Libertad con intención', [
        lead('La expresión de Keyons puede ser intensa, sensible, experimental y memorable sin perder claridad.'),
        prosa('El carácter expresivo no depende de utilizar muchos colores, llenar una composición de elementos o aplicar efectos visuales. Depende de construir una relación significativa entre forma, contenido y emoción.',
              'Una imagen puede dominar todo el espacio. Un título puede alterar la escala habitual. Un cielo puede transformar la atmósfera de una página. Una composición casi vacía puede resultar igualmente expresiva.',
              'La libertad visual se ejerce dentro de la identidad compartida de Keyons.'),
        pgrid([('Una identidad que permite explorar', ['La expresión visual de Keyons admite variaciones, contrastes y decisiones inesperadas.', 'La experimentación debe conservar una relación con los fundamentos de marca. La tipografía, el sistema cromático, la geometría y los principios de composición constituyen referencias reconocibles incluso cuando la pieza adopta una dirección poco convencional.']),
               ('La intensidad no es saturación', ['Una composición expresiva no necesita reunir todos los recursos disponibles.', 'El uso simultáneo de fotografías, degradados, texturas, titulares grandes y movimiento puede producir una imagen intensa, pero también generar competencia visual.', 'La intensidad se construye seleccionando qué elemento merece protagonismo y qué elementos deben acompañarlo.']),
               ('La emoción tiene una función', ['Los recursos expresivos deben transmitir una idea, construir una atmósfera o provocar una experiencia relacionada con el contenido.', 'Una fotografía puede aportar cercanía. Una composición abierta puede sugerir libertad. Una escala tipográfica inesperada puede transmitir determinación.', 'El recurso debe tener un propósito identificable.']),
               ('La claridad permanece', ['La libertad gráfica no elimina las responsabilidades de lectura, accesibilidad y comprensión.', 'La información esencial debe seguir siendo localizable. El contraste, la jerarquía y la organización del contenido no pueden depender de que la persona interprete correctamente una intención artística.'])]),
    ]),
    ('composicion', '17.2', 'Composición', 'Una retícula que permite explorar', [
        lead('La retícula de Keyons es una herramienta de composición, no una plantilla que todas las piezas deban repetir.'),
        prosa('Puede utilizarse una estructura simétrica, una composición asimétrica controlada o una organización editorial más experimental.',
              'Las variaciones deben conservar relaciones comprensibles entre los elementos.'),
        stack([('Jerarquía y protagonismo', ['Cada composición debería establecer un centro de atención reconocible.', 'El protagonismo puede recaer en una fotografía, una frase, una cifra, una textura o una relación espacial.', 'Los elementos secundarios deben apoyar esa decisión.', 'No es necesario que todos los componentes tengan una presencia equivalente.']),
               ('Espacio como recurso expresivo', ['El espacio libre permite crear contraste, pausa y expectativa.', 'Una composición con pocos elementos puede resultar más memorable que otra con abundantes recursos gráficos.', 'El espacio no debe entenderse como una zona pendiente de llenar.']),
               ('Asimetría con equilibrio', ['La asimetría puede utilizarse para producir movimiento, tensión o una lectura menos convencional.', 'Debe mantenerse un equilibrio perceptible mediante escala, distribución, alineación o contraste.', 'La irregularidad no es por sí misma una señal de creatividad.']),
               ('Composición no intercambiable', ['Cada pieza debe presentar decisiones visuales relacionadas con su contenido y propósito.', 'No basta con sustituir una fotografía, cambiar un título y conservar una composición genérica para considerar que existe una dirección creativa.', 'La identidad Keyons debe reconocerse por la calidad y coherencia de sus decisiones, no por repetir fórmulas visuales.'])]),
    ]),
    ('tipografia', '17.3', 'Tipografía', 'La letra también expresa', [
        lead('La tipografía puede asumir una función narrativa además de informativa.'),
        prosa('La escala, el peso, la alineación, el ritmo y el espacio permiten construir composiciones con personalidad sin abandonar las familias tipográficas oficiales.',
              'Un titular puede ocupar una proporción considerable del lienzo. Una palabra puede destacarse por su posición. Una composición puede utilizar un contraste marcado entre título y cuerpo.'),
        stack([('Libertad con jerarquía', ['Los tratamientos expresivos se concentran preferentemente en títulos, aperturas, mensajes breves y elementos editoriales protagonistas.', 'Los textos destinados a lectura continua mantienen condiciones de legibilidad, contraste y espaciado apropiadas.', 'La experimentación no debe trasladar complejidad innecesaria a párrafos, instrucciones o contenidos operativos.']),
               ('Tipografía como firma', ['La combinación de tipografía y diagramación puede ser suficiente para identificar una pieza como Keyons.', 'Una composición sin fotografía, ilustración ni degradado puede expresar plenamente la marca mediante proporciones, contraste y ritmo.', 'No es obligatorio incorporar recursos adicionales cuando la tipografía resuelve la intención visual.'])]),
    ]),
    ('color', '17.4', 'Color y cielos', 'El color construye atmósfera', [
        lead('El sistema cromático de Keyons permite composiciones contenidas e intensas.'),
        prosa('La expresión puede aumentar mediante contrastes, superficies de color, fotografías, cielos y degradados.',
              'La intensidad no exige utilizar toda la paleta. Una pieza monocromática también puede ser expresiva.'),
        stack([('Cielos', ['Los cielos son un recurso atmosférico propio de la identidad Keyons.', 'Permiten explorar transiciones de luz, profundidad, temperatura y estados visuales.', 'Su utilización debe responder a la intención de la pieza y a las normas de construcción cromática correspondientes.', 'No constituyen una paleta para representar categorías nominales, resultados o estados funcionales.']),
               ('Degradados', ['Los degradados deben percibirse como transiciones naturales y cuidadas.', 'Se deben evitar cambios bruscos de color, cortes visuales no intencionados y combinaciones que comprometan el contraste del contenido superpuesto.', 'La posición, extensión y dirección de un degradado pueden adaptarse a la composición.', 'No es necesario reproducir exactamente el mismo encuadre en todos los soportes.']),
               ('Color con propósito', ['El color puede establecer protagonismo, separar planos, comunicar temperatura emocional o reforzar una identidad.', 'Debe respetarse la diferencia entre color expresivo, color de datos y color semántico.', 'Un color oficial de marca no adquiere automáticamente una función de advertencia, éxito o error.', 'Las reglas cromáticas y de contraste existentes siguen siendo la fuente normativa para sus aplicaciones.'])]),
    ]),
    ('recursos', '17.5', 'Recursos', 'Cada recurso con un propósito', [
        pgrid([('Fotografía', ['La fotografía puede asumir el protagonismo de una composición.', 'Su selección debe responder a una intención narrativa y a criterios de calidad, autenticidad y pertinencia.', 'Se favorecen imágenes con carácter, iluminación cuidada, composición deliberada y una relación clara con el contenido.', 'No se requiere que todas las fotografías tengan una estética idéntica.']),
               ('Ilustración e imágenes sintéticas', ['La ilustración y las imágenes generadas mediante inteligencia artificial pueden formar parte de la expresión de Keyons.', 'Su dirección artística debe estar gobernada por criterio humano, originalidad y cumplimiento de derechos.', 'Una imagen sintética no debe presentarse como documentación fotográfica de un hecho real.']),
               ('Texturas y tramas', ['Las texturas pueden crear profundidad y carácter sin afectar la información.', 'Las tramas geométricas mantienen trazos definidos, continuos y uniformes.', 'Su presencia debe ser proporcionada al contenido. Cuando compiten con textos, cifras o elementos esenciales, deben reducirse o retirarse.']),
               ('Movimiento', ['El movimiento puede aportar ritmo, transición y carácter.', 'Las animaciones editoriales tienen mayor libertad expresiva que las operativas, pero deben conservar intención, continuidad y respeto por las preferencias de accesibilidad.', 'La animación no debe convertirse en un requisito para comprender el contenido.']),
               ('Firma humana', ['La expresión Keyons nace de decisiones de diseño deliberadas.', 'La intervención humana se manifiesta en la selección, composición, edición y evaluación del resultado, no en introducir defectos artificiales para aparentar originalidad.', 'La tecnología puede ampliar las posibilidades creativas; el criterio determina cuáles vale la pena utilizar.'])]),
    ]),
    ('limites', '17.6', 'Límites', 'La libertad no elimina la responsabilidad', [
        lead('Las composiciones expresivas deben conservar las condiciones necesarias de contraste, accesibilidad, comprensión y reconocimiento de marca.'),
        prosa('La intensidad visual nunca justifica ocultar información esencial o dificultar una acción.'),
        stack([('El recurso no es una obligación', ['No todas las piezas expresivas necesitan fotografía, textura, cielos, degradados o movimiento.', 'Tampoco existe un porcentaje universal de distribución cromática que determine si una pieza es válida.', 'Las proporciones orientativas pueden ayudar a iniciar una composición, pero su calidad se evalúa por el resultado y el contexto.']),
               ('Evitar la expresión automática', ['Una pieza pierde singularidad cuando sus decisiones gráficas son intercambiables con las de cualquier otra marca.', 'La acumulación de tendencias, efectos y recursos reconocibles no sustituye una dirección creativa propia.']),
               ('Cada contexto establece sus límites', ['Una campaña puede permitir una composición altamente experimental.', 'Un formulario de uso frecuente exige mayor estabilidad y previsibilidad.', 'La identidad puede expresar carácter en ambos contextos, pero no necesariamente con los mismos recursos ni la misma intensidad.'])]),
        cierre('Keyons no necesita verse siempre igual para ser reconocible.', 'Su identidad ofrece un lenguaje compartido. La expresión permite utilizarlo con libertad, sensibilidad y criterio.',
               'La creatividad no consiste en añadir más. Consiste en encontrar la forma que mejor comunica lo que importa.'),
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
