"""Módulo 01 · Experiencia (PEX): 01 Principios comunes, 02 Personas y contextos y 03 Elecciones verificadas.
Requisitos: textos de Keylin (base y ampliación, 2026-11-17). Los de PEX-016 a PEX-018 los redactó Claude a partir de las
«Ampliaciones necesarias» de su matriz y requieren aprobación. UIX-002, 003, 005, 007 y 048 se usan como referencia evaluada.
Titulares, entradas, decisiones, ejemplos y verificaciones: propuesta de Claude en borrador.
Composición: Guía 05 «Composición normativa según el contenido».
"""
from .base import N, req, stack, dims, matriz, pasos, detalle, numeradas, L, R, norma, seccion, validacion

MOD = 'principios-experiencia'
C1, C2, C3 = 'principios-compartidos', 'personas-y-contextos-de-uso', 'decisiones-verificables-de-experiencia'


def n1(nid, nombre, k, *a, **kw): return norma(nid, nombre, '01.01', MOD, C1, k, *a, **kw)
def n2(nid, nombre, k, *a, **kw): return norma(nid, nombre, '01.02', MOD, C2, k, *a, **kw)
def n3(nid, nombre, k, *a, **kw): return norma(nid, nombre, '01.03', MOD, C3, k, *a, **kw)


# ═════════════ 01 · Principios comunes ═════════════
CAP01 = [
    n1('KYN-SDI-PEX-001', 'La tarea primero', 1, 'Propósito y prioridad de la pantalla',
       'Define qué reconoce la persona al abrir cualquier pantalla: <strong>su propósito, su acción principal y lo que queda subordinado</strong>.', [
        dims([('Propósito', [N('Cada pantalla debe identificar su propósito y permitir reconocer la acción o información principal sin depender de elementos decorativos.', 'debe'),
                             'El título nombra la tarea o el objeto de la pantalla, no el nombre técnico del módulo: «Solicitudes pendientes», en lugar de «Gestión de trámites».']),
              ('Acción principal', [N('Cuando una pantalla permite realizar una tarea principal, esa acción debe distinguirse de las secundarias mediante una jerarquía visual y funcional consistente.', 'debe'),
                                    f'Cada grupo de decisión tiene una sola {R("KYN-SDI-CPE-001", "acción principal")}; las demás son secundarias.']),
              ('Recursos gráficos', [N('Los recursos gráficos no deben competir por la atención con información esencial o acciones necesarias para completar una tarea.', 'no-debe'),
                                     f'Ilustraciones, fotografías y color expresivo acompañan a la tarea sin ocupar el lugar de un dato o de una acción.'])]),
        detalle([('Aplicación según el contexto', [
            ('Pantallas de consulta', 'Sin una acción principal, la información principal ocupa su lugar en la jerarquía.'),
            ('Varias tareas en una pantalla', 'Se separan en grupos rotulados, cada uno con su acción principal.'),
            ('Paneles de inicio', 'Se ordenan por prioridad operativa: primero lo que exige una decisión del día.')])]),
    ], origen=['La tarea primero (base)', 'Una acción reconocible (ampliación)', 'Sin competencia visual innecesaria (ampliación)', 'UIX-001', 'UIX-028'],
       responsabilidad='Cada pantalla deja reconocer su propósito y su acción principal sin que los recursos gráficos compitan.',
       cita='11 Recursos visuales (Expresión proporcionada) cita esta norma',
       rel=['KYN-SDI-CPE-001', 'KYN-SDI-FUI-017', 'KYN-SDI-DAV-004'], verif=[('Primera mirada', 'Una persona que no conoce la pantalla la ve sin instrucciones. Cinco segundos es la hipótesis inicial de prueba, no un requisito.',
               'señala el propósito y la acción principal sin ayuda.'),
              ('Sin decoración', 'Se quitan de la pantalla los recursos decorativos.', 'la persona completa la tarea en el mismo tiempo y sin preguntas nuevas.')]),

    n1('KYN-SDI-PEX-002', 'Claridad antes que novedad', 2, 'Patrones de interacción conocidos',
       'Se aplica al diseñar un control o un recorrido: <strong>la convención conocida es el punto de partida</strong> y un patrón propio se justifica.', [
        req(N('La interfaz no debe ocultar funciones necesarias ni sustituir patrones comprensibles únicamente para conseguir una apariencia original.', 'no-debe')),
        stack([('Controles conocidos', ['Enlaces, casillas, menús y pestañas siguen las convenciones de la web y del sistema operativo. Un enlace subrayado lleva a otro lugar y una casilla marca una opción.']),
               ('Patrón propio', [f'Responde a un problema que el convencional no resuelve y se evalúa antes de extenderse.'])]),
        detalle([('Prioridad entre criterios (propuesta, desde UIX-005)', [
            ('Transparencia antes que fluidez', 'Cada paso importante se muestra, aunque el recorrido sea más largo.'),
            ('Control antes que automatización', f'La persona puede intervenir, revertir y decidir.'),
            ('Comprensión antes que velocidad', 'Un recorrido claro antes que uno rápido y confuso.'),
            ('Convención antes que novedad', 'Se innova donde aporta un valor comprobado.')])]),
    ], origen=['Claridad antes que novedad (base)', 'UIX-005'],
       responsabilidad='Las funciones y los patrones comprensibles se conservan por encima de la originalidad.',
       rel=['KYN-SDI-PEX-015', 'KYN-SDI-PEX-017'], verif=[('Comparación', 'Se prueba la misma tarea con el patrón propio y con el convencional.', 'el propio se conserva solo si iguala o mejora el resultado.')]),

    n1('KYN-SDI-PEX-003', 'Complejidad justificada', 3, 'Controles pertinentes a la tarea',
       'Decide cuántos controles, datos y pasos quedan a la vista: <strong>los que la tarea, el perfil y la frecuencia de uso necesitan</strong>.', [
        req(N('La cantidad de información y controles visibles debería corresponder a la tarea, al perfil de usuario y a la frecuencia de uso.', 'deberia')),
        stack([('Lo visible', [f'Lo que se usa en cada sesión queda a la vista; lo ocasional, a un paso.']),
               ('Pasos', ['Cada paso de una tarea pide una decisión o un dato nuevo. Los pasos que repiten información conocida se completan solos o se eliminan.']),
               ('Ejemplo', [f'En un listado de solicitudes, «Aprobar» y «Ver» están en cada fila; «Exportar» y «Archivar» van en el menú de acciones de la lista.'])]),
    ], origen=['Complejidad justificada (base)', 'Reducción de pasos innecesarios (ampliación de la matriz)', 'UIX-001'],
       responsabilidad='La cantidad de información, controles y pasos corresponde a la tarea, al perfil y a la frecuencia.',
       cita='04 Información progresiva (ARQ-004) desarrolla el detalle bajo demanda',
       rel=['KYN-SDI-ARQ-004', 'KYN-SDI-PEX-009', 'KYN-SDI-CPE-004'], verif=[('Controles', 'Se listan los controles visibles de la pantalla con su frecuencia de uso.', 'los de uso ocasional están en un segundo nivel.'),
              ('Pasos', 'Se cuentan los pasos de las tres tareas más frecuentes.', 'cada paso tiene una razón registrada.')]),

    n1('KYN-SDI-PEX-004', 'Estado comprensible', 4, 'Comunicar el estado de cada acción',
       'Se aplica a toda acción que la persona inicia: <strong>el sistema responde con su estado</strong> hasta que la acción termina o necesita algo.', [
        req(N('Después de una acción, el sistema debe comunicar si está procesando, si terminó o si requiere intervención.', 'debe')),
        matriz('Qué comunica el sistema después de una acción', [('Qué comunica', 'A la persona'), ('Cómo', 'En la interfaz')], [
            ('Procesando', ['Que la acción se recibió y sigue en curso.', f'Indicador en el control o en la zona afectada; texto descriptivo si la espera es larga.']),
            ('Terminó', ['El resultado real: qué cambió y dónde.', f'Confirmación específica.']),
            ('Requiere intervención', ['Qué falta y cómo continuar.', f'Mensaje junto al elemento afectado, con una acción.']),
            ('Falló', ['Qué pasó y cómo seguir.', f'Mensaje con una salida.'])]),
    ], origen=['Estado comprensible (base)', 'UIX-012', 'UIX-013'],
       responsabilidad='Después de una acción, el sistema comunica si procesa, terminó, necesita intervención o falló.',
       cita='15 Retroalimentación (Resultado visible) desarrolla los componentes',
       rel=['KYN-SDI-CNT-005', 'KYN-SDI-CPE-012', 'KYN-SDI-PAT-007', 'KYN-SDI-PAT-010'], verif=[('Tres situaciones', 'Cada acción principal se ejecuta con éxito, con una espera larga y con un fallo.', 'en los tres casos, la persona describe el estado sin preguntar.')], ver='grupo'),

    n1('KYN-SDI-PEX-005', 'Comportamiento previsible', 5, 'Comportamientos consistentes entre pantallas',
       'Una misma función se usa igual en todo el producto: <strong>lo aprendido en una pantalla sirve en las demás</strong>.', [
        req(N('Los componentes que realizan una misma función deben mantener un comportamiento consistente entre pantallas. Las diferencias requieren una justificación funcional.', 'debe')),
        stack([('Entre pantallas', ['Guardar, cancelar, eliminar y deshacer dan el mismo resultado, con los mismos mensajes y las mismas teclas, en todo el producto.']),
               ('Entre productos', [f'Los componentes canónicos se comportan igual en todos los productos Keyons.']),
               ('Navegación', ['Un destino se nombra igual en el menú, la ruta y el título, y conserva su lugar entre pantallas.'])]),
    ], origen=['Comportamiento previsible (ampliación)', 'Consistencia entre pantallas (ampliación de la matriz)', 'UIX-013'],
       responsabilidad='Una misma función se comporta igual en todas las pantallas y productos.',
       cita='05 Acciones previsibles (ARQ-006) aplica el principio a la navegación',
       rel=['KYN-SDI-ARQ-006', 'KYN-SDI-SPR-005', 'KYN-SDI-PEX-010'], verif=[('Dos contextos', 'Se ejecuta la misma operación en dos pantallas.', 'mismo resultado, mismos mensajes y mismas teclas.'),
              ('Diferencias', f'Se revisa cada diferencia de comportamiento entre pantallas.', 'cada una tiene su justificación registrada.')]),

    n1('KYN-SDI-PEX-006', 'Contexto antes de actuar', 6, 'Consecuencias visibles antes de confirmar',
       'Se aplica a las acciones que cambian información o decisiones importantes: <strong>la persona ve qué va a cambiar antes de confirmar</strong>.', [
        req(N('Cuando una acción puede afectar información o decisiones importantes, la interfaz debe proporcionar el contexto necesario para comprender sus consecuencias.', 'debe')),
        stack([('Qué se muestra', ['Qué va a cambiar, cuántos elementos, si se puede deshacer y quién más se ve afectado.']),
               ('Proporción', [f'La protección crece con el impacto: deshacer para lo reversible y {R("KYN-SDI-CPE-003", "confirmación explícita")} para lo irreversible.']),
               ('Ejemplo', ['Antes de eliminar 12 facturas, el diálogo indica cuántas son, que la acción no se puede deshacer y que el cliente dejará de verlas.'])]),
    ], origen=['Contexto antes de actuar (ampliación)', 'UIX-006'],
       responsabilidad='Antes de una acción de consecuencias, la persona ve qué va a cambiar.',
       cita='19 Procesos críticos (Consecuencias claras) se integra en esta norma',
       verif=[('Antes de confirmar', 'Antes de cada acción de impacto, se pide a la persona que describa qué va a cambiar.', 'su descripción coincide con lo que ocurre después.')], ver='grupo'),

    n1('KYN-SDI-PEX-016', 'Prevención de errores', 7, 'Prevención de errores frecuentes',
       'Se aplica a los datos y las acciones donde las personas se equivocan con frecuencia: <strong>la interfaz evita el error antes de tener que corregirlo</strong>.', [
        req(N('La interfaz debería prevenir los errores frecuentes mediante opciones válidas, valores sugeridos y formatos comprensibles antes de que la persona los cometa.', 'deberia')),
        stack([('Opciones válidas', ['Solo se ofrecen las opciones posibles: fechas existentes, cantidades dentro del rango y estados permitidos.']),
               ('Formatos', [f'El formato esperado se ve antes de escribir, en la etiqueta o en la ayuda del campo.']),
               ('Acciones de riesgo', [f'Se separan de las frecuentes y llevan su protección.'])]),
    ], origen=['Prevención de errores (ampliación de la matriz; requisito redactado por Claude)'],
       responsabilidad='La interfaz previene los errores frecuentes antes de que ocurran.',
       cita='13 Entradas y 16 Formularios desarrollan la validación',
       rel=['KYN-SDI-CPE-005', 'KYN-SDI-PEX-006'], verif=[('Errores frecuentes', 'Se registran los errores más frecuentes de una prueba con personas.', 'cada uno tiene una medida preventiva o una razón documentada para no tenerla.')], ver='grupo'),

    n1('KYN-SDI-PEX-017', 'Control de la persona', 8, 'Cancelar, deshacer y decidir',
       'Se aplica a toda operación que la persona inicia y a lo que el sistema completa o sugiere: <strong>cada operación ofrece la salida que corresponde a su efecto</strong>, antes y después de confirmarla.', [
        req(N('La persona debe poder cancelar, deshacer o corregir las acciones reversibles y decidir sobre lo que el sistema propone.', 'debe')),
        matriz('Salida según la operación', [('Antes de confirmar', 'Mientras se decide'), ('Después de confirmar', 'Cuando ya ocurrió')], [
            ('Acción reversible', ['Cancelar cierra sin cambios.', 'Deshacer en el mismo lugar, mientras el cambio no afecte a otras personas o sistemas. Después, la corrección es una acción nueva que queda registrada.']),
            ('Acción irreversible', ['El botón nombra la consecuencia, como «Eliminar definitivamente», y la confirmación dice qué se pierde.', f'Sin deshacer; la {R("KYN-SDI-CPE-003", "confirmación")} se refuerza según el riesgo.']),
            ('Proceso largo', ['Cancelar antes de iniciar.', 'Cancelar o pausar cuando el sistema puede detenerlo sin dejar datos a medias. Al hacerlo, informa qué quedó hecho y qué no.']),
            ('Propuesta del sistema', ['Lo completado o sugerido queda editable y marcado como propuesta.', 'Se corrige como cualquier dato propio.'])]),
        stack([('Aprobación de la persona', ['Una propuesta necesita aprobación explícita cuando cambia datos de otras personas, envía algo fuera del producto o tiene efecto económico o legal.']),
               ('Si la operación falla', ['Lo que la persona escribió o eligió se conserva. El mensaje dice qué se guardó y ofrece reintentar.']),
               ('Según la operación', ['El mecanismo depende del efecto de cada operación. Un listado puede deshacer una eliminación y un pago, en cambio, pide confirmación previa.'])]),
    ], origen=['Control de la persona (ampliación de la matriz; requisito redactado por Claude)', 'UIX-005', 'UIX-025'],
       responsabilidad='La persona puede cancelar, deshacer y decidir sobre lo que el sistema propone.',
       rel=['KYN-SDI-PAT-008', 'KYN-SDI-IAE-003'],
       verif=[('Reversión', 'Se ejecuta cada acción reversible y se deshace.', 'el estado anterior vuelve completo.'),
              ('Propuestas', 'Se revisan los datos que completa el sistema antes de confirmar.', 'cada uno se puede cambiar antes de confirmarlo.'),
              ('Fallo', 'Se provoca un fallo al guardar un formulario completo.', 'los datos escritos siguen en el formulario y el mensaje ofrece reintentar.')], ver='grupo'),
    n1('KYN-SDI-PEX-018', 'Reconocer antes que recordar', 9, 'Opciones y datos previos a la vista',
       'Se aplica a las tareas de varios pasos o pantallas: <strong>lo que la persona necesita para seguir está a la vista</strong>.', [
        req(N('La interfaz debería mostrar las opciones, los datos previos y el contexto necesario, en lugar de exigir que la persona los recuerde entre pantallas.', 'deberia')),
        stack([('Opciones', ['Listas y sugerencias en lugar de códigos que hay que escribir de memoria.']),
               ('Datos previos', ['Lo que la persona eligió en un paso sigue a la vista en el siguiente.']),
               ('Recientes', ['Búsquedas y elementos recientes disponibles cuando la tarea se repite.'])]),
    ], origen=['Reconocimiento frente a memorización (ampliación de la matriz; requisito redactado por Claude)'],
       responsabilidad='La interfaz muestra opciones, datos previos y contexto en lugar de exigir memoria.',
       verif=[('Recorrido', 'Se recorre una tarea de varios pasos sin papel ni notas.', 'ningún paso pide un dato que la persona vio o eligió antes y que ya no está a la vista.')]),

    seccion('ejemplo', '01', 'Ejemplo de aplicación', 'Un tablero residencial',
            'En un tablero residencial, las tareas pendientes, los avisos y los accesos operativos tienen <strong>una jerarquía basada en su utilidad</strong>, no en el atractivo de sus colores.', [
        stack([('Prioridad', ['Arriba, las tareas pendientes del día con su acción principal: «Revisar».']),
               ('Estado', ['Al aprobar una solicitud, la fila cambia a «Aprobada» y aparece «Deshacer».']),
               ('Consecuencias', ['Antes de rechazar una solicitud, el diálogo indica a quién se le avisa.'])]),
    ]),
    validacion('01.01', C1, 'El capítulo se comprueba cuando <strong>una persona puede identificar su ubicación, la acción principal y el estado de la pantalla sin asistencia</strong>. '
               'Las pruebas de acciones se hacen en una misma sesión, con las acciones principales del producto.'),
]

# ═════════════ 02 · Personas y contextos ═════════════
CAP02 = [
    n2('KYN-SDI-PEX-007', 'Diseñar para quienes utilizan el producto', 1, 'Perfiles operativos como base del diseño',
       'Define de dónde salen las decisiones de experiencia: <strong>de las tareas y las condiciones reales de quienes operan el producto</strong>.', [
        req(N('Las decisiones de experiencia deben basarse en tareas, responsabilidades y necesidades reales de los perfiles que utilizan el sistema.', 'debe')),
        stack([('Perfiles operativos', ['Cada producto documenta quién lo opera: tareas, frecuencia, responsabilidades, condiciones de uso y experiencia. Quien compra el producto y quien lo usa pueden ser personas distintas.']),
               ('Condiciones de uso', ['Dispositivo, entorno, interrupciones y conectividad forman parte del perfil.']),
               ('Accesibilidad', [f'Los perfiles incluyen personas con discapacidad y con atención variable.'])]),
        detalle([('Entregable: perfil operativo', [
            ('Contenido', 'Rol, tareas frecuentes y ocasionales, permisos, contexto de uso, dificultades observadas y fuente de cada dato.'),
            ('Fuente', f'Cada dato se marca como observado o como hipótesis.')])]),
    ], origen=['Diseñar para quienes utilizan el producto (base)', 'Perfiles operativos y condiciones de uso (ampliación de la matriz)', 'UIX-007', 'UIX-009'],
       responsabilidad='Las decisiones de experiencia parten de tareas y necesidades reales de quienes operan el producto.',
       rel=['KYN-SDI-PEX-014', 'SD-20', 'KYN-SDI-ACC-001'], verif=[('Pruebas por perfil', 'Se revisan las pruebas de tareas del producto.', 'cada perfil documentado tiene pruebas con personas de ese perfil, además de las de administración.')], ver='grupo'),

    n2('KYN-SDI-PEX-008', 'Roles y permisos', 2, 'Acciones y datos según el rol',
       'Se aplica a todo producto con roles: <strong>los permisos efectivos deciden qué acciones y datos ve cada persona</strong>, y el servidor lo confirma.', [
        dims([('Interfaz por rol', [N('La interfaz debe distinguir las acciones y la información disponibles para cada rol según sus permisos efectivos.', 'debe'),
                                    'Una acción sin permiso se oculta cuando la persona no necesita saber que existe. Se muestra deshabilitada, con el motivo y a quién pedir el permiso, cuando conocerla ayuda a la tarea.']),
              ('Permisos efectivos', [N('Los permisos efectivos deben determinar las acciones y datos disponibles.', 'debe'),
                                      'Se calculan con el rol y el contexto del registro, como la unidad o el estado. La interfaz muestra lo que ese cálculo permite.']),
              ('Validación en el servidor', [N('Ocultar un control en la interfaz no debe sustituir la validación de autorización.', 'no-debe'),
                                             f'El servidor rechaza toda operación sin permiso, aunque la interfaz ya la oculte, con un mensaje que no revela datos.'])]),
    ], origen=['Roles y necesidades diferenciadas (base)', 'Acceso por responsabilidades (ampliación)', 'UIX-008'],
       responsabilidad='Los permisos efectivos determinan acciones y datos; la interfaz no reemplaza la validación.',
       cita='06 Resultados autorizados (ARQ-016) aplica el límite a la búsqueda',
       rel=['KYN-SDI-ARQ-017'], verif=[('Perfiles', 'Se repite cada tarea con perfiles de distinto permiso.', 'cada perfil ve solo sus acciones y sus datos.'),
              ('Operación directa', 'Se envía la operación no autorizada directamente al servidor, sin pasar por la interfaz.', 'el servidor la rechaza y la respuesta no incluye datos del registro.')], ver='tecnica'),

    n2('KYN-SDI-PEX-009', 'Uso ocasional y frecuente', 3, 'Densidad y ayudas según la frecuencia de uso',
       'Se aplica cuando un producto tiene personas que lo usan a diario y otras que lo usan de vez en cuando: <strong>cambian la ayuda y la densidad, no los patrones</strong>.', [
        dims([('Densidad y ayudas', [N('Un mismo producto puede presentar distintas densidades y ayudas según el contexto operativo, sin cambiar innecesariamente sus patrones de interacción.', 'puede'),
                                     f'El uso ocasional lleva instrucciones visibles, ejemplos y el modo cómodo. El frecuente, ayuda a pedido y el modo denso, si el producto lo ofrece. Los controles y los nombres son los mismos.']),
              ('Esfuerzo de navegación', [N('Las tareas frecuentes deberían requerir menos esfuerzo de navegación que las tareas ocasionales, manteniendo controles y confirmaciones necesarios.', 'deberia'),
                                          'Las tareas diarias tienen accesos directos y elementos recientes; las ocasionales siguen el recorrido de la navegación.']),
              ('Presentación por tarea', [N('Una misma información puede presentarse de distintas maneras según la tarea y el rol, siempre que conserve su significado.', 'puede'),
                                          'Ejemplo: las solicitudes se ven en tabla para la administración y en lista breve para el residente, con los mismos estados y nombres.'])]),
    ], origen=['Uso ocasional y frecuente (base)', 'Frecuencia de uso (ampliación)', 'Contextos distintos (ampliación)', 'UIX-008', 'UIX-029'],
       responsabilidad='Densidad, ayudas y esfuerzo se ajustan a la frecuencia y al contexto, con los mismos patrones.',
       cita='10 Espacio y retícula define los modos de densidad',
       rel=['SD-10'], verif=[('Esfuerzo', 'Se miden los pasos y el tiempo de las tres tareas más frecuentes y de tres ocasionales comparables.', 'las frecuentes requieren menos esfuerzo, con los mismos patrones.')], ver='grupo'),

    seccion('ejemplo', '02', 'Ejemplo de aplicación', 'Administración y residentes',
            'La administración de un residencial y un residente pueden compartir componentes visuales, pero <strong>no necesitan las mismas acciones</strong>, navegación ni profundidad informativa.', [
        stack([('Administración', ['Ve todas las solicitudes, aprueba y exporta.']),
               ('Residente', ['Ve sus solicitudes y crea nuevas; la acción «Aprobar» no existe para su rol.'])]),
    ]),
    validacion('01.02', C2, 'El capítulo se comprueba cuando <strong>cada rol tiene tareas documentadas, permisos comprobados y recorridos evaluables</strong>. '
               'Las pruebas de perfiles se hacen con personas de cada perfil.'),
]

# ═════════════ 03 · Elecciones verificadas ═════════════
CAP03 = [
    n3('KYN-SDI-PEX-010', 'Decisiones justificadas', 1, 'Registro de decisiones de diseño',
       'Se aplica a toda decisión que cambia cómo se usa un producto: <strong>se registra con el problema que resuelve</strong>, para poder revisarla después.', [
        req(N('Toda decisión significativa de diseño debe relacionarse con un problema, una necesidad o una oportunidad identificable.', 'debe')),
        stack([('Alternativas', ['Se comparan al menos dos opciones con los mismos criterios: tarea, perfiles, riesgo y costo.']),
               ('Excepciones', [f'Una desviación de una norma se registra con su motivo, alcance y fecha de revisión.'])]),
        detalle([('Entregable: ficha de decisión', [
            ('Problema', 'Qué pasa y a quién afecta, con su evidencia.'),
            ('Decisión', 'Qué se eligió y por qué, frente a qué alternativas.'),
            ('Resultado esperado', 'Qué debería cambiar y cómo se va a medir.'),
            ('Reutilización', 'Si la decisión sirve a otros productos, se propone para la base compartida.')])]),
    ], origen=['Decisiones justificadas (base)', 'Problema antes de solución (ampliación)', 'Comparar alternativas y registrar excepciones (ampliación de la matriz)', 'UIX-003'],
       responsabilidad='Cada decisión significativa se vincula con un problema, una necesidad o una hipótesis, y queda registrada.',
       rel=['KYN-SDI-GOB-007', 'SD-34'], verif=[('Muestra', 'Se toman al azar tres decisiones de un proyecto.', 'cada una tiene su ficha completa.')]),

    n3('KYN-SDI-PEX-011', 'Prisma como metodología', 2, 'Fases de Prisma y sus entregables',
       'Ordena todo proyecto de diseño en <strong>cinco fases de nombre fijo</strong>, cada una con su entregable.', [
        req(N('Los proyectos deben seguir las cinco fases de Prisma: Amanecer, Mediodía, Atardecer, Anochecer y Galaxia.', 'debe')),
        pasos([('Amanecer', 'Arranque: tipo de proyecto, alcance, quién lo opera y modalidad de investigación.', 'Entregable', 'Acta de inicio aprobada.'),
               ('Mediodía', 'Investigación del contexto operativo real.', 'Entregable', 'Reporte de hallazgos.'),
               ('Atardecer', 'Definición del problema que se resuelve y del que queda fuera.', 'Entregable', 'Brief con criterios de aceptación medibles.'),
               ('Anochecer', f'Ideación, prototipado y validación con personas reales, por capas.', 'Entregable', 'Prototipo validado con su reporte.'),
               ('Galaxia', 'Producto vivo: evoluciona con lo observado.', 'Entregable', 'Bitácora de evolución.')]),
        detalle([('Origen y aprobación', [
            ('Fuente', 'Las fases y sus entregables vienen de UIX-002, con traslado aprobado el 2026-11-09.')])]),
    ], origen=['Prisma como metodología (base)', 'UIX-002'],
       responsabilidad='Los proyectos siguen las cinco fases de Prisma, con su entregable por fase.',
       cita='43 Implementación conserva la operación del método',
       rel=['KYN-SDI-PEX-012', 'SD-42'], verif=[('Expediente', 'Se revisa el expediente de un proyecto en curso.', 'cada fase cerrada tiene su entregable antes de abrir la siguiente.')]),

    n3('KYN-SDI-PEX-012', 'Diseño por capas', 3, 'Estructura, interacción y expresión por capas',
       'Define el orden de trabajo dentro de Anochecer: <strong>primero lo que funciona y después lo que expresa</strong>.', [
        req(N('Durante el diseño y la validación de interfaces se debería trabajar progresivamente sobre estructura, interacción y expresión.', 'deberia')),
        numeradas([('Estructura', ['Arquitectura de información, jerarquía, navegación y organización.']),
                   ('Interacción', ['Componentes, comportamiento, estados y recuperación.']),
                   ('Expresión', ['Identidad visual, color, imágenes, recursos y refinamiento.'])]),
        dims([('Evaluación previa', [N('La estructura y la interacción deben poder evaluarse antes de incorporar recursos gráficos expresivos que no sean necesarios para comprender la experiencia.', 'debe'),
                                     'Las primeras pruebas de Anochecer se hacen sin recursos expresivos.']),
              ('Base contenida', [N('Las propuestas de interfaces deberían evaluarse inicialmente con una base visual contenida, utilizando blanco, grises y Azul Noche, antes de incorporar recursos expresivos no esenciales.', 'deberia'),
                                  'El color funcional se suma cuando la tarea lo necesita para comprenderse, por ejemplo, un estado de error.']),
              ('Dentro de Prisma', ['Las capas se trabajan sobre todo en Anochecer y pueden repetirse en Galaxia. Son una forma de trabajo dentro de una fase; una capa se revisa de nuevo cuando una prueba lo pide.'])]),
    ], origen=['Diseño por capas (base)', 'Estructura antes de expresión (ampliación)'],
       responsabilidad='Estructura, interacción y expresión se trabajan por capas, de forma iterativa, dentro de Prisma.',
       verif=[('Base contenida', 'En la revisión de Anochecer se prueban las tareas principales con la propuesta en blanco, grises y Azul Noche.', 'las tareas se completan antes de sumar la expresión.')]),

    n3('KYN-SDI-PEX-013', 'Diseño basado en resultados', 4, 'Aprobación por resultados de uso',
       'Se aplica cuando se aprueba una propuesta: <strong>cuentan las tareas completadas y los problemas resueltos</strong>, además de la apariencia.', [
        req(N('Una propuesta no debe aprobarse únicamente por su apariencia visual cuando todavía existen problemas conocidos de comprensión, navegación o interacción.', 'no-debe')),
        stack([('Criterios', ['Tareas completadas, errores observados y problemas pendientes con su decisión.']),
               ('Prototipos', ['Se evalúan con tareas, no con preferencias: «¿qué haría aquí?» antes que «¿le gusta?».'])]),
    ], origen=['Diseño basado en resultados (base)', 'Evaluar prototipos (ampliación de la matriz)'],
       responsabilidad='Una propuesta se aprueba por sus resultados de comprensión, navegación e interacción.',
       verif=[('Aprobación', 'Se revisa el acta de aprobación de una propuesta.', 'incluye la lista de problemas conocidos, con su gravedad y su decisión.')], ver='referencia',
       ref=f'Cada aprobación lleva la lista de problemas conocidos con su gravedad y su decisión. Los críticos se resuelven o bloquean el lanzamiento, según {R("KYN-SDI-GOB-002")}.'),

    n3('KYN-SDI-PEX-014', 'Evidencia diferenciada', 5, 'Observaciones, hipótesis y decisiones diferenciadas',
       'Se aplica a toda documentación de diseño: <strong>cada afirmación dice de dónde viene</strong>.', [
        req(N('Las observaciones, hipótesis, resultados de pruebas y decisiones aprobadas deben distinguirse en la documentación.', 'debe'),
            N('Los comportamientos atribuidos a las personas que todavía no se hayan investigado deben identificarse como hipótesis.', 'debe')),
        matriz('Cuatro tipos de afirmación', [('Qué es', ''), ('Cómo se registra', '')], [
            ('Observación', ['Lo que se vio o se midió.', 'Con fuente, fecha y número de personas.']),
            ('Hipótesis', ['Lo que se supone.', 'Con la forma en que se va a comprobar.']),
            ('Resultado', ['Lo que mostró una prueba.', 'Con la tarea, el método y la muestra.']),
            ('Decisión', ['Lo aprobado.', 'Con quién lo aprobó y cuándo.'])]),
    ], origen=['Evidencia diferenciada (ampliación)', 'Hipótesis y evidencia (base, capítulo 02)'],
       responsabilidad='Observaciones, hipótesis, resultados y decisiones se distinguen en la documentación.',
       cita='44 Validación (Evidencia registrada) cita esta norma',
       verif=[('Documento de diseño', 'Se revisan las afirmaciones sobre personas de un documento de diseño.', 'cada una lleva su tipo y ninguna hipótesis aparece como hecho.')]),

    n3('KYN-SDI-PEX-015', 'Evaluación posterior', 6, 'Evaluación de cambios antes de extenderlos',
       'Se aplica a los cambios que podrían pasar a otros productos: <strong>primero se miden donde actúan</strong>.', [
        req(N('Los cambios relevantes deberían comprobarse en las tareas afectadas antes de extenderse a otros productos.', 'deberia')),
        stack([('Medidas', ['Completitud de tareas críticas, tiempo, errores y abandono, antes y después del cambio. Las medidas exactas se acuerdan con Producto, con UIX-048 como referencia.']),
               ('Extensión', ['Un cambio pasa a la base compartida solo con su evaluación.'])]),
    ], origen=['Evaluación posterior (ampliación)', 'UIX-048'],
       responsabilidad='Los cambios se comprueban en las tareas afectadas antes de extenderse.',
       cita='44 Validación define el protocolo de prueba',
       rel=['SD-34'], verif=[('Antes y después', 'Se revisa un cambio relevante ya extendido.', 'tiene sus medidas de antes y de después en la misma tarea.')]),

    seccion('ejemplo', '03', 'Ejemplo de aplicación', 'Un formulario por capas',
            'Se evalúa primero un formulario con blanco, grises y Azul Noche. Después se incorporan <strong>los colores funcionales y los recursos expresivos</strong> justificados.', [
        stack([('Estructura', ['Grupos de campos y orden del proceso, probados con tres tareas.']),
               ('Interacción', ['Validación, errores y recuperación, probados con datos incorrectos.']),
               ('Expresión', ['Color funcional e identidad, cuando las tareas ya se completan.']),
               ('Verificación del capítulo', ['La decisión documenta el problema, la solución elegida, la evidencia disponible y el resultado de su evaluación.'])]),
    ]),
]

CAPITULOS = [
    ('01', '01.01', C1, CAP01, 'Los principios que rigen el diseño de **todos los productos digitales de Keyons**: SaaS de nicho, herramientas internas y desarrollos a medida.'),
    ('01', '01.02', C2, CAP02, None),
    ('01', '01.03', C3, CAP03, None),
]
