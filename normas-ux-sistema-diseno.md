# Normas UX Keyons · para el Sistema de Diseño

**Versión:** traslado 0.1 · 2026-11-09
**Origen:** Manual de Producto v1, capítulo UIX (normas KYN-PRD-UIX-001 a 052)
**Destino:** libro Sistema de Diseño de la Biblioteca Keyons
**Aprobación del traslado:** Keylin Mendoza López y Oscar Mendoza López (Aprobadores Generales)

Este documento contiene **solo** las normas de experiencia de usuario. El resto del Manual de Producto (técnico, funcionalidad, metodología comercial) no se traslada. Cuando una norma cita otra del Manual de Producto (PRI, FIC, GOB, SAAS, MED, EST…), la cita se mantiene por su ID.

---

## A · Cambios ya aplicados en este documento

Aprobados por Keylin el 2026-11-09. Todo lo demás está igual que en el Manual de Producto.

| N.º | Norma | Cambio |
| --- | --- | --- |
| 1 | UIX-047, 050, 051, 052 | Nombres de fase corregidos a los oficiales: «Aurora» → Mediodía (3 veces), «Cenit» → Atardecer (1), «Constelación» → Anochecer (2), «Fase Noche» → Fase Anochecer (2) |
| 2 | UIX-002 | Se agrega: «Los nombres de las fases son fijos y no se cambian». |
| 3 | UIX-001 | Capa 1: se reemplaza el lenguaje biológico («estructuras biológicas», «gasto metabólico», «sobre-estimulación dopaminérgica») por principios comprobados: atención preatentiva, carga cognitiva, Ley de Hick, Ley de Fitts, efecto Zeigarnik |
| 4 | UIX-003 | «Mirada Instintiva (primeros 400 milisegundos)» pasa a «Mirada Instintiva (primera impresión)», con la cifra correcta: unos 50 milisegundos (Lindgaard y otros, 2006). La primera pregunta del checklist se reescribe sin «cerebro operativo» |
| 5 | UIX-021 | Se nombra la fuente de los 400 milisegundos: umbral de Doherty |
| 6 | UIX-038, 049, 052 | WCAG 2.1 → **WCAG 2.2 AA**. UIX-038 suma tres requisitos: área mínima de 24 × 24 px, foco nunca tapado y autenticación sin pruebas cognitivas |
| 7 | UIX-052 | Estela: todos los productos la llevan. En SaaS siempre presente, con su nombre y su estética, sin opción de desactivarla. En MED el agente se personaliza |
| 8 | UIX-052 | Marca en SaaS: base Keyons con personalización ligera por autoservicio (logo, color de marca, tipografía en zonas permitidas, portada y documentos que emite), sin afectar la legibilidad |

## B · Propuestas pendientes (NO aplicadas)

Keylin decide cada una. Hasta entonces, vale el texto original.

| N.º | Norma | Propuesta |
| --- | --- | --- |
| P1 | UIX-010 | La frontera ahora es entre el **libro de marca** (cómo se ve) y el **Sistema de Diseño** (cómo se comporta y cómo se construye). Hay que reescribir los títulos «Materia del Manual de Marca» y «Materia de este capítulo UIX» |
| P2 | UIX-044 | El recorrido de 2 a 5 minutos pasa a un recorrido corto de 3 a 5 pasos, más una lista de primeros pasos y estados vacíos que enseñan. Se mantienen los mini-recorridos por módulo |
| P3 | UIX-030 y UIX-046 | Fusionarlas en una sola norma de urgencia de notificaciones: hoy dicen lo mismo |
| P4 | Todas | Los ID KYN-PRD-UIX pertenecen al Manual de Producto. Decidir con Oscar el código del Sistema de Diseño. Los ID viejos quedan como «trasladada a…» y nunca se reutilizan |
| P5 | Nueva | **Siete estados obligatorios** en todo elemento interactivo: reposo, cursor encima, foco de teclado, presionado, seleccionado, deshabilitado y cargando. El foco de teclado siempre visible |

## C · Dónde va cada norma en el Sistema de Diseño

| Módulo › capítulo del Sistema de Diseño | Normas |
| --- | --- |
| Experiencia › Principios comunes | UIX-001, 005, 006, 012, 013 |
| Experiencia › Personas y contextos | UIX-007, 008, 009 |
| Experiencia › Elecciones verificadas | UIX-003, 048 |
| Arquitectura › Información | UIX-028 |
| Fundamentos › Espacio y retícula | UIX-029 |
| Componentes › Retroalimentación | UIX-030, 046 |
| Patrones › Flujos de trabajo | UIX-027, 031, 044 |
| Patrones › Recuperación | UIX-021, 022, 023, 024, 025, 026 |
| Patrones › Procesos críticos | UIX-014, 015 |
| Accesibilidad › Percepción y Operación | UIX-038 |
| Accesibilidad › Adaptación | UIX-039 |
| Contenido › Contenido | UIX-040 |
| Contenido › Escritura | UIX-041 |
| Datos › Dashboards | UIX-037 |
| IA y Estela › Principios de IA | UIX-016, 017, 018, 019, 020 |
| IA y Estela › Conversación | UIX-034, 035, 042, 043 |
| IA y Estela › Confianza segura | UIX-032, 033, 036 |
| Productos › Product Default y White-label | UIX-045, 052 |
| Gobierno › Gobierno normativo | UIX-010, 011, 051 |
| Gobierno › Validación | UIX-047, 049, 050 |
| Gobierno › Implementación | UIX-002, 004 (Método Prisma) |

---

## D · Normas

# **Capítulo UIX — Experiencia de Usuario e Interacción Humano-IA**

# *Capítulo que norma la lógica de interacción humano-IA en todos los productos, herramientas internas y agentes conversacionales de Keyons. Cubre comportamiento del sistema durante la espera, manejo de errores, comunicación de confianza del modelo, protocolos Human-in-the-Loop, explicabilidad, consentimiento, memoria conversacional, accesibilidad y firma UX de Keyons. La estética visual (colores, tipografías, iconografía) vive en el Manual de Marca (KYN-MRK) y NO se transcribe aquí.* 

## Sección A — Método Prisma Keyons

*El Método Prisma Keyons es el marco propio de investigación y diseño de experiencia sobre el cual se construyen todos los productos digitales de la empresa. Adopta la lógica del doble diamante y la extiende con una quinta fase de evolución continua post-lanzamiento. Se apoya en una doctrina biocognitiva dual aplicada transversalmente a cada fase. Ningún producto se aprueba comercialmente sin haber transitado formalmente por estas fases.*

### **KYN-PRD-UIX-001  |  Marco de Arquitectura Biocognitiva Dual: Ergonomía Instintiva y Procesamiento Analítico**

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

### **KYN-PRD-UIX-002  |  Método Prisma Keyons: fases obligatorias del proceso de diseño**

El Método Prisma Keyons estructura el trabajo de investigación y diseño en cinco fases obligatorias secuenciales. Ningún producto puede pasar de una fase a la siguiente sin cerrar formalmente los entregables mínimos de la fase anterior. La fase final (Galaxia) es permanente durante toda la vida del producto. Los nombres de las fases son fijos y no se cambian.

#### ***Fase 1 — Amanecer: Arranque formal del proyecto***

Tipificación formal del proyecto según su naturaleza (SaaS de nicho, MED en escenario A/B/C, capacitación, evento). Definición del alcance inicial, sponsor contratante, operador real que usará el producto, plazos, presupuesto y modalidad de investigación acordada. Se emite el expediente inicial del proyecto y las hipótesis preliminares del problema a resolver. 

* **Entregable mínimo:** Acta de tipificación firmada por el rol comercial responsable y aprobación del Product & AI Lead.

#### ***Fase 2 — Mediodía: Investigación profunda del contexto operativo real***

Investigación rigurosa del sector, del usuario final y de la operación diaria del cliente. La profundidad de investigación NO se degrada por presupuesto del cliente: se ajusta la metodología, no la seriedad. Cuando el cliente contrata investigación in situ (servicio premium, cotizado aparte), Keyons observa la operación real en el lugar. Cuando el cliente NO contrata in situ, Keyons compensa con entrevistas remotas profundas al operador real, análisis de flujos existentes, benchmarking del sector y observación de herramientas que el cliente ya utiliza. 

* **Entregable mínimo:** Reporte de hallazgos operativos firmado por el investigador responsable y validado por el Product & AI Lead.

#### ***Fase 3 — Atardecer: Definición precisa del problema a resolver***

Convergencia sobre la pregunta correcta. La mayoría de productos SaaS fallan por resolver con excelencia técnica una pregunta equivocada. En esta fase el equipo Keyons declara formalmente qué problema se resuelve, qué problema explícitamente NO se resuelve en esta iteración, y qué criterios objetivos definirán éxito. 

* **Entregable mínimo:** Brief de definición del problema con criterios de aceptación medibles, firmado por Aprobadores Generales y comunicado formalmente al cliente antes de iniciar Fase 4.

#### ***Fase 4 — Anochecer: Ideación, prototipado y validación***

Divergencia amplia de rutas de solución seguida de convergencia sobre la más viable, prototipado y validación con usuarios reales. Aplican tres reglas del método: (a) toda propuesta que incorpore IA **DEBE** compararse formalmente contra alternativa determinista; se elige IA solo cuando aporta valor diferencial claro conforme a KYN-PRD-PRI-011; (b) la validación se realiza con el operador real que usará el producto, no con el sponsor contratante; (c) los prototipos se prueban en flujos operativos reales.

* **Entregable mínimo:** Prototipo validado con al menos 5 usuarios reales del sector destino, con reporte de hallazgos y ajustes aplicados.

#### ***Fase 5 — Galaxia: Producto vivo en evolución permanente*** 

Ningún producto Keyons se considera cerrado. Toda solución activa entra en ciclo de evolución permanente donde se adapta al cambio del sector, al comportamiento observado de usuarios reales, a la evolución de modelos de IA base y al aprendizaje sistemático acumulado en otros proyectos. Un producto que deja de evolucionar entra en revisión de sunset conforme a KYN-PRD-FIC-004. 

**Entregable permanente:** Bitácora de evolución del producto con hallazgos post-lanzamiento, decisiones de mejora ejecutadas, métricas UX monitoreadas y aprendizajes contribuidos al sistema de diseño Keyons.

### **KYN-PRD-UIX-003  |  Doble Mirada Psicológica aplicada como criterio auditable en cada fase**

Durante las cinco fases del Método Prisma, toda decisión de diseño relevante **DEBE** evaluarse formalmente desde dos ángulos simultáneos que constituyen la Doble Mirada Psicológica del método. Esta evaluación NO es reflexión abstracta: se materializa en un checklist operativo de diez preguntas que el diseñador responde por escrito antes de cerrar la decisión.

#### ***Mirada Instintiva (primera impresión)***

Evalúa la primera impresión. La valoración visual de una interfaz se forma en unos 50 milisegundos (Lindgaard y otros, 2006): en ese instante la persona decide si el sistema "me sirve" o "me molesta".

* ¿La interfaz respeta la atención limitada de una persona que trabaja bajo presión?  
* ¿Evita esfuerzo cognitivo innecesario en tareas que la IA puede prellenar?  
* ¿El contraste visual dirige automáticamente la mirada hacia la excepción o la decisión pendiente?  
* ¿La retroalimentación al completar una acción es inmediata y transmite sensación de logro?  
* ¿La interfaz evita todo estímulo diseñado para adormecer el juicio crítico?

#### ***Mirada Cognitiva (siguientes minutos de operación)***

Evalúa cómo el usuario procesará conscientemente la interfaz durante el uso sostenido:

* ¿La carga cognitiva se mantiene dentro del umbral operativo del usuario esperado?  
* ¿La jerarquía visual guía correctamente hacia la próxima acción esperada?  
* ¿La revelación progresiva evita saturación en la vista principal?  
* ¿Los patrones respetan modelos mentales consolidados donde aplican?  
* ¿El sistema estimula pensamiento crítico o lo delega sin transparencia?

Toda decisión de diseño cuyo checklist arroje respuestas negativas o ambiguas se rediseña antes de continuar. El checklist firmado forma parte del expediente del proyecto y se conserva conforme a KYN-PRD-GOB-022.

### **KYN-PRD-UIX-004  |  Diferenciadores estructurales del Método Prisma frente al doble diamante estándar**

El Método Prisma Keyons se diferencia del doble diamante genérico del British Design Council por cinco decisiones estructurales que definen la identidad operativa del método. Estos diferenciadores son parte constitutiva del método y no son opcionales.

* **Investigación operativa en sitio como servicio opcional:** Keyons reconoce que la observación de campo genera diseños significativamente más sólidos, pero también tiene costo real. Se ofrece como servicio premium cotizable en la propuesta comercial. Cuando el cliente NO contrata investigación en sitio, Keyons aplica el método sobre información secundaria rigurosa con declaración explícita de que ciertos riesgos operativos podrían no detectarse hasta post-lanzamiento. La seriedad de la investigación nunca se degrada; se ajusta la metodología.  
* **IA como opción, no como default:** En la Fase Anochecer, toda propuesta que incorpore IA **DEBE** compararse formalmente contra al menos una alternativa de solución determinista. La elección de IA se justifica por aporte de valor diferencial claro, no por sesgo de "resolver todo con IA".  
* **Validación con múltiples contextos operativos de la organización cliente:** Cada superficie del producto se valida con usuarios reales del contexto que corresponde: dashboards ejecutivos con quienes los usan estratégicamente, flujos transaccionales con quienes los operan diariamente, reportes con quienes los consumen para decisiones. La validación centrada en un solo contexto genera productos incompletos. 

* **Producto vivo en evolución permanente (Fase Galaxia):** Ningún producto Keyons se declara terminado. La Fase Galaxia mantiene todo producto activo en ciclo de evolución continua alimentado por métricas UX monitoreadas y por aprendizaje acumulado entre proyectos.  
* **Aprendizaje sistemático entre proyectos alimenta el sistema de diseño:** Cada proyecto Keyons documenta hallazgos, patrones que funcionaron, patrones que fallaron y ajustes aplicados en la Fase Galaxia. Estos aprendizajes se sistematizan en el sistema de diseño Keyons, evitando que cada proyecto reinvente la rueda.

### **KYN-PRD-UIX-005  |  Doctrina Operativa: postura Keyons ante decisiones de diseño en conflicto**

Cuando dos principios de diseño válidos entren en conflicto durante un proyecto, Keyons adopta las siguientes posturas doctrinarias como criterio de decisión operativa. Estas posturas se citan formalmente cuando un diseñador debe justificar por qué eligió una alternativa sobre otra.

* **Cuando fluidez y transparencia compitan, gana transparencia:** La fluidez sin transparencia es manipulación. Prohibido ocultar un paso operativo con la excusa de "hacer más rápido" el flujo.  
* **Cuando automatización y control del usuario compitan, gana control:** El usuario preserva capacidad de intervenir, revertir y decidir. La automatización sirve al usuario, no al revés.  
* **Cuando eficiencia y comprensión compitan, gana comprensión:** Un flujo rápido que el usuario no entiende genera pánico operativo, no valor.  
* **Cuando estética y ergonomía compitan, gana ergonomía:** Una interfaz bella pero cansada de operar es una interfaz fallida. La belleza sirve a la función, no la sustituye.  
* **Cuando innovación y convención compitan, gana convención salvo aporte comprobado:** Respetar el modelo mental del usuario reduce curva de aprendizaje. Innovar donde aporta valor operativo real; imitar convención donde el usuario espera lo estándar.

### **KYN-PRD-UIX-006  |  Prohibición taxonómica de patrones oscuros (Dark Patterns)**

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

## Sección B — Doctrina y modelo de usuario

*Normas que definen para quién diseña Keyons. Todo trabajo de UX arranca por comprender arquetipos operativos reales del usuario destino. Sin modelo de usuario declarado, todo el resto del capítulo queda flotando sobre suposiciones.*

### **KYN-PRD-UIX-007  |  Arquetipos operativos obligatorios por vertical**

Todo vertical SaaS y todo proyecto MED de Keyons **DEBE** declarar formalmente los arquetipos operativos de sus usuarios reales antes de arrancar la Fase Atardecer. Un arquetipo operativo describe al usuario que realmente opera el producto ocho horas diarias, no al comprador corporativo que firma el contrato.

#### ***Contenido mínimo obligatorio de cada arquetipo***

* Rol operativo específico (por ejemplo: "recepcionista de mostrador de gimnasio con turno de 6 horas", no "personal administrativo").  
* Capacidad tecnológica esperada (bajo / medio / alto) con criterios objetivos.  
* Presión operativa diaria típica (volumen de transacciones, interrupciones, simultaneidad de tareas).  
* Tolerancia al error esperada (baja en verticales regulados, media en operación comercial, alta en exploración interna).  
* Entorno físico predominante de operación (mostrador con público presente, oficina cerrada, campo, móvil).  
* Herramientas actuales que utiliza y a las cuales estará acostumbrado.  
* Motivación primaria de uso (obligación laboral, mejora de productividad propia, atención al cliente).

Los arquetipos se validan con investigación real de la Fase Mediodía, no con suposiciones del equipo Keyons. Un arquetipo declarado sin evidencia de investigación se considera hipótesis, no arquetipo, y se marca como tal en el expediente del proyecto.

### **KYN-PRD-UIX-008  | Diseño diferenciado por contexto de uso del usuario dentro de la organización cliente** 

En productos vendidos a organizaciones, los usuarios interactúan con el sistema desde contextos operativos distintos según su rol y su momento de uso. Un mismo producto sirve a decisiones estratégicas (dashboards ejecutivos, informes de rendimiento, vistas agregadas), a operación transaccional diaria (mostrador, atención al cliente, procesamiento) y a análisis histórico. El diseño Keyons reconoce estos contextos y crea superficies específicas que funcionan óptimamente en cada uno, sin priorizar arbitrariamente un contexto sobre otro. Todos los usuarios de la organización cliente son usuarios de primera clase.

### **KYN-PRD-UIX-009  |  Consideración explícita de perfiles atencionales atípicos**

El diseño de todo producto Keyons **DEBE** contemplar explícitamente que una proporción significativa de la población operativa presenta perfiles atencionales atípicos (déficit de atención, hiperactividad, dislexia, ansiedad operativa). Estos usuarios no son casos extremos: son parte del arquetipo esperado en cualquier vertical.

#### ***Criterios operativos derivados***

* Interfaces con complejidad visual mínima operativa. Rechazo de saturación decorativa.  
* Jerarquía tipográfica clara y contrastada que permita escaneo visual rápido.  
* Agrupación semántica coherente que reduzca esfuerzo de organización mental por parte del usuario.  
* Posibilidad de retomar tareas interrumpidas sin pérdida de contexto ni obligación de reingreso de datos.  
* Ausencia de estímulos que compitan por la atención cuando el usuario está concentrado en una tarea crítica.  
* Esta norma no exige diagnósticos formales del usuario ni activación de "modo especial": exige que el diseño default de Keyons sea operativo para el rango real de perfiles atencionales presentes en la población trabajadora.

## Sección C — Sistema de diseño y firma UX Keyons

*Normas que definen la infraestructura de diseño compartida entre productos Keyons y los elementos silenciosos que unifican la experiencia entre soluciones distintas del portafolio.*

### **KYN-PRD-UIX-010  |  Frontera formal entre Manual de Marca y Manual de Producto UIX**

Para evitar duplicación conforme a KYN-PRD-GOB-004, esta norma declara qué materia de diseño de interfaces vive en el Manual de Marca (KYN-MRK) y qué materia vive en este capítulo UIX. La frontera se define por capa, no por producto.

#### ***Materia del Manual de Marca (KYN-MRK)***

Estética visual y expresión gráfica de la marca: paleta cromática, tipografías, iconografía visual, ilustraciones, fotografía, logos, marcas de agua, splash screens, tono de voz de la marca en comunicación pública, componentes visuales con carga estética.

#### ***Materia de este capítulo UIX***

Comportamiento funcional y ergonomía cognitiva: qué hace la interfaz ante estados del sistema, cómo se manifiesta la IA, cómo se maneja la latencia, cómo se comunica el error, cómo se estructura la información, cómo se conduce la interacción humano-máquina, cómo se gestiona la memoria conversacional, cómo se aplica accesibilidad, cómo se escribe el microcopy. UIX define QUÉ hace la interfaz y CÓMO se comporta; Marca define CÓMO se ve estéticamente.

### **KYN-PRD-UIX-011  |  Sistema de diseño Keyons: tokens funcionales, componentes canónicos y patrones de flujo**

Keyons opera un sistema de diseño único compartido entre todos sus productos, estructurado en tres capas jerárquicas.

#### ***Capa 1 — Tokens funcionales***

Definiciones atómicas de comportamiento que se aplican transversalmente a todos los productos: espaciados semánticos, umbrales de latencia y sus respuestas visuales asociadas, escala de urgencia de notificaciones, escala de confianza del modelo IA (verificado, revisar, requiere validación humana), duraciones estándar de animaciones y transiciones. Los tokens funcionales viven en este capítulo UIX; los tokens visuales (colores, tipografías, iconos) viven en el Manual de Marca.

#### ***Capa 2 — Componentes canónicos***

Biblioteca de componentes de interfaz reutilizables entre productos: banner de acción reversible, panel de aprobación con contexto, tarjeta de excepción operativa, modal de confirmación reforzada, estado vacío con guía de siguiente paso, panel de explicación de decisión de IA. Cada componente canónico tiene comportamiento definido en UIX y expresión visual definida en Manual de Marca.

#### ***Capa 3 — Patrones de flujo***

Secuencias probadas de interacción para tareas comunes entre verticales: alta de cliente en un tenant, procesamiento de pago con verificación, revisión y aprobación de propuesta generada por IA, exportación de historial operativo, offboarding de cuenta. Los patrones de flujo capitalizan el aprendizaje sistemático acumulado en la Fase Galaxia.

Modificaciones al sistema de diseño constituyen Cambio de Fondo conforme a KYN-PRD-GOB-020 y requieren aprobación de ambos Aprobadores Generales.

### **KYN-PRD-UIX-012  |  Firma UX Keyons: elementos silenciosos obligatorios en todo producto**

Los productos Keyons comparten una lista cerrada de elementos silenciosos de experiencia que, aunque el usuario final no los identifica conscientemente, marcan la diferencia acumulada de calidad y coherencia entre productos del portafolio. Son la firma UX Keyons y son obligatorios en todo producto sin excepción. NO son personalizables por el cliente conforme a KYN-PRD-UIX-045.

* Estructura tripartita fija de mensajes de error (qué pasó, por qué, qué hacer) conforme a KYN-PRD-UIX-024.  
* Ausencia absoluta de códigos técnicos crudos visibles al usuario final en cualquier contexto operativo.  
* Mensajes de espera en lenguaje humano descriptivo, siempre con nombre humano de la acción en curso.  
* Micro-transición consistente de confirmación de acción exitosa en todos los productos.  
* Presencia obligatoria de mecanismo de rollback visible en toda acción reversible.  
* Comportamiento del agente Estela idéntico entre verticales (detalle en capítulo EST).  
* Comunicación tripartita de confianza del modelo IA con etiqueta más color más icono, sin variaciones estéticas entre productos.  
* Ausencia absoluta de patrones oscuros conforme a la taxonomía prohibida en KYN-PRD-UIX-006.

### **KYN-PRD-UIX-013  |  Coherencia obligatoria entre productos del portafolio**

Un cliente que adopta un segundo producto Keyons **DEBE** percibir coherencia experiencial acumulada con el primero, sin necesidad de aprender nuevos patrones. Esta coherencia es activo comercial silencioso: crea lock-in emocional y refuerza percepción de marca operativa fuerte.

#### ***Criterios operativos de coherencia entre productos***

* Los tokens funcionales del sistema de diseño se aplican idénticamente en todos los productos activos.  
* Los componentes canónicos se comportan igual en todos los productos.  
* Los patrones de flujo comunes siguen la misma secuencia en todos los productos.  
* El agente Estela mantiene identidad y comportamiento consistentes en todos los verticales.

## Sección D — Arquitectura de la interacción humano-IA

*Corazón operativo del capítulo. Normas que definen cómo se manifiesta la inteligencia artificial en las interfaces de Keyons, cómo se conduce el diálogo entre usuario y sistema automatizado, y cómo se protege el juicio crítico del operador ante decisiones probabilísticas del modelo.*

### **KYN-PRD-UIX-014  |  Matriz de decisión Human-in-the-Loop por riesgo e irreversibilidad**

Toda acción ejecutable por un agente automatizado o por decisión asistida por IA **DEBE** clasificarse en uno de cuatro niveles de Human-in-the-Loop según la combinación de riesgo operativo y grado de irreversibilidad de la acción. La clasificación se declara por vertical en la Ficha Estándar de Producto conforme a KYN-PRD-FIC-002.

| Nivel | Descripción operativa | Ejemplos aplicados |
| :---- | :---- | :---- |
| Nivel 1 - Autonomía asistida | Riesgo bajo y acción completamente reversible. El sistema ejecuta; el usuario ve el resultado y puede editar libremente después sin fricción. | Sugerir texto en un campo, marcar lead como "en revisión", ordenar lista por fecha, sugerir prioridad tentativa. |
| Nivel 2 - Revisión posterior con rollback fácil | Riesgo bajo-medio, reversible en ventana corta. El sistema ejecuta y muestra la acción realizada en banner con botón de reversión visible durante 30 segundos. | Clasificar ticket automáticamente, autoetiquetar mensaje, sugerir asignación de responsable, categorizar transacción. |
| Nivel 3 - Aprobación previa obligatoria | Riesgo medio, reversible con esfuerzo. El sistema prepara la acción y muestra opciones "Aprobar / Editar / Descartar". El usuario DEBE confirmar antes de ejecutar. | Enviar correo automatizado al cliente, cambiar estado comercial de cliente, generar propuesta económica, notificar a tercero. |
| Nivel 4 - Aprobación reforzada con confirmación explícita | Riesgo alto o irreversible. Requiere confirmación explícita adicional del usuario. Registro obligatorio en log inmutable. Materializa la Zona Amarilla de KYN-PRD-PRI-013. | Aprobar crédito, procesar pago, eliminar datos de cliente, firmar contrato electrónicamente, ejecutar acción con efecto contable o legal. |

Las Zonas Rojas de KYN-PRD-PRI-013 NO se ejecutan nunca, ni siquiera con HITL Nivel 4. La elección de nivel para cada acción específica de un vertical se justifica formalmente en el expediente del proyecto según el arquetipo operativo del usuario destino declarado en KYN-PRD-UIX-007.

### **KYN-PRD-UIX-015  |  Personalización del HITL por vertical y por cliente: límites operativos**

El nivel de HITL aplicado a acciones específicas puede ajustarse por vertical y por cliente dentro del marco general de KYN-PRD-UIX-014, siempre respetando los siguientes límites operativos no negociables.

* **Personalización admisible por el cliente:** Un cliente puede solicitar que ciertas acciones actualmente en Nivel 3 se ejecuten como Nivel 2 para agilizar operación de alto volumen. La solicitud se acepta si el análisis de riesgo del proyecto respalda que la acción efectivamente admite menor supervisión en el contexto operativo específico del cliente.  
* **Personalización NO admisible por el cliente:** Un cliente **NO PUEDE** solicitar que una acción de Nivel 4 se ejecute como Nivel 1 o sin HITL, aunque insista, porque compromete integridad operativa, legal o comercial. La solicitud se declina formalmente con justificación escrita.  
* **Elevación obligatoria de nivel por parte de Keyons:** Keyons puede elevar unilateralmente el nivel HITL de una acción específica si detecta incidentes operativos, quejas de usuarios finales o cambios regulatorios que lo justifiquen. El cliente es notificado con anticipación.

Los casos límite donde la personalización solicitada por el cliente entre en zona gris se resuelven por Aprobadores por Dominio; el criterio final ante disenso es de los Aprobadores Generales conforme a KYN-PRD-GOB-012.

### **KYN-PRD-UIX-016  |  Comunicación tripartita de confianza del modelo**

La confianza del modelo IA sobre una respuesta o decisión se comunica al usuario mediante tres niveles categóricos con etiqueta orientada a la acción, color contextual e icono reconocible. Los puntajes numéricos crudos (por ejemplo "Confianza: 58%") NO se muestran por default al usuario final ni al operador, porque generan confusión analítica y parálisis de decisión. Pueden mostrarse bajo demanda en paneles de auditoría avanzada, pero nunca en la interfaz principal operativa.

| Nivel | Etiqueta | Comportamiento del sistema |
| :---- | :---- | :---- |
| Verificado (verde) | Verificado | Confianza alta. El sistema ejecuta la acción sugerida en segundo plano sin interrumpir al usuario. Confirmación visible como aviso no invasivo tras completarse. |
| Revisar (amarillo) | Revisar antes de aprobar | Confianza media. La interfaz resalta visualmente la propuesta y espera aprobación explícita del usuario antes de ejecutar. Materializa la Zona Amarilla de KYN-PRD-PRI-013. |
| Validación humana (rojo) | Requiere validación humana | Confianza baja o acción bajo zona amarilla de PRI-013. El sistema NO actúa. Escala al humano con contexto completo, opciones disponibles y datos que llevaron al escalamiento. |

La reducción a tres niveles categóricos no es simplificación estética: es aplicación operativa de la Ley de Hick, que establece que el tiempo de decisión crece logarítmicamente con el número de opciones disponibles. Tres niveles ofrecen resolución operativa suficiente sin activar parálisis analítica.

### **KYN-PRD-UIX-017  |  Transparencia obligatoria del modo copiloto vs. autopiloto**

El usuario **DEBE** poder identificar en cualquier momento si el sistema opera en modo autopiloto (actuando autónomamente) o en modo copiloto (esperando aprobación humana). Un indicador visual permanente y discreto en la interfaz declara el modo activo. Los cambios de modo generan notificación explícita al usuario, sin excepciones por conveniencia de diseño.

Esta transparencia preserva el juicio crítico del usuario y protege contra delegación invisible. Un usuario que no sabe si el sistema está actuando por su cuenta o esperándolo pierde control sobre la operación y no puede intervenir a tiempo. La transparencia del modo es requisito no negociable en todo producto Keyons.

### **KYN-PRD-UIX-018  |  Gestión de expectativas del usuario ante IA probabilística**

Los usuarios tienden a formar modelos mentales del software basados en experiencias previas con herramientas deterministas (una calculadora entrega el mismo resultado ante la misma entrada). Los modelos de lenguaje son probabilísticos: pueden variar entre ejecuciones. Si el modelo mental del usuario no se calibra activamente, la primera vez que el sistema responda distinto a lo esperado se genera frustración y pérdida de confianza.

#### ***Reglas de calibración del modelo mental***

* **Léxico obligatorio del agente:** El agente Keyons "sugiere", "propone", "estima". Nunca "determina", "resuelve", "garantiza", ni afirma con certeza absoluta un resultado probabilístico. La calibración lingüística del agente se detalla en KYN-PRD-UIX-042.  
* **Aviso explícito de variabilidad cuando aplique:** En respuestas donde la variabilidad entre ejecuciones puede ser material para el usuario, el sistema comunica explícitamente esa posibilidad con microcopy contextual.  
* **Distinción entre respuesta y decisión:** La interfaz distingue visualmente entre información recuperada por el sistema y propuestas generadas por el modelo IA. Ambas se muestran con tratamiento visual diferenciado para calibrar la expectativa correcta.

### **KYN-PRD-UIX-019  |  Explicabilidad activada por materialidad del impacto**

La explicación de por qué el sistema tomó una decisión (Explainable AI) NO se muestra por default en toda decisión automatizada, porque sobrecarga innecesariamente al usuario. La explicabilidad se rige por tres niveles graduales según la materialidad del impacto de la decisión sobre el usuario o sobre terceros.

* **Nivel Nulo (sin explicación visible):** Aplica a decisiones automáticas de bajo impacto (sugerir texto, ordenar lista, autocompletar campo, resaltar coincidencia). No se muestra explicación ni botón para pedirla.  
* **Nivel Bajo Demanda (explicación disponible si el usuario pregunta):** Aplica a decisiones medias donde el usuario podría razonablemente querer entender el razonamiento. Botón discreto "¿Por qué?" que abre panel con explicación al pedirlo.  
* **Nivel Obligatorio (explicación siempre visible junto a la decisión):** Aplica a decisiones que afectan materialmente al usuario o a terceros (denegar solicitud, clasificar como riesgo, aprobar crédito, alterar estado comercial, priorizar caso crítico) y siempre a acciones bajo Zona Amarilla de KYN-PRD-PRI-013 con HITL Nivel 3 o 4. La explicación es parte visible del componente, no bajo demanda.

Cada vertical Keyons declara en su Ficha Estándar de Producto qué tipos de decisión aplican a cada nivel de explicabilidad.

### **KYN-PRD-UIX-020  |  Estructura obligatoria del panel de explicación de decisión de IA**

Cuando la interfaz muestra explicación de una decisión (Nivel Bajo Demanda o Nivel Obligatorio conforme a KYN-PRD-UIX-019), el panel de explicación **DEBE** contener tres secciones en orden fijo, aplicando revelación progresiva.

* **Sección 1 — Explicación en lenguaje humano:** Resumen accesible del razonamiento en una o dos líneas. Ejemplo: "Clasifiqué este cliente como alto riesgo porque presenta 3 facturas vencidas en los últimos 60 días y superó el límite de crédito acordado en el contrato."  
* **Sección 2 — Fuentes o datos consultados:** Listado breve de qué información utilizó el modelo para llegar a la decisión, con enlaces al documento origen cuando aplique. Permite al usuario verificar rápidamente la validez del insumo del modelo.  
* **Sección 3 — Reglas de negocio aplicadas (bajo demanda dentro del panel):** Detalle técnico de las reglas configuradas por el cliente o por Keyons que llevaron a la clasificación. Este nivel de detalle se muestra solo si el usuario lo solicita explícitamente dentro del panel.

## Sección E — Estados operativos del sistema

*Normas que definen cómo la interfaz responde en los cuatro estados que deciden la percepción de calidad operativa: espera, error, vacío y éxito. Los estados mal diseñados son la causa número uno de percepción de baja calidad en productos digitales modernos.*

### **KYN-PRD-UIX-021  |  Protocolo de espera y percepción de responsividad**

La percepción de responsividad de un sistema se decide en los primeros 400 milisegundos (umbral de Doherty). Superado ese umbral, el usuario transita de confianza tácita a duda activa; si nada visible confirma que el sistema procesa, la duda escala a asunción de fallo. Keyons rige su comportamiento en espera por este principio operativo: el sistema DEBE comunicar procesamiento antes de que la duda del usuario aparezca, no después.

#### ***Umbrales de comunicación obligatoria***

| Umbral | Respuesta obligatoria de la interfaz |
| :---- | :---- |
| 0 a 0.4 seg | Nada visible. Percibido como instantáneo. |
| 0.4 a 1 seg | Microanimación sutil de feedback (cambio de color, movimiento mínimo). Confirma que la acción se registró. |
| 1 a 3 seg | Loader claro y visible en el componente donde ocurre la acción, sin cubrir el resto de la interfaz. |
| 3 a 10 seg | Loader + mensaje humano descriptivo del estado ("Consultando 3 fuentes...", no "Loading..."). |
| Más de 10 seg | Loader + mensaje humano + estimación de tiempo restante + opción de cancelar o realizar otra tarea en paralelo. |

Superar 30 segundos sin resolución activa protocolo de fallo del modelo conforme a KYN-PRD-UIX-023. Sistemas que dejan al usuario en pantalla estática superior a 3 segundos sin retroalimentación pierden porcentaje material de tasa de finalización en flujos operativos, y Keyons no admite ese costo por default en ningún producto. Criterio de aceptación pre-lanzamiento: un evaluador externo debe poder identificar en cada punto de espera del flujo qué está haciendo el sistema y cuánto falta.

### **KYN-PRD-UIX-022  |  Lenguaje humano obligatorio en mensajes de espera**

Cuando el tiempo de espera supera 3 segundos y se activa mensaje descriptivo conforme a KYN-PRD-UIX-021, el mensaje **DEBE** describir qué está haciendo el sistema en lenguaje humano orientado a la acción, nunca con jerga técnica ni con loaders neutros vacíos.

#### **Ejemplos correctos**

* "Consultando 3 fuentes..."  
* "Verificando pago con SINPE Móvil..."  
* "Preparando tu resumen..."  
* "Analizando 12 documentos..."

#### **Ejemplos prohibidos**

* "Loading..." (jerga técnica en inglés)  
* "Procesando request..." (jerga técnica)  
* Solo icono giratorio sin texto acompañante

En operaciones que superan 10 segundos, el mensaje descriptivo DEBE evolucionar con detalle progresivo, no permanecer estático. La mente humana interpreta un mensaje estático prolongado como señal de que el sistema colgó.

### **KYN-PRD-UIX-023  |  Protocolo de fallo del sistema con ruta alternativa obligatoria**

Cuando un componente automatizado por IA o una integración externa falla, la interfaz **DEBE** ofrecer al menos una ruta alternativa manual visible en el mismo componente donde ocurrió el fallo. Esta regla es dura y no admite excepciones por complejidad técnica.

#### ***Ejemplos de aplicación obligatoria***

* Si la verificación automática de pago con SINPE falla, el usuario **DEBE** poder adjuntar comprobante manualmente en el mismo momento y en el mismo componente, sin abandonar la pantalla.  
* Si el agente de IA no puede clasificar un lead, el usuario **DEBE** poder clasificarlo manualmente con opciones predefinidas visibles en el mismo componente.  
* Si la extracción automática de datos de un documento falla, el usuario **DEBE** poder ingresar los datos manualmente en el mismo flujo, sin reiniciar la operación.

Cuando técnicamente sea imposible ofrecer ruta alternativa manual en el momento, el mensaje **DEBE** indicar tiempo estimado de restablecimiento del servicio ("vuelve a intentar en 5 minutos") y no dejar al usuario en callejón sin salida.

### **KYN-PRD-UIX-024  |  Estructura tripartita obligatoria de mensajes de error**

Todo mensaje de error visible al usuario final **DEBE** cumplir la siguiente estructura fija de tres partes. Los códigos técnicos crudos ("Error 502", "NullPointerException", stack traces) están estrictamente prohibidos en la capa visible al usuario.

* **Parte 1 — Qué pasó (lenguaje humano):** Frase corta que describe la situación sin jerga técnica. Ejemplo: "El asistente no pudo verificar el pago en tiempo real."  
* **Parte 2 — Por qué (una línea máximo):** Explicación breve de la causa comprensible por un usuario no técnico. Ejemplo: "Conexión con SINPE interrumpida.  
* **Parte 3 — Qué hacer ahora (acción concreta con botón visible):** Botón o enlace de acción inmediata que resuelve la situación. Ejemplo: "Adjuntar comprobante manualmente.

Esta estructura tripartita convierte el momento de error, que es el momento de mayor vulnerabilidad emocional del usuario, en un momento de recuperación guiada y sensación de control. Es uno de los elementos de la firma UX Keyons conforme a KYN-PRD-UIX-012.

### **KYN-PRD-UIX-025  |  Reversibilidad como red de seguridad emocional operativa**

Toda acción destructiva o significativa que el usuario pueda ejecutar por error **DEBE** ser reversible o requerir confirmación explícita antes de ejecutarse. La interfaz se diseña asumiendo que los usuarios cometerán errores; el objetivo no es evitar el error, sino permitir su corrección sin costo emocional ni operativo.

#### ***Ventana de reversibilidad según nivel HITL***

* **HITL Nivel 2 — Rollback de 30 segundos:** banner con botón "Deshacer" visible durante 30 segundos tras la ejecución.  
* **HITL Nivel 3 — Rollback durante sesión activa:** la acción es reversible hasta que el usuario cierre la sesión o la ventana operativa.  
* **HITL Nivel 4 — Rollback hasta cierre operativo del ciclo:** la acción queda registrada en log inmutable con opción explícita de reversión hasta que la acción cumpla su ciclo operativo.

La reversibilidad es aplicación operativa del principio de Aversión a la Pérdida: el impacto psicológico de una pérdida es aproximadamente el doble que el placer de una ganancia equivalente. Saber que existe red de seguridad reduce ansiedad operativa y permite al usuario delegar en agentes de IA con confianza.

### **KYN-PRD-UIX-026  |  Diseño obligatorio de estados vacíos como oportunidad de guía**

Los estados vacíos NO se muestran nunca como pantalla en blanco, mensaje genérico "Sin datos" o pantalla de error. Todo estado vacío **DEBE** diseñarse como oportunidad de guía al usuario, cumpliendo tres reglas obligatorias.

* **Explicar en lenguaje humano por qué está vacío:** "Aún no tienes clientes registrados" en vez de "No hay resultados".  
* **Ofrecer al menos una acción concreta para salir del estado vacío:** Botón "Agregar tu primer cliente" o similar. La acción es siempre concreta y ejecutable desde el mismo componente.  
* **Diferenciar entre estado vacío inicial y estado vacío por filtro:** Cuando el usuario filtró y no hay resultados, el mensaje es distinto y sugiere ajustar el filtro ("Ningún cliente coincide con estos filtros. Prueba ampliar el rango de fechas.").

### **KYN-PRD-UIX-027  |  Micro-momentos de satisfacción operativa por cierre de ciclo**

Toda acción completada exitosamente por el usuario en un producto Keyons **DEBE** ir acompañada de una micro-transición de confirmación que active la percepción de logro y cierre de ciclo. Estas micro-transiciones no son decoración: son aplicación operativa del Efecto Zeigarnik, que establece que el cerebro humano busca cerrar ciclos abiertos y recibe recompensa cognitiva por lograrlo.

#### ***Criterios operativos de la micro-transición estándar***

* Transición limpia y fluida, sin cortes bruscos.  
* Cambio de estado visual al color asignado por el sistema de diseño para "completado".  
* Duración corta y consistente entre productos del portafolio (parte de la firma UX Keyons).  
* Actualización simultánea de indicadores de progreso relevantes.

## Sección F — Gestión de atención, carga cognitiva y ritmo

*Normas que regulan la demanda cognitiva que Keyons impone sobre el usuario y el ritmo con que la interfaz solicita su atención. La atención humana es recurso finito; su mala gestión es la causa principal de abandono en productos SaaS complejos.*

### **KYN-PRD-UIX-028  |  Aplicación operativa de revelación progresiva y jerarquía de la decisión**

En cada pantalla operativa, el usuario **DEBE** tener frente a sí solo la información y las opciones necesarias para tomar la próxima decisión esperada. La información complementaria y las opciones avanzadas se relegan a capas secundarias de interacción accesibles bajo demanda.

#### ***Criterios operativos de revelación progresiva***

* Toda pantalla operativa exhibe una única decisión primaria clara. Las decisiones secundarias existen pero no compiten visualmente con la primaria.  
* Los detalles técnicos, paneles de auditoría y opciones de configuración avanzada viven en pestañas, desplegables o modales accesibles con un clic explícito.  
* La cantidad de opciones simultáneas visibles en un punto de decisión se limita a un rango operativo (típicamente 3 a 5 opciones máximo). Superar ese rango activa parálisis analítica conforme a la Ley de Hick.

Criterio de auditoría vinculado: un evaluador externo sin conocimiento del vertical **DEBE** poder identificar en cada pantalla cuál es la próxima acción esperada en menos de 5 segundos.

### **KYN-PRD-UIX-029  |  Densidad visual: modo cómodo y modo denso con default por vertical**

Los productos Keyons ofrecen dos modos de densidad visual seleccionables por el usuario en la barra de configuración de vista.

* **Modo cómodo:** Mayor aire visual, menos elementos por pantalla. Apropiado para tareas de menor volumen y para usuarios ocasionales que operan el producto esporádicamente.  
* **Modo denso:** Mayor cantidad de datos por pantalla, apropiado para operadores profesionales con alto volumen diario. Similar en filosofía a interfaces de trading o dashboards financieros ejecutivos.

#### ***Regla de default por vertical***

Cada vertical Keyons declara en su Ficha Estándar de Producto el modo default según perfil operativo esperado del arquetipo primario (KYN-PRD-UIX-007). Como referencia orientadora: verticales con operadores profesionales de alto volumen diario (contable, financiero, legal ejecutivo) suelen tener default modo denso; verticales con operadores ocasionales o de negocio pequeño (gimnasio, spa, restaurante) suelen tener default modo cómodo.

### **KYN-PRD-UIX-030  |  Jerarquía de urgencia de notificaciones y prohibición de fatiga por alertas**

Todo evento del sistema que requiera atención del usuario se clasifica en uno de cuatro niveles de urgencia según su impacto operativo real. Cada nivel tiene modalidad de notificación asignada. Prohibido escalar niveles arbitrariamente para "asegurar que el usuario vea" un evento; la escalada arbitraria genera fatiga por alertas y termina provocando que el usuario ignore incluso las alertas críticas legítimas.

| Nivel | Modalidad de notificación | Ejemplos |
| :---- | :---- | :---- |
| Rutinario | Solo cambio visual sutil o texto discreto. Sin interrupción del flujo. | Confirmación de guardado automático, actualización menor de datos, indicador de sincronización. |
| Importante | Texto más icono con contraste moderado. Puede requerir acción pero no bloquea flujo. | Alerta de límite de plan cerca de agotarse, recordatorio de tarea pendiente, invitación a completar perfil. |
| Crítico | Texto, icono, animación breve y opcionalmente sonido corto. Requiere atención inmediata pero no bloquea el sistema. | Pago fallido en operación crítica, límite de plan alcanzado, error en integración operativa activa. |
| Catastrófico | Modal bloqueante con todas las modalidades activas y opción única de acción. Bloquea toda otra interacción hasta resolverse. | Pérdida total de conectividad durante transacción irreversible, brecha de seguridad detectada, fallo crítico de infraestructura. |

#### ***Reglas de agrupación inteligente***

* Alertas del mismo tipo generadas en secuencia rápida se agrupan automáticamente en una única notificación consolidada.  
* El sonido se usa con moderación extrema, siempre configurable por el usuario (activar/desactivar).  
* Ningún vertical puede tener más de 5 notificaciones rutinarias visibles simultáneamente en la interfaz principal. Excedentes se consolidan en centro de notificaciones.

### **KYN-PRD-UIX-031  |  Ritmo de progresión en flujos multi-paso**

Los flujos operativos que requieren múltiples pasos **DEBEN** estructurarse aprovechando el Efecto Zeigarnik para acelerar adopción y reducir abandono.

#### ***Criterios operativos del ritmo de progresión***

* Indicador visual de progreso siempre presente durante el flujo (barra de estado "3 de 5 pasos", línea de tiempo, mapa de proceso).  
* Los pasos se dividen en unidades cortas que aporten sensación de avance frecuente. Un paso que toma más de 3 minutos se subdivide en sub-pasos con cierre visible.  
* El usuario puede abandonar el flujo temporalmente y retomarlo desde el último paso completado, sin pérdida de datos ni obligación de reingreso.  
* Al finalizar el flujo, se muestra una pantalla de cierre explícita que confirma completitud y sugiere próximo paso natural.

## Sección G — Consentimiento, control y transparencia

*Normas sobre qué control efectivo tiene el usuario sobre sus datos, sobre las acciones del sistema, sobre la memoria conversacional y sobre la exportación de su historial operativo.*

### **KYN-PRD-UIX-032  |  Visibilidad de fuentes RAG según sensibilidad regulatoria del vertical**

La visibilidad de fuentes que el modelo consultó mediante Retrieval-Augmented Generation se rige según la sensibilidad regulatoria del sector del vertical, no como default universal aplicado igual a todos los productos.

* **Verticales regulados (legal, salud, financiero, contable):** Fuentes visibles obligatorias en cada respuesta que provenga de RAG, con cita al documento origen. Requisito de compliance y de protección legal del cliente profesional.  
* **Verticales no regulados (gimnasio, spa, restaurante, retail general):** Fuentes bajo demanda mediante botón "Ver fuentes" o control equivalente. El usuario final típicamente no las requiere; el operador puede consultarlas si duda.  
* **Herramientas internas Keyons:** Fuentes visibles por default. El equipo Keyons trabaja con datos operativos críticos y requiere trazabilidad completa.

Cada vertical Keyons declara formalmente su nivel de visibilidad de fuentes en su Ficha Estándar de Producto conforme a KYN-PRD-FIC-002.

### **KYN-PRD-UIX-033  |  Acceso al prompt: restringido al administrador del tenant**

El prompt exacto que se envía al modelo NO se muestra al usuario final por default. Los prompts base son activo de propiedad intelectual de Keyons regulado formalmente en el capítulo AGT (en construcción). El administrador del tenant tiene acceso al prompt bajo demanda desde un panel de auditoría, para permitir auditoría interna de calidad y compliance del cliente sin exponer la propiedad intelectual de Keyons a usuarios finales.

### **KYN-PRD-UIX-034  |  Memoria conversacional en tres niveles con controles diferenciados**

Todo agente conversacional Keyons implementa exactamente tres niveles de memoria conversacional, cada uno con controles diferenciados para el usuario. Esta estructura protege al usuario contra acumulación silenciosa de datos personales y preserva transparencia sobre qué recuerda el sistema.

* **Nivel A — Memoria de sesión (default activada):** el asistente recuerda todo lo hablado dentro de la sesión activa. Al cerrar sesión o iniciar nueva conversación, la memoria de sesión se limpia automáticamente. Es el default más seguro y predecible.  
* **Nivel B — Memoria persistente por usuario (opt-in explícito):** el asistente recuerda preferencias del usuario entre sesiones ("prefiero respuestas en formato lista"). Requiere activación explícita por el usuario. La memoria es siempre visible al usuario y editable o eliminable en cualquier momento.  
* **Nivel C — Contexto de tenant (compartido dentro de la empresa cliente):** información configurada por el administrador del tenant como contexto siempre presente para el asistente ("somos clínica dermatológica, no ofrezcas servicios estéticos generales"). Vive en la configuración del tenant.

### **KYN-PRD-UIX-035  |  Controles de olvido y transparencia sobre memoria acumulada**

El usuario tiene acceso permanente y visible a dos capacidades sobre la memoria del agente, sin fricción operativa que las disuade.

* **Botón "Olvidar" siempre visible:** permite resetear la memoria de sesión, la memoria persistente, o ambas, con un botón claro. La eliminación es irreversible y se ejecuta inmediatamente sin pasos de confirmación burocráticos, salvo un único paso de doble confirmación en el caso de memoria persistente acumulada mayor a 30 días.  
* **Log de transparencia "¿Qué recuerdas de mí?":** el usuario puede solicitar al agente que devuelva la lista completa de datos recordados en cada nivel de memoria. El log se muestra en lenguaje humano, no como estructura de datos técnica.

### **KYN-PRD-UIX-036  |  Restricciones del cliente sobre procesamiento con LLMs externos**

Los clientes corporativos **PUEDEN** configurar restricciones a nivel de módulo dentro del vertical para impedir que datos altamente confidenciales pasen por modelos de lenguaje externos (Google Gemini, Anthropic Claude, OpenAI GPT). En módulos restringidos, el sistema usa exclusivamente procesamiento determinista o modelos ejecutados en infraestructura controlada por el cliente cuando aplique la modalidad de despliegue conforme a KYN-PRD-MED-023.

La restricción se declara en la configuración administrativa del tenant, con banner informativo visible al usuario final que indica: "Este módulo procesa datos localmente por política de tu empresa". Esta transparencia calibra el modelo mental del usuario sobre qué hace el sistema con datos sensibles.

### **KYN-PRD-UIX-037  |  Exportación nativa de historial operativo en formatos estructurados**

El usuario **DEBE** tener capacidad nativa de exportar los historiales de chat, logs de auditoría y registros operativos de su tenant en formatos estructurados estándar (CSV y JSON como mínimo, más el formato específico del vertical cuando aplique). La exportación NO requiere autorización especial de Keyons ni se cobra como servicio adicional; es capacidad nativa de todo producto conforme a KYN-PRD-SAAS-022. Plazo máximo de respuesta a solicitud de exportación: 15 días hábiles.

## Sección H — Accesibilidad e inclusión

### **KYN-PRD-UIX-038  |  Cumplimiento mínimo WCAG 2.2 nivel AA**

Todo producto Keyons **DEBE** cumplir con las Web Content Accessibility Guidelines versión 2.2 en nivel AA como mínimo, respetando los cuatro principios rectores del estándar: perceptible, operable, comprensible y robusto.

#### ***Requisitos técnicos operativos derivados***

* Contraste de color mínimo: relación 4.5:1 para texto normal y 3:1 para texto grande.  
* Tamaño de fuente mínimo operativo: equivalente a 16 píxeles para texto de cuerpo en interfaces web y proporcional en aplicaciones móviles.  
* Navegación completa por teclado: toda funcionalidad accesible sin uso de ratón, con indicador visual claro del elemento con foco activo.  
* Compatibilidad con lectores de pantalla: etiquetas ARIA correctas en todos los componentes interactivos y descripciones alt en imágenes con contenido significativo.  
* Indicadores no dependientes exclusivamente del color: los estados y alertas se comunican con color más icono o texto, para no excluir a usuarios daltónicos (aproximadamente 8% de hombres y 0.5% de mujeres a nivel mundial).  
* Área mínima de cada control: 24 × 24 píxeles (WCAG 2.5.8).  
* El elemento con foco nunca queda tapado por otros elementos, como cabeceras fijas o avisos (WCAG 2.4.11).  
* Autenticación sin pruebas cognitivas: el usuario no debe resolver acertijos ni recordar códigos para iniciar sesión; se permite copiar y pegar y usar gestores de contraseñas (WCAG 3.3.8).

Cada vertical Keyons declara en su Ficha Estándar de Producto el nivel WCAG cumplido y las excepciones justificadas cuando aplique. El cumplimiento se verifica en el checklist de auditoría UX pre-lanzamiento conforme a KYN-PRD-UIX-050.

### **KYN-PRD-UIX-039  |  Adaptación operativa a contextos móvil y escritorio**

Todo producto Keyons cuya operación esperada incluya uso móvil **DEBE** ofrecer experiencia diseñada específicamente para pantalla táctil y contexto de uso móvil, no una versión reducida de la interfaz de escritorio.

#### ***Criterios operativos de adaptación móvil***

* Áreas táctiles mínimo 44x44 píxeles conforme a estándares WCAG táctiles.  
* Priorización de acciones: en móvil se muestra la acción primaria destacada; las secundarias se relegan a menú desplegable.  
* Consideración explícita de operación con una sola mano en pantallas grandes: elementos críticos ubicados en zonas alcanzables sin cambiar el agarre.  
* Feedback sensorial adaptado: sonido puede reemplazarse por vibración en móvil.  
* Estados offline manejados con transparencia: si la conectividad falla, la interfaz lo comunica claramente y ofrece cola de operaciones que se sincronizan al recuperar conexión.

## Sección I — UX Writing y voz del sistema

*Normas sobre cómo se escribe todo el texto que aparece en las interfaces de Keyons. En productos con IA conversacional, el UX writing representa aproximadamente 60% de la percepción de calidad del producto. Sin disciplina de escritura, cada vertical suena distinto y la marca operativa se diluye.*

### **KYN-PRD-UIX-040  |  Voz del sistema Keyons: registro, tono y calibración**

El sistema Keyons habla con voz consistente en todos sus productos y superficies. La voz se caracteriza por tres atributos que aplican simultáneamente.

* **Profesional pero cercana:** Léxico profesional del sector aplicado con claridad accesible. Evita jerga técnica innecesaria; explica lo técnico cuando aparece.  
* **Precisa pero humana:** Directa al punto sin sonar mecánica. Prefiere frases cortas y acciones concretas sobre construcciones formales prolongadas.  
* **Calibrada según certeza:** El sistema comunica con el nivel de confianza que corresponde a lo que sabe. "Sugiero..." cuando propone, "Confirmo..." cuando verifica, "Encontré..." cuando recupera. Nunca afirma con certeza absoluta un resultado probabilístico.

**Esta voz aplica a todo texto de la interfaz:** microcopy de botones, mensajes de error, mensajes de espera, respuestas del agente, notificaciones, correos transaccionales. La consistencia entre superficies es lo que hace que un cliente sienta que está interactuando con Keyons y no con un producto genérico.

### **KYN-PRD-UIX-041  |  Reglas de microcopy: botones, etiquetas y llamadas a acción**

El microcopy es el texto pequeño que decide si el usuario entiende qué hacer. Se rige por las siguientes reglas obligatorias.

* Botones nombran la acción, no genérico. "Agregar cliente" en lugar de "Aceptar". "Enviar comprobante" en lugar de "Ok".  
* Etiquetas de campos usan lenguaje del usuario, no jerga técnica. "Nombre completo" en lugar de "full\_name", "Fecha de vencimiento" en lugar de "due\_date".  
* Llamadas a acción son verbos en imperativo o infinitivo directo. "Comenzar", "Guardar", "Cancelar suscripción", nunca gerundio ("Comenzando...").  
* Textos de ayuda contextual son breves (máximo 2 líneas) y explican qué hacer, no qué es el campo. "Ingresa el correo donde recibirás notificaciones" en lugar de "Este campo es el correo electrónico".  
* Confirmaciones son específicas al contexto, no genéricas. "Cliente María González creada correctamente" en lugar de "Éxito".

### **KYN-PRD-UIX-042  |  Reglas de calibración lingüística en respuestas del agente IA**

Las respuestas del agente conversacional (Estela y sus derivados en cada vertical) **DEBEN** reflejar en su lenguaje el nivel de certeza real del modelo, para calibrar activamente el modelo mental del usuario conforme a KYN-PRD-UIX-018.

#### ***Verbos y frases obligatorios según certeza***

* Alta certeza (dato verificable, cálculo determinista): "Confirmo", "Encontré", "Verifiqué". Ejemplo: "Confirmé el pago de María González por 45.000 colones el 10 de septiembre."  
* Certeza media (propuesta razonada): "Sugiero", "Propongo", "Podría ser". Ejemplo: "Sugiero clasificar este lead como prioridad alta según su historial de consultas."  
* Certeza baja (interpretación probabilística de datos ambiguos): "Podría interpretarse como...", "No tengo certeza pero...", "Considera que...".

**Prohibido:** afirmaciones absolutas para resultados probabilísticos ("Determino que...", "Es", "Garantizo"). El agente Keyons nunca decreta; siempre calibra.

### **KYN-PRD-UIX-043  |  Manejo lingüístico de fallos y respuestas de "no sé" del modelo**

Cuando el modelo no tiene información suficiente para responder con calidad, la respuesta **DEBE** ser honesta y orientar al usuario hacia una alternativa productiva. Prohibidas las respuestas evasivas, las alucinaciones para "salvar" la respuesta, o los mensajes genéricos de sistema.

#### ***Estructura obligatoria de respuesta ante limitación del modelo***

* Reconocimiento explícito de la limitación en lenguaje humano.  
* Explicación breve de la causa cuando corresponda (falta información, tema fuera de dominio configurado, datos insuficientes).  
* Al menos una ruta alternativa productiva ofrecida al usuario.

**Ejemplo correcto:** "No tengo información sobre pagos anteriores a 2023 porque solo tengo acceso a los registros del año en curso. ¿Quieres que te ayude a solicitar el historial completo al equipo de soporte?" Ejemplo prohibido: "Lo siento, no puedo procesar esa solicitud en este momento."

## Sección J — Onboarding, personalización y feedback multimodal

*Normas sobre cómo el usuario aprende el producto por primera vez, qué elementos puede personalizar, y cómo el sistema comunica multimodalmente su estado.*

### **KYN-PRD-UIX-044  |  Tour guiado obligatorio de primera vez con lógica contextual**

Todo producto Keyons **DEBE** ofrecer al usuario, en su primer acceso, un tour guiado interactivo que explique las funciones principales sin necesidad de consultar manuales externos. El tour cumple tres reglas obligatorias.

* Duración total del tour completo entre 2 y 5 minutos como máximo.  
* Salteable en cualquier momento con opción de retomar más tarde desde el menú de ayuda.  
* **Contextual:** Cuando el usuario entra a un módulo por primera vez, se activa un mini-tour específico de ese módulo, no se le repite el tour general.

El tour usa léxico profesional pero narrado accesible, y prioriza mostrar acciones reales del flujo operativo, no descripciones estáticas de la interfaz. La calidad del tour guiado es determinante en la primera impresión del cliente y en la tasa de adopción temprana del producto.

### **KYN-PRD-UIX-045  |  Frontera obligatoria entre elementos personalizables y elementos fijos**

En cada producto Keyons, la interfaz contiene dos tipos de elementos claramente diferenciados por naturaleza. Esta frontera **DEBE** declararse formalmente antes del lanzamiento del producto.

#### ***Elementos personalizables por el cliente (administrador del tenant)***

Elementos que el administrador del tenant **PUEDE** modificar desde el panel de configuración del vertical, para adaptar la interfaz a su operación. Ejemplos típicos: items visibles del menú lateral, orden de columnas de tablas, campos visibles en formularios, dashboards activos y su orden, activación o desactivación de módulos opcionales.

#### ***Elementos fijos estandarizados por Keyons (no personalizables)***

Elementos que no pueden modificarse desde la configuración del tenant, porque su personalización comprometería la solidez, seguridad o coherencia del producto. Ejemplos típicos: comportamiento del agente Estela, lógica de HITL por nivel, sistema de comunicación de confianza del modelo, estructura de mensajes de error, presencia obligatoria de rollback, elementos de la firma UX Keyons declarados en KYN-PRD-UIX-012.

Cada vertical Keyons declara en su Ficha Estándar de Producto la lista de elementos personalizables y la lista de elementos fijos. Sin esta declaración, el vertical no puede lanzarse comercialmente. La modificación de un elemento fijo por solicitud puntual de un cliente NO se ejecuta por soporte de Keyons sin RFC formal aprobado por los Aprobadores Generales conforme a KYN-PRD-GOB-015.

### **KYN-PRD-UIX-046  |  Modalidades de feedback multimodal según urgencia y contexto**

El feedback del sistema al usuario se ajusta al nivel de urgencia del evento y al contexto operativo, aplicando escalada progresiva de modalidades sin sobrecargar sensorialmente al operador.

* **Feedback rutinario (urgencia baja):** solo texto o cambio visual sutil. Ejemplo: confirmación de guardado automático de un formulario.  
* **Feedback importante (urgencia media):** texto más icono con contraste moderado. Ejemplo: alerta de límite de plan cerca de agotarse.  
* **Feedback crítico (urgencia alta):** texto, icono, animación breve y opcionalmente sonido corto. Ejemplo: pago fallido en operación crítica de facturación.  
* **Feedback catastrófico (urgencia máxima):** modal bloqueante con las tres modalidades activas y opción única de acción. Ejemplo: pérdida total de conectividad durante la transacción.

El sonido se usa con moderación extrema y siempre configurable por el usuario. En contextos móviles el sonido puede reemplazarse por vibración. La escalada multimodal debe justificarse por la urgencia operativa real, nunca por preferencia estética del diseñador.

## Sección K — Validación, medición y evolución del diseño

*Normas sobre cómo Keyons prueba que un diseño funciona antes de lanzarlo y cómo mide su desempeño después. Sin validación empírica y sin medición sostenida, el manual UX es teoría no verificable. Estas normas convierten al Método Prisma en disciplina auditable.*

### **KYN-PRD-UIX-047  |  Protocolo obligatorio de usability testing pre-lanzamiento**

Ningún vertical Keyons se lanza comercialmente sin haber completado protocolo de usability testing con usuarios reales del sector destino. Este protocolo es requisito obligatorio de la Fase Anochecer del Método Prisma.

#### ***Requisitos mínimos del protocolo***

* Mínimo 5 usuarios reales del sector destino, no del equipo Keyons ni del sponsor contratante. Los usuarios corresponden al arquetipo operativo declarado en KYN-PRD-UIX-007.  
* Sesiones estructuradas con guion de tareas operativas reales, no exploración libre.  
* Observación de completitud, tiempo por tarea, puntos de fricción y comentarios verbatim del usuario.  
* Reporte formal de hallazgos con severidad clasificada (crítico / importante / menor).  
* Ajustes al prototipo aplicados y validados nuevamente antes de lanzar. Hallazgos críticos no resueltos bloquean lanzamiento.

Cuando el cliente contrata investigación en sitio, el usability testing puede ejecutarse en el lugar de operación real. Cuando no, se ejecuta remotamente con operadores reales convocados específicamente para el ejercicio.

### **KYN-PRD-UIX-048  |  Métricas UX obligatorias de éxito por producto**

Todo vertical Keyons **DEBE** monitorear continuamente las siguientes métricas UX de éxito durante la Fase Galaxia. Los resultados alimentan las decisiones de mejora del producto y el aprendizaje sistemático entre proyectos.

* **Tasa de completitud de flujos críticos:** Porcentaje de usuarios que inician y completan cada flujo operativo principal del producto (alta de cliente, procesamiento de pago, exportación de reporte). Umbral mínimo aceptable: 85%.  
* **Tiempo a primera acción exitosa (Time to First Value):** Tiempo transcurrido desde el primer login hasta que el usuario completa su primera acción operativa exitosa. Umbral orientador: menos de 10 minutos para verticales estándar.  
* **Tasa de abandono en flujos multi-paso:** Porcentaje de usuarios que abandonan cada paso intermedio de un flujo multi-paso. Los pasos con abandono superior a 25% se rediseñan.  
* **Frecuencia de uso de rollback:** Cantidad de veces que los usuarios usan mecanismos de reversión. Frecuencia alta puede indicar problema de diseño en la acción original que motiva la reversión.  
* **Satisfacción cualitativa:** Encuesta breve tras primeras 4 semanas de uso con NPS interno del producto y campo abierto de comentarios. Frecuencia trimestral en fase Galaxia.

Las métricas se registran en el sistema de observabilidad UX de Keyons (Polaris) y se revisan formalmente en cada ciclo de revisión conforme a KYN-PRD-GOB-016. Umbrales específicos por vertical se declaran en la Ficha Estándar de Producto.

### **KYN-PRD-UIX-049  |  Auditoría UX interna por ciclo de revisión del manual**

En cada ciclo de revisión del manual conforme a KYN-PRD-GOB-016, todos los verticales activos se someten a auditoría UX interna que verifica cumplimiento de las normas de este capítulo. La auditoría se ejecuta por el Digital Creative Strategist o por rol delegado con autorización expresa.

#### ***Alcance mínimo de la auditoría UX interna***

* Verificación del cumplimiento de la firma UX Keyons declarada en KYN-PRD-UIX-012.  
* Verificación del cumplimiento de la matriz HITL declarada en la Ficha Estándar de Producto.  
* Verificación de cumplimiento WCAG 2.2 nivel AA.  
* Revisión de métricas UX del período conforme a KYN-PRD-UIX-048 y comparación contra umbrales declarados.  
* Detección de patrones oscuros conforme a KYN-PRD-UIX-006 (no debería haber ninguno; su detección activa corrección inmediata).  
* Revisión del banco de aprendizajes contribuidos por el vertical al sistema de diseño Keyons.

El reporte de auditoría se registra formalmente y sus hallazgos alimentan propuestas RFC conforme a KYN-PRD-GOB-015 cuando revelen necesidad de ajustar normas o el sistema de diseño.

### **KYN-PRD-UIX-050  |  Checklist obligatorio de auditoría UX pre-lanzamiento**

Ningún vertical Keyons se lanza comercialmente sin completar formalmente el Checklist de Auditoría UX Pre-Lanzamiento firmado por el Digital Creative Strategist y el Product & AI Lead. El checklist es aplicación operativa del Protocolo de Homologación Keyons definido en KYN-PRD-GOB-023.

#### ***Puntos de verificación obligatorios del checklist***

* Método Prisma completado con evidencia formal de las 4 primeras fases (Amanecer, Mediodía, Atardecer, Anochecer).  
* Doble Mirada Psicológica aplicada y documentada en las decisiones de diseño principales.  
* Usability testing con mínimo 5 operadores reales completado y hallazgos críticos resueltos.  
* Arquetipos operativos declarados y validados con investigación de la Fase Mediodía.  
* Matriz HITL declarada formalmente en Ficha Estándar de Producto.  
* Nivel de visibilidad de fuentes RAG declarado en Ficha Estándar de Producto.  
* Nivel WCAG cumplido declarado con excepciones justificadas.  
* Modo de densidad visual por default declarado con justificación.  
* Lista de elementos personalizables y fijos declarada.  
* Cumplimiento verificado de todos los elementos de la Firma UX Keyons.  
* Ausencia verificada de patrones oscuros conforme a la taxonomía de KYN-PRD-UIX-006.  
* Métricas UX definidas y sistema de monitoreo configurado para arranque de Fase Galaxia.

El checklist se conserva en el expediente del proyecto conforme a KYN-PRD-GOB-022 y se revisa formalmente en las auditorías UX internas subsiguientes.

### **KYN-PRD-UIX-051  |  Sistema de aprendizaje sistemático entre proyectos**

Cada proyecto Keyons **DEBE** contribuir formalmente al Sistema de Aprendizaje UX de la empresa durante y al cierre de cada fase del Método Prisma. Este sistema es lo que materializa el diferenciador declarado en KYN-PRD-UIX-004 y capitaliza el conocimiento acumulado como activo reutilizable en futuros proyectos.

#### ***Contribuciones obligatorias al sistema de aprendizaje***

* Hallazgos de la Fase Mediodía sobre comportamiento operativo real del sector destino, categorizados para consulta por futuros proyectos del mismo sector.  
* Patrones de flujo que funcionaron especialmente bien y merecen consideración como candidatos a componentes canónicos del sistema de diseño.  
* Patrones que fallaron y las hipótesis sobre por qué fallaron, para evitar repetir el error.  
* Ajustes aplicados durante la Fase Galaxia y su impacto medido en las métricas UX.  
* Solicitudes recurrentes de clientes o usuarios que sugieren evolución del sistema de diseño o de las normas de este capítulo.

El sistema de aprendizaje se revisa formalmente en cada ciclo de revisión del manual conforme a KYN-PRD-GOB-016. Los hallazgos con implicación normativa se convierten en propuestas RFC conforme a KYN-PRD-GOB-015. Sin este sistema, cada proyecto Keyons reinventa la rueda; con él, la empresa evoluciona acumulativam 

### **KYN-PRD-UIX-052 | Márgenes de personalización por modalidad de contratación**

Todas las normas de este capítulo aplican de forma primaria y no negociable a ambas modalidades de contratación de Keyons: los verticales SaaS estandarizados vendidos por suscripción y los proyectos de desarrollo a medida (MED) conforme a KYN-PRD-MED-001. Esta norma consolida en un solo lugar los márgenes de personalización que Keyons admite acordar contractualmente con el cliente en cualquier modalidad, y declara explícitamente qué elementos de UX no son negociables bajo ninguna circunstancia contractual.

#### ***Propósito de esta norma***

Cuando un cliente MED contrata desarrollo a medida, es natural que solicite adaptaciones al comportamiento default de las normas UIX. La flexibilidad es parte del valor comercial de un proyecto MED. La flexibilidad, sin embargo, no es ilimitada: existen elementos que constituyen la firma UX de Keyons y la disciplina institucional del diseño, y esos no se negocian aunque el cliente pague por personalizarlos. Esta norma clarifica dónde termina la personalización admisible y dónde comienza la disciplina institucional no negociable, protegiendo simultáneamente la relación con el cliente y la coherencia interna de Keyons.

#### ***Clasificación de las normas UIX por margen de personalización***

Las normas de este capítulo se clasifican en tres categorías según su margen de personalización contractual. La categoría de cada norma se declara formalmente en el Acuerdo de Personalización UX del proyecto, firmado por el cliente y por los Aprobadores Generales antes de arrancar la Fase Anochecer del Método Prisma.

#### ***Categoría 1 — No negociables bajo ninguna modalidad contractual***

Son normas que constituyen la firma UX Keyons, la disciplina ética institucional o requisitos legales aplicables. No se personalizan aunque el cliente lo solicite y ofrezca sobreprecio.

* Marco de arquitectura biocognitiva dual (KYN-PRD-UIX-001) — doctrina de calidad institucional.  
* Prohibición taxonómica de patrones oscuros (KYN-PRD-UIX-006) — ética institucional no negociable, regida por su propio protocolo de declinación.  
* Firma UX Keyons (KYN-PRD-UIX-012) — elementos silenciosos que unifican la experiencia entre productos del portafolio.  
* Comunicación tripartita de confianza del modelo (KYN-PRD-UIX-016) — parte de la firma UX Keyons y coherencia entre productos.  
* Estructura tripartita obligatoria de mensajes de error (KYN-PRD-UIX-024) — parte de la firma UX Keyons.  
* Ruta alternativa obligatoria ante fallo del sistema (KYN-PRD-UIX-023) — protección operativa del usuario final.  
* Reversibilidad como red de seguridad emocional (KYN-PRD-UIX-025) — protección operativa del usuario final.  
* Cumplimiento mínimo WCAG 2.2 nivel AA (KYN-PRD-UIX-038) — cumplimiento legal en múltiples jurisdicciones.  
* Prohibición absoluta de códigos técnicos crudos visibles al usuario final — parte de la firma UX Keyons.

#### ***Categoría 2 — Parcialmente negociables dentro de parámetros establecidos***

* Son normas donde el cliente puede ajustar la configuración dentro de un rango operativo previamente definido por Keyons, siempre con justificación operativa razonable y sin comprometer la solidez del producto.  
* Nivel de HITL por tipo de acción (KYN-PRD-UIX-014 y KYN-PRD-UIX-015), el cliente puede solicitar ajustes de nivel dentro del marco general, con los límites definidos en KYN-PRD-UIX-015 (nunca reducir Nivel 4 a Nivel 1 o sin HITL).  
* Nivel de visibilidad de fuentes RAG (KYN-PRD-UIX-032), el cliente elige entre las tres opciones definidas según sensibilidad regulatoria de su sector.  
* Modo de densidad visual por default (KYN-PRD-UIX-029),  el cliente elige entre modo cómodo o modo denso según perfil operativo esperado.  
* Umbrales específicos de tiempo de espera para operaciones particularmente lentas del vertical (KYN-PRD-UIX-021), pueden ampliarse dentro de márgenes razonables cuando corresponde a operaciones técnicas que naturalmente requieren más tiempo (procesamiento de documentos extensos, integraciones con servicios externos lentos).  
* Voz del sistema (KYN-PRD-UIX-040),  puede adaptarse al tono corporativo del cliente manteniendo los tres atributos base (profesional pero cercana, precisa pero humana, calibrada según certeza).  
* Configuración del tour guiado (KYN-PRD-UIX-044),  el cliente decide si activarlo por default para todos los usuarios nuevos o solo bajo demanda; la existencia del tour como capacidad no es negociable.  
* Tipos de decisión que aplican a cada nivel de explicabilidad (KYN-PRD-UIX-019), el cliente clasifica sus tipos de decisión dentro del marco de tres niveles definido.

#### ***Categoría 3 — Totalmente negociables como opción comercial del cliente***

Son normas que definen elementos donde el cliente tiene autonomía plena para decidir según su modelo de negocio, siempre dentro de la modalidad de contratación acordada.

* Estela en el producto: todos los productos Keyons llevan a Estela. En verticales SaaS estandarizados, Estela está siempre presente, con su nombre y su estética, y no se desactiva. En proyectos MED, el cliente puede personalizar el agente conforme a lo que se detalle en el capítulo EST.  
* Marca visual del producto, el producto puede llevar marca del cliente en modalidad white-label conforme a lo pactado en contrato MED. En verticales SaaS, la base es la marca Keyons y el administrador del tenant puede aplicar una personalización ligera por su cuenta (logo, color de marca, tipografía en las zonas permitidas, portada y documentos que emite), sin afectar la legibilidad. Las zonas y los límites se definen en el capítulo Productos del Sistema de Diseño.  
* Estructura del menú lateral, disposición y orden de dashboards, campos visibles en tablas y formularios personalizables, el cliente configura desde el panel administrativo del tenant sin necesidad de intervención de Keyons.  
* Activación o desactivación de módulos opcionales del vertical, el cliente configura según los módulos contratados.  
* Integraciones con servicios externos específicos del cliente — se acuerdan caso a caso en el alcance del proyecto MED.

#### ***Regla operativa para proyectos MED***

Toda personalización que caiga en Categoría 2 o Categoría 3 se registra formalmente en el Acuerdo de Personalización UX del proyecto MED, firmado por el cliente y por los dos Aprobadores Generales antes de arrancar la Fase Anochecer del Método Prisma. El acuerdo detalla cada personalización solicitada, su categoría, la justificación operativa del cliente y las eventuales consecuencias operativas de la personalización (por ejemplo, si reduce nivel HITL en una acción específica, se documenta el análisis de riesgo que respalda la reducción).

Toda personalización que caiga en Categoría 1 se declina formalmente al cliente cuando la solicita, con explicación profesional de la razón. Si el cliente insiste después de la explicación, aplica el protocolo de declinación descrito en la norma correspondiente (KYN-PRD-UIX-006 para patrones oscuros, y regla general de KYN-PRD-UIX-015 para HITL).

#### ***Regla operativa para verticales SaaS estandarizados***

En verticales SaaS estandarizados, la personalización por parte del cliente se limita exclusivamente a las opciones expuestas en el panel administrativo del tenant, sin desarrollo específico. Solicitudes de personalización que excedan las opciones expuestas por default en el panel se evalúan como potencial proyecto MED complementario, o se declinan si no encajan con el modelo comercial del vertical, siempre conforme a KYN-PRD-SAAS-024.

#### ***Registro y trazabilidad***

Cada proyecto MED conserva su Acuerdo de Personalización UX en el expediente formal del proyecto conforme a KYN-PRD-GOB-022 durante los diez años de retención documental. Los ajustes posteriores al acuerdo requieren addendum firmado por ambas partes.
