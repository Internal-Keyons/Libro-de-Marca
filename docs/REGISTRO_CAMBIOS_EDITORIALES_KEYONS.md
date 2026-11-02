# Registro de cambios editoriales · Libro de Marca Keyons

Documentación de desarrollo. No forma parte del Libro de Marca ni se enlaza desde él.

- **Última intervención:** «Revisión editorial consolidada — Marca, capítulos 01–04», 2026-11-02, commit `1002216` en `main`.
- **Puntos de recuperación:**
  - `respaldo-2026-11-02c`: estado anterior a esta revisión, en el commit `5762edc`;
  - `respaldo-2026-11-02b`: estado anterior al registro.
- **Alcance:** capítulos 01 ADN, 02 Concepto, 03 Principios de diseño y 04 Voz.

## Estados

| Estado | Significado |
| --- | --- |
| Propuesta | Texto o ajuste sin aprobación expresa: recomendaciones, textos redactados por IA y propuestas de corrección que esperan revisión |
| Aprobada | Redacción exacta entregada por Keyons en una instrucción con identificador y operación |
| Implementada | La redacción está en el archivo de origen; se indica el commit |
| Validada | Keyons revisó la implementación en escritorio y móvil y la dio por buena |

- **Qué no cuenta como aprobación:** que un texto apareciera en una conversación o que una IA lo implementara.
- **El PDF documental:** es una referencia histórica; no sobrescribe el sitio.
- **Fuente de cada redacción:** la redacción aprobada es la de la instrucción correspondiente. La revisión consolidada del 2026-11-02 se identifica como «RC 02-11».

## Resultado de la revisión consolidada

| Resultado | Normas |
| --- | --- |
| Sustituidas con el texto exacto de RC 02-11 | ADN-001, 005, 006, 007 · CON-001, 002, 003, 004, 006, 008 · DIS-002, 003, 004, 005 · VOZ-001 a 007 (21 normas) |
| Conservadas sin cambios | ADN-002, 003, 004 · CON-005, 007, 009 · DIS-001 |
| Numeración visible corregida | CON-005 pasa de 2.2 a 2.2.1: ya no repite el número de CON-004. Los ID no cambian |
| Publicadas | Ninguna. El sitio publicado sigue en la versión del 29-10 (`b90f9b7`) |

## 01 · ADN · `marca/adn.html`

| Código | Subcapítulo | Ancla | Estado actual | Operación | Redacción aprobada | Implementación | Validación visual | Commit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KYN-MRK-ADN-001 | 1.1 Esencia de marca | #esencia | Vigente | Sustituir título, declaración y dos apartados | RC 02-11 | Implementada. Sale el cierre anterior: su idea quedó en «Por qué lo hacemos» | Pendiente | `1002216` |
| KYN-MRK-ADN-002 | 1.2 Propósito de marca | #proposito | Vigente | Conservar | — | Sin cambios | Pendiente | `c3e33d7` |
| KYN-MRK-ADN-003 | 1.2.3 Espectro de personalización | #espectro | Vigente | Conservar | — | Sin cambios | Pendiente | `c3e33d7` |
| KYN-MRK-ADN-004 | 1.3 Origen y visión global | #origen | Vigente | Conservar | — | Sin cambios | Pendiente | `c3e33d7` |
| KYN-MRK-ADN-005 | 1.4.1 Filosofía operativa | #filosofia | Vigente | Dos párrafos pasan a uno | RC 02-11 | Implementada | Pendiente | `1002216` |
| KYN-MRK-ADN-006 | 1.4.2 Propuesta de valor | #propuesta | Vigente | Sustituir introducción y cinco promesas | RC 02-11 | Implementada; la promesa 02 se titula «Damos claridad para decidir» | Pendiente | `1002216` |
| KYN-MRK-ADN-007 | 1.5 Principios de marca | #principios | Vigente | Sustituir solo el principio 02 | RC 02-11 | Implementada en un párrafo | Pendiente | `1002216` |

## 02 · Concepto · `marca/cielo.html`, `marca/metaforas.html`, `marca/composicion.html`

| Código | Subcapítulo | Ancla | Estado actual | Operación | Redacción aprobada | Implementación | Validación visual | Commit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KYN-MRK-CON-001 | 2.1 El concepto central | cielo.html#simbolo | Vigente | Sustituir texto de apertura y regla de cierre | RC 02-11 | Implementada. El segundo párrafo del cierre va como texto de apoyo | Pendiente | `1002216` |
| KYN-MRK-CON-002 | 2.1.1 Jerarquía de cielos | cielo.html#jerarquia | Vigente | Una precisión después del texto introductorio | RC 02-11 | Implementada como texto de apoyo. Sale el bloque «(Las proporciones)» porque repetía la idea | Pendiente | `1002216` |
| KYN-MRK-CON-003 | 2.1.2 Diario de Cielos | cielo.html#diario | Vigente | Agregar párrafo al final de «Firma humana» | RC 02-11 | Implementada | Pendiente | `1002216` |
| KYN-MRK-CON-004 | 2.2 Sistema de metáforas | metaforas.html#condiciones | Vigente | Criterios de 01 y 04 | RC 02-11 | Implementada. En 04, el primer párrafo es la explicación y el segundo el criterio | Pendiente | `1002216` |
| KYN-MRK-CON-005 | 2.2.1 Formalidad según canal | metaforas.html#canal | Vigente | Conservar; corregir numeración | RC 02-11 | Numeración corregida. Se conserva la nota redactada por IA (ver «Pendientes») | Pendiente | `1002216` |
| KYN-MRK-CON-006 | 2.3 Reglas de composición | composicion.html#reglas | Vigente | Revisión de la norma: introducción, cuatro criterios, cierre y condiciones de aplicación | Revisión CON-006, 2026-11-02 (RV 02-11) | Implementada. Criterio 02 nuevo: «Dirección humana, creación sin límites de herramienta». Las condiciones de aplicación van plegadas bajo el cierre | Pendiente | `8eaee97` |
| KYN-MRK-CON-007 | 2.4 Regla del contraste | composicion.html#contraste | Vigente | Conservar | — | Sin cambios | Pendiente | `c3e33d7` |
| KYN-MRK-CON-008 | 2.5 Anti-referentes | composicion.html#anti | Vigente | Sustituir la última comparación | RC 02-11 | Implementada. La nota final sustituye a la anterior sobre texturas | Pendiente | `1002216` |
| KYN-MRK-CON-009 | 2.6 Herencia estética | composicion.html#herencia | Vigente | Conservar | — | Sin cambios | Pendiente | `c3e33d7` |

## 03 · Principios de diseño · `marca/principios.html`

| Código | Subcapítulo | Ancla | Estado actual | Operación | Redacción aprobada | Implementación | Validación visual | Commit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KYN-MRK-DIS-001 | 3.1 Identidad y criterio | #criterio | Vigente | Conservar | — | Sin cambios | Pendiente | `8747573` |
| KYN-MRK-DIS-002 | 3.2 Roles definidos | #capas | Vigente | Sustituir «Marca exclusiva del cliente»; una precisión «Estética predeterminada» | RC 02-11 | Implementada. Sale «(Productos con estética predeterminada)», reemplazado por la nueva precisión | Pendiente | `1002216` |
| KYN-MRK-DIS-003 | 3.3 Calma y expresión | #calma | Vigente | Nueva diagramación, mismos textos | RC 02-11; diagramación RV 02-11 | Implementada. Dos conceptos con nombre y descripción, filete Azul Noche y sin divisor vertical; se apilan por debajo de 1200 px con barra lateral y en móvil | Pendiente | `de4d992`, `8eaee97` |
| KYN-MRK-DIS-004 | 3.4 Según contexto | #contexto | Vigente | Una precisión después de «Una herramienta operativa» | RC 02-11 | Implementada con el rótulo existente «(Dentro de una misma experiencia)» | Pendiente | `1002216` |
| KYN-MRK-DIS-005 | 3.5 Claridad primero | #comprension | Vigente | Una precisión al cierre | RC 02-11 | Implementada como texto de apoyo. Sale «(Claridad ante las dificultades)», de tres párrafos | Pendiente | `1002216` |
| KYN-MRK-DIS-006 | 3.6 Calidad sin firma visible | (sin sección) | Descontinuada | — | — | ID reservado; texto en Git | — | `8747573` |

## 04 · Voz · `marca/voz.html`, `marca/vocabulario.html`, `marca/trato.html`

La revisión consolidada reemplaza la propuesta de Voz del 2026-11-02 16:50.

| Código | Subcapítulo | Ancla | Estado actual | Operación | Redacción aprobada | Implementación | Validación visual | Commit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KYN-MRK-VOZ-001 | 4.1 Esencia de la voz | voz.html#modos | Vigente | Una única precisión | RC 02-11 | Implementada como texto de apoyo después del cierre. Sale «La voz según su aplicación» | Pendiente | `1002216` |
| KYN-MRK-VOZ-002 | 4.2 Reglas de escritura | voz.html#reglas | Vigente | Mejorar explicaciones y dos ejemplos «En Keyons» | RC 02-11; textos RV 02-11 | Implementada. En 01 se conserva el título «Afirmar antes que negar» (ver Pendientes). Los ejemplos «Antes» no cambian | Pendiente | `8eaee97` |
| KYN-MRK-VOZ-003 | 4.3 Vocabulario propio | vocabulario.html#propio | Vigente | Introducción y tres definiciones | RC 02-11 | Implementada | Pendiente | `1002216` |
| KYN-MRK-VOZ-004 | 4.4 Vocabulario que evitamos | vocabulario.html#evita | Vigente | Sustituir texto principal | RV 02-11 | Implementada | Pendiente | `8eaee97` |
| KYN-MRK-VOZ-005 | 4.5 El trato | trato.html#usted | Vigente | Excepción de Estela; precisión sobre productos de clientes | RC 02-11 | Implementada. La precisión reemplaza el bloque anterior de clientes, con su rótulo | Pendiente | `1002216` |
| KYN-MRK-VOZ-006 | 4.6 Primera o tercera persona | trato.html#persona | Vigente | Aligerar la composición | RC 02-11; diagramación RV 02-11 | Implementada. Las definiciones aprobadas de tercera y primera persona pasan a las notas del ejemplo y salen los dos bloques que las repetían. Queda «Consistencia» | Pendiente | `8eaee97` |
| KYN-MRK-VOZ-007 | 4.7 De lo técnico a lo humano | trato.html#traduccion | Vigente | Introducción, cuatro principios y diez definiciones | RC 02-11 | Implementada. «Context window» ya coincidía | Pendiente | `1002216` |

## Decisiones de presentación tomadas al implementar

| Norma | Decisión |
| --- | --- |
| CON-001, CON-002, DIS-003, DIS-005, VOZ-001, VOZ-006, VOZ-007 | El párrafo secundario usa el estilo de apoyo (`ed__more`, 16 px), no el de la declaración. Así la declaración conserva su protagonismo |
| CON-008 | La columna «En Keyons» de la última fila lleva título y descripción. Se agregó una regla local en `css/libro.css`: título en semibold, descripción en peso normal |
| DIS-003 | Entre 1001 y 1199 px, con barra lateral, cada columna quedaba en unos 190 px; ahí se apilan, como en móvil. En escritorio siguen en dos columnas |
| VOZ-007 | No se agregó el subtítulo «Cuatro principios»: repetía lo que ya muestra la rejilla numerada |

## Desviaciones que siguen abiertas

| Código | Qué hay | Por qué sigue |
| --- | --- | --- |
| CON-005 | Nota redactada por IA: «El canal no es el único criterio… KYN-MRK-DIS-004, Intensidad según contexto.» | La instrucción dice «Conservar íntegramente» y también «No agregar explicaciones» |
| VOZ-007 | Bloque «Relación con la comunicación de productos», con rótulos de IA | La instrucción no lo menciona |
| VOZ-005 | Bloque «(Aplicación en inglés)», de la propuesta del 02-11 | La instrucción no lo menciona |

Desviaciones cerradas: VOZ-006 (las notas del ejemplo ahora son las definiciones aprobadas), CON-002, CON-006, CON-008, VOZ-001, VOZ-002 y VOZ-004 (rótulos y reformulaciones de IA). También se quitaron las negritas que la IA había añadido en ADN-001, 005 y 006, CON-001 y en las entradas de Voz.

## Pendientes de decisión

1. **Contradicción con ILU-007:** «Patrones y texturas» (`fundamentos/elementos/graficos.html#patrones`) dice que las texturas se producen «nunca generadas por IA desde cero». CON-006 ahora lo permite. No se modificó, por instrucción de no tocar otras normas.
1. **VOZ-002, principio 01:** el texto entregado empieza con «Preferimos explicar qué hacemos y qué proponemos» sin título. Se conservó el título «Afirmar antes que negar» y esa frase abre la explicación. Confirmar.
2. **Desviaciones abiertas:** conservar o quitar cada una de la tabla anterior.
3. **Validación visual:** revisar las 21 normas en escritorio y móvil para pasarlas a «Validada».
4. **Propuesta editorial** (`propuestas/editorial/`): casos 01 a 04 superados por esta revisión; queda como referencia.

## Revisión del 2026-11-02 (RV 02-11)

- **Textos:** CON-006, VOZ-002 y VOZ-004.
- **Diagramación:** DIS-003 y VOZ-006.
- **Interfaz:** menos tracking en los rótulos en mayúsculas del menú lateral (área y subgrupos).
- **Sin cambios:** ADN-001, ADN-006, CON-001, CON-002, VOZ-001 y el resto de VOZ-002 coincidían ya con el texto reenviado.

## Cómo se mantiene este registro

1. **Una instrucción por cambio.** Cada instrucción editorial indica ID, ubicación, operación y texto exacto. Se aplica solo eso.
2. **Después de aplicar:**
   - `python tools/verificar.py --aprobar "ID · instrucción AAAA-MM-DD"` registra la nueva redacción en `data/referencia-contenido.json`;
   - la fila de este registro se actualiza con el commit.
3. **Antes de cada commit** corre `tools/verificar.py`. Detiene el commit si una norma falta o vuelve a una redacción anterior a la aprobada.
4. **Validación:** pasa a «Validada» solo cuando Keyons revisa la página en escritorio y móvil.
