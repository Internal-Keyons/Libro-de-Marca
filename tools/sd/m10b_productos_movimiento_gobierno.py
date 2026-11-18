"""Bloque 4 · 34 Base compartida, 35 Sitio web, 36 Herramientas y 38 White-label (SPR); 39 a 41 Movimiento (MOV);
42 Gobierno normativo, 43 Implementación y 45 Documentación (GOB). Requisitos: textos base de Keylin.
"""
from .base import N, req, stack, matriz, detalle, c, L, M, norma, R, validacion, dims


def nP(slug, n):
    def f(nid, nombre, k, *a, **kw): return norma(nid, nombre, n, 'sistemas-producto', slug, k, *a, **kw)
    return f
def nM(slug, n):
    def f(nid, nombre, k, *a, **kw): return norma(nid, nombre, n, 'movimiento-sensorial', slug, k, *a, **kw)
    return f
def nG(slug, n):
    def f(nid, nombre, k, *a, **kw): return norma(nid, nombre, n, 'calidad-gobierno', slug, k, *a, **kw)
    return f


def simple(fn, nid, nombre, k, titular, entrada, reqs, filas, verif, origen, resp, corto, cita='', ver='breve', ref=''):
    """Norma breve: requisitos y filas de decisión. La verificación (rótulo, condición, resultado) se presenta según su función."""
    partes = [req(*reqs)]
    if filas:
        partes.append(stack(filas))
    return fn(nid, nombre, k, titular, entrada, partes, origen=origen, responsabilidad=resp, corto=corto, cita=cita, verif=verif, ver=ver, ref=ref)


n34, n35, n36, n38 = nP('base-compartida', '10.01'), nP('sitio-web-corporativo-keyons', '10.02'), nP('herramientas-internas-keyons', '10.03'), nP('soluciones-personalizadas-y-white-label', '10.05')
n39, n40, n41 = nM('movimiento-operativo', '11.01'), nM('movimiento-editorial', '11.02'), nM('interaccion-multisensorial', '11.03')
n42, n43, n45 = nG('gobierno-normativo', '12.01'), nG('implementacion-tecnica', '12.02'), nG('documentacion-y-consulta', '12.04')

CAP34 = [
    simple(n34, 'KYN-SDI-SPR-005', 'Infraestructura común', 1, 'Reutilización de componentes, tokens y patrones', 'Se aplica al construir un producto: <strong>lo que ya funciona se reutiliza</strong>.',
           [N('Los productos deben reutilizar componentes, tokens y patrones canónicos cuando exista una solución adecuada a su necesidad.', 'debe')],
           [('Biblioteca', [f'Componentes, tokens y patrones de este libro, versionados ({R("KYN-SDI-FUI-003", "Cambios controlados")}).']), ('Firma UX', ['Los comportamientos comunes que hacen reconocible la calidad Keyons (desde UIX-012).'])],
           [('Reutilización', 'Se revisan los componentes nuevos de un producto.', 'cada uno justifica por qué no sirve uno canónico.')], ['Infraestructura común (base)', 'UIX-012', 'UIX-013'],
           'Los productos reutilizan componentes, tokens y patrones canónicos.', 'Infraestructura', ver='breve'),
    simple(n34, 'KYN-SDI-SPR-006', 'Variaciones justificadas', 2, 'Diferencias justificadas entre productos', 'Se aplica cuando dos productos resuelven algo distinto: <strong>cada diferencia tiene un motivo</strong>.',
           [N('Las diferencias entre productos deberían responder a requisitos funcionales, de contexto o de identidad comprobables.', 'deberia')],
           [('Registro', [f'Cada variación se registra con su motivo ({R("KYN-SDI-PEX-010", "Decisiones justificadas")}).'])],
           [('Revisión', 'Se comparan dos productos y se listan sus diferencias.', 'cada diferencia tiene su motivo registrado.')], ['Variaciones justificadas (base)'],
           'Las diferencias entre productos responden a requisitos comprobables.', 'Variaciones', ver='breve'),
    simple(n34, 'KYN-SDI-SPR-007', 'Compatibilidad', 3, 'Pruebas de los cambios compartidos', 'Se aplica a los cambios en lo que usan varios productos: <strong>se prueban en todos los que dependen de ellos</strong>.',
           [N('Los cambios compartidos deben evaluarse contra las aplicaciones que dependen de ellos.', 'debe')],
           [('Dependencias', ['Cada componente compartido lista los productos que lo usan.'])],
           [('Regresiones', 'Antes de publicar un cambio compartido, se prueban los productos que dependen de él.', 'ninguno presenta regresiones.')], ['Compatibilidad (base)'],
           'Los cambios compartidos se evalúan en sus productos dependientes.', 'Compatibilidad', cita='Aplica FUI-003 (07) a componentes', ver='referencia', ref=f'Se comprueba con el procedimiento de {R("KYN-SDI-FUI-003")}: cada cambio compartido se prueba en los productos que dependen de él antes de publicarse.'),
]
CAP35 = [
    simple(n35, 'KYN-SDI-SPR-008', 'Navegación y propósito', 1, 'Información y acciones del sitio web', 'Se aplica al sitio corporativo de Keyons: <strong>lleva a la información y a la acción</strong>.',
           [N('Las páginas web deben facilitar la localización de información, servicios y acciones relevantes.', 'debe')],
           [('Navegación', [f'Según {L("05")}.']), ('Identidad', [f'La expresión sigue el Libro de Marca ({M("KYN-MRK-COR-001")}).'])],
           [('Tareas', 'Se buscan información, servicios y contacto en escritorio y móvil.', 'se encuentran sin ayuda en los dos.')], ['Navegación y propósito (base)'],
           'Las páginas web facilitan encontrar información, servicios y acciones.', 'Navegación', ver='breve'),
    simple(n35, 'KYN-SDI-SPR-009', 'Interacción accesible', 2, 'Formularios y controles del sitio web', 'Se aplica a formularios, menús y controles del sitio: <strong>siguen las mismas normas que los productos</strong>.',
           [N('Los formularios, menús y controles del sitio deben respetar las normas funcionales compartidas.', 'debe')],
           [('Normas', [f'{L("13")}, {L("16")} y {L("20")} a {L("22")}.'])],
           [('Acciones', 'Se completan las acciones del sitio con teclado y en móvil.', 'todas se completan.')], ['Interacción accesible (base)'],
           'Formularios, menús y controles del sitio respetan las normas compartidas.', 'Interacción', ver='breve'),
]
CAP36 = [
    simple(n36, 'KYN-SDI-SPR-010', 'Eficiencia operativa', 1, 'Eficiencia de las herramientas internas', 'Se aplica a las herramientas de uso interno: <strong>lo frecuente, en menos pasos</strong>.',
           [N('Las herramientas internas deberían priorizar tareas frecuentes, legibilidad y reducción de pasos innecesarios.', 'deberia')],
           [('Densidad', [f'Modo denso por defecto para uso intensivo ({R("KYN-SDI-PEX-009", "Uso ocasional y frecuente")}).']), ('Atajos', ['Atajos de teclado visibles para lo frecuente.'])],
           [('Tareas frecuentes', 'Se cuentan los pasos y el tiempo de las tareas frecuentes.', 'cada paso tiene una razón; los innecesarios se eliminan.')], ['Eficiencia operativa (base)'],
           'Las herramientas internas priorizan tareas frecuentes y reducen pasos.', 'Eficiencia', ver='breve'),
    simple(n36, 'KYN-SDI-SPR-011', 'Permisos y contexto', 2, 'Funciones según el rol del operador', 'Se aplica a cada herramienta interna: <strong>cada operador ve lo de su rol y su contexto</strong>.',
           [N('Cada herramienta debe presentar las funciones y datos correspondientes al rol y contexto del operador.', 'debe')],
           [('Roles', [f'Según Roles y permisos ({R("KYN-SDI-PEX-008", "Roles y permisos")}).'])],
           [('Cambio de contexto', 'Se cambia entre contextos autorizados con cada rol.', 'cada rol ve solo sus funciones y datos en cada contexto.')], ['Permisos y contexto (base)'],
           'Cada herramienta presenta funciones y datos según el rol del operador.', 'Permisos', ver='breve'),
]
CAP38 = [
    simple(n38, 'KYN-SDI-SPR-012', 'Identidad del cliente', 1, 'Identidad del cliente en marca blanca', 'Se aplica a las soluciones de marca blanca: <strong>la marca cambia y la calidad se conserva</strong>.',
           [N('Las soluciones de marca blanca pueden sustituir los recursos visuales de Keyons dentro de los límites definidos para el producto.', 'puede')],
           [('Límites', [f'Los de Personalización controlada ({R("KYN-SDI-SPR-003", "Personalización controlada")}).'])],
           [('Tema del cliente', 'Se aplica la identidad del cliente y se revisan contraste y componentes.', 'se cumplen los mismos mínimos que con la identidad Keyons.')], ['Identidad del cliente (base)', 'UIX-052'],
           'Las soluciones de marca blanca pueden usar la identidad del cliente dentro de límites.', 'Identidad', ver='breve'),
    simple(n38, 'KYN-SDI-SPR-013', 'Calidad funcional', 2, 'Accesibilidad y seguridad con cualquier marca', 'Se aplica a toda personalización de marca blanca: <strong>lo esencial se mantiene</strong>.',
           [N('La personalización no debe comprometer accesibilidad, seguridad ni patrones de interacción necesarios.', 'no-debe')],
           [], [('Pruebas', 'Se repiten las pruebas de accesibilidad y seguridad con la identidad del cliente.', 'los resultados son los mismos que con la identidad Keyons.')], ['Calidad funcional (base)'],
           'La personalización no compromete accesibilidad, seguridad ni patrones.', 'Calidad', ver='tecnica'),
    simple(n38, 'KYN-SDI-SPR-014', 'Ausencia de firma', 3, 'Firma Keyons en productos sin autoría visible', 'Se aplica cuando el acuerdo pide un producto sin firma: <strong>el acuerdo define la firma</strong>.',
           [N('Los productos contratados sin firma visible no deben incorporar elementos de autoría Keyons que contradigan el acuerdo.', 'no-debe')],
           [('Alcance', [f'Según el modelo de marca blanca del Libro de Marca ({M("KYN-MRK-PER-004")}).'])],
           [('Revisión', 'Se revisa el producto entregado.', 'sin elementos de autoría Keyons fuera de lo acordado.')], ['Ausencia de firma (base)'],
           'Los productos sin firma no muestran autoría Keyons.', 'Sin firma', ver='breve'),
]
CAP39 = [
    simple(n39, 'KYN-SDI-MOV-001', 'Movimiento funcional', 1, 'Transiciones que explican un cambio', 'Se aplica al movimiento de la interfaz operativa: <strong>se mueve para orientar</strong>.',
           [N('Las transiciones operativas deben comunicar cambios de estado o continuidad cuando el movimiento facilite comprender la interacción.', 'debe')],
           [('Duraciones', [f'Tokens de movimiento del libro ({c("--m-fast")}, {c("--m-base")}).'])],
           [('Transiciones', 'Se prueban apertura, cierre, espera, confirmación e interrupción.', 'cada transición comunica el cambio de estado o la continuidad.')], ['Movimiento funcional (base)'],
           'Las transiciones operativas comunican cambios de estado o continuidad.', 'Funcional', ver='breve'),
    simple(n39, 'KYN-SDI-MOV-002', 'Duración proporcionada', 2, 'Duración del movimiento', 'Se aplica a toda transición: <strong>rápida y sin hacer esperar</strong>.',
           [N('El movimiento no debe retrasar innecesariamente la ejecución de tareas.', 'no-debe')],
           [('Preferencia', [f'Con movimiento reducido, las transiciones se acortan o desaparecen ({R("KYN-SDI-ACC-006", "Tiempo y movimiento")}).'])],
           [('Interrupción', 'Se lanza una nueva acción durante una transición.', 'la transición se interrumpe y la acción se ejecuta.')], ['Duración proporcionada (base)'],
           'El movimiento no retrasa las tareas.', 'Duración', ver='breve'),
]
CAP40 = [
    simple(n40, 'KYN-SDI-MOV-003', 'Expresión con propósito', 1, 'Movimiento editorial con propósito', 'Se aplica a las animaciones de piezas editoriales: <strong>acompañan la narrativa</strong>.',
           [N('Los recursos de movimiento editorial pueden utilizarse cuando contribuyan a la narrativa o identidad del producto.', 'puede')],
           [('Identidad', [f'Según el movimiento del Libro de Marca ({M("KYN-MRK-ICO-004")}).'])],
           [('Propósito', 'Se revisan las animaciones editoriales de una pieza.', 'cada una tiene su propósito registrado.')], ['Expresión con propósito (base)'],
           'El movimiento editorial se usa cuando aporta a la narrativa o la identidad.', 'Expresión', ver='breve'),
    simple(n40, 'KYN-SDI-MOV-004', 'Comprensión independiente', 2, 'Información comprensible sin animación', 'Se aplica a la información de una pieza animada: <strong>se entiende sin la animación</strong>.',
           [N('La información esencial debe poder comprenderse sin depender de una animación decorativa.', 'debe')],
           [], [('Tres modos', 'Se revisa la pieza con movimiento normal, reducido y desactivado.', 'la información esencial se entiende en los tres.')], ['Comprensión independiente (base)'],
           'La información esencial se entiende sin animación.', 'Comprensión', ver='breve'),
]
CAP41 = [
    simple(n41, 'KYN-SDI-MOV-005', 'Sonido', 1, 'Sonidos no esenciales', 'Se aplica a los sonidos de un producto: <strong>los no esenciales empiezan apagados</strong>.',
           [N('Los sonidos no esenciales pueden habilitarse mediante una preferencia explícita y permanecen desactivados por defecto.', 'puede')],
           [], [('Preferencia', 'Se usa el producto sin activar la preferencia de sonido.', 'solo suenan los avisos esenciales.')], ['Sonido (base)'],
           'Los sonidos no esenciales están desactivados por defecto.', 'Sonido', ver='breve'),
    simple(n41, 'KYN-SDI-MOV-006', 'Háptica', 2, 'Respuestas hápticas', 'Se aplica a la vibración en dispositivos compatibles: <strong>confirma cuando aporta</strong>.',
           [N('Las respuestas hápticas pueden utilizarse en dispositivos compatibles cuando aporten una confirmación útil.', 'puede')],
           [], [('Dispositivos', 'Se usa el producto en un dispositivo compatible.', 'la vibración acompaña solo confirmaciones útiles.')], ['Háptica (base)', 'UIX-046'],
           'La háptica se usa en dispositivos compatibles cuando confirma algo útil.', 'Háptica', ver='breve'),
    simple(n41, 'KYN-SDI-MOV-007', 'Alternativas', 3, 'Alternativas visibles al sonido y la vibración', 'Se aplica a toda información que usa sonido o vibración: <strong>también se ve</strong>.',
           [N('La información importante no debe depender únicamente de sonido o vibración.', 'no-debe')],
           [], [('Sin sonido ni vibración', 'Se desactivan el audio y la háptica.', 'todas las funciones se comprenden.')], ['Alternativas (base)'],
           'La información importante no depende solo de sonido o vibración.', 'Alternativas', ver='breve'),
]
CAP42 = [
    simple(n42, 'KYN-SDI-GOB-004', 'Fuente única', 1, 'Fuente normativa de cada requisito', 'Se aplica a todo requisito del sistema: <strong>una norma, una fuente</strong>.',
           [N('Cada requisito del sistema debe tener una fuente normativa identificable y evitar duplicaciones entre capítulos.', 'debe')],
           [('Registro', ['data/sd-normas.json, con código permanente por norma; las reservadas no se publican.']), ('Citas', ['Lo que regula otro capítulo se cita con enlace.'])],
           [('Consulta', 'Se busca un requisito por nombre, código, estado y referencias.', 'se encuentra en un solo lugar.')], ['Fuente única (base)', 'UIX-010'],
           'Cada requisito tiene una fuente identificable y sin duplicaciones.', 'Fuente única', ver='breve'),
    simple(n42, 'KYN-SDI-GOB-005', 'Estado visible', 2, 'Estado y versión de las normas', 'Se aplica a toda norma publicada: <strong>se sabe qué está aprobado</strong>.',
           [N('Las normas deben distinguir claramente su estado de aprobación y versión.', 'debe')],
           [('Estados', ['Vigente, Borrador y Por definir, en la franja de la portada y en el menú (Guía de la Biblioteca).'])],
           [('Estado', 'Se revisan las normas de un capítulo.', 'cada una muestra su estado y su versión.')], ['Estado visible (base)'],
           'Las normas muestran su estado de aprobación y versión.', 'Estado', ver='breve'),
]
CAP43 = [
    simple(n43, 'KYN-SDI-GOB-006', 'Uso de componentes canónicos', 1, 'Implementación con componentes canónicos', 'Se aplica al implementar un producto: <strong>se construye sobre el sistema</strong>.',
           [N('Las implementaciones deben utilizar los componentes y tokens compartidos cuando sean aplicables.', 'debe')],
           [], [('Código', 'La revisión de código busca componentes y tokens propios donde existe uno compartido.', 'cada caso usa el compartido o tiene una excepción registrada.')], ['Uso de componentes canónicos (base)', 'UIX-011'],
           'Las implementaciones usan los componentes y tokens compartidos.', 'Canónicos', cita='Aplica FUI-001 (07) y SPR-005 (34)', ver='tecnica'),
    simple(n43, 'KYN-SDI-GOB-007', 'Excepciones justificadas', 2, 'Registro de excepciones', 'Se aplica a toda desviación de una norma: <strong>se documenta con su alcance y su fecha de revisión</strong>.',
           [N('Las desviaciones deben documentar su necesidad, alcance y condiciones de revisión.', 'debe')],
           [('Registro', [f'Motivo, alcance, responsable y fecha de revisión ({R("KYN-SDI-PEX-010", "Decisiones justificadas")}).'])],
           [('Registro', 'Se revisan las desviaciones encontradas en el código.', 'cada una tiene su registro.')], ['Excepciones justificadas (base)'],
           'Las desviaciones documentan necesidad, alcance y revisión.', 'Excepciones', ver='breve'),
    simple(n43, 'KYN-SDI-GOB-008', 'Entrega comprobable', 3, 'Pruebas de los componentes compartidos', 'Se aplica antes de reutilizar un componente: <strong>llega con sus pruebas</strong> de comportamiento, accesibilidad y estados.',
           [N('Los componentes compartidos deben incluir pruebas de comportamiento, accesibilidad y estados relevantes antes de considerarse listos para reutilización.', 'debe')],
           [('Pruebas', [f'Comportamiento, estados ({R("KYN-SDI-CPE-002", "Estados de los controles")}), teclado y accesibilidad automática y manual.'])],
           [('Listo para reutilizar', 'Se revisa el componente antes de publicarlo.', 'sus pruebas pasan y su documentación está completa.')], ['Entrega comprobable (base)'],
           'Los componentes compartidos se entregan con pruebas.', 'Entrega', ver='referencia', ref=f'Se comprueba con {R("KYN-SDI-GOB-009")}: el componente se publica con sus pruebas en verde y su documentación completa.'),
]
CAP45 = [
    simple(n45, 'KYN-SDI-GOB-009', 'Componentes documentados', 1, 'Documentación de los componentes canónicos', 'Se aplica a todo componente canónico: <strong>se documenta para que nadie tenga que inventar</strong>.',
           [N('Cada componente canónico debe describir propósito, variantes, estados, comportamiento, accesibilidad y restricciones de uso.', 'debe')],
           [('Modelo', ['Las normas de 12 Acciones y 13 Entradas son el modelo de documentación.'])],
           [('Implementación', 'Un desarrollador implementa el componente solo con su documentación.', 'sin inventar comportamientos fundamentales.')], ['Componentes documentados (base)'],
           'Cada componente canónico documenta propósito, variantes, estados, comportamiento y accesibilidad.', 'Componentes', ver='breve'),
    simple(n45, 'KYN-SDI-GOB-010', 'Ejemplos funcionales', 2, 'Ejemplos de uso correcto e incorrecto', 'Se aplica a la documentación de componentes y patrones: <strong>muestra el uso correcto</strong> donde hay dudas.',
           [N('La documentación debería ofrecer ejemplos correctos y usos incorrectos cuando ayuden a evitar interpretaciones ambiguas.', 'deberia')],
           [], [('Ambigüedad', 'Se revisan las dudas frecuentes de implementación.', 'cada una tiene su ejemplo.')], ['Ejemplos funcionales (base)'],
           'La documentación ofrece ejemplos correctos e incorrectos cuando ayudan.', 'Ejemplos', ver='breve'),
    simple(n45, 'KYN-SDI-GOB-011', 'Versionado', 3, 'Versiones y notas de cambios', 'Se aplica a los cambios relevantes del sistema: <strong>se sabe qué cambió y a quién afecta</strong>.',
           [N('Los cambios relevantes deben mantener trazabilidad y comunicar sus efectos sobre productos existentes.', 'debe')],
           [('Nota de cambios', ['Versión, qué cambió, a quién afecta y cómo migrar.'])],
           [('Trazabilidad', 'Se revisan los cambios publicados.', 'cada uno tiene su nota de cambios con los productos afectados.')], ['Versionado (base)'],
           'Los cambios relevantes son trazables y comunican sus efectos.', 'Versionado', ver='breve'),
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
