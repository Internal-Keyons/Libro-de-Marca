"""Módulo 05 · Patrones (PAT): 16 Formularios, 17 Flujos de trabajo y 18 Recuperación (Bloque 3). 19 va en el Bloque 4.
Requisitos: textos de Keylin (docs/sd/fuente-keylin-2026-11-17.md). PAT-010 (estados vacíos y de espera) lleva un requisito redactado
por Claude a partir de la matriz y de UIX-021 y UIX-026, y requiere aprobación. Patrones: secuencia, condiciones, estados, errores,
recuperación y excepciones. Los formularios se describen como norma; su diagramación se decide con Keylin (CLAUDE.md).
"""
from .base import N, req, stack, matriz, pasos, detalle, c, L, norma, seccion

MOD = 'patrones-interaccion'
C16, C17, C18 = 'formularios-y-validaciones', 'flujos-de-trabajo', 'estados-y-recuperacion'
def n16(nid, nombre, k, *a, **kw): return norma(nid, nombre, '05.01', MOD, C16, k, *a, **kw)
def n17(nid, nombre, k, *a, **kw): return norma(nid, nombre, '05.02', MOD, C17, k, *a, **kw)
def n18(nid, nombre, k, *a, **kw): return norma(nid, nombre, '05.03', MOD, C18, k, *a, **kw)


# ═════════════ 16 · Formularios ═════════════
CAP16 = [
    n16('KYN-SDI-PAT-001', 'Flujo comprensible', 1, 'El formulario sigue el orden del proceso real',
        'Se completa <strong>en el orden en que se piensa</strong>.', [
        req(N('Los formularios deben agrupar campos relacionados y seguir una secuencia que corresponda al proceso real.', 'debe')),
        pasos([('Entrar', 'El título dice para qué es el formulario y qué datos conviene tener a mano.', 'Decisión', 'Si es largo, se anuncia cuántos pasos tiene.'),
               ('Completar por grupos', f'Los campos relacionados van juntos, con un título de grupo ({c("<fieldset>")} y {c("<legend>")}).', 'Decisión', 'Una columna; el orden del grupo sigue el del proceso.'),
               ('Revisar', 'En los formularios de varios pasos, un resumen antes de enviar.', 'Decisión', 'Cada dato del resumen se puede editar.'),
               ('Enviar', 'El botón principal nombra la acción: «Enviar solicitud».', 'Decisión', 'Muestra la carga y evita el doble envío (CPE-002).'),
               ('Confirmar', 'El resultado y el siguiente paso.', 'Decisión', 'Según Terminación clara (PAT-006).')]),
        detalle([
            ('Varios pasos', [
                ('Cuándo', f'Cuando el formulario reúne decisiones distintas o es largo. El progreso sigue {L("17")}.')]),
            ('Verificación', [
                ('Recorrido', 'Personas del perfil completan el formulario sin ayuda, en el orden propuesto.')])]),
    ], origen=['Flujo comprensible (base)', 'Agrupación comprensible y formularios multipaso (matriz)'],
       responsabilidad='Los formularios agrupan campos y siguen la secuencia del proceso real.', corto='Flujo'),

    n16('KYN-SDI-PAT-002', 'Prevención de pérdidas', 2, 'Lo escrito no se pierde por un accidente',
        'El trabajo de la persona <strong>se protege</strong>.', [
        req(N('Cuando exista riesgo de perder información introducida, el sistema debe ofrecer un mecanismo apropiado de recuperación o advertencia.', 'debe')),
        matriz('Situaciones de riesgo', [('Qué hace el sistema', ''), ('Salida', '')], [
            ('Salir con cambios sin guardar', ['Avisa antes de salir.', 'Guardar, descartar o seguir editando.']),
            ('Sesión vencida', ['Conserva lo escrito.', 'Al iniciar sesión, la persona vuelve al formulario con sus datos.']),
            ('Error de red al enviar', ['Conserva los datos.', 'Reintentar sin volver a escribir.']),
            ('Formulario largo', ['Guarda un borrador, si el producto lo permite.', 'Retomar donde quedó.'])]),
        detalle([
            ('Privacidad', [
                ('Datos sensibles', 'Las contraseñas y los datos de pago no se guardan en borradores.')]),
            ('Verificación', [
                ('Interrupciones', 'Se interrumpe el formulario de cuatro formas: salir, vencer la sesión, cortar la red y cerrar la pestaña. Resultado esperado: el trabajo se recupera o el aviso llega antes.')])]),
    ], origen=['Prevención de pérdidas (base)', 'UIX-025'], responsabilidad='El sistema advierte o recupera ante el riesgo de perder lo escrito.', corto='Sin pérdidas'),

    n16('KYN-SDI-PAT-003', 'Validación proporcionada', 3, 'La validación ayuda sin interrumpir',
        'Corregir <strong>sin empezar de nuevo</strong>.', [
        req(N('La validación no debe interrumpir innecesariamente la entrada ni provocar la eliminación de valores correctos.', 'no-debe')),
        stack([('Momento', ['Según Validación útil de 13 Entradas (CPE-006): sin errores mientras se escribe por primera vez.']),
               ('Valores correctos', ['Un error del servidor nunca borra lo que estaba bien.']),
               ('Errores del servidor', ['Se muestran junto al campo que corresponde, con el resto de los datos intactos.'])]),
        detalle([
            ('Verificación', [
                ('Error al enviar', 'Se envía con un dato inválido. Resultado esperado: solo ese campo se marca y los demás conservan su valor.')])]),
    ], origen=['Validación proporcionada (base)'], responsabilidad='La validación no interrumpe ni borra valores correctos.',
       corto='Validación', cita='13 Entradas (CPE-006) define cuándo y cómo se valida'),

    seccion('ejemplo', '16', 'Ejemplo de aplicación', 'Completar, interrumpir y retomar',
            'Un formulario de solicitud <strong>se completa, se interrumpe y se retoma</strong> sin perder lo escrito.', [
        stack([('Verificación del capítulo', ['Completar, corregir, interrumpir y retomar el formulario.'])]),
    ]),
]

# ═════════════ 17 · Flujos de trabajo ═════════════
CAP17 = [
    n17('KYN-SDI-PAT-004', 'Secuencia y progreso', 1, 'La persona sabe en qué paso está y qué falta',
        'El progreso <strong>reduce la incertidumbre</strong>.', [
        req(N('Los procesos de varios pasos deben comunicar su avance y las acciones necesarias para continuar.', 'debe')),
        stack([('Indicador', ['Paso actual, total y nombre de cada paso: «Paso 2 de 4 · Datos del residente».']),
               ('Avanzar', ['Cada paso se valida al continuar; el botón dice adónde lleva: «Continuar a pagos».']),
               ('Retroceder', ['Atrás vuelve al paso anterior con sus datos (PAT-005).'])]),
        detalle([
            ('Notas técnicas', [
                ('Anuncio', f'El indicador marca el paso actual con {c("aria-current=" + chr(34) + "step" + chr(34))}.')]),
            ('Verificación', [
                ('Recorrido', 'En cada paso, la persona dice cuántos faltan y qué necesita para continuar.')])]),
    ], origen=['Secuencia y progreso (base)', 'UIX-031'], responsabilidad='Los procesos de varios pasos comunican avance y lo necesario para continuar.', corto='Progreso'),

    n17('KYN-SDI-PAT-005', 'Contexto conservado', 2, 'Volver atrás no borra lo decidido',
        'Corregir un paso <strong>no obliga a rehacer los demás</strong>.', [
        req(N('El sistema debería conservar información y decisiones válidas cuando la persona retrocede o corrige un paso.', 'deberia'),
            N('Cuando una tarea pueda interrumpirse, el producto debería conservar el progreso recuperable, respetando los requisitos de seguridad y privacidad.', 'deberia')),
        stack([('Al retroceder', ['Los pasos siguientes conservan sus datos, salvo los que dependen del cambio, que se marcan para revisar.']),
               ('Al interrumpir', ['El progreso se guarda y la persona lo retoma desde el mismo paso.'])]),
        detalle([
            ('Verificación', [
                ('Corregir un paso', 'Se corrige el paso 1 desde el paso 3. Resultado esperado: solo cambia lo que depende de esa corrección.'),
                ('Interrumpir', 'Se cierra la sesión en el paso 3 y se vuelve. Resultado esperado: el proceso sigue en el paso 3.')])]),
    ], origen=['Contexto conservado (base)', 'Continuidad del trabajo (ampliación del capítulo 02)'],
       responsabilidad='El sistema conserva decisiones válidas al retroceder y el progreso al interrumpir.', corto='Contexto'),

    n17('KYN-SDI-PAT-006', 'Terminación clara', 3, 'Al terminar, la persona sabe qué pasó y adónde ir',
        'Cada tarea <strong>cierra con un resultado</strong>.', [
        req(N('Al finalizar, la interfaz debe indicar el resultado y ofrecer un destino o siguiente acción comprensible.', 'debe')),
        matriz('Ciclo de un registro', [('Comportamiento', ''), ('Al terminar', '')], [
            ('Crear', ['Formulario con los datos mínimos.', 'Muestra el registro creado y confirma: «Solicitud 2026-118 creada».']),
            ('Editar', ['En el lugar o en un formulario; Cancelar devuelve al estado anterior.', 'Muestra el valor nuevo y «Cambios guardados».']),
            ('Guardar', ['Explícito o automático; el estado «Guardando» o «Guardado» se ve.', 'Confirma sin bloquear el trabajo.']),
            ('Eliminar', ['Según Acciones destructivas (CPE-003).', 'Confirma y ofrece Deshacer cuando se puede.'])]),
        detalle([
            ('Verificación', [
                ('Cuatro acciones', 'Se crea, edita, guarda y elimina un registro. Resultado esperado: cada acción termina con su resultado y un siguiente paso.')])]),
    ], origen=['Terminación clara (base)', 'Crear, editar, guardar y eliminar (descripción del capítulo)'],
       responsabilidad='Cada proceso termina con su resultado y un siguiente paso; el ciclo de un registro es consistente.', corto='Terminación'),

    seccion('ejemplo', '17', 'Ejemplo de aplicación', 'Un proceso de cuatro pasos',
            'Un alta de residente avanza en cuatro pasos, <strong>permite volver sin perder datos</strong> y termina con el registro creado.', [
        stack([('Verificación del capítulo', ['Completar un proceso, regresar, corregir información y finalizar.'])]),
    ]),
]

# ═════════════ 18 · Recuperación ═════════════
CAP18 = [
    n18('KYN-SDI-PAT-007', 'Ruta de salida', 1, 'Ante un error, siempre hay un camino',
        'Un error <strong>explica y ofrece una salida</strong>.', [
        req(N('Ante un error que impide continuar, la interfaz debe ofrecer una alternativa viable o explicar claramente qué impide la recuperación.', 'debe')),
        matriz('Errores y salidas', [('Qué se dice', ''), ('Salida', '')], [
            ('Red o servidor', ['Que la acción no se completó y si los datos se conservaron.', 'Reintentar.']),
            ('Servicio externo o IA', ['Que el servicio no respondió.', 'Una ruta manual en el mismo lugar (desde UIX-023).']),
            ('Permiso', ['Que no tiene acceso, sin revelar datos.', f'Volver o solicitar acceso (ARQ-017 en {L("05")}).']),
            ('Datos inválidos', ['Qué dato y cómo corregirlo.', 'El campo, con su mensaje (CPE-006).'])]),
        detalle([
            ('Verificación', [
                ('Simulación', 'Se simulan errores de red, de servicio, de permiso y de datos. Resultado esperado: cada uno ofrece su salida.')])]),
    ], origen=['Ruta de salida (base)', 'UIX-023', 'UIX-024'], responsabilidad='Ante un error, la interfaz ofrece una alternativa viable o explica qué la impide.',
       corto='Ruta de salida', cita='24 Mensajes define la redacción del error'),

    n18('KYN-SDI-PAT-008', 'Reversibilidad', 2, 'Lo que se puede deshacer, se ofrece deshacer',
        'Deshacer <strong>quita el miedo a equivocarse</strong>.', [
        req(N('Las acciones reversibles deberían ofrecer una opción de deshacer o restaurar cuando resulte técnica y funcionalmente apropiado.', 'deberia')),
        stack([('Deshacer', [f'Aviso breve, sin bloquear la pantalla, con «Deshacer» durante un tiempo suficiente; se anuncia con {c("role=" + chr(34) + "status" + chr(34))}.']),
               ('Restaurar', ['Lo eliminado pasa a una papelera desde donde se recupera, cuando el producto lo permite.'])]),
        detalle([
            ('Verificación', [
                ('Deshacer', 'Se ejecuta una acción reversible y se deshace. Resultado esperado: el estado anterior vuelve completo.')])]),
    ], origen=['Reversibilidad (base)', 'UIX-025'], responsabilidad='Las acciones reversibles ofrecen deshacer o restaurar.', corto='Deshacer',
       cita='Aplica Control de la persona (PEX-017)'),

    n18('KYN-SDI-PAT-009', 'Persistencia', 3, 'Un fallo no borra lo que estaba bien',
        'Lo válido <strong>sobrevive al error</strong>.', [
        req(N('Un fallo no debe eliminar información válida que pueda conservarse de forma segura.', 'no-debe')),
        stack([('Qué se conserva', ['Datos escritos, filtros, selección y posición, mientras sea seguro.']),
               ('Qué no se conserva', ['Datos de pago y contraseñas, por seguridad.'])]),
        detalle([
            ('Verificación', [
                ('Fallo forzado', 'Se fuerza un fallo a mitad de una tarea. Resultado esperado: al reintentar, los datos válidos siguen ahí.')])]),
    ], origen=['Persistencia (base)'], responsabilidad='Un fallo no elimina información válida que pueda conservarse con seguridad.', corto='Persistencia'),

    n18('KYN-SDI-PAT-010', 'Estados vacíos y de espera', 4, 'Un vacío y una espera también orientan',
        'Ninguna pantalla queda <strong>sin explicación</strong>.', [
        req(N('Un estado vacío debe explicar por qué no hay contenido y ofrecer el siguiente paso.', 'debe'),
            N('Una espera debe indicar que el sistema está trabajando.', 'debe')),
        matriz('Estados vacíos y de espera', [('Qué muestra', ''), ('Acción', '')], [
            ('Vacío por primera vez', ['Para qué sirve el espacio: «Aún no hay solicitudes».', 'Crear la primera.']),
            ('Vacío por filtros', [f'Que los filtros no tienen coincidencias ({L("06")}).', 'Quitar filtros.']),
            ('Espera breve', ['Un indicador en el lugar de la acción.', '—']),
            ('Espera larga', [f'Qué está haciendo el sistema y, si se conoce, el avance ({L("15")}).', 'Cancelar, si se puede.'])]),
        detalle([
            ('Notas técnicas', [
                ('Anuncio', f'Los cambios de estado se anuncian en una región {c("role=" + chr(34) + "status" + chr(34))}, sin mover el foco.'),
                ('Umbral', 'El tiempo a partir del cual una espera es larga es una hipótesis que hay que validar (UIX-021 proponía 400 ms y 3 s).')]),
            ('Verificación', [
                ('Cuatro casos', 'Se fuerza cada estado. Resultado esperado: ninguno queda en blanco ni sin una acción posible.')])]),
    ], origen=['Estados vacíos y de espera (matriz y descripción del capítulo; requisito redactado por Claude)', 'UIX-021', 'UIX-026'],
       responsabilidad='Los estados vacíos explican y orientan; las esperas muestran que el sistema trabaja.', corto='Vacíos y esperas'),

    seccion('ejemplo', '18', 'Ejemplo de aplicación', 'Un pago que no se verificó',
            'Si la verificación automática de un pago falla, <strong>la persona puede adjuntar el comprobante</strong> en el mismo lugar.', [
        stack([('Verificación del capítulo', ['Simular errores de red, validación y operación, comprobando la recuperación.'])]),
    ]),
]

CAPITULOS = [
    ('05', '05.01', C16, CAP16, None),
    ('05', '05.02', C17, CAP17, None),
    ('05', '05.03', C18, CAP18, None),
]
