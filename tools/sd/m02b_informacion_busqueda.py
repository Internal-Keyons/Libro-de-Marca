"""Módulo 02 · Arquitectura (ARQ), capítulos 04 Información y 06 Búsqueda (el 05 Navegación está en m02_arquitectura.py).
Requisitos: textos de Keylin (base y ampliación, 2026-11-17). Decisiones, comportamientos, excepciones y verificaciones:
propuesta de Claude en borrador. Las «Ampliaciones necesarias» de su matriz se integran en las normas existentes.
"""
from .base import N, req, stack, matriz, contraste, detalle, sub, L, norma, seccion

MOD = 'arquitectura-navegacion'

# ═════════════ 04 · Información ═════════════
C4 = 'arquitectura-de-informacion'
def n4(nid, nombre, k, *a, **kw): return norma(nid, nombre, '02.01', MOD, C4, k, *a, **kw)


CAP04 = [
    n4('KYN-SDI-ARQ-001', 'Organización comprensible', 1, 'El contenido se agrupa como lo piensan las personas',
       'La organización <strong>sigue las tareas</strong>, no el organigrama.', [
        req(N('El contenido debe agruparse según la relación entre tareas, conceptos y necesidades de las personas, no exclusivamente según la estructura interna de la empresa.', 'debe'),
            N('Las agrupaciones de información deben responder a relaciones funcionales o conceptuales identificables.', 'debe')),
        stack([('Cómo se decide', ['Con las tareas y el vocabulario de los perfiles (PEX-007). Cuando la estructura es nueva, con un ordenamiento de tarjetas o una prueba de árbol.']),
               ('Estructura de página', ['Cada página tiene un objeto principal y sus grupos; cada grupo se nombra por su contenido.']),
               ('Relaciones', ['Desde un elemento se llega a lo relacionado sin volver al menú: del cliente a sus facturas, de la factura a su pago.'])]),
        detalle([
            ('Verificación', [
                ('Prueba de árbol', 'Personas de cada perfil buscan cinco elementos frecuentes en la estructura, sin la interfaz. Se registra la tasa de éxito; el umbral lo fija 44 Validación.'),
                ('Resultado esperado', 'Encuentran los elementos sin conocer cómo está organizada la base de datos.')])]),
    ], origen=['Organización comprensible (base)', 'Agrupación con sentido (ampliación)', 'Estructura de páginas, agrupación y navegación contextual (ampliación de la matriz)'],
       responsabilidad='El contenido se agrupa por tareas y conceptos de las personas, con relaciones identificables.'),

    n4('KYN-SDI-ARQ-002', 'Nombres comprensibles', 2, 'Cada sección se nombra como la reconoce la persona',
       'Un nombre claro <strong>evita buscar</strong>.', [
        req(N('Las categorías, secciones y elementos de navegación deben utilizar denominaciones que las personas puedan reconocer según su contexto de trabajo.', 'debe')),
        stack([('Vocabulario', ['El de los perfiles, no el del código ni el de la base de datos.']),
               ('Un concepto, un nombre', [f'El mismo concepto se nombra igual en todo el producto ({L("23")}).']),
               ('Siglas', ['Solo las que el perfil usa a diario.'])]),
        sub('Ejemplos'),
        contraste([('Entidades', 'Clientes'), ('Módulo de gestión de tickets', 'Solicitudes'), ('Config.', 'Configuración')]),
        detalle([
            ('Verificación', [
                ('Comprensión', 'Se muestra cada nombre de sección sin contexto y la persona dice qué espera encontrar.'),
                ('Resultado esperado', 'Lo que espera coincide con el contenido de la sección.')])]),
    ], origen=['Nombres comprensibles (ampliación)', 'Nombres de categorías (ampliación de la matriz)', 'UIX-041'],
       responsabilidad='Categorías, secciones y destinos usan nombres que las personas reconocen.',
       cita='23 Escritura (Consistencia) desarrolla la redacción'),

    n4('KYN-SDI-ARQ-003', 'Jerarquía identificable', 3, 'Se distingue lo principal de lo complementario',
       'La jerarquía <strong>ordena la lectura</strong>.', [
        req(N('Las páginas deben diferenciar información principal, secundaria y complementaria mediante una jerarquía consistente.', 'debe')),
        matriz('Tres niveles de información', [('Qué contiene', ''), ('Dónde va', '')], [
            ('Principal', ['Lo que identifica el objeto y permite la tarea.', 'Título, datos clave y acción principal, arriba y con mayor peso.']),
            ('Secundaria', ['Lo que amplía o permite tareas frecuentes relacionadas.', 'Grupos rotulados, debajo o al lado.']),
            ('Complementaria', ['Historial, auditoría y configuración.', 'A pedido: pestañas, acordeones o enlaces (ARQ-004).'])]),
        detalle([
            ('Verificación', [
                ('Tres datos', 'Se pide a la persona que nombre los tres datos más importantes de la pantalla.'),
                ('Resultado esperado', f'Coinciden con la información principal definida. La jerarquía visual se revisa con {L("09")}.')])]),
    ], origen=['Jerarquía identificable (base)', 'Jerarquías (ampliación de la matriz)'],
       responsabilidad='Las páginas distinguen información principal, secundaria y complementaria.',
       cita='09 Tipografía define la jerarquía visual'),

    n4('KYN-SDI-ARQ-004', 'Información progresiva', 4, 'Lo esencial a la vista; el detalle, a pedido',
       'El detalle aparece <strong>cuando hace falta</strong>.', [
        req(N('La información necesaria para decidir o ejecutar la siguiente acción debe permanecer disponible en el momento correspondiente.', 'debe'),
            N('Los detalles especializados pueden presentarse progresivamente cuando su presencia inicial aumente innecesariamente la complejidad.', 'puede')),
        stack([('Lo que siempre se ve', ['Requisitos, consecuencias, errores y datos obligatorios.']),
               ('Cómo se revela', [f'Pestañas, acordeones, paneles o enlaces, según {L("14")}. El control dice qué contiene.']),
               ('Sin perder el contexto', ['Al abrir un detalle, la persona sigue viendo de qué elemento es.'])]),
        detalle([
            ('Verificación', [
                ('Siguiente acción', 'En cada paso de una tarea, la persona decide sin abrir detalles para buscar un dato necesario.'),
                ('Detalle', 'Cada detalle oculto se encuentra desde el control que lo anuncia, sin perder la tarea.')])]),
    ], origen=['Información progresiva (base)', 'Detalle progresivo (ampliación)', 'Información esencial visible (ampliación)', 'Revelación progresiva (ampliación de la matriz)', 'UIX-028'],
       responsabilidad='Lo esencial está visible en su momento; el detalle se ofrece a pedido sin ocultar requisitos.'),

    seccion('ejemplo', '04', 'Ejemplo de aplicación', 'Un expediente',
            'Un expediente muestra primero <strong>los datos necesarios para identificarlo y trabajar</strong>; los registros históricos permanecen accesibles sin competir con la tarea principal.', [
        stack([('Principal', ['Nombre, número, estado y la acción «Actualizar».']),
               ('Complementaria', ['Historial y auditoría, en una pestaña.']),
               ('Verificación del capítulo', ['Las personas encuentran información importante sin tener que conocer cómo está organizada internamente la base de datos.'])]),
    ]),
]

# ═════════════ 06 · Búsqueda ═════════════
C6 = 'busqueda-y-orientacion'
def n6(nid, nombre, k, *a, **kw): return norma(nid, nombre, '02.03', MOD, C6, k, *a, **kw)


CAP06 = [
    n6('KYN-SDI-ARQ-011', 'Alcance identificable', 1, 'Se sabe dónde busca la búsqueda',
       'El alcance <strong>ajusta lo que se espera encontrar</strong>.', [
        req(N('Cuando una búsqueda está limitada a una sección, categoría o conjunto de datos, su alcance debe resultar comprensible.', 'debe')),
        stack([('Global o local', ['La búsqueda global vive en la cabecera; la local, junto a la lista que filtra, con un texto que nombra su alcance: «Buscar en solicitudes».']),
               ('Cambio de alcance', ['Desde una búsqueda local sin resultados se ofrece buscar en todo el producto.'])]),
        detalle([
            ('Verificación', [
                ('Dos búsquedas', 'La persona distingue, sin escribir nada, cuál busca en todo el producto y cuál dentro de la lista.')])]),
    ], origen=['Alcance identificable (ampliación)', 'Búsqueda global frente a local (ampliación de la matriz)'],
       responsabilidad='Se entiende si la búsqueda es global o está limitada a una sección o conjunto.'),

    n6('KYN-SDI-ARQ-012', 'Resultados pertinentes', 2, 'La búsqueda encuentra lo que la tarea necesita',
       'Se encuentra <strong>por lo que la persona recuerda</strong>.', [
        req(N('La búsqueda debe utilizar los campos y contenidos relevantes para la tarea, respetando los permisos de acceso.', 'debe')),
        stack([('Campos', ['Nombre, código, identificación y los datos que el perfil usa para recordar un registro.']),
               ('Coincidencia parcial', ['Encuentra por parte del texto, sin distinguir mayúsculas ni tildes.']),
               ('Orden', ['Primero las coincidencias exactas; después, las más recientes o las más usadas, según la tarea.'])]),
        detalle([
            ('Autocompletado', [
                ('Cuándo', 'En listas conocidas: clientes, productos, direcciones.'),
                ('Comportamiento', f'Las sugerencias aparecen al escribir; las flechas las recorren, Enter elige y Escape cierra. Sigue el patrón de cuadro combinado de {L("13")}.')]),
            ('Errores de escritura', [
                ('Sugerencia', 'Cuando el producto lo permite, se ofrece la forma correcta: «¿Quiso decir…?».')]),
            ('Verificación', [
                ('Consultas reales', 'Se buscan registros con nombre parcial, sin tildes y con un error de escritura. Resultado esperado: el registro buscado aparece entre los primeros resultados.')])]),
    ], origen=['Resultados pertinentes (base)', 'Autocompletado, búsqueda parcial, errores ortográficos y resultados ordenados (ampliación de la matriz)'],
       responsabilidad='La búsqueda usa los campos relevantes, encuentra por coincidencia parcial y ordena por pertinencia.',
       cita='El límite de permisos está en ARQ-016'),

    n6('KYN-SDI-ARQ-013', 'Resultados comprensibles', 3, 'Cada resultado se distingue de los parecidos',
       'Se elige el resultado <strong>sin abrirlo</strong>.', [
        req(N('Cada resultado debe proporcionar información suficiente para distinguirlo de otros elementos similares.', 'debe')),
        stack([('Datos del resultado', ['Nombre, tipo y uno o dos datos que lo diferencian, como código, fecha o unidad.']),
               ('Coincidencia', ['El término buscado se resalta en el resultado.']),
               ('Muchos resultados', [f'Se indica el total y se pagina o se carga por partes; los filtros reducen la lista ({L("26")}).'])]),
        detalle([
            ('Verificación', [
                ('Nombres parecidos', 'Se buscan dos registros con nombres casi iguales. Resultado esperado: la persona elige el correcto sin abrirlos.')])]),
    ], origen=['Resultados comprensibles (base)', 'Manejo de resultados extensos (ampliación de la matriz)'],
       responsabilidad='Cada resultado se distingue de otros similares y los resultados extensos se pueden recorrer.'),

    n6('KYN-SDI-ARQ-014', 'Filtros visibles', 4, 'Los filtros activos están a la vista',
       'Cada lista muestra <strong>qué la está filtrando</strong>.', [
        req(N('Los filtros activos deben poder identificarse y modificarse sin perder innecesariamente la consulta.', 'debe')),
        stack([('Filtros activos', ['Se muestran como etiquetas que se quitan una a una, con «Quitar filtros» para todos.']),
               ('Combinación', ['Los filtros se combinan sin borrar la consulta escrita.']),
               ('Al volver', [f'Se conservan según Regreso sin pérdida, en {L("05")}.'])]),
        detalle([
            ('Verificación', [
                ('Aplicar y quitar', 'Se aplican, combinan y quitan filtros. Resultado esperado: la consulta escrita se mantiene y cada filtro activo se ve.')])]),
    ], origen=['Filtros visibles (ampliación)', 'Conservación de filtros (ampliación de la matriz)'],
       responsabilidad='Los filtros activos se ven y se modifican sin perder la consulta.',
       cita='La conservación al volver la regula ARQ-010 (05)'),

    n6('KYN-SDI-ARQ-015', 'Sin resultados', 5, 'Una búsqueda vacía explica qué pasó y cómo seguir',
       'Sin resultados <strong>también hay un camino</strong>.', [
        req(N('Cuando no existen coincidencias, la interfaz debe explicar la situación y ofrecer una acción útil, como modificar la consulta o retirar filtros.', 'debe'),
            N('La interfaz debe distinguir entre una búsqueda sin coincidencias y un error que impidió realizar la consulta.', 'debe')),
        matriz('Tres situaciones sin resultados', [('Qué se dice', ''), ('Cómo sigue', '')], [
            ('Sin coincidencias', ['Que no hay resultados para esa consulta y esos filtros.', 'Revisar el término, quitar filtros o buscar en todo el producto.']),
            ('Error de consulta', ['Que la búsqueda no se pudo realizar.', f'Reintentar; si persiste, una ruta alternativa ({L("18")}).']),
            ('Sin acceso al alcance', ['Que no tiene acceso a ese conjunto, sin revelar su contenido (ARQ-016).', 'Cambiar de alcance o solicitar acceso, si el producto lo prevé.'])]),
        detalle([
            ('Verificación', [
                ('Tres casos', f'Se fuerza cada situación. Resultado esperado: tres mensajes distintos, cada uno con su salida. La redacción sigue {L("24")}.')])]),
    ], origen=['Sin resultados (base)', 'Ausencia de resultados (ampliación)', 'UIX-026', 'UIX-023'],
       responsabilidad='Sin coincidencias, la interfaz lo explica y ofrece una acción; un error y la falta de acceso se distinguen.',
       cita='24 Mensajes define la redacción'),

    n6('KYN-SDI-ARQ-016', 'Resultados autorizados', 6, 'La búsqueda solo muestra lo que la persona puede ver',
       'Ningún resultado <strong>revela lo restringido</strong>.', [
        req(N('La búsqueda no debe revelar información que la persona carece de permiso para consultar, ni mediante resultados, cantidades, sugerencias o fragmentos de contenido.', 'no-debe')),
        stack([('Dónde se filtra', ['En el servidor, antes de contar, sugerir o resaltar.']),
               ('Totales y sugerencias', ['Se calculan sobre lo autorizado.']),
               ('Registros con partes restringidas', ['El resultado muestra solo los campos permitidos.'])]),
        detalle([
            ('Verificación', [
                ('Perfiles distintos', 'Se repiten las mismas consultas con perfiles de distinto permiso.'),
                ('Resultado esperado', 'Resultados, totales, sugerencias y fragmentos cambian según el permiso, y ninguna respuesta del servidor incluye datos no autorizados.')])]),
    ], origen=['Resultados autorizados (ampliación)'],
       responsabilidad='La búsqueda no revela, por ninguna vía, información sin permiso.',
       cita='Aplica PEX-008 a la búsqueda'),

    seccion('ejemplo', '06', 'Ejemplo de aplicación', 'Residentes con nombres parecidos',
            'Una búsqueda de residentes diferencia personas con nombres similares <strong>mediante datos identificativos permitidos</strong>.', [
        stack([('Resultado', ['«Ana Mora · Casa 12 · desde 2021» y «Ana Mora · Casa 40 · desde 2024».']),
               ('Verificación del capítulo', ['Se comprueban resultados coincidentes, consultas sin coincidencias, errores de búsqueda y restricciones por permisos.'])]),
    ]),
]

CAPITULOS = [
    ('02', '02.01', C4, CAP04, None),
    ('02', '02.03', C6, CAP06, None),
]
