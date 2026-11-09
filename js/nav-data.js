/* ═══════════════════════════════════════════════════════════════
   KEYONS · MAPA DEL MANUAL
   Una sola fuente para la cabecera, el lateral, la portada, las
   páginas de área, el paginador y el buscador.
   Para agregar una página: agregala aquí con su href.
   s: 'v' vigente · 'b' borrador · 'p' por definir (valor por defecto)
   k: clave estable del capítulo (ancla #cap-k); no cambia si cambia el número.
   was: número anterior a la renumeración de 2026-10-29, para enlaces viejos.
   full: nombre completo del área cuando el menú usa uno corto.
   href: ruta desde la raíz. Sin href, la página aún no existe.
   Un href con #ancla es una sección dentro de una página de capítulo.
   color: degradado corporativo que identifica al área.
   ═══════════════════════════════════════════════════════════════ */
window.KEYONS_NAV = [
  {
    id: 'marca', t: 'Marca', href: 'marca/index.html', color: 'noche', colorName: 'Azul Noche',
    d: 'Quiénes somos, qué creemos y cómo hablamos.',
    ch: [
      { n: '01', k: 'adn', was: '01', t: 'ADN', s: 'b', d: 'La esencia, el propósito y los principios que no se negocian.', items: [
        { t: 'Esencia', s: 'b', href: 'marca/adn.html#esencia' }, { t: 'Propósito', s: 'b', href: 'marca/adn.html#proposito' },
        { t: 'Personalización', s: 'b', href: 'marca/adn.html#espectro' }, { t: 'Origen', s: 'b', href: 'marca/adn.html#origen' },
        { t: 'Filosofía', s: 'b', href: 'marca/adn.html#filosofia' },
        { t: 'Propuesta de valor', s: 'b', href: 'marca/adn.html#propuesta' }, { t: 'Principios', s: 'b', href: 'marca/adn.html#principios' } ] },
      { n: '02', k: 'concepto', was: '02', t: 'Concepto', s: 'b', d: 'El cielo como símbolo, las metáforas y lo que no somos.', items: [
        { sub: 'El Cielo' },
        { t: 'El símbolo', s: 'b', href: 'marca/cielo.html#simbolo' }, { t: 'Jerarquía de cielos', s: 'b', href: 'marca/cielo.html#jerarquia' },
        { t: 'Diario de Cielos', s: 'b', href: 'marca/cielo.html#diario' },
        { sub: 'Metáforas' },
        { t: 'Cinco condiciones', s: 'b', href: 'marca/metaforas.html#condiciones' }, { t: 'Formalidad por canal', s: 'b', href: 'marca/metaforas.html#canal' },
        { sub: 'Composición' },
        { t: 'Composición', s: 'b', href: 'marca/composicion.html#reglas' }, { t: 'Regla del contraste', s: 'b', href: 'marca/composicion.html#contraste' },
        { t: 'Anti-referentes', s: 'b', href: 'marca/composicion.html#anti' }, { t: 'Herencia estética', s: 'b', href: 'marca/composicion.html#herencia' } ] },
      { n: '03', k: 'principios', t: 'Principios', s: 'v', d: 'Cinco principios que guían cada decisión de diseño de Keyons, con su marca o la del cliente.', items: [
        { t: 'Diseñar con identidad, construir con criterio', st: 'Identidad y criterio', s: 'v', href: 'marca/principios.html#criterio' },
        { t: 'Identidad, experiencia y sistema', st: 'Roles definidos', s: 'v', href: 'marca/principios.html#capas' },
        { t: 'Calma y expresión', s: 'v', href: 'marca/principios.html#calma' },
        { t: 'Intensidad según contexto', st: 'Según contexto', s: 'v', href: 'marca/principios.html#contexto' },
        { t: 'Claridad primero', s: 'v', href: 'marca/principios.html#comprension' } ] },
      { n: '04', k: 'voz', was: '03', t: 'Voz', s: 'b', d: 'Cómo escribe Keyons: dos modos, cuatro reglas y un vocabulario propio.', items: [
        { sub: 'La voz' },
        { t: 'Dos modos', s: 'b', href: 'marca/voz.html#modos' }, { t: 'Reglas de escritura', s: 'b', href: 'marca/voz.html#reglas' },
        { sub: 'Vocabulario' },
        { t: 'Palabras propias', s: 'b', href: 'marca/vocabulario.html#propio' }, { t: 'Palabras que evitamos', st: 'Palabras evitadas', s: 'b', href: 'marca/vocabulario.html#evita' },
        { sub: 'Trato y traducción' },
        { t: 'El trato', s: 'b', href: 'marca/trato.html#usted' }, { t: 'Primera o tercera persona', st: 'Persona gramatical', s: 'b', href: 'marca/trato.html#persona' },
        { t: 'De lo técnico a lo humano', st: 'Traducción técnica', s: 'b', href: 'marca/trato.html#traduccion' } ] },
      { n: '05', k: 'estela', was: '04', t: 'Estela', s: 'p', d: 'La cara de Keyons: quién es, cómo habla, cómo se ve y cómo actúa.', items: [
        { t: 'Quién es', s: 'p' }, { t: 'Personalidad', s: 'p' }, { t: 'Voz y trato', s: 'p' },
        { t: 'Estética', s: 'p' }, { t: 'Comportamiento', s: 'p' }, { t: 'En la interfaz', s: 'p' } ] }
    ]
  },
  {
    id: 'fundamentos', t: 'Fundamentos', href: 'fundamentos/index.html', color: 'cielo', colorName: 'Azul Cielo',
    d: 'El núcleo visual que comparten todos los modos.',
    ch: [
      { n: '06', k: 'identidad', was: '05', t: 'Identidad', s: 'b', d: 'Logotipo, isotipo e insignia: construcción y uso.', items: [
        { sub: 'Logotipo' },
        { t: 'Versiones', s: 'b', href: 'fundamentos/identidad/logotipo.html#versiones' }, { t: 'Construcción', s: 'b', href: 'fundamentos/identidad/logotipo.html#construccion' },
        { t: 'Geometría', s: 'b', href: 'fundamentos/identidad/logotipo.html#geometria' }, { t: 'Área de protección', s: 'b', href: 'fundamentos/identidad/logotipo.html#proteccion' },
        { t: 'Tamaño mínimo', s: 'b', href: 'fundamentos/identidad/logotipo.html#minimo' },
        { t: 'Usos incorrectos', s: 'b', href: 'fundamentos/identidad/logotipo.html#incorrectos' },
        { sub: 'Isotipo' },
        { t: 'El corchete', s: 'b', href: 'fundamentos/identidad/isotipo.html#corchete' }, { t: 'Estado y evolución', s: 'b', href: 'fundamentos/identidad/isotipo.html#evolucion' },
        { t: 'Destello central', s: 'b', href: 'fundamentos/identidad/isotipo.html#destello' }, { t: 'Criterio de transición', s: 'b', href: 'fundamentos/identidad/isotipo.html#transicion' } ] },
      { n: '07', k: 'color', was: '06', t: 'Color', s: 'b', d: 'Un sistema en capas: paleta base, escalas, cielos y color por modo.', items: [
        { sub: 'Paleta base' },
        { t: 'Sistema en capas', s: 'b', href: 'fundamentos/color/paleta-base.html#capas' }, { t: 'Colores principales', s: 'b', href: 'fundamentos/color/paleta-base.html#principales' },
        { t: 'Colores de apoyo', s: 'b', href: 'fundamentos/color/paleta-base.html#apoyo' }, { t: 'Reglas de uso', s: 'b', href: 'fundamentos/color/paleta-base.html#reglas' },
        { t: 'Combinaciones', s: 'b', href: 'fundamentos/color/paleta-base.html#contraste' }, { t: 'Escalas tonales', s: 'b', href: 'fundamentos/color/escalas.html#escalas' },
        { sub: 'Cielos' },
        { t: 'Cinco cielos', s: 'b', href: 'fundamentos/color/cielos.html#cielos' }, { t: 'Cielos especiales', s: 'b', href: 'fundamentos/color/cielos.html#especiales' },
        { t: 'Gradientes', s: 'b', href: 'fundamentos/color/cielos.html#gradientes' },
        { sub: 'Color por modo' },
        { t: 'Institucional', s: 'b', href: 'fundamentos/color/por-modo.html#institucional' }, { t: 'Expresivo', s: 'b', href: 'fundamentos/color/por-modo.html#expresivo' },
        { t: 'Interfaz', s: 'b', href: 'fundamentos/color/por-modo.html#interfaz' },
        { sub: 'Funcionales' },
        { t: 'Grises tipográficos', s: 'b', href: 'fundamentos/color/funcionales.html#grises' }, { t: 'Estados del sistema', s: 'b', href: 'fundamentos/color/funcionales.html#estados' },
        { t: 'Acción y superficies', s: 'b', href: 'fundamentos/color/funcionales.html#accion' } ] },
      { n: '08', k: 'tipografia', was: '07', t: 'Tipografía', s: 'b', d: 'Plus Jakarta Sans y TASA Orbiter: escala, jerarquía y reglas.', items: [
        { t: 'Familias tipográficas', st: 'Familias', s: 'b', href: 'fundamentos/tipografia/sistema.html#familias' }, { t: 'Escala y jerarquía', s: 'b', href: 'fundamentos/tipografia/sistema.html#escala' }, { t: 'Probador tipográfico', st: 'Probador', s: 'b', href: 'fundamentos/tipografia/sistema.html#probador' },
        { t: 'Etiquetas de contexto', st: 'Etiquetas', s: 'b', href: 'fundamentos/tipografia/sistema.html#kickers' },
        { t: 'Criterios de aplicación', st: 'Criterios', s: 'b', href: 'fundamentos/tipografia/sistema.html#reglas' }, { t: 'Uso por función', s: 'v', href: 'fundamentos/tipografia/sistema.html#funcion' }, { t: 'Tracking y espaciado de letras', st: 'Tracking', s: 'b', href: 'fundamentos/tipografia/sistema.html#tracking' }, { t: 'Tipografía para impresión', st: 'Impresión', s: 'b', href: 'fundamentos/tipografia/sistema.html#impreso' } ] },
      { n: '09', k: 'forma', was: '08', t: 'Geometría y espacio', st: 'Geometría y espacio', s: 'v', d: 'El lenguaje geométrico de Keyons: esquinas, radios y espacio.', items: [
        { sub: 'Geometría' },
        { t: 'Lenguaje geométrico Keyons', st: 'Lenguaje', s: 'v', href: 'fundamentos/forma/espacio.html#esquinas' },
        { t: 'Sistema de radios y curvaturas', st: 'Radios y curvaturas', s: 'v', href: 'fundamentos/forma/espacio.html#radios' },
        { t: 'Proporciones', s: 'p' },
        { sub: 'Espacio y ritmo' },
        { t: 'Sistema de espaciado', st: 'Espaciado', s: 'v', href: 'fundamentos/forma/espacio.html#espaciado' },
        { t: 'Contenedores', s: 'p' },
        { t: 'Elevación', s: 'p' } ] },
      { n: '10', k: 'composicion', t: 'Composición', s: 'v', d: 'Cómo elegir la estructura que conviene a cada contenido: retícula, ritmo, densidad, patrones y diagramas.', items: [
        { t: 'Componer según el contenido', st: 'Componer', s: 'v', href: 'fundamentos/composicion/editorial.html#decidir' },
        { t: 'Simetría y asimetría', s: 'v', href: 'fundamentos/composicion/editorial.html#simetria' },
        { t: 'Retículas editoriales', s: 'v', href: 'fundamentos/composicion/editorial.html#reticulas' },
        { t: 'Ritmo y equilibrio visual', st: 'Ritmo y equilibrio', s: 'v', href: 'fundamentos/composicion/editorial.html#ritmo' },
        { t: 'Jerarquía y densidad de información', st: 'Jerarquía y densidad', s: 'v', href: 'fundamentos/composicion/editorial.html#densidad' },
        { t: 'Diagramas de información', st: 'Diagramas', s: 'v', href: 'fundamentos/composicion/editorial.html#diagramas' },
        { t: 'Ejemplos de aplicación', st: 'Ejemplos', s: 'b', href: 'fundamentos/composicion/editorial.html#ejemplos' } ] },
      { n: '11', k: 'elementos', was: ['09', '12'], t: 'Elementos gráficos', s: 'b', d: 'Viñetas, énfasis, transparencia, luz, cielos, tramas y fotografía.', items: [
        { sub: 'Estructura' },
        { t: 'Viñetas y marcadores gráficos', st: 'Viñetas y marcadores', s: 'b', href: 'fundamentos/elementos/graficos.html#vinetas' }, { t: 'Recursos de énfasis visual', st: 'Énfasis visual', s: 'b', href: 'fundamentos/elementos/graficos.html#enfasis' }, { t: 'Líneas, guías y medidas', st: 'Líneas y medidas', s: 'b', href: 'fundamentos/elementos/graficos.html#lineas' },
        { sub: 'Atmósfera visual' },
        { t: 'Transparencia y superposición', st: 'Transparencia', s: 'b', href: 'fundamentos/elementos/graficos.html#cristal' }, { t: 'Luz y profundidad', s: 'v', href: 'fundamentos/elementos/graficos.html#profundidad' }, { t: 'Ventanas de cielo', s: 'b', href: 'fundamentos/elementos/graficos.html#ventana' }, { t: 'Ráfagas de color', st: 'Ráfagas', s: 'b', href: 'fundamentos/elementos/graficos.html#rafagas' },
        { sub: 'Tramas y texturas' },
        { t: 'Tramas y texturas', s: 'b', href: 'fundamentos/elementos/graficos.html#patrones' },
        { sub: 'Imágenes' },
        { t: 'Fotografía e imágenes', st: 'Fotografía', s: 'b', href: 'fundamentos/elementos/graficos.html#fotografia' } ] },
      { n: '12', k: 'iconografia', was: ['10', '13'], t: 'Iconografía', s: 'b', d: 'Estilo de trazo, tamaños según contexto y catálogo.', items: [
        { t: 'Retícula', s: 'b', href: 'fundamentos/iconografia/iconos.html#reticula' }, { t: 'Familias y variantes', s: 'b', href: 'fundamentos/iconografia/iconos.html#familias' }, { t: 'Uso', s: 'b', href: 'fundamentos/iconografia/iconos.html#uso' }, { t: 'Animación', s: 'b', href: 'fundamentos/iconografia/iconos.html#animacion' }, { t: 'Catálogo', s: 'b', href: 'fundamentos/iconografia/iconos.html#catalogo' }, { t: 'Entrega técnica', s: 'b', href: 'fundamentos/iconografia/iconos.html#entrega' } ] },
      { n: '13', k: 'datos', was: ['11', '14'], t: 'Datos y visualización', st: 'Datos', s: 'b', d: 'Gráficos que comunican con rigor: principios, color, tipografía y estructura.', items: [
        { t: 'Principios', s: 'b', href: 'fundamentos/datos/graficos.html#principios' }, { t: 'Sistema cromático', s: 'b', href: 'fundamentos/datos/graficos.html#paleta' },
        { t: 'Tipografía en gráficos', st: 'Tipografía', s: 'b', href: 'fundamentos/datos/graficos.html#tipografia' }, { t: 'Tipos de gráfico', s: 'b', href: 'fundamentos/datos/graficos.html#tipos' },
        { t: 'Estructura', s: 'b', href: 'fundamentos/datos/graficos.html#estructura' } ] },
      { n: '14', k: 'movimiento', was: ['12', '15'], t: 'Movimiento', s: 'p', d: 'Curvas, duraciones y resortes de la firma de movimiento.', items: [
        { t: 'Personalidad de movimiento', st: 'Personalidad' }, { t: 'Duraciones y curvas' }, { t: 'Transiciones' } ] },
      { n: '15', k: 'accesibilidad', was: ['13', '16'], t: 'Accesibilidad visual', st: 'Accesibilidad', s: 'b', d: 'Contraste, tamaños mínimos y verificación.', items: [
        { t: 'Legibilidad y jerarquía', st: 'Legibilidad', s: 'b' }, { t: 'Contraste y tamaño', s: 'b' },
        { t: 'Checklist de verificación', st: 'Checklist', s: 'b' } ] }
    ]
  },
  {
    id: 'modos', t: 'Modos', href: 'modos/index.html', color: 'salmon', colorName: 'Salmón Tierra',
    d: 'Cómo se ve y suena la marca en cada registro.',
    ch: [
      { n: '16', k: 'corporativo', was: ['14', '17'], t: 'Corporativo', s: 'p', d: 'El registro formal: sobrio, claro y preciso, de principio a fin.', items: [
        { sub: 'Principios' },
        { t: 'Cuándo aplica' }, { t: 'Color en el modo' }, { t: 'Metáfora contenida' },
        { sub: 'Sistema' },
        { t: 'Formatos de página' }, { t: 'Retícula y márgenes' }, { t: 'Tipografía en documento', st: 'Tipografía' }, { t: 'Uso del logo' },
        { sub: 'Componentes' },
        { t: 'Portada' }, { t: 'Encabezado y pie' }, { t: 'Títulos y numeración' }, { t: 'Tablas y cifras' },
        { t: 'Gráficos' }, { t: 'Notas y citas' }, { t: 'Bloque de firmas' }, { t: 'Sellos y marca de agua', st: 'Sellos' } ] },
      { n: '17', k: 'expresivo', was: ['15', '18'], t: 'Expresivo', s: 'b', d: 'El registro abierto: cielos, narrativa y emoción, siempre sobre la retícula.', items: [
        { sub: 'Principios' }, { t: 'Libertad por canal', s: 'b' },
        { sub: 'Sistema' }, { t: 'Cielos aplicados', s: 'b' }, { t: 'Degradados', s: 'b' },
        { sub: 'Componentes' }, { t: 'Firma humana' }, { t: 'Titulares expresivos' } ] },
      { n: '18', k: 'digital', was: ['16', '19'], t: 'Digital', s: 'b', d: 'Producto e interfaz: sobrio con momentos vivos. Componentes y patrones.', items: [
        { sub: 'Principios' }, { t: 'Sobrio con momentos vivos', st: 'Sobriedad viva', s: 'b' },
        { sub: 'Sistema' }, { t: 'Tokens', s: 'b' }, { t: 'Densidad' },
        { sub: 'Componentes' }, { t: 'Botones', s: 'b' }, { t: 'Campos de formulario', st: 'Formularios', s: 'v' },
        { t: 'Mensajes de estado', s: 'v' }, { t: 'Badges', s: 'b' }, { t: 'Navegación' }, { t: 'Tablas y datos' },
        { sub: 'Aplicaciones' }, { t: 'Estela · acciones generativas', st: 'Estela en interfaz', s: 'b' }, { t: 'Estados vacíos' }, { t: 'Onboarding' }, { t: 'Dashboards' } ] }
    ]
  },
  {
    id: 'aplicaciones', t: 'Aplicaciones', href: 'aplicaciones/index.html', color: 'atardecer', colorName: 'Salmón Atardecer',
    d: 'Dónde se aplica la marca: cada canal con sus reglas.',
    ch: [
      { n: '19', k: 'documentos', was: ['17', '20'], t: 'Documentos', s: 'p', d: 'Propuestas, contratos, facturas, correspondencia y papelería.', items: [
        { grp: 'Comerciales' }, { t: 'Propuesta comercial', deep: 1 }, { t: 'Cotización', deep: 1 }, { t: 'Presentación', deep: 1 }, { t: 'Caso de éxito', deep: 1 },
        { grp: 'Legales' }, { t: 'Contrato', deep: 1 }, { t: 'Confidencialidad', deep: 1 }, { t: 'Anexos', deep: 1 },
        { grp: 'Financieras' }, { t: 'Factura electrónica', deep: 1 }, { t: 'Recibo', deep: 1 }, { t: 'Estado de cuenta', deep: 1 },
        { grp: 'Correspondencia' }, { t: 'Carta', deep: 1 }, { t: 'Firma de correo', deep: 1 }, { t: 'Firma digital', deep: 1 },
        { grp: 'Papelería' }, { t: 'Tarjeta de presentación', st: 'Tarjeta', deep: 1 }, { t: 'Hoja membretada', deep: 1 }, { t: 'Sobre y carpeta', deep: 1 } ] },
      { n: '20', k: 'presentaciones', was: ['18', '21'], t: 'Presentaciones', s: 'b', d: 'Para clientes, capacitaciones, el equipo y talleres: método, historia, voz y estética.', items: [
        { sub: 'Para qué' }, { t: 'Tipos', s: 'b', href: 'aplicaciones/presentaciones.html#tipos' }, { t: 'Método', s: 'b', href: 'aplicaciones/presentaciones.html#metodo' }, { sub: 'Contenido' }, { t: 'Storytelling', s: 'b', href: 'aplicaciones/presentaciones.html#historia' }, { t: 'El arco Keyons', s: 'b', href: 'aplicaciones/presentaciones.html#arco' }, { t: 'Escribir para la pantalla', st: 'Para la pantalla', s: 'b', href: 'aplicaciones/presentaciones.html#escribir' }, { t: 'Límites y notas', s: 'b', href: 'aplicaciones/presentaciones.html#limites' }, { sub: 'Estética' }, { t: 'Lienzo y retícula', s: 'b', href: 'aplicaciones/presentaciones.html#lienzo' }, { t: 'Tipografía', s: 'b', href: 'aplicaciones/presentaciones.html#tipografia' }, { t: 'Contraste', s: 'b', href: 'aplicaciones/presentaciones.html#contraste' }, { t: 'Ritmo', s: 'b', href: 'aplicaciones/presentaciones.html#ritmo' }, { t: 'Riesgo y estado', s: 'b', href: 'aplicaciones/presentaciones.html#riesgo' }, { t: 'Imagen y gráficos', s: 'b', href: 'aplicaciones/presentaciones.html#imagen' }, { sub: 'Hacerla' }, { t: 'Plantillas', s: 'b', href: 'aplicaciones/presentaciones.html#plantillas' }, { t: 'Antes de presentar', s: 'b', href: 'aplicaciones/presentaciones.html#antes' } ] },
      { n: '21', k: 'redes', was: ['20', '22'], t: 'Redes y campañas', st: 'Redes', s: 'p', d: 'Publicaciones, campañas y contenido para redes sociales.', items: [
        { t: 'Redes sociales' }, { t: 'Campañas' } ] },
      { n: '22', k: 'eventos', was: ['21', '23'], t: 'Eventos y merch', st: 'Eventos', s: 'p', d: 'Eventos, talleres presenciales y artículos de marca.', items: [
        { t: 'Eventos' }, { t: 'Merch' } ] },
      { n: '23', k: 'personalizacion', was: ['22', '24'], t: 'Personalización', s: 'b', d: 'Productos para clientes: qué cambia y qué se queda en SaaS, Boutique y marca blanca.', items: [
        { t: 'Tres modelos', s: 'b', href: 'aplicaciones/personalizacion.html#modelos' }, { t: 'Modelo A · SaaS', st: 'Modelo SaaS', s: 'b', href: 'aplicaciones/personalizacion.html#saas' },
        { t: 'Modelo B · Boutique', st: 'Modelo Boutique', s: 'b', href: 'aplicaciones/personalizacion.html#boutique' }, { t: 'Modelo C · Marca blanca', st: 'Marca blanca', s: 'b', href: 'aplicaciones/personalizacion.html#blanca' } ] }
    ]
  },
  {
    id: 'recursos', t: 'Recursos', href: 'recursos/index.html', color: 'noche', colorName: 'Azul Noche',
    d: 'El espacio de trabajo: imágenes, texturas, íconos y plantillas.',
    ch: [
      { n: '24', k: 'galeria', was: ['23', '25'], t: 'Galería de imágenes', st: 'Galería', s: 'b', d: 'Degradados, cielos, naturaleza y personas, con ID y crédito.', items: [
        { t: 'Galería', s: 'b', href: 'recursos/galeria.html#galeria' } ] },
      { n: '25', k: 'texturas', was: ['24', '26'], t: 'Texturas', s: 'b', d: 'Cielos hechos con código, con ID.', items: [
        { t: 'Catálogo', s: 'b', href: 'recursos/texturas.html#texturas' } ] },
      { n: '26', k: 'iconos', was: ['25', '27'], t: 'Íconos', s: 'b', d: 'El catálogo completo de la familia.', items: [
        { t: 'Catálogo', s: 'b', href: 'recursos/iconos.html#catalogo' } ] },
      { n: '27', k: 'plantillas', was: ['26', '28'], t: 'Plantillas', s: 'b', d: 'Plantillas de presentación y manuales.', items: [
        { t: 'Plantillas', s: 'b', href: 'recursos/plantillas.html#plantillas' }, { t: 'Documentos', s: 'b', href: 'recursos/plantillas.html#documentos' } ] },
      { n: '28', k: 'referencia', was: ['27', '29'], t: 'Referencia', s: 'b', d: 'La memoria de las decisiones.', items: [
        { t: 'Nomenclatura de reglas', st: 'Nomenclatura', s: 'b', href: 'recursos/referencia.html#nomenclatura' }, { t: 'Índice de reglas', st: 'Índice', s: 'b', href: 'recursos/referencia.html#indice' },
        { t: 'Trazabilidad de Criterios visuales', st: 'Trazabilidad', s: 'v', href: 'fundamentos/criterio/antipatrones.html#trazabilidad' }, { t: 'Registro de decisiones', st: 'Decisiones' }, { t: 'Glosario' }, { t: 'Cambios' } ] },
      { n: '29', k: 'tecnicos', t: 'Recursos técnicos', st: 'Técnicos', s: 'b', d: 'La expresión visual en HTML, CSS y JS, lista para copiar.', items: [
        { t: 'Catálogo', s: 'b', href: 'recursos/tecnicos.html#tecnicos' } ] }
    ]
  }
];
