"""Módulo 02 · Arquitectura (ARQ), capítulos 04 Información y 06 Búsqueda (el 05 Navegación está en m02_arquitectura.py).
Requisitos: textos de Keylin (base y ampliación, 2026-11-17). Titulares, entradas, decisiones, comportamientos, excepciones y
verificaciones: propuesta de Claude en borrador. Las «Ampliaciones necesarias» de su matriz se integran en las normas existentes.
Composición: Guía 05 «Composición normativa según el contenido».
"""
from .base import N, req, stack, dims, matriz, contraste, detalle, sub, L, R, norma, seccion, validacion

MOD = 'arquitectura-navegacion'

# ═════════════ 04 · Información ═════════════
C4 = 'arquitectura-de-informacion'
def n4(nid, nombre, k, *a, **kw): return norma(nid, nombre, '02.01', MOD, C4, k, *a, **kw)


CAP04 = [
    n4('KYN-SDI-ARQ-001', 'Organización comprensible', 1, 'Agrupación del contenido por tareas',
       'Define cómo se agrupa el contenido de un producto: <strong>según las tareas y los conceptos de las personas</strong>, y no según la estructura interna de la empresa.', [
        dims([('Agrupación', [N('El contenido debe agruparse según la relación entre tareas, conceptos y necesidades de las personas, no exclusivamente según la estructura interna de la empresa.', 'debe'),
                              f'Se decide con las tareas y el vocabulario de los perfiles. Cuando la estructura es nueva, se prueba con un ordenamiento de tarjetas o una prueba de árbol.']),
              ('Relaciones', [N('Las agrupaciones de información deben responder a relaciones funcionales o conceptuales identificables.', 'debe'),
                              'Cada página tiene un objeto principal y sus grupos, nombrados por su contenido. Desde un elemento se llega a lo relacionado sin volver al menú: del cliente a sus facturas, de la factura a su pago.'])]),
    ], origen=['Organización comprensible (base)', 'Agrupación con sentido (ampliación)', 'Estructura de páginas, agrupación y navegación contextual (ampliación de la matriz)'],
       responsabilidad='El contenido se agrupa por tareas y conceptos de las personas, con relaciones identificables.',
       rel=['KYN-SDI-PEX-007', 'KYN-SDI-GOB-001'], verif=[('Prueba de árbol', 'Personas de cada perfil buscan cinco elementos frecuentes en la estructura, sin la interfaz. El umbral de éxito se fija antes de la prueba.',
               'encuentran los elementos sin conocer cómo está organizada la base de datos.')], ver='grupo'),

    n4('KYN-SDI-ARQ-002', 'Nombres comprensibles', 2, 'Nombres reconocibles para secciones y destinos',
       'Se aplica al nombrar menús, categorías, secciones y funciones: <strong>cada nombre usa el vocabulario de quien trabaja con el producto</strong>.', [
        req(N('Las categorías, secciones y elementos de navegación deben utilizar denominaciones que las personas puedan reconocer según su contexto de trabajo.', 'debe')),
        stack([('Vocabulario', ['Los nombres salen de las palabras que los perfiles usan en su trabajo, recogidas en entrevistas, documentos y solicitudes reales. El vocabulario del código o de la base de datos queda fuera de la interfaz.']),
               ('Etiqueta y título', ['La etiqueta del menú es corta y nombra el destino. El título de la página puede precisarlo sin cambiar su sentido: menú «Solicitudes» y título «Solicitudes pendientes».']),
               ('Siglas', ['Solo las que el perfil usa a diario. Las demás se escriben completas, y una sigla nueva aparece completa la primera vez.']),
               ('Un concepto, un nombre', ['El mismo concepto conserva su nombre en el menú, los títulos, los botones y los mensajes de todo el producto.'])]),
        sub('Ejemplos'),
        contraste([('Entidades', 'Clientes'), ('Módulo de gestión de tickets', 'Solicitudes'), ('Config.', 'Configuración')]),
    ], origen=['Nombres comprensibles (ampliación)', 'Nombres de categorías (ampliación de la matriz)', 'UIX-041'],
       responsabilidad='Categorías, secciones y destinos usan nombres que las personas reconocen.',
       cita='23 Escritura (Consistencia) desarrolla la redacción', rel=['KYN-SDI-CNT-002'],
       verif=[('Comprensión', 'Se muestra cada nombre de sección sin contexto y se pide decir qué se espera encontrar.', 'lo que la persona espera coincide con el contenido de la sección.'),
              ('Tarea real', 'Se pide completar una tarea real eligiendo su destino en el menú.', 'la persona elige el destino correcto al primer intento.')], ver='grupo'),
    n4('KYN-SDI-ARQ-003', 'Jerarquía identificable', 3, 'Información principal, secundaria y complementaria',
       'Se aplica a cada página: <strong>tres niveles de información con un lugar y un peso propios</strong>.', [
        req(N('Las páginas deben diferenciar información principal, secundaria y complementaria mediante una jerarquía consistente.', 'debe')),
        matriz('Tres niveles de información', [('Qué contiene', ''), ('Dónde va', '')], [
            ('Principal', ['Lo que identifica el objeto y permite la tarea.', 'Título, datos clave y acción principal, arriba y con mayor peso.']),
            ('Secundaria', ['Lo que amplía o permite tareas frecuentes relacionadas.', 'Grupos rotulados, debajo o al lado.']),
            ('Complementaria', ['Historial, auditoría y configuración.', f'A pedido: pestañas, acordeones o enlaces.'])]),
    ], origen=['Jerarquía identificable (base)', 'Jerarquías (ampliación de la matriz)'],
       responsabilidad='Las páginas distinguen información principal, secundaria y complementaria.',
       cita='09 Tipografía define la jerarquía visual',
       rel=['KYN-SDI-ARQ-004', 'KYN-SDI-FUI-009'], verif=[('Tres datos', 'Se pide a la persona que nombre los tres datos más importantes de la pantalla.', 'coinciden con la información principal definida y son lo primero que destaca la jerarquía visual.')]),

    n4('KYN-SDI-ARQ-004', 'Información progresiva', 4, 'Información esencial y detalle progresivo',
       'Decide qué se ve al abrir una pantalla y qué se abre a pedido: <strong>lo necesario para la siguiente acción está siempre disponible</strong>.', [
        dims([('Información necesaria', [N('La información necesaria para decidir o ejecutar la siguiente acción debe permanecer disponible en el momento correspondiente.', 'debe'),
                                         'Requisitos, consecuencias, errores y datos obligatorios están a la vista en el paso que los necesita.']),
              ('Detalle a pedido', [N('Los detalles especializados pueden presentarse progresivamente cuando su presencia inicial aumente innecesariamente la complejidad.', 'puede'),
                                    f'Se revelan con pestañas, acordeones, paneles o enlaces, según {R("KYN-SDI-CPE-008")}; el control dice qué contiene. Al abrir un detalle, la persona sigue viendo de qué elemento es.']),
              ('Ejemplo', ['En una factura, el total, el estado y el vencimiento se ven siempre. El desglose de impuestos y el historial de pagos se abren a pedido.'])]),
    ], origen=['Información progresiva (base)', 'Detalle progresivo (ampliación)', 'Información esencial visible (ampliación)', 'Revelación progresiva (ampliación de la matriz)', 'UIX-028'],
       responsabilidad='Lo esencial está visible en su momento; el detalle se ofrece a pedido sin ocultar requisitos.',
       verif=[('Siguiente acción', 'Se recorre cada paso de una tarea.', 'la persona decide sin abrir detalles para buscar un dato necesario.'),
              ('Detalle', 'Se busca cada detalle oculto desde el control que lo anuncia.', 'se encuentra sin perder la tarea.')]),

    seccion('ejemplo', '04', 'Ejemplo de aplicación', 'Un expediente',
            'Un expediente muestra primero <strong>los datos necesarios para identificarlo y trabajar</strong>; los registros históricos permanecen accesibles sin competir con la tarea principal.', [
        stack([('Principal', ['Nombre, número, estado y la acción «Actualizar».']),
               ('Complementaria', ['Historial y auditoría, en una pestaña.'])]),
    ]),
    validacion('02.01', C4, 'El capítulo se comprueba cuando <strong>las personas encuentran información importante sin tener que conocer cómo está organizada internamente la base de datos</strong>. '
               'La prueba de árbol y la de nombres se hacen en la misma sesión, antes de diseñar la interfaz.'),
]

# ═════════════ 06 · Búsqueda ═════════════
C6 = 'busqueda-y-orientacion'
def n6(nid, nombre, k, *a, **kw): return norma(nid, nombre, '02.03', MOD, C6, k, *a, **kw)


CAP06 = [
    n6('KYN-SDI-ARQ-011', 'Alcance identificable', 1, 'Alcance de la búsqueda',
       'Se aplica a toda búsqueda: <strong>la persona sabe si busca en todo el producto o en una parte</strong>.', [
        req(N('Cuando una búsqueda está limitada a una sección, categoría o conjunto de datos, su alcance debe resultar comprensible.', 'debe')),
        stack([('Global o local', ['La búsqueda global vive en la cabecera; la local, junto a la lista que filtra, con un texto que nombra su alcance: «Buscar en solicitudes».']),
               ('Cambio de alcance', ['Desde una búsqueda local sin resultados se ofrece buscar en todo el producto.'])]),
    ], origen=['Alcance identificable (ampliación)', 'Búsqueda global frente a local (ampliación de la matriz)'],
       responsabilidad='Se entiende si la búsqueda es global o está limitada a una sección o conjunto.',
       verif=[('Dos búsquedas', 'Se muestran una búsqueda global y una local, sin escribir nada.', 'la persona distingue cuál busca en todo el producto y cuál dentro de la lista.')]),

    n6('KYN-SDI-ARQ-012', 'Resultados pertinentes', 2, 'Campos, coincidencias y orden de la búsqueda',
       'Define qué datos consulta la búsqueda, cómo compara lo que se escribe y en qué orden presenta lo encontrado: <strong>cada producto configura estos criterios según sus tareas y permisos</strong>.', [
        req(N('La búsqueda debe utilizar los campos y contenidos relevantes para la tarea, respetando los permisos de acceso.', 'debe')),
        stack([('Campos consultables', ['Los que el perfil usa para reconocer un registro: nombre, código, identificación y los datos propios de la tarea. Cada producto define la lista, y la búsqueda consulta solo lo que el perfil puede ver.']),
               ('Coincidencias', ['La exacta y la parcial cuentan: una parte del nombre encuentra el registro completo.']),
               ('Tildes, mayúsculas e identificadores', ['Las tildes y las mayúsculas se ignoran. Un identificador se compara sin espacios, guiones ni puntos, y así «001-234» y «001234» encuentran el mismo registro.']),
               ('Orden', ['Cada producto define sus criterios y los documenta: coincidencia exacta, uso reciente, frecuencia o fecha. Una tarea de consulta suele empezar por la coincidencia exacta; una bandeja de trabajo, por lo más reciente.']),
               ('Buscar, filtrar y ordenar', ['Buscar encuentra registros por lo que se escribe. Filtrar reduce el conjunto con criterios conocidos, como el estado o la fecha. Ordenar cambia la secuencia sin quitar registros, y cada uno se muestra por separado.'])]),
        detalle([
            ('Autocompletado', [
                ('Cuándo', 'En listas conocidas: clientes, productos, direcciones.'),
                ('Comportamiento', f'Las sugerencias aparecen al escribir; las flechas las recorren, Enter elige y Escape cierra. Sigue el patrón de cuadro combinado de {L("13")}.')]),
            ('Errores de escritura', [
                ('Sugerencia', 'Cuando el producto lo permite, se ofrece la forma correcta: «¿Quiso decir…?».')])]),
    ], origen=['Resultados pertinentes (base)', 'Autocompletado, búsqueda parcial, errores ortográficos y resultados ordenados (ampliación de la matriz)'],
       responsabilidad='La búsqueda usa los campos relevantes, encuentra por coincidencia parcial y ordena según los criterios de cada producto.',
       cita='El límite de permisos está en ARQ-016', rel=['KYN-SDI-ARQ-016'],
       verif=[('Consultas reales', 'Se buscan registros con nombre parcial, sin tildes, con un identificador escrito de otra forma y con un error de escritura.', 'el registro buscado aparece entre los primeros resultados.')], ver='grupo'),
    n6('KYN-SDI-ARQ-013', 'Resultados comprensibles', 3, 'Datos que distinguen cada resultado',
       'Se aplica a cada resultado de búsqueda: <strong>se elige el correcto sin abrirlo</strong>.', [
        req(N('Cada resultado debe proporcionar información suficiente para distinguirlo de otros elementos similares.', 'debe')),
        stack([('Datos del resultado', ['Nombre, tipo y uno o dos datos que lo diferencian, como código, fecha o unidad.']),
               ('Coincidencia', ['El término buscado se resalta en el resultado.']),
               ('Muchos resultados', [f'Se indica el total y se pagina o se carga por partes; los filtros reducen la lista.'])]),
    ], origen=['Resultados comprensibles (base)', 'Manejo de resultados extensos (ampliación de la matriz)'],
       responsabilidad='Cada resultado se distingue de otros similares y los resultados extensos se pueden recorrer.',
       rel=['KYN-SDI-DAV-002'], verif=[('Nombres parecidos', 'Se buscan dos registros con nombres casi iguales.', 'la persona elige el correcto sin abrirlos.')], ver='grupo'),

    n6('KYN-SDI-ARQ-014', 'Filtros visibles', 4, 'Filtros activos a la vista',
       'Se aplica a toda lista filtrada: <strong>se ve qué la está filtrando</strong> y cada filtro se cambia sin perder la consulta.', [
        req(N('Los filtros activos deben poder identificarse y modificarse sin perder innecesariamente la consulta.', 'debe')),
        stack([('Filtros activos', ['Se muestran como etiquetas que se quitan una a una, con «Quitar filtros» para todos.']),
               ('Combinación', ['Los filtros se combinan sin borrar la consulta escrita.']),
               ('Al volver', [f'La consulta, los filtros y la posición en la lista se conservan, como en el {R("KYN-SDI-ARQ-010", "regreso sin pérdida")} de la navegación.'])]),
    ], origen=['Filtros visibles (ampliación)', 'Conservación de filtros (ampliación de la matriz)'],
       responsabilidad='Los filtros activos se ven y se modifican sin perder la consulta.',
       cita='La conservación al volver la regula ARQ-010 (05)',
       verif=[('Aplicar y quitar', 'Se aplican, combinan y quitan filtros sobre una consulta escrita.', 'la consulta se mantiene y cada filtro activo se ve.')], ver='grupo'),

    n6('KYN-SDI-ARQ-015', 'Sin resultados', 5, 'Búsquedas sin resultados',
       'Se aplica cuando una búsqueda vuelve vacía: <strong>la interfaz explica por qué y ofrece cómo seguir</strong>.', [
        req(N('Cuando no existen coincidencias, la interfaz debe explicar la situación y ofrecer una acción útil, como modificar la consulta o retirar filtros.', 'debe'),
            N('La interfaz debe distinguir entre una búsqueda sin coincidencias y un error que impidió realizar la consulta.', 'debe')),
        matriz('Tres situaciones sin resultados', [('Qué se dice', ''), ('Cómo sigue', '')], [
            ('Sin coincidencias', ['Que no hay resultados para esa consulta y esos filtros.', 'Revisar el término, quitar filtros o buscar en todo el producto.']),
            ('Error de consulta', ['Que la búsqueda no se pudo realizar.', f'Reintentar; si persiste, una ruta alternativa.']),
            ('Sin acceso al alcance', [f'Que no tiene acceso a ese conjunto, sin revelar su contenido.', 'Cambiar de alcance o solicitar acceso, si el producto lo prevé.'])]),
    ], origen=['Sin resultados (base)', 'Ausencia de resultados (ampliación)', 'UIX-026', 'UIX-023'],
       responsabilidad='Sin coincidencias, la interfaz lo explica y ofrece una acción; un error y la falta de acceso se distinguen.',
       cita='24 Mensajes define la redacción',
       rel=['KYN-SDI-ARQ-016', 'KYN-SDI-PAT-007', 'KYN-SDI-CNT-004'], verif=[('Tres casos', 'Se fuerza cada situación de la tabla.', 'tres mensajes distintos, cada uno con lo que pasó y su salida.')], ver='grupo'),

    n6('KYN-SDI-ARQ-016', 'Resultados autorizados', 6, 'Resultados según permisos',
       'Se aplica a resultados, totales, sugerencias y fragmentos: <strong>la búsqueda muestra solo lo que la persona puede consultar</strong>.', [
        req(N('La búsqueda no debe revelar información que la persona carece de permiso para consultar, ni mediante resultados, cantidades, sugerencias o fragmentos de contenido.', 'no-debe')),
        stack([('Dónde se filtra', ['En el servidor, antes de contar, sugerir o resaltar.']),
               ('Totales y sugerencias', ['Se calculan sobre lo autorizado.']),
               ('Registros con partes restringidas', ['El resultado muestra solo los campos permitidos.'])]),
    ], origen=['Resultados autorizados (ampliación)'],
       responsabilidad='La búsqueda no revela, por ninguna vía, información sin permiso.',
       cita='Aplica PEX-008 a la búsqueda',
       verif=[('Perfiles distintos', 'Se repiten las mismas consultas con perfiles de distinto permiso y se revisan las respuestas del servidor.',
               'resultados, totales, sugerencias y fragmentos cambian según el permiso, y ninguna respuesta incluye datos no autorizados.')], ver='tecnica'),

    seccion('ejemplo', '06', 'Ejemplo de aplicación', 'Residentes con nombres parecidos',
            'Una búsqueda de residentes diferencia personas con nombres similares <strong>mediante datos identificativos permitidos</strong>.', [
        stack([('Resultado', ['«Ana Mora · Casa 12 · desde 2021» y «Ana Mora · Casa 40 · desde 2024».'])]),
    ]),
    validacion('02.03', C6, 'El capítulo se comprueba con <strong>resultados coincidentes, consultas sin coincidencias, errores de búsqueda y restricciones por permisos</strong>. '
               'Estas pruebas se hacen juntas, con las mismas consultas reales.'),
]

CAPITULOS = [
    ('02', '02.01', C4, CAP04, None),
    ('02', '02.03', C6, CAP06, None),
]
