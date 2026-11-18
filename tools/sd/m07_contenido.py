"""Bloque 4 · Módulo 07 Contenido (CNT): 23 Escritura, 24 Mensajes y 25 Localización; y 27 Gráficos y 28 Indicadores (DAV).
Requisitos: textos base de Keylin. La voz se cita del Libro de Marca (capítulo Voz) y de reglas-de-voz.md; no se copia.
"""
from .base import N, req, stack, matriz, detalle, contraste, sub, c, L, M, norma, seccion


def n23(nid, nombre, k, *a, **kw): return norma(nid, nombre, '07.01', 'contenido-comunicacion', 'escritura-de-interfaz', k, *a, **kw)
def n24(nid, nombre, k, *a, **kw): return norma(nid, nombre, '07.02', 'contenido-comunicacion', 'mensajes-del-sistema', k, *a, **kw)
def n25(nid, nombre, k, *a, **kw): return norma(nid, nombre, '07.03', 'contenido-comunicacion', 'lenguaje-y-localizacion', k, *a, **kw)
def n27(nid, nombre, k, *a, **kw): return norma(nid, nombre, '08.02', 'datos-visualizacion', 'graficos-de-datos', k, *a, **kw)
def n28(nid, nombre, k, *a, **kw): return norma(nid, nombre, '08.03', 'datos-visualizacion', 'indicadores-y-cifras', k, *a, **kw)


# ═════════════ 23 · Escritura ═════════════
CAP23 = [
    n23('KYN-SDI-CNT-001', 'Lenguaje funcional', 1, 'Cada texto dice qué se puede hacer y qué pasará',
        'El texto de interfaz <strong>es una instrucción</strong>.', [
        req(N('Las instrucciones y etiquetas deben indicar con claridad qué puede hacer la persona y qué resultado esperar.', 'debe')),
        sub('Ejemplos'),
        contraste([('Aceptar', 'Agregar cliente'), ('Ok', 'Enviar comprobante'), ('Enviar', 'Enviar solicitud de mantenimiento')]),
        stack([('Botones', ['Verbo y objeto.']),
               ('Etiquetas', ['El nombre del dato en el lenguaje de la persona: «Nombre completo», no «Name».']),
               ('Voz', [f'Trato de usted y voz del sistema según el capítulo Voz del Libro de Marca ({M("KYN-MRK-VOZ-001")}).'])]),
        detalle([
            ('Verificación', [
                ('Sin explicación', 'La persona dice qué hará cada botón antes de usarlo, sin ayuda externa.')])]),
    ], origen=['Lenguaje funcional (base)', 'UIX-041', 'UIX-040'], responsabilidad='Instrucciones y etiquetas dicen qué hacer y qué resultado esperar.', corto='Lenguaje funcional'),

    n23('KYN-SDI-CNT-002', 'Consistencia', 2, 'Una acción, un nombre',
        'El mismo concepto <strong>se llama siempre igual</strong>.', [
        req(N('Una misma acción o concepto debe utilizar una denominación consistente dentro del contexto del producto.', 'debe')),
        stack([('Glosario', ['Cada producto mantiene su lista de términos: acción, objeto y estados.']),
               ('Navegación', [f'Para nombres de secciones rige Nombres comprensibles ({L("04")}).'])]),
        detalle([
            ('Verificación', [
                ('Glosario', 'Se revisan todas las pantallas contra el glosario. Resultado esperado: un término por concepto.')])]),
    ], origen=['Consistencia (base)'], responsabilidad='Cada acción o concepto usa una sola denominación.', corto='Consistencia'),

    n23('KYN-SDI-CNT-003', 'Brevedad útil', 3, 'Lo justo para comprender',
        'Breve, <strong>sin quitar lo necesario</strong>.', [
        req(N('El contenido debería ser tan breve como permita la comprensión, sin eliminar información necesaria.', 'deberia')),
        stack([('Límites de la marca', ['Hasta 25 palabras por oración y frases con una sola idea (reglas de voz).']),
               ('Ayudas', ['Una ayuda breve visible; el detalle, a pedido (ARQ-004).'])]),
        detalle([
            ('Verificación', [
                ('Interpretación', 'Las personas interpretan correctamente etiquetas y acciones sin explicación adicional.')])]),
    ], origen=['Brevedad útil (base)'], responsabilidad='Los textos son tan breves como permite la comprensión.', corto='Brevedad'),
]

# ═════════════ 24 · Mensajes ═════════════
CAP24 = [
    n24('KYN-SDI-CNT-004', 'Errores comprensibles', 1, 'Un error dice qué pasó y cómo seguir',
        'Explicar <strong>y ofrecer una salida</strong>.', [
        req(N('Los mensajes de error deben explicar qué ocurrió y cómo continuar o recuperarse cuando exista una acción posible.', 'debe')),
        matriz('Estructura de un mensaje de error (desde UIX-024)', [('Qué dice', ''), ('Ejemplo', '')], [
            ('Qué pasó', ['La situación en lenguaje claro, sin códigos técnicos.', '«El pago está pendiente de verificación.»']),
            ('Por qué, si ayuda', ['La causa, cuando la persona puede hacer algo con ella.', '«El comprobante no se pudo leer.»']),
            ('Qué hacer', ['La acción para continuar.', '«Adjunte el comprobante de nuevo.»'])]),
        detalle([
            ('Verificación', [
                ('Revisión', 'Ningún mensaje muestra códigos técnicos y cada uno ofrece una acción cuando existe.')])]),
    ], origen=['Errores comprensibles (base)', 'UIX-024'], responsabilidad='Los errores explican qué pasó y cómo continuar.', corto='Errores'),

    n24('KYN-SDI-CNT-005', 'Confirmaciones específicas', 2, 'Una confirmación dice lo que de verdad ocurrió',
        'Confirmar <strong>solo lo hecho</strong>.', [
        req(N('Los mensajes de éxito deben describir el resultado real y no afirmar acciones que todavía no se hayan completado.', 'debe')),
        sub('Ejemplos'),
        contraste([('¡Éxito!', 'Cliente María González registrado.'), ('Pago realizado', 'Pago enviado; la confirmación del banco llega en unos minutos.')]),
        detalle([
            ('Verificación', [
                ('Procesos en curso', 'En un proceso que sigue después de la acción, el mensaje no lo da por terminado.')])]),
    ], origen=['Confirmaciones específicas (base)'], responsabilidad='Las confirmaciones describen el resultado real.', corto='Confirmaciones'),

    n24('KYN-SDI-CNT-006', 'Información segura', 3, 'Un mensaje no revela lo que no corresponde',
        'Explicar <strong>sin exponer</strong>.', [
        req(N('Los mensajes no deben exponer información técnica sensible ni datos que la persona no está autorizada a consultar.', 'no-debe')),
        stack([('Técnico', ['Rutas, consultas y trazas de error se registran internamente, no en pantalla.']),
               ('Permisos', [f'Ver Acceso directo y rutas no disponibles ({L("05")}) y Resultados autorizados ({L("06")}).'])]),
        detalle([
            ('Verificación', [
                ('Fallos forzados', 'Se fuerzan errores de servidor y de permisos. Resultado esperado: ningún mensaje muestra datos internos ni restringidos.')])]),
    ], origen=['Información segura (base)'], responsabilidad='Los mensajes no exponen información técnica sensible ni datos restringidos.', corto='Seguridad'),
]

# ═════════════ 25 · Localización ═════════════
CAP25 = [
    n25('KYN-SDI-CNT-007', 'Lenguaje adecuado', 1, 'Cada idioma con sus formatos',
        'Localizar es <strong>más que traducir</strong>.', [
        req(N('Las interfaces deben adaptar idioma, formatos, unidades y convenciones cuando se ofrece una localización específica.', 'debe')),
        matriz('Formatos en español de Costa Rica (referencia)', [('Formato', ''), ('Ejemplo', '')], [
            ('Números', ['Miles con punto y decimales con coma.', '1.240,50']),
            ('Moneda', ['Símbolo pegado a la cifra.', '₡45.000']),
            ('Fechas', ['Día, mes y año.', '30 de junio de 2026 · 30/06/2026']),
            ('Porcentajes y unidades', ['Con espacio.', '50 %, 16 px'])]),
        detalle([
            ('Verificación', [
                ('Datos reales', 'Se prueban fechas, números, montos y nombres reales en cada idioma admitido.')])]),
    ], origen=['Lenguaje adecuado (base)', 'Convenciones de escritura (reglas de voz)'], responsabilidad='Las localizaciones adaptan idioma, formatos, unidades y convenciones.', corto='Lenguaje'),

    n25('KYN-SDI-CNT-008', 'Consistencia lingüística', 2, 'La traducción conserva la función',
        'Cada idioma <strong>dice lo mismo</strong>.', [
        req(N('Las traducciones deben conservar el significado funcional de acciones, estados e instrucciones.', 'debe')),
        stack([('Glosario por idioma', ['El glosario de cada producto (CNT-002) tiene su versión en cada idioma.'])]),
        detalle([
            ('Verificación', [
                ('Revisión cruzada', 'Una persona nativa revisa acciones, estados y mensajes contra el original.')])]),
    ], origen=['Consistencia lingüística (base)'], responsabilidad='Las traducciones conservan el significado funcional.', corto='Traducción'),

    n25('KYN-SDI-CNT-009', 'Espacio variable', 3, 'Los componentes aceptan textos más largos',
        'Otro idioma <strong>no rompe la interfaz</strong>.', [
        req(N('Los componentes deben tolerar variaciones razonables de longitud entre idiomas sin perder funcionalidad.', 'debe')),
        stack([('Diseño', ['Botones y etiquetas crecen con su texto; las columnas permiten dos líneas.']),
               ('Dirección de lectura', ['Las localizaciones de derecha a izquierda, si se ofrecen, invierten la disposición.'])]),
        detalle([
            ('Verificación', [
                ('Textos largos', 'Se prueba con textos un tercio más largos que el español. Resultado esperado: nada se corta ni se superpone.')])]),
    ], origen=['Espacio variable (base)'], responsabilidad='Los componentes toleran textos de distinta longitud entre idiomas.', corto='Espacio variable'),
]

# ═════════════ 27 · Gráficos ═════════════
CAP27 = [
    n27('KYN-SDI-DAV-007', 'Representación apropiada', 1, 'Cada relación tiene su gráfico',
        'Elegir el gráfico <strong>por la pregunta que responde</strong>.', [
        req(N('El tipo de gráfico debe corresponder a la relación que se necesita comunicar.', 'debe')),
        matriz('Relación y gráfico', [('Gráfico', ''), ('Origen', 'Libro de Marca')], [
            ('Evolución en el tiempo', ['Línea o columnas.', M('KYN-MRK-DAT-004')]),
            ('Comparación entre categorías', ['Barras.', M('KYN-MRK-DAT-004')]),
            ('Partes de un todo', ['Barras apiladas al 100 % o pocas porciones.', M('KYN-MRK-DAT-004')]),
            ('Distribución', ['Histograma o puntos.', M('KYN-MRK-DAT-004')])]),
        detalle([
            ('Verificación', [
                ('Pregunta', 'Para cada gráfico se escribe la pregunta que responde; el tipo corresponde a esa pregunta.')])]),
    ], origen=['Representación apropiada (base)'], responsabilidad='El tipo de gráfico corresponde a la relación que comunica.', corto='Representación'),

    n27('KYN-SDI-DAV-008', 'Color de datos', 2, 'Las paletas siguen la naturaleza de los datos',
        'El color de los datos <strong>tiene sus reglas</strong>.', [
        req(N('Los gráficos deben respetar las reglas oficiales de paletas categóricas, secuenciales y divergentes según la naturaleza de los datos.', 'debe')),
        stack([('Fuente única', [f'Las paletas son las de {M("KYN-MRK-DAT-002")}; aquí no se repiten.'])]),
        detalle([
            ('Verificación', [
                ('Paleta', 'Cada gráfico usa una sola paleta oficial, la que corresponde a sus datos.')])]),
    ], origen=['Color de datos (base)'], responsabilidad='Los gráficos usan las paletas oficiales según sus datos.', corto='Color de datos'),

    n27('KYN-SDI-DAV-009', 'Interpretación accesible', 3, 'Un gráfico se entiende sin el color',
        'Los valores <strong>se pueden leer de más de una forma</strong>.', [
        req(N('La información no debe depender exclusivamente del color ni ocultar unidades, escalas o referencias necesarias.', 'no-debe')),
        stack([('Señales', ['Etiquetas directas, formas o patrones además del color.']),
               ('Alternativa', ['Tabla de datos o descripción con los valores clave, accesible desde el gráfico.']),
               ('Ejes', ['Unidades y escalas visibles; el eje que no empieza en cero se indica.'])]),
        detalle([
            ('Verificación', [
                ('Formas de acceso', 'Se interpretan los valores en escala de grises, con lector de pantalla y con la tabla de datos.')])]),
    ], origen=['Interpretación accesible (base)'], responsabilidad='Los gráficos no dependen del color y muestran unidades y escalas.', corto='Interpretación'),
]

# ═════════════ 28 · Indicadores ═════════════
CAP28 = [
    n28('KYN-SDI-DAV-010', 'Contexto suficiente', 1, 'Cada indicador dice qué mide',
        'Una cifra sin contexto <strong>no se puede interpretar</strong>.', [
        req(N('Cada indicador debe identificar su significado, unidad, período y referencia cuando sean necesarios para interpretarlo.', 'debe')),
        matriz('Anatomía de un indicador', [('Qué es', ''), ('Ejemplo', '')], [
            ('Nombre', ['Qué mide.', 'Pagos vencidos']),
            ('Valor y unidad', ['La cifra con su unidad.', '₡1.240.000']),
            ('Período', ['A qué tiempo corresponde.', 'Noviembre de 2026']),
            ('Referencia', ['Comparación o meta.', '+12 % frente a octubre'])]),
        detalle([
            ('Verificación', [
                ('Interpretación', 'Personas distintas interpretan el indicador de la misma forma.')])]),
    ], origen=['Contexto suficiente (base)'], responsabilidad='Cada indicador muestra significado, unidad, período y referencia.', corto='Contexto'),

    n28('KYN-SDI-DAV-011', 'Estados fundamentados', 2, 'Los umbrales responden a criterios definidos',
        'Un color de alerta <strong>tiene una regla detrás</strong>.', [
        req(N('Los umbrales y colores de evaluación deben responder a criterios definidos, no a límites arbitrarios introducidos por diseño.', 'debe')),
        stack([('Origen del umbral', ['Lo define el área responsable del dato; diseño lo representa.']),
               ('Señal', ['Estado con color, ícono y texto (FUI-005).'])]),
        detalle([
            ('Verificación', [
                ('Registro', 'Cada umbral tiene su criterio y su responsable registrados.')])]),
    ], origen=['Estados fundamentados (base)'], responsabilidad='Umbrales y colores de evaluación responden a criterios definidos.', corto='Umbrales'),

    n28('KYN-SDI-DAV-012', 'Actualización visible', 3, 'Se sabe cuándo se actualizó el dato',
        'La vigencia <strong>es parte del dato</strong>.', [
        req(N('La información debería indicar cuándo fue actualizada cuando su vigencia afecte una decisión.', 'deberia')),
        stack([('Cómo', ['«Actualizado hoy a las 9:40», junto al indicador o arriba del tablero.'])]),
        detalle([
            ('Verificación', [
                ('Datos viejos', 'Con datos sin actualizar, el aviso de vigencia se ve.')])]),
    ], origen=['Actualización visible (base)'], responsabilidad='La información muestra cuándo se actualizó cuando su vigencia importa.', corto='Actualización'),
]

CAPITULOS = [
    ('07', '07.01', 'escritura-de-interfaz', CAP23, None),
    ('07', '07.02', 'mensajes-del-sistema', CAP24, None),
    ('07', '07.03', 'lenguaje-y-localizacion', CAP25, None),
    ('08', '08.02', 'graficos-de-datos', CAP27, None),
    ('08', '08.03', 'indicadores-y-cifras', CAP28, None),
]
