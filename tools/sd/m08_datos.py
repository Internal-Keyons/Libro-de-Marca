"""Módulo 08 · Datos (DAV): 26 Tablas y 29 Dashboards (Bloque 3). 27 y 28 van en el Bloque 4.
Requisitos: textos de Keylin (docs/sd/fuente-keylin-2026-11-17.md). Componentes y patrones descritos en texto y tablas.
"""
from .base import N, req, stack, matriz, detalle, c, L, M, norma, seccion

MOD = 'datos-visualizacion'
C26, C29 = 'tablas-y-datos-estructurados', 'dashboards-e-informes'
def n26(nid, nombre, k, *a, **kw): return norma(nid, nombre, '08.01', MOD, C26, k, *a, **kw)
def n29(nid, nombre, k, *a, **kw): return norma(nid, nombre, '08.04', MOD, C29, k, *a, **kw)


# ═════════════ 26 · Tablas ═════════════
CAP26 = [
    n26('KYN-SDI-DAV-001', 'Lectura y comparación', 1, 'Una tabla se lee por filas y se compara por columnas',
        'La tabla <strong>sirve para comparar</strong>.', [
        req(N('Las tablas deben utilizar encabezados comprensibles, alineación consistente y una organización apropiada para comparar datos.', 'debe')),
        matriz('Alineación por tipo de dato', [('Alineación', ''), ('Formato', '')], [
            ('Texto', ['A la izquierda.', 'Se trunca según FUI-011.']),
            ('Números y montos', ['A la derecha, con cifras tabulares.', 'Miles con punto y decimales con coma; moneda pegada a la cifra.']),
            ('Fechas', ['A la izquierda.', 'Día, mes y año en el mismo formato en toda la tabla.']),
            ('Estados', ['A la izquierda.', 'Etiqueta con color e ícono (FUI-005).'])]),
        stack([('Encabezados', ['Nombran el dato y su unidad: «Monto (₡)». Se mantienen visibles al desplazar una tabla larga.']),
               ('Primera columna', ['Identifica el registro: nombre o código.'])]),
        detalle([
            ('Notas técnicas', [
                ('Estructura', f'{c("<table>")} con {c("<th scope>")} en encabezados de columna y de fila; un título o {c("<caption>")} nombra la tabla.'),
                ('Orden', f'La columna ordenada lleva {c("aria-sort")} y una flecha que indica el sentido.')]),
            ('Verificación', [
                ('Lector de pantalla', 'Al recorrer una celda se anuncian su fila y su columna.'),
                ('Comparación', 'La persona compara dos registros sin abrirlos.')])]),
    ], origen=['Lectura y comparación (base)', 'UIX-037'], responsabilidad='Las tablas tienen encabezados, alineación y organización para comparar.', corto='Lectura'),

    n26('KYN-SDI-DAV-002', 'Herramientas proporcionadas', 2, 'Buscar, filtrar, ordenar y paginar cuando hace falta',
        'Las herramientas <strong>crecen con el volumen</strong>.', [
        req(N('Búsqueda, filtros, orden y paginación deberían incorporarse según el volumen y las tareas reales.', 'deberia')),
        matriz('Herramientas según el volumen (propuesta)', [('Qué se ofrece', ''), ('Por qué', '')], [
            ('Pocos registros', ['Orden por columna.', 'Se ve todo de una vez.']),
            ('Decenas', ['Orden, búsqueda y filtros frecuentes.', 'Encontrar sin recorrer.']),
            ('Cientos o más', ['Además, paginación o carga por partes, y el total.', 'Mantener la respuesta rápida.'])]),
        stack([('Conservación', [f'Búsqueda, filtros, orden y página se conservan al volver de un registro (Regreso sin pérdida, {L("05")}).']),
               ('Filtros activos', [f'Visibles y removibles (Filtros visibles, {L("06")}).'])]),
        detalle([
            ('Verificación', [
                ('Volúmenes', 'Se prueba la tabla vacía, con pocos registros y con miles. Resultado esperado: las herramientas responden al volumen y el total es correcto.')])]),
    ], origen=['Herramientas proporcionadas (base)'], responsabilidad='Búsqueda, filtros, orden y paginación se ajustan al volumen y la tarea.', corto='Herramientas'),

    n26('KYN-SDI-DAV-003', 'Acciones identificables', 3, 'Las acciones de cada fila se distinguen de sus datos',
        'Leer y actuar <strong>no se confunden</strong>.', [
        req(N('Las acciones por registro deben distinguirse de los valores informativos y respetar los permisos correspondientes.', 'debe')),
        stack([('Dónde van', ['En la última columna: la frecuente visible y las demás en un menú de acciones (CPE-004).']),
               ('Selección múltiple', ['Casillas en la primera columna; las acciones sobre la selección aparecen arriba e indican cuántos registros afectan.']),
               ('Permisos', ['Cada persona ve solo las acciones de su rol (PEX-008).'])]),
        detalle([
            ('En móvil', [
                ('Adaptación', 'La tabla pasa a una lista de tarjetas con los datos clave y las acciones, o conserva el desplazamiento horizontal con la primera columna fija, según la tarea.')]),
            ('Verificación', [
                ('Casos', 'Tablas vacías, extensas, filtradas, ordenadas y en pantallas pequeñas, con perfiles de distinto permiso.')])]),
    ], origen=['Acciones identificables (base)'], responsabilidad='Las acciones por registro se distinguen de los valores y respetan permisos.', corto='Acciones'),

    seccion('ejemplo', '26', 'Ejemplo de aplicación', 'Una lista de pagos',
            'Una tabla de pagos alinea los montos a la derecha, <strong>marca el estado con ícono y texto</strong> y deja las acciones al final de cada fila.', [
        stack([('Verificación del capítulo', ['Probar tablas vacías, extensas, filtradas, ordenadas y adaptadas a pantallas pequeñas.'])]),
    ]),
]

# ═════════════ 29 · Dashboards ═════════════
CAP29 = [
    n29('KYN-SDI-DAV-004', 'Diseño por tarea', 1, 'El tablero responde a las decisiones de quien lo usa',
        'Un tablero <strong>sirve para actuar</strong>.', [
        req(N('Los tableros deben priorizar la información necesaria para las decisiones y actividades de sus usuarios.', 'debe')),
        stack([('Punto de partida', ['Las tareas y decisiones de cada perfil (PEX-007): qué necesita saber al empezar el día y qué tiene que hacer.']),
               ('Contenido', ['Pendientes, excepciones y riesgos primero; los indicadores de contexto después.']),
               ('Cada indicador', [f'Lleva su significado, unidad, período y referencia ({L("28")}).'])]),
        detalle([
            ('Verificación', [
                ('Con personas', 'La persona identifica qué requiere su atención y actúa sin recorrer datos irrelevantes.')])]),
    ], origen=['Diseño por tarea (base)'], responsabilidad='Los tableros priorizan la información para las decisiones de sus usuarios.', corto='Por tarea'),

    n29('KYN-SDI-DAV-005', 'Jerarquía informativa', 2, 'No todos los indicadores pesan lo mismo',
        'La importancia <strong>se ve en el tamaño y el lugar</strong>.', [
        req(N('Los indicadores no deben recibir el mismo protagonismo cuando su importancia operativa sea diferente.', 'no-debe')),
        matriz('Niveles de un tablero', [('Qué contiene', ''), ('Cómo se presenta', '')], [
            ('Primero', ['Lo que exige acción hoy: pendientes, alertas, vencimientos.', 'Arriba, con mayor tamaño y su acción.']),
            ('Segundo', ['Los indicadores clave del período.', 'Cifras con su comparación y tendencia.']),
            ('Tercero', ['Contexto y detalle.', f'Gráficos y tablas debajo o a pedido ({L("27")}).'])]),
        detalle([
            ('Verificación', [
                ('Cinco segundos', 'Se muestra el tablero y la persona dice qué es lo más importante. Cinco segundos es una hipótesis de prueba.')])]),
    ], origen=['Jerarquía informativa (base)'], responsabilidad='Los indicadores reciben protagonismo según su importancia operativa.', corto='Jerarquía',
       cita='Aplica 04 Jerarquía identificable (ARQ-003)'),

    n29('KYN-SDI-DAV-006', 'Profundidad de consulta', 3, 'Del resumen al detalle, sin perder el contexto',
        'El tablero resume; <strong>el detalle está a un paso</strong>.', [
        req(N('Un tablero puede ofrecer acceso a vistas detalladas, filtros y análisis cuando sean necesarios para completar una tarea.', 'puede')),
        stack([('Del indicador al detalle', ['Cada indicador lleva a la lista o el informe que lo explica, con el mismo filtro y período.']),
               ('Filtros del tablero', ['Período y alcance visibles arriba; se aplican a todo el tablero.']),
               ('Exportar', ['Las vistas de datos se exportan en formatos estructurados (desde UIX-037).'])]),
        detalle([
            ('Verificación', [
                ('Recorrido', 'Desde un indicador, la persona llega al detalle y vuelve con el mismo filtro y período.')])]),
    ], origen=['Profundidad de consulta (base)', 'Exploración y exportación (descripción del capítulo)', 'UIX-037'],
       responsabilidad='El tablero lleva a vistas detalladas, filtros y exportación cuando la tarea lo necesita.', corto='Profundidad'),

    seccion('ejemplo', '29', 'Ejemplo de aplicación', 'El tablero de una administración',
            'El tablero de una administración residencial muestra primero <strong>las solicitudes pendientes y los pagos vencidos</strong>, con su acción.', [
        stack([('Verificación del capítulo', ['La persona identifica la información relevante y puede actuar sin recorrer datos irrelevantes.'])]),
    ]),
]

CAPITULOS = [
    ('08', '08.01', C26, CAP26, None),
    ('08', '08.04', C29, CAP29, None),
]
