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
