/* ═══════════════════════════════════════════════════════════════
   KEYONS · MAPA DEL SISTEMA DE DISEÑO
   Segundo libro de la Biblioteca. Usa el mismo código que el Libro de
   Marca (js/libro.js); este archivo reemplaza a js/nav-data.js en sus páginas.
   Un área con doce módulos. Cada módulo es un capítulo con una página.
   s: 'v' vigente · 'b' borrador · 'p' por definir (valor por defecto)
   k: clave estable del módulo; también es su código provisional de normas.
   Para agregar una norma: una sección <section class="ed" id="..."> en la
   página del módulo y un ítem aquí con href 'sistema-diseno/modulo.html#id'.
   ═══════════════════════════════════════════════════════════════ */
window.KEYONS_BOOK = {
  home: 'sistema-diseno/index.html',
  menu: 'chapters',
  menuLabel: 'Módulos del Sistema de Diseño',
  alt: [['Libro de Marca', 'inicio.html'], ['Cómo se documenta una norma', 'sistema-diseno/plantilla.html']]
};

window.KEYONS_NAV = [
  {
    id: 'sd', t: 'Sistema de Diseño', full: 'Módulos del Sistema de Diseño', href: 'sistema-diseno/modulos.html', color: 'noche', colorName: 'Azul Noche',
    d: 'UX, UI, componentes, patrones, accesibilidad e interfaces de producto.',
    ch: [
      { n: '01', k: 'PEX', t: 'Principios de experiencia', s: 'p', d: 'Los criterios que orientan cada decisión de experiencia en los productos Keyons.', items: [
        { t: 'Principios de experiencia', st: 'Alcance', s: 'b', href: 'sistema-diseno/principios-experiencia.html' } ] },
      { n: '02', k: 'ARQ', t: 'Arquitectura y navegación', s: 'p', d: 'La organización de la información, los recorridos y la navegación de cada producto.', items: [
        { t: 'Arquitectura y navegación', st: 'Alcance', s: 'b', href: 'sistema-diseno/arquitectura-navegacion.html' } ] },
      { n: '03', k: 'FUI', t: 'Fundamentos de interfaz', s: 'p', d: 'Color, tipografía, espacio, forma e iconografía aplicados a la interfaz mediante tokens.', items: [
        { t: 'Fundamentos de interfaz', st: 'Alcance', s: 'b', href: 'sistema-diseno/fundamentos-interfaz.html' } ] },
      { n: '04', k: 'CPE', t: 'Componentes y estados', s: 'p', d: 'Los componentes de interfaz, sus variantes y cada uno de sus estados.', items: [
        { t: 'Componentes y estados', st: 'Alcance', s: 'b', href: 'sistema-diseno/componentes-estados.html' } ] },
      { n: '05', k: 'PAT', t: 'Patrones de interacción', s: 'p', d: 'Soluciones recurrentes para tareas completas: formularios, búsquedas, flujos y estados vacíos.', items: [
        { t: 'Patrones de interacción', st: 'Alcance', s: 'b', href: 'sistema-diseno/patrones-interaccion.html' } ] },
      { n: '06', k: 'ACC', t: 'Accesibilidad y adaptación', s: 'p', d: 'Lo que cada interfaz necesita para funcionar con distintas capacidades, dispositivos y contextos.', items: [
        { t: 'Accesibilidad y adaptación', st: 'Alcance', s: 'b', href: 'sistema-diseno/accesibilidad-adaptacion.html' } ] },
      { n: '07', k: 'CNT', t: 'Contenido y comunicación', s: 'p', d: 'La escritura de la interfaz: etiquetas, instrucciones, mensajes y errores.', items: [
        { t: 'Contenido y comunicación', st: 'Alcance', s: 'b', href: 'sistema-diseno/contenido-comunicacion.html' } ] },
      { n: '08', k: 'DAV', t: 'Datos y visualización', s: 'p', d: 'Tablas, tableros y gráficos dentro de los productos.', items: [
        { t: 'Datos y visualización', st: 'Alcance', s: 'b', href: 'sistema-diseno/datos-visualizacion.html' } ] },
      { n: '09', k: 'IAE', t: 'Experiencias con IA y Estela', s: 'p', d: 'La interacción con inteligencia artificial y con Estela: conversación, confianza y control humano.', items: [
        { t: 'Experiencias con IA y Estela', st: 'Alcance', s: 'b', href: 'sistema-diseno/ia-estela.html' } ] },
      { n: '10', k: 'SPR', t: 'Sistemas de producto', s: 'p', d: 'Cómo se aplica el sistema en cada contexto de interfaz y hasta dónde llega la personalización.', items: [
        { t: 'Sistemas de producto', st: 'Alcance', s: 'b', href: 'sistema-diseno/sistemas-producto.html' } ] },
      { n: '11', k: 'MOV', t: 'Movimiento e interacción sensorial', s: 'p', d: 'Movimiento, transiciones y respuesta sensorial de la interfaz.', items: [
        { t: 'Movimiento e interacción sensorial', st: 'Alcance', s: 'b', href: 'sistema-diseno/movimiento-sensorial.html' } ] },
      { n: '12', k: 'GOB', t: 'Calidad y gobierno del diseño', s: 'p', d: 'Revisión, aprobación, versiones y mantenimiento de las normas del sistema.', items: [
        { t: 'Calidad y gobierno del diseño', st: 'Alcance', s: 'b', href: 'sistema-diseno/calidad-gobierno.html' } ] }
    ]
  }
];
