"""Módulo 03 · Fundamentos (FUI): 07 Tokens, 08 Color funcional, 09 Tipografía y 10 Espacio y retícula.
Requisitos: textos de Keylin (docs/sd/fuente-keylin-2026-11-17.md). Decisiones, comportamientos, excepciones y verificaciones:
propuesta de Claude en borrador. Los valores citan los tokens reales de css/tokens.css y las normas del Libro de Marca.
"""
from .base import N, req, stack, matriz, detalle, c, L, M, norma, seccion

MOD = 'fundamentos-interfaz'
C7, C8, C9, C10 = 'tokens-de-diseno', 'color-funcional', 'tipografia-aplicada', 'espacio-reticula-y-geometria'
def n7(nid, nombre, k, *a, **kw): return norma(nid, nombre, '03.01', MOD, C7, k, *a, **kw)
def n8(nid, nombre, k, *a, **kw): return norma(nid, nombre, '03.02', MOD, C8, k, *a, **kw)
def n9(nid, nombre, k, *a, **kw): return norma(nid, nombre, '03.03', MOD, C9, k, *a, **kw)
def n10(nid, nombre, k, *a, **kw): return norma(nid, nombre, '03.04', MOD, C10, k, *a, **kw)


# ═════════════ 07 · Tokens ═════════════
CAP07 = [
    n7('KYN-SDI-FUI-001', 'Fuente única de valores', 1, 'Cada valor compartido vive en un token',
       'Un valor se cambia <strong>en un solo lugar</strong>.', [
        req(N('Los componentes deben utilizar tokens oficiales para los valores visuales y funcionales compartidos, evitando valores arbitrarios repetidos en el código.', 'debe')),
        matriz('Tres niveles de token', [('Qué guarda', ''), ('Ejemplo real', 'css/tokens.css')], [
            ('Base', ['El valor crudo de la paleta, las escalas y las medidas.', f'{c("--k-cielo-500")}, {c("--k-noche-900")}, {c("--s4")}']),
            ('Semántico', ['El rol del valor en la interfaz.', f'{c("--color-text")}, {c("--color-border")}, {c("--color-status-error")}']),
            ('De componente', ['Una decisión propia de un componente, apoyada en un semántico.', f'{c("--r-control")}, {c("--line-w-control")}'])]),
        stack([('Uso', ['Los componentes leen tokens semánticos o de componente; los de base solo se usan para definir otros tokens.']),
               ('Nomenclatura', [f'Prefijo por categoría y rol, del general al particular: {c("--color-text-2")}, {c("--color-border-strong")}, {c("--fs-16")}.'])]),
        detalle([
            ('Verificación', [
                ('Búsqueda', 'En el código de los componentes no aparecen colores, medidas ni radios escritos a mano, salvo en el archivo de tokens.'),
                ('Cambio de prueba', f'Se cambia {c("--color-text")} en una rama de prueba. Resultado esperado: todos los textos responden y nada más cambia.')])]),
    ], origen=['Fuente única de valores (base)', 'Tokens semánticos oficiales (matriz)', 'UIX-011'],
       responsabilidad='Los componentes usan tokens oficiales para todo valor compartido.', corto='Fuente única'),

    n7('KYN-SDI-FUI-002', 'Roles semánticos', 2, 'El token dice para qué sirve, no qué color es',
       'Un nombre por función <strong>sobrevive a un cambio de tema</strong>.', [
        req(N('Los tokens deben describir su función, como superficie, texto, borde, foco, acción o estado, en lugar de depender únicamente del nombre de un color.', 'debe')),
        matriz('Roles semánticos y sus tokens', [('Tokens', 'css/tokens.css'), ('Para qué', '')], [
            ('Superficie', [f'{c("--color-bg")}, {c("--color-surface")}, {c("--color-inverse")}', 'Fondos de página, de componentes y de bloques invertidos.']),
            ('Texto', [f'{c("--color-text")}, {c("--color-text-2")}, {c("--color-text-3")}, {c("--color-text-disabled")}', 'Jerarquía de lectura y estado deshabilitado.']),
            ('Borde', [f'{c("--color-border")}, {c("--color-border-strong")}', 'Divisores y contornos de controles.']),
            ('Foco', [c('--color-focus'), 'El indicador de foco. Ver la decisión pendiente en FUI-007.']),
            ('Acción', ['Pendiente: hoy no hay token de acción propio.', f'El botón principal usa los colores de {M("KYN-MRK-COL-015")}. Se propone {c("--color-action")} y {c("--color-on-action")}.']),
            ('Estado', [f'{c("--color-status-success")}, {c("--color-status-warning")}, {c("--color-status-error")}, {c("--color-status-info")}, {c("--color-status-review")}', 'Confirmaciones, avisos, errores, información y revisión (FUI-005).'])]),
        detalle([
            ('Temas', [
                ('Cómo funciona', 'Un tema redefine los tokens semánticos; los de base y los componentes no cambian.'),
                ('Estado', 'El tema claro es el actual. El tema oscuro y los temas de cliente (38 White-label) están pendientes.')]),
            ('Verificación', [
                ('Revisión de nombres', 'Ningún componente usa un token con nombre de color para expresar una función.')])]),
    ], origen=['Roles semánticos (base)', 'Temas claro y oscuro (pendiente de la matriz)'],
       responsabilidad='Los tokens se nombran por su función y permiten cambiar de tema.', corto='Roles semánticos'),

    n7('KYN-SDI-FUI-003', 'Cambios controlados', 3, 'Un token compartido se cambia con su revisión',
       'Un cambio en un token <strong>llega a todos los productos</strong>.', [
        req(N('Una modificación de tokens compartidos debe comprobarse en los componentes y productos afectados antes de aprobarse.', 'debe')),
        stack([('Procedimiento', ['Propuesta con el motivo, lista de componentes y productos afectados, revisión visual en cada uno y aprobación.']),
               ('Versión', [f'Cada cambio publicado lleva su versión y su nota de cambios ({L("45")}).']),
               ('Aprobación', [f'Los cambios en tokens compartidos se aprueban según {L("42")}.'])]),
        detalle([
            ('Verificación', [
                ('Antes y después', 'Se capturan las pantallas clave de cada producto afectado antes y después del cambio. Resultado esperado: solo cambia lo previsto.')])]),
    ], origen=['Cambios controlados (base)', 'UIX-011'],
       responsabilidad='Los cambios de tokens se comprueban en componentes y productos antes de aprobarse.', corto='Cambios controlados'),

    seccion('ejemplo', '07', 'Ejemplo de aplicación', 'Un botón principal',
            'Un botón usa <strong>tokens de acción y de texto sobre acción</strong>, no un color hexadecimal escrito en cada pantalla.', [
        stack([('Hoy', [f'El fondo y el texto del botón salen de {M("KYN-MRK-COL-015")}; falta su token semántico propio (FUI-002).']),
               ('Verificación del capítulo', ['Los componentes reutilizables heredan los valores correctos y los cambios no provocan regresiones en otras vistas.'])]),
    ]),
]

# ═════════════ 08 · Color funcional ═════════════
CAP08 = [
    n8('KYN-SDI-FUI-004', 'Color con función', 1, 'Cada color de la interfaz cumple una función',
       'El color <strong>informa antes de decorar</strong>.', [
        req(N('Cada color aplicado a una interfaz debe cumplir una función de identidad, jerarquía, acción, estado o diferenciación de información.', 'debe')),
        matriz('Funciones del color en pantalla', [('Colores', ''), ('Norma de origen', 'Libro de Marca')], [
            ('Identidad', ['Azul Noche y Azul Cielo, contenidos.', M('KYN-MRK-COL-012')]),
            ('Jerarquía', ['Grises tipográficos.', M('KYN-MRK-COL-013')]),
            ('Acción', ['El color del botón principal y los enlaces.', M('KYN-MRK-COL-015')]),
            ('Estado', ['Los colores de estado con su ícono.', M('KYN-MRK-COL-014')]),
            ('Datos', ['Las paletas de gráficos.', M('KYN-MRK-DAT-002')])]),
        detalle([
            ('Verificación', [
                ('Inventario', 'Se listan los colores de una pantalla y la función de cada uno. Resultado esperado: ninguno queda sin función.')])]),
    ], origen=['Color con función (base)'], responsabilidad='Cada color de la interfaz cumple una función identificable.', corto='Color con función'),

    n8('KYN-SDI-FUI-005', 'Estados semánticos', 2, 'Cada estado se reconoce sin depender del color',
       'El color acompaña; <strong>el ícono y el texto confirman</strong>.', [
        req(N('Los errores, advertencias y confirmaciones deben utilizar las funciones cromáticas oficiales y señales adicionales que permitan comprenderlos sin depender exclusivamente del color.', 'debe')),
        matriz('Estados y sus señales', [('Fondo', 'Token'), ('Señal adicional', '')], [
            ('Éxito', [c('--color-status-success'), 'Ícono de verificación y texto del resultado.']),
            ('Advertencia', [c('--color-status-warning'), 'Ícono de advertencia y qué conviene revisar.']),
            ('Error', [c('--color-status-error'), 'Ícono de advertencia, mensaje que explica y relación visible con el elemento afectado.']),
            ('Información', [c('--color-status-info'), 'Ícono de información.']),
            ('En revisión', [c('--color-status-review'), 'Etiqueta de texto.'])]),
        detalle([
            ('Notas técnicas', [
                ('Texto sobre el fondo de estado', 'Azul Noche, que cumple el contraste de lectura sobre los cinco fondos.'),
                ('Íconos', f'Del catálogo aprobado ({M("KYN-MRK-ICO-005")}).')]),
            ('Verificación', [
                ('Escala de grises', 'Con la pantalla en escala de grises, cada estado sigue distinguiéndose por su ícono y su texto.')])]),
    ], origen=['Estados semánticos (base)', 'UIX-038'], responsabilidad='Los estados usan el color oficial y una señal adicional.', corto='Estados'),

    n8('KYN-SDI-FUI-006', 'Separación de significados', 3, 'El error tiene su propio color',
       'Un color, <strong>un significado</strong>.', [
        req(N('Salmón Tierra no debe utilizarse como sustituto del color semántico de error.', 'no-debe')),
        stack([('Salmón Tierra', [f'Es un color de identidad y de acento expresivo ({M("KYN-MRK-COL-004")}).']),
               ('Error', [f'Usa {c("--color-status-error")} con su ícono y su mensaje (FUI-005).'])]),
        detalle([
            ('Verificación', [
                ('Revisión', 'Ningún mensaje de error ni campo inválido usa Salmón Tierra.')])]),
    ], origen=['Separación de significados (base)'], responsabilidad='Salmón Tierra no reemplaza al color de error.', corto='Significados'),

    n8('KYN-SDI-FUI-007', 'Contraste', 4, 'Cada combinación se lee y se distingue',
       'El contraste <strong>se mide, no se estima</strong>.', [
        req(N('Las combinaciones cromáticas deben respetar los criterios de contraste aplicables de WCAG 2.2 AA.', 'debe')),
        matriz('Mínimos de contraste de WCAG 2.2 AA', [('Mínimo', ''), ('Criterio', '')], [
            ('Texto normal', ['4,5:1', '1.4.3']),
            ('Texto grande (24 px, o 18,66 px en negrita)', ['3:1', '1.4.3']),
            ('Componentes, bordes de campos, íconos que informan y foco', ['3:1 contra lo que los rodea', '1.4.11']),
            ('Controles deshabilitados', ['Sin mínimo, pero legibles', 'Excepción de 1.4.3'])]),
        detalle([
            ('Decisión pendiente', [
                ('Color del foco', f'{c("--color-focus")} es Azul Cielo y sobre Blanco Keyons da 2,6:1, por debajo de 3:1. El libro usa hoy un anillo Azul Noche. Requiere aprobación: pasar el token a Azul Noche.')]),
            ('Verificación', [
                ('Pares de tokens', f'Se mide cada par de texto y fondo, y de borde y fondo, de los tokens semánticos. Las combinaciones aprobadas están en {M("KYN-MRK-COL-005")}.')])]),
    ], origen=['Contraste (base)', 'UIX-038'], responsabilidad='Las combinaciones cumplen los mínimos de contraste de WCAG 2.2 AA.', corto='Contraste'),

    seccion('ejemplo', '08', 'Ejemplo de aplicación', 'Un error de formulario',
            'Un error de formulario utiliza <strong>un indicador semántico, texto explicativo</strong> y una relación visual clara con el campo.', [
        stack([('Señales', ['Borde del campo con el color de error, ícono de advertencia y mensaje debajo: «Ingrese una fecha posterior a hoy».']),
               ('Verificación del capítulo', ['Los estados pueden distinguirse visualmente y comprenderse sin depender únicamente del color.'])]),
    ]),
]

# ═════════════ 09 · Tipografía ═════════════
CAP09 = [
    n9('KYN-SDI-FUI-008', 'Sistema tipográfico', 1, 'La interfaz usa la tipografía oficial',
       'Una sola voz tipográfica <strong>en todos los productos</strong>.', [
        req(N('Las interfaces deben utilizar las familias, pesos y criterios tipográficos oficiales de Keyons o el tema aprobado para el producto.', 'debe')),
        matriz('Escala aplicada a la interfaz (propuesta)', [('Tamaño', 'Token'), ('Uso', '')], [
            ('Título de pantalla', [f'{c("--fs-24")} o {c("--fs-32")}', 'Uno por pantalla.']),
            ('Título de sección', [c('--fs-20'), 'Grupos y paneles.']),
            ('Cuerpo y valores', [c('--fs-16'), 'Texto corrido, campos y celdas.']),
            ('Etiquetas', [c('--fs-14'), 'Rótulos de campos, botones y menús.']),
            ('Ayudas y metadatos', [c('--fs-12'), 'Fechas, contadores y notas breves.'])]),
        detalle([
            ('Notas técnicas', [
                ('Familias', f'{c("--font-sans")} para la interfaz; {c("--font-display")} solo en títulos expresivos. Su uso sigue {M("KYN-MRK-TYP-006")}.'),
                ('Cifras', 'Las cifras de tablas e indicadores usan números tabulares para alinearse.'),
                ('Escala', f'La escala viene de {M("KYN-MRK-TYP-002")}. La asignación por uso es una propuesta.')]),
            ('Verificación', [
                ('Inventario', 'Cada texto de una pantalla usa un tamaño de la escala y su familia oficial.')])]),
    ], origen=['Sistema tipográfico (base)'], responsabilidad='Las interfaces usan las familias, pesos y escala oficiales.', corto='Sistema tipográfico'),

    n9('KYN-SDI-FUI-009', 'Jerarquía consistente', 2, 'Cada función de texto se reconoce siempre igual',
       'La misma función, <strong>el mismo aspecto</strong>.', [
        req(N('Títulos, etiquetas, valores, ayudas y textos operativos deben mantener diferencias reconocibles de función y jerarquía.', 'debe')),
        stack([('Diferencias', ['La jerarquía combina tamaño, peso y color de la escala; no depende de un solo rasgo.']),
               ('Etiqueta y valor', ['La etiqueta va en gris secundario y el valor en el color principal del texto.'])]),
        detalle([
            ('Verificación', [
                ('Comparación', 'En dos pantallas distintas, un mismo tipo de texto tiene el mismo tamaño, peso y color.')])]),
    ], origen=['Jerarquía consistente (base)'], responsabilidad='Cada función de texto mantiene un aspecto reconocible.', corto='Jerarquía'),

    n9('KYN-SDI-FUI-010', 'Legibilidad', 3, 'El texto se lee con ampliación y en cualquier pantalla',
       'La lectura <strong>se adapta sin perder contenido</strong>.', [
        req(N('Los textos deben conservar legibilidad con ampliación, ajustes de espaciado y diferentes tamaños de pantalla.', 'debe')),
        matriz('Criterios de WCAG 2.2 AA para el texto', [('Qué se comprueba', ''), ('Criterio', '')], [
            ('Ampliación', ['El texto se amplía al 200 % sin perder contenido ni funciones.', '1.4.4']),
            ('Adaptación', ['A 320 px de ancho no hace falta desplazarse en horizontal.', '1.4.10']),
            ('Espaciado', ['Con interlineado 1,5, párrafos al doble, letras +0,12 y palabras +0,16, nada se corta ni se superpone.', '1.4.12'])]),
        detalle([
            ('Notas técnicas', [
                ('Medidas', 'Tamaños en unidades relativas; las cajas de texto crecen con su contenido.'),
                ('Medida de lectura', 'El texto corrido respeta 600 px (Guía 05, Sistema de diagramación).')]),
            ('Verificación', [
                ('Tres pruebas', 'Ampliación al 200 %, ancho de 320 px y espaciado de texto aumentado.')])]),
    ], origen=['Legibilidad (base)'], responsabilidad='El texto se lee con ampliación, espaciado y en cualquier pantalla.', corto='Legibilidad'),

    n9('KYN-SDI-FUI-011', 'Truncamiento', 4, 'Un texto acortado sigue disponible completo',
       'Abreviar <strong>no es perder información</strong>.', [
        req(N('La información necesaria para comprender o ejecutar una tarea no debe perderse definitivamente por truncamiento visual.', 'no-debe')),
        matriz('Cuándo y cómo se acorta', [('Se permite', ''), ('Cómo se recupera', '')], [
            ('Nombres en columnas estrechas', ['Sí, al final y con puntos suspensivos.', 'Valor completo al pasar el cursor, con el foco y en el detalle.']),
            ('Descripciones largas', ['Sí, en dos o tres líneas.', '«Ver más» o el detalle del registro.']),
            ('Cifras, fechas y códigos', ['No.', 'La columna se ensancha o el valor pasa a otra línea.']),
            ('Mensajes de error y acciones', ['No.', '—'])]),
        detalle([
            ('Verificación', [
                ('Textos largos', 'Se cargan nombres y descripciones de longitud máxima. Resultado esperado: el valor completo se puede leer en cada caso.')])]),
    ], origen=['Truncamiento (base)'], responsabilidad='Lo acortado sigue disponible completo.', corto='Truncamiento'),

    seccion('ejemplo', '09', 'Ejemplo de aplicación', 'Un nombre largo en una tabla',
            'Una tabla puede abreviar un nombre en una columna estrecha, siempre que <strong>el valor completo siga estando disponible</strong>.', [
        stack([('Verificación del capítulo', ['Se revisan textos largos, zoom, ampliación de espaciado y adaptación móvil.'])]),
    ]),
]

# ═════════════ 10 · Espacio y retícula ═════════════
CAP10 = [
    n10('KYN-SDI-FUI-012', 'Espaciado compartido', 1, 'Los espacios salen de la escala oficial',
        'Un ritmo común <strong>ordena todas las pantallas</strong>.', [
        req(N('Los componentes deben aplicar la escala espacial oficial de Keyons y sus tokens correspondientes.', 'debe')),
        matriz('Escala espacial', [('Tokens', ''), ('Uso habitual en interfaz (propuesta)', '')], [
            ('4 a 12 px', [f'{c("--s1")}, {c("--s2")}, {c("--s3")}', 'Dentro de un control: ícono y texto, etiqueta y campo.']),
            ('16 a 24 px', [f'{c("--s4")}, {c("--s5")}, {c("--s6")}', 'Entre campos y entre filas de una lista.']),
            ('32 a 48 px', [f'{c("--s8")}, {c("--s10")}, {c("--s12")}', 'Entre grupos y secciones de una pantalla.']),
            ('64 px o más', [f'{c("--s16")} en adelante', 'Entre bloques mayores de una página.'])]),
        detalle([
            ('Notas técnicas', [
                ('Origen', f'La escala es la de {M("KYN-MRK-ESP-003")}; la asignación por uso es una propuesta.')]),
            ('Verificación', [
                ('Búsqueda', 'Ningún margen ni separación de un componente usa un valor fuera de la escala.')])]),
    ], origen=['Espaciado compartido (base)'], responsabilidad='Los componentes usan la escala espacial oficial.', corto='Espaciado'),

    n10('KYN-SDI-FUI-013', 'Agrupación semántica', 2, 'Lo que está cerca está relacionado',
        'La distancia <strong>dice qué va junto</strong>.', [
        req(N('La proximidad entre elementos debe reflejar su relación funcional: etiqueta y campo, título y contenido, acción y resultado.', 'debe')),
        stack([('Regla de proximidad', ['El espacio dentro de un grupo es menor que el espacio entre grupos.']),
               ('Acción y resultado', ['El mensaje de resultado aparece junto a la acción o al elemento afectado.'])]),
        detalle([
            ('Verificación', [
                ('Agrupación', 'La persona señala qué elementos van juntos sin leer las etiquetas. Resultado esperado: coincide con los grupos definidos.')])]),
    ], origen=['Agrupación semántica (base)'], responsabilidad='La proximidad refleja la relación funcional.', corto='Agrupación'),

    n10('KYN-SDI-FUI-014', 'Composición adaptable', 3, 'La retícula se reorganiza sin perder nada',
        'Cambia la disposición; <strong>la tarea sigue completa</strong>.', [
        req(N('Las retículas deben reorganizarse sin producir solapamientos, pérdida de controles ni recortes que impidan completar tareas.', 'debe')),
        stack([('Retícula', [f'Columnas, márgenes y medianiles siguen {M("KYN-MRK-ESP-004")}.']),
               ('Densidad', [f'Modo cómodo y modo denso, con valor predeterminado según el perfil (PEX-009), según {M("KYN-MRK-ESP-005")}.']),
               ('Esquinas', [f'Radios de la escala: {c("--r-control")} en controles, {c("--r-component")} en componentes y {c("--r-card")} en tarjetas ({M("KYN-MRK-ESP-002")}).'])]),
        detalle([
            ('Verificación', [
                ('Cuatro casos', 'Contenido largo, estados de error, anchos de 320 a 1440 px y los dos modos de densidad. Resultado esperado: sin solapamientos ni controles perdidos.')])]),
    ], origen=['Composición adaptable (base)', 'Densidad y esquinas (descripción del capítulo)', 'UIX-029'],
       responsabilidad='La retícula se adapta sin solapamientos ni pérdidas, con densidad y esquinas oficiales.', corto='Adaptación'),

    seccion('ejemplo', '10', 'Ejemplo de aplicación', 'Un formulario agrupado',
            'En un formulario, <strong>cada etiqueta permanece asociada visualmente a su campo</strong> y los grupos de información son reconocibles.', [
        stack([('Verificación del capítulo', ['Se prueban contenido largo, estados de error, distintos anchos y variaciones de densidad.'])]),
    ]),
]

CAPITULOS = [
    ('03', '03.01', C7, CAP07, None),
    ('03', '03.02', C8, CAP08, None),
    ('03', '03.03', C9, CAP09, None),
    ('03', '03.04', C10, CAP10, None),
]
