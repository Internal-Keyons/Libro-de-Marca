# Sistema de Diseño · base normativa de interfaces (PROPUESTA)

**Estado:** documento de trabajo para revisión de Keylin. Nada de esto está publicado ni vigente. Fecha: 2026-11-12.

**Cómo se armó:** solo con lo que ya existe en el proyecto:
- la arquitectura del libro (`data/sistema-diseno.json`);
- las 52 normas heredadas KYN-PRD-UIX (`normas-ux-sistema-diseno.md`, traslado aprobado el 2026-11-09, en borrador dentro del Sistema de Diseño);
- la tabla «Dónde va cada norma» de ese documento;
- las normas del Libro de Marca que cada módulo ya cita.

No se inventan medidas, sombras, composiciones ni variantes. Lo que pide exploración visual queda marcado como pendiente.

**Marcas de estado:**
- **Heredada:** norma del Manual de Producto con traslado aprobado; conserva su ID.
- **Propuesta:** criterio para aprobar.
- **Pendiente visual:** necesita validación de apariencia.

**Identificadores:**
- Los KYN-PRD-UIX se conservan con su trazabilidad.
- No se emiten normas nuevas KYN-SDI hasta que se resuelva la convención del libro (`docs/CORRESPONDENCIAS_SD.md`).

**Libro de Marca:** es la fuente de identidad. Aquí se cita por ID y no se copia.

## 01 · Principios de experiencia

Define los principios de calidad de experiencia compartidos por las herramientas internas y los productos para clientes.

**Identidad (Libro de Marca, se cita y no se copia):** KYN-MRK-DIS-001 Diseñar con identidad, construir con criterio, KYN-MRK-DIS-002 Identidad, experiencia y sistema: roles definidos, KYN-MRK-DIS-003 Diseño: calma y expresión, KYN-MRK-DIS-004 Intensidad según contexto, KYN-MRK-DIS-005 Claridad antes que complejidad

| Capítulo | Alcance | Normas heredadas | Estado |
| --- | --- | --- | --- |
| 01 Principios comunes | Cinco principios que rigen el diseño de **todos los productos digitales de Keyons**: SaaS de nicho, herramientas internas y desarrollos a medida. Son la base de los demás capítulos de este libro. | UIX-001, UIX-005, UIX-006, UIX-012, UIX-013 | Heredada + criterios propuestos |
| 02 Personas y contextos | Quién usa cada producto, para qué tarea, con qué frecuencia y con cuánta carga. | UIX-007, UIX-008, UIX-009 | Heredada + criterios propuestos |
| 03 Elecciones verificadas | Hipótesis, criterios de aceptación e indicadores para medir la experiencia. | UIX-003, UIX-048 | Heredada + criterios propuestos |

### Criterios verificables de las normas heredadas

**KYN-PRD-UIX-001 · Marco de Arquitectura Biocognitiva Dual: Ergonomía Instintiva y Procesamiento Analítico** (Heredada)
- Criterio de aceptación: Todo producto digital desarrollado por Keyons DEBE estructurarse bajo un modelo de interacción dual que armonice las respuestas neuro-conductuales involuntarias del usuario con los principios de procesamiento cognitivo deliberado. Este marc
- Criterio de aceptación: El diseño de interfaz DEBE alinearse con la forma en que las personas perciben antes de pensar: la atención preatentiva (lo que se nota sin buscarlo, como el color, el tamaño o el movimiento), la economía de esfuerzo (teoría de la carga cog
- Criterio de aceptación: Economía de Esfuerzo Cognitivo: La interfaz DEBE reducir al mínimo el esfuerzo del usuario. Toda tarea repetitiva de captura de datos se transforma en un flujo de propuesta y validación (de creador a revisor). El operador aprueba o corrige 
- Criterio de aceptación: Focalización Pre-Atentiva: El uso del color, la escala y la jerarquía visual DEBE responder a patrones de contraste estricto que dirijan la mirada del operador de forma automática hacia las excepciones operativas, discrepancias o estados de

**KYN-PRD-UIX-005 · Doctrina Operativa: postura Keyons ante decisiones de diseño en conflicto** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-006 · Prohibición taxonómica de patrones oscuros (Dark Patterns)** (Heredada)
- Criterio de aceptación: Fricción asimétrica: prohibido diseñar procesos donde suscribirse toma un clic y desuscribirse toma diez. La reversión de una acción DEBE tener aproximadamente la misma fricción que la activación.
- Criterio de aceptación: Cuando un cliente solicita "algo agresivo" o "más conversiones", el equipo Keyons DEBE identificar cuál de estas alternativas legítimas satisface el objetivo comercial real del cliente. En la mayoría de casos, el objetivo declarado por el c

**KYN-PRD-UIX-012 · Firma UX Keyons: elementos silenciosos obligatorios en todo producto** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-013 · Coherencia obligatoria entre productos del portafolio** (Heredada)
- Criterio de aceptación: Un cliente que adopta un segundo producto Keyons DEBE percibir coherencia experiencial acumulada con el primero, sin necesidad de aprender nuevos patrones. Esta coherencia es activo comercial silencioso: crea lock-in emocional y refuerza pe

**KYN-PRD-UIX-007 · Arquetipos operativos obligatorios por vertical** (Heredada)
- Criterio de aceptación: Todo vertical SaaS y todo proyecto MED de Keyons DEBE declarar formalmente los arquetipos operativos de sus usuarios reales antes de arrancar la Fase Atardecer. Un arquetipo operativo describe al usuario que realmente opera el producto ocho

**KYN-PRD-UIX-008 · Diseño diferenciado por contexto de uso del usuario dentro de la organización cliente** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-009 · Consideración explícita de perfiles atencionales atípicos** (Heredada)
- Criterio de aceptación: El diseño de todo producto Keyons DEBE contemplar explícitamente que una proporción significativa de la población operativa presenta perfiles atencionales atípicos (déficit de atención, hiperactividad, dislexia, ansiedad operativa). Estos u

**KYN-PRD-UIX-003 · Doble Mirada Psicológica aplicada como criterio auditable en cada fase** (Heredada)
- Criterio de aceptación: Durante las cinco fases del Método Prisma, toda decisión de diseño relevante DEBE evaluarse formalmente desde dos ángulos simultáneos que constituyen la Doble Mirada Psicológica del método. Esta evaluación NO es reflexión abstracta: se mate

**KYN-PRD-UIX-048 · Métricas UX obligatorias de éxito por producto** (Heredada)
- Criterio de aceptación: Todo vertical Keyons DEBE monitorear continuamente las siguientes métricas UX de éxito durante la Fase Galaxia. Los resultados alimentan las decisiones de mejora del producto y el aprendizaje sistemático entre proyectos.

## 02 · Arquitectura y navegación

Establece cómo se organiza la información y cómo las personas se desplazan por las aplicaciones.

**Identidad (Libro de Marca, se cita y no se copia):** KYN-MRK-ESP-004 Retícula y responsive, KYN-MRK-CMP-001 Componer según el contenido, KYN-MRK-ESP-006 Diagramas de información

| Capítulo | Alcance | Normas heredadas | Estado |
| --- | --- | --- | --- |
| 04 Información | Mapas de contenido, taxonomías y relaciones entre la información. | UIX-028 | Heredada + criterios propuestos |
| 05 Navegación | Estructura base de aplicación, menús, cabeceras, rutas y niveles. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 06 Búsqueda | Búsqueda, filtros y orientación sobre dónde se está y cómo continuar. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |

### Criterios verificables de las normas heredadas

**KYN-PRD-UIX-028 · Aplicación operativa de revelación progresiva y jerarquía de la decisión** (Heredada)
- Criterio de aceptación: En cada pantalla operativa, el usuario DEBE tener frente a sí solo la información y las opciones necesarias para tomar la próxima decisión esperada. La información complementaria y las opciones avanzadas se relegan a capas secundarias de in
- Criterio de aceptación: Criterio de auditoría vinculado: un evaluador externo sin conocimiento del vertical DEBE poder identificar en cada pantalla cuál es la próxima acción esperada en menos de 5 segundos.

## 03 · Fundamentos de interfaz

Traduce los fundamentos visuales de Marca a reglas técnicas y visuales aplicables a interfaces.

**Identidad (Libro de Marca, se cita y no se copia):** KYN-MRK-COL-012 Modo interfaz, KYN-MRK-COL-013 Grises tipográficos, KYN-MRK-TYP-006 Uso por función, KYN-MRK-ESP-001 Lenguaje geométrico Keyons, KYN-MRK-ESP-002 Sistema de radios y curvaturas, KYN-MRK-ESP-003 Sistema de espaciado, KYN-MRK-ICO-003 Uso

| Capítulo | Alcance | Normas heredadas | Estado |
| --- | --- | --- | --- |
| 07 Tokens | Tokens base, semánticos y de componente; nomenclatura, temas y versiones. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 08 Color funcional | Superficies, texto, bordes, interacción, foco, estados y contraste. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 09 Tipografía | Familias oficiales aplicadas a interfaz: jerarquías, escalas y cifras. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 10 Espacio y retícula | Retículas, puntos de adaptación, espaciado, densidad y esquinas. | UIX-029 | Heredada + criterios propuestos |
| 11 Recursos visuales | Iconografía funcional, bordes, sombras, elevación e imágenes aplicadas. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |

### Criterios verificables de las normas heredadas

**KYN-PRD-UIX-029 · Densidad visual: modo cómodo y modo denso con default por vertical** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

## 04 · Componentes y estados

Define los componentes reutilizables y sus variantes. Aquí se documentan las piezas, mientras que los flujos completos pertenecen a Patrones de interacción.

**Identidad (Libro de Marca, se cita y no se copia):** KYN-MRK-COL-014 Estados del sistema, KYN-MRK-COL-015 Acción y superficies, KYN-MRK-ESP-002 Sistema de radios y curvaturas, KYN-MRK-ILU-004 Transparencia y superposición

| Capítulo | Alcance | Normas heredadas | Estado |
| --- | --- | --- | --- |
| 12 Acciones | Botones, enlaces, menús y sus estados de disponibilidad y proceso. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 13 Entradas | Campos, selectores, casillas, interruptores, fechas y archivos. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 14 Estructura | Pestañas, tablas, listas, contenedores y contenido expandible. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 15 Retroalimentación | Alertas, etiquetas de estado, diálogos, paneles e indicadores de carga. | UIX-030, UIX-046 | Heredada + criterios propuestos |

### Criterios verificables de las normas heredadas

**KYN-PRD-UIX-030 · Jerarquía de urgencia de notificaciones y prohibición de fatiga por alertas** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-046 · Modalidades de feedback multimodal según urgencia y contexto** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

## 05 · Patrones de interacción

Define cómo se combinan los componentes para resolver tareas y procesos completos.

**Identidad (Libro de Marca, se cita y no se copia):** KYN-MRK-DIS-004 Intensidad según contexto, KYN-MRK-DIS-005 Claridad antes que complejidad, KYN-MRK-CMP-001 Componer según el contenido

| Capítulo | Alcance | Normas heredadas | Estado |
| --- | --- | --- | --- |
| 16 Formularios | Estructura, ayuda contextual, validación y formularios de varios pasos. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 17 Flujos de trabajo | Crear, editar, guardar, eliminar y continuar tareas sin perder trabajo. | UIX-027, UIX-031, UIX-044 | Heredada + criterios propuestos |
| 18 Recuperación | Estados vacíos y de espera, reintentos, deshacer y errores. | UIX-021, UIX-022, UIX-023, UIX-024, UIX-025, UIX-026 | Heredada + criterios propuestos |
| 19 Procesos críticos | Confirmaciones de alto impacto, permisos y trazabilidad de acciones. | UIX-014, UIX-015 | Heredada + criterios propuestos |

### Criterios verificables de las normas heredadas

**KYN-PRD-UIX-027 · Micro-momentos de satisfacción operativa por cierre de ciclo** (Heredada)
- Criterio de aceptación: Toda acción completada exitosamente por el usuario en un producto Keyons DEBE ir acompañada de una micro-transición de confirmación que active la percepción de logro y cierre de ciclo. Estas micro-transiciones no son decoración: son aplicac

**KYN-PRD-UIX-031 · Ritmo de progresión en flujos multi-paso** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-044 · Tour guiado obligatorio de primera vez con lógica contextual** (Heredada)
- Criterio de aceptación: Todo producto Keyons DEBE ofrecer al usuario, en su primer acceso, un tour guiado interactivo que explique las funciones principales sin necesidad de consultar manuales externos. El tour cumple tres reglas obligatorias.

**KYN-PRD-UIX-021 · Protocolo de espera y percepción de responsividad** (Heredada)
- Criterio de aceptación: La percepción de responsividad de un sistema se decide en los primeros 400 milisegundos (umbral de Doherty). Superado ese umbral, el usuario transita de confianza tácita a duda activa; si nada visible confirma que el sistema procesa, la dud

**KYN-PRD-UIX-022 · Lenguaje humano obligatorio en mensajes de espera** (Heredada)
- Criterio de aceptación: Cuando el tiempo de espera supera 3 segundos y se activa mensaje descriptivo conforme a KYN-PRD-UIX-021, el mensaje DEBE describir qué está haciendo el sistema en lenguaje humano orientado a la acción, nunca con jerga técnica ni con loaders
- Criterio de aceptación: En operaciones que superan 10 segundos, el mensaje descriptivo DEBE evolucionar con detalle progresivo, no permanecer estático. La mente humana interpreta un mensaje estático prolongado como señal de que el sistema colgó.

**KYN-PRD-UIX-023 · Protocolo de fallo del sistema con ruta alternativa obligatoria** (Heredada)
- Criterio de aceptación: Cuando un componente automatizado por IA o una integración externa falla, la interfaz DEBE ofrecer al menos una ruta alternativa manual visible en el mismo componente donde ocurrió el fallo. Esta regla es dura y no admite excepciones por co
- Criterio de aceptación: Si la verificación automática de pago con SINPE falla, el usuario DEBE poder adjuntar comprobante manualmente en el mismo momento y en el mismo componente, sin abandonar la pantalla.
- Criterio de aceptación: Si el agente de IA no puede clasificar un lead, el usuario DEBE poder clasificarlo manualmente con opciones predefinidas visibles en el mismo componente.
- Criterio de aceptación: Si la extracción automática de datos de un documento falla, el usuario DEBE poder ingresar los datos manualmente en el mismo flujo, sin reiniciar la operación.

**KYN-PRD-UIX-024 · Estructura tripartita obligatoria de mensajes de error** (Heredada)
- Criterio de aceptación: Todo mensaje de error visible al usuario final DEBE cumplir la siguiente estructura fija de tres partes. Los códigos técnicos crudos ("Error 502", "NullPointerException", stack traces) están estrictamente prohibidos en la capa visible al us

**KYN-PRD-UIX-025 · Reversibilidad como red de seguridad emocional operativa** (Heredada)
- Criterio de aceptación: Toda acción destructiva o significativa que el usuario pueda ejecutar por error DEBE ser reversible o requerir confirmación explícita antes de ejecutarse. La interfaz se diseña asumiendo que los usuarios cometerán errores; el objetivo no es

**KYN-PRD-UIX-026 · Diseño obligatorio de estados vacíos como oportunidad de guía** (Heredada)
- Criterio de aceptación: Los estados vacíos NO se muestran nunca como pantalla en blanco, mensaje genérico "Sin datos" o pantalla de error. Todo estado vacío DEBE diseñarse como oportunidad de guía al usuario, cumpliendo tres reglas obligatorias.

**KYN-PRD-UIX-014 · Matriz de decisión Human-in-the-Loop por riesgo e irreversibilidad** (Heredada)
- Criterio de aceptación: Toda acción ejecutable por un agente automatizado o por decisión asistida por IA DEBE clasificarse en uno de cuatro niveles de Human-in-the-Loop según la combinación de riesgo operativo y grado de irreversibilidad de la acción. La clasifica
- Criterio de aceptación: | Nivel 3 - Aprobación previa obligatoria | Riesgo medio, reversible con esfuerzo. El sistema prepara la acción y muestra opciones "Aprobar / Editar / Descartar". El usuario DEBE confirmar antes de ejecutar. | Enviar correo automatizado al 

**KYN-PRD-UIX-015 · Personalización del HITL por vertical y por cliente: límites operativos** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

## 06 · Accesibilidad y adaptación

Establece los requisitos de accesibilidad y adaptación, tomando WCAG 2.2 nivel AA como referencia de cumplimiento.

**Identidad (Libro de Marca, se cita y no se copia):** KYN-MRK-COL-005 Combinaciones, KYN-MRK-VIS-008 Contraste insuficiente, capítulo 16 Accesibilidad

| Capítulo | Alcance | Normas heredadas | Estado |
| --- | --- | --- | --- |
| 20 Percepción | Contraste, información más allá del color, zoom y espaciado de texto. | UIX-038 | Heredada + criterios propuestos |
| 21 Operación | Teclado, foco, lectores de pantalla y objetivos táctiles. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 22 Adaptación | Dispositivos, preferencias del sistema y distintas capacidades de uso. | UIX-039 | Heredada + criterios propuestos |

### Criterios verificables de las normas heredadas

**KYN-PRD-UIX-038 · Cumplimiento mínimo WCAG 2.2 nivel AA** (Heredada)
- Criterio de aceptación: Todo producto Keyons DEBE cumplir con las Web Content Accessibility Guidelines versión 2.2 en nivel AA como mínimo, respetando los cuatro principios rectores del estándar: perceptible, operable, comprensible y robusto.
- Criterio de aceptación: Contraste de color mínimo: relación 4.5:1 para texto normal y 3:1 para texto grande.
- Criterio de aceptación: Tamaño de fuente mínimo operativo: equivalente a 16 píxeles para texto de cuerpo en interfaces web y proporcional en aplicaciones móviles.
- Criterio de aceptación: Navegación completa por teclado: toda funcionalidad accesible sin uso de ratón, con indicador visual claro del elemento con foco activo.

**KYN-PRD-UIX-039 · Adaptación operativa a contextos móvil y escritorio** (Heredada)
- Criterio de aceptación: Todo producto Keyons cuya operación esperada incluya uso móvil DEBE ofrecer experiencia diseñada específicamente para pantalla táctil y contexto de uso móvil, no una versión reducida de la interfaz de escritorio.
- Criterio de aceptación: Áreas táctiles mínimo 44x44 píxeles conforme a estándares WCAG táctiles.

## 07 · Contenido y comunicación

Aplica los principios de voz y claridad a los mensajes de las interfaces.

**Identidad (Libro de Marca, se cita y no se copia):** KYN-MRK-VOZ-001 Esencia de la voz, KYN-MRK-VOZ-002 Reglas de escritura, KYN-MRK-VOZ-003 Vocabulario propio, KYN-MRK-VOZ-004 Vocabulario que evitamos, KYN-MRK-VOZ-007 De lo técnico a lo humano

| Capítulo | Alcance | Normas heredadas | Estado |
| --- | --- | --- | --- |
| 23 Escritura | Etiquetas, llamadas a la acción, instrucciones y textos de ayuda. | UIX-041 | Heredada + criterios propuestos |
| 24 Mensajes | Confirmaciones, progreso, errores, advertencias y estados vacíos. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 25 Localización | Terminología, idiomas, adaptación regional y tono de cada producto. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |

### Criterios verificables de las normas heredadas

**KYN-PRD-UIX-041 · Reglas de microcopy: botones, etiquetas y llamadas a acción** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

## 08 · Datos y visualización

Define cómo presentar información cuantitativa y operativa sin comprometer la interpretación.

**Identidad (Libro de Marca, se cita y no se copia):** KYN-MRK-DAT-001 Principios, KYN-MRK-DAT-002 Sistema cromático, KYN-MRK-DAT-003 Tipografía en gráficos, KYN-MRK-DAT-004 Tipos de gráfico, KYN-MRK-DAT-005 Estructura

| Capítulo | Alcance | Normas heredadas | Estado |
| --- | --- | --- | --- |
| 26 Tablas | Columnas, orden, filtros, paginación y densidad de tablas. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 27 Gráficos | Tipo de gráfico, paletas, escalas, leyendas y accesibilidad. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 28 Indicadores | Formatos numéricos, unidades, variaciones y datos incompletos. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 29 Dashboards | Tableros organizados por tareas, exploración y exportación de resultados. | UIX-037 | Heredada + criterios propuestos |

### Criterios verificables de las normas heredadas

**KYN-PRD-UIX-037 · Exportación nativa de historial operativo en formatos estructurados** (Heredada)
- Criterio de aceptación: El usuario DEBE tener capacidad nativa de exportar los historiales de chat, logs de auditoría y registros operativos de su tenant en formatos estructurados estándar (CSV y JSON como mínimo, más el formato específico del vertical cuando apli

## 09 · Experiencias con IA y Estela

Define la interacción con IA. La identidad y personalidad de Estela se documentarán en el Libro de Marca; aquí se definirá cómo se aplican en productos.

**Identidad (Libro de Marca, se cita y no se copia):** KYN-MRK-VOZ-005 El trato, KYN-MRK-ADN-007 Principios de marca, capítulo 05 Estela

| Capítulo | Alcance | Normas heredadas | Estado |
| --- | --- | --- | --- |
| 30 Principios de IA | Capacidades, límites, fuentes y control del usuario frente a la IA. | UIX-001, UIX-005, UIX-006, UIX-012, UIX-013, UIX-016, UIX-017, UIX-018, UIX-019, UIX-020 | Heredada + criterios propuestos |
| 31 Conversación | Cómo se aplica Estela en la conversación: mensajes, archivos e historial. | UIX-034, UIX-035, UIX-042, UIX-043 | Heredada + criterios propuestos |
| 32 Agentes | Agentes, planificación, aprobaciones y registro de cada ejecución. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 33 Confianza segura | Privacidad, acceso, escalamiento humano y acciones automáticas visibles. | UIX-032, UIX-033, UIX-036 | Heredada + criterios propuestos |

### Criterios verificables de las normas heredadas

**KYN-PRD-UIX-001 · Marco de Arquitectura Biocognitiva Dual: Ergonomía Instintiva y Procesamiento Analítico** (Heredada)
- Criterio de aceptación: Todo producto digital desarrollado por Keyons DEBE estructurarse bajo un modelo de interacción dual que armonice las respuestas neuro-conductuales involuntarias del usuario con los principios de procesamiento cognitivo deliberado. Este marc
- Criterio de aceptación: El diseño de interfaz DEBE alinearse con la forma en que las personas perciben antes de pensar: la atención preatentiva (lo que se nota sin buscarlo, como el color, el tamaño o el movimiento), la economía de esfuerzo (teoría de la carga cog
- Criterio de aceptación: Economía de Esfuerzo Cognitivo: La interfaz DEBE reducir al mínimo el esfuerzo del usuario. Toda tarea repetitiva de captura de datos se transforma en un flujo de propuesta y validación (de creador a revisor). El operador aprueba o corrige 
- Criterio de aceptación: Focalización Pre-Atentiva: El uso del color, la escala y la jerarquía visual DEBE responder a patrones de contraste estricto que dirijan la mirada del operador de forma automática hacia las excepciones operativas, discrepancias o estados de

**KYN-PRD-UIX-005 · Doctrina Operativa: postura Keyons ante decisiones de diseño en conflicto** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-006 · Prohibición taxonómica de patrones oscuros (Dark Patterns)** (Heredada)
- Criterio de aceptación: Fricción asimétrica: prohibido diseñar procesos donde suscribirse toma un clic y desuscribirse toma diez. La reversión de una acción DEBE tener aproximadamente la misma fricción que la activación.
- Criterio de aceptación: Cuando un cliente solicita "algo agresivo" o "más conversiones", el equipo Keyons DEBE identificar cuál de estas alternativas legítimas satisface el objetivo comercial real del cliente. En la mayoría de casos, el objetivo declarado por el c

**KYN-PRD-UIX-012 · Firma UX Keyons: elementos silenciosos obligatorios en todo producto** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-013 · Coherencia obligatoria entre productos del portafolio** (Heredada)
- Criterio de aceptación: Un cliente que adopta un segundo producto Keyons DEBE percibir coherencia experiencial acumulada con el primero, sin necesidad de aprender nuevos patrones. Esta coherencia es activo comercial silencioso: crea lock-in emocional y refuerza pe

**KYN-PRD-UIX-016 · Comunicación tripartita de confianza del modelo** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-017 · Transparencia obligatoria del modo copiloto vs. autopiloto** (Heredada)
- Criterio de aceptación: El usuario DEBE poder identificar en cualquier momento si el sistema opera en modo autopiloto (actuando autónomamente) o en modo copiloto (esperando aprobación humana). Un indicador visual permanente y discreto en la interfaz declara el mod

**KYN-PRD-UIX-018 · Gestión de expectativas del usuario ante IA probabilística** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-019 · Explicabilidad activada por materialidad del impacto** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-020 · Estructura obligatoria del panel de explicación de decisión de IA** (Heredada)
- Criterio de aceptación: Cuando la interfaz muestra explicación de una decisión (Nivel Bajo Demanda o Nivel Obligatorio conforme a KYN-PRD-UIX-019), el panel de explicación DEBE contener tres secciones en orden fijo, aplicando revelación progresiva.

**KYN-PRD-UIX-034 · Memoria conversacional en tres niveles con controles diferenciados** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-035 · Controles de olvido y transparencia sobre memoria acumulada** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-042 · Reglas de calibración lingüística en respuestas del agente IA** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-043 · Manejo lingüístico de fallos y respuestas de \** (Heredada)
- Criterio de aceptación: Cuando el modelo no tiene información suficiente para responder con calidad, la respuesta DEBE ser honesta y orientar al usuario hacia una alternativa productiva. Prohibidas las respuestas evasivas, las alucinaciones para "salvar" la respue

**KYN-PRD-UIX-032 · Visibilidad de fuentes RAG según sensibilidad regulatoria del vertical** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-033 · Acceso al prompt: restringido al administrador del tenant** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-036 · Restricciones del cliente sobre procesamiento con LLMs externos** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

## 10 · Sistemas de producto

Define las diferentes aplicaciones del sistema de diseño, con fundamentos compartidos y expresiones visuales distintas.

**Identidad (Libro de Marca, se cita y no se copia):** KYN-MRK-DIS-002 Identidad, experiencia y sistema: roles definidos, KYN-MRK-PER-001 Tres modelos, KYN-MRK-PER-002 Modelo A · SaaS, KYN-MRK-PER-003 Modelo B · Boutique, KYN-MRK-PER-004 Modelo C · Marca blanca

| Capítulo | Alcance | Normas heredadas | Estado |
| --- | --- | --- | --- |
| 34 Base compartida | Estándares UX comunes, componentes reutilizables y herencia de temas. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 35 Sitio web | La identidad corporativa en el sitio web: navegación, composición y acciones. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 36 Herramientas | Identidad operativa, navegación por roles y espacios de trabajo densos. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 37 Product Default | Estética neutral premium, estructura SaaS y opciones de configuración. | UIX-045, UIX-052 | Heredada + criterios propuestos |
| 38 White-label | Identidades de clientes, marca blanca y límites de personalización. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |

### Criterios verificables de las normas heredadas

**KYN-PRD-UIX-045 · Frontera obligatoria entre elementos personalizables y elementos fijos** (Heredada)
- Criterio de aceptación: En cada producto Keyons, la interfaz contiene dos tipos de elementos claramente diferenciados por naturaleza. Esta frontera DEBE declararse formalmente antes del lanzamiento del producto.
- Criterio de aceptación: Elementos que el administrador del tenant PUEDE modificar desde el panel de configuración del vertical, para adaptar la interfaz a su operación. Ejemplos típicos: items visibles del menú lateral, orden de columnas de tablas, campos visibles

**KYN-PRD-UIX-052 · Márgenes de personalización por modalidad de contratación** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

## 11 · Movimiento e interacción sensorial

Regula el movimiento y los recursos sensoriales, sin convertirlos en requisitos decorativos.

**Identidad (Libro de Marca, se cita y no se copia):** KYN-MRK-ICO-004 Animación, KYN-MRK-ILU-006 Ráfagas de color, capítulo 15 Movimiento

| Capítulo | Alcance | Normas heredadas | Estado |
| --- | --- | --- | --- |
| 39 Operación activa | Transiciones funcionales, retroalimentación, progreso y sus límites. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 40 Movimiento editorial | Entradas, cambios de escena y movimiento atmosférico según el contexto. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |
| 41 Multisensorial | Sonido, respuesta háptica y atajos del sistema operativo. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |

Sin normas heredadas en este módulo: todo su contenido queda **pendiente de definición**.

## 12 · Calidad y gobierno del diseño

Establece cómo se gestionan, implementan, prueban y mantienen las reglas del Sistema de Diseño.

**Identidad (Libro de Marca, se cita y no se copia):** KYN-MRK-REF-001 Nomenclatura, KYN-MRK-REF-002 Índice, KYN-MRK-VIS-001 Jerarquía visual repetitiva, KYN-MRK-VIS-009 Lenguaje genérico, KYN-MRK-VIS-012 Composición no intercambiable

| Capítulo | Alcance | Normas heredadas | Estado |
| --- | --- | --- | --- |
| 42 Gobierno normativo | Fuente oficial, identificadores permanentes, aprobación y cambios. | UIX-010, UIX-011, UIX-051 | Heredada + criterios propuestos |
| 43 Implementación | Tokens y componentes en código, especificaciones y versiones. | UIX-002, UIX-004 | Heredada + criterios propuestos |
| 44 Validación | Verificación visual, funcional, de usabilidad y de accesibilidad. | UIX-047, UIX-049, UIX-050 | Heredada + criterios propuestos |
| 45 Documentación | Catálogo de normas, exportación para personas e IA y permisos. | — | Pendiente: sin norma; requiere definición (y validación visual si toca apariencia) |

### Criterios verificables de las normas heredadas

**KYN-PRD-UIX-010 · Frontera formal entre Manual de Marca y Manual de Producto UIX** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-011 · Sistema de diseño Keyons: tokens funcionales, componentes canónicos y patrones de flujo** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-051 · Sistema de aprendizaje sistemático entre proyectos** (Heredada)
- Criterio de aceptación: Cada proyecto Keyons DEBE contribuir formalmente al Sistema de Aprendizaje UX de la empresa durante y al cierre de cada fase del Método Prisma. Este sistema es lo que materializa el diferenciador declarado en KYN-PRD-UIX-004 y capitaliza el

**KYN-PRD-UIX-002 · Método Prisma Keyons: fases obligatorias del proceso de diseño** (Heredada)
- Criterio de aceptación: Divergencia amplia de rutas de solución seguida de convergencia sobre la más viable, prototipado y validación con usuarios reales. Aplican tres reglas del método: (a) toda propuesta que incorpore IA DEBE compararse formalmente contra altern

**KYN-PRD-UIX-004 · Diferenciadores estructurales del Método Prisma frente al doble diamante estándar** (Heredada)
- Criterio de aceptación: IA como opción, no como default: En la Fase Anochecer, toda propuesta que incorpore IA DEBE compararse formalmente contra al menos una alternativa de solución determinista. La elección de IA se justifica por aporte de valor diferencial clar

**KYN-PRD-UIX-047 · Protocolo obligatorio de usability testing pre-lanzamiento** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-049 · Auditoría UX interna por ciclo de revisión del manual** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

**KYN-PRD-UIX-050 · Checklist obligatorio de auditoría UX pre-lanzamiento** (Heredada)
- Criterio de aceptación: por redactar a partir del texto de la norma (Propuesta)

## Normas heredadas sin capítulo asignado automáticamente

KYN-PRD-UIX-040

## Propuestas existentes que Keylin aún no decide (del traslado)

Propuestas pendientes (NO aplicadas)

Keylin decide cada una. Hasta entonces, vale el texto original.

| N.º | Norma | Propuesta |
| --- | --- | --- |
| P1 | UIX-010 | La frontera ahora es entre el **libro de marca** (cómo se ve) y el **Sistema de Diseño** (cómo se comporta y cómo se construye). Hay que reescribir los títulos «Materia del Manual de Marca» y «Materia de este capítulo UIX» |
| P2 | UIX-044 | El recorrido de 2 a 5 minutos pasa a un recorrido corto de 3 a 5 pasos, más una lista de primeros pasos y estados vacíos que enseñan. Se mantienen los mini-recorridos por módulo |
| P3 | UIX-030 y UIX-046 | Fusionarlas en una sola norma de urgencia de notificaciones: hoy dicen lo mismo |
| P4 | Todas | Los ID KYN-PRD-UIX pertenecen al Manual de Producto. Decidir con Oscar el código del Sistema de Diseño. Los ID viejos quedan como «trasladada a…» y nunca se reutilizan |
| P5 | Nueva | **Siete estados obligatorios** en todo elemento interactivo: reposo, cursor encima, foco de teclado, presionado, seleccionado, deshabilitado y cargando. El foco de teclado siempre visible |

## Decisiones de apariencia pendientes de validación visual

- Tokens de diseño, color funcional, tipografía aplicada, espacio y retícula de interfaz (módulo Fundamentos de interfaz).
- Estados visuales de los componentes (siete estados de la propuesta P5): su apariencia concreta.
- Movimiento operativo y editorial: duraciones y curvas propias de interfaz, si difieren de las del Libro de Marca.
- Estética de Estela en la interfaz conversacional.

Estas decisiones se explorarán más adelante en el espacio experimental, que todavía no se construye. No se aprueban de forma automática.

