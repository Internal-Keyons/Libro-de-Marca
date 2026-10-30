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
    id: 'marca', t: 'Marca', href: 'marca/index.html', color: 'cielo', colorName: 'Azul Cielo',
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
      { n: '03', k: 'principios', t: 'Principios de diseño', s: 'v', d: 'Seis principios que guían cada decisión de diseño de Keyons, con su marca o la del cliente.', items: [
        { t: 'Diseñar con identidad, construir con criterio', st: 'Identidad y criterio', s: 'v', href: 'marca/principios.html#criterio' },
        { t: 'Identidad, experiencia y sistema', s: 'v', href: 'marca/principios.html#capas' },
        { t: 'Calma estructural y expresión visual', st: 'Calma y expresión', s: 'v', href: 'marca/principios.html#calma' },
        { t: 'Expresividad contextual', s: 'v', href: 'marca/principios.html#contexto' },
        { t: 'Comprensión antes que complejidad', st: 'Comprensión', s: 'v', href: 'marca/principios.html#comprension' },
        { t: 'Calidad sin firma visible', s: 'v', href: 'marca/principios.html#calidad' } ] },
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
    id: 'fundamentos', t: 'Fundamentos', href: 'fundamentos/index.html', color: 'noche', colorName: 'Azul Noche',
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
        { t: 'Familias', s: 'b', href: 'fundamentos/tipografia/sistema.html#familias' }, { t: 'Escala y jerarquía', s: 'b', href: 'fundamentos/tipografia/sistema.html#escala' }, { t: 'Probador', s: 'b', href: 'fundamentos/tipografia/sistema.html#probador' },
        { t: 'Titular editorial', s: 'v', href: 'fundamentos/tipografia/sistema.html#titular' }, { t: 'Kickers', s: 'b', href: 'fundamentos/tipografia/sistema.html#kickers' },
        { t: 'Reglas de uso', s: 'b', href: 'fundamentos/tipografia/sistema.html#reglas' }, { t: 'Tipografía en impreso', st: 'En impreso', s: 'p' } ] },
      { n: '09', k: 'forma', was: '08', t: 'Forma y espacio', s: 'v', d: 'Interior curvo, exterior recto. Radio y separación.', items: [
        { t: 'Regla de esquinas', s: 'b', href: 'fundamentos/forma/espacio.html#esquinas' }, { t: 'Radios', s: 'b', href: 'fundamentos/forma/espacio.html#radios' }, { t: 'Espaciado', s: 'b', href: 'fundamentos/forma/espacio.html#espaciado' }, { t: 'Retícula y responsive', s: 'b', href: 'fundamentos/forma/espacio.html#reticula' }, { t: 'Densidad', s: 'b', href: 'fundamentos/forma/espacio.html#densidad' }, { t: 'Patrones de contenido', s: 'b', href: 'fundamentos/forma/espacio.html#patrones' }, { t: 'Diagramas de información', s: 'b', href: 'fundamentos/forma/espacio.html#diagramas' } ] },
      { n: '10', k: 'composicion', t: 'Composición editorial y retículas', st: 'Composición editorial', s: 'b', d: 'Cómo decidir la composición que conviene a cada contenido: retícula, simetría, asimetría y ritmo.', items: [
        { t: 'Decidir la composición', s: 'b', href: 'fundamentos/composicion/editorial.html#decidir' },
        { t: 'Simetría y asimetría', s: 'b', href: 'fundamentos/composicion/editorial.html#simetria' },
        { t: 'Retículas editoriales', s: 'b', href: 'fundamentos/composicion/editorial.html#reticulas' },
        { t: 'Ritmo visual', s: 'b', href: 'fundamentos/composicion/editorial.html#ritmo' } ] },
      { n: '11', k: 'criterio', t: 'Criterio visual y antipatrones', st: 'Antipatrones', s: 'v', d: 'Dieciséis normas para reconocer lo genérico y elegir una alternativa con razón.', items: [
        { sub: 'Estructura y jerarquía' },
        { t: 'Kicker decorativo', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-001' },
        { t: 'Tracking indiscriminado', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-002' },
        { t: 'Jerarquía visual repetitiva', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-003' },
        { t: 'Tarjetas innecesarias', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-004' },
        { sub: 'Recursos gráficos' },
        { t: 'Gradientes ornamentales', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-005' },
        { t: 'Geometría genérica', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-006' },
        { t: 'Acentos tipográficos repetidos', st: 'Acentos repetidos', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-007' },
        { t: 'Iconografía de relleno', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-008' },
        { t: 'Saturación de microelementos', st: 'Microelementos', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-009' },
        { sub: 'Composición y movimiento' },
        { t: 'Simetría automática', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-010' },
        { t: 'Movimiento ornamental', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-011' },
        { t: 'Contraste insuficiente', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-012' },
        { sub: 'Carácter y orientación' },
        { t: 'Lenguaje genérico', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-013' },
        { t: 'Maximalismo uniforme', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-014' },
        { t: 'Originalidad a costa de orientación', st: 'Orientación', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-015' },
        { t: 'Composición no intercambiable', st: 'No intercambiable', s: 'v', href: 'fundamentos/criterio/antipatrones.html#vis-016' } ] },
      { n: '12', k: 'elementos', was: '09', t: 'Elementos gráficos', s: 'b', d: 'Viñetas, alternancia de formas, cristal y fotografía.', items: [
        { t: 'Viñetas de marca', s: 'b', href: 'fundamentos/elementos/graficos.html#vinetas' }, { t: 'Elementos de énfasis', s: 'b', href: 'fundamentos/elementos/graficos.html#enfasis' }, { t: 'Líneas y cotas', s: 'b', href: 'fundamentos/elementos/graficos.html#lineas' }, { t: 'Cristal', s: 'b', href: 'fundamentos/elementos/graficos.html#cristal' }, { t: 'Ventanas de cielo', s: 'b', href: 'fundamentos/elementos/graficos.html#ventana' }, { t: 'Ráfagas', s: 'b', href: 'fundamentos/elementos/graficos.html#rafagas' }, { t: 'Patrones y texturas', s: 'b', href: 'fundamentos/elementos/graficos.html#patrones' }, { t: 'Fotografía', s: 'b', href: 'fundamentos/elementos/graficos.html#fotografia' } ] },
      { n: '13', k: 'iconografia', was: '10', t: 'Iconografía', s: 'b', d: 'Estilo de trazo, tamaños según contexto y catálogo.', items: [
        { t: 'Retícula', s: 'b', href: 'fundamentos/iconografia/iconos.html#reticula' }, { t: 'Familias y variantes', s: 'b', href: 'fundamentos/iconografia/iconos.html#familias' }, { t: 'Uso', s: 'b', href: 'fundamentos/iconografia/iconos.html#uso' }, { t: 'Animación', s: 'b', href: 'fundamentos/iconografia/iconos.html#animacion' }, { t: 'Catálogo', s: 'b', href: 'fundamentos/iconografia/iconos.html#catalogo' }, { t: 'Entrega técnica', s: 'b', href: 'fundamentos/iconografia/iconos.html#entrega' } ] },
      { n: '14', k: 'datos', was: '11', t: 'Datos', s: 'b', d: 'Gráficos que comunican con rigor: principios, color, tipografía y estructura.', items: [
        { t: 'Principios', s: 'b', href: 'fundamentos/datos/graficos.html#principios' }, { t: 'Sistema cromático', s: 'b', href: 'fundamentos/datos/graficos.html#paleta' },
        { t: 'Tipografía en gráficos', st: 'Tipografía', s: 'b', href: 'fundamentos/datos/graficos.html#tipografia' }, { t: 'Tipos de gráfico', s: 'b', href: 'fundamentos/datos/graficos.html#tipos' },
        { t: 'Estructura', s: 'b', href: 'fundamentos/datos/graficos.html#estructura' } ] },
      { n: '15', k: 'movimiento', was: '12', t: 'Movimiento', s: 'p', d: 'Curvas, duraciones y resortes de la firma de movimiento.', items: [
        { t: 'Personalidad de movimiento', st: 'Personalidad' }, { t: 'Duraciones y curvas' }, { t: 'Transiciones' } ] },
      { n: '16', k: 'accesibilidad', was: '13', t: 'Accesibilidad', s: 'b', d: 'Contraste, tamaños mínimos y verificación.', items: [
        { t: 'Legibilidad y jerarquía', st: 'Legibilidad', s: 'b' }, { t: 'Contraste y tamaño', s: 'b' },
        { t: 'Checklist de verificación', st: 'Checklist', s: 'b' } ] }
    ]
  },
  {
    id: 'modos', t: 'Modos', href: 'modos/index.html', color: 'salmon', colorName: 'Salmón Tierra',
    d: 'Cómo se ve y suena la marca en cada registro.',
    ch: [
      { n: '17', k: 'corporativo', was: '14', t: 'Corporativo', s: 'p', d: 'El registro formal: sobrio, claro y preciso, de principio a fin.', items: [
        { sub: 'Principios' },
        { t: 'Cuándo aplica' }, { t: 'Color en el modo' }, { t: 'Metáfora contenida' },
        { sub: 'Sistema' },
        { t: 'Formatos de página' }, { t: 'Retícula y márgenes' }, { t: 'Tipografía en documento', st: 'Tipografía' }, { t: 'Uso del logo' },
        { sub: 'Componentes' },
        { t: 'Portada' }, { t: 'Encabezado y pie' }, { t: 'Títulos y numeración' }, { t: 'Tablas y cifras' },
        { t: 'Gráficos' }, { t: 'Notas y citas' }, { t: 'Bloque de firmas' }, { t: 'Sellos y marca de agua', st: 'Sellos' } ] },
      { n: '18', k: 'expresivo', was: '15', t: 'Expresivo', s: 'b', d: 'El registro abierto: cielos, narrativa y emoción, siempre sobre la retícula.', items: [
        { sub: 'Principios' }, { t: 'Libertad por canal', s: 'b' },
        { sub: 'Sistema' }, { t: 'Cielos aplicados', s: 'b' }, { t: 'Degradados', s: 'b' },
        { sub: 'Componentes' }, { t: 'Firma humana' }, { t: 'Titulares expresivos' } ] },
      { n: '19', k: 'digital', was: '16', t: 'Digital', s: 'b', d: 'Producto e interfaz: sobrio con momentos vivos. Componentes y patrones.', items: [
        { sub: 'Principios' }, { t: 'Sobrio con momentos vivos', st: 'Sobriedad viva', s: 'b' },
        { sub: 'Sistema' }, { t: 'Tokens', s: 'b' }, { t: 'Densidad' },
        { sub: 'Componentes' }, { t: 'Botones', s: 'b' }, { t: 'Campos de formulario', st: 'Formularios', s: 'v' },
        { t: 'Mensajes de estado', s: 'v' }, { t: 'Badges', s: 'b' }, { t: 'Navegación' }, { t: 'Tablas y datos' },
        { sub: 'Aplicaciones' }, { t: 'Estela · acciones generativas', st: 'Estela en interfaz', s: 'b' }, { t: 'Estados vacíos' }, { t: 'Onboarding' }, { t: 'Dashboards' } ] }
    ]
  },
  {
    id: 'interfaces', t: 'Interfaces', full: 'Sistemas de Interfaces', href: 'interfaces/index.html', color: 'cielo2', colorName: 'Por definir',
    d: 'La aplicación del diseño Keyons en páginas web, herramientas internas, productos SaaS y desarrollos personalizados.',
    ch: [
      { n: '20', k: 'arquitectura', t: 'Arquitectura de sistemas de diseño', st: 'Arquitectura', s: 'p', d: 'Identidad, experiencia, sistema y expresión de cada producto: cuatro capas que no se confunden.', items: [
        { t: 'Las cuatro capas' }, { t: 'Capas de tokens' }, { t: 'Qué hereda cada producto' }, { t: 'Relación con el manual Sistema de Diseño', st: 'Sistema de Diseño' } ] },
      { n: '21', k: 'tokens', t: 'Tokens visuales y temas', st: 'Tokens y temas', s: 'p', d: 'Tokens semánticos de interfaz y temas. Los valores de color, tipografía y espacio viven en Fundamentos.', items: [
        { t: 'Tokens semánticos' }, { t: 'Temperatura sobria y viva' }, { t: 'Temas claro y oscuro' }, { t: 'Temas de cliente' } ] },
      { n: '22', k: 'componentes', t: 'Componentes UI', s: 'p', d: 'Botones, campos, mensajes, badges y tablas con la geometría de Forma y espacio.', items: [
        { t: 'Botones' }, { t: 'Campos de formulario', st: 'Formularios' }, { t: 'Mensajes de estado' }, { t: 'Badges' }, { t: 'Tablas y datos' }, { t: 'Estados de los componentes', st: 'Estados' } ] },
      { n: '23', k: 'patrones', t: 'Patrones visuales y navegación', st: 'Patrones y navegación', s: 'p', d: 'Cómo se orienta la persona: dónde está, qué puede hacer, qué ocurre y cómo sigue.', items: [
        { t: 'Navegación' }, { t: 'Jerarquía de pantalla' }, { t: 'Estados vacíos' }, { t: 'Onboarding' }, { t: 'Tableros' } ] },
      { n: '24', k: 'saas', t: 'SaaS predeterminado', st: 'SaaS', s: 'p', d: 'La interfaz por defecto de los productos Keyons y las zonas que el cliente ajusta.', items: [
        { t: 'Qué es intocable' }, { t: 'Zonas personalizables' }, { t: 'Documentos generados' } ] },
      { n: '25', k: 'marca-blanca', t: 'Personalización y white-label', st: 'White-label', s: 'p', d: 'Productos bajo la identidad del cliente: la calidad Keyons sin firma visible.', items: [
        { t: 'Tema del cliente' }, { t: 'Créditos' }, { t: 'Calidad sin firma' } ] },
      { n: '26', k: 'estela-ui', t: 'Interfaces de Estela', st: 'Estela', s: 'p', d: 'Cómo aparece y actúa Estela en pantalla. Su personalidad vive en Marca.', items: [
        { t: 'Presencia y avatar' }, { t: 'Conversación' }, { t: 'Acciones generativas' }, { t: 'Estados de la agente' } ] },
      { n: '27', k: 'motion', t: 'Motion e identidad sensorial digital', st: 'Motion', s: 'p', d: 'Movimiento de interfaz, Ráfaga y la experiencia sensorial de los productos.', items: [
        { t: 'Movimiento de interfaz' }, { t: 'Ráfaga y cielo' }, { t: 'Duraciones y curvas' }, { t: 'Movimiento reducido' } ] },
      { n: '28', k: 'accesibilidad-ui', t: 'Guías visuales de accesibilidad', st: 'Accesibilidad', s: 'p', d: 'Foco, objetivos táctiles, contraste en componentes y estados que no dependen del color.', items: [
        { t: 'Foco visible' }, { t: 'Objetivos táctiles' }, { t: 'Contraste en componentes' }, { t: 'Estados sin depender del color' } ] }
    ]
  },
  {
    id: 'aplicaciones', t: 'Aplicaciones', href: 'aplicaciones/index.html', color: 'atardecer', colorName: 'Salmón Atardecer',
    d: 'Dónde se aplica la marca: cada canal con sus reglas.',
    ch: [
      { n: '29', k: 'documentos', was: '17', t: 'Documentos', s: 'p', d: 'Propuestas, contratos, facturas, correspondencia y papelería.', items: [
        { grp: 'Comerciales' }, { t: 'Propuesta comercial', deep: 1 }, { t: 'Cotización', deep: 1 }, { t: 'Presentación', deep: 1 }, { t: 'Caso de éxito', deep: 1 },
        { grp: 'Legales' }, { t: 'Contrato', deep: 1 }, { t: 'Confidencialidad', deep: 1 }, { t: 'Anexos', deep: 1 },
        { grp: 'Financieras' }, { t: 'Factura electrónica', deep: 1 }, { t: 'Recibo', deep: 1 }, { t: 'Estado de cuenta', deep: 1 },
        { grp: 'Correspondencia' }, { t: 'Carta', deep: 1 }, { t: 'Firma de correo', deep: 1 }, { t: 'Firma digital', deep: 1 },
        { grp: 'Papelería' }, { t: 'Tarjeta de presentación', st: 'Tarjeta', deep: 1 }, { t: 'Hoja membretada', deep: 1 }, { t: 'Sobre y carpeta', deep: 1 } ] },
      { n: '30', k: 'presentaciones', was: '18', t: 'Presentaciones', s: 'b', d: 'Para clientes, capacitaciones, el equipo y talleres: método, historia, voz y estética.', items: [
        { sub: 'Para qué' }, { t: 'Tipos', s: 'b', href: 'aplicaciones/presentaciones.html#tipos' }, { t: 'Método', s: 'b', href: 'aplicaciones/presentaciones.html#metodo' }, { sub: 'Contenido' }, { t: 'Storytelling', s: 'b', href: 'aplicaciones/presentaciones.html#historia' }, { t: 'El arco Keyons', s: 'b', href: 'aplicaciones/presentaciones.html#arco' }, { t: 'Escribir para la pantalla', s: 'b', href: 'aplicaciones/presentaciones.html#escribir' }, { t: 'Límites y notas', s: 'b', href: 'aplicaciones/presentaciones.html#limites' }, { sub: 'Estética' }, { t: 'Lienzo y retícula', s: 'b', href: 'aplicaciones/presentaciones.html#lienzo' }, { t: 'Tipografía', s: 'b', href: 'aplicaciones/presentaciones.html#tipografia' }, { t: 'Contraste', s: 'b', href: 'aplicaciones/presentaciones.html#contraste' }, { t: 'Ritmo', s: 'b', href: 'aplicaciones/presentaciones.html#ritmo' }, { t: 'Riesgo y estado', s: 'b', href: 'aplicaciones/presentaciones.html#riesgo' }, { t: 'Imagen y gráficos', s: 'b', href: 'aplicaciones/presentaciones.html#imagen' }, { sub: 'Hacerla' }, { t: 'Plantillas', s: 'b', href: 'aplicaciones/presentaciones.html#plantillas' }, { t: 'Antes de presentar', s: 'b', href: 'aplicaciones/presentaciones.html#antes' } ] },
      { n: '31', k: 'sitio-web', was: '19', t: 'Sitio web', s: 'b', d: 'Claridad antes que creatividad, con momentos de cielo.', items: [
        { sub: 'Principios' }, { t: 'Claridad antes que creatividad', st: 'Claridad primero', s: 'b' },
        { sub: 'Sistema' }, { t: 'Lectura en Z' }, { t: 'Retícula web' },
        { sub: 'Componentes' }, { t: 'Cabecera', s: 'v' }, { t: 'Titulares de sección', s: 'v' }, { t: 'Tarjetas' },
        { sub: 'Aplicaciones' }, { t: 'Páginas tipo' } ] },
      { n: '32', k: 'redes', was: '20', t: 'Redes y campañas', st: 'Redes', s: 'p', d: 'Publicaciones, campañas y contenido para redes sociales.', items: [
        { t: 'Redes sociales' }, { t: 'Campañas' } ] },
      { n: '33', k: 'eventos', was: '21', t: 'Eventos y merch', st: 'Eventos', s: 'p', d: 'Eventos, talleres presenciales y artículos de marca.', items: [
        { t: 'Eventos' }, { t: 'Merch' } ] },
      { n: '34', k: 'personalizacion', was: '22', t: 'Personalización', s: 'b', d: 'Productos para clientes: qué cambia y qué se queda en SaaS, Boutique y marca blanca.', items: [
        { t: 'Tres modelos', s: 'b', href: 'aplicaciones/personalizacion.html#modelos' }, { t: 'Modelo A · SaaS', st: 'Modelo SaaS', s: 'b', href: 'aplicaciones/personalizacion.html#saas' },
        { t: 'Modelo B · Boutique', st: 'Modelo Boutique', s: 'b', href: 'aplicaciones/personalizacion.html#boutique' }, { t: 'Modelo C · Marca blanca', st: 'Marca blanca', s: 'b', href: 'aplicaciones/personalizacion.html#blanca' } ] }
    ]
  },
  {
    id: 'recursos', t: 'Recursos', href: 'recursos/index.html', color: 'mediodia', colorName: 'Cielo Mediodía',
    d: 'El espacio de trabajo: imágenes, texturas, íconos y plantillas.',
    ch: [
      { n: '35', k: 'galeria', was: '23', t: 'Galería de imágenes', st: 'Galería', s: 'b', d: 'Degradados, cielos, naturaleza y personas, con ID y crédito.', items: [
        { t: 'Galería', s: 'b', href: 'recursos/galeria.html#galeria' } ] },
      { n: '36', k: 'texturas', was: '24', t: 'Texturas y degradados', st: 'Texturas', s: 'b', d: 'Cielos hechos con código, con ID.', items: [
        { t: 'Catálogo', s: 'b', href: 'recursos/texturas.html#texturas' } ] },
      { n: '37', k: 'iconos', was: '25', t: 'Íconos', s: 'b', d: 'El catálogo completo de la familia.', items: [
        { t: 'Catálogo', s: 'b', href: 'recursos/iconos.html#catalogo' } ] },
      { n: '38', k: 'plantillas', was: '26', t: 'Plantillas y documentos', st: 'Plantillas', s: 'b', d: 'Plantillas de presentación y manuales.', items: [
        { t: 'Plantillas', s: 'b', href: 'recursos/plantillas.html#plantillas' }, { t: 'Documentos', s: 'b', href: 'recursos/plantillas.html#documentos' } ] },
      { n: '39', k: 'referencia', was: '27', t: 'Referencia', s: 'b', d: 'La memoria de las decisiones.', items: [
        { t: 'Nomenclatura de reglas', st: 'Nomenclatura', s: 'b', href: 'recursos/referencia.html#nomenclatura' }, { t: 'Índice de reglas', st: 'Índice', s: 'b', href: 'recursos/referencia.html#indice' },
        { t: 'Registro de decisiones', st: 'Decisiones' }, { t: 'Glosario' }, { t: 'Cambios' } ] }
    ]
  }
];
