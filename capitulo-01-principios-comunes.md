# Sistema de Diseño · Módulo Experiencia · 01 Principios comunes

**Estado:** contenido para aprobación de Keylin.
**Reemplaza:** los ocho subcapítulos actuales (Claridad y orientación, Consistencia y previsibilidad, Control y confianza, y las normas 01.01.04 a 01.01.08).

**Convención de redacción:** cada enunciado de la norma está en indicativo. Su nivel (Debe, Debería, Puede) va en una etiqueta al inicio de la fila, no dentro de la frase. En la versión md para IA, cada enunciado lleva su nivel entre corchetes: [DEBE], [DEBERÍA] o [PUEDE].

Las frases entre `**` son la única frase destacada en semibold de cada bloque.

---

## Apertura del capítulo

**Título:** Principios comunes

**Bajada:** Cinco principios que rigen el diseño de **todos los productos digitales de Keyons**: SaaS de nicho, herramientas internas y desarrollos a medida. Son la base de los demás capítulos de este libro.

**A quién está dirigido:** equipos de diseño, desarrollo y producto, y agentes de IA que construyen interfaces Keyons.

**Cómo leer las normas:**

| Etiqueta | Significado |
| --- | --- |
| Debe | Requisito obligatorio. |
| Debería | Recomendación. Si no se aplica, se documenta el motivo. |
| Puede | Alternativa permitida. |

---

## 1 · Claridad

**Rótulo:** KYN-PRD-UIX-001 · Claridad

**Titular:** Cada pantalla presenta solo la información necesaria para la tarea en curso

**Fundamento:** En contextos operativos, la atención es limitada y las tareas se interrumpen con frecuencia. **Reducir la carga cognitiva de cada pantalla** acorta el tiempo de decisión y disminuye los errores.

**Norma:**

| Nivel | Enunciado |
| --- | --- |
| Debe | Cada pantalla tiene una acción principal identificable en menos de 5 segundos. |
| Debe | El título y la ruta de navegación indican dónde está la persona y en qué tarea. |
| Debe | La jerarquía visual dirige la atención primero a las excepciones, los riesgos y las decisiones pendientes. |
| Debería | La información complementaria está disponible a un clic, fuera de la vista principal, según la norma de revelación progresiva. |
| Debe | Cuando el sistema dispone de un dato, lo presenta como propuesta para que la persona lo revise y lo apruebe. |

---

## 2 · Coherencia

**Rótulo:** KYN-PRD-UIX-013 · Coherencia

**Titular:** Todos los productos Keyons comparten la misma lógica de uso

**Fundamento:** La coherencia reduce la curva de aprendizaje: **lo que una persona aprende en un producto le sirve en el siguiente**. Los comportamientos previsibles permiten concentrar la atención en el trabajo y no en la interfaz.

**Norma:**

| Nivel | Enunciado |
| --- | --- |
| Debe | Guardar, editar, cancelar y eliminar significan lo mismo y se comportan igual en todos los módulos y productos. |
| Debe | Cada acción muestra su estado: pendiente, en proceso, completada o fallida. |
| Debe | Los tokens y los componentes del sistema se aplican sin variaciones entre productos. |
| Debe | Las tareas comunes siguen la misma secuencia en todos los productos. |
| Debe | Estela mantiene su identidad y su comportamiento en todos los productos. |
| Puede | La identidad del cliente cambia el color y la marca; las convenciones de uso se mantienen. |

---

## 3 · Control

**Rótulo:** KYN-PRD-UIX-005 · Control

**Titular:** La persona conserva el criterio en cada decisión

**Fundamento:** Un sistema con IA actúa sobre datos y procesos reales. Para confiar en él, **la persona necesita entender qué hace, anticipar sus consecuencias y poder intervenir** en cualquier momento.

**Norma:**

| Nivel | Enunciado |
| --- | --- |
| Debe | Antes de una acción significativa, la interfaz muestra sus consecuencias. |
| Debe | La interfaz distingue lo que propone la IA, lo que está pendiente de verificación y lo que aprobó una persona. |
| Debe | La persona puede intervenir, revertir y decidir sobre lo que hace el sistema, según la matriz de intervención humana. |
| Debe | Ante un fallo, la interfaz informa el estado real y ofrece cómo continuar. |
| Debe | Cuando dos criterios de diseño compiten, se aplica el orden de prioridad que sigue. |

**Orden de prioridad** (lista numerada compacta):
1. Transparencia antes que fluidez
2. Control antes que automatización
3. Comprensión antes que velocidad
4. Ergonomía antes que estética
5. Convención antes que novedad, salvo que la innovación aporte un valor comprobado

---

## 4 · Diseño honesto

**Rótulo:** KYN-PRD-UIX-006 · Diseño honesto

**Titular:** Cada decisión se toma con información clara y en libertad

**Fundamento:** Las técnicas que presionan o confunden mejoran métricas de corto plazo, pero deterioran la confianza, la reputación del cliente y su cumplimiento regulatorio. **Un producto honesto sostiene la relación a largo plazo.**

**Norma:**

| Nivel | Enunciado |
| --- | --- |
| Debe | Las opciones de aceptar y rechazar se redactan con el mismo respeto. |
| Debe | El color y la etiqueta de cada acción muestran su naturaleza real, también en cobros y acciones irreversibles. |
| Debe | Los plazos y la disponibilidad que se comunican son reales. |
| Debe | Cancelar requiere el mismo esfuerzo que contratar. |
| Debe | Los consentimientos sensibles (uso de datos, cobros recurrentes, procesamiento con modelos externos) los activa la persona. |
| Debe | Cada notificación responde a una necesidad real de la persona. |
| Debe | La persona controla la carga de contenido y la reproducción de medios. |
| Debe | Ante un pedido del cliente que comprometa estos criterios, Keyons propone una alternativa que cumple el mismo objetivo. Si el cliente lo mantiene, los Aprobadores Generales declinan ese alcance por escrito. |

---

## 5 · Firma UX

**Rótulo:** KYN-PRD-UIX-012 · Firma UX

**Titular:** Ocho elementos que hacen reconocible la calidad Keyons

**Fundamento:** La calidad percibida se construye en los detalles que se repiten. **Estos elementos son iguales en todos los productos** y hacen que la experiencia se reconozca como Keyons, con cualquier marca.

**Norma:**

| Nivel | Enunciado |
| --- | --- |
| Debe | Todo producto incluye los ocho elementos de la firma UX. Ningún cliente los personaliza. |

**Los ocho elementos** (lista en dos columnas):
1. Mensajes de error con tres partes: qué pasó, por qué y qué hacer
2. Mensajes en lenguaje claro, sin códigos técnicos
3. Esperas que describen la acción en curso
4. La misma confirmación al completar una acción
5. Opción de deshacer visible en toda acción reversible
6. Estela con el mismo comportamiento en todos los productos
7. Confianza de la IA comunicada con etiqueta, color e ícono
8. Diseño honesto en todas las decisiones

---

## Cierre del capítulo

**Lista de verificación** (casillas circulares):
- La acción principal de cada pantalla se identifica en menos de 5 segundos.
- Las acciones comunes se comportan igual que en los demás productos Keyons.
- Lo que propone la IA se distingue de lo que aprobó una persona.
- Las decisiones sensibles las activa la persona y los plazos comunicados son reales.
- Los ocho elementos de la firma UX están presentes.

**Botón discreto:** Descargar para usar con IA (.md)

---

# Diagramación

Esta sección es para Claude desarrollador. No se publica.

## Modelos

Los capítulos Concepto, Principios e Identidad del libro de marca, con los espacios que ya mediste:
- 32 px entre el titular y la entrada.
- 48 px entre la entrada y el componente.
- 32 px arriba y 128 px abajo de cada sección, con una línea fina entre secciones.

## Pieza por pieza

| Pieza | Cómo se diagrama |
| --- | --- |
| Apertura del capítulo | El encabezado de capítulo que ya usa el libro |
| «Cómo leer las normas» | Tres filas: la etiqueta a la izquierda y el significado a la derecha. Peso regular |
| Rótulo de cada principio | A la izquierda: el ID en gris terciario de 12 px y debajo el nombre en 14 px. Sin estado |
| Titular | El titular gris de los capítulos modelo |
| Fundamento | La entrada de 20 px de los modelos, con una sola frase en semibold (la marcada con `**`) |
| Norma | Filas separadas por línea de 1 px en Cielo 100. A la izquierda, la etiqueta del nivel como badge en píldora de 12 px, peso 500, texto Azul Noche: Debe con fondo Cielo 200 (#C6D5EC), Debería con fondo Gris suave (#E0E1E5) y Puede con contorno de 1 px en Cielo 200 y fondo transparente. A la derecha, el enunciado en 16 px, peso regular, Azul Noche, con un máximo de dos renglones |
| Orden de prioridad (Control) | Lista numerada compacta, debajo de la tabla de la norma |
| Los ocho elementos (Firma UX) | Lista en dos columnas con viñetas de 20 px, a 20 px del texto (R02) |
| Lista de verificación | El componente de casillas circulares del libro |
| Botón «Descargar para usar con IA» | Botón de texto, al final del capítulo |

## Reglas

- Sin maquetas de interfaz.
- Sin enlaces «Texto completo» ni bloques «Relacionado». Las referencias a otras normas van dentro del texto («según la norma de revelación progresiva»), con enlace.
- Semibold solo en la frase marcada de cada Fundamento. Nada más en semibold.
- Construí primero solo el principio 1 · Claridad. Mandame la captura y esperá mi «sigue» antes de hacer los demás.
