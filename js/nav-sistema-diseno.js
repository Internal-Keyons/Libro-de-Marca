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
      { n: '01', k: '01-01', t: 'Principios comunes', full: 'Principios comunes', d: 'Cinco principios que rigen el diseño de todos los productos digitales de Keyons: SaaS de nicho, herramientas internas y desarrollos a medida. Son la base de los demás capítulos de este libro.', s: 'b', items: [
          { t: 'Claridad', st: 'Claridad', s: 'b', href: 'sistema-diseno/principios-experiencia/principios-compartidos.html#s-01-01-01' },
          { t: 'Coherencia', st: 'Coherencia', s: 'p' },
          { t: 'Control', st: 'Control', s: 'p' },
          { t: 'Diseño honesto', st: 'Diseño honesto', s: 'p' },
          { t: 'Firma UX', st: 'Firma UX', s: 'p' } ] },
      { n: '02', k: '01-02', t: 'Personas y contextos', full: 'Personas y contextos de uso', d: 'Quién usa cada producto, para qué tarea, con qué frecuencia y con cuánta carga.', s: 'p', items: [
          { t: 'Roles y capacidades', st: 'Roles y capacidades', s: 'p', href: 'sistema-diseno/principios-experiencia/personas-y-contextos-de-uso.html#s-01-02-01' },
          { t: 'Objetivos y tareas', st: 'Objetivos y tareas', s: 'p', href: 'sistema-diseno/principios-experiencia/personas-y-contextos-de-uso.html#s-01-02-02' },
          { t: 'Carga cognitiva', st: 'Carga cognitiva', s: 'p', href: 'sistema-diseno/principios-experiencia/personas-y-contextos-de-uso.html#s-01-02-03' } ] },
      { n: '03', k: '01-03', t: 'Elecciones verificadas', full: 'Decisiones verificables de experiencia', d: 'Hipótesis, criterios de aceptación e indicadores para medir la experiencia.', s: 'p', items: [
          { t: 'Hipótesis y requisitos', st: 'Hipótesis y requisitos', s: 'p', href: 'sistema-diseno/principios-experiencia/decisiones-verificables-de-experiencia.html#s-01-03-01' },
          { t: 'Criterios UX', st: 'Criterios UX', s: 'p', href: 'sistema-diseno/principios-experiencia/decisiones-verificables-de-experiencia.html#s-01-03-02' },
          { t: 'Indicadores', st: 'Indicadores', s: 'p', href: 'sistema-diseno/principios-experiencia/decisiones-verificables-de-experiencia.html#s-01-03-03' } ] }
    ]
  },
  {
    id: 'arq', k: 'ARQ', t: 'Arquitectura', full: 'Arquitectura y navegación', href: 'sistema-diseno/arquitectura-navegacion.html', color: 'cielo', colorName: 'Azul Cielo',
    cd: 'Cómo se organiza la información y cómo se recorre.',
    d: 'Establece cómo se organiza la información y cómo las personas se desplazan por las aplicaciones.',
    ch: [
      { n: '04', k: '02-01', t: 'Información', full: 'Arquitectura de información', d: 'Mapas de contenido, taxonomías y relaciones entre la información.', s: 'p', items: [
          { t: 'Mapas de contenido', st: 'Mapas de contenido', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/arquitectura-de-informacion.html#s-02-01-01' },
          { t: 'Taxonomías', st: 'Taxonomías', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/arquitectura-de-informacion.html#s-02-01-02' },
          { t: 'Jerarquías', st: 'Jerarquías', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/arquitectura-de-informacion.html#s-02-01-03' } ] },
      { n: '05', k: '02-02', t: 'Navegación', full: 'Estructura de navegación', d: 'Estructura base de aplicación, menús, cabeceras, rutas y niveles.', s: 'p', items: [
          { t: 'Estructura base', st: 'Estructura base', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html#s-02-02-01' },
          { t: 'Menús laterales', st: 'Menús laterales', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html#s-02-02-02' },
          { t: 'Rutas y niveles', st: 'Rutas y niveles', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/estructura-de-navegacion.html#s-02-02-03' } ] },
      { n: '06', k: '02-03', t: 'Búsqueda', full: 'Búsqueda y orientación', d: 'Búsqueda, filtros y orientación sobre dónde se está y cómo continuar.', s: 'p', items: [
          { t: 'Búsqueda global', st: 'Búsqueda global', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/busqueda-y-orientacion.html#s-02-03-01' },
          { t: 'Filtros', st: 'Filtros', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/busqueda-y-orientacion.html#s-02-03-02' },
          { t: 'Ubicación y contexto', st: 'Ubicación y contexto', s: 'p', href: 'sistema-diseno/arquitectura-navegacion/busqueda-y-orientacion.html#s-02-03-03' } ] }
    ]
  },
  {
    id: 'fui', k: 'FUI', t: 'Fundamentos', full: 'Fundamentos de interfaz', href: 'sistema-diseno/fundamentos-interfaz.html', color: 'salmon', colorName: 'Salmón Tierra',
    cd: 'Los fundamentos de Marca convertidos en reglas de interfaz.',
    d: 'Traduce los fundamentos visuales de Marca a reglas técnicas y visuales aplicables a interfaces.',
    ch: [
      { n: '07', k: '03-01', t: 'Tokens', full: 'Tokens de diseño', d: 'Tokens base, semánticos y de componente; nomenclatura, temas y versiones.', s: 'p', items: [
          { t: 'Tokens base', st: 'Tokens base', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/tokens-de-diseno.html#s-03-01-01' },
          { t: 'Nomenclatura', st: 'Nomenclatura', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/tokens-de-diseno.html#s-03-01-02' },
          { t: 'Temas visuales', st: 'Temas visuales', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/tokens-de-diseno.html#s-03-01-03' } ] },
      { n: '08', k: '03-02', t: 'Color funcional', full: 'Color funcional', d: 'Superficies, texto, bordes, interacción, foco, estados y contraste.', s: 'p', items: [
          { t: 'Superficies', st: 'Superficies', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/color-funcional.html#s-03-02-01' },
          { t: 'Colores de interacción', st: 'Colores de interacción', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/color-funcional.html#s-03-02-02' },
          { t: 'Contraste', st: 'Contraste', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/color-funcional.html#s-03-02-03' } ] },
      { n: '09', k: '03-03', t: 'Tipografía', full: 'Tipografía aplicada', d: 'Familias oficiales aplicadas a interfaz: jerarquías, escalas y cifras.', s: 'p', items: [
          { t: 'Familias tipográficas', st: 'Familias tipográficas', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/tipografia-aplicada.html#s-03-03-01' },
          { t: 'Jerarquías y escalas', st: 'Jerarquías y escalas', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/tipografia-aplicada.html#s-03-03-02' },
          { t: 'Cifras y datos', st: 'Cifras y datos', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/tipografia-aplicada.html#s-03-03-03' } ] },
      { n: '10', k: '03-04', t: 'Espacio y retícula', full: 'Espacio, retícula y geometría', d: 'Retículas, puntos de adaptación, espaciado, densidad y esquinas.', s: 'p', items: [
          { t: 'Retículas', st: 'Retículas', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/espacio-reticula-y-geometria.html#s-03-04-01' },
          { t: 'Espaciado', st: 'Espaciado', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/espacio-reticula-y-geometria.html#s-03-04-02' },
          { t: 'Geometría', st: 'Geometría', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/espacio-reticula-y-geometria.html#s-03-04-03' } ] },
      { n: '11', k: '03-05', t: 'Recursos visuales', full: 'Recursos visuales de interfaz', d: 'Iconografía funcional, bordes, sombras, elevación e imágenes aplicadas.', s: 'p', items: [
          { t: 'Iconografía funcional', st: 'Iconografía funcional', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/recursos-visuales-de-interfaz.html#s-03-05-01' },
          { t: 'Bordes', st: 'Bordes', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/recursos-visuales-de-interfaz.html#s-03-05-02' },
          { t: 'Imágenes', st: 'Imágenes', s: 'p', href: 'sistema-diseno/fundamentos-interfaz/recursos-visuales-de-interfaz.html#s-03-05-03' } ] }
    ]
  },
  {
    id: 'cpe', k: 'CPE', t: 'Componentes', full: 'Componentes y estados', href: 'sistema-diseno/componentes-estados.html', color: 'atardecer', colorName: 'Salmón Atardecer',
    cd: 'Piezas reutilizables, sus variantes y sus estados.',
    d: 'Define los componentes reutilizables y sus variantes. Aquí se documentan las piezas, mientras que los flujos completos pertenecen a Patrones de interacción.',
    ch: [
      { n: '12', k: '04-01', t: 'Acciones', full: 'Componentes de acción', d: 'Botones, enlaces, menús y sus estados de disponibilidad y proceso.', s: 'p', items: [
          { t: 'Botones', st: 'Botones', s: 'p', href: 'sistema-diseno/componentes-estados/componentes-de-accion.html#s-04-01-01' },
          { t: 'Enlaces', st: 'Enlaces', s: 'p', href: 'sistema-diseno/componentes-estados/componentes-de-accion.html#s-04-01-02' },
          { t: 'Disponibilidad', st: 'Disponibilidad', s: 'p', href: 'sistema-diseno/componentes-estados/componentes-de-accion.html#s-04-01-03' } ] },
      { n: '13', k: '04-02', t: 'Entradas', full: 'Controles de entrada', d: 'Campos, selectores, casillas, interruptores, fechas y archivos.', s: 'p', items: [
          { t: 'Campos de texto', st: 'Campos de texto', s: 'p', href: 'sistema-diseno/componentes-estados/controles-de-entrada.html#s-04-02-01' },
          { t: 'Selectores', st: 'Selectores', s: 'p', href: 'sistema-diseno/componentes-estados/controles-de-entrada.html#s-04-02-02' },
          { t: 'Fechas', st: 'Fechas', s: 'p', href: 'sistema-diseno/componentes-estados/controles-de-entrada.html#s-04-02-03' } ] },
      { n: '14', k: '04-03', t: 'Estructura', full: 'Componentes de estructura', d: 'Pestañas, tablas, listas, contenedores y contenido expandible.', s: 'p', items: [
          { t: 'Pestañas', st: 'Pestañas', s: 'p', href: 'sistema-diseno/componentes-estados/componentes-de-estructura.html#s-04-03-01' },
          { t: 'Tablas', st: 'Tablas', s: 'p', href: 'sistema-diseno/componentes-estados/componentes-de-estructura.html#s-04-03-02' },
          { t: 'Acordeones', st: 'Acordeones', s: 'p', href: 'sistema-diseno/componentes-estados/componentes-de-estructura.html#s-04-03-03' } ] },
      { n: '15', k: '04-04', t: 'Retroalimentación', full: 'Retroalimentación y superposiciones', d: 'Alertas, etiquetas de estado, diálogos, paneles e indicadores de carga.', s: 'p', items: [
          { t: 'Alertas', st: 'Alertas', s: 'p', href: 'sistema-diseno/componentes-estados/retroalimentacion-y-superposiciones.html#s-04-04-01' },
          { t: 'Diálogos', st: 'Diálogos', s: 'p', href: 'sistema-diseno/componentes-estados/retroalimentacion-y-superposiciones.html#s-04-04-02' },
          { t: 'Indicadores de progreso', st: 'Indicadores de progreso', s: 'p', href: 'sistema-diseno/componentes-estados/retroalimentacion-y-superposiciones.html#s-04-04-03' } ] }
    ]
  },
  {
    id: 'pat', k: 'PAT', t: 'Patrones', full: 'Patrones de interacción', href: 'sistema-diseno/patrones-interaccion.html', color: 'noche', colorName: 'Azul Noche',
    cd: 'Componentes combinados para resolver tareas completas.',
    d: 'Define cómo se combinan los componentes para resolver tareas y procesos completos.',
    ch: [
      { n: '16', k: '05-01', t: 'Formularios', full: 'Formularios y validaciones', d: 'Estructura, ayuda contextual, validación y formularios de varios pasos.', s: 'p', items: [
          { t: 'Estructura y ayuda', st: 'Estructura y ayuda', s: 'p', href: 'sistema-diseno/patrones-interaccion/formularios-y-validaciones.html#s-05-01-01' },
          { t: 'Validación', st: 'Validación', s: 'p', href: 'sistema-diseno/patrones-interaccion/formularios-y-validaciones.html#s-05-01-02' },
          { t: 'Múltiples pasos', st: 'Múltiples pasos', s: 'p', href: 'sistema-diseno/patrones-interaccion/formularios-y-validaciones.html#s-05-01-03' } ] },
      { n: '17', k: '05-02', t: 'Flujos de trabajo', full: 'Flujos de trabajo', d: 'Crear, editar, guardar, eliminar y continuar tareas sin perder trabajo.', s: 'p', items: [
          { t: 'Creación', st: 'Creación', s: 'p', href: 'sistema-diseno/patrones-interaccion/flujos-de-trabajo.html#s-05-02-01' },
          { t: 'Eliminación', st: 'Eliminación', s: 'p', href: 'sistema-diseno/patrones-interaccion/flujos-de-trabajo.html#s-05-02-02' },
          { t: 'Borradores', st: 'Borradores', s: 'p', href: 'sistema-diseno/patrones-interaccion/flujos-de-trabajo.html#s-05-02-03' } ] },
      { n: '18', k: '05-03', t: 'Recuperación', full: 'Estados y recuperación', d: 'Estados vacíos y de espera, reintentos, deshacer y errores.', s: 'p', items: [
          { t: 'Estados vacíos', st: 'Estados vacíos', s: 'p', href: 'sistema-diseno/patrones-interaccion/estados-y-recuperacion.html#s-05-03-01' },
          { t: 'Reintentos', st: 'Reintentos', s: 'p', href: 'sistema-diseno/patrones-interaccion/estados-y-recuperacion.html#s-05-03-02' },
          { t: 'Errores', st: 'Errores', s: 'p', href: 'sistema-diseno/patrones-interaccion/estados-y-recuperacion.html#s-05-03-03' } ] },
      { n: '19', k: '05-04', t: 'Procesos críticos', full: 'Decisiones y operaciones sensibles', d: 'Confirmaciones de alto impacto, permisos y trazabilidad de acciones.', s: 'p', items: [
          { t: 'Confirmaciones', st: 'Confirmaciones', s: 'p', href: 'sistema-diseno/patrones-interaccion/decisiones-y-operaciones-sensibles.html#s-05-04-01' },
          { t: 'Permisos', st: 'Permisos', s: 'p', href: 'sistema-diseno/patrones-interaccion/decisiones-y-operaciones-sensibles.html#s-05-04-02' },
          { t: 'Trazabilidad visible', st: 'Trazabilidad visible', s: 'p', href: 'sistema-diseno/patrones-interaccion/decisiones-y-operaciones-sensibles.html#s-05-04-03' } ] }
    ]
  },
  {
    id: 'acc', k: 'ACC', t: 'Accesibilidad', full: 'Accesibilidad y adaptación', href: 'sistema-diseno/accesibilidad-adaptacion.html', color: 'cielo', colorName: 'Azul Cielo',
    cd: 'Requisitos de acceso y adaptación, con WCAG 2.2 AA.',
    d: 'Establece los requisitos de accesibilidad y adaptación, tomando WCAG 2.2 nivel AA como referencia de cumplimiento.',
    ch: [
      { n: '20', k: '06-01', t: 'Percepción', full: 'Accesibilidad perceptiva', d: 'Contraste, información más allá del color, zoom y espaciado de texto.', s: 'p', items: [
          { t: 'Contraste y legibilidad', st: 'Contraste y legibilidad', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-perceptiva.html#s-06-01-01' },
          { t: 'Sin depender del color', st: 'Sin depender del color', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-perceptiva.html#s-06-01-02' },
          { t: 'Zoom y redistribución', st: 'Zoom y redistribución', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-perceptiva.html#s-06-01-03' } ] },
      { n: '21', k: '06-02', t: 'Operación', full: 'Accesibilidad operativa', d: 'Teclado, foco, lectores de pantalla y objetivos táctiles.', s: 'p', items: [
          { t: 'Teclado', st: 'Teclado', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-operativa.html#s-06-02-01' },
          { t: 'Lectores de pantalla', st: 'Lectores de pantalla', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-operativa.html#s-06-02-02' },
          { t: 'Objetivos táctiles', st: 'Objetivos táctiles', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/accesibilidad-operativa.html#s-06-02-03' } ] },
      { n: '22', k: '06-03', t: 'Adaptación', full: 'Adaptación de la experiencia', d: 'Dispositivos, preferencias del sistema y distintas capacidades de uso.', s: 'p', items: [
          { t: 'Diseño adaptable', st: 'Diseño adaptable', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/adaptacion-de-la-experiencia.html#s-06-03-01' },
          { t: 'Preferencias del sistema', st: 'Preferencias del sistema', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/adaptacion-de-la-experiencia.html#s-06-03-02' },
          { t: 'Diferentes capacidades', st: 'Diferentes capacidades', s: 'p', href: 'sistema-diseno/accesibilidad-adaptacion/adaptacion-de-la-experiencia.html#s-06-03-03' } ] }
    ]
  },
  {
    id: 'cnt', k: 'CNT', t: 'Contenido', full: 'Contenido y comunicación', href: 'sistema-diseno/contenido-comunicacion.html', color: 'salmon', colorName: 'Salmón Tierra',
    cd: 'La voz de Keyons aplicada a los mensajes de interfaz.',
    d: 'Aplica los principios de voz y claridad a los mensajes de las interfaces.',
    ch: [
      { n: '23', k: '07-01', t: 'Escritura', full: 'Escritura de interfaz', d: 'Etiquetas, llamadas a la acción, instrucciones y textos de ayuda.', s: 'p', items: [
          { t: 'Etiquetas', st: 'Etiquetas', s: 'p', href: 'sistema-diseno/contenido-comunicacion/escritura-de-interfaz.html#s-07-01-01' },
          { t: 'Instrucciones', st: 'Instrucciones', s: 'p', href: 'sistema-diseno/contenido-comunicacion/escritura-de-interfaz.html#s-07-01-02' },
          { t: 'Brevedad', st: 'Brevedad', s: 'p', href: 'sistema-diseno/contenido-comunicacion/escritura-de-interfaz.html#s-07-01-03' } ] },
      { n: '24', k: '07-02', t: 'Mensajes', full: 'Mensajes del sistema', d: 'Confirmaciones, progreso, errores, advertencias y estados vacíos.', s: 'p', items: [
          { t: 'Confirmaciones', st: 'Confirmaciones', s: 'p', href: 'sistema-diseno/contenido-comunicacion/mensajes-del-sistema.html#s-07-02-01' },
          { t: 'Errores', st: 'Errores', s: 'p', href: 'sistema-diseno/contenido-comunicacion/mensajes-del-sistema.html#s-07-02-02' },
          { t: 'Advertencias', st: 'Advertencias', s: 'p', href: 'sistema-diseno/contenido-comunicacion/mensajes-del-sistema.html#s-07-02-03' } ] },
      { n: '25', k: '07-03', t: 'Localización', full: 'Lenguaje y localización', d: 'Terminología, idiomas, adaptación regional y tono de cada producto.', s: 'p', items: [
          { t: 'Terminología', st: 'Terminología', s: 'p', href: 'sistema-diseno/contenido-comunicacion/lenguaje-y-localizacion.html#s-07-03-01' },
          { t: 'Idiomas y regiones', st: 'Idiomas y regiones', s: 'p', href: 'sistema-diseno/contenido-comunicacion/lenguaje-y-localizacion.html#s-07-03-02' },
          { t: 'Voz y tono', st: 'Voz y tono', s: 'p', href: 'sistema-diseno/contenido-comunicacion/lenguaje-y-localizacion.html#s-07-03-03' } ] }
    ]
  },
  {
    id: 'dav', k: 'DAV', t: 'Datos', full: 'Datos y visualización', href: 'sistema-diseno/datos-visualizacion.html', color: 'atardecer', colorName: 'Salmón Atardecer',
    cd: 'Información cuantitativa clara y bien interpretada.',
    d: 'Define cómo presentar información cuantitativa y operativa sin comprometer la interpretación.',
    ch: [
      { n: '26', k: '08-01', t: 'Tablas', full: 'Tablas y datos estructurados', d: 'Columnas, orden, filtros, paginación y densidad de tablas.', s: 'p', items: [
          { t: 'Columnas', st: 'Columnas', s: 'p', href: 'sistema-diseno/datos-visualizacion/tablas-y-datos-estructurados.html#s-08-01-01' },
          { t: 'Filtros', st: 'Filtros', s: 'p', href: 'sistema-diseno/datos-visualizacion/tablas-y-datos-estructurados.html#s-08-01-02' },
          { t: 'Densidad', st: 'Densidad', s: 'p', href: 'sistema-diseno/datos-visualizacion/tablas-y-datos-estructurados.html#s-08-01-03' } ] },
      { n: '27', k: '08-02', t: 'Gráficos', full: 'Gráficos de datos', d: 'Tipo de gráfico, paletas, escalas, leyendas y accesibilidad.', s: 'p', items: [
          { t: 'Tipo de gráfico', st: 'Tipo de gráfico', s: 'p', href: 'sistema-diseno/datos-visualizacion/graficos-de-datos.html#s-08-02-01' },
          { t: 'Paletas categóricas', st: 'Paletas categóricas', s: 'p', href: 'sistema-diseno/datos-visualizacion/graficos-de-datos.html#s-08-02-02' },
          { t: 'Escalas', st: 'Escalas', s: 'p', href: 'sistema-diseno/datos-visualizacion/graficos-de-datos.html#s-08-02-03' } ] },
      { n: '28', k: '08-03', t: 'Indicadores', full: 'Indicadores y cifras', d: 'Formatos numéricos, unidades, variaciones y datos incompletos.', s: 'p', items: [
          { t: 'Formatos numéricos', st: 'Formatos numéricos', s: 'p', href: 'sistema-diseno/datos-visualizacion/indicadores-y-cifras.html#s-08-03-01' },
          { t: 'Variaciones', st: 'Variaciones', s: 'p', href: 'sistema-diseno/datos-visualizacion/indicadores-y-cifras.html#s-08-03-02' },
          { t: 'Datos ausentes', st: 'Datos ausentes', s: 'p', href: 'sistema-diseno/datos-visualizacion/indicadores-y-cifras.html#s-08-03-03' } ] },
      { n: '29', k: '08-04', t: 'Dashboards', full: 'Dashboards e informes', d: 'Tableros organizados por tareas, exploración y exportación de resultados.', s: 'p', items: [
          { t: 'Organización', st: 'Organización', s: 'p', href: 'sistema-diseno/datos-visualizacion/dashboards-e-informes.html#s-08-04-01' },
          { t: 'Exploración', st: 'Exploración', s: 'p', href: 'sistema-diseno/datos-visualizacion/dashboards-e-informes.html#s-08-04-02' },
          { t: 'Exportación', st: 'Exportación', s: 'p', href: 'sistema-diseno/datos-visualizacion/dashboards-e-informes.html#s-08-04-03' } ] }
    ]
  },
  {
    id: 'iae', k: 'IAE', t: 'IA y Estela', full: 'Experiencias con IA y Estela', href: 'sistema-diseno/ia-estela.html', color: 'noche', colorName: 'Azul Noche',
    cd: 'Cómo se interactúa con la IA y con Estela en los productos.',
    d: 'Define la interacción con IA. La identidad y personalidad de Estela se documentarán en el Libro de Marca; aquí se definirá cómo se aplican en productos.',
    ch: [
      { n: '30', k: '09-01', t: 'Principios de IA', full: 'Principios de experiencia con IA', d: 'Capacidades, límites, fuentes y control del usuario frente a la IA.', s: 'p', items: [
          { t: 'Transparencia', st: 'Transparencia', s: 'p', href: 'sistema-diseno/ia-estela/principios-de-experiencia-con-ia.html#s-09-01-01' },
          { t: 'Incertidumbre', st: 'Incertidumbre', s: 'p', href: 'sistema-diseno/ia-estela/principios-de-experiencia-con-ia.html#s-09-01-02' },
          { t: 'Control del usuario', st: 'Control del usuario', s: 'p', href: 'sistema-diseno/ia-estela/principios-de-experiencia-con-ia.html#s-09-01-03' } ] },
      { n: '31', k: '09-02', t: 'Conversación', full: 'Interfaz conversacional de Estela', d: 'Cómo se aplica Estela en la conversación: mensajes, archivos e historial.', s: 'p', items: [
          { t: 'Identidad de Estela', st: 'Identidad de Estela', s: 'p', href: 'sistema-diseno/ia-estela/interfaz-conversacional-de-estela.html#s-09-02-01' },
          { t: 'Mensajes', st: 'Mensajes', s: 'p', href: 'sistema-diseno/ia-estela/interfaz-conversacional-de-estela.html#s-09-02-02' },
          { t: 'Historial', st: 'Historial', s: 'p', href: 'sistema-diseno/ia-estela/interfaz-conversacional-de-estela.html#s-09-02-03' } ] },
      { n: '32', k: '09-03', t: 'Agentes', full: 'Agentes y ejecución de acciones', d: 'Agentes, planificación, aprobaciones y registro de cada ejecución.', s: 'p', items: [
          { t: 'Orquestación', st: 'Orquestación', s: 'p', href: 'sistema-diseno/ia-estela/agentes-y-ejecucion-de-acciones.html#s-09-03-01' },
          { t: 'Planificación', st: 'Planificación', s: 'p', href: 'sistema-diseno/ia-estela/agentes-y-ejecucion-de-acciones.html#s-09-03-02' },
          { t: 'Aprobaciones y registro', st: 'Aprobaciones y registro', s: 'p', href: 'sistema-diseno/ia-estela/agentes-y-ejecucion-de-acciones.html#s-09-03-03' } ] },
      { n: '33', k: '09-04', t: 'Confianza segura', full: 'Seguridad y confianza en IA', d: 'Privacidad, acceso, escalamiento humano y acciones automáticas visibles.', s: 'p', items: [
          { t: 'Privacidad', st: 'Privacidad', s: 'p', href: 'sistema-diseno/ia-estela/seguridad-y-confianza-en-ia.html#s-09-04-01' },
          { t: 'Errores', st: 'Errores', s: 'p', href: 'sistema-diseno/ia-estela/seguridad-y-confianza-en-ia.html#s-09-04-02' },
          { t: 'Acciones automáticas', st: 'Acciones automáticas', s: 'p', href: 'sistema-diseno/ia-estela/seguridad-y-confianza-en-ia.html#s-09-04-03' } ] }
    ]
  },
  {
    id: 'spr', k: 'SPR', t: 'Productos', full: 'Sistemas de producto', href: 'sistema-diseno/sistemas-producto.html', color: 'cielo', colorName: 'Azul Cielo',
    cd: 'Una base común con expresiones visuales distintas.',
    d: 'Define las diferentes aplicaciones del sistema de diseño, con fundamentos compartidos y expresiones visuales distintas.',
    ch: [
      { n: '34', k: '10-01', t: 'Base compartida', full: 'Base compartida', d: 'Estándares UX comunes, componentes reutilizables y herencia de temas.', s: 'p', items: [
          { t: 'Estándares UX comunes', st: 'Estándares UX comunes', s: 'p', href: 'sistema-diseno/sistemas-producto/base-compartida.html#s-10-01-01' },
          { t: 'Reutilización', st: 'Reutilización', s: 'p', href: 'sistema-diseno/sistemas-producto/base-compartida.html#s-10-01-02' },
          { t: 'Herencia de temas', st: 'Herencia de temas', s: 'p', href: 'sistema-diseno/sistemas-producto/base-compartida.html#s-10-01-03' } ] },
      { n: '35', k: '10-02', t: 'Sitio web', full: 'Sitio web corporativo Keyons', d: 'La identidad corporativa en el sitio web: navegación, composición y acciones.', s: 'p', items: [
          { t: 'Aplicación funcional', st: 'Aplicación funcional', s: 'p', href: 'sistema-diseno/sistemas-producto/sitio-web-corporativo-keyons.html#s-10-02-01' },
          { t: 'Navegación', st: 'Navegación', s: 'p', href: 'sistema-diseno/sistemas-producto/sitio-web-corporativo-keyons.html#s-10-02-02' },
          { t: 'Interacciones', st: 'Interacciones', s: 'p', href: 'sistema-diseno/sistemas-producto/sitio-web-corporativo-keyons.html#s-10-02-03' } ] },
      { n: '36', k: '10-03', t: 'Herramientas', full: 'Herramientas internas Keyons', d: 'Identidad operativa, navegación por roles y espacios de trabajo densos.', s: 'p', items: [
          { t: 'Identidad visual', st: 'Identidad visual', s: 'p', href: 'sistema-diseno/sistemas-producto/herramientas-internas-keyons.html#s-10-03-01' },
          { t: 'Navegación por roles', st: 'Navegación por roles', s: 'p', href: 'sistema-diseno/sistemas-producto/herramientas-internas-keyons.html#s-10-03-02' },
          { t: 'Densidad informativa', st: 'Densidad informativa', s: 'p', href: 'sistema-diseno/sistemas-producto/herramientas-internas-keyons.html#s-10-03-03' } ] },
      { n: '37', k: '10-04', t: 'Product Default', full: 'Keyons Product Default', d: 'Estética neutral premium, estructura SaaS y opciones de configuración.', s: 'p', items: [
          { t: 'Estética neutral premium', st: 'Estética neutral premium', s: 'p', href: 'sistema-diseno/sistemas-producto/keyons-product-default.html#s-10-04-01' },
          { t: 'Estructura base', st: 'Estructura base', s: 'p', href: 'sistema-diseno/sistemas-producto/keyons-product-default.html#s-10-04-02' },
          { t: 'Configuración', st: 'Configuración', s: 'p', href: 'sistema-diseno/sistemas-producto/keyons-product-default.html#s-10-04-03' } ] },
      { n: '38', k: '10-05', t: 'White-label', full: 'Soluciones personalizadas y white-label', d: 'Identidades de clientes, marca blanca y límites de personalización.', s: 'p', items: [
          { t: 'Identidades de clientes', st: 'Identidades de clientes', s: 'p', href: 'sistema-diseno/sistemas-producto/soluciones-personalizadas-y-white-label.html#s-10-05-01' },
          { t: 'Marca blanca', st: 'Marca blanca', s: 'p', href: 'sistema-diseno/sistemas-producto/soluciones-personalizadas-y-white-label.html#s-10-05-02' },
          { t: 'Límites', st: 'Límites', s: 'p', href: 'sistema-diseno/sistemas-producto/soluciones-personalizadas-y-white-label.html#s-10-05-03' } ] }
    ]
  },
  {
    id: 'mov', k: 'MOV', t: 'Movimiento', full: 'Movimiento e interacción sensorial', href: 'sistema-diseno/movimiento-sensorial.html', color: 'salmon', colorName: 'Salmón Tierra',
    cd: 'Movimiento y recursos sensoriales con un propósito claro.',
    d: 'Regula el movimiento y los recursos sensoriales, sin convertirlos en requisitos decorativos.',
    ch: [
      { n: '39', k: '11-01', t: 'Operación activa', full: 'Movimiento operativo', d: 'Transiciones funcionales, retroalimentación, progreso y sus límites.', s: 'p', items: [
          { t: 'Transiciones funcionales', st: 'Transiciones funcionales', s: 'p', href: 'sistema-diseno/movimiento-sensorial/movimiento-operativo.html#s-11-01-01' },
          { t: 'Retroalimentación', st: 'Retroalimentación', s: 'p', href: 'sistema-diseno/movimiento-sensorial/movimiento-operativo.html#s-11-01-02' },
          { t: 'Interrupciones', st: 'Interrupciones', s: 'p', href: 'sistema-diseno/movimiento-sensorial/movimiento-operativo.html#s-11-01-03' } ] },
      { n: '40', k: '11-02', t: 'Movimiento editorial', full: 'Movimiento editorial', d: 'Entradas, cambios de escena y movimiento atmosférico según el contexto.', s: 'p', items: [
          { t: 'Entradas', st: 'Entradas', s: 'p', href: 'sistema-diseno/movimiento-sensorial/movimiento-editorial.html#s-11-02-01' },
          { t: 'Movimiento atmosférico', st: 'Movimiento atmosférico', s: 'p', href: 'sistema-diseno/movimiento-sensorial/movimiento-editorial.html#s-11-02-02' },
          { t: 'Intensidad', st: 'Intensidad', s: 'p', href: 'sistema-diseno/movimiento-sensorial/movimiento-editorial.html#s-11-02-03' } ] },
      { n: '41', k: '11-03', t: 'Multisensorial', full: 'Interacción multisensorial', d: 'Sonido, respuesta háptica y atajos del sistema operativo.', s: 'p', items: [
          { t: 'Sonido', st: 'Sonido', s: 'p', href: 'sistema-diseno/movimiento-sensorial/interaccion-multisensorial.html#s-11-03-01' },
          { t: 'Respuesta háptica', st: 'Respuesta háptica', s: 'p', href: 'sistema-diseno/movimiento-sensorial/interaccion-multisensorial.html#s-11-03-02' },
          { t: 'Atajos de teclado', st: 'Atajos de teclado', s: 'p', href: 'sistema-diseno/movimiento-sensorial/interaccion-multisensorial.html#s-11-03-03' } ] }
    ]
  },
  {
    id: 'gob', k: 'GOB', t: 'Gobierno', full: 'Calidad y gobierno del diseño', href: 'sistema-diseno/calidad-gobierno.html', color: 'atardecer', colorName: 'Salmón Atardecer',
    cd: 'Cómo se gestionan, implementan y prueban las normas.',
    d: 'Establece cómo se gestionan, implementan, prueban y mantienen las reglas del Sistema de Diseño.',
    ch: [
      { n: '42', k: '12-01', t: 'Gobierno normativo', full: 'Gobierno normativo', d: 'Fuente oficial, identificadores permanentes, aprobación y cambios.', s: 'p', items: [
          { t: 'Propiedad', st: 'Propiedad', s: 'p', href: 'sistema-diseno/calidad-gobierno/gobierno-normativo.html#s-12-01-01' },
          { t: 'Identificadores', st: 'Identificadores', s: 'p', href: 'sistema-diseno/calidad-gobierno/gobierno-normativo.html#s-12-01-02' },
          { t: 'Aprobación', st: 'Aprobación', s: 'p', href: 'sistema-diseno/calidad-gobierno/gobierno-normativo.html#s-12-01-03' } ] },
      { n: '43', k: '12-02', t: 'Implementación', full: 'Implementación técnica', d: 'Tokens y componentes en código, especificaciones y versiones.', s: 'p', items: [
          { t: 'Traducción de tokens', st: 'Traducción de tokens', s: 'p', href: 'sistema-diseno/calidad-gobierno/implementacion-tecnica.html#s-12-02-01' },
          { t: 'Especificaciones', st: 'Especificaciones', s: 'p', href: 'sistema-diseno/calidad-gobierno/implementacion-tecnica.html#s-12-02-02' },
          { t: 'Compatibilidad', st: 'Compatibilidad', s: 'p', href: 'sistema-diseno/calidad-gobierno/implementacion-tecnica.html#s-12-02-03' } ] },
      { n: '44', k: '12-03', t: 'Validación', full: 'Validación de calidad', d: 'Verificación visual, funcional, de usabilidad y de accesibilidad.', s: 'p', items: [
          { t: 'Verificación visual', st: 'Verificación visual', s: 'p', href: 'sistema-diseno/calidad-gobierno/validacion-de-calidad.html#s-12-03-01' },
          { t: 'Pruebas de usabilidad', st: 'Pruebas de usabilidad', s: 'p', href: 'sistema-diseno/calidad-gobierno/validacion-de-calidad.html#s-12-03-02' },
          { t: 'Regresiones', st: 'Regresiones', s: 'p', href: 'sistema-diseno/calidad-gobierno/validacion-de-calidad.html#s-12-03-03' } ] },
      { n: '45', k: '12-04', t: 'Documentación', full: 'Documentación y consulta', d: 'Catálogo de normas, exportación para personas e IA y permisos.', s: 'p', items: [
          { t: 'Catálogo', st: 'Catálogo', s: 'p', href: 'sistema-diseno/calidad-gobierno/documentacion-y-consulta.html#s-12-04-01' },
          { t: 'Exportación para IA', st: 'Exportación para IA', s: 'p', href: 'sistema-diseno/calidad-gobierno/documentacion-y-consulta.html#s-12-04-02' },
          { t: 'Consulta autorizada', st: 'Consulta autorizada', s: 'p', href: 'sistema-diseno/calidad-gobierno/documentacion-y-consulta.html#s-12-04-03' } ] }
    ]
  }
];
