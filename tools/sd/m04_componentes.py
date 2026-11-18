"""Módulo 04 · Componentes (CPE): 12 Acciones y 13 Entradas (Bloque 3). 14 y 15 van en el Bloque 4.
Requisitos: textos de Keylin (docs/sd/fuente-keylin-2026-11-17.md). CPE-004 (menú de acciones) lleva un requisito redactado por
Claude a partir de la descripción del capítulo y requiere aprobación. Componentes: propósito, anatomía, variantes, estados,
comportamiento, accesibilidad y pruebas, en texto y tablas (sin maquetas hasta la hoja de componentes aprobada).
"""
from .base import N, req, stack, matriz, detalle, c, L, M, norma, seccion, R, validacion, dims

MOD = 'componentes-estados'
C12, C13 = 'componentes-de-accion', 'controles-de-entrada'
def n12(nid, nombre, k, *a, **kw): return norma(nid, nombre, '04.01', MOD, C12, k, *a, **kw)
def n13(nid, nombre, k, *a, **kw): return norma(nid, nombre, '04.02', MOD, C13, k, *a, **kw)


# ═════════════ 12 · Acciones ═════════════
CAP12 = [
    n12('KYN-SDI-CPE-001', 'Jerarquía de acciones', 1, 'Acción principal, secundaria y destructiva',
        'Se aplica a todo grupo de botones que resuelve una decisión: <strong>la jerarquía dice qué hacer primero</strong>.', [
        req(N('Las acciones principales y secundarias deben distinguirse de forma consistente dentro de cada grupo de decisión.', 'debe')),
        matriz('Variantes de botón', [('Cuándo', ''), ('Cuántas', 'Por grupo de decisión')], [
            ('Principal', ['La acción que completa la tarea: Guardar, Enviar, Aprobar.', 'Una.']),
            ('Secundaria', ['Alternativas de la misma decisión: Cancelar, Guardar borrador.', 'Las necesarias.']),
            ('De texto', ['Acciones menores o de navegación: Ver detalle, Editar.', 'Las necesarias.']),
            ('Destructiva', [f'Eliminar, revocar, cerrar una cuenta.', 'La que corresponda; nunca con el aspecto de la principal.'])]),
        stack([('Anatomía', ['Etiqueta con verbo y objeto («Guardar cambios»), ícono opcional y área de toque suficiente. El ícono va a la izquierda; a la derecha, solo si indica dirección.']),
               ('Botón o enlace', ['Un botón ejecuta una acción y un enlace lleva a otro lugar, en todas las pantallas.']),
               ('Apariencia', [f'Los colores de la principal siguen {M("KYN-MRK-COL-015")}; los radios, {c("--r-control")} o {c("--r-pill")}.'])]),
        detalle([
            ('Orden en un grupo', [
                ('Escritorio', 'La principal, al final del grupo, a la derecha; las secundarias, a su izquierda.'),
                ('Móvil', 'La principal ocupa el ancho y va primero, arriba de las secundarias.')])]),
    ], rel=['KYN-SDI-CPE-003', 'KYN-SDI-ARQ-006'], verif=[('Grupo', 'Se revisa cada grupo de decisión de una pantalla.', 'hay una sola acción principal por grupo.'), ('Comparación', 'Se ven Guardar, Cancelar y Eliminar en escala de grises.', 'las tres se distinguen a simple vista.')], ver='breve',
       origen=['Jerarquía (base)', 'Variantes y jerarquía (matriz)'], responsabilidad='Las acciones principales, secundarias y destructivas se distinguen con consistencia.',
       corto='Jerarquía'),

    n12('KYN-SDI-CPE-002', 'Estados de los controles', 2, 'Estados de los controles interactivos',
        'Se aplica a botones, enlaces y controles de acción: <strong>cada estado se ve y se anuncia</strong> antes de que la persona pregunte.', [
        req(N('Los controles interactivos deben contemplar los estados aplicables: normal, hover cuando corresponda, foco, activación, carga y deshabilitado.', 'debe')),
        matriz('Estados de un botón', [('Cómo se ve', ''), ('Cómo se comporta', '')], [
            ('Reposo', ['Su variante.', 'Responde al puntero, al toque y al teclado.']),
            ('Cursor encima', ['Cambio de fondo o de subrayado.', 'Solo con puntero; en pantallas táctiles no existe.']),
            ('Foco', [f'Anillo de 2 px en Azul Noche, separado del borde.', 'Solo al llegar con el teclado (:focus-visible).']),
            ('Presionado', ['Leve cambio de tono.', 'Mientras se mantiene presionado.']),
            ('Cargando', ['Indicador dentro del botón; la etiqueta conserva su ancho.', 'Ignora nuevos clics; anuncia «procesando» con aria-busy.']),
            ('Deshabilitado', ['Texto y fondo atenuados.', 'Explica cerca por qué no está disponible.']),
            ('Activado', ['Señal de forma y color (por ejemplo, Favorito).', f'Anuncia su estado con {c("aria-pressed")}.'])]),
        detalle([
            ('Notas técnicas', [
                ('Teclado', f'Un {c("<button>")} se activa con Enter y con Espacio; un enlace, con Enter.'),
                ('Deshabilitado', f'Si la persona necesita saber por qué no puede usarlo, se prefiere {c("aria-disabled")} a {c("disabled")}: el control sigue recibiendo el foco y su explicación se lee.'),
                ('Doble envío', 'Un segundo clic durante la carga no repite la acción.')])]),
    ], rel=['SD-21'], verif=[('Cuatro formas', 'Se activa cada variante con puntero, toque, Enter y Espacio.', 'responde igual por las cuatro vías.'), ('Carga', 'Se hace doble clic durante la carga.', 'la acción se ejecuta una sola vez.'), ('Lector de pantalla', 'Se recorre cada control con NVDA o VoiceOver.', 'se anuncian el nombre, el estado activado y la carga.')], ver='tecnica',
       origen=['Estados (base)', 'Activación, foco, carga y deshabilitación (matriz)', 'Propuesta P5 de las UIX (siete estados)'],
       responsabilidad='Los controles contemplan reposo, cursor encima, foco, presionado, carga, deshabilitado y activado.', corto='Estados'),

    n12('KYN-SDI-CPE-003', 'Acciones destructivas', 3, 'Protección de las acciones destructivas',
        'Se aplica a eliminar, revocar, cerrar y toda acción de alto impacto: <strong>la protección crece con el riesgo</strong>.', [
        req(N('Las acciones de alto impacto deben comunicar sus consecuencias y aplicar la protección correspondiente a su riesgo.', 'debe')),
        matriz('Protección según el riesgo', [('Protección', ''), ('Ejemplo', '')], [
            ('Reversible', ['Se ejecuta y ofrece Deshacer.', 'Archivar una solicitud.']),
            ('Irreversible', ['Confirmación en un diálogo que nombra el objeto y la consecuencia.', '«Eliminar la factura 2026-118. Esta acción no se puede deshacer.»']),
            ('Irreversible y crítica', [f'Confirmación reforzada: escribir el nombre del objeto o una autorización adicional.', 'Cerrar una cuenta con datos de clientes.'])]),
        stack([('Etiqueta', ['El botón nombra la consecuencia: «Eliminar 3 facturas», no «Aceptar».']),
               ('Diálogo de confirmación', ['El botón de confirmar repite el verbo; el foco inicial va a Cancelar.'])]),
    ], rel=['SD-19'], verif=[('Prueba de riesgo', 'Se intenta cada acción destructiva del producto.', 'la protección corresponde a su fila de la tabla y el texto nombra lo que se pierde.')], ver='breve',
       origen=['Acciones destructivas (base)', 'UIX-025'], responsabilidad='Las acciones de alto impacto comunican consecuencias y aplican protección según el riesgo.',
       corto='Destructivas'),

    n12('KYN-SDI-CPE-004', 'Menú de acciones', 4, 'Menú de acciones ocasionales',
        'Se aplica cuando un elemento tiene más acciones de las que caben o conviene mostrar: <strong>lo ocasional se agrupa sin esconder lo necesario</strong>.', [
        dims([('Qué va en el menú', [N('Las acciones secundarias de un elemento pueden agruparse en un menú cuando son ocasionales o no caben.', 'puede'),
                                     f'La acción frecuente o principal queda visible.']),
              ('Botón', [N('El botón que abre el menú debe nombrar su función.', 'debe'),
                         f'Lleva el ícono de más opciones y un nombre accesible con su objeto: «Más acciones para la factura 2026-118», con {c("aria-haspopup")} y {c("aria-expanded")}.'])]),
        detalle([
            ('Teclado', [
                ('Abrir', 'Enter, Espacio o flecha abajo abren el menú y el foco pasa a la primera opción.'),
                ('Recorrer', 'Las flechas recorren las opciones; Inicio y Fin van a la primera y a la última.'),
                ('Cerrar', 'Escape cierra el menú y el foco vuelve al botón. Elegir una opción lo cierra y ejecuta la acción.')])]),
    ], rel=['KYN-SDI-ARQ-007'], verif=[('Teclado', 'Se abre el menú, se recorre y se cierra solo con teclado.', 'el foco sigue el recorrido descrito y vuelve al botón al cerrar.'), ('Lector de pantalla', 'Se abre el menú con NVDA o VoiceOver.', 'se anuncian el menú, su estado y cada opción.')], ver='tecnica',
       origen=['Menús (descripción del capítulo; requisito redactado por Claude)'], responsabilidad='Las acciones ocasionales se agrupan en un menú accesible.',
       corto='Menú de acciones'),

    seccion('ejemplo', '12', 'Ejemplo de aplicación', 'Guardar, cancelar y eliminar',
            'Guardar, cancelar y eliminar <strong>no comparten una jerarquía visual</strong> que pueda inducir confusión.', [
        stack([('En el formulario', ['«Guardar cambios» es la principal; «Cancelar», secundaria; «Eliminar registro» va aparte, como destructiva.']),
               ('Verificación del capítulo', ['Se comprueban todas las variantes con teclado, puntero, pantalla táctil y estados de procesamiento.'])]),
    ]),
]

# ═════════════ 13 · Entradas ═════════════
CAP13 = [
    n13('KYN-SDI-CPE-005', 'Etiquetas identificables', 1, 'Etiqueta, ayuda y error de cada campo',
        'Se aplica a todo campo de entrada: <strong>la etiqueta dice qué pide</strong> y sigue visible al escribir.', [
        req(N('Cada campo debe tener una etiqueta que explique qué información solicita, independientemente del texto de ejemplo.', 'debe')),
        matriz('Anatomía de un campo', [('Qué es', ''), ('Cuándo', '')], [
            ('Etiqueta', ['Nombre del dato, visible arriba del campo.', 'Siempre.']),
            ('Ayuda o formato', ['Formato esperado o aclaración breve.', 'Cuando el dato tiene formato o reglas: «DD/MM/AAAA».']),
            ('Campo', ['El control de entrada.', 'Siempre.']),
            ('Mensaje de error', [f'Qué falta y cómo corregirlo.', 'Cuando el valor no es válido.']),
            ('Contador', ['Caracteres usados y límite.', 'Cuando hay un límite de longitud.'])]),
        stack([('Obligatorio u opcional', ['Se marca lo que es menos frecuente en el formulario: si casi todo es obligatorio, se marca «(opcional)».']),
               ('Texto de ejemplo', ['Muestra un valor posible; nunca reemplaza a la etiqueta ni a la ayuda.'])]),
        detalle([
            ('Notas técnicas', [
                ('Asociación', f'{c("<label for>")} une etiqueta y campo; {c("aria-describedby")} une la ayuda y el error.'),
                ('Autocompletado', f'Los datos personales llevan su {c("autocomplete")} correcto: nombre, correo, teléfono, dirección.')])]),
    ], rel=['KYN-SDI-CPE-006'], verif=[('Lector de pantalla', 'Se entra en cada campo con un lector de pantalla.', 'se anuncian la etiqueta, la ayuda y, si existe, el error.'), ('Campo con valor', 'Se completa cada campo.', 'la etiqueta sigue visible.')], ver='grupo',
       origen=['Etiquetas identificables (base)', 'Etiqueta y formato esperado (matriz)'], responsabilidad='Cada campo tiene etiqueta visible, ayuda cuando hace falta y asociaciones accesibles.',
       corto='Etiquetas'),

    n13('KYN-SDI-CPE-006', 'Validación útil', 2, 'Mensajes de error en los campos',
        'Se aplica a los errores de entrada: <strong>cada error dice dónde está y cómo corregirlo</strong>, en el momento adecuado.', [
        req(N('Los errores de entrada deben identificar el campo afectado y explicar cómo corregir la información.', 'debe')),
        matriz('Cuándo se valida', [('Qué pasa', ''), ('Por qué', '')], [
            ('Mientras escribe por primera vez', ['Sin mensajes de error.', 'La persona todavía no terminó.']),
            ('Al salir del campo', ['Se valida el formato y se muestra el error si corresponde.', 'Aviso temprano sin interrumpir.']),
            ('Al enviar', ['Se validan todos; el foco va al primer error y, si hay varios, aparece un resumen arriba.', 'Nada queda sin ver.']),
            ('Al corregir', ['El error desaparece en cuanto el valor es válido.', 'La persona ve que lo resolvió.'])]),
        detalle([
            ('Notas técnicas', [
                ('Estado', f'El campo con error lleva {c("aria-invalid")} y su mensaje unido con {c("aria-describedby")}.'),
                ('Resumen', f'El resumen de errores se anuncia ({c("role=" + chr(34) + "alert" + chr(34))}) y cada error enlaza a su campo.'),
                ('Redacción', f'Qué pasó y qué hacer: «Ingrese un correo con @».')])]),
    ], rel=['SD-24'], verif=[('Cuatro casos', 'Se prueban campos vacíos, valores incorrectos, entradas largas y la corrección de cada error.', 'cada error nombra el campo y la corrección, y desaparece al corregirse.')], ver='grupo',
       origen=['Validación útil (base)', 'Comportamiento de validación y recuperación (matriz)'], responsabilidad='Los errores identifican el campo y explican cómo corregir, en el momento adecuado.',
       corto='Validación'),

    n13('KYN-SDI-CPE-007', 'Control apropiado', 3, 'Control según el tipo de dato',
        'Define qué control usa cada dato: <strong>el que pide menos esfuerzo y evita errores</strong>.', [
        req(N('La selección de un control debería responder al tipo de dato y al esfuerzo que requiere introducirlo.', 'deberia')),
        matriz('Qué control usar', [('Control', ''), ('Notas', '')], [
            ('Una opción entre pocas', ['Botones de opción, todos visibles.', 'Se ven las opciones sin abrir nada.']),
            ('Una opción entre muchas', ['Lista desplegable o cuadro combinado con búsqueda.', 'Búsqueda cuando la lista es larga.']),
            ('Varias opciones', ['Casillas.', 'Cada una con su etiqueta.']),
            ('Activar con efecto inmediato', ['Interruptor.', 'El cambio ocurre al tocarlo, sin Guardar.']),
            ('Fecha', ['Campo con formato visible y selector opcional.', 'Se puede escribir o elegir.']),
            ('Número con unidad', ['Campo numérico con la unidad visible.', 'Teclado numérico en móvil.']),
            ('Archivo', ['Selector de archivo, con arrastrar opcional.', 'Tipos y tamaño máximo visibles.'])]),
        detalle([
            ('Estados del campo', [
                ('Reposo y foco', 'El foco cambia el borde del campo, sin anillo adicional (reglas-visuales 4.5).'),
                ('Lleno, error y deshabilitado', 'Con valor; con borde, ícono y mensaje de error; atenuado y sin respuesta.'),
                ('Solo lectura', 'El valor se lee y se puede copiar, sin aspecto de campo editable.')])]),
    ], verif=[('Tipos de dato', 'Se revisa el control de cada campo del formulario contra la tabla.', 'coincide con la tabla o tiene una razón registrada.')], ver='grupo',
       origen=['Control apropiado (base)', 'Campos, selectores, casillas, interruptores, fechas y archivos (descripción del capítulo)'],
       responsabilidad='Cada dato usa el control que corresponde a su tipo y esfuerzo.', corto='Control apropiado'),

    seccion('ejemplo', '13', 'Ejemplo de aplicación', 'Una fecha',
            'Una fecha se presenta con <strong>un formato comprensible</strong> y permite introducir valores válidos sin generar ambigüedad.', [
        stack([('Campo', ['Etiqueta «Fecha de ingreso», ayuda «DD/MM/AAAA» y selector de calendario opcional.'])]),
    ]),
    validacion('04.02', C13, 'El capítulo se comprueba con <strong>campos vacíos, valores incorrectos, entradas largas, lectores de pantalla y teclado</strong>, en el mismo formulario.'),
]

CAPITULOS = [
    ('04', '04.01', C12, CAP12, None),
    ('04', '04.02', C13, CAP13, None),
]
