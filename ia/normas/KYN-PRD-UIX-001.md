---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-11"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-001"
titulo: "Marco de Arquitectura Biocognitiva Dual: Ergonomía Instintiva y Procesamiento Analítico"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-001 · Marco de Arquitectura Biocognitiva Dual: Ergonomía Instintiva y Procesamiento Analítico

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
