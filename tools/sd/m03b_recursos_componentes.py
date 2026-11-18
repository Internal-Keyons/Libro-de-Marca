"""Bloque 4 · 11 Recursos visuales (FUI), 14 Estructura y 15 Retroalimentación (CPE), y 19 Procesos críticos (PAT).
Requisitos: textos base de Keylin (docs/sd/fuente-keylin-2026-11-17.md, Bloque 4). Lo demás es propuesta de Claude en borrador.
"""
from .base import N, req, stack, matriz, detalle, serie, c, L, M, norma, seccion, R, validacion, dims


# ═════════════ 11 · Recursos visuales ═════════════
def n11(nid, nombre, k, *a, **kw): return norma(nid, nombre, '03.05', 'fundamentos-interfaz', 'recursos-visuales-de-interfaz', k, *a, **kw)


CAP11 = [
    n11('KYN-SDI-FUI-015', 'Iconos funcionales', 1, 'Función de cada ícono',
        'Se aplica a todo ícono de la interfaz: <strong>informa o acciona</strong>, y se entiende o lleva texto.', [
        req(N('Los iconos deben identificar una acción, estado, categoría o significado comprensible.', 'debe')),
        matriz('Uso de íconos en la interfaz', [('Cómo', ''), ('Accesibilidad', '')], [
            ('Con texto', ['El ícono acompaña a la etiqueta.', 'Decorativo para el lector: aria-hidden.']),
            ('Solo ícono', ['Solo cuando su significado es universal: cerrar, buscar, más opciones.', 'Nombre accesible y etiqueta con el foco y el cursor.']),
            ('De estado', [f'Junto al texto del estado ({R("KYN-SDI-FUI-005", "Estados semánticos")}).', 'El texto lleva el significado.'])]),
        detalle([
            ('Notas técnicas', [
                ('Catálogo', f'Del catálogo aprobado ({M("KYN-MRK-ICO-005")}); los decorativos no reemplazan a los funcionales.')])]),
    ], verif=[('Comprensión', 'Se muestran los íconos sin etiquetas y se pregunta qué hace cada uno.', 'los que no se entienden solos llevan texto visible.')], ver='breve',
       origen=['Iconos funcionales (base)'], responsabilidad='Cada ícono identifica una acción, estado, categoría o significado.', corto='Íconos'),

    n11('KYN-SDI-FUI-016', 'Identidad visual', 2, 'Recursos gráficos según la marca',
        'Se aplica a íconos, ilustraciones, fotografías y patrones de una interfaz: <strong>la identidad se aplica con sus normas</strong>.', [
        req(N('Los recursos gráficos deben utilizar las normas oficiales de iconografía, ilustración, fotografía y composición cuando corresponda aplicar la identidad Keyons.', 'debe')),
        stack([('Dónde están', [f'Iconografía, ilustración, fotografía y composición viven en el Libro de Marca; aquí se citan ({M("KYN-MRK-ICO-003")}, {M("KYN-MRK-ESP-004")}).']),
               ('Productos sin firma', [f'Los recursos de cliente siguen {L("38")}.'])]),
    ], verif=[('Revisión', 'Se revisan los recursos gráficos de una pantalla.', 'cada uno corresponde a una norma del Libro de Marca o a la identidad aprobada del cliente.')], ver='breve',
       origen=['Identidad visual (base)'], responsabilidad='Los recursos gráficos aplican las normas oficiales de la marca.', corto='Identidad'),

    n11('KYN-SDI-FUI-017', 'Expresión proporcionada', 3, 'Recursos expresivos subordinados a la tarea',
        'Se aplica a fotografías, degradados, texturas y animaciones: <strong>acompañan sin competir</strong> con la información y las acciones.', [
        req(N('Fotografías, degradados, texturas y otros recursos expresivos no deben competir con tareas o información esencial.', 'no-debe')),
        stack([('Principio', [f'Se aplica La tarea primero ({L("01")}): esta norma la desarrolla para los recursos gráficos.']),
               ('Dónde sí', [f'Bienvenidas, estados vacíos y recorridos de presentación ({R("KYN-SDI-SPR-002", "Sobriedad operativa")}).'])]),
    ], verif=[('Retirar lo decorativo', 'Se quita un recurso decorativo de la pantalla.', 'la información necesaria para usar la interfaz sigue completa.')], ver='breve',
       origen=['Expresión proporcionada (base)'], responsabilidad='Los recursos expresivos no compiten con tareas ni información esencial.', corto='Expresión',
       cita='Desarrolla PEX-001 (01) para los recursos gráficos'),

    seccion('ejemplo', '11', 'Ejemplo de aplicación', 'Bienvenida y registro',
            'Una pantalla de bienvenida puede incorporar <strong>una fotografía protagonista</strong>; una pantalla de registro operativo puede mantenerse contenida.', [
        stack([('Verificación del capítulo', ['Al retirar un elemento meramente decorativo, se comprueba que no desaparece información necesaria para utilizar la interfaz.'])]),
    ]),
]

# ═════════════ 14 · Estructura ═════════════
def n14(nid, nombre, k, *a, **kw): return norma(nid, nombre, '04.03', 'componentes-estados', 'componentes-de-estructura', k, *a, **kw)


CAP14 = [
    n14('KYN-SDI-CPE-008', 'Contenedores con función', 1, 'Paneles, pestañas, acordeones y diálogos',
        'Define cuándo se usa cada contenedor: <strong>cuando su estructura facilita la tarea</strong>.', [
        req(N('Paneles, pestañas, acordeones y diálogos deben utilizarse cuando su estructura facilite la comprensión o interacción.', 'debe')),
        matriz('Qué contenedor usar', [('Cuándo', ''), ('Comportamiento', '')], [
            ('Pestañas', ['Vistas paralelas del mismo objeto, una a la vez.', f'Flechas entre pestañas; el panel cambia al activarlas ({R("KYN-SDI-ARQ-008", "Identificación de controles")}).']),
            ('Acordeón', ['Secciones largas que se consultan por partes.', f'Elementos {c("details")} y {c("summary")}; varios abiertos; ninguno se abre solo.']),
            ('Panel lateral', ['Detalle de un elemento sin perder la lista.', 'Se cierra con Escape y devuelve el foco.']),
            ('Diálogo', [f'Una decisión que interrumpe la tarea ({R("KYN-SDI-CPE-010", "Diálogos")}).', 'Modal, con foco dentro.'])]),
    ], verif=[('Por contenedor', 'Se abre, se cierra y se recorre cada contenedor con teclado.', 'el foco vuelve al control que lo abrió.')], ver='tecnica',
       origen=['Contenedores con función (base)'], responsabilidad='Paneles, pestañas, acordeones y diálogos se usan cuando facilitan la tarea.', corto='Contenedores'),

    n14('KYN-SDI-CPE-009', 'Jerarquía estable', 2, 'Contenedores necesarios',
        'Se aplica al agrupar contenido en cajas, tarjetas o paneles: <strong>cada contenedor aporta orden</strong>.', [
        req(N('El contenido no debe fragmentarse en contenedores adicionales sin una razón funcional o informativa.', 'no-debe')),
        stack([('Regla', ['Una tarjeta solo cuando agrupa algo que se mueve, se selecciona o se lee como unidad.']),
               ('Anidamiento', ['Sin contenedores dentro de contenedores, salvo una tabla dentro de un panel.'])]),
    ], verif=[('Quitar un contenedor', 'Se quita un contenedor y una persona completa la tarea con su contenido.', 'la persona agrupa y encuentra la información igual que antes; en ese caso, el contenedor se elimina.')], ver='breve',
       origen=['Jerarquía estable (base)'], responsabilidad='El contenido no se fragmenta en contenedores sin razón.', corto='Jerarquía'),

    n14('KYN-SDI-CPE-010', 'Diálogos', 3, 'Propósito, acciones y salida de los diálogos',
        'Se aplica a todo diálogo que interrumpe la tarea: <strong>dice para qué es y cómo salir</strong>.', [
        req(N('Un diálogo que interrumpe la tarea debe presentar claramente su propósito, las acciones disponibles y la forma de salir.', 'debe')),
        matriz('Anatomía de un diálogo', [('Qué contiene', ''), ('Accesibilidad', '')], [
            ('Título', ['La decisión, en una frase.', 'Nombre del diálogo (aria-labelledby).']),
            ('Contenido', ['Lo necesario para decidir.', 'Descripción (aria-describedby).']),
            ('Acciones', ['Principal y Cancelar, con verbos.', 'Botones con nombre.']),
            ('Salida', ['Botón Cerrar y Escape.', 'El foco vuelve al control que lo abrió.'])]),
        detalle([
            ('Notas técnicas', [
                ('Modal', f'{c("<dialog>")} abierto con showModal(), o un panel con aria-modal y el fondo inerte. El foco entra al primer control, o a Cancelar si la acción es destructiva.')])]),
    ], verif=[('Ciclo', 'Se abre el diálogo, se recorre con Tab y se cierra con Escape.', 'el foco queda dentro mientras está abierto y vuelve al control que lo abrió.')], ver='tecnica',
       origen=['Diálogos (base)'], responsabilidad='Los diálogos presentan propósito, acciones y salida, con foco gestionado.', corto='Diálogos'),

    seccion('ejemplo', '14', 'Ejemplo de aplicación', 'Confirmar una eliminación',
            'Una confirmación de eliminación puede justificar un diálogo; <strong>una explicación secundaria no necesita interrumpir</strong> la pantalla.', [
        stack([('Verificación del capítulo', ['Se comprueba la comprensión, el foco y el retorno al contexto anterior.'])]),
    ]),
]

# ═════════════ 15 · Retroalimentación ═════════════
def n15(nid, nombre, k, *a, **kw): return norma(nid, nombre, '04.04', 'componentes-estados', 'retroalimentacion-y-superposiciones', k, *a, **kw)


CAP15 = [
    n15('KYN-SDI-CPE-011', 'Resultado visible', 1, 'Componentes de respuesta a una acción',
        'Desarrolla los componentes con que el sistema muestra el resultado o el proceso de una acción: <strong>lo hecho se ve hecho</strong>.', [
        req(N('Las acciones que modifican información deben comunicar su resultado o estado de procesamiento.', 'debe')),
        matriz('Componentes de respuesta', [('Cuándo', ''), ('Anuncio', '')], [
            ('En línea', ['Resultado junto al elemento: «Guardado».', 'role="status"']),
            ('Aviso breve', ['Confirmación que no bloquea, con Deshacer si aplica.', 'role="status"; se mantiene si tiene foco o cursor encima']),
            ('Banner', ['Estado que afecta a toda la pantalla.', 'role="status" o role="alert" si es urgente']),
            ('Progreso', ['Procesos largos: barra con porcentaje o pasos.', 'progressbar con su valor'])]),
    ], verif=[('Cuatro casos', 'Se prueban éxito, espera, fallo y repetición de la acción.', 'cada caso se ve y se anuncia con su componente.')], ver='grupo',
       origen=['Resultado visible (base)', 'UIX-027'], responsabilidad='Las acciones que modifican información comunican su resultado o su proceso.', corto='Resultado',
       cita='Desarrolla PEX-004 (01) en componentes'),

    n15('KYN-SDI-CPE-012', 'Mensajes pertinentes', 2, 'Mensajes que explican lo ocurrido',
        'Se aplica a todo mensaje de respuesta: <strong>dice lo que realmente pasó</strong>, con su objeto y su resultado.', [
        req(N('La retroalimentación debe explicar lo ocurrido sin utilizar mensajes genéricos que impidan comprender el estado real.', 'debe')),
        stack([('Concreto', ['«Cliente Ana Mora registrado» en lugar de «Éxito».']),
               ('Redacción', [f'Trato de usted, voz activa y palabras del perfil, según {L("24")}.'])]),
    ], verif=[('Mensajes', 'Se revisan los mensajes de respuesta del producto.', 'cada uno nombra el objeto y el resultado.')], ver='grupo',
       origen=['Mensajes pertinentes (base)'], responsabilidad='La retroalimentación explica el estado real, sin mensajes genéricos.', corto='Mensajes',
       cita='24 Mensajes define la redacción'),

    n15('KYN-SDI-CPE-013', 'Atención proporcionada', 3, 'Niveles de urgencia de las notificaciones',
        'Se aplica a avisos y notificaciones: <strong>cada uno pide la atención que merece</strong>.', [
        req(N('Las notificaciones deberían diferenciarse según urgencia y consecuencias, evitando interrumpir tareas por eventos menores.', 'deberia')),
        matriz('Niveles de urgencia (desde UIX-030 y UIX-046, unidas)', [('Qué es', ''), ('Cómo avisa', '')], [
            ('Bajo', ['Confirmaciones de rutina.', 'Cambio en el lugar o aviso breve.']),
            ('Medio', ['Algo que conviene revisar pronto.', 'Banner o contador en la navegación.']),
            ('Alto', ['Algo que pide acción hoy.', 'Banner persistente y notificación.']),
            ('Crítico', ['Riesgo o bloqueo inmediato.', 'Diálogo o alerta que interrumpe.'])]),
    ], verif=[('Escalada', 'Se revisa el nivel asignado a cada evento notificado.', 'cada nivel corresponde a la urgencia y la consecuencia del evento.')], ver='breve',
       origen=['Atención proporcionada (base)', 'UIX-030', 'UIX-046'], responsabilidad='Las notificaciones se diferencian por urgencia y no interrumpen por eventos menores.', corto='Atención'),

    seccion('ejemplo', '15', 'Ejemplo de aplicación', 'Después de guardar',
            'Después de guardar, la persona <strong>reconoce que el cambio se registró</strong>. Si falló, entiende qué debe hacer.', [
    ]),
    validacion('04.04', 'retroalimentacion-y-superposiciones', 'El capítulo se comprueba probando <strong>éxito, espera, fallo y repetición</strong> de las mismas acciones.'),
]

# ═════════════ 19 · Procesos críticos ═════════════
def n19(nid, nombre, k, *a, **kw): return norma(nid, nombre, '05.04', 'patrones-interaccion', 'decisiones-y-operaciones-sensibles', k, *a, **kw)


CAP19 = [
    n19('KYN-SDI-PAT-011', 'Autorización', 1, 'Autorización y confirmación de operaciones críticas',
        'Se aplica a las operaciones de alto riesgo: <strong>se comprueba quién puede hacerlas</strong> y se pide la confirmación que corresponde.', [
        req(N('El sistema debe comprobar los permisos y las confirmaciones correspondientes al riesgo de la acción.', 'debe')),
        stack([('Consecuencias', ['Antes de ejecutar, la interfaz muestra qué va a cambiar y en cuántos elementos.']),
               ('Confirmación', [f'Su nivel lo define {R("KYN-SDI-CPE-003")}: deshacer, confirmar o confirmar con refuerzo.']),
               ('Intervención humana', [f'Las acciones automatizadas de riesgo piden aprobación según {L("32")}.'])]),
    ], rel=['KYN-SDI-PEX-006'], verif=[('Cuatro casos', 'Se prueban la ejecución autorizada, el permiso insuficiente, la cancelación y el fallo.', 'cada caso termina como describe la norma, sin ejecutar nada sin autorización.')], ver='tecnica',
       origen=['Autorización (base)', 'Consecuencias claras (base; integrada en PEX-006)', 'UIX-014'],
       responsabilidad='Las operaciones críticas comprueban permisos y piden la confirmación que corresponde al riesgo.', corto='Autorización'),

    n19('KYN-SDI-PAT-012', 'Trazabilidad', 2, 'Registro de operaciones críticas',
        'Se aplica a las operaciones críticas: <strong>queda registro de qué ocurrió y bajo qué autorización</strong>.', [
        req(N('Las operaciones críticas deben permitir reconstruir qué ocurrió y bajo qué autorización, según los requisitos de seguridad y auditoría del producto.', 'debe')),
        matriz('Qué se registra', [('Dato', ''), ('Para qué', '')], [
            ('Quién', ['Persona o agente y su rol.', 'Responsabilidad.']),
            ('Qué y cuándo', ['La operación, el objeto y la hora.', 'Reconstrucción.']),
            ('Bajo qué autorización', ['El permiso o la aprobación usada.', 'Auditoría.']),
            ('Resultado', ['Éxito, fallo o reversión.', 'Seguimiento.'])]),
    ], verif=[('Reconstrucción', 'Se reconstruye una operación crítica desde su registro.', 'se sabe qué ocurrió, quién lo autorizó y cuándo, sin preguntar a nadie.')], ver='breve',
       origen=['Trazabilidad (base)'], responsabilidad='Las operaciones críticas quedan registradas con su autorización.', corto='Trazabilidad'),

    seccion('ejemplo', '19', 'Ejemplo de aplicación', 'Anular un pago',
            'Anular un pago <strong>muestra el monto y a quién afecta</strong>, pide la autorización del rol y deja su registro.', [
        stack([('Verificación del capítulo', ['Probar ejecución autorizada, permisos insuficientes, cancelación y fallos.'])]),
    ]),
]

CAPITULOS = [
    ('03', '03.05', 'recursos-visuales-de-interfaz', CAP11, None),
    ('04', '04.03', 'componentes-de-estructura', CAP14, None),
    ('04', '04.04', 'retroalimentacion-y-superposiciones', CAP15, None),
    ('05', '05.04', 'decisiones-y-operaciones-sensibles', CAP19, None),
]
