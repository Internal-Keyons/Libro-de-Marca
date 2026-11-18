/* ═══════════════════════════════════════════════════════════════
   KEYONS · MAPA DEL SISTEMA DE DISEÑO
   Generado por tools/sistema_diseno.py desde data/sistema-diseno.json.
   No se edita a mano: se cambia el JSON y se vuelve a generar.
   Cada módulo es un área, como en el Libro de Marca: t es el nombre corto
   (menú, tarjeta, lateral) y full el título completo (página de área).
   Capítulos numerados del 01 al 45 en todo el libro; k conserva la clave
   interna (anclas #cap-01-01). Los códigos de norma van aparte.
   ═══════════════════════════════════════════════════════════════ */
window.KEYONS_BOOK = {
  id: 'sistema-diseno',
  home: 'sistema-diseno/index.html',
  alt: [['Descargar PDF', 'documental/sistema-diseno-keyons.pdf', 'down', true], ['Normas para IA', 'ia/sistema-diseno.md', 'code']],
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
      { n: '01', k: '01-01', t: 'Principios comunes', full: 'Principios comunes', d: 'Los principios que rigen el diseño de todos los productos digitales de Keyons: SaaS de nicho, herramientas internas y desarrollos a medida.', s: 'b', items: [
          { t: 'La tarea primero', st: 'La tarea primero', s: 'b', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html#s-01-01-01' },
          { t: 'Claridad primero', st: 'Claridad primero', s: 'b', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html#s-01-01-02' },
          { t: 'Complejidad', st: 'Complejidad', s: 'b', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html#s-01-01-03' },
          { t: 'Estado comprensible', st: 'Estado comprensible', s: 'b', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html#s-01-01-04' },
          { t: 'Previsibilidad', st: 'Previsibilidad', s: 'b', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html#s-01-01-05' },
          { t: 'Contexto previo', st: 'Contexto previo', s: 'b', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html#s-01-01-06' },
          { t: 'Prevención de errores', st: 'Prevención de errores', s: 'b', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html#s-01-01-07' },
          { t: 'Control de la persona', st: 'Control de la persona', s: 'b', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html#s-01-01-08' },
          { t: 'Reconocer', st: 'Reconocer', s: 'b', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html#s-01-01-09' } ] },
      { n: '02', k: '01-02', t: 'Personas y contextos', full: 'Personas y contextos de uso', d: 'Quién usa cada producto, para qué tarea, con qué frecuencia y con cuánta carga.', s: 'b', items: [
          { t: 'Personas reales', st: 'Personas reales', s: 'b', href: 'sistema-diseno/principios-experiencia/personas-y-contextos-de-uso.html#s-01-02-01' },
          { t: 'Roles y permisos', st: 'Roles y permisos', s: 'b', href: 'sistema-diseno/principios-experiencia/personas-y-contextos-de-uso.html#s-01-02-02' },
          { t: 'Frecuencia de uso', st: 'Frecuencia de uso', s: 'b', href: 'sistema-diseno/principios-experiencia/personas-y-contextos-de-uso.html#s-01-02-03' } ] },
      { n: '03', k: '01-03', t: 'Elecciones verificadas', full: 'Decisiones verificables de experiencia', d: 'Hipótesis, criterios de aceptación e indicadores para medir la experiencia.', s: 'b', items: [
          { t: 'Decisiones', st: 'Decisiones', s: 'b', href: 'sistema-diseno/principios-experiencia/decisiones-verificables-de-experiencia.html#s-01-03-01' },
          { t: 'Prisma', st: 'Prisma', s: 'b', href: 'sistema-diseno/principios-experiencia/decisiones-verificables-de-experiencia.html#s-01-03-02' },
          { t: 'Diseño por capas', st: 'Diseño por capas', s: 'b', href: 'sistema-diseno/principios-experiencia/decisiones-verificables-de-experiencia.html#s-01-03-03' },
          { t: 'Resultados', st: 'Resultados', s: 'b', href: 'sistema-diseno/principios-experiencia/decisiones-verificables-de-experiencia.html#s-01-03-04' },
          { t: 'Evidencia', st: 'Evidencia', s: 'b', href: 'sistema-diseno/principios-experiencia/decisiones-verificables-de-experiencia.html#s-01-03-05' },
          { t: 'Evaluación posterior', st: 'Evaluación posterior', s: 'b', href: 'sistema-diseno/principios-experiencia/decisiones-verificables-de-experiencia.html#s-01-03-06' } ] }
    ]
  },
  {
    id: 'arq', k: 'ARQ', t: 'Arquitectura', full: 'Arquitectura y navegación', href: 'sistema-diseno/arquitectura-navegacion.html', color: 'cielo', colorName: 'Azul Cielo',
    cd: 'Cómo se organiza la información y cómo se recorre.',
    d: 'Establece cómo se organiza la información y cómo las personas se desplazan por las aplicaciones.',
    ch: [
      { n: '04', k: '02-01', t: 'Información', full: 'Arquitectura de información', d: 'Mapas de contenido, taxonomías y relaciones entre la información.', s: 'b', items: [
          { t: 'Organización', st: 'Organización', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/arquitectura-de-informacion.html#s-02-01-01' },
          { t: 'Nombres', st: 'Nombres', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/arquitectura-de-informacion.html#s-02-01-02' },
          { t: 'Jerarquía identificable', st: 'Jerarquía identificable', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/arquitectura-de-informacion.html#s-02-01-03' },
          { t: 'Detalle a pedido', st: 'Detalle a pedido', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/arquitectura-de-informacion.html#s-02-01-04' } ] },
      { n: '05', k: '02-02', t: 'Navegación', full: 'Estructura de navegación', d: 'Cómo se reconoce la ubicación, se recorren los destinos y se retoma el trabajo, en cualquier forma de navegación.', s: 'b', items: [
          { t: 'Ubicación actual', st: 'Ubicación actual', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html#s-02-02-01' },
          { t: 'Acciones previsibles', st: 'Acciones previsibles', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html#s-02-02-02' },
          { t: 'Navegación visible', st: 'Navegación visible', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html#s-02-02-03' },
          { t: 'Controles', st: 'Controles', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html#s-02-02-04' },
          { t: 'Adaptación', st: 'Adaptación', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html#s-02-02-05' },
          { t: 'Regreso sin pérdida', st: 'Regreso sin pérdida', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html#s-02-02-06' },
          { t: 'Acceso directo', st: 'Acceso directo', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html#s-02-02-07' } ] },
      { n: '06', k: '02-03', t: 'Búsqueda', full: 'Búsqueda y orientación', d: 'Búsqueda, filtros y orientación sobre dónde se está y cómo continuar.', s: 'b', items: [
          { t: 'Alcance identificable', st: 'Alcance identificable', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/busqueda-y-orientacion.html#s-02-03-01' },
          { t: 'Pertinencia', st: 'Pertinencia', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/busqueda-y-orientacion.html#s-02-03-02' },
          { t: 'Resultados claros', st: 'Resultados claros', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/busqueda-y-orientacion.html#s-02-03-03' },
          { t: 'Filtros visibles', st: 'Filtros visibles', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/busqueda-y-orientacion.html#s-02-03-04' },
          { t: 'Sin resultados', st: 'Sin resultados', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/busqueda-y-orientacion.html#s-02-03-05' },
          { t: 'Permisos', st: 'Permisos', s: 'b', href: 'sistema-diseno/arquitectura-navegacion/busqueda-y-orientacion.html#s-02-03-06' } ] }
    ]
  },
  {
    id: 'fui', k: 'FUI', t: 'Fundamentos', full: 'Fundamentos de interfaz', href: 'sistema-diseno/fundamentos-interfaz.html', color: 'salmon', colorName: 'Salmón Tierra',
    cd: 'Los fundamentos de Marca convertidos en reglas de interfaz.',
    d: 'Traduce los fundamentos visuales de Marca a reglas técnicas y visuales aplicables a interfaces.',
    ch: [
      { n: '07', k: '03-01', t: 'Tokens', full: 'Tokens de diseño', d: 'Tokens base, semánticos y de componente; nomenclatura, temas y versiones.', s: 'b', items: [
          { t: 'Fuente única', st: 'Fuente única', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/tokens-de-diseno.html#s-03-01-01' },
          { t: 'Roles semánticos', st: 'Roles semánticos', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/tokens-de-diseno.html#s-03-01-02' },
          { t: 'Cambios controlados', st: 'Cambios controlados', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/tokens-de-diseno.html#s-03-01-03' } ] },
      { n: '08', k: '03-02', t: 'Color funcional', full: 'Color funcional', d: 'Superficies, texto, bordes, interacción, foco, estados y contraste.', s: 'b', items: [
          { t: 'Color con función', st: 'Color con función', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/color-funcional.html#s-03-02-01' },
          { t: 'Estados', st: 'Estados', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/color-funcional.html#s-03-02-02' },
          { t: 'Significados', st: 'Significados', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/color-funcional.html#s-03-02-03' },
          { t: 'Contraste', st: 'Contraste', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/color-funcional.html#s-03-02-04' } ] },
      { n: '09', k: '03-03', t: 'Tipografía', full: 'Tipografía aplicada', d: 'Familias oficiales aplicadas a interfaz: jerarquías, escalas y cifras.', s: 'b', items: [
          { t: 'Sistema tipográfico', st: 'Sistema tipográfico', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/tipografia-aplicada.html#s-03-03-01' },
          { t: 'Jerarquía', st: 'Jerarquía', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/tipografia-aplicada.html#s-03-03-02' },
          { t: 'Legibilidad', st: 'Legibilidad', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/tipografia-aplicada.html#s-03-03-03' },
          { t: 'Truncamiento', st: 'Truncamiento', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/tipografia-aplicada.html#s-03-03-04' } ] },
      { n: '10', k: '03-04', t: 'Espacio y retícula', full: 'Espacio, retícula y geometría', d: 'Retículas, puntos de adaptación, espaciado, densidad y esquinas.', s: 'b', items: [
          { t: 'Espaciado', st: 'Espaciado', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/espacio-reticula-y-geometria.html#s-03-04-01' },
          { t: 'Agrupación', st: 'Agrupación', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/espacio-reticula-y-geometria.html#s-03-04-02' },
          { t: 'Adaptación', st: 'Adaptación', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/espacio-reticula-y-geometria.html#s-03-04-03' } ] },
      { n: '11', k: '03-05', t: 'Recursos visuales', full: 'Recursos visuales de interfaz', d: 'Iconografía funcional, bordes, sombras, elevación e imágenes aplicadas.', s: 'b', items: [
          { t: 'Íconos', st: 'Íconos', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/recursos-visuales-de-interfaz.html#s-03-05-01' },
          { t: 'Identidad', st: 'Identidad', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/recursos-visuales-de-interfaz.html#s-03-05-02' },
          { t: 'Expresión', st: 'Expresión', s: 'b', href: 'sistema-diseno/fundamentos-interfaz/recursos-visuales-de-interfaz.html#s-03-05-03' } ] }
    ]
  },
  {
    id: 'cpe', k: 'CPE', t: 'Componentes', full: 'Componentes y estados', href: 'sistema-diseno/componentes-estados.html', color: 'atardecer', colorName: 'Salmón Atardecer',
    cd: 'Piezas reutilizables, sus variantes y sus estados.',
    d: 'Define los componentes reutilizables y sus variantes. Aquí se documentan las piezas, mientras que los flujos completos pertenecen a Patrones de interacción.',
    ch: [
      { n: '12', k: '04-01', t: 'Acciones', full: 'Componentes de acción', d: 'Botones, enlaces, menús y sus estados de disponibilidad y proceso.', s: 'b', items: [
          { t: 'Jerarquía', st: 'Jerarquía', s: 'b', href: 'sistema-diseno/componentes-estados/componentes-de-accion.html#s-04-01-01' },
          { t: 'Estados', st: 'Estados', s: 'b', href: 'sistema-diseno/componentes-estados/componentes-de-accion.html#s-04-01-02' },
          { t: 'Destructivas', st: 'Destructivas', s: 'b', href: 'sistema-diseno/componentes-estados/componentes-de-accion.html#s-04-01-03' },
          { t: 'Menú de acciones', st: 'Menú de acciones', s: 'b', href: 'sistema-diseno/componentes-estados/componentes-de-accion.html#s-04-01-04' } ] },
      { n: '13', k: '04-02', t: 'Entradas', full: 'Controles de entrada', d: 'Campos, selectores, casillas, interruptores, fechas y archivos.', s: 'b', items: [
          { t: 'Etiquetas', st: 'Etiquetas', s: 'b', href: 'sistema-diseno/componentes-estados/controles-de-entrada.html#s-04-02-01' },
          { t: 'Validación', st: 'Validación', s: 'b', href: 'sistema-diseno/componentes-estados/controles-de-entrada.html#s-04-02-02' },
          { t: 'Control apropiado', st: 'Control apropiado', s: 'b', href: 'sistema-diseno/componentes-estados/controles-de-entrada.html#s-04-02-03' } ] },
      { n: '14', k: '04-03', t: 'Estructura', full: 'Componentes de estructura', d: 'Pestañas, tablas, listas, contenedores y contenido expandible.', s: 'b', items: [
          { t: 'Contenedores', st: 'Contenedores', s: 'b', href: 'sistema-diseno/componentes-estados/componentes-de-estructura.html#s-04-03-01' },
          { t: 'Jerarquía', st: 'Jerarquía', s: 'b', href: 'sistema-diseno/componentes-estados/componentes-de-estructura.html#s-04-03-02' },
          { t: 'Diálogos', st: 'Diálogos', s: 'b', href: 'sistema-diseno/componentes-estados/componentes-de-estructura.html#s-04-03-03' } ] },
      { n: '15', k: '04-04', t: 'Retroalimentación', full: 'Retroalimentación y superposiciones', d: 'Alertas, etiquetas de estado, diálogos, paneles e indicadores de carga.', s: 'b', items: [
          { t: 'Resultado', st: 'Resultado', s: 'b', href: 'sistema-diseno/componentes-estados/retroalimentacion-y-superposiciones.html#s-04-04-01' },
          { t: 'Mensajes', st: 'Mensajes', s: 'b', href: 'sistema-diseno/componentes-estados/retroalimentacion-y-superposiciones.html#s-04-04-02' },
          { t: 'Atención', st: 'Atención', s: 'b', href: 'sistema-diseno/componentes-estados/retroalimentacion-y-superposiciones.html#s-04-04-03' } ] }
    ]
  },
  {
    id: 'pat', k: 'PAT', t: 'Patrones', full: 'Patrones de interacción', href: 'sistema-diseno/patrones-interaccion.html', color: 'noche', colorName: 'Azul Noche',
    cd: 'Componentes combinados para resolver tareas completas.',
    d: 'Define cómo se combinan los componentes para resolver tareas y procesos completos.',
    ch: [
      { n: '16', k: '05-01', t: 'Formularios', full: 'Formularios y validaciones', d: 'Estructura, ayuda contextual, validación y formularios de varios pasos.', s: 'b', items: [
          { t: 'Flujo', st: 'Flujo', s: 'b', href: 'sistema-diseno/patrones-interaccion/formularios-y-validaciones.html#s-05-01-01' },
          { t: 'Sin pérdidas', st: 'Sin pérdidas', s: 'b', href: 'sistema-diseno/patrones-interaccion/formularios-y-validaciones.html#s-05-01-02' },
          { t: 'Validación', st: 'Validación', s: 'b', href: 'sistema-diseno/patrones-interaccion/formularios-y-validaciones.html#s-05-01-03' } ] },
      { n: '17', k: '05-02', t: 'Flujos de trabajo', full: 'Flujos de trabajo', d: 'Crear, editar, guardar, eliminar y continuar tareas sin perder trabajo.', s: 'b', items: [
          { t: 'Progreso', st: 'Progreso', s: 'b', href: 'sistema-diseno/patrones-interaccion/flujos-de-trabajo.html#s-05-02-01' },
          { t: 'Contexto', st: 'Contexto', s: 'b', href: 'sistema-diseno/patrones-interaccion/flujos-de-trabajo.html#s-05-02-02' },
          { t: 'Terminación', st: 'Terminación', s: 'b', href: 'sistema-diseno/patrones-interaccion/flujos-de-trabajo.html#s-05-02-03' } ] },
      { n: '18', k: '05-03', t: 'Recuperación', full: 'Estados y recuperación', d: 'Estados vacíos y de espera, reintentos, deshacer y errores.', s: 'b', items: [
          { t: 'Ruta de salida', st: 'Ruta de salida', s: 'b', href: 'sistema-diseno/patrones-interaccion/estados-y-recuperacion.html#s-05-03-01' },
          { t: 'Deshacer', st: 'Deshacer', s: 'b', href: 'sistema-diseno/patrones-interaccion/estados-y-recuperacion.html#s-05-03-02' },
          { t: 'Persistencia', st: 'Persistencia', s: 'b', href: 'sistema-diseno/patrones-interaccion/estados-y-recuperacion.html#s-05-03-03' },
          { t: 'Vacíos y esperas', st: 'Vacíos y esperas', s: 'b', href: 'sistema-diseno/patrones-interaccion/estados-y-recuperacion.html#s-05-03-04' } ] },
      { n: '19', k: '05-04', t: 'Procesos críticos', full: 'Decisiones y operaciones sensibles', d: 'Confirmaciones de alto impacto, permisos y trazabilidad de acciones.', s: 'b', items: [
          { t: 'Autorización', st: 'Autorización', s: 'b', href: 'sistema-diseno/patrones-interaccion/decisiones-y-operaciones-sensibles.html#s-05-04-01' },
          { t: 'Trazabilidad', st: 'Trazabilidad', s: 'b', href: 'sistema-diseno/patrones-interaccion/decisiones-y-operaciones-sensibles.html#s-05-04-02' } ] }
    ]
  },
  {
    id: 'acc', k: 'ACC', t: 'Accesibilidad', full: 'Accesibilidad y adaptación', href: 'sistema-diseno/accesibilidad-adaptacion.html', color: 'cielo', colorName: 'Azul Cielo',
    cd: 'Requisitos de acceso y adaptación, con WCAG 2.2 AA.',
    d: 'Establece los requisitos de accesibilidad y adaptación, tomando WCAG 2.2 nivel AA como referencia de cumplimiento.',
    ch: [
      { n: '20', k: '06-01', t: 'Percepción', full: 'Accesibilidad perceptiva', d: 'Contraste, información más allá del color, zoom y espaciado de texto.', s: 'b', items: [
          { t: 'Conformidad', st: 'Conformidad', s: 'b', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-perceptiva.html#s-06-01-01' },
          { t: 'Perceptible', st: 'Perceptible', s: 'b', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-perceptiva.html#s-06-01-02' },
          { t: 'Lectura adaptable', st: 'Lectura adaptable', s: 'b', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-perceptiva.html#s-06-01-03' } ] },
      { n: '21', k: '06-02', t: 'Operación', full: 'Accesibilidad operativa', d: 'Teclado, foco, lectores de pantalla y objetivos táctiles.', s: 'b', items: [
          { t: 'Teclado', st: 'Teclado', s: 'b', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-operativa.html#s-06-02-01' },
          { t: 'Foco', st: 'Foco', s: 'b', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-operativa.html#s-06-02-02' },
          { t: 'Tiempo y movimiento', st: 'Tiempo y movimiento', s: 'b', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-operativa.html#s-06-02-03' } ] },
      { n: '22', k: '06-03', t: 'Adaptación', full: 'Adaptación de la experiencia', d: 'Dispositivos, preferencias del sistema y distintas capacidades de uso.', s: 'b', items: [
          { t: 'Diseño adaptable', st: 'Diseño adaptable', s: 'b', href: 'sistema-diseno/accesibilidad-adaptacion/adaptacion-de-la-experiencia.html#s-06-03-01' },
          { t: 'Objetivos', st: 'Objetivos', s: 'b', href: 'sistema-diseno/accesibilidad-adaptacion/adaptacion-de-la-experiencia.html#s-06-03-02' },
          { t: 'Variaciones', st: 'Variaciones', s: 'b', href: 'sistema-diseno/accesibilidad-adaptacion/adaptacion-de-la-experiencia.html#s-06-03-03' } ] }
    ]
  },
  {
    id: 'cnt', k: 'CNT', t: 'Contenido', full: 'Contenido y comunicación', href: 'sistema-diseno/contenido-comunicacion.html', color: 'salmon', colorName: 'Salmón Tierra',
    cd: 'La voz de Keyons aplicada a los mensajes de interfaz.',
    d: 'Aplica los principios de voz y claridad a los mensajes de las interfaces.',
    ch: [
      { n: '23', k: '07-01', t: 'Escritura', full: 'Escritura de interfaz', d: 'Etiquetas, llamadas a la acción, instrucciones y textos de ayuda.', s: 'b', items: [
          { t: 'Lenguaje funcional', st: 'Lenguaje funcional', s: 'b', href: 'sistema-diseno/contenido-comunicacion/escritura-de-interfaz.html#s-07-01-01' },
          { t: 'Consistencia', st: 'Consistencia', s: 'b', href: 'sistema-diseno/contenido-comunicacion/escritura-de-interfaz.html#s-07-01-02' },
          { t: 'Brevedad', st: 'Brevedad', s: 'b', href: 'sistema-diseno/contenido-comunicacion/escritura-de-interfaz.html#s-07-01-03' } ] },
      { n: '24', k: '07-02', t: 'Mensajes', full: 'Mensajes del sistema', d: 'Confirmaciones, progreso, errores, advertencias y estados vacíos.', s: 'b', items: [
          { t: 'Errores', st: 'Errores', s: 'b', href: 'sistema-diseno/contenido-comunicacion/mensajes-del-sistema.html#s-07-02-01' },
          { t: 'Confirmaciones', st: 'Confirmaciones', s: 'b', href: 'sistema-diseno/contenido-comunicacion/mensajes-del-sistema.html#s-07-02-02' },
          { t: 'Seguridad', st: 'Seguridad', s: 'b', href: 'sistema-diseno/contenido-comunicacion/mensajes-del-sistema.html#s-07-02-03' } ] },
      { n: '25', k: '07-03', t: 'Localización', full: 'Lenguaje y localización', d: 'Terminología, idiomas, adaptación regional y tono de cada producto.', s: 'b', items: [
          { t: 'Lenguaje', st: 'Lenguaje', s: 'b', href: 'sistema-diseno/contenido-comunicacion/lenguaje-y-localizacion.html#s-07-03-01' },
          { t: 'Traducción', st: 'Traducción', s: 'b', href: 'sistema-diseno/contenido-comunicacion/lenguaje-y-localizacion.html#s-07-03-02' },
          { t: 'Espacio variable', st: 'Espacio variable', s: 'b', href: 'sistema-diseno/contenido-comunicacion/lenguaje-y-localizacion.html#s-07-03-03' } ] }
    ]
  },
  {
    id: 'dav', k: 'DAV', t: 'Datos', full: 'Datos y visualización', href: 'sistema-diseno/datos-visualizacion.html', color: 'atardecer', colorName: 'Salmón Atardecer',
    cd: 'Información cuantitativa clara y bien interpretada.',
    d: 'Define cómo presentar información cuantitativa y operativa sin comprometer la interpretación.',
    ch: [
      { n: '26', k: '08-01', t: 'Tablas', full: 'Tablas y datos estructurados', d: 'Columnas, orden, filtros, paginación y densidad de tablas.', s: 'b', items: [
          { t: 'Lectura', st: 'Lectura', s: 'b', href: 'sistema-diseno/datos-visualizacion/tablas-y-datos-estructurados.html#s-08-01-01' },
          { t: 'Herramientas', st: 'Herramientas', s: 'b', href: 'sistema-diseno/datos-visualizacion/tablas-y-datos-estructurados.html#s-08-01-02' },
          { t: 'Acciones', st: 'Acciones', s: 'b', href: 'sistema-diseno/datos-visualizacion/tablas-y-datos-estructurados.html#s-08-01-03' } ] },
      { n: '27', k: '08-02', t: 'Gráficos', full: 'Gráficos de datos', d: 'Tipo de gráfico, paletas, escalas, leyendas y accesibilidad.', s: 'b', items: [
          { t: 'Representación', st: 'Representación', s: 'b', href: 'sistema-diseno/datos-visualizacion/graficos-de-datos.html#s-08-02-01' },
          { t: 'Color de datos', st: 'Color de datos', s: 'b', href: 'sistema-diseno/datos-visualizacion/graficos-de-datos.html#s-08-02-02' },
          { t: 'Interpretación', st: 'Interpretación', s: 'b', href: 'sistema-diseno/datos-visualizacion/graficos-de-datos.html#s-08-02-03' } ] },
      { n: '28', k: '08-03', t: 'Indicadores', full: 'Indicadores y cifras', d: 'Formatos numéricos, unidades, variaciones y datos incompletos.', s: 'b', items: [
          { t: 'Contexto', st: 'Contexto', s: 'b', href: 'sistema-diseno/datos-visualizacion/indicadores-y-cifras.html#s-08-03-01' },
          { t: 'Umbrales', st: 'Umbrales', s: 'b', href: 'sistema-diseno/datos-visualizacion/indicadores-y-cifras.html#s-08-03-02' },
          { t: 'Actualización', st: 'Actualización', s: 'b', href: 'sistema-diseno/datos-visualizacion/indicadores-y-cifras.html#s-08-03-03' } ] },
      { n: '29', k: '08-04', t: 'Dashboards', full: 'Dashboards e informes', d: 'Tableros organizados por tareas, exploración y exportación de resultados.', s: 'b', items: [
          { t: 'Por tarea', st: 'Por tarea', s: 'b', href: 'sistema-diseno/datos-visualizacion/dashboards-e-informes.html#s-08-04-01' },
          { t: 'Jerarquía', st: 'Jerarquía', s: 'b', href: 'sistema-diseno/datos-visualizacion/dashboards-e-informes.html#s-08-04-02' },
          { t: 'Profundidad', st: 'Profundidad', s: 'b', href: 'sistema-diseno/datos-visualizacion/dashboards-e-informes.html#s-08-04-03' } ] }
    ]
  },
  {
    id: 'iae', k: 'IAE', t: 'IA y Estela', full: 'Experiencias con IA y Estela', href: 'sistema-diseno/ia-estela.html', color: 'noche', colorName: 'Azul Noche',
    cd: 'Cómo se interactúa con la IA y con Estela en los productos.',
    d: 'Define la interacción con IA. La identidad y personalidad de Estela se documentarán en el Libro de Marca; aquí se definirá cómo se aplican en productos.',
    ch: [
      { n: '30', k: '09-01', t: 'Principios de IA', full: 'Principios de experiencia con IA', d: 'Capacidades, límites, fuentes y control del usuario frente a la IA.', s: 'b', items: [
          { t: 'Transparencia', st: 'Transparencia', s: 'b', href: 'sistema-diseno/ia-estela/principios-de-experiencia-con-ia.html#s-09-01-01' },
          { t: 'Incertidumbre', st: 'Incertidumbre', s: 'b', href: 'sistema-diseno/ia-estela/principios-de-experiencia-con-ia.html#s-09-01-02' },
          { t: 'Control humano', st: 'Control humano', s: 'b', href: 'sistema-diseno/ia-estela/principios-de-experiencia-con-ia.html#s-09-01-03' } ] },
      { n: '31', k: '09-02', t: 'Conversación', full: 'Interfaz conversacional de Estela', d: 'Cómo se aplica Estela en la conversación: mensajes, archivos e historial.', s: 'b', items: [
          { t: 'Contexto', st: 'Contexto', s: 'b', href: 'sistema-diseno/ia-estela/interfaz-conversacional-de-estela.html#s-09-02-01' },
          { t: 'Preguntas', st: 'Preguntas', s: 'b', href: 'sistema-diseno/ia-estela/interfaz-conversacional-de-estela.html#s-09-02-02' },
          { t: 'Respuesta', st: 'Respuesta', s: 'b', href: 'sistema-diseno/ia-estela/interfaz-conversacional-de-estela.html#s-09-02-03' } ] },
      { n: '32', k: '09-03', t: 'Agentes', full: 'Agentes y ejecución de acciones', d: 'Agentes, planificación, aprobaciones y registro de cada ejecución.', s: 'b', items: [
          { t: 'Responsabilidad', st: 'Responsabilidad', s: 'b', href: 'sistema-diseno/ia-estela/agentes-y-ejecucion-de-acciones.html#s-09-03-01' },
          { t: 'Límites', st: 'Límites', s: 'b', href: 'sistema-diseno/ia-estela/agentes-y-ejecucion-de-acciones.html#s-09-03-02' },
          { t: 'Identidad', st: 'Identidad', s: 'b', href: 'sistema-diseno/ia-estela/agentes-y-ejecucion-de-acciones.html#s-09-03-03' } ] },
      { n: '33', k: '09-04', t: 'Confianza segura', full: 'Seguridad y confianza en IA', d: 'Privacidad, acceso, escalamiento humano y acciones automáticas visibles.', s: 'b', items: [
          { t: 'Confianza', st: 'Confianza', s: 'b', href: 'sistema-diseno/ia-estela/seguridad-y-confianza-en-ia.html#s-09-04-01' },
          { t: 'Verificación', st: 'Verificación', s: 'b', href: 'sistema-diseno/ia-estela/seguridad-y-confianza-en-ia.html#s-09-04-02' },
          { t: 'Privacidad', st: 'Privacidad', s: 'b', href: 'sistema-diseno/ia-estela/seguridad-y-confianza-en-ia.html#s-09-04-03' } ] }
    ]
  },
  {
    id: 'spr', k: 'SPR', t: 'Productos', full: 'Sistemas de producto', href: 'sistema-diseno/sistemas-producto.html', color: 'cielo', colorName: 'Azul Cielo',
    cd: 'Una base común con expresiones visuales distintas.',
    d: 'Define las diferentes aplicaciones del sistema de diseño, con fundamentos compartidos y expresiones visuales distintas.',
    ch: [
      { n: '34', k: '10-01', t: 'Base compartida', full: 'Base compartida', d: 'Estándares UX comunes, componentes reutilizables y herencia de temas.', s: 'b', items: [
          { t: 'Infraestructura', st: 'Infraestructura', s: 'b', href: 'sistema-diseno/sistemas-producto/base-compartida.html#s-10-01-01' },
          { t: 'Variaciones', st: 'Variaciones', s: 'b', href: 'sistema-diseno/sistemas-producto/base-compartida.html#s-10-01-02' },
          { t: 'Compatibilidad', st: 'Compatibilidad', s: 'b', href: 'sistema-diseno/sistemas-producto/base-compartida.html#s-10-01-03' } ] },
      { n: '35', k: '10-02', t: 'Sitio web', full: 'Sitio web corporativo Keyons', d: 'La identidad corporativa en el sitio web: navegación, composición y acciones.', s: 'b', items: [
          { t: 'Navegación', st: 'Navegación', s: 'b', href: 'sistema-diseno/sistemas-producto/sitio-web-corporativo-keyons.html#s-10-02-01' },
          { t: 'Interacción', st: 'Interacción', s: 'b', href: 'sistema-diseno/sistemas-producto/sitio-web-corporativo-keyons.html#s-10-02-02' } ] },
      { n: '36', k: '10-03', t: 'Herramientas', full: 'Herramientas internas Keyons', d: 'Identidad operativa, navegación por roles y espacios de trabajo densos.', s: 'b', items: [
          { t: 'Eficiencia', st: 'Eficiencia', s: 'b', href: 'sistema-diseno/sistemas-producto/herramientas-internas-keyons.html#s-10-03-01' },
          { t: 'Permisos', st: 'Permisos', s: 'b', href: 'sistema-diseno/sistemas-producto/herramientas-internas-keyons.html#s-10-03-02' } ] },
      { n: '37', k: '10-04', t: 'Product Default', full: 'Keyons Product Default', d: 'Estética neutral premium, estructura SaaS y opciones de configuración.', s: 'b', items: [
          { t: 'Predeterminada', st: 'Predeterminada', s: 'b', href: 'sistema-diseno/sistemas-producto/keyons-product-default.html#s-10-04-01' },
          { t: 'Sobriedad', st: 'Sobriedad', s: 'b', href: 'sistema-diseno/sistemas-producto/keyons-product-default.html#s-10-04-02' },
          { t: 'Personalización', st: 'Personalización', s: 'b', href: 'sistema-diseno/sistemas-producto/keyons-product-default.html#s-10-04-03' },
          { t: 'Navegación', st: 'Navegación', s: 'b', href: 'sistema-diseno/sistemas-producto/keyons-product-default.html#s-10-04-04' } ] },
      { n: '38', k: '10-05', t: 'White-label', full: 'Soluciones personalizadas y white-label', d: 'Identidades de clientes, marca blanca y límites de personalización.', s: 'b', items: [
          { t: 'Identidad', st: 'Identidad', s: 'b', href: 'sistema-diseno/sistemas-producto/soluciones-personalizadas-y-white-label.html#s-10-05-01' },
          { t: 'Calidad', st: 'Calidad', s: 'b', href: 'sistema-diseno/sistemas-producto/soluciones-personalizadas-y-white-label.html#s-10-05-02' },
          { t: 'Sin firma', st: 'Sin firma', s: 'b', href: 'sistema-diseno/sistemas-producto/soluciones-personalizadas-y-white-label.html#s-10-05-03' } ] }
    ]
  },
  {
    id: 'mov', k: 'MOV', t: 'Movimiento', full: 'Movimiento e interacción sensorial', href: 'sistema-diseno/movimiento-sensorial.html', color: 'salmon', colorName: 'Salmón Tierra',
    cd: 'Movimiento y recursos sensoriales con un propósito claro.',
    d: 'Regula el movimiento y los recursos sensoriales, sin convertirlos en requisitos decorativos.',
    ch: [
      { n: '39', k: '11-01', t: 'Operación activa', full: 'Movimiento operativo', d: 'Transiciones funcionales, retroalimentación, progreso y sus límites.', s: 'b', items: [
          { t: 'Funcional', st: 'Funcional', s: 'b', href: 'sistema-diseno/movimiento-sensorial/movimiento-operativo.html#s-11-01-01' },
          { t: 'Duración', st: 'Duración', s: 'b', href: 'sistema-diseno/movimiento-sensorial/movimiento-operativo.html#s-11-01-02' } ] },
      { n: '40', k: '11-02', t: 'Movimiento editorial', full: 'Movimiento editorial', d: 'Entradas, cambios de escena y movimiento atmosférico según el contexto.', s: 'b', items: [
          { t: 'Expresión', st: 'Expresión', s: 'b', href: 'sistema-diseno/movimiento-sensorial/movimiento-editorial.html#s-11-02-01' },
          { t: 'Comprensión', st: 'Comprensión', s: 'b', href: 'sistema-diseno/movimiento-sensorial/movimiento-editorial.html#s-11-02-02' } ] },
      { n: '41', k: '11-03', t: 'Multisensorial', full: 'Interacción multisensorial', d: 'Sonido, respuesta háptica y atajos del sistema operativo.', s: 'b', items: [
          { t: 'Sonido', st: 'Sonido', s: 'b', href: 'sistema-diseno/movimiento-sensorial/interaccion-multisensorial.html#s-11-03-01' },
          { t: 'Háptica', st: 'Háptica', s: 'b', href: 'sistema-diseno/movimiento-sensorial/interaccion-multisensorial.html#s-11-03-02' },
          { t: 'Alternativas', st: 'Alternativas', s: 'b', href: 'sistema-diseno/movimiento-sensorial/interaccion-multisensorial.html#s-11-03-03' } ] }
    ]
  },
  {
    id: 'gob', k: 'GOB', t: 'Gobierno', full: 'Calidad y gobierno del diseño', href: 'sistema-diseno/calidad-gobierno.html', color: 'atardecer', colorName: 'Salmón Atardecer',
    cd: 'Cómo se gestionan, implementan y prueban las normas.',
    d: 'Establece cómo se gestionan, implementan, prueban y mantienen las reglas del Sistema de Diseño.',
    ch: [
      { n: '42', k: '12-01', t: 'Gobierno normativo', full: 'Gobierno normativo', d: 'Fuente oficial, identificadores permanentes, aprobación y cambios.', s: 'b', items: [
          { t: 'Fuente única', st: 'Fuente única', s: 'b', href: 'sistema-diseno/calidad-gobierno/gobierno-normativo.html#s-12-01-01' },
          { t: 'Estado', st: 'Estado', s: 'b', href: 'sistema-diseno/calidad-gobierno/gobierno-normativo.html#s-12-01-02' } ] },
      { n: '43', k: '12-02', t: 'Implementación', full: 'Implementación técnica', d: 'Tokens y componentes en código, especificaciones y versiones.', s: 'b', items: [
          { t: 'Canónicos', st: 'Canónicos', s: 'b', href: 'sistema-diseno/calidad-gobierno/implementacion-tecnica.html#s-12-02-01' },
          { t: 'Excepciones', st: 'Excepciones', s: 'b', href: 'sistema-diseno/calidad-gobierno/implementacion-tecnica.html#s-12-02-02' },
          { t: 'Entrega', st: 'Entrega', s: 'b', href: 'sistema-diseno/calidad-gobierno/implementacion-tecnica.html#s-12-02-03' } ] },
      { n: '44', k: '12-03', t: 'Validación', full: 'Validación de calidad', d: 'Verificación visual, funcional, de usabilidad y de accesibilidad.', s: 'b', items: [
          { t: 'Tareas reales', st: 'Tareas reales', s: 'b', href: 'sistema-diseno/calidad-gobierno/validacion-de-calidad.html#s-12-03-01' },
          { t: 'Problemas críticos', st: 'Problemas críticos', s: 'b', href: 'sistema-diseno/calidad-gobierno/validacion-de-calidad.html#s-12-03-02' },
          { t: 'Protocolo', st: 'Protocolo', s: 'b', href: 'sistema-diseno/calidad-gobierno/validacion-de-calidad.html#s-12-03-03' } ] },
      { n: '45', k: '12-04', t: 'Documentación', full: 'Documentación y consulta', d: 'Catálogo de normas, exportación para personas e IA y permisos.', s: 'b', items: [
          { t: 'Componentes', st: 'Componentes', s: 'b', href: 'sistema-diseno/calidad-gobierno/documentacion-y-consulta.html#s-12-04-01' },
          { t: 'Ejemplos', st: 'Ejemplos', s: 'b', href: 'sistema-diseno/calidad-gobierno/documentacion-y-consulta.html#s-12-04-02' },
          { t: 'Versionado', st: 'Versionado', s: 'b', href: 'sistema-diseno/calidad-gobierno/documentacion-y-consulta.html#s-12-04-03' } ] }
    ]
  }
];
