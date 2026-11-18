# Bloque 3 · capítulos prioritarios para Product Default y Pinar de Río · 17 de noviembre de 2026 · borrador

**Capítulos:** 07, 08, 09, 10, 12, 13, 16, 17, 18, 20, 21, 22, 26, 29, 37 y 44.

**Normas emitidas en borrador:**
- FUI-001 a 014;
- CPE-001 a 007;
- PAT-001 a 010;
- ACC-001 a 009;
- DAV-001 a 006;
- SPR-001 a 004;
- GOB-001 a 003.

**Total:** 53 normas nuevas. Con los Bloques 1 y 2 suman 88 normas en 22 capítulos.

**Fuente:** sus textos base, en `docs/sd/fuente-keylin-2026-11-17.md`, y su matriz. Las UIX se usaron como referencia evaluada.

## Requisitos que redactó Claude (requieren aprobación)

| Código | Norma | Origen |
| --- | --- | --- |
| CPE-004 | Menú de acciones | Descripción del capítulo 12: «menús» |
| PAT-010 | Estados vacíos y de espera | Matriz del 18, UIX-021 y UIX-026 |
| SPR-004 | Navegación predeterminada | Decisión que el 05 remite al 37 |
| GOB-003 | Protocolo previo al lanzamiento | Descripción del 44, UIX-047 y UIX-050 |
| ACC-001 | Referencia de conformidad | Se cambió el verbo para meter DEBE dentro de la frase |

## Decisiones que requieren aprobación

1. **Color del foco:** el token `--color-focus` es Azul Cielo y da 2,6:1 sobre Blanco Keyons, por debajo del 3:1 que pide WCAG 1.4.11. El libro usa un anillo Azul Noche. Se propone pasar el token a Azul Noche (FUI-007).
2. **Token de acción:** no existe un token semántico propio para el botón principal. Se propone `--color-action` y `--color-on-action` (FUI-002).
3. **Tamaño táctil de Keyons:** 44 × 44 px como preferencia sobre el mínimo AA de 24 × 24 px (ACC-008).
4. **Propuestas marcadas en el texto:**
   - escala tipográfica asignada por uso (FUI-008);
   - espacios por uso (FUI-012);
   - herramientas de tabla según el volumen (DAV-002);
   - gravedad de los problemas (GOB-002);
   - qué se puede personalizar (SPR-003);
   - patrón de navegación SaaS (SPR-004).
5. **El tema visual predeterminado de Product Default** todavía no está aprobado (SPR-001).

## Duplicaciones evitadas

- **Evidencia registrada (44):** es la misma obligación que PEX-014 (03), así que se cita y no se emite de nuevo.
- **Continuidad del trabajo (02):** se unió a Contexto conservado, PAT-005 (17).
- **Lectura adaptable (20):** cita Legibilidad, FUI-010 (09).
- **Teclado de menús (21):** cita ARQ-008 (05).

## Cobertura por capítulo

| Cap. | Desarrollado | Parcial | Pendiente o requiere aprobación |
| --- | --- | --- | --- |
| 07 Tokens | Niveles, roles, nomenclatura, procedimiento de cambio | Temas (solo el claro) | Tema oscuro; token de acción; catálogo completo de tokens funcionales |
| 08 Color funcional | Funciones, estados con señal, separación de significados, mínimos de contraste | — | Color del foco |
| 09 Tipografía | Familias, jerarquía, legibilidad WCAG, truncamiento | Escala por uso (propuesta) | Aprobación de la escala por uso |
| 10 Espacio y retícula | Escala, proximidad, adaptación, densidad, radios | Espacios por uso (propuesta) | Puntos de adaptación del producto (se cita ESP-004) |
| 12 Acciones | Variantes, anatomía, estados, teclado, destructivas, menú | Orden de botones en móvil (propuesta) | CPE-004; hoja de componentes aprobada para su apariencia |
| 13 Entradas | Anatomía, validación por momento, control por tipo de dato, estados, accesibilidad | Selector de fecha y de archivo (comportamiento detallado) | Hoja de componentes |
| 16 Formularios | Secuencia, prevención de pérdidas, validación proporcionada | Formularios de varios pasos (remite al 17) | Diagramación de formularios (la decide Keylin) |
| 17 Flujos de trabajo | Progreso, contexto, interrupción, terminación, ciclo de un registro | Edición masiva | Borradores automáticos (según producto) |
| 18 Recuperación | Errores y salidas, deshacer, persistencia, vacíos y esperas | Umbral de espera larga (hipótesis) | PAT-010 |
| 20 Percepción | Conformidad, alternativas por tipo, lectura adaptable | — | Matriz completa de criterios WCAG |
| 21 Operación | Teclas, trampas, atajos, foco visible y sin tapar, tiempo y movimiento | — | Color del foco (FUI-007) |
| 22 Adaptación | Reorganización, orientación, tamaños en tres niveles, variaciones de uso | — | Preferencia de 44 px |
| 26 Tablas | Alineación, encabezados, accesibilidad, herramientas por volumen, acciones, móvil | Selección múltiple (acciones masivas) | — |
| 29 Dashboards | Diseño por tarea, niveles de jerarquía, profundidad y exportación | — | Indicadores (los desarrolla el 28, en el Bloque 4) |
| 37 Product Default | Componentes canónicos, sobriedad, personalización, navegación SaaS | — | Tema aprobado; SPR-004; tabla de personalización |
| 44 Validación | Tareas reales, gravedad, protocolo con cinco evidencias | — | GOB-003; número de participantes y firmantes |

**Estado:** todos los capítulos son borrador con contenido. Ninguno se declara terminado, porque todos tienen pendientes o aprobaciones.

## Pruebas

| Prueba | Resultado |
| --- | --- |
| `verificar.py` | 0 errores |
| Líneas dobles en las 16 páginas | 0 |
| Desborde a 375 px en las 16 páginas | Ninguno |
| `menu-etiquetas.js` | `[]` |
| Enlaces entre capítulos y al Libro de Marca | 0 rotos |
| Buscador | 590 entradas; las normas reservadas no aparecen |
| Pendiente | Prueba con lector de pantalla real |

**Capturas:** `propuestas/capturas-sd-bloque-3/`, una hoja de escritorio y una de móvil por capítulo, tomadas sin foco.

## Archivos

- `tools/sd/m03_fundamentos.py`, `m04_componentes.py`, `m05_patrones.py`, `m06_accesibilidad.py`, `m08_datos.py`, `m10_productos.py` y `m12_gobierno.py` (nuevos);
- `tools/sd/base.py` (enlace a normas de Marca);
- `docs/sd/fuente-keylin-2026-11-17.md`;
- las páginas y registros regenerados.
