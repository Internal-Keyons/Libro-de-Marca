"""Bloque 4 · 34 Base compartida, 35 Sitio web, 36 Herramientas y 38 White-label (SPR); 39 a 41 Movimiento (MOV);
42 Gobierno normativo, 43 Implementación y 45 Documentación (GOB). Requisitos: textos base de Keylin.
"""
from .base import N, req, stack, matriz, detalle, c, L, M, norma


def nP(slug, n):
    def f(nid, nombre, k, *a, **kw): return norma(nid, nombre, n, 'sistemas-producto', slug, k, *a, **kw)
    return f
def nM(slug, n):
    def f(nid, nombre, k, *a, **kw): return norma(nid, nombre, n, 'movimiento-sensorial', slug, k, *a, **kw)
    return f
def nG(slug, n):
    def f(nid, nombre, k, *a, **kw): return norma(nid, nombre, n, 'calidad-gobierno', slug, k, *a, **kw)
    return f


def simple(fn, nid, nombre, k, titular, entrada, reqs, filas, verif, origen, resp, corto, cita=''):
    """Norma breve: requisitos, filas de decisión y verificación en detalle plegable"""
    partes = [req(*reqs)]
    if filas:
        partes.append(stack(filas))
    partes.append(detalle([('Verificación', verif)]))
    return fn(nid, nombre, k, titular, entrada, partes, origen=origen, responsabilidad=resp, corto=corto, cita=cita)


n34, n35, n36, n38 = nP('base-compartida', '10.01'), nP('sitio-web-corporativo-keyons', '10.02'), nP('herramientas-internas-keyons', '10.03'), nP('soluciones-personalizadas-y-white-label', '10.05')
n39, n40, n41 = nM('movimiento-operativo', '11.01'), nM('movimiento-editorial', '11.02'), nM('interaccion-multisensorial', '11.03')
n42, n43, n45 = nG('gobierno-normativo', '12.01'), nG('implementacion-tecnica', '12.02'), nG('documentacion-y-consulta', '12.04')

CAP34 = [
    simple(n34, 'KYN-SDI-SPR-005', 'Infraestructura común', 1, 'Los productos reutilizan lo que ya funciona', 'Lo común <strong>se construye una vez</strong>.',
           [N('Los productos deben reutilizar componentes, tokens y patrones canónicos cuando exista una solución adecuada a su necesidad.', 'debe')],
           [('Biblioteca', ['Componentes, tokens y patrones de este libro, versionados (FUI-003).']), ('Firma UX', ['Los comportamientos comunes que hacen reconocible la calidad Keyons (desde UIX-012).'])],
           [('Reutilización', 'Cada componente nuevo justifica por qué no sirve uno canónico.')], ['Infraestructura común (base)', 'UIX-012', 'UIX-013'],
           'Los productos reutilizan componentes, tokens y patrones canónicos.', 'Infraestructura'),
    simple(n34, 'KYN-SDI-SPR-006', 'Variaciones justificadas', 2, 'Cada diferencia entre productos tiene una razón', 'Distinto <strong>solo cuando hace falta</strong>.',
           [N('Las diferencias entre productos deberían responder a requisitos funcionales, de contexto o de identidad comprobables.', 'deberia')],
           [('Registro', ['Cada variación se registra con su motivo (PEX-010).'])],
           [('Revisión', 'Toda diferencia entre dos productos tiene su motivo registrado.')], ['Variaciones justificadas (base)'],
           'Las diferencias entre productos responden a requisitos comprobables.', 'Variaciones'),
    simple(n34, 'KYN-SDI-SPR-007', 'Compatibilidad', 3, 'Un cambio compartido se prueba en todos', 'Lo común <strong>se cuida en común</strong>.',
           [N('Los cambios compartidos deben evaluarse contra las aplicaciones que dependen de ellos.', 'debe')],
           [('Dependencias', ['Cada componente compartido lista los productos que lo usan.'])],
           [('Regresiones', 'Antes de publicar un cambio, se prueban los productos que dependen de él.')], ['Compatibilidad (base)'],
           'Los cambios compartidos se evalúan en sus productos dependientes.', 'Compatibilidad', cita='Aplica FUI-003 (07) a componentes'),
]
CAP35 = [
    simple(n35, 'KYN-SDI-SPR-008', 'Navegación y propósito', 1, 'El sitio lleva a la información y a la acción', 'Encontrar <strong>y actuar</strong>.',
           [N('Las páginas web deben facilitar la localización de información, servicios y acciones relevantes.', 'debe')],
           [('Navegación', [f'Según {L("05")}.']), ('Identidad', [f'La expresión sigue el Libro de Marca ({M("KYN-MRK-COR-001")}).'])],
           [('Tareas', 'Se localizan información, servicios y contacto en escritorio y móvil.')], ['Navegación y propósito (base)'],
           'Las páginas web facilitan encontrar información, servicios y acciones.', 'Navegación'),
    simple(n35, 'KYN-SDI-SPR-009', 'Interacción accesible', 2, 'Los formularios del sitio siguen las normas', 'El sitio <strong>usa el mismo sistema</strong>.',
           [N('Los formularios, menús y controles del sitio deben respetar las normas funcionales compartidas.', 'debe')],
           [('Normas', [f'{L("13")}, {L("16")} y {L("20")} a {L("22")}.'])],
           [('Acciones', 'Se completan las acciones del sitio con teclado y en móvil.')], ['Interacción accesible (base)'],
           'Formularios, menús y controles del sitio respetan las normas compartidas.', 'Interacción'),
]
CAP36 = [
    simple(n36, 'KYN-SDI-SPR-010', 'Eficiencia operativa', 1, 'Lo frecuente, en menos pasos', 'Herramientas <strong>para trabajar rápido</strong>.',
           [N('Las herramientas internas deberían priorizar tareas frecuentes, legibilidad y reducción de pasos innecesarios.', 'deberia')],
           [('Densidad', ['Modo denso por defecto para uso intensivo (PEX-009).']), ('Atajos', ['Atajos de teclado visibles para lo frecuente.'])],
           [('Tareas frecuentes', 'Se cuentan los pasos y el tiempo de las tareas frecuentes; se reducen los innecesarios.')], ['Eficiencia operativa (base)'],
           'Las herramientas internas priorizan tareas frecuentes y reducen pasos.', 'Eficiencia'),
    simple(n36, 'KYN-SDI-SPR-011', 'Permisos y contexto', 2, 'Cada operador ve lo de su rol', 'Funciones <strong>según el rol</strong>.',
           [N('Cada herramienta debe presentar las funciones y datos correspondientes al rol y contexto del operador.', 'debe')],
           [('Roles', ['Según Roles y permisos (PEX-008).'])],
           [('Cambio de contexto', 'Se cambia entre contextos autorizados y se resuelven errores con cada rol.')], ['Permisos y contexto (base)'],
           'Cada herramienta presenta funciones y datos según el rol del operador.', 'Permisos'),
]
CAP38 = [
    simple(n38, 'KYN-SDI-SPR-012', 'Identidad del cliente', 1, 'El cliente puede usar su propia identidad', 'La marca cambia; <strong>la calidad no</strong>.',
           [N('Las soluciones de marca blanca pueden sustituir los recursos visuales de Keyons dentro de los límites definidos para el producto.', 'puede')],
           [('Límites', ['Los de Personalización controlada (SPR-003).'])],
           [('Tema del cliente', 'Se aplica la identidad del cliente y se revisan contraste y componentes.')], ['Identidad del cliente (base)', 'UIX-052'],
           'Las soluciones de marca blanca pueden usar la identidad del cliente dentro de límites.', 'Identidad'),
    simple(n38, 'KYN-SDI-SPR-013', 'Calidad funcional', 2, 'Personalizar no rompe lo esencial', 'Accesible y seguro <strong>con cualquier marca</strong>.',
           [N('La personalización no debe comprometer accesibilidad, seguridad ni patrones de interacción necesarios.', 'no-debe')],
           [], [('Pruebas', 'Con la identidad del cliente se repiten las pruebas de accesibilidad y seguridad.')], ['Calidad funcional (base)'],
           'La personalización no compromete accesibilidad, seguridad ni patrones.', 'Calidad'),
    simple(n38, 'KYN-SDI-SPR-014', 'Ausencia de firma', 3, 'Sin firma visible cuando el acuerdo lo pide', 'El acuerdo <strong>define la firma</strong>.',
           [N('Los productos contratados sin firma visible no deben incorporar elementos de autoría Keyons que contradigan el acuerdo.', 'no-debe')],
           [('Alcance', [f'Según el modelo de marca blanca del Libro de Marca ({M("KYN-MRK-PER-004")}).'])],
           [('Revisión', 'En el producto entregado no aparecen elementos de autoría Keyons fuera de lo acordado.')], ['Ausencia de firma (base)'],
           'Los productos sin firma no muestran autoría Keyons.', 'Sin firma'),
]
CAP39 = [
    simple(n39, 'KYN-SDI-MOV-001', 'Movimiento funcional', 1, 'El movimiento explica un cambio', 'Moverse <strong>para orientar</strong>.',
           [N('Las transiciones operativas deben comunicar cambios de estado o continuidad cuando el movimiento facilite comprender la interacción.', 'debe')],
           [('Duraciones', [f'Tokens de movimiento del libro ({c("--m-fast")}, {c("--m-base")}).'])],
           [('Transiciones', 'Se prueban apertura, cierre, espera, confirmación e interrupción.')], ['Movimiento funcional (base)'],
           'Las transiciones operativas comunican cambios de estado o continuidad.', 'Funcional'),
    simple(n39, 'KYN-SDI-MOV-002', 'Duración proporcionada', 2, 'El movimiento no hace esperar', 'Rápido <strong>y respetuoso</strong>.',
           [N('El movimiento no debe retrasar innecesariamente la ejecución de tareas.', 'no-debe')],
           [('Preferencia', ['Con movimiento reducido, las transiciones se acortan o desaparecen (ACC-006).'])],
           [('Interrupción', 'Una transición se puede interrumpir con una nueva acción.')], ['Duración proporcionada (base)'],
           'El movimiento no retrasa las tareas.', 'Duración'),
]
CAP40 = [
    simple(n40, 'KYN-SDI-MOV-003', 'Expresión con propósito', 1, 'El movimiento editorial acompaña la narrativa', 'Expresar <strong>con intención</strong>.',
           [N('Los recursos de movimiento editorial pueden utilizarse cuando contribuyan a la narrativa o identidad del producto.', 'puede')],
           [('Identidad', [f'Según el movimiento del Libro de Marca ({M("KYN-MRK-ICO-004")}).'])],
           [('Propósito', 'Cada animación editorial tiene un propósito registrado.')], ['Expresión con propósito (base)'],
           'El movimiento editorial se usa cuando aporta a la narrativa o la identidad.', 'Expresión'),
    simple(n40, 'KYN-SDI-MOV-004', 'Comprensión independiente', 2, 'Se entiende sin la animación', 'La animación <strong>suma, no sostiene</strong>.',
           [N('La información esencial debe poder comprenderse sin depender de una animación decorativa.', 'debe')],
           [], [('Tres modos', 'Se revisa con movimiento normal, reducido y desactivado.')], ['Comprensión independiente (base)'],
           'La información esencial se entiende sin animación.', 'Comprensión'),
]
CAP41 = [
    simple(n41, 'KYN-SDI-MOV-005', 'Sonido', 1, 'El sonido no esencial empieza apagado', 'Sonar <strong>solo si la persona quiere</strong>.',
           [N('Los sonidos no esenciales pueden habilitarse mediante una preferencia explícita y permanecen desactivados por defecto.', 'puede')],
           [], [('Preferencia', 'Sin activar la preferencia, el producto no emite sonidos no esenciales.')], ['Sonido (base)'],
           'Los sonidos no esenciales están desactivados por defecto.', 'Sonido'),
    simple(n41, 'KYN-SDI-MOV-006', 'Háptica', 2, 'La vibración confirma cuando aporta', 'Una confirmación <strong>que se siente</strong>.',
           [N('Las respuestas hápticas pueden utilizarse en dispositivos compatibles cuando aporten una confirmación útil.', 'puede')],
           [], [('Dispositivos', 'En un dispositivo compatible, la vibración acompaña solo confirmaciones útiles.')], ['Háptica (base)', 'UIX-046'],
           'La háptica se usa en dispositivos compatibles cuando confirma algo útil.', 'Háptica'),
    simple(n41, 'KYN-SDI-MOV-007', 'Alternativas', 3, 'Nada importante depende solo del sonido o la vibración', 'Siempre <strong>también se ve</strong>.',
           [N('La información importante no debe depender únicamente de sonido o vibración.', 'no-debe')],
           [], [('Sin sonido ni vibración', 'Con audio y háptica desactivados, todas las funciones se comprenden.')], ['Alternativas (base)'],
           'La información importante no depende solo de sonido o vibración.', 'Alternativas'),
]
CAP42 = [
    simple(n42, 'KYN-SDI-GOB-004', 'Fuente única', 1, 'Cada requisito vive en un solo lugar', 'Una norma, <strong>una fuente</strong>.',
           [N('Cada requisito del sistema debe tener una fuente normativa identificable y evitar duplicaciones entre capítulos.', 'debe')],
           [('Registro', ['data/sd-normas.json, con código permanente por norma; las reservadas no se publican.']), ('Citas', ['Lo que regula otro capítulo se cita con enlace.'])],
           [('Consulta', 'Cada requisito se encuentra por nombre, código, estado y referencias.')], ['Fuente única (base)', 'UIX-010'],
           'Cada requisito tiene una fuente identificable y sin duplicaciones.', 'Fuente única'),
    simple(n42, 'KYN-SDI-GOB-005', 'Estado visible', 2, 'Cada norma dice si está vigente', 'Saber <strong>qué está aprobado</strong>.',
           [N('Las normas deben distinguir claramente su estado de aprobación y versión.', 'debe')],
           [('Estados', ['Vigente, Borrador y Por definir, en la franja de la portada y en el menú (Guía de la Biblioteca).'])],
           [('Estado', 'Cada norma muestra su estado y versión.')], ['Estado visible (base)'],
           'Las normas muestran su estado de aprobación y versión.', 'Estado'),
]
CAP43 = [
    simple(n43, 'KYN-SDI-GOB-006', 'Uso de componentes canónicos', 1, 'Se implementa con lo compartido', 'Construir <strong>sobre el sistema</strong>.',
           [N('Las implementaciones deben utilizar los componentes y tokens compartidos cuando sean aplicables.', 'debe')],
           [], [('Código', 'La revisión de código comprueba el uso de componentes y tokens compartidos.')], ['Uso de componentes canónicos (base)', 'UIX-011'],
           'Las implementaciones usan los componentes y tokens compartidos.', 'Canónicos', cita='Aplica FUI-001 (07) y SPR-005 (34)'),
    simple(n43, 'KYN-SDI-GOB-007', 'Excepciones justificadas', 2, 'Cada desviación se documenta', 'Una excepción <strong>tiene fecha de revisión</strong>.',
           [N('Las desviaciones deben documentar su necesidad, alcance y condiciones de revisión.', 'debe')],
           [('Registro', ['Motivo, alcance, responsable y fecha de revisión (PEX-010).'])],
           [('Registro', 'Toda desviación encontrada en el código tiene su registro.')], ['Excepciones justificadas (base)'],
           'Las desviaciones documentan necesidad, alcance y revisión.', 'Excepciones'),
    simple(n43, 'KYN-SDI-GOB-008', 'Entrega comprobable', 3, 'Un componente compartido llega con sus pruebas', 'Probado <strong>antes de reutilizarse</strong>.',
           [N('Los componentes compartidos deben incluir pruebas de comportamiento, accesibilidad y estados relevantes antes de considerarse listos para reutilización.', 'debe')],
           [('Pruebas', ['Comportamiento, estados (CPE-002), teclado y accesibilidad automática y manual.'])],
           [('Listo para reutilizar', 'El componente tiene sus pruebas en verde y su documentación (GOB-009).')], ['Entrega comprobable (base)'],
           'Los componentes compartidos se entregan con pruebas.', 'Entrega'),
]
CAP45 = [
    simple(n45, 'KYN-SDI-GOB-009', 'Componentes documentados', 1, 'Cada componente explica cómo usarlo', 'Documentar <strong>para no inventar</strong>.',
           [N('Cada componente canónico debe describir propósito, variantes, estados, comportamiento, accesibilidad y restricciones de uso.', 'debe')],
           [('Modelo', ['Las normas de 12 Acciones y 13 Entradas son el modelo de documentación.'])],
           [('Implementación', 'Un desarrollador implementa el componente con su documentación, sin inventar comportamientos fundamentales.')], ['Componentes documentados (base)'],
           'Cada componente canónico documenta propósito, variantes, estados, comportamiento y accesibilidad.', 'Componentes'),
    simple(n45, 'KYN-SDI-GOB-010', 'Ejemplos funcionales', 2, 'Ejemplos que evitan malentendidos', 'Mostrar <strong>el uso correcto</strong>.',
           [N('La documentación debería ofrecer ejemplos correctos y usos incorrectos cuando ayuden a evitar interpretaciones ambiguas.', 'deberia')],
           [], [('Ambigüedad', 'Las dudas frecuentes de implementación tienen su ejemplo.')], ['Ejemplos funcionales (base)'],
           'La documentación ofrece ejemplos correctos e incorrectos cuando ayudan.', 'Ejemplos'),
    simple(n45, 'KYN-SDI-GOB-011', 'Versionado', 3, 'Cada cambio relevante deja su rastro', 'Saber <strong>qué cambió y a quién afecta</strong>.',
           [N('Los cambios relevantes deben mantener trazabilidad y comunicar sus efectos sobre productos existentes.', 'debe')],
           [('Nota de cambios', ['Versión, qué cambió, a quién afecta y cómo migrar.'])],
           [('Trazabilidad', 'Cada cambio publicado tiene su nota de cambios.')], ['Versionado (base)'],
           'Los cambios relevantes son trazables y comunican sus efectos.', 'Versionado'),
]

CAPITULOS = [
    ('10', '10.01', 'base-compartida', CAP34, None),
    ('10', '10.02', 'sitio-web-corporativo-keyons', CAP35, None),
    ('10', '10.03', 'herramientas-internas-keyons', CAP36, None),
    ('10', '10.05', 'soluciones-personalizadas-y-white-label', CAP38, None),
    ('11', '11.01', 'movimiento-operativo', CAP39, None),
    ('11', '11.02', 'movimiento-editorial', CAP40, None),
    ('11', '11.03', 'interaccion-multisensorial', CAP41, None),
    ('12', '12.01', 'gobierno-normativo', CAP42, None),
    ('12', '12.02', 'implementacion-tecnica', CAP43, None),
    ('12', '12.04', 'documentacion-y-consulta', CAP45, None),
]
