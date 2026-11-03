/* ═══════════════════════════════════════════════════════════════
   KEYONS · MAPA DEL SISTEMA DE DISEÑO
   Generado por tools/sistema_diseno.py desde data/sistema-diseno.json.
   No se edita a mano: se cambia el JSON y se vuelve a generar.
   Libro → módulo → capítulo → subcapítulo → norma. Los números son
   ubicación documental; los códigos de norma son permanentes y aparte.
   ═══════════════════════════════════════════════════════════════ */
window.KEYONS_BOOK = {
  home: 'sistema-diseno/index.html',
  menu: 'chapters',
  menuLabel: 'Módulos del Sistema de Diseño',
  alt: [['Libro de Marca', 'inicio.html', 'right'], ['Plantilla de norma', 'sistema-diseno/plantilla.html', 'code']],
  status: { p: 'Contenido pendiente' },
  legend: ['e', 'p', 'b', 'r', 'v', 'd'],
  words: { ch: 'Módulos', pg: 'Capítulos', pgs: 'capítulos' }
};

window.KEYONS_NAV = [
  {
    id: 'sd', t: 'Sistema de Diseño', full: 'Módulos del Sistema de Diseño', href: 'sistema-diseno/modulos.html', color: 'noche', colorName: 'Azul Noche',
    d: 'Doce módulos, 45 capítulos y 135 subcapítulos: la estructura donde se desarrollan las normas de UX y UI de Keyons.',
    ch: [
      { n: '01', k: 'PEX', t: 'Principios de experiencia', s: 'e', color: 'noche', d: 'Define los principios de calidad de experiencia compartidos por las herramientas internas y los productos para clientes.', items: [
        { n: '01', idx: true, t: 'Índice del módulo', st: 'Índice del módulo', s: 'e', href: 'sistema-diseno/principios-experiencia.html' },
        { n: '01.01', t: 'Principios compartidos', s: 'e', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html' },
        { n: '01.02', t: 'Personas y contextos de uso', s: 'e', href: 'sistema-diseno/principios-experiencia/personas-y-contextos-de-uso.html' },
        { n: '01.03', t: 'Decisiones verificables de experiencia', s: 'e', href: 'sistema-diseno/principios-experiencia/decisiones-verificables-de-experiencia.html' } ] },
      { n: '02', k: 'ARQ', t: 'Arquitectura y navegación', s: 'e', color: 'cielo', d: 'Establece cómo se organiza la información y cómo las personas se desplazan por las aplicaciones.', items: [
        { n: '02', idx: true, t: 'Índice del módulo', st: 'Índice del módulo', s: 'e', href: 'sistema-diseno/arquitectura-navegacion.html' },
        { n: '02.01', t: 'Arquitectura de información', s: 'e', href: 'sistema-diseno/arquitectura-navegacion/arquitectura-de-informacion.html' },
        { n: '02.02', t: 'Estructura de navegación', s: 'e', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html' },
        { n: '02.03', t: 'Búsqueda y orientación', s: 'e', href: 'sistema-diseno/arquitectura-navegacion/busqueda-y-orientacion.html' } ] },
      { n: '03', k: 'FUI', t: 'Fundamentos de interfaz', s: 'e', color: 'salmon', d: 'Traduce los fundamentos visuales de Marca a reglas técnicas y visuales aplicables a interfaces.', items: [
        { n: '03', idx: true, t: 'Índice del módulo', st: 'Índice del módulo', s: 'e', href: 'sistema-diseno/fundamentos-interfaz.html' },
        { n: '03.01', t: 'Tokens de diseño', s: 'e', href: 'sistema-diseno/fundamentos-interfaz/tokens-de-diseno.html' },
        { n: '03.02', t: 'Color funcional', s: 'e', href: 'sistema-diseno/fundamentos-interfaz/color-funcional.html' },
        { n: '03.03', t: 'Tipografía aplicada', s: 'e', href: 'sistema-diseno/fundamentos-interfaz/tipografia-aplicada.html' },
        { n: '03.04', t: 'Espacio, retícula y geometría', s: 'e', href: 'sistema-diseno/fundamentos-interfaz/espacio-reticula-y-geometria.html' },
        { n: '03.05', t: 'Recursos visuales de interfaz', s: 'e', href: 'sistema-diseno/fundamentos-interfaz/recursos-visuales-de-interfaz.html' } ] },
      { n: '04', k: 'CPE', t: 'Componentes y estados', s: 'e', color: 'atardecer', d: 'Define los componentes reutilizables y sus variantes. Aquí se documentan las piezas, mientras que los flujos completos pertenecen a Patrones de interacción.', items: [
        { n: '04', idx: true, t: 'Índice del módulo', st: 'Índice del módulo', s: 'e', href: 'sistema-diseno/componentes-estados.html' },
        { n: '04.01', t: 'Componentes de acción', s: 'e', href: 'sistema-diseno/componentes-estados/componentes-de-accion.html' },
        { n: '04.02', t: 'Controles de entrada', s: 'e', href: 'sistema-diseno/componentes-estados/controles-de-entrada.html' },
        { n: '04.03', t: 'Componentes de estructura', s: 'e', href: 'sistema-diseno/componentes-estados/componentes-de-estructura.html' },
        { n: '04.04', t: 'Retroalimentación y superposiciones', s: 'e', href: 'sistema-diseno/componentes-estados/retroalimentacion-y-superposiciones.html' } ] },
      { n: '05', k: 'PAT', t: 'Patrones de interacción', s: 'e', color: 'noche', d: 'Define cómo se combinan los componentes para resolver tareas y procesos completos.', items: [
        { n: '05', idx: true, t: 'Índice del módulo', st: 'Índice del módulo', s: 'e', href: 'sistema-diseno/patrones-interaccion.html' },
        { n: '05.01', t: 'Formularios y validaciones', s: 'e', href: 'sistema-diseno/patrones-interaccion/formularios-y-validaciones.html' },
        { n: '05.02', t: 'Flujos de trabajo', s: 'e', href: 'sistema-diseno/patrones-interaccion/flujos-de-trabajo.html' },
        { n: '05.03', t: 'Estados y recuperación', s: 'e', href: 'sistema-diseno/patrones-interaccion/estados-y-recuperacion.html' },
        { n: '05.04', t: 'Decisiones y operaciones sensibles', s: 'e', href: 'sistema-diseno/patrones-interaccion/decisiones-y-operaciones-sensibles.html' } ] },
      { n: '06', k: 'ACC', t: 'Accesibilidad y adaptación', s: 'e', color: 'cielo', d: 'Establece los requisitos de accesibilidad y adaptación, tomando WCAG 2.2 nivel AA como referencia de cumplimiento.', items: [
        { n: '06', idx: true, t: 'Índice del módulo', st: 'Índice del módulo', s: 'e', href: 'sistema-diseno/accesibilidad-adaptacion.html' },
        { n: '06.01', t: 'Accesibilidad perceptiva', s: 'e', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-perceptiva.html' },
        { n: '06.02', t: 'Accesibilidad operativa', s: 'e', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-operativa.html' },
        { n: '06.03', t: 'Adaptación de la experiencia', s: 'e', href: 'sistema-diseno/accesibilidad-adaptacion/adaptacion-de-la-experiencia.html' } ] },
      { n: '07', k: 'CNT', t: 'Contenido y comunicación', s: 'e', color: 'salmon', d: 'Aplica los principios de voz y claridad a los mensajes de las interfaces.', items: [
        { n: '07', idx: true, t: 'Índice del módulo', st: 'Índice del módulo', s: 'e', href: 'sistema-diseno/contenido-comunicacion.html' },
        { n: '07.01', t: 'Escritura de interfaz', s: 'e', href: 'sistema-diseno/contenido-comunicacion/escritura-de-interfaz.html' },
        { n: '07.02', t: 'Mensajes del sistema', s: 'e', href: 'sistema-diseno/contenido-comunicacion/mensajes-del-sistema.html' },
        { n: '07.03', t: 'Lenguaje y localización', s: 'e', href: 'sistema-diseno/contenido-comunicacion/lenguaje-y-localizacion.html' } ] },
      { n: '08', k: 'DAV', t: 'Datos y visualización', s: 'e', color: 'atardecer', d: 'Define cómo presentar información cuantitativa y operativa sin comprometer la interpretación.', items: [
        { n: '08', idx: true, t: 'Índice del módulo', st: 'Índice del módulo', s: 'e', href: 'sistema-diseno/datos-visualizacion.html' },
        { n: '08.01', t: 'Tablas y datos estructurados', s: 'e', href: 'sistema-diseno/datos-visualizacion/tablas-y-datos-estructurados.html' },
        { n: '08.02', t: 'Gráficos de datos', s: 'e', href: 'sistema-diseno/datos-visualizacion/graficos-de-datos.html' },
        { n: '08.03', t: 'Indicadores y cifras', s: 'e', href: 'sistema-diseno/datos-visualizacion/indicadores-y-cifras.html' },
        { n: '08.04', t: 'Dashboards e informes', s: 'e', href: 'sistema-diseno/datos-visualizacion/dashboards-e-informes.html' } ] },
      { n: '09', k: 'IAE', t: 'Experiencias con IA y Estela', s: 'e', color: 'noche', d: 'Define la interacción con IA. La identidad y personalidad de Estela se documentarán en el Libro de Marca; aquí se definirá cómo se aplican en productos.', items: [
        { n: '09', idx: true, t: 'Índice del módulo', st: 'Índice del módulo', s: 'e', href: 'sistema-diseno/ia-estela.html' },
        { n: '09.01', t: 'Principios de experiencia con IA', s: 'e', href: 'sistema-diseno/ia-estela/principios-de-experiencia-con-ia.html' },
        { n: '09.02', t: 'Interfaz conversacional de Estela', s: 'e', href: 'sistema-diseno/ia-estela/interfaz-conversacional-de-estela.html' },
        { n: '09.03', t: 'Agentes y ejecución de acciones', s: 'e', href: 'sistema-diseno/ia-estela/agentes-y-ejecucion-de-acciones.html' },
        { n: '09.04', t: 'Seguridad y confianza en IA', s: 'e', href: 'sistema-diseno/ia-estela/seguridad-y-confianza-en-ia.html' } ] },
      { n: '10', k: 'SPR', t: 'Sistemas de producto', s: 'e', color: 'cielo', d: 'Define las diferentes aplicaciones del sistema de diseño, con fundamentos compartidos y expresiones visuales distintas.', items: [
        { n: '10', idx: true, t: 'Índice del módulo', st: 'Índice del módulo', s: 'e', href: 'sistema-diseno/sistemas-producto.html' },
        { n: '10.01', t: 'Base compartida', s: 'e', href: 'sistema-diseno/sistemas-producto/base-compartida.html' },
        { n: '10.02', t: 'Sitio web corporativo Keyons', s: 'e', href: 'sistema-diseno/sistemas-producto/sitio-web-corporativo-keyons.html' },
        { n: '10.03', t: 'Herramientas internas Keyons', s: 'e', href: 'sistema-diseno/sistemas-producto/herramientas-internas-keyons.html' },
        { n: '10.04', t: 'Keyons Product Default', s: 'e', href: 'sistema-diseno/sistemas-producto/keyons-product-default.html' },
        { n: '10.05', t: 'Soluciones personalizadas y white-label', s: 'e', href: 'sistema-diseno/sistemas-producto/soluciones-personalizadas-y-white-label.html' } ] },
      { n: '11', k: 'MOV', t: 'Movimiento e interacción sensorial', s: 'e', color: 'salmon', d: 'Regula el movimiento y los recursos sensoriales, sin convertirlos en requisitos decorativos.', items: [
        { n: '11', idx: true, t: 'Índice del módulo', st: 'Índice del módulo', s: 'e', href: 'sistema-diseno/movimiento-sensorial.html' },
        { n: '11.01', t: 'Movimiento operativo', s: 'e', href: 'sistema-diseno/movimiento-sensorial/movimiento-operativo.html' },
        { n: '11.02', t: 'Movimiento editorial', s: 'e', href: 'sistema-diseno/movimiento-sensorial/movimiento-editorial.html' },
        { n: '11.03', t: 'Interacción multisensorial', s: 'e', href: 'sistema-diseno/movimiento-sensorial/interaccion-multisensorial.html' } ] },
      { n: '12', k: 'GOB', t: 'Calidad y gobierno del diseño', s: 'e', color: 'atardecer', d: 'Establece cómo se gestionan, implementan, prueban y mantienen las reglas del Sistema de Diseño.', items: [
        { n: '12', idx: true, t: 'Índice del módulo', st: 'Índice del módulo', s: 'e', href: 'sistema-diseno/calidad-gobierno.html' },
        { n: '12.01', t: 'Gobierno normativo', s: 'e', href: 'sistema-diseno/calidad-gobierno/gobierno-normativo.html' },
        { n: '12.02', t: 'Implementación técnica', s: 'e', href: 'sistema-diseno/calidad-gobierno/implementacion-tecnica.html' },
        { n: '12.03', t: 'Validación de calidad', s: 'e', href: 'sistema-diseno/calidad-gobierno/validacion-de-calidad.html' },
        { n: '12.04', t: 'Documentación y consulta', s: 'e', href: 'sistema-diseno/calidad-gobierno/documentacion-y-consulta.html' } ] }
    ]
  }
];
