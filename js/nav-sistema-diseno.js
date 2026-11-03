/* ═══════════════════════════════════════════════════════════════
   KEYONS · MAPA DEL SISTEMA DE DISEÑO
   Generado por tools/sistema_diseno.py desde data/sistema-diseno.json.
   No se edita a mano: se cambia el JSON y se vuelve a generar.
   Cada módulo es un área, como en el Libro de Marca: t es el nombre corto
   (menú, tarjeta, lateral) y full el título completo (página de área).
   Los números son ubicación documental; los códigos de norma van aparte.
   ═══════════════════════════════════════════════════════════════ */
window.KEYONS_BOOK = {
  id: 'sistema-diseno',
  home: 'sistema-diseno/index.html',
  menuLabel: 'Módulos del Sistema de Diseño',
  alt: [['Libro de Marca', 'inicio.html', 'right'], ['Plantilla de norma', 'sistema-diseno/plantilla.html', 'code']],
  status: { p: 'Contenido pendiente' },
  legend: ['e', 'p', 'b', 'r', 'v', 'd'],
  words: { ch: 'Capítulos', pg: 'Subcapítulos', pgs: 'subcapítulos' },
  cardShort: true,
  areaFull: true
};

window.KEYONS_NAV = [
  {
    id: 'pex', k: 'PEX', t: 'Experiencia', full: 'Principios de experiencia', href: 'sistema-diseno/principios-experiencia.html', color: 'noche', colorName: 'Azul Noche',
    cd: 'Criterios de calidad comunes a herramientas internas y productos.',
    d: 'Define los principios de calidad de experiencia compartidos por las herramientas internas y los productos para clientes.',
    ch: [
      { n: '01.01', k: '01-01', t: 'Principios comunes', full: 'Principios compartidos', s: 'e', items: [
          { n: '01.01.01', t: 'Claridad y orientación', st: 'Claridad y orientación', s: 'p', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html#s-01-01-01' },
          { n: '01.01.02', t: 'Consistencia y previsibilidad', st: 'Consistencia', s: 'p', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html#s-01-01-02' },
          { n: '01.01.03', t: 'Control y confianza', st: 'Control y confianza', s: 'p', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html#s-01-01-03' } ] },
      { n: '01.02', k: '01-02', t: 'Personas y contextos', full: 'Personas y contextos de uso', s: 'e', items: [
          { n: '01.02.01', t: 'Roles y capacidades de los usuarios', st: 'Roles y capacidades', s: 'p', href: 'sistema-diseno/principios-experiencia/personas-y-contextos-de-uso.html#s-01-02-01' },
          { n: '01.02.02', t: 'Objetivos, tareas y frecuencia de uso', st: 'Objetivos y tareas', s: 'p', href: 'sistema-diseno/principios-experiencia/personas-y-contextos-de-uso.html#s-01-02-02' },
          { n: '01.02.03', t: 'Carga cognitiva y densidad informativa', st: 'Carga cognitiva', s: 'p', href: 'sistema-diseno/principios-experiencia/personas-y-contextos-de-uso.html#s-01-02-03' } ] },
      { n: '01.03', k: '01-03', t: 'Decisiones verificables', full: 'Decisiones verificables de experiencia', s: 'e', items: [
          { n: '01.03.01', t: 'Principios, hipótesis y requisitos', st: 'Hipótesis y requisitos', s: 'p', href: 'sistema-diseno/principios-experiencia/decisiones-verificables-de-experiencia.html#s-01-03-01' },
          { n: '01.03.02', t: 'Criterios de aceptación UX', st: 'Criterios UX', s: 'p', href: 'sistema-diseno/principios-experiencia/decisiones-verificables-de-experiencia.html#s-01-03-02' },
          { n: '01.03.03', t: 'Indicadores de calidad de experiencia', st: 'Indicadores', s: 'p', href: 'sistema-diseno/principios-experiencia/decisiones-verificables-de-experiencia.html#s-01-03-03' } ] }
    ]
  },
  {
    id: 'arq', k: 'ARQ', t: 'Arquitectura', full: 'Arquitectura y navegación', href: 'sistema-diseno/arquitectura-navegacion.html', color: 'cielo', colorName: 'Azul Cielo',
    cd: 'Cómo se organiza la información y cómo se recorre.',
    d: 'Establece cómo se organiza la información y cómo las personas se desplazan por las aplicaciones.',
    ch: [
      { n: '02.01', k: '02-01', t: 'Información', full: 'Arquitectura de información', s: 'e', items: [
          { n: '02.01.01', t: 'Mapas de contenido y módulos funcionales', st: 'Mapas de contenido', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/arquitectura-de-informacion.html#s-02-01-01' },
          { n: '02.01.02', t: 'Taxonomías y nomenclatura', st: 'Taxonomías', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/arquitectura-de-informacion.html#s-02-01-02' },
          { n: '02.01.03', t: 'Jerarquías y relaciones de información', st: 'Jerarquías', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/arquitectura-de-informacion.html#s-02-01-03' } ] },
      { n: '02.02', k: '02-02', t: 'Navegación', full: 'Estructura de navegación', s: 'e', items: [
          { n: '02.02.01', t: 'Estructura base de aplicación', st: 'Estructura base', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html#s-02-02-01' },
          { n: '02.02.02', t: 'Menús laterales, cabeceras y navegación contextual', st: 'Menús laterales', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html#s-02-02-02' },
          { n: '02.02.03', t: 'Rutas, niveles y navegación adaptable', st: 'Rutas y niveles', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html#s-02-02-03' } ] },
      { n: '02.03', k: '02-03', t: 'Búsqueda', full: 'Búsqueda y orientación', s: 'e', items: [
          { n: '02.03.01', t: 'Búsqueda global y contextual', st: 'Búsqueda global', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/busqueda-y-orientacion.html#s-02-03-01' },
          { n: '02.03.02', t: 'Filtros y descubrimiento de contenido', st: 'Filtros', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/busqueda-y-orientacion.html#s-02-03-02' },
          { n: '02.03.03', t: 'Ubicación, rutas de navegación y cambio de contexto', st: 'Ubicación y contexto', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/busqueda-y-orientacion.html#s-02-03-03' } ] }
    ]
  },
  {
    id: 'fui', k: 'FUI', t: 'Fundamentos', full: 'Fundamentos de interfaz', href: 'sistema-diseno/fundamentos-interfaz.html', color: 'salmon', colorName: 'Salmón Tierra',
    cd: 'Los fundamentos de Marca convertidos en reglas de interfaz.',
    d: 'Traduce los fundamentos visuales de Marca a reglas técnicas y visuales aplicables a interfaces.',
    ch: [
      { n: '03.01', k: '03-01', t: 'Tokens', full: 'Tokens de diseño', s: 'e', items: [
          { n: '03.01.01', t: 'Tokens base, semánticos y de componente', st: 'Tokens base', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/tokens-de-diseno.html#s-03-01-01' },
          { n: '03.01.02', t: 'Nomenclatura, jerarquía y herencia', st: 'Nomenclatura', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/tokens-de-diseno.html#s-03-01-02' },
          { n: '03.01.03', t: 'Temas visuales y versionado', st: 'Temas visuales', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/tokens-de-diseno.html#s-03-01-03' } ] },
      { n: '03.02', k: '03-02', t: 'Color funcional', full: 'Color funcional', s: 'e', items: [
          { n: '03.02.01', t: 'Superficies, texto y bordes', st: 'Superficies', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/color-funcional.html#s-03-02-01' },
          { n: '03.02.02', t: 'Colores de interacción, foco y estados', st: 'Colores de interacción', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/color-funcional.html#s-03-02-02' },
          { n: '03.02.03', t: 'Contraste y adaptación entre modos de color', st: 'Contraste', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/color-funcional.html#s-03-02-03' } ] },
      { n: '03.03', k: '03-03', t: 'Tipografía', full: 'Tipografía aplicada', s: 'e', items: [
          { n: '03.03.01', t: 'Funciones de las familias tipográficas oficiales', st: 'Familias tipográficas', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/tipografia-aplicada.html#s-03-03-01' },
          { n: '03.03.02', t: 'Jerarquías, escalas y legibilidad', st: 'Jerarquías y escalas', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/tipografia-aplicada.html#s-03-03-02' },
          { n: '03.03.03', t: 'Números, cifras y tipografía de datos', st: 'Cifras y datos', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/tipografia-aplicada.html#s-03-03-03' } ] },
      { n: '03.04', k: '03-04', t: 'Espacio y retícula', full: 'Espacio, retícula y geometría', s: 'e', items: [
          { n: '03.04.01', t: 'Retículas y puntos de adaptación', st: 'Retículas', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/espacio-reticula-y-geometria.html#s-03-04-01' },
          { n: '03.04.02', t: 'Espaciado y densidad de interfaz', st: 'Espaciado', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/espacio-reticula-y-geometria.html#s-03-04-02' },
          { n: '03.04.03', t: 'Geometría y esquinas de componentes', st: 'Geometría', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/espacio-reticula-y-geometria.html#s-03-04-03' } ] },
      { n: '03.05', k: '03-05', t: 'Recursos visuales', full: 'Recursos visuales de interfaz', s: 'e', items: [
          { n: '03.05.01', t: 'Iconografía funcional', st: 'Iconografía funcional', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/recursos-visuales-de-interfaz.html#s-03-05-01' },
          { n: '03.05.02', t: 'Bordes, sombras y elevación', st: 'Bordes', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/recursos-visuales-de-interfaz.html#s-03-05-02' },
          { n: '03.05.03', t: 'Imágenes, degradados y texturas aplicadas', st: 'Imágenes', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/recursos-visuales-de-interfaz.html#s-03-05-03' } ] }
    ]
  },
  {
    id: 'cpe', k: 'CPE', t: 'Componentes', full: 'Componentes y estados', href: 'sistema-diseno/componentes-estados.html', color: 'atardecer', colorName: 'Salmón Atardecer',
    cd: 'Piezas reutilizables, sus variantes y sus estados.',
    d: 'Define los componentes reutilizables y sus variantes. Aquí se documentan las piezas, mientras que los flujos completos pertenecen a Patrones de interacción.',
    ch: [
      { n: '04.01', k: '04-01', t: 'Acciones', full: 'Componentes de acción', s: 'e', items: [
          { n: '04.01.01', t: 'Botones y botones con icono', st: 'Botones', s: 'p', href: 'sistema-diseno/componentes-estados/componentes-de-accion.html#s-04-01-01' },
          { n: '04.01.02', t: 'Enlaces, menús y acciones', st: 'Enlaces', s: 'p', href: 'sistema-diseno/componentes-estados/componentes-de-accion.html#s-04-01-02' },
          { n: '04.01.03', t: 'Estados de disponibilidad y procesamiento', st: 'Disponibilidad', s: 'p', href: 'sistema-diseno/componentes-estados/componentes-de-accion.html#s-04-01-03' } ] },
      { n: '04.02', k: '04-02', t: 'Entradas', full: 'Controles de entrada', s: 'e', items: [
          { n: '04.02.01', t: 'Campos de texto y áreas de escritura', st: 'Campos de texto', s: 'p', href: 'sistema-diseno/componentes-estados/controles-de-entrada.html#s-04-02-01' },
          { n: '04.02.02', t: 'Selectores, casillas, radios e interruptores', st: 'Selectores', s: 'p', href: 'sistema-diseno/componentes-estados/controles-de-entrada.html#s-04-02-02' },
          { n: '04.02.03', t: 'Fechas, archivos y entradas especializadas', st: 'Fechas', s: 'p', href: 'sistema-diseno/componentes-estados/controles-de-entrada.html#s-04-02-03' } ] },
      { n: '04.03', k: '04-03', t: 'Estructura', full: 'Componentes de estructura', s: 'e', items: [
          { n: '04.03.01', t: 'Pestañas y componentes de navegación', st: 'Pestañas', s: 'p', href: 'sistema-diseno/componentes-estados/componentes-de-estructura.html#s-04-03-01' },
          { n: '04.03.02', t: 'Tablas, listas y contenedores', st: 'Tablas', s: 'p', href: 'sistema-diseno/componentes-estados/componentes-de-estructura.html#s-04-03-02' },
          { n: '04.03.03', t: 'Acordeones, árboles y contenido expandible', st: 'Acordeones', s: 'p', href: 'sistema-diseno/componentes-estados/componentes-de-estructura.html#s-04-03-03' } ] },
      { n: '04.04', k: '04-04', t: 'Retroalimentación', full: 'Retroalimentación y superposiciones', s: 'e', items: [
          { n: '04.04.01', t: 'Alertas, notificaciones y etiquetas de estado', st: 'Alertas', s: 'p', href: 'sistema-diseno/componentes-estados/retroalimentacion-y-superposiciones.html#s-04-04-01' },
          { n: '04.04.02', t: 'Diálogos, paneles y ventanas emergentes', st: 'Diálogos', s: 'p', href: 'sistema-diseno/componentes-estados/retroalimentacion-y-superposiciones.html#s-04-04-02' },
          { n: '04.04.03', t: 'Indicadores de progreso y carga', st: 'Indicadores de progreso', s: 'p', href: 'sistema-diseno/componentes-estados/retroalimentacion-y-superposiciones.html#s-04-04-03' } ] }
    ]
  },
  {
    id: 'pat', k: 'PAT', t: 'Patrones', full: 'Patrones de interacción', href: 'sistema-diseno/patrones-interaccion.html', color: 'noche', colorName: 'Azul Noche',
    cd: 'Componentes combinados para resolver tareas completas.',
    d: 'Define cómo se combinan los componentes para resolver tareas y procesos completos.',
    ch: [
      { n: '05.01', k: '05-01', t: 'Formularios', full: 'Formularios y validaciones', s: 'e', items: [
          { n: '05.01.01', t: 'Estructura y ayuda contextual', st: 'Estructura y ayuda', s: 'p', href: 'sistema-diseno/patrones-interaccion/formularios-y-validaciones.html#s-05-01-01' },
          { n: '05.01.02', t: 'Validación y comunicación de errores', st: 'Validación', s: 'p', href: 'sistema-diseno/patrones-interaccion/formularios-y-validaciones.html#s-05-01-02' },
          { n: '05.01.03', t: 'Formularios de múltiples pasos', st: 'Múltiples pasos', s: 'p', href: 'sistema-diseno/patrones-interaccion/formularios-y-validaciones.html#s-05-01-03' } ] },
      { n: '05.02', k: '05-02', t: 'Flujos de trabajo', full: 'Flujos de trabajo', s: 'e', items: [
          { n: '05.02.01', t: 'Creación, edición y guardado', st: 'Creación', s: 'p', href: 'sistema-diseno/patrones-interaccion/flujos-de-trabajo.html#s-05-02-01' },
          { n: '05.02.02', t: 'Eliminación y acciones masivas', st: 'Eliminación', s: 'p', href: 'sistema-diseno/patrones-interaccion/flujos-de-trabajo.html#s-05-02-02' },
          { n: '05.02.03', t: 'Borradores y continuidad de tareas', st: 'Borradores', s: 'p', href: 'sistema-diseno/patrones-interaccion/flujos-de-trabajo.html#s-05-02-03' } ] },
      { n: '05.03', k: '05-03', t: 'Recuperación', full: 'Estados y recuperación', s: 'e', items: [
          { n: '05.03.01', t: 'Estados vacíos y de espera', st: 'Estados vacíos', s: 'p', href: 'sistema-diseno/patrones-interaccion/estados-y-recuperacion.html#s-05-03-01' },
          { n: '05.03.02', t: 'Reintentos, deshacer y recuperación', st: 'Reintentos', s: 'p', href: 'sistema-diseno/patrones-interaccion/estados-y-recuperacion.html#s-05-03-02' },
          { n: '05.03.03', t: 'Errores y continuidad operativa', st: 'Errores', s: 'p', href: 'sistema-diseno/patrones-interaccion/estados-y-recuperacion.html#s-05-03-03' } ] },
      { n: '05.04', k: '05-04', t: 'Operaciones sensibles', full: 'Decisiones y operaciones sensibles', s: 'e', items: [
          { n: '05.04.01', t: 'Confirmaciones de alto impacto', st: 'Confirmaciones', s: 'p', href: 'sistema-diseno/patrones-interaccion/decisiones-y-operaciones-sensibles.html#s-05-04-01' },
          { n: '05.04.02', t: 'Permisos y autorizaciones humanas', st: 'Permisos', s: 'p', href: 'sistema-diseno/patrones-interaccion/decisiones-y-operaciones-sensibles.html#s-05-04-02' },
          { n: '05.04.03', t: 'Trazabilidad visible de acciones', st: 'Trazabilidad visible', s: 'p', href: 'sistema-diseno/patrones-interaccion/decisiones-y-operaciones-sensibles.html#s-05-04-03' } ] }
    ]
  },
  {
    id: 'acc', k: 'ACC', t: 'Accesibilidad', full: 'Accesibilidad y adaptación', href: 'sistema-diseno/accesibilidad-adaptacion.html', color: 'cielo', colorName: 'Azul Cielo',
    cd: 'Requisitos de acceso y adaptación, con WCAG 2.2 AA.',
    d: 'Establece los requisitos de accesibilidad y adaptación, tomando WCAG 2.2 nivel AA como referencia de cumplimiento.',
    ch: [
      { n: '06.01', k: '06-01', t: 'Percepción', full: 'Accesibilidad perceptiva', s: 'e', items: [
          { n: '06.01.01', t: 'Contraste y legibilidad', st: 'Contraste y legibilidad', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-perceptiva.html#s-06-01-01' },
          { n: '06.01.02', t: 'Información no dependiente del color', st: 'Sin depender del color', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-perceptiva.html#s-06-01-02' },
          { n: '06.01.03', t: 'Zoom, redistribución y espaciado de texto', st: 'Zoom y redistribución', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-perceptiva.html#s-06-01-03' } ] },
      { n: '06.02', k: '06-02', t: 'Operación', full: 'Accesibilidad operativa', s: 'e', items: [
          { n: '06.02.01', t: 'Teclado y secuencia de foco', st: 'Teclado', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-operativa.html#s-06-02-01' },
          { n: '06.02.02', t: 'Lectores de pantalla y semántica accesible', st: 'Lectores de pantalla', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-operativa.html#s-06-02-02' },
          { n: '06.02.03', t: 'Objetivos táctiles y formas de interacción', st: 'Objetivos táctiles', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-operativa.html#s-06-02-03' } ] },
      { n: '06.03', k: '06-03', t: 'Adaptación', full: 'Adaptación de la experiencia', s: 'e', items: [
          { n: '06.03.01', t: 'Diseño adaptable y dispositivos', st: 'Diseño adaptable', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/adaptacion-de-la-experiencia.html#s-06-03-01' },
          { n: '06.03.02', t: 'Preferencias del sistema y movimiento reducido', st: 'Preferencias del sistema', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/adaptacion-de-la-experiencia.html#s-06-03-02' },
          { n: '06.03.03', t: 'Diferentes capacidades y condiciones de uso', st: 'Diferentes capacidades', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/adaptacion-de-la-experiencia.html#s-06-03-03' } ] }
    ]
  },
  {
    id: 'cnt', k: 'CNT', t: 'Contenido', full: 'Contenido y comunicación', href: 'sistema-diseno/contenido-comunicacion.html', color: 'salmon', colorName: 'Salmón Tierra',
    cd: 'La voz de Keyons aplicada a los mensajes de interfaz.',
    d: 'Aplica los principios de voz y claridad a los mensajes de las interfaces.',
    ch: [
      { n: '07.01', k: '07-01', t: 'Escritura', full: 'Escritura de interfaz', s: 'e', items: [
          { n: '07.01.01', t: 'Etiquetas y llamadas a la acción', st: 'Etiquetas', s: 'p', href: 'sistema-diseno/contenido-comunicacion/escritura-de-interfaz.html#s-07-01-01' },
          { n: '07.01.02', t: 'Instrucciones y textos de ayuda', st: 'Instrucciones', s: 'p', href: 'sistema-diseno/contenido-comunicacion/escritura-de-interfaz.html#s-07-01-02' },
          { n: '07.01.03', t: 'Brevedad, claridad y consistencia verbal', st: 'Brevedad', s: 'p', href: 'sistema-diseno/contenido-comunicacion/escritura-de-interfaz.html#s-07-01-03' } ] },
      { n: '07.02', k: '07-02', t: 'Mensajes', full: 'Mensajes del sistema', s: 'e', items: [
          { n: '07.02.01', t: 'Confirmaciones y mensajes de progreso', st: 'Confirmaciones', s: 'p', href: 'sistema-diseno/contenido-comunicacion/mensajes-del-sistema.html#s-07-02-01' },
          { n: '07.02.02', t: 'Errores y acciones de recuperación', st: 'Errores', s: 'p', href: 'sistema-diseno/contenido-comunicacion/mensajes-del-sistema.html#s-07-02-02' },
          { n: '07.02.03', t: 'Advertencias, límites y estados vacíos', st: 'Advertencias', s: 'p', href: 'sistema-diseno/contenido-comunicacion/mensajes-del-sistema.html#s-07-02-03' } ] },
      { n: '07.03', k: '07-03', t: 'Localización', full: 'Lenguaje y localización', s: 'e', items: [
          { n: '07.03.01', t: 'Terminología y lenguaje técnico', st: 'Terminología', s: 'p', href: 'sistema-diseno/contenido-comunicacion/lenguaje-y-localizacion.html#s-07-03-01' },
          { n: '07.03.02', t: 'Español, inglés y adaptación regional', st: 'Idiomas y regiones', s: 'p', href: 'sistema-diseno/contenido-comunicacion/lenguaje-y-localizacion.html#s-07-03-02' },
          { n: '07.03.03', t: 'Voz y tono según identidad de producto', st: 'Voz y tono', s: 'p', href: 'sistema-diseno/contenido-comunicacion/lenguaje-y-localizacion.html#s-07-03-03' } ] }
    ]
  },
  {
    id: 'dav', k: 'DAV', t: 'Datos', full: 'Datos y visualización', href: 'sistema-diseno/datos-visualizacion.html', color: 'atardecer', colorName: 'Salmón Atardecer',
    cd: 'Información cuantitativa clara y bien interpretada.',
    d: 'Define cómo presentar información cuantitativa y operativa sin comprometer la interpretación.',
    ch: [
      { n: '08.01', k: '08-01', t: 'Tablas', full: 'Tablas y datos estructurados', s: 'e', items: [
          { n: '08.01.01', t: 'Columnas, ordenamiento y estructura', st: 'Columnas', s: 'p', href: 'sistema-diseno/datos-visualizacion/tablas-y-datos-estructurados.html#s-08-01-01' },
          { n: '08.01.02', t: 'Filtros, paginación y navegación de registros', st: 'Filtros', s: 'p', href: 'sistema-diseno/datos-visualizacion/tablas-y-datos-estructurados.html#s-08-01-02' },
          { n: '08.01.03', t: 'Densidad y adaptación de tablas', st: 'Densidad', s: 'p', href: 'sistema-diseno/datos-visualizacion/tablas-y-datos-estructurados.html#s-08-01-03' } ] },
      { n: '08.02', k: '08-02', t: 'Gráficos', full: 'Gráficos de datos', s: 'e', items: [
          { n: '08.02.01', t: 'Selección del tipo de visualización', st: 'Tipo de gráfico', s: 'p', href: 'sistema-diseno/datos-visualizacion/graficos-de-datos.html#s-08-02-01' },
          { n: '08.02.02', t: 'Paletas categóricas, secuenciales y divergentes', st: 'Paletas categóricas', s: 'p', href: 'sistema-diseno/datos-visualizacion/graficos-de-datos.html#s-08-02-02' },
          { n: '08.02.03', t: 'Escalas, leyendas y accesibilidad de gráficos', st: 'Escalas', s: 'p', href: 'sistema-diseno/datos-visualizacion/graficos-de-datos.html#s-08-02-03' } ] },
      { n: '08.03', k: '08-03', t: 'Indicadores', full: 'Indicadores y cifras', s: 'e', items: [
          { n: '08.03.01', t: 'Formatos numéricos, unidades y fechas', st: 'Formatos numéricos', s: 'p', href: 'sistema-diseno/datos-visualizacion/indicadores-y-cifras.html#s-08-03-01' },
          { n: '08.03.02', t: 'Variaciones, comparaciones y tendencias', st: 'Variaciones', s: 'p', href: 'sistema-diseno/datos-visualizacion/indicadores-y-cifras.html#s-08-03-02' },
          { n: '08.03.03', t: 'Datos ausentes, inciertos o incompletos', st: 'Datos ausentes', s: 'p', href: 'sistema-diseno/datos-visualizacion/indicadores-y-cifras.html#s-08-03-03' } ] },
      { n: '08.04', k: '08-04', t: 'Dashboards', full: 'Dashboards e informes', s: 'e', items: [
          { n: '08.04.01', t: 'Organización según tareas y decisiones', st: 'Organización', s: 'p', href: 'sistema-diseno/datos-visualizacion/dashboards-e-informes.html#s-08-04-01' },
          { n: '08.04.02', t: 'Exploración y profundización de datos', st: 'Exploración', s: 'p', href: 'sistema-diseno/datos-visualizacion/dashboards-e-informes.html#s-08-04-02' },
          { n: '08.04.03', t: 'Exportación, impresión y presentación de resultados', st: 'Exportación', s: 'p', href: 'sistema-diseno/datos-visualizacion/dashboards-e-informes.html#s-08-04-03' } ] }
    ]
  },
  {
    id: 'iae', k: 'IAE', t: 'IA y Estela', full: 'Experiencias con IA y Estela', href: 'sistema-diseno/ia-estela.html', color: 'noche', colorName: 'Azul Noche',
    cd: 'Cómo se interactúa con la IA y con Estela en los productos.',
    d: 'Define la interacción con IA. La identidad y personalidad de Estela se documentarán en el Libro de Marca; aquí se definirá cómo se aplican en productos.',
    ch: [
      { n: '09.01', k: '09-01', t: 'Principios de IA', full: 'Principios de experiencia con IA', s: 'e', items: [
          { n: '09.01.01', t: 'Transparencia de capacidades y límites', st: 'Transparencia', s: 'p', href: 'sistema-diseno/ia-estela/principios-de-experiencia-con-ia.html#s-09-01-01' },
          { n: '09.01.02', t: 'Incertidumbre, fuentes y verificación', st: 'Incertidumbre', s: 'p', href: 'sistema-diseno/ia-estela/principios-de-experiencia-con-ia.html#s-09-01-02' },
          { n: '09.01.03', t: 'Control del usuario sobre la interacción', st: 'Control del usuario', s: 'p', href: 'sistema-diseno/ia-estela/principios-de-experiencia-con-ia.html#s-09-01-03' } ] },
      { n: '09.02', k: '09-02', t: 'Conversación', full: 'Interfaz conversacional de Estela', s: 'e', items: [
          { n: '09.02.01', t: 'Aplicación de su identidad y personalidad', st: 'Identidad de Estela', s: 'p', href: 'sistema-diseno/ia-estela/interfaz-conversacional-de-estela.html#s-09-02-01' },
          { n: '09.02.02', t: 'Mensajes, referencias y archivos', st: 'Mensajes', s: 'p', href: 'sistema-diseno/ia-estela/interfaz-conversacional-de-estela.html#s-09-02-02' },
          { n: '09.02.03', t: 'Historial, contexto y continuidad conversacional', st: 'Historial', s: 'p', href: 'sistema-diseno/ia-estela/interfaz-conversacional-de-estela.html#s-09-02-03' } ] },
      { n: '09.03', k: '09-03', t: 'Agentes', full: 'Agentes y ejecución de acciones', s: 'e', items: [
          { n: '09.03.01', t: 'Orquestación y representación de agentes', st: 'Orquestación', s: 'p', href: 'sistema-diseno/ia-estela/agentes-y-ejecucion-de-acciones.html#s-09-03-01' },
          { n: '09.03.02', t: 'Planificación y visualización de acciones', st: 'Planificación', s: 'p', href: 'sistema-diseno/ia-estela/agentes-y-ejecucion-de-acciones.html#s-09-03-02' },
          { n: '09.03.03', t: 'Confirmaciones, aprobaciones y registro de ejecución', st: 'Aprobaciones y registro', s: 'p', href: 'sistema-diseno/ia-estela/agentes-y-ejecucion-de-acciones.html#s-09-03-03' } ] },
      { n: '09.04', k: '09-04', t: 'Seguridad y confianza', full: 'Seguridad y confianza en IA', s: 'e', items: [
          { n: '09.04.01', t: 'Privacidad y control de acceso', st: 'Privacidad', s: 'p', href: 'sistema-diseno/ia-estela/seguridad-y-confianza-en-ia.html#s-09-04-01' },
          { n: '09.04.02', t: 'Errores, límites y escalamiento humano', st: 'Errores', s: 'p', href: 'sistema-diseno/ia-estela/seguridad-y-confianza-en-ia.html#s-09-04-02' },
          { n: '09.04.03', t: 'Diferenciación entre acciones automáticas y humanas', st: 'Acciones automáticas', s: 'p', href: 'sistema-diseno/ia-estela/seguridad-y-confianza-en-ia.html#s-09-04-03' } ] }
    ]
  },
  {
    id: 'spr', k: 'SPR', t: 'Productos', full: 'Sistemas de producto', href: 'sistema-diseno/sistemas-producto.html', color: 'cielo', colorName: 'Azul Cielo',
    cd: 'Una base común con expresiones visuales distintas.',
    d: 'Define las diferentes aplicaciones del sistema de diseño, con fundamentos compartidos y expresiones visuales distintas.',
    ch: [
      { n: '10.01', k: '10-01', t: 'Base compartida', full: 'Base compartida', s: 'e', items: [
          { n: '10.01.01', t: 'Estándares UX comunes', st: 'Estándares UX comunes', s: 'p', href: 'sistema-diseno/sistemas-producto/base-compartida.html#s-10-01-01' },
          { n: '10.01.02', t: 'Reutilización de componentes', st: 'Reutilización', s: 'p', href: 'sistema-diseno/sistemas-producto/base-compartida.html#s-10-01-02' },
          { n: '10.01.03', t: 'Herencia y variación de temas visuales', st: 'Herencia de temas', s: 'p', href: 'sistema-diseno/sistemas-producto/base-compartida.html#s-10-01-03' } ] },
      { n: '10.02', k: '10-02', t: 'Sitio web', full: 'Sitio web corporativo Keyons', s: 'e', items: [
          { n: '10.02.01', t: 'Aplicación funcional de la identidad corporativa', st: 'Aplicación funcional', s: 'p', href: 'sistema-diseno/sistemas-producto/sitio-web-corporativo-keyons.html#s-10-02-01' },
          { n: '10.02.02', t: 'Navegación y composición web', st: 'Navegación', s: 'p', href: 'sistema-diseno/sistemas-producto/sitio-web-corporativo-keyons.html#s-10-02-02' },
          { n: '10.02.03', t: 'Interacciones y acciones públicas', st: 'Interacciones', s: 'p', href: 'sistema-diseno/sistemas-producto/sitio-web-corporativo-keyons.html#s-10-02-03' } ] },
      { n: '10.03', k: '10-03', t: 'Herramientas internas', full: 'Herramientas internas Keyons', s: 'e', items: [
          { n: '10.03.01', t: 'Identidad visual operativa Keyons', st: 'Identidad visual', s: 'p', href: 'sistema-diseno/sistemas-producto/herramientas-internas-keyons.html#s-10-03-01' },
          { n: '10.03.02', t: 'Navegación por roles y tareas', st: 'Navegación por roles', s: 'p', href: 'sistema-diseno/sistemas-producto/herramientas-internas-keyons.html#s-10-03-02' },
          { n: '10.03.03', t: 'Densidad informativa y espacios de trabajo', st: 'Densidad informativa', s: 'p', href: 'sistema-diseno/sistemas-producto/herramientas-internas-keyons.html#s-10-03-03' } ] },
      { n: '10.04', k: '10-04', t: 'Product Default', full: 'Keyons Product Default', s: 'e', items: [
          { n: '10.04.01', t: 'Estética neutral premium', st: 'Estética neutral premium', s: 'p', href: 'sistema-diseno/sistemas-producto/keyons-product-default.html#s-10-04-01' },
          { n: '10.04.02', t: 'Estructura base de aplicaciones SaaS', st: 'Estructura base', s: 'p', href: 'sistema-diseno/sistemas-producto/keyons-product-default.html#s-10-04-02' },
          { n: '10.04.03', t: 'Opciones de configuración y personalización', st: 'Configuración', s: 'p', href: 'sistema-diseno/sistemas-producto/keyons-product-default.html#s-10-04-03' } ] },
      { n: '10.05', k: '10-05', t: 'White-label', full: 'Soluciones personalizadas y white-label', s: 'e', items: [
          { n: '10.05.01', t: 'Aplicación de identidades de clientes', st: 'Identidades de clientes', s: 'p', href: 'sistema-diseno/sistemas-producto/soluciones-personalizadas-y-white-label.html#s-10-05-01' },
          { n: '10.05.02', t: 'Marca blanca sin firma visual del proveedor', st: 'Marca blanca', s: 'p', href: 'sistema-diseno/sistemas-producto/soluciones-personalizadas-y-white-label.html#s-10-05-02' },
          { n: '10.05.03', t: 'Límites de personalización y consistencia funcional', st: 'Límites', s: 'p', href: 'sistema-diseno/sistemas-producto/soluciones-personalizadas-y-white-label.html#s-10-05-03' } ] }
    ]
  },
  {
    id: 'mov', k: 'MOV', t: 'Movimiento', full: 'Movimiento e interacción sensorial', href: 'sistema-diseno/movimiento-sensorial.html', color: 'salmon', colorName: 'Salmón Tierra',
    cd: 'Movimiento y recursos sensoriales con un propósito claro.',
    d: 'Regula el movimiento y los recursos sensoriales, sin convertirlos en requisitos decorativos.',
    ch: [
      { n: '11.01', k: '11-01', t: 'Movimiento operativo', full: 'Movimiento operativo', s: 'e', items: [
          { n: '11.01.01', t: 'Transiciones funcionales', st: 'Transiciones funcionales', s: 'p', href: 'sistema-diseno/movimiento-sensorial/movimiento-operativo.html#s-11-01-01' },
          { n: '11.01.02', t: 'Retroalimentación y progreso', st: 'Retroalimentación', s: 'p', href: 'sistema-diseno/movimiento-sensorial/movimiento-operativo.html#s-11-01-02' },
          { n: '11.01.03', t: 'Interrupciones y límites del movimiento', st: 'Interrupciones', s: 'p', href: 'sistema-diseno/movimiento-sensorial/movimiento-operativo.html#s-11-01-03' } ] },
      { n: '11.02', k: '11-02', t: 'Movimiento editorial', full: 'Movimiento editorial', s: 'e', items: [
          { n: '11.02.01', t: 'Entradas y cambios de escena', st: 'Entradas', s: 'p', href: 'sistema-diseno/movimiento-sensorial/movimiento-editorial.html#s-11-02-01' },
          { n: '11.02.02', t: 'Movimiento atmosférico y expresivo', st: 'Movimiento atmosférico', s: 'p', href: 'sistema-diseno/movimiento-sensorial/movimiento-editorial.html#s-11-02-02' },
          { n: '11.02.03', t: 'Intensidad y adaptación al contexto', st: 'Intensidad', s: 'p', href: 'sistema-diseno/movimiento-sensorial/movimiento-editorial.html#s-11-02-03' } ] },
      { n: '11.03', k: '11-03', t: 'Multisensorial', full: 'Interacción multisensorial', s: 'e', items: [
          { n: '11.03.01', t: 'Sonido y control de reproducción', st: 'Sonido', s: 'p', href: 'sistema-diseno/movimiento-sensorial/interaccion-multisensorial.html#s-11-03-01' },
          { n: '11.03.02', t: 'Respuesta háptica', st: 'Respuesta háptica', s: 'p', href: 'sistema-diseno/movimiento-sensorial/interaccion-multisensorial.html#s-11-03-02' },
          { n: '11.03.03', t: 'Atajos de teclado y convenciones del sistema operativo', st: 'Atajos de teclado', s: 'p', href: 'sistema-diseno/movimiento-sensorial/interaccion-multisensorial.html#s-11-03-03' } ] }
    ]
  },
  {
    id: 'gob', k: 'GOB', t: 'Gobierno', full: 'Calidad y gobierno del diseño', href: 'sistema-diseno/calidad-gobierno.html', color: 'atardecer', colorName: 'Salmón Atardecer',
    cd: 'Cómo se gestionan, implementan y prueban las normas.',
    d: 'Establece cómo se gestionan, implementan, prueban y mantienen las reglas del Sistema de Diseño.',
    ch: [
      { n: '12.01', k: '12-01', t: 'Gobierno normativo', full: 'Gobierno normativo', s: 'e', items: [
          { n: '12.01.01', t: 'Propiedad y fuente oficial de cada norma', st: 'Propiedad', s: 'p', href: 'sistema-diseno/calidad-gobierno/gobierno-normativo.html#s-12-01-01' },
          { n: '12.01.02', t: 'Identificadores y referencias permanentes', st: 'Identificadores', s: 'p', href: 'sistema-diseno/calidad-gobierno/gobierno-normativo.html#s-12-01-02' },
          { n: '12.01.03', t: 'Aprobación, cambios y descontinuación', st: 'Aprobación', s: 'p', href: 'sistema-diseno/calidad-gobierno/gobierno-normativo.html#s-12-01-03' } ] },
      { n: '12.02', k: '12-02', t: 'Implementación', full: 'Implementación técnica', s: 'e', items: [
          { n: '12.02.01', t: 'Traducción de tokens y componentes a código', st: 'Traducción de tokens', s: 'p', href: 'sistema-diseno/calidad-gobierno/implementacion-tecnica.html#s-12-02-01' },
          { n: '12.02.02', t: 'Especificaciones para desarrollo', st: 'Especificaciones', s: 'p', href: 'sistema-diseno/calidad-gobierno/implementacion-tecnica.html#s-12-02-02' },
          { n: '12.02.03', t: 'Compatibilidad, mantenimiento y versiones', st: 'Compatibilidad', s: 'p', href: 'sistema-diseno/calidad-gobierno/implementacion-tecnica.html#s-12-02-03' } ] },
      { n: '12.03', k: '12-03', t: 'Validación', full: 'Validación de calidad', s: 'e', items: [
          { n: '12.03.01', t: 'Verificación visual y funcional', st: 'Verificación visual', s: 'p', href: 'sistema-diseno/calidad-gobierno/validacion-de-calidad.html#s-12-03-01' },
          { n: '12.03.02', t: 'Pruebas de usabilidad por perfiles y tareas', st: 'Pruebas de usabilidad', s: 'p', href: 'sistema-diseno/calidad-gobierno/validacion-de-calidad.html#s-12-03-02' },
          { n: '12.03.03', t: 'Verificación de accesibilidad y regresiones', st: 'Regresiones', s: 'p', href: 'sistema-diseno/calidad-gobierno/validacion-de-calidad.html#s-12-03-03' } ] },
      { n: '12.04', k: '12-04', t: 'Documentación', full: 'Documentación y consulta', s: 'e', items: [
          { n: '12.04.01', t: 'Catálogo y relaciones entre normas', st: 'Catálogo', s: 'p', href: 'sistema-diseno/calidad-gobierno/documentacion-y-consulta.html#s-12-04-01' },
          { n: '12.04.02', t: 'Exportación para personas y sistemas de IA', st: 'Exportación para IA', s: 'p', href: 'sistema-diseno/calidad-gobierno/documentacion-y-consulta.html#s-12-04-02' },
          { n: '12.04.03', t: 'Consulta autorizada y permisos documentales', st: 'Consulta autorizada', s: 'p', href: 'sistema-diseno/calidad-gobierno/documentacion-y-consulta.html#s-12-04-03' } ] }
    ]
  }
];
