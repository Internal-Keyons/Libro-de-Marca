# Bloque 4 · capítulos restantes · 17 de noviembre de 2026 · borrador

**Capítulos:** 11, 14, 15, 19, 23, 24, 25, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43 y 45.

**Normas emitidas en borrador:**
- FUI-015 a 017;
- CPE-008 a 013;
- PAT-011 y 012;
- CNT-001 a 009;
- DAV-007 a 012;
- IAE-001 a 012;
- SPR-005 a 014;
- MOV-001 a 007;
- GOB-004 a 011.

**Total:** 63 normas.

**El Sistema de Diseño hoy:**
- los 45 capítulos tienen contenido;
- hay **151 normas en borrador**, sin códigos reservados pendientes;
- el buscador tiene 647 entradas.

## Profundidad: honestidad sobre el alcance

Este bloque es más breve que el Bloque 3.
- La mayoría de los capítulos lleva sus requisitos base, una composición principal (tabla o filas) y una verificación concreta. **No están desarrollados al mismo nivel que los prioritarios.**
- Los capítulos de componentes y patrones de este bloque (14, 15, 19) y los de IA (30 a 33) tienen tablas de decisión.
- Los de productos, movimiento y gobierno (34 a 45) son normas breves.

## Duplicaciones evitadas

| Norma de su texto | Dónde quedó |
| --- | --- |
| Expresión proporcionada (11) | Se emite como FUI-017 y cita PEX-001 (01), que fija el principio |
| Consecuencias claras (19) | Integrada en Contexto antes de actuar, PEX-006 (01). El 19 conserva Autorización y Trazabilidad |
| Resultado visible (15) | CPE-011 desarrolla los componentes de PEX-004 (01) |
| Notificaciones de UIX-030 y UIX-046 | Unidas en Atención proporcionada (CPE-013) |

## Cobertura por capítulo

| Cap. | Desarrollado | Parcial | Pendiente o requiere aprobación |
| --- | --- | --- | --- |
| 11 Recursos visuales | Íconos funcionales, identidad, expresión | — | — |
| 14 Estructura | Qué contenedor usar, jerarquía, diálogo con anatomía y foco | Pestañas y acordeón de producto (apariencia) | Hoja de componentes |
| 15 Retroalimentación | Componentes de respuesta, mensajes, niveles de urgencia | — | Niveles de urgencia (propuesta desde UIX) |
| 19 Procesos críticos | Autorización, trazabilidad | Confirmación reforzada (en CPE-003) | — |
| 23 Escritura | Lenguaje funcional, consistencia, brevedad | Glosario por producto | Glosario de cada producto |
| 24 Mensajes | Errores en tres partes, confirmaciones, seguridad | Advertencias y espera (en 15 y 18) | — |
| 25 Localización | Formatos, traducción, espacio variable | Idiomas de derecha a izquierda | Idiomas que se ofrecen |
| 27 Gráficos | Tipo por relación, paletas (se citan), accesibilidad | — | — |
| 28 Indicadores | Anatomía, umbrales, vigencia | — | Responsables de umbrales por producto |
| 30 Principios de IA | Transparencia, niveles de confianza, supervisión por riesgo | — | Niveles de confianza y de supervisión (propuesta desde UIX) |
| 31 Conversación | Contexto, preguntas, respuesta accionable | Memoria persistente | Memoria (propuesta desde UIX-034 y 035) |
| 32 Agentes | Responsabilidad, límites, identidad | Panel de actividad del agente | — |
| 33 Confianza segura | Calibración, verificación humana, privacidad | Visibilidad de fuentes por sector | — |
| 34 Base compartida | Reutilización, variaciones, compatibilidad | Firma UX (lista de comportamientos) | Lista de la firma UX |
| 35 Sitio web | Navegación y propósito, interacción | Contenido y SEO (fuera de alcance) | — |
| 36 Herramientas | Eficiencia, permisos | — | — |
| 38 White-label | Identidad, calidad, ausencia de firma | Límites de personalización (SPR-003) | — |
| 39 Operación activa | Movimiento funcional, duración | Curvas y duraciones por componente | Tokens de curva |
| 40 Movimiento editorial | Propósito, comprensión independiente | — | — |
| 41 Multisensorial | Sonido, háptica, alternativas | — | — |
| 42 Gobierno normativo | Fuente única, estado visible | Responsables y firmantes | Roles de aprobación |
| 43 Implementación | Canónicos, excepciones, entrega con pruebas | — | — |
| 45 Documentación | Componentes documentados, ejemplos, versionado | Plantilla de documentación | — |

**Estado:** todos son borrador con contenido. Ninguno se declara terminado.

## Pruebas

| Prueba | Resultado |
| --- | --- |
| `verificar.py` | 0 errores |
| Líneas dobles en las 23 páginas | 0 |
| Desborde a 375 px | Ninguno |
| `menu-etiquetas.js` | `[]` |
| Enlaces | 0 rotos |
| Códigos reservados pendientes | Ninguno |
| Pendiente | Prueba con lector de pantalla real; revisión de Keylin de los textos redactados por Claude |

**Capturas:** `propuestas/capturas-sd-bloque-4/`, una hoja de escritorio y una de móvil por capítulo, tomadas sin foco.

## Archivos

- `tools/sd/m03b_recursos_componentes.py`, `m07_contenido.py`, `m09_ia_estela.py` y `m10b_productos_movimiento_gobierno.py`;
- `docs/sd/fuente-keylin-2026-11-17.md` (sección del Bloque 4);
- las páginas y registros regenerados.
