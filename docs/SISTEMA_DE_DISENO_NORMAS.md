# Sistema de Diseño · propuesta de sistema normativo

Estado: **propuesta registrada, sin códigos emitidos.** Ningún identificador de esta propuesta se usa como permanente hasta que la dirección de marca lo apruebe.

## Criterio

«Cada regla independiente de aplicación tendrá un identificador normativo único, un estado de vigencia y una ubicación documental definida».

## Espacio de nombres propuesto

`KYN-SDI-<módulo>-<número de tres cifras>`

| Prefijo | Libro | Estado |
|---|---|---|
| `KYN-MRK` | Libro de Marca | En uso (133 normas registradas) |
| `KYN-PRD` | Manual de Producto | En uso, identificadores históricos (por ejemplo, `KYN-PRD-UIX-001`) |
| `KYN-SDI` | Sistema de Diseño | **Propuesto** |

El prefijo `KYN-SDI` no choca con `KYN-MRK` ni con `KYN-PRD`. Tampoco figura en los registros del proyecto.

### Códigos de módulo propuestos

| Módulo | Código | Nombre corto |
|---|---|---|
| 01 | PEX | Experiencia |
| 02 | ARQ | Arquitectura |
| 03 | FUI | Fundamentos |
| 04 | CPE | Componentes |
| 05 | PAT | Patrones |
| 06 | ACC | Accesibilidad |
| 07 | CNT | Contenido |
| 08 | DAV | Datos |
| 09 | IAE | IA y Estela |
| 10 | SPR | Productos |
| 11 | MOV | Movimiento |
| 12 | GOB | Gobierno |

Ejemplo, todavía sin emitir: `KYN-SDI-PEX-001` sería la primera norma de Principios de experiencia.

## Niveles documentales

| Nivel | Lleva código | Ejemplo |
|---|---|---|
| Módulo | Código de módulo (PEX), no de norma | 01 · Principios de experiencia |
| Capítulo | No; número visible correlativo (01 a 45) | 01 · Principios compartidos |
| Subcapítulo | No; ancla estable (`#s-01-01-01`) | Claridad y orientación |
| **Norma** | **Sí: `KYN-SDI-…`** | «Ubicación comprensible», cuando se apruebe como regla independiente |
| Ejemplo | No; acompaña a su norma | Formulario de registro |
| Nota técnica | No; acompaña a su norma | Tokens, valores de implementación |
| Referencia | No; cita el código de origen | `KYN-MRK-TYP-002`, `KYN-PRD-UIX-023` |

## Reglas

1. Un código emitido no cambia, no se borra ni se reutiliza.
2. Si una materia ya tiene autoridad normativa en el Libro de Marca, el Sistema de Diseño la cita por su código original (`KYN-MRK-…`) y desarrolla solo su especificación de implementación.
3. Los identificadores históricos del Manual de Producto (`KYN-PRD-…`) se conservan y se citan como antecedentes. No se declaran migrados mientras no se compare su texto.
4. Las normas se registrarían en `data/sd-normas.json`, con la misma estructura que `data/normas.json`: ruta y ancla → ID, título, número visible y estado.

## Para emitir los primeros códigos

- Aprobar el prefijo `KYN-SDI` y los códigos de módulo.
- Aprobar el texto de cada principio del capítulo 01. Los nueve principios de Principios compartidos son candidatos a norma: tres por subcapítulo.
