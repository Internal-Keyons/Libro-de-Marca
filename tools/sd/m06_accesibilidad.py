"""Módulo 06 · Accesibilidad (ACC): 20 Percepción, 21 Operación y 22 Adaptación.
Requisitos: textos de Keylin (docs/sd/fuente-keylin-2026-11-17.md). ACC-001 reescribe el verbo para meter DEBE dentro de la frase
(mismo criterio aprobado para los cinco DEBE del 2026-11-17; requiere su visto bueno). Criterios de WCAG 2.2 citados por número.
"""
from .base import N, req, stack, matriz, detalle, c, L, M, norma, seccion, R, validacion, dims

MOD = 'accesibilidad-adaptacion'
C20, C21, C22 = 'accesibilidad-perceptiva', 'accesibilidad-operativa', 'adaptacion-de-la-experiencia'
def n20(nid, nombre, k, *a, **kw): return norma(nid, nombre, '06.01', MOD, C20, k, *a, **kw)
def n21(nid, nombre, k, *a, **kw): return norma(nid, nombre, '06.02', MOD, C21, k, *a, **kw)
def n22(nid, nombre, k, *a, **kw): return norma(nid, nombre, '06.03', MOD, C22, k, *a, **kw)


# ═════════════ 20 · Percepción ═════════════
CAP20 = [
    n20('KYN-SDI-ACC-001', 'Referencia de conformidad', 1, 'WCAG 2.2 AA como referencia de conformidad',
        'Define el mínimo de accesibilidad de todo producto web de Keyons: <strong>WCAG 2.2 nivel AA</strong>, comprobado con herramientas y con personas.', [
        req(N('Los productos web de Keyons deben diseñarse y verificarse tomando WCAG 2.2 nivel AA como objetivo mínimo de accesibilidad.', 'debe')),
        stack([('Alcance', ['Todas las pantallas, estados y documentos que el producto genera.']),
               ('Declaración', [f'Cada producto registra su nivel alcanzado y las excepciones justificadas, con su plan de corrección ({L("44")}).'])]),
    ], verif=[('Revisión doble', 'Se revisa cada pantalla con una herramienta automática y, después, a mano con teclado y lector de pantalla.', 'ningún criterio AA queda incumplido; la herramienta sola no alcanza para darlo por cumplido.')], ver='breve',
       origen=['Referencia de conformidad (base)', 'UIX-038'], responsabilidad='Los productos web se diseñan y verifican con WCAG 2.2 AA como mínimo.', corto='Conformidad'),

    n20('KYN-SDI-ACC-002', 'Información perceptible', 2, 'Alternativas para cada recurso sensorial',
        'Se aplica a imágenes, colores, sonidos y controles: <strong>el significado llega por más de un sentido</strong>.', [
        req(N('Los contenidos y controles deben ofrecer contraste, etiquetas y alternativas apropiadas para que su significado no dependa de un único recurso sensorial.', 'debe')),
        matriz('Alternativas por tipo de contenido', [('Alternativa', ''), ('Criterio', 'WCAG')], [
            ('Imagen informativa', ['Texto alternativo que dice lo que la imagen comunica.', '1.1.1']),
            ('Imagen decorativa', [f'Texto alternativo vacío ({c("alt=" + chr(34) + chr(34))}).', '1.1.1']),
            ('Gráfico de datos', [f'Valores accesibles en tabla o texto ({L("27")}).', '1.1.1']),
            ('Color con significado', [f'Ícono, texto o forma además del color ({R("KYN-SDI-FUI-005", "Estados semánticos")}).', '1.4.1']),
            ('Audio o video', ['Subtítulos y transcripción.', '1.2'])]),
    ], verif=[('Sin imágenes ni color', 'Se recorre la pantalla con imágenes desactivadas y en escala de grises.', 'el significado se mantiene.')], ver='grupo',
       origen=['Información perceptible (base)'], responsabilidad='El significado no depende de un único recurso sensorial.', corto='Perceptible',
       cita=f'08 Color funcional ({R("KYN-SDI-FUI-007", "Contraste")}) fija los mínimos de contraste'),

    n20('KYN-SDI-ACC-003', 'Lectura adaptable', 3, 'Ampliación y ajustes de presentación',
        'Se aplica cuando la persona amplía la pantalla o ajusta el texto: <strong>el contenido y las funciones se conservan</strong>.', [
        req(N('La interfaz debe conservar su contenido y funcionalidad ante ampliación y ajustes de presentación, conforme a los criterios aplicables.', 'debe')),
        stack([('Criterios', ['Ampliación al 200 % (1.4.4), adaptación a 320 px sin desplazamiento horizontal (1.4.10) y espaciado de texto (1.4.12).']),
               ('Desarrollo', [f'Las decisiones de texto están en Legibilidad, en {L("09")}.'])]),
    ], verif=[('Tres pruebas', 'Se aplican ampliación al 200 % y al 400 %, ancho de 320 px y espaciado de texto aumentado.', 'sin pérdida de contenido ni de funciones.')], ver='grupo',
       origen=['Lectura adaptable (base)'], responsabilidad='La interfaz conserva contenido y funciones con ampliación y ajustes de texto.', corto='Lectura adaptable',
       cita=f'09 Tipografía ({R("KYN-SDI-FUI-010", "Legibilidad")}) desarrolla las decisiones de texto'),

    seccion('ejemplo', '20', 'Ejemplo de aplicación', 'Un indicador de estado',
            'Un estado «Vencido» se reconoce <strong>por su ícono y su texto</strong>, además de su color.', [
    ]),
    validacion('06.01', C20, 'El capítulo se comprueba con <strong>contraste, ampliación, texto, alternativas y tecnologías de asistencia</strong>.'),
]

# ═════════════ 21 · Operación ═════════════
CAP21 = [
    n21('KYN-SDI-ACC-004', 'Teclado', 1, 'Uso completo con teclado',
        'Se aplica a toda función interactiva: <strong>lo que se hace con el puntero se hace con el teclado</strong>.', [
        req(N('Todas las funciones interactivas deben poder utilizarse mediante teclado cuando corresponda a su plataforma.', 'debe')),
        matriz('Teclas esperadas', [('Teclas', ''), ('Dónde', '')], [
            ('Recorrer', ['Tab y Mayús + Tab.', 'Entre controles, en el orden visual.']),
            ('Activar', ['Enter en enlaces; Enter y Espacio en botones.', 'Todos los controles.']),
            ('Moverse dentro', ['Flechas, Inicio y Fin.', 'Menús, pestañas, listas y opciones.']),
            ('Salir', ['Escape.', 'Menús, diálogos y paneles; el foco vuelve al control que los abrió.'])]),
        detalle([
            ('Notas técnicas', [
                ('Trampas', 'Ningún componente atrapa el foco, salvo un diálogo modal mientras está abierto (2.1.2).'),
                ('Atajos', 'Los atajos de una sola tecla se pueden desactivar o cambiar (2.1.4).')])]),
    ], verif=[('Sin ratón', 'Se completan las tareas principales solo con teclado.', 'todas se completan, sin trampas de foco.')], ver='tecnica',
       origen=['Teclado (base)', 'UIX-038'], responsabilidad='Todas las funciones interactivas se usan con teclado.', corto='Teclado',
       cita=f'05 Navegación ({R("KYN-SDI-ARQ-008", "Identificación de controles")}) desarrolla el teclado de los menús'),

    n21('KYN-SDI-ACC-005', 'Foco identificable', 2, 'Indicador de foco visible',
        'Se aplica a todo control que recibe el foco: <strong>siempre se ve dónde está</strong>.', [
        req(N('El foco debe ser perceptible y no quedar completamente oculto por otros elementos de la interfaz.', 'debe')),
        stack([('Indicador', [f'Anillo de 2 px en Azul Noche, separado del borde, visible con el teclado (:focus-visible). La decisión sobre {c("--color-focus")} está pendiente en {R("KYN-SDI-FUI-007")}.']),
               ('Sin ocultarse', ['Cabeceras fijas, avisos y paneles no tapan el elemento con foco (2.4.11).']),
               ('Orden', ['El foco sigue el orden visual y lógico de la página (2.4.3).'])]),
    ], verif=[('Recorrido', 'Se recorre la página con Tab con la cabecera fija visible.', 'el foco se ve completo en cada paso.'), ('Contraste del indicador', 'Se mide el anillo de foco contra su fondo.', 'alcanza 3:1 (WCAG 1.4.11).')], ver='tecnica',
       origen=['Foco identificable (base)'], responsabilidad='El foco es perceptible, sigue el orden lógico y no queda oculto.', corto='Foco'),

    n21('KYN-SDI-ACC-006', 'Tiempo y movimiento', 3, 'Límites de tiempo y movimiento',
        'Se aplica a sesiones con tiempo, contenidos que se mueven y animaciones: <strong>la persona controla el tiempo y el movimiento</strong>.', [
        req(N('Las interacciones deben respetar los criterios de accesibilidad relacionados con límites de tiempo, movimiento y control de contenido.', 'debe')),
        matriz('Tiempo y movimiento', [('Decisión', ''), ('Criterio', 'WCAG')], [
            ('Límites de tiempo', [f'Se avisa antes y se puede extender; la sesión conserva los datos ({R("KYN-SDI-PAT-002", "Prevención de pérdidas")}).', '2.2.1']),
            ('Contenido que se mueve o se actualiza solo', ['Se puede pausar, detener u ocultar.', '2.2.2']),
            ('Destellos', ['Nada destella más de tres veces por segundo.', '2.3.1']),
            ('Animaciones', [f'Respetan la preferencia de movimiento reducido ({L("39")}).', '2.3.3, recomendado'])]),
    ], verif=[('Movimiento reducido', 'Se activa la preferencia de movimiento reducido del sistema.', 'las animaciones no esenciales se detienen.'), ('Sesión por vencer', 'Se deja una sesión hasta el aviso de vencimiento.', 'aparece el aviso con la opción de extender el tiempo.')], ver='tecnica',
       origen=['Tiempo y movimiento (base)'], responsabilidad='Se respetan los límites de tiempo, el control del movimiento y los destellos.', corto='Tiempo y movimiento'),

    seccion('ejemplo', '21', 'Ejemplo de aplicación', 'Una tarea sin ratón',
            'Una persona aprueba una solicitud <strong>solo con el teclado</strong>, desde el menú hasta la confirmación.', [
        stack([('Verificación del capítulo', ['Completar recorridos sin ratón y comprobar orden de foco, controles y recuperación.'])]),
    ]),
]

# ═════════════ 22 · Adaptación ═════════════
CAP22 = [
    n22('KYN-SDI-ACC-007', 'Diseño adaptable', 1, 'Funciones completas en cualquier ancho',
        'Se aplica a toda pantalla en móvil, tableta y escritorio: <strong>cambia la disposición y se conservan las funciones</strong>.', [
        req(N('Las pantallas deben reorganizarse según el espacio disponible sin eliminar funcionalidades esenciales.', 'debe')),
        stack([('Cómo se reorganiza', [f'Según la retícula de {L("10")} y la navegación de {L("05")}.']),
               ('Orientación', ['La pantalla funciona en vertical y en horizontal, salvo que una orientación sea esencial (1.3.4).'])]),
    ], verif=[('Anchos', 'Se recorre cada tarea a 320, 768, 1024 y 1440 px.', 'las funciones esenciales están en todos los anchos.')], ver='tecnica',
       origen=['Diseño adaptable (base)'], responsabilidad='Las pantallas se reorganizan sin eliminar funciones esenciales.', corto='Diseño adaptable'),

    n22('KYN-SDI-ACC-008', 'Interacciones accesibles', 2, 'Tamaño y separación de los objetivos',
        'Se aplica a todo elemento que se toca o se pulsa: <strong>el tamaño y la separación evitan los toques equivocados</strong>.', [
        req(N('Los objetivos interactivos deben cumplir los criterios aplicables de tamaño y separación de WCAG 2.2 AA.', 'debe')),
        matriz('Tamaño de los objetivos', [('Tamaño', ''), ('Estado', '')], [
            ('WCAG 2.2 AA · 2.5.8', ['24 × 24 px CSS como mínimo, o espacio suficiente alrededor.', 'Obligatorio.']),
            ('WCAG AAA · 2.5.5', ['44 × 44 px CSS.', 'Recomendación del estándar.']),
            ('Preferencia Keyons', ['44 × 44 px en los controles táctiles principales, cuando el espacio lo permite.', 'Propuesta; requiere aprobación.'])]),
        detalle([
            ('Excepciones de 2.5.8', [
                ('Cuáles', 'Enlaces dentro de un texto, controles del navegador, objetivos con un equivalente que cumple y presentaciones esenciales.')])]),
    ], verif=[('Medición', 'Se mide el menor objetivo interactivo de cada pantalla.', '24 × 24 px CSS como mínimo, o una excepción documentada.')], ver='breve',
       origen=['Interacciones accesibles (base)', 'UIX-038', 'UIX-039 (44 px, revisado)'],
       responsabilidad='Los objetivos cumplen el tamaño y la separación de WCAG 2.2 AA; 44 px es una preferencia por aprobar.', corto='Objetivos'),

    n22('KYN-SDI-ACC-009', 'Variaciones de uso', 3, 'Dispositivos, entradas y condiciones de uso',
        'Se aplica al definir dónde y cómo se usa un producto: <strong>la misma tarea con distintas manos y pantallas</strong>.', [
        req(N('Las experiencias deberían considerar dispositivos, métodos de entrada y condiciones operativas diferentes.', 'deberia')),
        matriz('Variaciones a considerar', [('Qué se decide', ''), ('Ejemplo', '')], [
            ('Métodos de entrada', ['Puntero, toque, teclado y voz.', 'Ninguna función exige un gesto complejo sin alternativa (2.5.1).']),
            ('Preferencias del sistema', ['Movimiento reducido, tamaño de texto y modo de alto contraste.', 'La interfaz respeta las preferencias del dispositivo.']),
            ('Condiciones', ['Una sola mano, luz exterior, conexión lenta.', 'Acciones principales al alcance del pulgar en móvil (desde UIX-039).']),
            ('Capacidades', ['Visión, audición, motricidad y atención.', f'Perfiles con atención variable ({R("KYN-SDI-PEX-007", "Diseñar para quienes utilizan el producto")}).'])]),
    ], verif=[('Matriz de uso', 'Se prueba cada tarea principal con dos métodos de entrada como mínimo y con las preferencias del sistema activadas.', 'la tarea se completa en cada combinación.')], ver='breve',
       origen=['Variaciones de uso (base)', 'Preferencias del sistema y distintas capacidades (descripción del capítulo)', 'UIX-039'],
       responsabilidad='Las experiencias consideran dispositivos, métodos de entrada, preferencias y condiciones.', corto='Variaciones'),

    seccion('ejemplo', '22', 'Ejemplo de aplicación', 'El mismo registro en tres pantallas',
            'Un registro se crea igual en escritorio, tableta y móvil, <strong>con los mismos datos y acciones</strong>.', [
        stack([('Verificación del capítulo', ['Móvil, escritorio, zoom, orientación y métodos de interacción disponibles.'])]),
    ]),
]

CAPITULOS = [
    ('06', '06.01', C20, CAP20, None),
    ('06', '06.02', C21, CAP21, None),
    ('06', '06.03', C22, CAP22, None),
]
