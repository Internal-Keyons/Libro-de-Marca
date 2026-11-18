"""Módulo 03 · Fundamentos (FUI): 07 Tokens, 08 Color funcional, 09 Tipografía y 10 Espacio y retícula.
Requisitos: textos de Keylin (docs/sd/fuente-keylin-2026-11-17.md). Titulares, entradas, decisiones, comportamientos,
excepciones y verificaciones: propuesta de Claude en borrador. Los valores citan los tokens reales de css/tokens.css y las
normas del Libro de Marca. Composición: Guía 05 «Composición normativa según el contenido».
"""
from .base import N, req, stack, matriz, detalle, c, L, M, R, norma, seccion, validacion, dims

MOD = 'fundamentos-interfaz'
C7, C8, C9, C10 = 'tokens-de-diseno', 'color-funcional', 'tipografia-aplicada', 'espacio-reticula-y-geometria'
def n7(nid, nombre, k, *a, **kw): return norma(nid, nombre, '03.01', MOD, C7, k, *a, **kw)
def n8(nid, nombre, k, *a, **kw): return norma(nid, nombre, '03.02', MOD, C8, k, *a, **kw)
def n9(nid, nombre, k, *a, **kw): return norma(nid, nombre, '03.03', MOD, C9, k, *a, **kw)
def n10(nid, nombre, k, *a, **kw): return norma(nid, nombre, '03.04', MOD, C10, k, *a, **kw)


# ═════════════ 07 · Tokens ═════════════
CAP07 = [
    n7('KYN-SDI-FUI-001', 'Fuente única de valores', 1, 'Tokens para todo valor compartido',
       'Se aplica a colores, medidas, radios y demás valores que usan varios componentes: <strong>cada uno se define en un solo lugar</strong>.', [
        req(N('Los componentes deben utilizar tokens oficiales para los valores visuales y funcionales compartidos, evitando valores arbitrarios repetidos en el código.', 'debe')),
        matriz('Tres niveles de token', [('Qué guarda', ''), ('Ejemplo real', 'css/tokens.css')], [
            ('Base', ['El valor crudo de la paleta, las escalas y las medidas.', f'{c("--k-cielo-500")}, {c("--k-noche-900")}, {c("--s4")}']),
            ('Semántico', ['El rol del valor en la interfaz.', f'{c("--color-text")}, {c("--color-border")}, {c("--color-status-error")}']),
            ('De componente', ['Una decisión propia de un componente, apoyada en un semántico.', f'{c("--r-control")}, {c("--line-w-control")}'])]),
        stack([('Uso', ['Los componentes leen tokens semánticos o de componente; los de base solo se usan para definir otros tokens.']),
               ('Nomenclatura', [f'Prefijo por categoría y rol, del general al particular: {c("--color-text-2")}, {c("--color-border-strong")}, {c("--fs-16")}.'])]),
    ], origen=['Fuente única de valores (base)', 'Tokens semánticos oficiales (matriz)', 'UIX-011'],
       responsabilidad='Los componentes usan tokens oficiales para todo valor compartido.', corto='Fuente única',
       verif=[('Búsqueda en el código', 'Se buscan colores, medidas y radios escritos a mano en el código de los componentes.', 'solo aparecen en el archivo de tokens.')], ver='grupo'),

    n7('KYN-SDI-FUI-002', 'Roles semánticos', 2, 'Tokens nombrados por su función',
       'Define cómo se nombra un token de interfaz: <strong>por su función</strong>, para que sobreviva a un cambio de tema.', [
        req(N('Los tokens deben describir su función, como superficie, texto, borde, foco, acción o estado, en lugar de depender únicamente del nombre de un color.', 'debe')),
        matriz('Roles semánticos y sus tokens', [('Tokens', 'css/tokens.css'), ('Para qué', '')], [
            ('Superficie', [f'{c("--color-bg")}, {c("--color-surface")}, {c("--color-inverse")}', 'Fondos de página, de componentes y de bloques invertidos.']),
            ('Texto', [f'{c("--color-text")}, {c("--color-text-2")}, {c("--color-text-3")}, {c("--color-text-disabled")}', 'Jerarquía de lectura y estado deshabilitado.']),
            ('Borde', [f'{c("--color-border")}, {c("--color-border-strong")}', 'Divisores y contornos de controles.']),
            ('Foco', [c('--color-focus'), f'El indicador de foco. Su color está en revisión.']),
            ('Acción', ['Hoy sin token propio.', f'El botón principal usa los colores de {M("KYN-MRK-COL-015")}. Se propone {c("--color-action")} y {c("--color-on-action")}.']),
            ('Estado', [f'{c("--color-status-success")}, {c("--color-status-warning")}, {c("--color-status-error")}, {c("--color-status-info")}, {c("--color-status-review")}',
                        f'Confirmaciones, avisos, errores, información y revisión.'])]),
        detalle([('Temas', [
            ('Cómo funciona', 'Un tema redefine los tokens semánticos; los de base y los componentes se mantienen.'),
            ('Estado', 'El tema claro es el actual. El tema oscuro y los temas de cliente para marca blanca están pendientes.')])]),
    ], origen=['Roles semánticos (base)', 'Temas claro y oscuro (pendiente de la matriz)'],
       responsabilidad='Los tokens se nombran por su función y permiten cambiar de tema.', corto='Roles semánticos',
       rel=['KYN-SDI-FUI-005', 'KYN-SDI-FUI-007'], verif=[('Revisión de nombres', 'Se revisan los tokens que usa cada componente.', 'ninguno usa un token con nombre de color para expresar una función.')]),

    n7('KYN-SDI-FUI-003', 'Cambios controlados', 3, 'Revisión de cambios en tokens compartidos',
       'Se aplica antes de cambiar un token que usan varios productos: <strong>el cambio se comprueba donde llega</strong>.', [
        req(N('Una modificación de tokens compartidos debe comprobarse en los componentes y productos afectados antes de aprobarse.', 'debe')),
        stack([('Procedimiento', ['Propuesta con el motivo, lista de componentes y productos afectados, revisión visual en cada uno y aprobación.']),
               ('Versión', ['Cada cambio publicado lleva su versión y su nota de cambios.']),
               ('Aprobación', ['Los cambios en tokens compartidos se aprueban antes de publicarse.'])]),
    ], origen=['Cambios controlados (base)', 'UIX-011'],
       responsabilidad='Los cambios de tokens se comprueban en componentes y productos antes de aprobarse.', corto='Cambios controlados',
       rel=['KYN-SDI-GOB-011', 'SD-42'], verif=[('Antes y después', f'Se cambia {c("--color-text")} en una rama de prueba y se capturan las pantallas clave de cada producto antes y después.', 'cambian todos los textos y nada más.')], ver='grupo'),

    seccion('ejemplo', '07', 'Ejemplo de aplicación', 'Un botón principal',
            'Un botón usa <strong>tokens de acción y de texto sobre acción</strong>, no un color hexadecimal escrito en cada pantalla.', [
        stack([('Hoy', [f'El fondo y el texto del botón salen de {M("KYN-MRK-COL-015")}; falta su token semántico propio, según {R("KYN-SDI-FUI-002")}.'])]),
    ]),
    validacion('03.01', C7, 'El capítulo se comprueba cuando <strong>los componentes reutilizables heredan los valores correctos</strong> y los cambios no provocan regresiones en otras vistas.'),
]

# ═════════════ 08 · Color funcional ═════════════
CAP08 = [
    n8('KYN-SDI-FUI-004', 'Color con función', 1, 'Función de cada color en la interfaz',
       'Se aplica a todo color de una pantalla: <strong>cada uno cumple una función</strong> de identidad, jerarquía, acción, estado o datos.', [
        req(N('Cada color aplicado a una interfaz debe cumplir una función de identidad, jerarquía, acción, estado o diferenciación de información.', 'debe')),
        matriz('Funciones del color en pantalla', [('Colores', ''), ('Norma de origen', 'Libro de Marca')], [
            ('Identidad', ['Azul Noche y Azul Cielo, contenidos.', M('KYN-MRK-COL-012')]),
            ('Jerarquía', ['Grises tipográficos.', M('KYN-MRK-COL-013')]),
            ('Acción', ['El color del botón principal y los enlaces.', M('KYN-MRK-COL-015')]),
            ('Estado', ['Los colores de estado con su ícono.', M('KYN-MRK-COL-014')]),
            ('Datos', ['Las paletas de gráficos.', M('KYN-MRK-DAT-002')])]),
    ], origen=['Color con función (base)'], responsabilidad='Cada color de la interfaz cumple una función identificable.', corto='Color con función',
       verif=[('Inventario', 'Se listan los colores de una pantalla con la función de cada uno.', 'ninguno queda sin función.')]),

    n8('KYN-SDI-FUI-005', 'Estados semánticos', 2, 'Estados con color y señal adicional',
       'Se aplica a errores, advertencias, confirmaciones e información: <strong>el color acompaña y el ícono y el texto confirman</strong>.', [
        req(N('Los errores, advertencias y confirmaciones deben utilizar las funciones cromáticas oficiales y señales adicionales que permitan comprenderlos sin depender exclusivamente del color.', 'debe')),
        matriz('Estados y sus señales', [('Fondo', 'Token'), ('Señal adicional', '')], [
            ('Éxito', [c('--color-status-success'), 'Ícono de verificación y texto del resultado.']),
            ('Advertencia', [c('--color-status-warning'), 'Ícono de advertencia y qué conviene revisar.']),
            ('Error', [c('--color-status-error'), 'Ícono de advertencia, mensaje que explica y relación visible con el elemento afectado.']),
            ('Información', [c('--color-status-info'), 'Ícono de información.']),
            ('En revisión', [c('--color-status-review'), 'Etiqueta de texto.'])]),
        detalle([('Notas técnicas', [
            ('Texto sobre el fondo de estado', 'Azul Noche, que cumple el contraste de lectura sobre los cinco fondos.'),
            ('Íconos', f'Del catálogo aprobado.')])]),
    ], origen=['Estados semánticos (base)', 'UIX-038'], responsabilidad='Los estados usan el color oficial y una señal adicional.', corto='Estados',
       rel=['KYN-MRK-ICO-005'], verif=[('Escala de grises', 'Se ve una pantalla con los cinco estados en escala de grises.', 'cada estado sigue distinguiéndose por su ícono y su texto.')], ver='grupo'),

    n8('KYN-SDI-FUI-006', 'Separación de significados', 3, 'Salmón Tierra y el color de error',
       'Se aplica a errores y a acentos de identidad: <strong>cada color conserva un solo significado</strong>.', [
        req(N('Salmón Tierra no debe utilizarse como sustituto del color semántico de error.', 'no-debe')),
        stack([('Salmón Tierra', [f'Es un color de identidad y de acento expresivo.']),
               ('Error', [f'Usa {c("--color-status-error")} con su ícono y su mensaje.'])]),
    ], origen=['Separación de significados (base)'], responsabilidad='Salmón Tierra no reemplaza al color de error.', corto='Significados',
       rel=['KYN-MRK-COL-004', 'KYN-SDI-FUI-005'], verif=[('Revisión de errores', 'Se revisan los mensajes de error y los campos inválidos de una pantalla.', 'ninguno usa Salmón Tierra.')], ver='grupo'),

    n8('KYN-SDI-FUI-007', 'Contraste', 4, 'Contraste mínimo de las combinaciones',
       'Se aplica a todo par de texto, borde, ícono o foco con su fondo: <strong>el contraste se mide</strong> contra los mínimos de WCAG 2.2 AA.', [
        req(N('Las combinaciones cromáticas deben respetar los criterios de contraste aplicables de WCAG 2.2 AA.', 'debe')),
        matriz('Mínimos de contraste de WCAG 2.2 AA', [('Mínimo', ''), ('Criterio', '')], [
            ('Texto normal', ['4,5:1', '1.4.3']),
            ('Texto grande (24 px, o 18,66 px en negrita)', ['3:1', '1.4.3']),
            ('Componentes, bordes de campos, íconos que informan y foco', ['3:1 contra lo que los rodea', '1.4.11']),
            ('Controles deshabilitados', ['Sin mínimo, pero legibles', 'Excepción de 1.4.3'])]),
        detalle([('Decisión pendiente', [
            ('Color del foco', f'{c("--color-focus")} es Azul Cielo y sobre Blanco Keyons da 2,6:1, por debajo de 3:1. El libro usa hoy un anillo Azul Noche. Requiere aprobación: pasar el token a Azul Noche.')])]),
    ], origen=['Contraste (base)', 'UIX-038'], responsabilidad='Las combinaciones cumplen los mínimos de contraste de WCAG 2.2 AA.', corto='Contraste',
       verif=[('Pares de tokens', f'Se mide con una herramienta de contraste cada par de texto y fondo, y de borde y fondo, de los tokens semánticos. Las combinaciones aprobadas están en {M("KYN-MRK-COL-005")}.',
               'cada par alcanza el mínimo de la tabla; el foco queda como excepción pendiente hasta su decisión.')], ver='tecnica'),

    seccion('ejemplo', '08', 'Ejemplo de aplicación', 'Un error de formulario',
            'Un error de formulario utiliza <strong>un indicador semántico, texto explicativo</strong> y una relación visual clara con el campo.', [
        stack([('Señales', ['Borde del campo con el color de error, ícono de advertencia y mensaje debajo: «Ingrese una fecha posterior a hoy».'])]),
    ]),
    validacion('03.02', C8, 'El capítulo se comprueba cuando <strong>los estados pueden distinguirse visualmente y comprenderse sin depender únicamente del color</strong>.'),
]

# ═════════════ 09 · Tipografía ═════════════
CAP09 = [
    n9('KYN-SDI-FUI-008', 'Sistema tipográfico', 1, 'Familias, pesos y escala tipográfica',
       'Define qué letra usa la interfaz y en qué tamaños: <strong>la tipografía oficial, con la escala del libro</strong>.', [
        req(N('Las interfaces deben utilizar las familias, pesos y criterios tipográficos oficiales de Keyons o el tema aprobado para el producto.', 'debe')),
        matriz('Escala aplicada a la interfaz (propuesta)', [('Tamaño', 'Token'), ('Uso', '')], [
            ('Título de pantalla', [f'{c("--fs-24")} o {c("--fs-32")}', 'Uno por pantalla.']),
            ('Título de sección', [c('--fs-20'), 'Grupos y paneles.']),
            ('Cuerpo y valores', [c('--fs-16'), 'Texto corrido, campos y celdas.']),
            ('Etiquetas', [c('--fs-14'), 'Rótulos de campos, botones y menús.']),
            ('Ayudas y metadatos', [c('--fs-12'), 'Fechas, contadores y notas breves.'])]),
        detalle([('Notas técnicas', [
            ('Familias', f'{c("--font-sans")} para la interfaz; {c("--font-display")} solo en títulos expresivos.'),
            ('Cifras', 'Las cifras de tablas e indicadores usan números tabulares para alinearse.'),
            ('Escala', f'La escala viene de {M("KYN-MRK-TYP-002")}. La asignación por uso es una propuesta.')])]),
    ], origen=['Sistema tipográfico (base)'], responsabilidad='Las interfaces usan las familias, pesos y escala oficiales.', corto='Sistema tipográfico',
       rel=['KYN-MRK-TYP-006'], verif=[('Inventario', 'Se revisa cada texto de una pantalla con el inspector del navegador.', 'cada uno usa un tamaño de la escala y su familia oficial.')]),

    n9('KYN-SDI-FUI-009', 'Jerarquía consistente', 2, 'Jerarquía de las funciones de texto',
       'Se aplica a títulos, etiquetas, valores y ayudas: <strong>la misma función conserva el mismo aspecto</strong> en todas las pantallas.', [
        req(N('Títulos, etiquetas, valores, ayudas y textos operativos deben mantener diferencias reconocibles de función y jerarquía.', 'debe')),
        stack([('Diferencias', ['La jerarquía combina tamaño, peso y color de la escala, y nunca depende de un solo rasgo.']),
               ('Etiqueta y valor', ['La etiqueta va en gris secundario y el valor en el color principal del texto.'])]),
    ], origen=['Jerarquía consistente (base)'], responsabilidad='Cada función de texto mantiene un aspecto reconocible.', corto='Jerarquía',
       verif=[('Comparación', 'Se compara un mismo tipo de texto en dos pantallas distintas.', 'tiene el mismo tamaño, peso y color.')]),

    n9('KYN-SDI-FUI-010', 'Legibilidad', 3, 'Legibilidad con ampliación y espaciado',
       'Se aplica a todo texto de la interfaz: <strong>se lee con ampliación, con más espaciado y en cualquier ancho</strong>.', [
        req(N('Los textos deben conservar legibilidad con ampliación, ajustes de espaciado y diferentes tamaños de pantalla.', 'debe')),
        matriz('Criterios de WCAG 2.2 AA para el texto', [('Qué se comprueba', ''), ('Criterio', '')], [
            ('Ampliación', ['El texto se amplía al 200 % sin perder contenido ni funciones.', '1.4.4']),
            ('Adaptación', ['A 320 px de ancho, el contenido se lee sin desplazamiento horizontal.', '1.4.10']),
            ('Espaciado', ['Con interlineado 1,5, párrafos al doble, letras +0,12 y palabras +0,16, nada se corta ni se superpone.', '1.4.12'])]),
        detalle([('Notas técnicas', [
            ('Medidas', 'Tamaños en unidades relativas; las cajas de texto crecen con su contenido.'),
            ('Medida de lectura', 'El texto corrido respeta 600 px (Guía 05, Sistema de diagramación).')])]),
    ], origen=['Legibilidad (base)'], responsabilidad='El texto se lee con ampliación, espaciado y en cualquier pantalla.', corto='Legibilidad',
       verif=[('Tres pruebas', 'Se aplican a cada pantalla la ampliación al 200 %, el ancho de 320 px y el espaciado de texto aumentado.', 'se cumple cada fila de la tabla.')], ver='grupo'),

    n9('KYN-SDI-FUI-011', 'Truncamiento', 4, 'Textos truncados y su valor completo',
       'Se aplica cuando un texto no cabe en su espacio: <strong>se puede abreviar, pero el valor completo sigue disponible</strong>.', [
        req(N('La información necesaria para comprender o ejecutar una tarea no debe perderse definitivamente por truncamiento visual.', 'no-debe')),
        matriz('Cuándo y cómo se acorta', [('Se permite', ''), ('Cómo se recupera', '')], [
            ('Nombres en columnas estrechas', ['Sí, al final y con puntos suspensivos.', 'Valor completo al pasar el cursor, con el foco y en el detalle.']),
            ('Descripciones largas', ['Sí, en dos o tres líneas.', '«Ver más» o el detalle del registro.']),
            ('Cifras, fechas y códigos', ['Nunca.', 'La columna se ensancha o el valor pasa a otra línea.']),
            ('Mensajes de error y acciones', ['Nunca.', 'Se muestran completos.'])]),
    ], origen=['Truncamiento (base)'], responsabilidad='Lo acortado sigue disponible completo.', corto='Truncamiento',
       verif=[('Textos largos', 'Se cargan nombres y descripciones de longitud máxima.', 'el valor completo se puede leer en cada caso.')], ver='grupo'),

    seccion('ejemplo', '09', 'Ejemplo de aplicación', 'Un nombre largo en una tabla',
            'Una tabla puede abreviar un nombre en una columna estrecha, siempre que <strong>el valor completo siga estando disponible</strong>.', [
        stack([('Nombre largo', ['«Asociación de Propietarios del Residencial Las Palmas» se ve abreviado en la columna. El nombre completo aparece al pasar el cursor, con el foco y en el detalle.'])]),
    ]),
    validacion('03.03', C9, 'El capítulo se comprueba revisando <strong>textos largos, ampliación, espaciado aumentado y adaptación móvil</strong> en las mismas pantallas.'),
]

# ═════════════ 10 · Espacio y retícula ═════════════
CAP10 = [
    n10('KYN-SDI-FUI-012', 'Espaciado compartido', 1, 'Escala espacial de los componentes',
        'Define de dónde salen márgenes y separaciones: <strong>de la escala espacial oficial</strong>, que da un ritmo común a todas las pantallas.', [
        req(N('Los componentes deben aplicar la escala espacial oficial de Keyons y sus tokens correspondientes.', 'debe')),
        matriz('Escala espacial', [('Tokens', ''), ('Uso habitual en interfaz (propuesta)', '')], [
            ('4 a 12 px', [f'{c("--s1")}, {c("--s2")}, {c("--s3")}', 'Dentro de un control: ícono y texto, etiqueta y campo.']),
            ('16 a 24 px', [f'{c("--s4")}, {c("--s5")}, {c("--s6")}', 'Entre campos y entre filas de una lista.']),
            ('32 a 48 px', [f'{c("--s8")}, {c("--s10")}, {c("--s12")}', 'Entre grupos y secciones de una pantalla.']),
            ('64 px o más', [f'{c("--s16")} en adelante', 'Entre bloques mayores de una página.'])]),
        detalle([('Notas técnicas', [
            ('Origen', f'La escala es la de {M("KYN-MRK-ESP-003")}; la asignación por uso es una propuesta.')])]),
    ], origen=['Espaciado compartido (base)'], responsabilidad='Los componentes usan la escala espacial oficial.', corto='Espaciado',
       verif=[('Búsqueda en el código', 'Se buscan márgenes y separaciones escritos a mano en los componentes.', 'todos usan un valor de la escala.')]),

    n10('KYN-SDI-FUI-013', 'Agrupación semántica', 2, 'Proximidad según la relación funcional',
        'Se aplica a etiquetas, campos, títulos, acciones y resultados: <strong>la distancia dice qué va junto</strong>.', [
        req(N('La proximidad entre elementos debe reflejar su relación funcional: etiqueta y campo, título y contenido, acción y resultado.', 'debe')),
        stack([('Grupos', ['El espacio dentro de un grupo es menor que el espacio entre grupos.']),
               ('Acción y resultado', ['El mensaje de resultado aparece junto a la acción o al elemento afectado.'])]),
    ], origen=['Agrupación semántica (base)'], responsabilidad='La proximidad refleja la relación funcional.', corto='Agrupación',
       verif=[('Agrupación', 'Se pide a la persona que señale qué elementos van juntos, sin leer las etiquetas.', 'coincide con los grupos definidos.')], ver='grupo'),

    n10('KYN-SDI-FUI-014', 'Composición adaptable', 3, 'Retícula adaptable, densidad y esquinas',
        'Se aplica cuando cambia el ancho o la densidad de una pantalla: <strong>cambia la disposición y la tarea sigue completa</strong>.', [
        req(N('Las retículas deben reorganizarse sin producir solapamientos, pérdida de controles ni recortes que impidan completar tareas.', 'debe')),
        stack([('Retícula', [f'Columnas, márgenes y medianiles siguen {M("KYN-MRK-ESP-004")}.']),
               ('Densidad', ['Modo cómodo y modo denso; el predeterminado depende de la frecuencia de uso del perfil.']),
               ('Esquinas', [f'Radios de la escala: {c("--r-control")} en controles, {c("--r-component")} en componentes y {c("--r-card")} en tarjetas.'])]),
    ], origen=['Composición adaptable (base)', 'Densidad y esquinas (descripción del capítulo)', 'UIX-029'],
       responsabilidad='La retícula se adapta sin solapamientos ni pérdidas, con densidad y esquinas oficiales.', corto='Adaptación',
       rel=['KYN-MRK-ESP-002', 'KYN-MRK-ESP-005', 'KYN-SDI-PEX-009'], verif=[('Cuatro casos', 'Se prueban contenido largo, estados de error, anchos de 320 a 1440 px y los dos modos de densidad.', 'sin solapamientos ni controles perdidos.')], ver='grupo'),

    seccion('ejemplo', '10', 'Ejemplo de aplicación', 'Un formulario agrupado',
            'En un formulario, <strong>cada etiqueta permanece asociada visualmente a su campo</strong> y los grupos de información son reconocibles.', [
        stack([('Grupos', ['«Datos del residente» y «Datos de la vivienda» se separan con 32 px. Dentro de cada grupo hay 16 px entre campos y 8 px entre la etiqueta y su campo.'])]),
    ]),
    validacion('03.04', C10, 'El capítulo se comprueba con <strong>contenido largo, estados de error, distintos anchos y variaciones de densidad</strong>.'),
]

CAPITULOS = [
    ('03', '03.01', C7, CAP07, None),
    ('03', '03.02', C8, CAP08, None),
    ('03', '03.03', C9, CAP09, None),
    ('03', '03.04', C10, CAP10, None),
]
