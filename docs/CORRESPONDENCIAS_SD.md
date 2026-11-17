# Identificadores del Sistema de Diseño · correspondencias

Revisión del 2026-11-12, dentro de la intervención P3 de la Biblioteca. Este documento es interno: no se publica (`.vercelignore`).

## Esquemas encontrados

| Esquema | Dónde aparece | Estado | Decisión |
|---|---|---|---|
| `KYN-PRD-UIX-###` | `normas-ux-sistema-diseno.md`, `data/sistema-diseno.json` (campo `norma`), `ia/normas/KYN-PRD-UIX-001…052.md`, `data/sd-capitulos/principios-compartidos.html` | 52 identificadores emitidos | Se conservan sin cambios. Son identificadores históricos del Manual de Producto que el Sistema de Diseño cita. |
| `KYN-SDI` | `js/sistema-diseno.js` (códigos de módulo en la plantilla, `KYN-SDI-PEX`…), `data/gobierno.json`, `docs/SISTEMA_DE_DISENO_NORMAS.md` (ejemplo `KYN-SDI-PEX-001`) | Ningún ID con número emitido | Queda reservado para las normas nuevas del Libro 02: `KYN-SDI-<MÓDULO>-###`. |
| Sin identificador | Subcapítulos de `data/sistema-diseno.json` sin campo `norma` | Contenido en estructura o pendiente | Siguen sin ID. Un subcapítulo recibe ID solo cuando Keylin aprueba su norma. |

Comprobaciones hechas antes de decidir:
- `KYN-SDI-` seguido de un número no aparece en ningún archivo del libro. El prefijo está libre.
- Los 52 `KYN-PRD-UIX` no se repiten en `data/sistema-diseno.json` ni coinciden con ningún `KYN-MRK`.
- `KYN-PRD` figura en la Guía como prefijo de Producto e Ingeniería, con sus identificadores históricos.

## Correspondencias y excepción por inmutabilidad

- Las normas heredadas `KYN-PRD-UIX-###` mantienen su ID para siempre (identificadores permanentes desde la versión 1).
- **Excepción documentada:** el segmento `KYN-PRD-UIX` queda reservado para esas normas heredadas. Cuando se construya Producto e Ingeniería, sus normas nuevas usarán `KYN-PRD` con otros segmentos de área, nunca `UIX`.
- Si una norma heredada se reescribe como norma propia del Sistema de Diseño, recibe un `KYN-SDI` nuevo y la heredada queda «integrada en» la nueva, con su ID intacto. Ningún contenido pasa a vigente por este documento.

| Libro | Prefijo | Normas emitidas |
|---|---|---|
| Marca y Experiencia | `KYN-MRK` | 126 (`data/normas.json`) |
| Sistema de Diseño | `KYN-SDI` | 6 emitidas en borrador (ARQ-005 a 010, capítulo 05) y 25 reservadas, en `data/sd-normas.json` |
| Sistema de Diseño (heredadas) | `KYN-PRD-UIX` | 52 |

## Verificación

`python tools/verificar.py` revisa en cada corrida: IDs duplicados en los dos registros y entre ellos, normas `KYN-PRD-UIX` citadas sin su archivo en `ia/normas`, `KYN-SDI` emitidos sin registro, referencias `KYN-MRK` del Sistema de Diseño a normas inexistentes, anclas de los dos índices, bloques «Normas relacionadas» y la estructura de cada norma redactada.

## Actualización del 2026-11-17

- Registro propio: `data/sd-normas.json` (fuente única de los códigos `KYN-SDI-<módulo>-###`). Lo generan y leen `tools/sd_capitulos.py`, `tools/niveles.py` y `tools/verificar.py`.
- Códigos de módulo en uso: PEX (Experiencia, capítulos 01–03) y ARQ (Arquitectura, capítulos 04–06). Decisión de Keylin: un código por norma.
- Emitidas en borrador, con página: KYN-SDI-ARQ-005 a 010 (capítulo 05 Navegación).
- Reservadas, sin página ni buscador: PEX-001 a 015 y ARQ-001 a 004 y 011 a 016. `verificar.py` da error si una reservada aparece publicada.
- Las UIX conservan su ID; su destino en los 45 capítulos está en `propuestas/auditoria-uix-2026-11-17.md`; la matriz, en `propuestas/matriz-normativa-sd-01-06.md`.
