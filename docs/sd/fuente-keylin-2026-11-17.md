# Textos fuente de Keylin · Sistema de Diseño · 17 de noviembre de 2026

Uso interno. Son los requisitos de origen de las normas KYN-SDI. Las páginas los citan en `origen` (`data/sd-normas.json`).
Capítulos 01 a 06: textos base y ampliación, en `propuestas/matriz-normativa-sd-01-06.md` (columna «Textos de origen»).
Este archivo guarda los del Bloque 3 tal como llegaron; los del Bloque 4 se suman al construirlos.

## 07. Tokens
- **Fuente única de valores:** Los componentes DEBEN utilizar tokens oficiales para los valores visuales y funcionales compartidos, evitando valores arbitrarios repetidos en el código.
- **Roles semánticos:** Los tokens DEBEN describir su función, como superficie, texto, borde, foco, acción o estado, en lugar de depender únicamente del nombre de un color.
- **Cambios controlados:** Una modificación de tokens compartidos DEBE comprobarse en los componentes y productos afectados antes de aprobarse.
- Aplicación: Un botón utiliza `action-primary` y `text-on-primary`, no un color hexadecimal escrito de forma independiente en cada pantalla.
- Verificación: Los componentes reutilizables heredan los valores correctos y los cambios no provocan regresiones en otras vistas.
- Matriz: Los componentes compartidos DEBEN utilizar tokens semánticos oficiales para superficies, texto, bordes, foco, acciones, estados y espaciados. Comprobación: cambiar un token del tema y comprobar que todos los componentes afectados responden correctamente. Pendientes: catálogo de tokens funcionales, temas claro y oscuro.

## 08. Color funcional
- **Color con función:** Cada color aplicado a una interfaz DEBE cumplir una función de identidad, jerarquía, acción, estado o diferenciación de información.
- **Estados semánticos:** Los errores, advertencias y confirmaciones DEBEN utilizar las funciones cromáticas oficiales y señales adicionales que permitan comprenderlos sin depender exclusivamente del color.
- **Separación de significados:** Salmón Tierra NO DEBE utilizarse como sustituto del color semántico de error.
- **Contraste:** Las combinaciones cromáticas DEBEN respetar los criterios de contraste aplicables de WCAG 2.2 AA.
- Aplicación: Un error de formulario utiliza un indicador semántico, texto explicativo y una relación visual clara con el campo.
- Verificación: Los estados pueden distinguirse visualmente y comprenderse sin depender únicamente del color.
- Matriz: Los colores de marca no sustituyen automáticamente los colores semánticos. Comprobación: revisar acciones, selección, errores, advertencias, confirmaciones y estados deshabilitados.

## 09. Tipografía
- **Sistema tipográfico:** Las interfaces DEBEN utilizar las familias, pesos y criterios tipográficos oficiales de Keyons o el tema aprobado para el producto.
- **Jerarquía consistente:** Títulos, etiquetas, valores, ayudas y textos operativos DEBEN mantener diferencias reconocibles de función y jerarquía.
- **Legibilidad:** Los textos DEBEN conservar legibilidad con ampliación, ajustes de espaciado y diferentes tamaños de pantalla.
- **Truncamiento:** La información necesaria para comprender o ejecutar una tarea NO DEBE perderse definitivamente por truncamiento visual.
- Aplicación: Una tabla puede abreviar un nombre en una columna estrecha, siempre que el valor completo siga estando disponible.
- Verificación: Se revisan textos largos, zoom, ampliación de espaciado y adaptación móvil.

## 10. Espacio y retícula
- **Espaciado compartido:** Los componentes DEBEN aplicar la escala espacial oficial de Keyons y sus tokens correspondientes.
- **Agrupación semántica:** La proximidad entre elementos DEBE reflejar su relación funcional: etiqueta y campo, título y contenido, acción y resultado.
- **Composición adaptable:** Las retículas DEBEN reorganizarse sin producir solapamientos, pérdida de controles ni recortes que impidan completar tareas.
- Aplicación: En un formulario, cada etiqueta permanece asociada visualmente a su campo y los grupos de información son reconocibles.
- Verificación: Se prueban contenido largo, estados de error, distintos anchos y variaciones de densidad.

## 12. Acciones
- **Jerarquía:** Las acciones principales y secundarias DEBEN distinguirse de forma consistente dentro de cada grupo de decisión.
- **Estados:** Los controles interactivos DEBEN contemplar los estados aplicables: normal, hover cuando corresponda, foco, activación, carga y deshabilitado.
- **Acciones destructivas:** Las acciones de alto impacto DEBEN comunicar sus consecuencias y aplicar la protección correspondiente a su riesgo.
- Aplicación: Guardar, cancelar y eliminar no comparten una jerarquía visual que pueda inducir confusión.
- Verificación: Se comprueban todas las variantes con teclado, puntero, pantalla táctil y estados de procesamiento.

## 13. Entradas
- **Etiquetas identificables:** Cada campo DEBE tener una etiqueta que explique qué información solicita, independientemente del texto de ejemplo.
- **Validación útil:** Los errores de entrada DEBEN identificar el campo afectado y explicar cómo corregir la información.
- **Control apropiado:** La selección de un control DEBERÍA responder al tipo de dato y al esfuerzo que requiere introducirlo.
- Aplicación: Una fecha se presenta con un formato comprensible y permite introducir valores válidos sin generar ambigüedad.
- Verificación: Se prueban campos vacíos, valores incorrectos, entradas largas, lectores de pantalla y navegación por teclado.

## 16. Formularios
- **Flujo comprensible:** Los formularios DEBEN agrupar campos relacionados y seguir una secuencia que corresponda al proceso real.
- **Prevención de pérdidas:** Cuando exista riesgo de perder información introducida, el sistema DEBE ofrecer un mecanismo apropiado de recuperación o advertencia.
- **Validación proporcionada:** La validación NO DEBE interrumpir innecesariamente la entrada ni provocar la eliminación de valores correctos.
- Verificación: Completar, corregir, interrumpir y retomar el formulario.

## 17. Flujos de trabajo
- **Secuencia y progreso:** Los procesos de varios pasos DEBEN comunicar su avance y las acciones necesarias para continuar.
- **Contexto conservado:** El sistema DEBERÍA conservar información y decisiones válidas cuando la persona retrocede o corrige un paso.
- **Terminación clara:** Al finalizar, la interfaz DEBE indicar el resultado y ofrecer un destino o siguiente acción comprensible.
- (Desde 02, ampliación) **Continuidad del trabajo:** Cuando una tarea pueda interrumpirse, el producto DEBERÍA conservar el progreso recuperable, respetando los requisitos de seguridad y privacidad.
- Verificación: Completar un proceso, regresar, corregir información y finalizar.

## 18. Recuperación
- **Ruta de salida:** Ante un error que impide continuar, la interfaz DEBE ofrecer una alternativa viable o explicar claramente qué impide la recuperación.
- **Reversibilidad:** Las acciones reversibles DEBERÍAN ofrecer una opción de deshacer o restaurar cuando resulte técnica y funcionalmente apropiado.
- **Persistencia:** Un fallo NO DEBE eliminar información válida que pueda conservarse de forma segura.
- Verificación: Simular errores de red, validación y operación, comprobando la recuperación.

## 20. Percepción
- **Referencia de conformidad:** Los productos web de Keyons se diseñan y verifican tomando WCAG 2.2 nivel AA como objetivo mínimo de accesibilidad. DEBE
- **Información perceptible:** Los contenidos y controles DEBEN ofrecer contraste, etiquetas y alternativas apropiadas para que su significado no dependa de un único recurso sensorial.
- **Lectura adaptable:** La interfaz DEBE conservar su contenido y funcionalidad ante ampliación y ajustes de presentación, conforme a los criterios aplicables.
- Verificación: Contraste, zoom, texto, alternativas y pruebas con tecnologías de asistencia.

## 21. Operación
- **Teclado:** Todas las funciones interactivas DEBEN poder utilizarse mediante teclado cuando corresponda a su plataforma.
- **Foco identificable:** El foco DEBE ser perceptible y no quedar completamente oculto por otros elementos de la interfaz.
- **Tiempo y movimiento:** Las interacciones DEBEN respetar los criterios de accesibilidad relacionados con límites de tiempo, movimiento y control de contenido.
- Verificación: Completar recorridos sin ratón y comprobar orden de foco, controles y recuperación.

## 22. Adaptación
- **Diseño adaptable:** Las pantallas DEBEN reorganizarse según el espacio disponible sin eliminar funcionalidades esenciales.
- **Interacciones accesibles:** Los objetivos interactivos DEBEN cumplir los criterios aplicables de tamaño y separación de WCAG 2.2 AA.
- **Variaciones de uso:** Las experiencias DEBERÍAN considerar dispositivos, métodos de entrada y condiciones operativas diferentes.
- Verificación: Móvil, escritorio, zoom, orientación y métodos de interacción disponibles.

## 26. Tablas
- **Lectura y comparación:** Las tablas DEBEN utilizar encabezados comprensibles, alineación consistente y una organización apropiada para comparar datos.
- **Herramientas proporcionadas:** Búsqueda, filtros, orden y paginación DEBERÍAN incorporarse según el volumen y las tareas reales.
- **Acciones identificables:** Las acciones por registro DEBEN distinguirse de los valores informativos y respetar los permisos correspondientes.
- Verificación: Probar tablas vacías, extensas, filtradas, ordenadas y adaptadas a pantallas pequeñas.

## 29. Dashboards
- **Diseño por tarea:** Los tableros DEBEN priorizar la información necesaria para las decisiones y actividades de sus usuarios.
- **Jerarquía informativa:** Los indicadores NO DEBEN recibir el mismo protagonismo cuando su importancia operativa sea diferente.
- **Profundidad de consulta:** Un tablero PUEDE ofrecer acceso a vistas detalladas, filtros y análisis cuando sean necesarios para completar una tarea.
- Verificación: La persona identifica la información relevante y puede actuar sin recorrer datos irrelevantes.

## 37. Product Default
- **Experiencia predeterminada:** Los productos que utilizan Keyons Product Default DEBEN aplicar los componentes funcionales canónicos y el tema visual predeterminado aprobado.
- **Sobriedad operativa:** Las interfaces de uso frecuente DEBERÍAN priorizar superficies contenidas, claridad y jerarquía antes que recursos expresivos.
- **Personalización controlada:** Las variaciones permitidas DEBEN conservar la accesibilidad, consistencia y comportamiento funcional del producto.
- Verificación: Aplicar el sistema a diferentes productos y comprobar continuidad visual y funcional.

## 44. Validación
- **Tareas reales:** Las evaluaciones DEBEN utilizar tareas representativas de los perfiles que operarán el producto.
- **Evidencia registrada:** Los resultados DEBEN distinguir observaciones, problemas identificados, hipótesis y decisiones posteriores.
- **Problemas críticos:** Los defectos que impidan completar tareas esenciales de forma segura DEBEN resolverse o contar con una decisión explícita de bloqueo antes del lanzamiento correspondiente.
- Verificación: Registrar finalización de tareas, errores, dificultades y resultados de las correcciones.

## Bloque 4 · requisitos tal como se publican (de sus textos base)

Extraídos de las páginas generadas: cada requisito es su texto base; las uniones y los requisitos redactados por Claude se indican en `origen` de `data/sd-normas.json`.


### recursos-visuales-de-interfaz

- **KYN-SDI-FUI-015 Iconos funcionales:** Los iconos DEBEN identificar una acción, estado, categoría o significado comprensible.
- **KYN-SDI-FUI-016 Identidad visual:** Los recursos gráficos DEBEN utilizar las normas oficiales de iconografía, ilustración, fotografía y composición cuando corresponda aplicar la identidad Keyons.
- **KYN-SDI-FUI-017 Expresión proporcionada:** Fotografías, degradados, texturas y otros recursos expresivos NO DEBEN competir con tareas o información esencial.

### componentes-de-estructura

- **KYN-SDI-CPE-008 Contenedores con función:** Paneles, pestañas, acordeones y diálogos DEBEN utilizarse cuando su estructura facilite la comprensión o interacción.
- **KYN-SDI-CPE-009 Jerarquía estable:** El contenido NO DEBE fragmentarse en contenedores adicionales sin una razón funcional o informativa.
- **KYN-SDI-CPE-010 Diálogos:** Un diálogo que interrumpe la tarea DEBE presentar claramente su propósito, las acciones disponibles y la forma de salir.

### retroalimentacion-y-superposiciones

- **KYN-SDI-CPE-011 Resultado visible:** Las acciones que modifican información DEBEN comunicar su resultado o estado de procesamiento.
- **KYN-SDI-CPE-012 Mensajes pertinentes:** La retroalimentación DEBE explicar lo ocurrido sin utilizar mensajes genéricos que impidan comprender el estado real.
- **KYN-SDI-CPE-013 Atención proporcionada:** Las notificaciones DEBERÍAN diferenciarse según urgencia y consecuencias, evitando interrumpir tareas por eventos menores.

### decisiones-y-operaciones-sensibles

- **KYN-SDI-PAT-011 Autorización:** El sistema DEBE comprobar los permisos y las confirmaciones correspondientes al riesgo de la acción.
- **KYN-SDI-PAT-012 Trazabilidad:** Las operaciones críticas DEBEN permitir reconstruir qué ocurrió y bajo qué autorización, según los requisitos de seguridad y auditoría del producto.

### escritura-de-interfaz

- **KYN-SDI-CNT-001 Lenguaje funcional:** Las instrucciones y etiquetas DEBEN indicar con claridad qué puede hacer la persona y qué resultado esperar.
- **KYN-SDI-CNT-002 Consistencia:** Una misma acción o concepto DEBE utilizar una denominación consistente dentro del contexto del producto.
- **KYN-SDI-CNT-003 Brevedad útil:** El contenido DEBERÍA ser tan breve como permita la comprensión, sin eliminar información necesaria.

### mensajes-del-sistema

- **KYN-SDI-CNT-004 Errores comprensibles:** Los mensajes de error DEBEN explicar qué ocurrió y cómo continuar o recuperarse cuando exista una acción posible.
- **KYN-SDI-CNT-005 Confirmaciones específicas:** Los mensajes de éxito DEBEN describir el resultado real y no afirmar acciones que todavía no se hayan completado.
- **KYN-SDI-CNT-006 Información segura:** Los mensajes NO DEBEN exponer información técnica sensible ni datos que la persona no está autorizada a consultar.

### lenguaje-y-localizacion

- **KYN-SDI-CNT-007 Lenguaje adecuado:** Las interfaces DEBEN adaptar idioma, formatos, unidades y convenciones cuando se ofrece una localización específica.
- **KYN-SDI-CNT-008 Consistencia lingüística:** Las traducciones DEBEN conservar el significado funcional de acciones, estados e instrucciones.
- **KYN-SDI-CNT-009 Espacio variable:** Los componentes DEBEN tolerar variaciones razonables de longitud entre idiomas sin perder funcionalidad.

### graficos-de-datos

- **KYN-SDI-DAV-007 Representación apropiada:** El tipo de gráfico DEBE corresponder a la relación que se necesita comunicar.
- **KYN-SDI-DAV-008 Color de datos:** Los gráficos DEBEN respetar las reglas oficiales de paletas categóricas, secuenciales y divergentes según la naturaleza de los datos.
- **KYN-SDI-DAV-009 Interpretación accesible:** La información NO DEBE depender exclusivamente del color ni ocultar unidades, escalas o referencias necesarias.

### indicadores-y-cifras

- **KYN-SDI-DAV-010 Contexto suficiente:** Cada indicador DEBE identificar su significado, unidad, período y referencia cuando sean necesarios para interpretarlo.
- **KYN-SDI-DAV-011 Estados fundamentados:** Los umbrales y colores de evaluación DEBEN responder a criterios definidos, no a límites arbitrarios introducidos por diseño.
- **KYN-SDI-DAV-012 Actualización visible:** La información DEBERÍA indicar cuándo fue actualizada cuando su vigencia afecte una decisión.

### principios-de-experiencia-con-ia

- **KYN-SDI-IAE-001 Transparencia:** Las personas DEBEN poder distinguir qué contenido o acción proviene de capacidades de inteligencia artificial cuando esa distinción afecta la comprensión o decisión.
- **KYN-SDI-IAE-002 Incertidumbre:** El sistema NO DEBE presentar como verificada información generada que no ha sido comprobada.
- **KYN-SDI-IAE-003 Control humano:** Las decisiones automatizadas DEBEN incorporar el nivel de supervisión y autorización correspondiente a su riesgo.

### interfaz-conversacional-de-estela

- **KYN-SDI-IAE-004 Contexto útil:** La conversación DEBE conservar el contexto necesario dentro de los límites de permisos y privacidad aplicables.
- **KYN-SDI-IAE-005 Preguntas pertinentes:** Estela DEBERÍA solicitar únicamente la información adicional necesaria para avanzar con precisión.
- **KYN-SDI-IAE-006 Respuesta accionable:** Las respuestas DEBEN distinguir información, recomendaciones y acciones que el sistema realmente puede ejecutar.

### agentes-y-ejecucion-de-acciones

- **KYN-SDI-IAE-007 Responsabilidad identificable:** Las acciones visibles ejecutadas por agentes DEBEN permitir comprender qué se está haciendo y cuál fue su resultado.
- **KYN-SDI-IAE-008 Límites de actuación:** Los agentes NO DEBEN ejecutar acciones fuera de sus permisos o autorizaciones.
- **KYN-SDI-IAE-009 Identidad pública consistente:** La experiencia PUEDE presentar a Estela como identidad pública de capacidades coordinadas, sin exponer innecesariamente su arquitectura interna.

### seguridad-y-confianza-en-ia

- **KYN-SDI-IAE-010 Confianza calibrada:** Los indicadores de confianza DEBEN corresponder al significado y evidencia definidos para cada estado.
- **KYN-SDI-IAE-011 Verificación humana:** Cuando una decisión requiera aprobación, el sistema DEBE presentar información suficiente para evaluarla antes de continuar.
- **KYN-SDI-IAE-012 Privacidad:** Las interfaces de IA NO DEBEN revelar contenido o contexto de otros usuarios sin autorización.

### base-compartida

- **KYN-SDI-SPR-005 Infraestructura común:** Los productos DEBEN reutilizar componentes, tokens y patrones canónicos cuando exista una solución adecuada a su necesidad.
- **KYN-SDI-SPR-006 Variaciones justificadas:** Las diferencias entre productos DEBERÍAN responder a requisitos funcionales, de contexto o de identidad comprobables.
- **KYN-SDI-SPR-007 Compatibilidad:** Los cambios compartidos DEBEN evaluarse contra las aplicaciones que dependen de ellos.

### sitio-web-corporativo-keyons

- **KYN-SDI-SPR-008 Navegación y propósito:** Las páginas web DEBEN facilitar la localización de información, servicios y acciones relevantes.
- **KYN-SDI-SPR-009 Interacción accesible:** Los formularios, menús y controles del sitio DEBEN respetar las normas funcionales compartidas.

### herramientas-internas-keyons

- **KYN-SDI-SPR-010 Eficiencia operativa:** Las herramientas internas DEBERÍAN priorizar tareas frecuentes, legibilidad y reducción de pasos innecesarios.
- **KYN-SDI-SPR-011 Permisos y contexto:** Cada herramienta DEBE presentar las funciones y datos correspondientes al rol y contexto del operador.

### soluciones-personalizadas-y-white-label

- **KYN-SDI-SPR-012 Identidad del cliente:** Las soluciones de marca blanca PUEDEN sustituir los recursos visuales de Keyons dentro de los límites definidos para el producto.
- **KYN-SDI-SPR-013 Calidad funcional:** La personalización NO DEBE comprometer accesibilidad, seguridad ni patrones de interacción necesarios.
- **KYN-SDI-SPR-014 Ausencia de firma:** Los productos contratados sin firma visible NO DEBEN incorporar elementos de autoría Keyons que contradigan el acuerdo.

### movimiento-operativo

- **KYN-SDI-MOV-001 Movimiento funcional:** Las transiciones operativas DEBEN comunicar cambios de estado o continuidad cuando el movimiento facilite comprender la interacción.
- **KYN-SDI-MOV-002 Duración proporcionada:** El movimiento NO DEBE retrasar innecesariamente la ejecución de tareas.

### movimiento-editorial

- **KYN-SDI-MOV-003 Expresión con propósito:** Los recursos de movimiento editorial PUEDEN utilizarse cuando contribuyan a la narrativa o identidad del producto.
- **KYN-SDI-MOV-004 Comprensión independiente:** La información esencial DEBE poder comprenderse sin depender de una animación decorativa.

### interaccion-multisensorial

- **KYN-SDI-MOV-005 Sonido:** Los sonidos no esenciales PUEDEN habilitarse mediante una preferencia explícita y permanecen desactivados por defecto.
- **KYN-SDI-MOV-006 Háptica:** Las respuestas hápticas PUEDEN utilizarse en dispositivos compatibles cuando aporten una confirmación útil.
- **KYN-SDI-MOV-007 Alternativas:** La información importante NO DEBE depender únicamente de sonido o vibración.

### gobierno-normativo

- **KYN-SDI-GOB-004 Fuente única:** Cada requisito del sistema DEBE tener una fuente normativa identificable y evitar duplicaciones entre capítulos.
- **KYN-SDI-GOB-005 Estado visible:** Las normas DEBEN distinguir claramente su estado de aprobación y versión.

### implementacion-tecnica

- **KYN-SDI-GOB-006 Uso de componentes canónicos:** Las implementaciones DEBEN utilizar los componentes y tokens compartidos cuando sean aplicables.
- **KYN-SDI-GOB-007 Excepciones justificadas:** Las desviaciones DEBEN documentar su necesidad, alcance y condiciones de revisión.
- **KYN-SDI-GOB-008 Entrega comprobable:** Los componentes compartidos DEBEN incluir pruebas de comportamiento, accesibilidad y estados relevantes antes de considerarse listos para reutilización.

### documentacion-y-consulta

- **KYN-SDI-GOB-009 Componentes documentados:** Cada componente canónico DEBE describir propósito, variantes, estados, comportamiento, accesibilidad y restricciones de uso.
- **KYN-SDI-GOB-010 Ejemplos funcionales:** La documentación DEBERÍA ofrecer ejemplos correctos y usos incorrectos cuando ayuden a evitar interpretaciones ambiguas.
- **KYN-SDI-GOB-011 Versionado:** Los cambios relevantes DEBEN mantener trazabilidad y comunicar sus efectos sobre productos existentes.
