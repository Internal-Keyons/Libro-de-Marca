---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-11"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-052"
titulo: "Márgenes de personalización por modalidad de contratación"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-052 · Márgenes de personalización por modalidad de contratación

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
