"""Módulo 01 · Experiencia (PEX): 01 Principios comunes, 02 Personas y contextos y 03 Elecciones verificadas.
Requisitos: textos de Keylin (base y ampliación, 2026-11-17). Los de PEX-016 a PEX-018 los redactó Claude a partir de las
«Ampliaciones necesarias» de su matriz y requieren aprobación. UIX-002, 003, 005, 007 y 048 se usan como referencia evaluada.
Decisiones, comportamientos, excepciones y verificaciones: propuesta de Claude en borrador.
"""
from .base import N, req, stack, matriz, pasos, detalle, numeradas, c, L, norma, seccion

MOD = 'principios-experiencia'
C1, C2, C3 = 'principios-compartidos', 'personas-y-contextos-de-uso', 'decisiones-verificables-de-experiencia'


def n1(nid, nombre, k, *a, **kw): return norma(nid, nombre, '01.01', MOD, C1, k, *a, **kw)
def n2(nid, nombre, k, *a, **kw): return norma(nid, nombre, '01.02', MOD, C2, k, *a, **kw)
def n3(nid, nombre, k, *a, **kw): return norma(nid, nombre, '01.03', MOD, C3, k, *a, **kw)


# ═════════════ 01 · Principios comunes ═════════════
CAP01 = [
    n1('KYN-SDI-PEX-001', 'La tarea primero', 1, 'Cada pantalla deja claro para qué está',
       'La tarea decide <strong>qué se ve primero</strong>.', [
        req(N('Cada pantalla debe identificar su propósito y permitir reconocer la acción o información principal sin depender de elementos decorativos.', 'debe'),
            N('Cuando una pantalla permite realizar una tarea principal, esa acción debe distinguirse de las secundarias mediante una jerarquía visual y funcional consistente.', 'debe'),
            N('Los recursos gráficos no deben competir por la atención con información esencial o acciones necesarias para completar una tarea.', 'no-debe')),
        stack([('Propósito', ['El título nombra la tarea o el objeto de la pantalla, no el nombre técnico del módulo.']),
               ('Acción principal', [f'Una sola acción principal por grupo de decisión; las demás son secundarias. Su jerarquía la define {L("12")}.']),
               ('Recursos gráficos', [f'Acompañan a la tarea y su uso lo regula {L("11")}.'])]),
        detalle([
            ('Casos límite', [
                ('Pantallas de consulta', 'La información principal ocupa el lugar de la acción principal.'),
                ('Varias tareas en una pantalla', 'Se separan en grupos, cada uno con su acción principal.'),
                ('Paneles de inicio', f'Se ordenan por prioridad operativa, según {L("29")}.')]),
            ('Verificación', [
                ('Primera mirada', 'Una persona que no conoce la pantalla señala la acción o la información principal sin instrucciones. Cinco segundos es la hipótesis inicial de prueba.'),
                ('Sin decoración', 'Al quitar los recursos decorativos, la tarea se entiende y se completa igual.')])]),
    ], origen=['La tarea primero (base)', 'Una acción reconocible (ampliación)', 'Sin competencia visual innecesaria (ampliación)', 'UIX-001', 'UIX-028'],
       responsabilidad='Cada pantalla deja reconocer su propósito y su acción principal sin que los recursos gráficos compitan.',
       cita='11 Recursos visuales (Expresión proporcionada) cita esta norma'),

    n1('KYN-SDI-PEX-002', 'Claridad antes que novedad', 2, 'Lo conocido se usa sin aprenderlo de nuevo',
       'Un patrón comprensible <strong>ahorra explicaciones</strong>.', [
        req(N('La interfaz no debe ocultar funciones necesarias ni sustituir patrones comprensibles únicamente para conseguir una apariencia original.', 'no-debe')),
        stack([('Patrones', ['Para los controles conocidos (enlaces, casillas, menús, pestañas) se usan las convenciones de la web y del sistema operativo.']),
               ('Innovación', ['Un patrón nuevo responde a un problema que el conocido no resuelve y se valida antes de extenderse (PEX-015).'])]),
        detalle([
            ('Cuando dos criterios compiten (propuesta, desde UIX-005)', [
                ('Transparencia antes que fluidez', 'Cada paso importante se muestra, aunque el recorrido sea más largo.'),
                ('Control antes que automatización', 'La persona puede intervenir, revertir y decidir (PEX-017).'),
                ('Comprensión antes que velocidad', 'Un recorrido claro antes que uno rápido y confuso.'),
                ('Convención antes que novedad', 'Se innova donde aporta un valor comprobado.')]),
            ('Verificación', [
                ('Comparación', 'La misma tarea se prueba con el patrón propio y con el convencional. El propio se conserva solo si iguala o mejora el resultado.'),
                ('Funciones visibles', 'Cada función necesaria se encuentra sin pistas externas.')])]),
    ], origen=['Claridad antes que novedad (base)', 'UIX-005'],
       responsabilidad='Las funciones y los patrones comprensibles se conservan por encima de la originalidad.'),

    n1('KYN-SDI-PEX-003', 'Complejidad justificada', 3, 'Cada control visible tiene una razón',
       'Lo visible <strong>corresponde a la tarea</strong>.', [
        req(N('La cantidad de información y controles visibles debería corresponder a la tarea, al perfil de usuario y a la frecuencia de uso.', 'deberia')),
        stack([('Lo visible', [f'Lo que se usa en cada sesión está a la vista; lo ocasional, a un paso, según Información progresiva, en {L("04")}.']),
               ('Pasos', ['Cada paso de una tarea aporta una decisión o un dato. Los que repiten información conocida se eliminan o se completan solos.']),
               ('Perfiles', ['La densidad cambia con el perfil y la frecuencia, según PEX-009.'])]),
        detalle([
            ('Verificación', [
                ('Recuento de controles', 'Se listan los controles visibles con su frecuencia de uso. Resultado esperado: los de uso raro están en un segundo nivel.'),
                ('Recuento de pasos', 'Se cuentan los pasos de las tareas frecuentes. Resultado esperado: cada paso tiene una razón registrada.')])]),
    ], origen=['Complejidad justificada (base)', 'Reducción de pasos innecesarios (ampliación de la matriz)', 'UIX-001'],
       responsabilidad='La cantidad de información, controles y pasos corresponde a la tarea, al perfil y a la frecuencia.',
       cita='04 Información progresiva (ARQ-004) desarrolla el detalle bajo demanda'),

    n1('KYN-SDI-PEX-004', 'Estado comprensible', 4, 'La persona sabe qué pasó con lo que hizo',
       'Cada acción <strong>tiene una respuesta</strong>.', [
        req(N('Después de una acción, el sistema debe comunicar si está procesando, si terminó o si requiere intervención.', 'debe')),
        matriz('Qué comunica el sistema después de una acción', [('Qué comunica', 'A la persona'), ('Cómo', 'Dónde se desarrolla')], [
            ('Procesando', ['Que la acción se recibió y sigue en curso.', f'Indicador en el control o en la zona afectada; texto descriptivo si la espera es larga ({L("15")}).']),
            ('Terminó', ['El resultado real: qué cambió y dónde.', f'Confirmación específica ({L("24")}).']),
            ('Requiere intervención', ['Qué falta y cómo continuar.', 'Mensaje junto al elemento afectado, con una acción.']),
            ('Falló', ['Qué pasó y cómo seguir.', f'Mensaje con una salida ({L("18")}).'])]),
        detalle([
            ('Verificación', [
                ('Tres situaciones', 'Cada acción principal se ejecuta con éxito, con una espera larga y con un fallo.'),
                ('Resultado esperado', 'En los tres casos, la persona describe el estado sin preguntar.')])]),
    ], origen=['Estado comprensible (base)', 'UIX-012', 'UIX-013'],
       responsabilidad='Después de una acción, el sistema comunica si procesa, terminó, necesita intervención o falló.',
       cita='15 Retroalimentación desarrolla los componentes'),

    n1('KYN-SDI-PEX-005', 'Comportamiento previsible', 5, 'Lo que funciona igual se aprende una vez',
       'La consistencia <strong>libera la atención</strong> para el trabajo.', [
        req(N('Los componentes que realizan una misma función deben mantener un comportamiento consistente entre pantallas. Las diferencias requieren una justificación funcional.', 'debe')),
        stack([('Entre pantallas', ['Guardar, cancelar, eliminar y deshacer se comportan igual en todo el producto.']),
               ('Entre productos', [f'Los componentes canónicos se comportan igual en todos los productos Keyons ({L("34")}).']),
               ('Navegación', [f'Para nombres y destinos de navegación rige Acciones previsibles, en {L("05")}.'])]),
        detalle([
            ('Verificación', [
                ('Dos contextos', 'Se ejecuta la misma operación en dos pantallas. Resultado esperado: mismo resultado, mismos mensajes y mismas teclas.'),
                ('Diferencias', 'Cada diferencia de comportamiento tiene su justificación registrada (PEX-010).')])]),
    ], origen=['Comportamiento previsible (ampliación)', 'Consistencia entre pantallas (ampliación de la matriz)', 'UIX-013'],
       responsabilidad='Una misma función se comporta igual en todas las pantallas y productos.',
       cita='05 Acciones previsibles (ARQ-006) aplica el principio a la navegación'),

    n1('KYN-SDI-PEX-006', 'Contexto antes de actuar', 6, 'Antes de confirmar, la persona ve qué va a cambiar',
       'Se decide <strong>con las consecuencias a la vista</strong>.', [
        req(N('Cuando una acción puede afectar información o decisiones importantes, la interfaz debe proporcionar el contexto necesario para comprender sus consecuencias.', 'debe')),
        stack([('Qué se muestra', ['Qué va a cambiar, cuántos elementos, si se puede deshacer y quién más se ve afectado.']),
               ('Proporción', [f'La protección crece con el impacto: deshacer para lo reversible; confirmación explícita para lo irreversible ({L("19")}).'])]),
        detalle([
            ('Verificación', [
                ('Antes de confirmar', 'Antes de cada acción de impacto, la persona describe qué va a cambiar.'),
                ('Resultado esperado', 'Su descripción coincide con lo que ocurre después.')])]),
    ], origen=['Contexto antes de actuar (ampliación)', 'UIX-006'],
       responsabilidad='Antes de una acción de consecuencias, la persona ve qué va a cambiar.',
       cita='19 Procesos críticos (Consecuencias claras) se integra en esta norma o la cita'),

    n1('KYN-SDI-PEX-016', 'Prevención de errores', 7, 'La interfaz evita el error antes de corregirlo',
       'Prevenir <strong>cuesta menos que reparar</strong>.', [
        req(N('La interfaz debería prevenir los errores frecuentes mediante opciones válidas, valores sugeridos y formatos comprensibles antes de que la persona los cometa.', 'deberia')),
        stack([('Opciones válidas', ['Solo se ofrecen las opciones posibles: fechas existentes, cantidades dentro del rango, estados permitidos.']),
               ('Formatos', [f'El formato esperado se ve antes de escribir ({L("13")}).']),
               ('Acciones de riesgo', ['Se separan de las frecuentes y llevan su protección (PEX-006).'])]),
        detalle([
            ('Verificación', [
                ('Errores frecuentes', 'Se registran los errores más frecuentes de una prueba con personas.'),
                ('Resultado esperado', 'Cada uno tiene una medida preventiva o una razón documentada para no tenerla.')])]),
    ], origen=['Prevención de errores (ampliación de la matriz; requisito redactado por Claude)'],
       responsabilidad='La interfaz previene los errores frecuentes antes de que ocurran.',
       cita='13 Entradas y 16 Formularios desarrollan la validación'),

    n1('KYN-SDI-PEX-017', 'Control de la persona', 8, 'La persona puede detener, deshacer y decidir',
       'El sistema propone; <strong>la persona decide</strong>.', [
        req(N('La persona debe poder cancelar, deshacer o corregir las acciones reversibles y decidir sobre lo que el sistema propone.', 'debe')),
        stack([('Deshacer', [f'Toda acción reversible ofrece deshacer en el mismo lugar ({L("18")}).']),
               ('Propuestas del sistema', [f'Lo que el sistema completa o sugiere se presenta como propuesta para revisar ({L("30")}).']),
               ('Procesos largos', ['Se pueden cancelar o pausar cuando el proceso lo permite, y se informa qué queda hecho.'])]),
        detalle([
            ('Verificación', [
                ('Reversión', 'Se ejecuta cada acción reversible y se deshace. Resultado esperado: el estado anterior vuelve completo.'),
                ('Propuestas', 'Cada dato que completa el sistema se puede revisar y cambiar antes de confirmarlo.')])]),
    ], origen=['Control de la persona (ampliación de la matriz; requisito redactado por Claude)', 'UIX-005', 'UIX-025'],
       responsabilidad='La persona puede cancelar, deshacer y decidir sobre lo que el sistema propone.'),

    n1('KYN-SDI-PEX-018', 'Reconocer antes que recordar', 9, 'La interfaz muestra lo que la persona tendría que recordar',
       'La memoria de la persona <strong>no es parte de la tarea</strong>.', [
        req(N('La interfaz debería mostrar las opciones, los datos previos y el contexto necesario, en lugar de exigir que la persona los recuerde entre pantallas.', 'deberia')),
        stack([('Opciones visibles', ['Listas y sugerencias en lugar de códigos que hay que escribir de memoria.']),
               ('Datos previos', ['Lo que la persona eligió en un paso anterior sigue a la vista en el siguiente.']),
               ('Recientes', ['Búsquedas y elementos recientes disponibles cuando la tarea se repite.'])]),
        detalle([
            ('Verificación', [
                ('Recorrido', 'Se recorre una tarea de varios pasos sin papel ni notas.'),
                ('Resultado esperado', 'Ningún paso pide un dato que la persona vio o eligió antes y que ya no está a la vista.')])]),
    ], origen=['Reconocimiento frente a memorización (ampliación de la matriz; requisito redactado por Claude)'],
       responsabilidad='La interfaz muestra opciones, datos previos y contexto en lugar de exigir memoria.'),

    seccion('ejemplo', '01', 'Ejemplo de aplicación', 'Un tablero residencial',
            'En un tablero residencial, las tareas pendientes, los avisos y los accesos operativos tienen <strong>una jerarquía basada en su utilidad</strong>, no en el atractivo de sus colores.', [
        stack([('La tarea primero', ['Arriba, las tareas pendientes del día con su acción principal: «Revisar».']),
               ('Estado', ['Al aprobar una solicitud, la fila cambia a «Aprobada» y aparece «Deshacer».']),
               ('Verificación del capítulo', ['Una persona puede identificar su ubicación, la acción principal y el estado de la pantalla sin asistencia.'])]),
    ]),
]

# ═════════════ 02 · Personas y contextos ═════════════
CAP02 = [
    n2('KYN-SDI-PEX-007', 'Diseñar para quienes utilizan el producto', 1, 'El diseño parte de quien opera el producto',
       'Las decisiones se apoyan en <strong>tareas reales</strong>.', [
        req(N('Las decisiones de experiencia deben basarse en tareas, responsabilidades y necesidades reales de los perfiles que utilizan el sistema.', 'debe')),
        stack([('Perfiles operativos', ['Cada producto documenta quién lo opera: tareas, frecuencia, responsabilidades, condiciones de uso y experiencia. Quien compra el producto no reemplaza a quien lo usa.']),
               ('Condiciones de uso', ['Dispositivo, entorno, interrupciones y conectividad forman parte del perfil.']),
               ('Accesibilidad', [f'Los perfiles incluyen personas con discapacidad y con atención variable. Sus criterios técnicos están en {L("20")}, {L("21")} y {L("22")}.'])]),
        detalle([
            ('Entregable: perfil operativo', [
                ('Contenido', 'Rol, tareas frecuentes y ocasionales, permisos, contexto de uso, dificultades observadas y fuente de cada dato.'),
                ('Fuente', 'Cada dato se marca como observado o como hipótesis (PEX-014).')]),
            ('Verificación', [
                ('Pruebas por perfil', 'Las tareas se prueban con personas de cada perfil, no solo con administradores o desarrolladores.')])]),
    ], origen=['Diseñar para quienes utilizan el producto (base)', 'Perfiles operativos y condiciones de uso (ampliación de la matriz)', 'UIX-007', 'UIX-009'],
       responsabilidad='Las decisiones de experiencia parten de tareas y necesidades reales de quienes operan el producto.'),

    n2('KYN-SDI-PEX-008', 'Roles y permisos', 2, 'Cada rol encuentra lo que le corresponde',
       'Los permisos <strong>definen lo disponible</strong>.', [
        req(N('La interfaz debe distinguir las acciones y la información disponibles para cada rol según sus permisos efectivos.', 'debe'),
            N('Los permisos efectivos deben determinar las acciones y datos disponibles.', 'debe'),
            N('Ocultar un control en la interfaz no debe sustituir la validación de autorización.', 'no-debe')),
        matriz('Qué hacer con una acción sin permiso', [('Cuándo', 'Se elige'), ('Cómo', 'Se presenta')], [
            ('Ocultar', ['Cuando la persona no necesita saber que la acción existe.', 'Sin rastro en la interfaz.']),
            ('Mostrar deshabilitada', ['Cuando conocerla ayuda a la tarea.', 'Con el motivo y a quién pedir el permiso.']),
            ('Rechazar en el servidor', ['Siempre, aunque la interfaz ya la oculte.', 'Con un mensaje que no revela datos (ARQ-017).'])]),
        detalle([
            ('Verificación', [
                ('Perfiles', 'Se repite cada tarea con perfiles de distinto permiso. Resultado esperado: cada uno ve solo lo suyo.'),
                ('Operación directa', 'Se intenta la operación no autorizada directamente contra el servidor. Resultado esperado: se rechaza.')])]),
    ], origen=['Roles y necesidades diferenciadas (base)', 'Acceso por responsabilidades (ampliación)', 'UIX-008'],
       responsabilidad='Los permisos efectivos determinan acciones y datos; la interfaz no reemplaza la validación.',
       cita='06 Resultados autorizados (ARQ-016) aplica el límite a la búsqueda'),

    n2('KYN-SDI-PEX-009', 'Uso ocasional y frecuente', 3, 'La experiencia se ajusta a la frecuencia de uso',
       'Lo diario <strong>pide menos esfuerzo</strong>.', [
        req(N('Un mismo producto puede presentar distintas densidades y ayudas según el contexto operativo, sin cambiar innecesariamente sus patrones de interacción.', 'puede'),
            N('Las tareas frecuentes deberían requerir menos esfuerzo de navegación que las tareas ocasionales, manteniendo controles y confirmaciones necesarios.', 'deberia'),
            N('Una misma información puede presentarse de distintas maneras según la tarea y el rol, siempre que conserve su significado.', 'puede')),
        matriz('Diferencias entre uso ocasional y frecuente', [('Uso ocasional', 'Principiantes'), ('Uso frecuente', 'Experimentados')], [
            ('Ayuda', ['Instrucciones visibles y ejemplos.', 'Ayuda a pedido; atajos a la vista.']),
            ('Densidad', ['Modo cómodo.', f'Modo denso, si el producto lo ofrece ({L("10")}).']),
            ('Acceso', ['Recorrido guiado por la navegación.', 'Accesos directos y elementos recientes.']),
            ('Patrones', ['Los mismos controles y nombres.', 'Los mismos controles y nombres.'])]),
        detalle([
            ('Verificación', [
                ('Esfuerzo', 'Se miden los pasos y el tiempo de las tres tareas más frecuentes.'),
                ('Resultado esperado', 'Requieren menos esfuerzo que tareas ocasionales comparables, con los mismos patrones.')])]),
    ], origen=['Uso ocasional y frecuente (base)', 'Frecuencia de uso (ampliación)', 'Contextos distintos (ampliación)', 'UIX-008', 'UIX-029'],
       responsabilidad='Densidad, ayudas y esfuerzo se ajustan a la frecuencia y al contexto, con los mismos patrones.',
       cita='10 Espacio y retícula define los modos de densidad'),

    seccion('ejemplo', '02', 'Ejemplo de aplicación', 'Administración y residentes',
            'La administración de un residencial y un residente pueden compartir componentes visuales, pero <strong>no necesitan las mismas acciones</strong>, navegación ni profundidad informativa.', [
        stack([('Administración', ['Ve todas las solicitudes, aprueba y exporta.']),
               ('Residente', ['Ve sus solicitudes y crea nuevas; la acción «Aprobar» no existe para su rol.']),
               ('Verificación del capítulo', ['Cada rol tiene tareas documentadas, permisos comprobados y recorridos evaluables.'])]),
    ]),
]

# ═════════════ 03 · Elecciones verificadas ═════════════
CAP03 = [
    n3('KYN-SDI-PEX-010', 'Decisiones justificadas', 1, 'Cada decisión responde a un problema',
       'Una decisión documentada <strong>se puede revisar</strong>.', [
        req(N('Toda decisión significativa de diseño debe relacionarse con un problema, una necesidad o una oportunidad identificable.', 'debe')),
        stack([('Registro', ['Problema, alternativas, decisión, evidencia y resultado esperado.']),
               ('Alternativas', ['Se comparan al menos dos opciones con los mismos criterios: tarea, perfiles, riesgo y costo.']),
               ('Excepciones', [f'Una desviación de una norma se registra con su motivo, alcance y fecha de revisión ({L("43")}).'])]),
        detalle([
            ('Entregable: ficha de decisión', [
                ('Problema', 'Qué pasa y a quién afecta, con su evidencia.'),
                ('Decisión', 'Qué se eligió y por qué, frente a qué alternativas.'),
                ('Resultado esperado', 'Qué debería cambiar y cómo se va a medir.'),
                ('Reutilización', 'Si la decisión sirve a otros productos, se propone para 34 Base compartida.')]),
            ('Verificación', [
                ('Muestra', 'Se toman tres decisiones de un proyecto al azar. Resultado esperado: cada una tiene su ficha completa.')])]),
    ], origen=['Decisiones justificadas (base)', 'Problema antes de solución (ampliación)', 'Comparar alternativas y registrar excepciones (ampliación de la matriz)', 'UIX-003'],
       responsabilidad='Cada decisión significativa se vincula con un problema, una necesidad o una hipótesis, y queda registrada.'),

    n3('KYN-SDI-PEX-011', 'Prisma como metodología', 2, 'Los proyectos siguen las cinco fases de Prisma',
       'Un método común <strong>ordena el trabajo</strong>.', [
        req(N('Los proyectos deben seguir las cinco fases de Prisma: Amanecer, Mediodía, Atardecer, Anochecer y Galaxia.', 'debe')),
        pasos([('Amanecer', 'Arranque: tipo de proyecto, alcance, quién lo opera y modalidad de investigación.', 'Entregable', 'Acta de inicio aprobada.'),
               ('Mediodía', 'Investigación del contexto operativo real.', 'Entregable', 'Reporte de hallazgos.'),
               ('Atardecer', 'Definición del problema que se resuelve y del que queda fuera.', 'Entregable', 'Brief con criterios de aceptación medibles.'),
               ('Anochecer', 'Ideación, prototipado y validación con personas reales, por capas (PEX-012).', 'Entregable', 'Prototipo validado con su reporte.'),
               ('Galaxia', 'Producto vivo: evoluciona con lo observado.', 'Entregable', 'Bitácora de evolución.')]),
        detalle([
            ('Origen y estado', [
                ('Fuente', 'Las fases y sus entregables vienen de UIX-002 (traslado aprobado el 2026-11-09). Las firmas y los roles de aprobación se definen en 42 Gobierno normativo.'),
                ('Nombres', 'Los nombres de las fases son fijos.')]),
            ('Verificación', [
                ('Expediente', 'Cada proyecto tiene el entregable de cada fase cerrada antes de abrir la siguiente.')])]),
    ], origen=['Prisma como metodología (base)', 'UIX-002'],
       responsabilidad='Los proyectos siguen las cinco fases de Prisma, con su entregable por fase.',
       cita='43 Implementación conserva la operación del método'),

    n3('KYN-SDI-PEX-012', 'Diseño por capas', 3, 'La interfaz se construye por capas',
       'Primero lo que funciona; <strong>después lo que expresa</strong>.', [
        req(N('Durante el diseño y la validación de interfaces se debería trabajar progresivamente sobre estructura, interacción y expresión.', 'deberia'),
            N('La estructura y la interacción deben poder evaluarse antes de incorporar recursos gráficos expresivos que no sean necesarios para comprender la experiencia.', 'debe'),
            N('Las propuestas de interfaces deberían evaluarse inicialmente con una base visual contenida, utilizando blanco, grises y Azul Noche, antes de incorporar recursos expresivos no esenciales.', 'deberia')),
        numeradas([('Estructura', ['Arquitectura de información, jerarquía, navegación y organización.']),
                   ('Interacción', ['Componentes, comportamiento, estados y recuperación.']),
                   ('Expresión', ['Identidad visual, color, imágenes, recursos y refinamiento.'])]),
        stack([('Dentro de Prisma', ['Las capas se trabajan sobre todo en Anochecer y pueden repetirse en Galaxia. Son una forma de trabajo dentro de una fase, no fases nuevas.']),
               ('Iteración', ['Una capa se revisa de nuevo cuando una prueba lo pide, aunque ya se haya avanzado a la siguiente.'])]),
        detalle([
            ('Verificación', [
                ('Base contenida', 'En la revisión de Anochecer, la estructura y la interacción se prueban con blanco, grises y Azul Noche.'),
                ('Resultado esperado', 'Las tareas se completan antes de sumar la expresión.')])]),
    ], origen=['Diseño por capas (base)', 'Estructura antes de expresión (ampliación)'],
       responsabilidad='Estructura, interacción y expresión se trabajan por capas, de forma iterativa, dentro de Prisma.'),

    n3('KYN-SDI-PEX-013', 'Diseño basado en resultados', 4, 'Una propuesta se aprueba por lo que logra',
       'La apariencia <strong>no reemplaza la prueba</strong>.', [
        req(N('Una propuesta no debe aprobarse únicamente por su apariencia visual cuando todavía existen problemas conocidos de comprensión, navegación o interacción.', 'no-debe')),
        stack([('Criterios', ['Tareas completadas, errores observados y problemas pendientes con su decisión.']),
               ('Problemas conocidos', [f'Se listan con su gravedad; los críticos se resuelven o bloquean el lanzamiento ({L("44")}).']),
               ('Prototipos', ['Se evalúan con tareas, no con preferencias: «¿qué haría aquí?» antes que «¿le gusta?».'])]),
        detalle([
            ('Verificación', [
                ('Aprobación', 'Cada aprobación incluye la lista de problemas conocidos y su decisión.')])]),
    ], origen=['Diseño basado en resultados (base)', 'Evaluar prototipos (ampliación de la matriz)'],
       responsabilidad='Una propuesta se aprueba por sus resultados de comprensión, navegación e interacción.'),

    n3('KYN-SDI-PEX-014', 'Evidencia diferenciada', 5, 'Se distingue lo observado de lo supuesto',
       'Cada afirmación <strong>dice de dónde viene</strong>.', [
        req(N('Las observaciones, hipótesis, resultados de pruebas y decisiones aprobadas deben distinguirse en la documentación.', 'debe'),
            N('Los comportamientos atribuidos a las personas que todavía no se hayan investigado deben identificarse como hipótesis.', 'debe')),
        matriz('Cuatro tipos de afirmación', [('Qué es', ''), ('Cómo se registra', '')], [
            ('Observación', ['Lo que se vio o se midió.', 'Con fuente, fecha y número de personas.']),
            ('Hipótesis', ['Lo que se supone.', 'Con la forma en que se va a comprobar.']),
            ('Resultado', ['Lo que mostró una prueba.', 'Con la tarea, el método y la muestra.']),
            ('Decisión', ['Lo aprobado.', 'Con quién lo aprobó y cuándo.'])]),
        detalle([
            ('Verificación', [
                ('Documento de diseño', 'Cada afirmación sobre personas lleva su tipo. Resultado esperado: ninguna hipótesis aparece como hecho.')])]),
    ], origen=['Evidencia diferenciada (ampliación)', 'Hipótesis y evidencia (base, capítulo 02)'],
       responsabilidad='Observaciones, hipótesis, resultados y decisiones se distinguen en la documentación.',
       cita='44 Validación (Evidencia registrada) cita esta norma'),

    n3('KYN-SDI-PEX-015', 'Evaluación posterior', 6, 'Los cambios se comprueban donde actúan',
       'Se mide <strong>antes de extender</strong> un cambio.', [
        req(N('Los cambios relevantes deberían comprobarse en las tareas afectadas antes de extenderse a otros productos.', 'deberia')),
        stack([('Medidas', ['Completitud de tareas críticas, tiempo, errores y abandono, antes y después del cambio. Las medidas exactas se acuerdan con Producto (desde UIX-048, como referencia).']),
               ('Extensión', [f'Un cambio pasa a {L("34")} solo con su evaluación.'])]),
        detalle([
            ('Verificación', [
                ('Antes y después', 'Cada cambio relevante tiene sus medidas de antes y de después en la misma tarea.')])]),
    ], origen=['Evaluación posterior (ampliación)', 'UIX-048'],
       responsabilidad='Los cambios se comprueban en las tareas afectadas antes de extenderse.',
       cita='44 Validación define el protocolo de prueba'),

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
