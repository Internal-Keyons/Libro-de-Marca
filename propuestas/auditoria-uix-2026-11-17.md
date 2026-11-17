# Auditoría de las normas UIX · 17 de noviembre de 2026

**Fuente:** `normas-ux-sistema-diseno.md` (Manual de Producto v1, KYN-PRD-UIX-001 a 052, traslado del 2026-11-09).
**Cómo se lee:** la fuente es un documento anterior. No es contenido vigente de la Biblioteca. Cada norma se evalúa y se le asigna un destino entre los 45 capítulos del Sistema de Diseño.
**Esta etapa:** solo se integran temas de los capítulos 01 a 06, y en esta entrega solo el 05 Navegación tiene página. Las demás normas quedan con su destino para las etapas siguientes.
**Trazabilidad:**
- Las UIX conservan su ID. Ni el ID ni el texto se copian.
- Cuando una decisión pasa a una norma nueva, la fila dice «integrada en KYN-SDI-…».
- Las normas reservadas aparecen en `propuestas/matriz-normativa-sd-01-06.md`.

Columnas:
- **Útil:** la decisión que conviene recuperar.
- **Revisar:** lo obsoleto, lo contradictorio o lo que se aparta de la Biblioteca.
- **Destino:** el capítulo del Sistema de Diseño.
- **Relación con 01–06:** la dependencia con la etapa actual.

## 1 · Normas con destino en 01–06

| UIX | Tema | Útil | Revisar | Destino | Relación con 01–06 |
| --- | --- | --- | --- | --- | --- |
| 001 | Marco biocognitivo | Atención dirigida; lo justo para decidir; el sistema propone y la persona aprueba | El lenguaje teórico extenso (capas, leyes) no va en la lectura principal | 01 · integrada en PEX-001 y PEX-003 (reservadas) | Directa |
| 005 | Doctrina operativa | Orden de prioridad ante conflictos: transparencia, control, comprensión, ergonomía, convención | «Doctrina» y «postura» son metatexto | 01 · integrada en PEX-002 (reservada); el orden de prioridad se propone como decisión de PEX-002 | Directa |
| 006 | Patrones oscuros | Taxonomía de patrones prohibidos; cancelar con el mismo esfuerzo que contratar | Por su alcance comercial y regulatorio, pide un capítulo propio | 19 Procesos críticos y 24 Mensajes; 01 la cita | Dependencia: 01 (Contexto antes de actuar) |
| 012 | Firma UX | Lista cerrada de comportamientos comunes | Mezcla mensajes (24), espera (15), reversibilidad (18) y confianza de IA (33) | Se reparte en 15, 18, 24 y 33; 34 Base compartida conserva la lista | Dependencia: 01 (Estado comprensible) |
| 013 | Coherencia entre productos | Mismos componentes, flujos y comportamientos | «Lock-in emocional» es lenguaje comercial y sale | 01 · integrada en PEX-005 (reservada); 34 Base compartida | Directa |
| 007 | Arquetipos | El arquetipo describe a quien opera el producto, no a quien lo compra | El «contenido mínimo obligatorio» corresponde a un entregable de Prisma | 02 · integrada en PEX-007 (reservada) | Directa |
| 008 | Contextos de uso | Estratégico, transaccional y de campo dentro de una misma organización | — | 02 · integrada en PEX-009 (reservada) | Directa |
| 009 | Perfiles atencionales atípicos | Diseñar para atención variable, dislexia y ansiedad operativa | Sin texto de Keylin en 02; se propone como decisión de PEX-007 | 02 (propuesta) y 20 Percepción | Directa |
| 003 | Doble mirada | Checklist de diez preguntas por decisión | Pesa demasiado en la lectura principal; va en detalle a pedido | 03 · integrada en PEX-010 (reservada) | Directa |
| 048 | Métricas UX | Completitud de flujos críticos, tiempo por tarea, errores, abandono | Las métricas exactas se validan con Producto | 03 · integrada en PEX-015 (reservada); 44 Validación | Directa |
| 028 | Revelación progresiva | Una decisión primaria por pantalla; detalle bajo demanda | «3 a 5 opciones» y «5 segundos» son hipótesis de prueba, no requisitos universales | 04 · integrada en ARQ-004 (reservada); 01 cita la acción principal | Directa |

## 2 · Normas con destino posterior y dependencia con 01–06

Estas normas quedan registradas para sus capítulos. Ninguna se mezcla en 01–06.

| UIX | Tema | Útil | Revisar | Destino | Dependencia con 01–06 |
| --- | --- | --- | --- | --- | --- |
| 011 | Tokens, componentes canónicos y patrones de flujo | Tres capas: tokens funcionales, componentes canónicos, patrones de flujo | La frontera con Marca cambió (ver 010) | 07 Tokens, 12–15 Componentes, 16–19 Patrones, 43 Implementación | 05: los controles de navegación son componentes canónicos (14 Estructura) |
| 038 | WCAG 2.2 AA | Teclado completo, foco visible y sin tapar, color más señal, objetivo mínimo de 24 × 24 px | El texto mínimo de 16 px es una decisión de 09 Tipografía, no de WCAG | 20 Percepción, 21 Operación, 22 Adaptación | 05: foco, teclado y estado de los controles de navegación |
| 039 | Móvil y escritorio | Diseño específico para pantalla táctil; acción primaria destacada; uso con una mano; estados sin conexión | **Contradicción:** pide 44 × 44 px «conforme a WCAG». El mínimo AA de WCAG 2.2 es 24 × 24 px (2.5.8); 44 × 44 px es AAA (2.5.5). Decidir el valor en 22 | 22 Adaptación | 05: ARQ-009 cita 22 para el tamaño de los objetivos |
| 025 | Reversibilidad | Deshacer visible; confirmación solo cuando no hay deshacer | — | 18 Recuperación | 05: ARQ-010 (regreso sin pérdida) |
| 023 | Ruta alternativa ante fallos | Siempre una salida manual en el mismo componente | — | 18 Recuperación | 06: errores de búsqueda (ARQ-015) |
| 024 | Mensajes de error en tres partes | Qué pasó, por qué y qué hacer | — | 24 Mensajes | 06: ARQ-015 cita 24 |
| 026 | Estados vacíos | Explicar por qué está vacío y ofrecer el siguiente paso | — | 18 Recuperación y 24 Mensajes | 06: búsqueda sin resultados (ARQ-015) |
| 041 | Microcopy | Los botones nombran la acción; etiquetas en lenguaje de la persona | — | 23 Escritura | 04 y 05: nombres de destinos (ARQ-002, ARQ-006) |
| 040 | Voz del sistema | Profesional y cercana, precisa y humana | Se apoya en el capítulo Voz del Libro de Marca y no lo repite | 23 Escritura (cita KYN-MRK-VOZ) | 04: nombres comprensibles |
| 029 | Densidad cómoda y densa | Dos modos con valor por defecto según el arquetipo | — | 10 Espacio y retícula | 02: PEX-009 (frecuencia de uso) |
| 031 | Flujos de varios pasos | Indicador de progreso siempre visible | — | 17 Flujos de trabajo | 05: los flujos de un paso son excepción de ARQ-005 |
| 044 | Recorrido de primera vez | Recorrido salteable; estados vacíos que enseñan | La propuesta P2 (3 a 5 pasos) sigue pendiente | 17 Flujos de trabajo | 05: el recorrido no reemplaza a la navegación visible (ARQ-007) |
| 030 y 046 | Urgencia de notificaciones | Cuatro niveles de urgencia; contra la fatiga por alertas | P3: fusionarlas, porque dicen lo mismo | 15 Retroalimentación | Sin dependencia directa |
| 047 | Pruebas de usabilidad | Mínimo cinco personas reales del sector antes del lanzamiento | — | 44 Validación | 03: PEX-015; 05: pruebas de ubicación de ARQ-005 |
| 049 y 050 | Auditoría y checklist previo al lanzamiento | Puntos de verificación firmados | — | 44 Validación | 01–06: las verificaciones de cada norma alimentan el checklist |

## 3 · Normas sin relación directa con 01–06

| UIX | Tema | Destino | Nota |
| --- | --- | --- | --- |
| 002 | Método Prisma | 03 (Prisma como metodología, PEX-011) y 43 Implementación | Nombres de fase oficiales: Amanecer, Mediodía, Atardecer, Anochecer y Galaxia |
| 004 | Diferenciadores de Prisma | 43 Implementación | Compara Prisma con el doble diamante. Sale de la lectura: Keyons se describe sin compararse |
| 010 | Frontera Marca / Producto | 42 Gobierno normativo | P1 pendiente: la frontera ahora es Libro de Marca / Sistema de Diseño |
| 014 y 015 | Intervención humana por riesgo | 19 Procesos críticos y 32 Agentes | — |
| 016 a 020 | Confianza, modos y explicabilidad de la IA | 30 Principios de IA y 33 Confianza segura | — |
| 021 y 022 | Espera y mensajes de espera | 15 Retroalimentación y 24 Mensajes | El umbral de 400 ms es una hipótesis que hay que validar |
| 027 | Confirmación al cerrar una tarea | 15 Retroalimentación | Hay que validar cuánto movimiento se usa (39 Operación activa) |
| 032 a 036 | Fuentes, memoria, olvido y modelos externos | 31 Conversación y 33 Confianza segura | — |
| 037 | Exportación de historiales | 29 Dashboards y 26 Tablas | — |
| 042 y 043 | Lenguaje del agente según certeza | 31 Conversación | — |
| 045 y 052 | Personalizable y fijo; márgenes por contratación | 37 Product Default y 38 White-label | — |
| 051 | Aprendizaje entre proyectos | 42 Gobierno normativo | — |

## 4 · Contradicciones y decisiones abiertas

1. **Tamaño táctil:** 44 × 44 px (UIX-039) frente a 24 × 24 px (UIX-038 y WCAG 2.2 AA). Se decide en 22 Adaptación.
2. **«5 segundos»** (UIX-001, UIX-028): queda como hipótesis inicial de prueba, no como obligación universal (indicación de Keylin, 2026-11-17).
3. **Notificaciones** (UIX-030 y 046): dicen lo mismo. Se proponen como una sola norma en 15.
4. **UIX-004** compara Prisma con otro método. La Biblioteca describe a Keyons sin compararse (reglas de voz).
5. **El capítulo 01 publicado** muestra hoy UIX-001 Claridad, de la ronda anterior. Se reemplaza cuando se construya el 01 con las normas reservadas PEX-001 a PEX-006.
