"""Módulo 02 · Arquitectura (ARQ): 04 Información, 05 Navegación y 06 Búsqueda.
Requisitos: textos de Keylin (base, ampliación, «Estados de navegación» y «Acceso directo», 2026-11-17).
Decisiones, comportamientos, excepciones y verificaciones: propuesta de Claude en borrador.
"""
from .base import N, req, stack, matriz, pasos, contraste, detalle, prosa, sub, c, L, norma, seccion

MOD = 'arquitectura-navegacion'

# ═════════════ 05 · Navegación ═════════════
# Reglas generales para navegación lateral, superior, pestañas, rutas jerárquicas y navegación móvil.
# El capítulo no impone un patrón: el predeterminado de los productos SaaS lo define 37 Product Default.
C5 = 'estructura-de-navegacion'


def n5(nid, nombre, k, *a, **kw):
    return norma(nid, nombre, '02.02', MOD, C5, k, *a, **kw)


CAP05 = [
    n5('KYN-SDI-ARQ-005', 'Ubicación actual', 1, 'La persona sabe dónde está y cómo seguir',
       'Quien reconoce dónde está decide el siguiente paso <strong>sin recordar el camino</strong>.', [
        req(N('La navegación debe permitir reconocer en qué sección se encuentra la persona y cómo acceder a las demás áreas autorizadas.', 'debe'),
            N('La sección activa debe distinguirse visualmente y mantener una relación comprensible con sus secciones superiores cuando existan.', 'debe')),
        stack([('Sección activa', [f'Se marca con una señal de forma, como una barra, un fondo o un subrayado, y otra de color o de peso. Su apariencia la definen {L("08")} y {L("14")}.']),
               ('Grupo superior', ['El grupo de la página queda abierto o señalado. Desde el tercer nivel, una ruta jerárquica muestra el camino.']),
               ('Al navegar', ['El indicador, el título y la ruta cambian juntos. El foco se gestiona según el tipo de cambio.'])]),
        detalle([
            ('Según el tipo de navegación', [
                ('Lateral o superior', 'El destino de la página abierta lleva el indicador. En la lateral, su grupo queda abierto; en la superior, señalado en la barra.'),
                ('Pestañas', f'Las que llevan a otra página son enlaces y la activa lleva {c('aria-current="page"')}. Las que cambian un panel en la misma página siguen el patrón de pestañas de ARQ-008.'),
                ('Ruta jerárquica', f'Un {c("<nav>")} con nombre accesible («Ruta») y una lista ordenada, del nivel más general al actual. El último nivel nombra la página y lleva {c("aria-current")}.'),
                ('Móvil', 'El título de la pantalla nombra la sección y la ruta se abrevia al nivel superior inmediato. Al abrir el menú, el destino activo se ve marcado.')]),
            ('Foco según el tipo de cambio', [
                ('Página nueva completa', 'El foco queda donde lo deja el navegador, al inicio del documento. El enlace «Ir al contenido» es lo primero que alcanza el teclado; el foco no se lleva a él automáticamente.'),
                ('Vista nueva sin recargar', 'El foco pasa al título principal de la vista. Si la tarea necesita que el foco se quede donde estaba, una región en vivo anuncia el cambio.'),
                ('Filtro, orden o pestaña de panel', 'El foco queda en el control que se usó. Si el resultado cambia fuera de la vista, se anuncia.'),
                ('Panel o diálogo', 'El foco entra al abrir y vuelve al control que lo abrió al cerrar, según ARQ-009.')]),
            ('Excepciones', [
                ('Cuáles', 'Los flujos de un paso, los diálogos y el inicio de sesión prescinden de la navegación general.'),
                ('Qué conservan', 'Su título visible y una salida.')]),
            ('Verificación', [
                ('Con personas', 'Desde una pantalla de segundo o tercer nivel, abierta con un enlace directo, la persona nombra la sección y el grupo y llega a otra sección principal sin ayuda. Se registra el tiempo; cinco segundos es la hipótesis inicial de prueba, no un requisito.'),
                ('Escala de grises', 'Con la pantalla en escala de grises, la sección activa sigue distinguiéndose.'),
                ('Lector de pantalla', 'Con NVDA o VoiceOver, al recorrer la navegación, el enlace activo se anuncia como «página actual».'),
                ('Cambio de destino', 'En cada tipo de cambio, el indicador, el título, la ruta y el foco se comportan como indica «Foco según el tipo de cambio».')])]),
    ], origen=['Ubicación actual (base)', 'Ubicación actual (ampliación)', 'Verificación base del capítulo 05'],
       responsabilidad='La persona reconoce la sección activa, su grupo superior y cómo llegar a las demás áreas.'),

    n5('KYN-SDI-ARQ-006', 'Acciones previsibles', 2, 'Cada destino conserva su sentido y su lugar',
       'Una navegación estable <strong>se aprende una vez</strong>.', [
        req(N('Los elementos navegables deben mantener nombres, destinos y comportamientos consistentes en todo el producto.', 'debe'),
            N('Las funciones principales deberían conservar una ubicación y denominación consistentes entre las pantallas equivalentes.', 'deberia')),
        stack([('Nombre', [f'Un destino se nombra de forma coherente en el menú, la ruta y el título. Puede abreviarse o precisarse sin cambiar de significado; su redacción sigue Nombres comprensibles, en {L("04")}.']),
               ('Enlace o botón', ['Un enlace lleva a otro lugar; un botón ejecuta una acción. Cada control conserva su tipo en todas las pantallas.']),
               ('Ubicación', ['Las funciones principales ocupan la misma posición en pantallas equivalentes, por ejemplo, en todos los listados de un módulo.'])]),
        sub('Ejemplos'),
        contraste([('Menú «Solicitudes» y título «Gestión de trámites»', 'Menú «Solicitudes» y título «Solicitudes pendientes»: el título precisa sin cambiar el sentido.'),
                   ('«Exportar» descarga en un listado y abre un diálogo en otro', '«Exportar» abre el mismo diálogo en todos los listados.'),
                   ('Un texto subrayado que guarda cambios', 'Guardar es un botón; el texto subrayado lleva a otro lugar.')]),
        detalle([
            ('Otra pestaña o salida del producto', [
                ('Comportamiento', 'Los enlaces abren en la misma pestaña.'),
                ('Excepción', 'El enlace que abre otra pestaña o sale del producto lo anuncia con el ícono «abrir externo» y un texto accesible.')]),
            ('Verificación', [
                ('Inventario', 'Se listan los destinos con su nombre en el menú, la ruta y el título. Resultado esperado: cada variante conserva el significado del destino.'),
                ('Recorrido', 'Se completa la misma tarea desde dos áreas autorizadas. Resultado esperado: el mismo destino, con el mismo comportamiento.')])]),
    ], origen=['Acciones previsibles (base)', 'Acceso consistente (ampliación)'],
       responsabilidad='Cada destino conserva un nombre coherente, su lugar y su comportamiento en todo el producto.',
       cita='Aplica PEX-005 a la navegación; los nombres siguen ARQ-002'),

    n5('KYN-SDI-ARQ-007', 'Navegación visible', 3, 'Toda función necesaria tiene una señal a la vista',
       'Lo que se ve <strong>se puede usar</strong> con puntero, teclado y tacto.', [
        req(N('Las funciones necesarias no deben depender exclusivamente de interacciones ocultas o de pasar el cursor sobre una zona sin señal.', 'no-debe')),
        matriz('Interacciones ocultas y su alternativa visible', [('Como única vía', 'Lo que se evita'), ('Alternativa visible', 'Lo que se diseña')], [
            ('Pasar el cursor', ['Un menú o una acción que solo aparece al pasar el cursor.', 'Aparece también con el foco del teclado y con un toque.']),
            ('Gestos', ['Deslizar o mantener presionado para editar o eliminar.', 'Un botón o un menú de opciones visible en el elemento.']),
            ('Atajos de teclado', ['Una función que solo tiene atajo.', 'Un control visible; el atajo se muestra como ayuda.']),
            ('Destinos que no caben', ['Destinos fuera de la pantalla, sin aviso.', 'Un control «Más» que indica que hay más destinos.']),
            ('Íconos solos', ['Un ícono suelto como única señal de un destino principal.', 'Nombre visible en los destinos principales; en los demás, nombre accesible y etiqueta con el foco y el cursor.'])]),
        detalle([
            ('Contenido que aparece con el cursor o el foco', [
                ('Cierre', 'Escape lo cierra sin mover el puntero ni el foco.'),
                ('Permanencia', 'Sigue visible mientras el puntero está encima y hasta que la persona lo cierra o mueve el foco (WCAG 1.4.13).')]),
            ('Verificación', [
                ('Tres recorridos', 'Se completan las tareas principales solo con teclado, solo con toques y solo con puntero. Resultado esperado: todas se completan.'),
                ('Contenido emergente', 'Cada contenido que aparece con el cursor se abre también con el foco y se cierra con Escape.')])]),
    ], origen=['Navegación visible (base)'], responsabilidad='Toda función necesaria tiene una señal visible para puntero, teclado y tacto.'),

    n5('KYN-SDI-ARQ-008', 'Identificación de controles', 4, 'Cada control dice qué hace y en qué estado está',
       'La misma información <strong>para quien mira y para quien escucha</strong>.', [
        req(N('Los controles de navegación deben comunicar su función y estado mediante señales comprensibles y accesibles.', 'debe'),
            N('Los elementos de navegación deben distinguir su estado actual, disponibilidad y comportamiento interactivo sin depender exclusivamente del color.', 'debe'),
            N('Los estados de foco y selección no deben confundirse: el foco identifica dónde está interactuando la persona; la selección identifica la ubicación o contenido actual.', 'no-debe')),
        stack([('Estados visuales', ['Reposo, cursor encima, foco, actual, deshabilitado y no disponible se distinguen entre sí. Foco y actual pueden coincidir y se ven a la vez.']),
               ('Sección activa', ['La sección activa mantiene una señal reconocible incluso cuando el cursor se encuentra sobre otro elemento.']),
               ('Semántica primero', [f'Se usan los elementos que ya resuelven la función: {c("<nav>")}, {c("<a href>")}, {c("<button>")} y listas. ARIA completa lo que el HTML no expresa.'])]),
        matriz('Cuatro patrones y su estado', [('Elemento', 'Cómo se construye'), ('Estado', 'Qué se anuncia')], [
            ('Página actual', [f'Enlace {c("<a href>")} dentro de un {c("<nav>")}.', f'{c("aria-current")} con valor «page»: «página actual».']),
            ('Pestaña seleccionada', ['Patrón de pestañas: cada pestaña dentro de una lista de pestañas, asociada a su panel.', f'{c("aria-selected")}: «seleccionada».']),
            ('Grupo expandible', [f'{c("<button>")} que abre o cierra su grupo.', f'{c("aria-expanded")} y {c("aria-controls")}: «expandido» o «contraído».']),
            ('Panel modal', [f'{c("<dialog>")} abierto como modal, o un panel con {c("aria-modal")} y el fondo inerte.', 'Su nombre al abrir; el foco queda dentro hasta cerrarlo.'])]),
        detalle([
            ('Teclado según el tipo de menú', [
                ('Grupo desplegable', 'Enter o Espacio lo abren y lo cierran. El foco queda en el botón y el siguiente Tab entra en sus destinos.'),
                ('Menú sobre el contenido', 'Enter o Espacio lo abren y el foco pasa al primer destino. Escape lo cierra y el foco vuelve al botón; también se cierra al salir el foco o al tocar fuera.'),
                ('Pestañas', 'Tab entra a la pestaña seleccionada; las flechas recorren las demás. El panel cambia al activarlas o al moverse, según la tarea.'),
                ('Panel móvil', 'Se describe en ARQ-009.'),
                ('Navegación larga', 'El enlace «Ir al contenido» es lo primero que alcanza el teclado; al activarlo, el foco pasa al inicio del contenido principal.')]),
            ('Nombres accesibles', [
                ('Varias navegaciones', f'Cuando una página tiene más de un {c("<nav>")}, cada uno lleva su nombre: «Principal», «Ruta», «Secciones».'),
                ('Botón con solo ícono', f'Lleva su nombre en {c("aria-label")} y una etiqueta visible con el foco y el cursor.'),
                ('Foco', f'Se ve completo en cada control, sin quedar debajo de una cabecera fija. Su apariencia la define {L("21")}.')]),
            ('Verificación', [
                ('Revisión automática', 'Una herramienta como axe o Lighthouse no reporta errores de nombre, rol ni estado. Es necesaria, pero no alcanza.'),
                ('Teclado', 'Se recorre la navegación con Tab, se abre con Enter o Espacio y se cierra con Escape. Resultado esperado: el foco siempre visible y en el lugar descrito.'),
                ('Lector de pantalla', 'Con NVDA y Firefox o Chrome, y con VoiceOver y Safari: cada navegación se anuncia con su nombre; cada grupo, «expandido» o «contraído»; la página activa, «página actual»; la pestaña, «seleccionada».'),
                ('Foco y selección', 'Al mover el foco o el puntero por otros destinos, la sección activa sigue marcada y distinta del foco.')])]),
    ], origen=['Identificación de controles (ampliación)', 'Estados de navegación (texto de Keylin, 2026-11-17)', 'UIX-038'],
       responsabilidad='Los controles de navegación comunican función, estado y disponibilidad con semántica y señales accesibles, y distinguen foco de selección.',
       cita=f'21 Operación (Teclado, Foco identificable) define el foco del producto'),

    n5('KYN-SDI-ARQ-009', 'Adaptación por dispositivo', 5, 'La presentación cambia; los destinos se reconocen',
       'Cambia la forma; <strong>los destinos se reconocen</strong> en cualquier pantalla.', [
        req(N('La navegación puede modificar su presentación según el espacio disponible, conservando acceso a las funciones esenciales.', 'puede'),
            N('La navegación debe conservar acceso a sus destinos esenciales cuando cambia de escritorio a móvil.', 'debe')),
        matriz('Qué se mantiene y qué cambia entre tamaños de pantalla', [('Se mantiene', 'En todos los tamaños'), ('Cambia', 'Según el espacio')], [
            ('Destinos', ['Los destinos esenciales, con nombres reconocibles.', 'Cuántos se ven a la vez y su orden, si mejora el uso; los secundarios pasan a «Más».']),
            ('Formato', ['Un control visible para cada destino.', 'Navegación lateral, superior, barra inferior, pestañas o panel.']),
            ('Ubicación', ['La sección activa y el título de la página.', 'La ruta jerárquica se abrevia al nivel superior inmediato.']),
            ('Controles', ['Nombre accesible, estado y un orden de foco que sigue al orden visual.', 'El tamaño de los objetivos, según el contexto.'])]),
        prosa(f'El formato predeterminado de los productos SaaS lo define {L("37")}.'),
        detalle([
            ('Panel de navegación móvil', [
                ('Estados', f'Cerrado, abierto y en transición. El botón que lo abre refleja el estado con {c("aria-expanded")}.'),
                ('Al abrir', f'El foco entra al panel. El fondo queda inerte ({c("inert")}) y sin desplazamiento.'),
                ('Al cerrar', 'Escape, el botón Cerrar o un toque fuera lo cierran. El foco vuelve al botón que lo abrió.'),
                ('Al cambiar de tamaño', 'Si al girar la pantalla o ampliar la ventana el panel deja de hacer falta, se cierra y el foco queda en un elemento visible.'),
                ('Movimiento', 'La transición respeta la preferencia de movimiento reducido.')]),
            ('Tamaño de los objetivos', [
                ('WCAG 2.2 AA · 2.5.8', 'Mínimo de 24 × 24 px CSS, o espacio suficiente alrededor. Excepciones: enlaces dentro de un texto, controles del navegador, un control equivalente que cumple y presentaciones esenciales.'),
                ('WCAG AAA · 2.5.5', '44 × 44 px CSS, con excepciones equivalentes.'),
                ('Preferencia Keyons', f'Propuesta: 44 × 44 px en los controles táctiles principales cuando el espacio lo permite. Requiere aprobación; se decide en {L("22")}.')]),
            ('Verificación', [
                ('Ancho y ampliación', 'A 320 px de ancho y con ampliación del 400 %, se buscan los destinos esenciales de escritorio. Resultado esperado: están todos, sin desplazamiento horizontal (WCAG 1.4.10).'),
                ('Orden', 'Si el orden cambia entre dispositivos, cada destino se encuentra por su nombre.'),
                ('Panel', 'Se abre y se cierra con teclado y con toque. Resultado esperado: el foco entra, el fondo no responde y el foco vuelve al botón.'),
                ('Objetivos', 'Se mide el menor objetivo interactivo. Resultado esperado: 24 × 24 px CSS como mínimo, o una excepción documentada.')])]),
    ], origen=['Adaptación por dispositivo (base)', 'Menús adaptables (ampliación)', 'UIX-039'],
       responsabilidad='La presentación cambia con el espacio; los destinos esenciales se mantienen accesibles y reconocibles.',
       cita='22 Adaptación define el tamaño de los objetivos; 37 Product Default, el patrón SaaS'),

    n5('KYN-SDI-ARQ-010', 'Regreso sin pérdida', 6, 'Volver a una lista devuelve el trabajo donde quedó',
       'Retomar una lista es <strong>continuar la misma tarea</strong>.', [
        req(N('Cuando se vuelve desde un detalle a un listado, el sistema debería conservar filtros, búsqueda y posición cuando sean relevantes para continuar la tarea.', 'deberia')),
        pasos([('Abrir', 'La persona abre un registro desde un listado filtrado, ordenado o con una búsqueda.', 'Decisión', 'El sistema conserva la consulta, los filtros, el orden y la posición.'),
               ('Volver', 'Regresa con el control Volver de la interfaz o con el del navegador.', 'Decisión', 'Los dos llevan al mismo listado, en el mismo estado.'),
               ('Retomar', 'El listado muestra la misma búsqueda, los mismos filtros y el mismo orden.', 'Decisión', 'La posición se restaura y el foco vuelve al registro abierto.')]),
        stack([('Dónde se conserva', ['Depende de la tarea, la privacidad y la seguridad. La dirección (URL) sirve cuando la vista se comparte o se recarga y no expone datos sensibles; el estado de la sesión, cuando no. El capítulo no impone una técnica.']),
               ('Cambios pendientes', [f'Si la persona sale con cambios sin guardar, el producto los protege según {L("16")} y {L("17")}.'])]),
        detalle([
            ('Excepciones', [
                ('Registro eliminado o fuera del filtro', 'El listado se recupera igual y avisa del cambio.'),
                ('Sesión nueva', 'El listado empieza en su estado inicial, salvo las preferencias que la persona guardó.')]),
            ('Verificación', [
                ('Volver', 'Se abre el registro número 15 de un listado filtrado y ordenado, y se vuelve con los dos controles. Resultado esperado: mismos filtros, orden, página y posición, con el foco en ese registro.'),
                ('Recargar', 'Si la vista se puede recargar, los filtros siguen aplicados después de hacerlo.'),
                ('Privacidad', 'Ningún dato sensible queda en la dirección ni en el historial del navegador.')])]),
    ], origen=['Regreso sin pérdida (ampliación)', 'Recuperación (base, capítulo 06)', 'Recuperación del contexto (ampliación, capítulo 06)', 'UIX-025'],
       responsabilidad='Al volver de un detalle, la lista conserva búsqueda, filtros, orden y posición cuando sirven para continuar.',
       cita='06 Búsqueda cita esta norma para la consulta conservada; 16 y 17 regulan los cambios pendientes'),

    n5('KYN-SDI-ARQ-017', 'Acceso directo y rutas no disponibles', 7, 'Cada dirección lleva a un destino o a una salida',
       'Un enlace guardado o compartido <strong>funciona como cualquier otra entrada</strong>.', [
        req(N('Las rutas internas deben permitir abrir directamente una página autorizada cuando el producto admita navegación mediante enlaces.', 'debe'),
            N('Cuando una ruta no exista, no esté disponible o carezca de autorización, el sistema debe comunicar la situación y ofrecer una salida apropiada, sin revelar información restringida.', 'debe')),
        matriz('Qué ve la persona según la ruta que abre', [('Qué ve', 'Al abrir la dirección'), ('Cómo sigue', 'La salida')], [
            ('Ruta autorizada', ['La página completa, con la sección activa marcada (ARQ-005).', 'Navega como desde el menú.']),
            ('Ruta inexistente', ['Un mensaje de página no encontrada, dentro del producto y con su navegación.', 'Un enlace al inicio o a la sección más cercana, y la búsqueda si existe.']),
            ('Sin autorización', ['Un mensaje de acceso no disponible, sin datos de la página pedida.', 'Volver o solicitar acceso, según el producto.']),
            ('Sesión vencida', ['El inicio de sesión, que conserva la dirección pedida.', 'Al entrar, la persona llega a la página que buscaba.'])]),
        detalle([
            ('Detalle', [
                ('Información restringida', 'Cuando confirmar que un recurso existe ya revela información, la respuesta es la misma que para una ruta inexistente.'),
                ('Texto del mensaje', f'Sigue {L("24")}: qué pasó y cómo continuar.'),
                ('Ubicación', 'La página de error conserva la navegación general y solo marca una sección si corresponde.')]),
            ('Verificación', [
                ('Cuatro rutas', 'Se abren directamente una ruta válida, una inexistente, una no autorizada y una con la sesión vencida.'),
                ('Resultado esperado', 'La página correcta; un mensaje con salida; ningún dato restringido en el título, el mensaje ni el código de la página; y, tras iniciar sesión, la página pedida.')])]),
    ], origen=['Acceso directo y rutas no disponibles (texto de Keylin, 2026-11-17)'],
       responsabilidad='Las rutas internas se abren directamente y las no disponibles comunican la situación con una salida, sin revelar información.',
       cita='24 Mensajes define el texto; 18 Recuperación, las rutas alternativas'),

    seccion('ejemplo', '05', 'Ejemplo de aplicación', 'Una solicitud dentro de Administración',
            'Si una pantalla pertenece a Administración › Solicitudes, <strong>el menú señala la sección activa</strong> y la persona puede regresar al listado sin perder innecesariamente su contexto.', [
        stack([('Ubicación', ['El menú marca Administración y, dentro, Solicitudes. La ruta muestra Administración › Solicitudes › Solicitud 2026-118.']),
               ('Nombres', ['El menú dice «Solicitudes» y el título del listado, «Solicitudes pendientes».']),
               ('En móvil', ['El panel de navegación conserva los mismos destinos, y la ruta se abrevia a «Solicitudes».']),
               ('Regreso', ['Al volver de la solicitud, el listado conserva el filtro «Pendientes», el orden y la posición.'])]),
    ]),
]

CAPITULOS = [
    # (número de módulo, clave del capítulo, slug, secciones, descripción corta propuesta)
    ('02', '02.02', C5, CAP05, 'Cómo se reconoce la ubicación, se recorren los destinos y se retoma el trabajo, en cualquier forma de navegación.'),
]
