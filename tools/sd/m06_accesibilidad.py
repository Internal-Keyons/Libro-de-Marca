"""Módulo 06 · Accesibilidad (ACC): 20 Percepción, 21 Operación y 22 Adaptación.
Requisitos: textos de Keylin (docs/sd/fuente-keylin-2026-11-17.md). ACC-001 reescribe el verbo para meter DEBE dentro de la frase
(mismo criterio aprobado para los cinco DEBE del 2026-11-17; requiere su visto bueno). Criterios de WCAG 2.2 citados por número.
"""
from .base import N, req, stack, matriz, detalle, c, L, M, norma, seccion

MOD = 'accesibilidad-adaptacion'
C20, C21, C22 = 'accesibilidad-perceptiva', 'accesibilidad-operativa', 'adaptacion-de-la-experiencia'
def n20(nid, nombre, k, *a, **kw): return norma(nid, nombre, '06.01', MOD, C20, k, *a, **kw)
def n21(nid, nombre, k, *a, **kw): return norma(nid, nombre, '06.02', MOD, C21, k, *a, **kw)
def n22(nid, nombre, k, *a, **kw): return norma(nid, nombre, '06.03', MOD, C22, k, *a, **kw)


# ═════════════ 20 · Percepción ═════════════
CAP20 = [
    n20('KYN-SDI-ACC-001', 'Referencia de conformidad', 1, 'WCAG 2.2 AA es el mínimo de todo producto web',
        'Un estándar común <strong>hace comparable la calidad</strong>.', [
        req(N('Los productos web de Keyons deben diseñarse y verificarse tomando WCAG 2.2 nivel AA como objetivo mínimo de accesibilidad.', 'debe')),
        stack([('Alcance', ['Todas las pantallas, estados y documentos que el producto genera.']),
               ('Declaración', [f'Cada producto registra su nivel alcanzado y las excepciones justificadas, con su plan de corrección ({L("44")}).'])]),
        detalle([
            ('Verificación', [
                ('Revisión doble', 'Herramienta automática y revisión manual con teclado y lector de pantalla. La automática sola no alcanza.')])]),
    ], origen=['Referencia de conformidad (base)', 'UIX-038'], responsabilidad='Los productos web se diseñan y verifican con WCAG 2.2 AA como mínimo.', corto='Conformidad'),

    n20('KYN-SDI-ACC-002', 'Información perceptible', 2, 'El significado llega por más de un sentido',
        'Nada depende <strong>de un solo recurso sensorial</strong>.', [
        req(N('Los contenidos y controles deben ofrecer contraste, etiquetas y alternativas apropiadas para que su significado no dependa de un único recurso sensorial.', 'debe')),
        matriz('Alternativas por tipo de contenido', [('Alternativa', ''), ('Criterio', 'WCAG')], [
            ('Imagen informativa', ['Texto alternativo que dice lo que la imagen comunica.', '1.1.1']),
            ('Imagen decorativa', [f'Texto alternativo vacío ({c("alt=" + chr(34) + chr(34))}).', '1.1.1']),
            ('Gráfico de datos', [f'Valores accesibles en tabla o texto ({L("27")}).', '1.1.1']),
            ('Color con significado', ['Ícono, texto o forma además del color (FUI-005).', '1.4.1']),
            ('Audio o video', ['Subtítulos y transcripción.', '1.2'])]),
        detalle([
            ('Verificación', [
                ('Sin imágenes ni color', 'Se recorre la pantalla con imágenes desactivadas y en escala de grises. Resultado esperado: el significado se mantiene.')])]),
    ], origen=['Información perceptible (base)'], responsabilidad='El significado no depende de un único recurso sensorial.', corto='Perceptible',
       cita='08 Color funcional (FUI-007) fija los mínimos de contraste'),

    n20('KYN-SDI-ACC-003', 'Lectura adaptable', 3, 'La interfaz resiste la ampliación y los ajustes de texto',
        'Cada persona <strong>ajusta la lectura a su medida</strong>.', [
        req(N('La interfaz debe conservar su contenido y funcionalidad ante ampliación y ajustes de presentación, conforme a los criterios aplicables.', 'debe')),
        stack([('Criterios', ['Ampliación al 200 % (1.4.4), adaptación a 320 px sin desplazamiento horizontal (1.4.10) y espaciado de texto (1.4.12).']),
               ('Desarrollo', [f'Las decisiones de texto están en Legibilidad, en {L("09")}.'])]),
        detalle([
            ('Verificación', [
                ('Tres pruebas', 'Ampliación al 200 % y al 400 %, ancho de 320 px y espaciado de texto aumentado. Resultado esperado: sin pérdida de contenido ni de funciones.')])]),
    ], origen=['Lectura adaptable (base)'], responsabilidad='La interfaz conserva contenido y funciones con ampliación y ajustes de texto.', corto='Lectura adaptable',
       cita='09 Tipografía (FUI-010) desarrolla las decisiones de texto'),

    seccion('ejemplo', '20', 'Ejemplo de aplicación', 'Un indicador de estado',
            'Un estado «Vencido» se reconoce <strong>por su ícono y su texto</strong>, además de su color.', [
        stack([('Verificación del capítulo', ['Contraste, zoom, texto, alternativas y pruebas con tecnologías de asistencia.'])]),
    ]),
]

# ═════════════ 21 · Operación ═════════════
CAP21 = [
    n21('KYN-SDI-ACC-004', 'Teclado', 1, 'Todo lo que se hace con el puntero se hace con el teclado',
        'El teclado <strong>es una forma completa de usar el producto</strong>.', [
        req(N('Todas las funciones interactivas deben poder utilizarse mediante teclado cuando corresponda a su plataforma.', 'debe')),
        matriz('Teclas esperadas', [('Teclas', ''), ('Dónde', '')], [
            ('Recorrer', ['Tab y Mayús + Tab.', 'Entre controles, en el orden visual.']),
            ('Activar', ['Enter en enlaces; Enter y Espacio en botones.', 'Todos los controles.']),
            ('Moverse dentro', ['Flechas, Inicio y Fin.', 'Menús, pestañas, listas y opciones.']),
            ('Salir', ['Escape.', 'Menús, diálogos y paneles; el foco vuelve al control que los abrió.'])]),
        detalle([
            ('Notas técnicas', [
                ('Trampas', 'Ningún componente atrapa el foco, salvo un diálogo modal mientras está abierto (2.1.2).'),
                ('Atajos', 'Los atajos de una sola tecla se pueden desactivar o cambiar (2.1.4).')]),
            ('Verificación', [
                ('Sin ratón', 'Se completan las tareas principales solo con teclado. Resultado esperado: todas se completan.')])]),
    ], origen=['Teclado (base)', 'UIX-038'], responsabilidad='Todas las funciones interactivas se usan con teclado.', corto='Teclado',
       cita='05 Navegación (ARQ-008) desarrolla el teclado de los menús'),

    n21('KYN-SDI-ACC-005', 'Foco identificable', 2, 'Siempre se ve dónde está el foco',
        'El foco es <strong>la ubicación de quien usa el teclado</strong>.', [
        req(N('El foco debe ser perceptible y no quedar completamente oculto por otros elementos de la interfaz.', 'debe')),
        stack([('Indicador', [f'Anillo de 2 px en Azul Noche, separado del borde, visible con el teclado (:focus-visible). La decisión sobre {c("--color-focus")} está pendiente en FUI-007.']),
               ('Sin ocultarse', ['Cabeceras fijas, avisos y paneles no tapan el elemento con foco (2.4.11).']),
               ('Orden', ['El foco sigue el orden visual y lógico de la página (2.4.3).'])]),
        detalle([
            ('Verificación', [
                ('Recorrido', 'Se recorre la página con Tab con la cabecera fija visible. Resultado esperado: el foco se ve completo en cada paso.'),
                ('Contraste del indicador', 'El anillo alcanza 3:1 contra el fondo (1.4.11).')])]),
    ], origen=['Foco identificable (base)'], responsabilidad='El foco es perceptible, sigue el orden lógico y no queda oculto.', corto='Foco'),

    n21('KYN-SDI-ACC-006', 'Tiempo y movimiento', 3, 'La persona controla el tiempo y el movimiento',
        'Nada se apura <strong>ni se mueve sin permiso</strong>.', [
        req(N('Las interacciones deben respetar los criterios de accesibilidad relacionados con límites de tiempo, movimiento y control de contenido.', 'debe')),
        matriz('Tiempo y movimiento', [('Decisión', ''), ('Criterio', 'WCAG')], [
            ('Límites de tiempo', ['Se avisa antes y se puede extender; la sesión conserva los datos (PAT-002).', '2.2.1']),
            ('Contenido que se mueve o se actualiza solo', ['Se puede pausar, detener u ocultar.', '2.2.2']),
            ('Destellos', ['Nada destella más de tres veces por segundo.', '2.3.1']),
            ('Animaciones', [f'Respetan la preferencia de movimiento reducido ({L("39")}).', '2.3.3, recomendado'])]),
        detalle([
            ('Verificación', [
                ('Preferencias', 'Con movimiento reducido activado, las animaciones no esenciales se detienen. Con una sesión por vencer, aparece el aviso con la opción de extender.')])]),
    ], origen=['Tiempo y movimiento (base)'], responsabilidad='Se respetan los límites de tiempo, el control del movimiento y los destellos.', corto='Tiempo y movimiento'),

    seccion('ejemplo', '21', 'Ejemplo de aplicación', 'Una tarea sin ratón',
            'Una persona aprueba una solicitud <strong>solo con el teclado</strong>, desde el menú hasta la confirmación.', [
        stack([('Verificación del capítulo', ['Completar recorridos sin ratón y comprobar orden de foco, controles y recuperación.'])]),
    ]),
]

# ═════════════ 22 · Adaptación ═════════════
CAP22 = [
    n22('KYN-SDI-ACC-007', 'Diseño adaptable', 1, 'Cada pantalla funciona en cualquier tamaño',
        'Cambia la disposición; <strong>no se pierden funciones</strong>.', [
        req(N('Las pantallas deben reorganizarse según el espacio disponible sin eliminar funcionalidades esenciales.', 'debe')),
        stack([('Cómo se reorganiza', [f'Según la retícula de {L("10")} y la navegación de {L("05")}.']),
               ('Orientación', ['La pantalla funciona en vertical y en horizontal, salvo que una orientación sea esencial (1.3.4).'])]),
        detalle([
            ('Verificación', [
                ('Anchos', 'Se recorre cada tarea a 320, 768, 1024 y 1440 px. Resultado esperado: las funciones esenciales están en todos.')])]),
    ], origen=['Diseño adaptable (base)'], responsabilidad='Las pantallas se reorganizan sin eliminar funciones esenciales.', corto='Diseño adaptable'),

    n22('KYN-SDI-ACC-008', 'Interacciones accesibles', 2, 'Cada objetivo se toca sin errores',
        'El tamaño y la separación <strong>evitan los toques equivocados</strong>.', [
        req(N('Los objetivos interactivos deben cumplir los criterios aplicables de tamaño y separación de WCAG 2.2 AA.', 'debe')),
        matriz('Tamaño de los objetivos', [('Tamaño', ''), ('Estado', '')], [
            ('WCAG 2.2 AA · 2.5.8', ['24 × 24 px CSS como mínimo, o espacio suficiente alrededor.', 'Obligatorio.']),
            ('WCAG AAA · 2.5.5', ['44 × 44 px CSS.', 'Recomendación del estándar.']),
            ('Preferencia Keyons', ['44 × 44 px en los controles táctiles principales, cuando el espacio lo permite.', 'Propuesta; requiere aprobación.'])]),
        detalle([
            ('Excepciones de 2.5.8', [
                ('Cuáles', 'Enlaces dentro de un texto, controles del navegador, objetivos con un equivalente que cumple y presentaciones esenciales.')]),
            ('Verificación', [
                ('Medición', 'Se mide el menor objetivo de cada pantalla. Resultado esperado: 24 × 24 px como mínimo o una excepción documentada.')])]),
    ], origen=['Interacciones accesibles (base)', 'UIX-038', 'UIX-039 (44 px, revisado)'],
       responsabilidad='Los objetivos cumplen el tamaño y la separación de WCAG 2.2 AA; 44 px es una preferencia por aprobar.', corto='Objetivos'),

    n22('KYN-SDI-ACC-009', 'Variaciones de uso', 3, 'El producto considera cómo y dónde se usa',
        'Distintas manos, distintas pantallas, <strong>la misma tarea</strong>.', [
        req(N('Las experiencias deberían considerar dispositivos, métodos de entrada y condiciones operativas diferentes.', 'deberia')),
        matriz('Variaciones a considerar', [('Qué se decide', ''), ('Ejemplo', '')], [
            ('Métodos de entrada', ['Puntero, toque, teclado y voz.', 'Ninguna función exige un gesto complejo sin alternativa (2.5.1).']),
            ('Preferencias del sistema', ['Movimiento reducido, tamaño de texto y modo de alto contraste.', 'La interfaz respeta las preferencias del dispositivo.']),
            ('Condiciones', ['Una sola mano, luz exterior, conexión lenta.', 'Acciones principales al alcance del pulgar en móvil (desde UIX-039).']),
            ('Capacidades', ['Visión, audición, motricidad y atención.', 'Perfiles con atención variable (PEX-007).'])]),
        detalle([
            ('Verificación', [
                ('Matriz de uso', 'Cada tarea principal se prueba con al menos dos métodos de entrada y con las preferencias del sistema activadas.')])]),
    ], origen=['Variaciones de uso (base)', 'Preferencias del sistema y distintas capacidades (descripción del capítulo)', 'UIX-039'],
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
