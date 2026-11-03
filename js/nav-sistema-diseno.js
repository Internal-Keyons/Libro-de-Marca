/* ═══════════════════════════════════════════════════════════════
   KEYONS · MAPA DEL SISTEMA DE DISEÑO
   Segundo libro de la Biblioteca. Usa el mismo código que el Libro de
   Marca (js/libro.js); este archivo reemplaza a js/nav-data.js en sus páginas.
   Un área con doce módulos. Cada módulo es un capítulo con una página y sus secciones.
   s: 'v' vigente · 'b' borrador · 'p' por definir (valor por defecto)
   k: clave estable del módulo; también es su código provisional de normas.
   Para agregar una norma: una sección <section class="ed" id="..."> en la
   página del módulo y un ítem aquí con href 'sistema-diseno/modulo.html#id'.
   ═══════════════════════════════════════════════════════════════ */
window.KEYONS_BOOK = {
  home: 'sistema-diseno/index.html',
  menu: 'chapters',
  menuLabel: 'Módulos del Sistema de Diseño',
  alt: [['Libro de Marca', 'inicio.html', 'right'], ['Plantilla de norma', 'sistema-diseno/plantilla.html', 'code']]
};

window.KEYONS_NAV = [
  {
    id: 'sd', t: 'Sistema de Diseño', full: 'Módulos del Sistema de Diseño', href: 'sistema-diseno/modulos.html', color: 'noche', colorName: 'Azul Noche',
    d: 'UX, UI, componentes, patrones, accesibilidad e interfaces de producto.',
    ch: [
      { n: '01', k: 'PEX', t: 'Principios de experiencia', s: 'p', d: 'Los criterios que orientan cada decisión de experiencia en los productos Keyons.', items: [
        { t: 'Normas del módulo', st: 'Normas', s: 'p', href: 'sistema-diseno/principios-experiencia.html#normas' }, { t: 'Normas de marca que aplica', st: 'Libro de Marca', s: 'b', href: 'sistema-diseno/principios-experiencia.html#marca' } ] },
      { n: '02', k: 'ARQ', t: 'Arquitectura y navegación', s: 'p', d: 'La organización de la información, los recorridos y la navegación de cada producto.', items: [
        { t: 'Normas del módulo', st: 'Normas', s: 'p', href: 'sistema-diseno/arquitectura-navegacion.html#normas' }, { t: 'Normas de marca que aplica', st: 'Libro de Marca', s: 'b', href: 'sistema-diseno/arquitectura-navegacion.html#marca' } ] },
      { n: '03', k: 'FUI', t: 'Fundamentos de interfaz', s: 'p', d: 'Color, tipografía, espacio, forma e iconografía aplicados a la interfaz mediante tokens.', items: [
        { t: 'Normas del módulo', st: 'Normas', s: 'p', href: 'sistema-diseno/fundamentos-interfaz.html#normas' }, { t: 'Normas de marca que aplica', st: 'Libro de Marca', s: 'b', href: 'sistema-diseno/fundamentos-interfaz.html#marca' } ] },
      { n: '04', k: 'CPE', t: 'Componentes y estados', s: 'p', d: 'Los componentes de interfaz, sus variantes y cada uno de sus estados.', items: [
        { t: 'Normas del módulo', st: 'Normas', s: 'p', href: 'sistema-diseno/componentes-estados.html#normas' }, { t: 'Normas de marca que aplica', st: 'Libro de Marca', s: 'b', href: 'sistema-diseno/componentes-estados.html#marca' } ] },
      { n: '05', k: 'PAT', t: 'Patrones de interacción', s: 'p', d: 'Soluciones recurrentes para tareas completas: formularios, búsquedas, flujos y estados vacíos.', items: [
        { t: 'Normas del módulo', st: 'Normas', s: 'p', href: 'sistema-diseno/patrones-interaccion.html#normas' }, { t: 'Normas de marca que aplica', st: 'Libro de Marca', s: 'b', href: 'sistema-diseno/patrones-interaccion.html#marca' } ] },
      { n: '06', k: 'ACC', t: 'Accesibilidad y adaptación', s: 'p', d: 'Lo que cada interfaz necesita para funcionar con distintas capacidades, dispositivos y contextos.', items: [
        { t: 'Normas del módulo', st: 'Normas', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion.html#normas' }, { t: 'Normas de marca que aplica', st: 'Libro de Marca', s: 'b', href: 'sistema-diseno/accesibilidad-adaptacion.html#marca' } ] },
      { n: '07', k: 'CNT', t: 'Contenido y comunicación', s: 'p', d: 'La escritura de la interfaz: etiquetas, instrucciones, mensajes y errores.', items: [
        { t: 'Normas del módulo', st: 'Normas', s: 'p', href: 'sistema-diseno/contenido-comunicacion.html#normas' }, { t: 'Normas de marca que aplica', st: 'Libro de Marca', s: 'b', href: 'sistema-diseno/contenido-comunicacion.html#marca' } ] },
      { n: '08', k: 'DAV', t: 'Datos y visualización', s: 'p', d: 'Tablas, tableros y gráficos dentro de los productos.', items: [
        { t: 'Normas del módulo', st: 'Normas', s: 'p', href: 'sistema-diseno/datos-visualizacion.html#normas' }, { t: 'Normas de marca que aplica', st: 'Libro de Marca', s: 'b', href: 'sistema-diseno/datos-visualizacion.html#marca' } ] },
      { n: '09', k: 'IAE', t: 'Experiencias con IA y Estela', s: 'p', d: 'La interacción con inteligencia artificial y con Estela: conversación, confianza y control humano.', items: [
        { t: 'Normas del módulo', st: 'Normas', s: 'p', href: 'sistema-diseno/ia-estela.html#normas' }, { t: 'Normas de marca que aplica', st: 'Libro de Marca', s: 'b', href: 'sistema-diseno/ia-estela.html#marca' } ] },
      { n: '10', k: 'SPR', t: 'Sistemas de producto', s: 'p', d: 'Cómo se aplica el sistema en cada contexto de interfaz y hasta dónde llega la personalización.', items: [
        { t: 'Normas del módulo', st: 'Normas', s: 'p', href: 'sistema-diseno/sistemas-producto.html#normas' }, { t: 'Normas de marca que aplica', st: 'Libro de Marca', s: 'b', href: 'sistema-diseno/sistemas-producto.html#marca' } ] },
      { n: '11', k: 'MOV', t: 'Movimiento e interacción sensorial', s: 'p', d: 'Movimiento, transiciones y respuesta sensorial de la interfaz.', items: [
        { t: 'Normas del módulo', st: 'Normas', s: 'p', href: 'sistema-diseno/movimiento-sensorial.html#normas' }, { t: 'Normas de marca que aplica', st: 'Libro de Marca', s: 'b', href: 'sistema-diseno/movimiento-sensorial.html#marca' } ] },
      { n: '12', k: 'GOB', t: 'Calidad y gobierno del diseño', s: 'p', d: 'Revisión, aprobación, versiones y mantenimiento de las normas del sistema.', items: [
        { t: 'Normas del módulo', st: 'Normas', s: 'p', href: 'sistema-diseno/calidad-gobierno.html#normas' }, { t: 'Normas de marca que aplica', st: 'Libro de Marca', s: 'b', href: 'sistema-diseno/calidad-gobierno.html#marca' } ] }
    ]
  }
];
