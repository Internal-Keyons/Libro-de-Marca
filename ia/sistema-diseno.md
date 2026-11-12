---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# Capítulo 01 · Principios comunes

## KYN-PRD-UIX-001 · Marco de Arquitectura Biocognitiva Dual: Ergonomía Instintiva y Procesamiento Analítico

Todo producto digital desarrollado por Keyons **DEBE** estructurarse bajo un modelo de interacción dual que armonice las respuestas neuro-conductuales involuntarias del usuario con los principios de procesamiento cognitivo deliberado. Este marco es la doctrina operativa aplicada durante las cinco fases del Método Prisma.

#### ***Capa 1 — Atención preatentiva y ergonomía instintiva (atención involuntaria)***

El diseño de interfaz **DEBE** alinearse con la forma en que las personas perciben antes de pensar: la atención preatentiva (lo que se nota sin buscarlo, como el color, el tamaño o el movimiento), la economía de esfuerzo (teoría de la carga cognitiva, Ley de Hick, Ley de Fitts) y la necesidad de cerrar tareas abiertas (efecto Zeigarnik).

* **Economía de Esfuerzo Cognitivo:** La interfaz **DEBE** reducir al mínimo el esfuerzo del usuario. Toda tarea repetitiva de captura de datos se transforma en un flujo de propuesta y validación (de creador a revisor). El operador aprueba o corrige lo que el sistema propuso, no rellena desde cero.  
* **Focalización Pre-Atentiva:** El uso del color, la escala y la jerarquía visual **DEBE** responder a patrones de contraste estricto que dirijan la mirada del operador de forma automática hacia las excepciones operativas, discrepancias o estados de riesgo, sin obligarlo a rastrear activamente la pantalla.  
* **Aceleración por Retroalimentación Sensorial:** Toda acción completada con éxito dentro del sistema **DEBE** ofrecer una respuesta visual o auditiva inmediata y fluida que confirme la transición de estado, activando la percepción de logro y efectividad operacional.

#### ***Capa 2 — Ergonomía de Interacción Digital (Procesamiento Deliberado)***

Simultáneamente, la interfaz **DEBE** aplicar los principios comprobados de la Ciencia de la Interacción Humano-Computadora (HCI) para estructurar la información compleja de forma comprensible.

* **Minimización de Carga Extrínseca:** Queda prohibido recargar la interfaz con elementos decorativos o redundantes que compitan por la memoria de trabajo del usuario. Cada componente visible **DEBE** justificar su presencia por aporte directo a la decisión que el usuario toma en ese momento.  
* **Arquitectura de Revelación Progresiva:** La información detallada y los parámetros técnicos profundos **DEBEN** mantenerse ocultos bajo capas secundarias de interacción, mostrándose únicamente cuando el contexto operativo lo exija.  
* **Alineación con Modelos Mentales:** Los patrones de navegación, botones y estados del sistema **DEBEN** respetar las convenciones consolidadas de la industria para evitar curvas de aprendizaje innecesarias. Innovar donde aporta valor operativo real; respetar convención donde el usuario espera lo estándar.

#### ***Capa 3 — Confluencia Operativa: Simbiosis entre Atención y Juicio Crítico***

El sello diferenciador del UX en Keyons radica en el equilibrio ético y funcional de ambas capas anteriores.

* **Prohibición de Patrones Oscuros (Dark Patterns):** queda estrictamente prohibida la utilización de mecanismos de retención pasiva o de recompensa artificial (comunes en redes sociales o videojuegos) diseñados para adormecer el criterio del usuario o prolongar el tiempo de uso de forma artificial. La lista taxonómica de patrones oscuros prohibidos se detalla en KYN-PRD-UIX-006.  
* **Foco Involuntario para Criterio Consciente:** la capa instintiva se utiliza exclusivamente para atraer el foco de atención hacia el punto exacto de la interfaz, mientras que la capa ergonómica prepara la información para que el usuario tome una decisión humana informada y analítica. Toda captura de atención **DEBE** acompañarse de decisión activa consciente, nunca de consumo pasivo.

Criterio de auditoría UX pre-lanzamiento vinculado a esta norma: un evaluador externo, sin conocimiento previo del producto, DEBE poder identificar qué acción se espera del usuario en cada pantalla dentro de los primeros 5 segundos de observación. Si no lo logra, la interfaz no cumple con el marco biocognitivo dual.

## KYN-PRD-UIX-013 · Coherencia obligatoria entre productos del portafolio

Un cliente que adopta un segundo producto Keyons **DEBE** percibir coherencia experiencial acumulada con el primero, sin necesidad de aprender nuevos patrones. Esta coherencia es activo comercial silencioso: crea lock-in emocional y refuerza percepción de marca operativa fuerte.

#### ***Criterios operativos de coherencia entre productos***

* Los tokens funcionales del sistema de diseño se aplican idénticamente en todos los productos activos.  
* Los componentes canónicos se comportan igual en todos los productos.  
* Los patrones de flujo comunes siguen la misma secuencia en todos los productos.  
* El agente Estela mantiene identidad y comportamiento consistentes en todos los verticales.

## KYN-PRD-UIX-005 · Doctrina Operativa: postura Keyons ante decisiones de diseño en conflicto

Cuando dos principios de diseño válidos entren en conflicto durante un proyecto, Keyons adopta las siguientes posturas doctrinarias como criterio de decisión operativa. Estas posturas se citan formalmente cuando un diseñador debe justificar por qué eligió una alternativa sobre otra.

* **Cuando fluidez y transparencia compitan, gana transparencia:** La fluidez sin transparencia es manipulación. Prohibido ocultar un paso operativo con la excusa de "hacer más rápido" el flujo.  
* **Cuando automatización y control del usuario compitan, gana control:** El usuario preserva capacidad de intervenir, revertir y decidir. La automatización sirve al usuario, no al revés.  
* **Cuando eficiencia y comprensión compitan, gana comprensión:** Un flujo rápido que el usuario no entiende genera pánico operativo, no valor.  
* **Cuando estética y ergonomía compitan, gana ergonomía:** Una interfaz bella pero cansada de operar es una interfaz fallida. La belleza sirve a la función, no la sustituye.  
* **Cuando innovación y convención compitan, gana convención salvo aporte comprobado:** Respetar el modelo mental del usuario reduce curva de aprendizaje. Innovar donde aporta valor operativo real; imitar convención donde el usuario espera lo estándar.

## KYN-PRD-UIX-006 · Prohibición taxonómica de patrones oscuros (Dark Patterns)

Los patrones oscuros son diseños que manipulan al usuario para tomar decisiones contrarias a su interés. Están estrictamente prohibidos en todo producto Keyons sin excepción, independientemente de que aumenten métricas comerciales de corto plazo. La siguiente lista taxonómica es exhaustiva y su violación constituye motivo suficiente para bloquear lanzamiento de un producto.

* **Confirmación con doble negación (Confirmshaming):** Prohibido redactar botones de rechazo con frases que hagan sentir culpable al usuario ("No, no quiero mejorar mi negocio"). Los rechazos son neutros y respetuosos.  
* **Botones destructivos disfrazados de acción positiva:** Prohibido usar color verde o etiquetas positivas para botones que ejecutan acciones destructivas o cobros. El color y la etiqueta comunican la naturaleza real de la acción.  
* **Countdown timers artificiales:** Prohibido crear urgencia falsa con temporizadores que presionan decisiones sin razón operativa real. Solo se admiten temporizadores cuando corresponden a un límite operativo genuino.  
* **Fricción asimétrica:** prohibido diseñar procesos donde suscribirse toma un clic y desuscribirse toma diez. La reversión de una acción **DEBE** tener aproximadamente la misma fricción que la activación.  
* **Opt-in preseleccionado en decisiones sensibles:** Prohibido dejar casillas premarcadas para consentimientos que impliquen compartir datos, activar cobros recurrentes o autorizar procesamientos con LLMs externos. El opt-in sensible siempre requiere acción explícita del usuario.  
* **Sobre-notificación diseñada para retención:** Prohibidas notificaciones sin propósito operativo real cuyo único objetivo sea traer al usuario de vuelta al producto.  
* **Scroll infinito o autoplay sin control:** Prohibidos en cualquier producto Keyons. Todo contenido de página o se controla explícitamente por el usuario. Los productos Keyons son herramientas operativas, no plataformas de consumo pasivo.

#### ***Estrategia comercial legítima vs. patrón oscuro: cómo distinguirlos***

Existen mecanismos comerciales legítimos que Keyons SÍ implementa cuando el cliente los requiere, y que logran el mismo resultado comercial que un patrón oscuro sin manipular al usuario contra su interés. La diferencia clave es simple: el patrón oscuro engaña o manipula; la estrategia comercial legítima destaca valor real y crea urgencia real.

* **Countdown real basado en límite operativo genuino:** "La promoción vence el 30 de junio a las 23:59" es válido si la promoción efectivamente vence en esa fecha. Se prohíbe el temporizador que se resetea al recargar la página.  
* **Copy persuasivo que resalta valor comprobable:** "Únete a más de 5.000 empresas que optimizaron su facturación" es válido si el número es real. Se prohíbe la prueba social inventada.  
* **Notificaciones con propósito operativo real:** "Tu suscripción vence en 3 días" es válido. Se prohíbe la notificación diseñada solo para traer al usuario de vuelta al producto sin propósito operativo.  
* **Escasez real y verificable:** "Quedan 3 cupos en el próximo evento presencial" es válido si el evento efectivamente tiene 3 cupos disponibles. Se prohíbe la escasez inventada.  
* **Botón prominente para acción principal esperada:** destacar visualmente el botón de acción esperada es válido y forma parte de la jerarquía visual sana. Se prohíbe disfrazar visualmente una acción destructiva como acción positiva.  
* **Testimonios reales de clientes reales, con permiso documentado:** "María González, contadora en Cartago, dijo: '...'" es válido si el testimonio es real y María autorizó por escrito su publicación. Se prohíben los testimonios inventados o publicados sin consentimiento.

Cuando un cliente solicita "algo agresivo" o "más conversiones", el equipo Keyons **DEBE** identificar cuál de estas alternativas legítimas satisface el objetivo comercial real del cliente. En la mayoría de casos, el objetivo declarado por el cliente (más ventas, menos churn, más leads) es alcanzable con estrategias legítimas, y el cliente acepta la alternativa cuando comprende que consigue el mismo resultado sin exponer a su marca a riesgos éticos, reputacionales o regulatorios.

#### ***Protocolo ante solicitud de cliente que roza patrón oscuro***

Cuando el cliente solicita explícitamente la implementación de un mecanismo que Keyons identifica como patrón oscuro conforme a la taxonomía de esta norma, el equipo aplica el siguiente protocolo secuencial de tres pasos antes de tomar decisión definitiva.

* **Paso 1 — Reformular el objetivo comercial real del cliente:** El equipo Keyons documenta cuál es el resultado comercial que el cliente busca (más conversiones, menos churn, más urgencia en la decisión, mayor retención). El método específico solicitado por el cliente se separa del objetivo comercial subyacente, porque frecuentemente el cliente solicita el método porque lo conoce de otras plataformas, no porque el método sea el único camino a su objetivo.  
* **Paso 2 — Ofrecer al cliente al menos una alternativa profesional equivalente:** El equipo Keyons presenta al cliente la o las opciones de estrategia comercial legítima definidas arriba que satisfacen su objetivo comercial real. La presentación es concreta, comparativa, con estimación de impacto esperado, y transparente sobre las razones por las cuales Keyons prefiere la alternativa (protección de marca del cliente, cumplimiento regulatorio emergente, sostenibilidad de la relación con usuarios finales, coherencia con doctrina Keyons).  
* **Paso 3 — Documentar formalmente si el cliente insiste después de la alternativa:** Si el cliente insiste en implementar el patrón oscuro después de escuchar la alternativa, el equipo comercial documenta por escrito en el expediente del proyecto la solicitud específica, la alternativa ofrecida, y la insistencia del cliente. Este registro es requisito indispensable para activar el mecanismo de declinación descrito en la siguiente subsección.

#### ***Declinación de proyecto por patrón oscuro no negociable***

Cuando el cliente insiste formalmente en la implementación de un patrón oscuro después de recorrer el protocolo anterior, Keyons declina el alcance específico solicitado. La declinación se ejecuta con el siguiente procedimiento formal.

* La declinación se comunica al cliente por escrito, firmada por los dos Aprobadores Generales conforme a KYN-PRD-GOB-010, con explicación profesional de las razones (integridad de marca Keyons ante otros clientes actuales y futuros, protección legal del propio cliente ante regulaciones emergentes de patrones oscuros en Costa Rica, Europa y otros mercados donde Keyons opera o pueda operar, coherencia interna del equipo Keyons y sostenibilidad del talento profesional que Keyons construye a mediano plazo).  
* La declinación se limita al alcance específico solicitado. El resto del proyecto puede continuar si el cliente acepta reemplazar el patrón oscuro por una alternativa legítima, o el proyecto completo se declina si el patrón oscuro es central al alcance solicitado.  
* Ningún miembro del equipo Keyons puede implementar patrones oscuros por acuerdo verbal informal con el cliente, aunque el cliente presione, ofrezca sobreprecio, o amenace con cambiar de proveedor. La disciplina institucional protege al equipo individualmente y a la empresa colectivamente.  
* La declinación se registra en la bitácora de gobernanza conforme a KYN-PRD-GOB-024 como incidencia operativa, para que quede constancia formal de la disciplina aplicada. El registro no incluye datos comerciales sensibles del cliente que faciliten identificación externa; solo el hecho de la declinación y la categoría del patrón oscuro solicitado.

Esta postura tiene efecto comercial neto positivo comprobado en la industria: los clientes que valoran integridad profesional eligen a Keyons precisamente por esta disciplina, y los clientes que hubieran generado problemas éticos futuros se auto seleccionan fuera del portafolio en la fase de negociación, protegiendo a Keyons de costos posteriores de reputación, litigio o pérdida de talento interno.

## KYN-PRD-UIX-012 · Firma UX Keyons: elementos silenciosos obligatorios en todo producto

Los productos Keyons comparten una lista cerrada de elementos silenciosos de experiencia que, aunque el usuario final no los identifica conscientemente, marcan la diferencia acumulada de calidad y coherencia entre productos del portafolio. Son la firma UX Keyons y son obligatorios en todo producto sin excepción. NO son personalizables por el cliente conforme a KYN-PRD-UIX-045.

* Estructura tripartita fija de mensajes de error (qué pasó, por qué, qué hacer) conforme a KYN-PRD-UIX-024.  
* Ausencia absoluta de códigos técnicos crudos visibles al usuario final en cualquier contexto operativo.  
* Mensajes de espera en lenguaje humano descriptivo, siempre con nombre humano de la acción en curso.  
* Micro-transición consistente de confirmación de acción exitosa en todos los productos.  
* Presencia obligatoria de mecanismo de rollback visible en toda acción reversible.  
* Comportamiento del agente Estela idéntico entre verticales (detalle en capítulo EST).  
* Comunicación tripartita de confianza del modelo IA con etiqueta más color más icono, sin variaciones estéticas entre productos.  
* Ausencia absoluta de patrones oscuros conforme a la taxonomía prohibida en KYN-PRD-UIX-006.
