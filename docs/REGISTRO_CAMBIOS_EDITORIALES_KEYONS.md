# Registro de cambios editoriales · Libro de Marca Keyons

Documentación de desarrollo. No forma parte del Libro de Marca ni se enlaza desde él.

- **Corte:** 2026-11-02, rama `main`, commit `9afe693` más los ajustes de encabezados de esta sesión.
- **Punto de recuperación:** etiqueta `respaldo-2026-11-02b`.
- **Alcance de esta primera etapa:** capítulos 01 ADN, 02 Concepto, 03 Principios de diseño y 04 Voz. No se modificó ninguna redacción para preparar este registro.

## Estados

| Estado | Significado |
| --- | --- |
| Propuesta | Texto o ajuste sin aprobación expresa: recomendaciones, textos redactados por IA y propuestas de corrección que esperan revisión |
| Aprobada | Redacción exacta entregada por Keyons en una instrucción con identificador y operación |
| Implementada | La redacción está en el archivo de origen; se indica el commit |
| Validada | Keyons revisó la implementación en escritorio y móvil y la dio por buena |

- **Qué no cuenta como aprobación:** que un texto apareciera en una conversación o que una IA lo implementara.
- **El PDF documental:** es una referencia histórica; no sobrescribe el sitio.
- **Fuentes del registro:** la redacción aprobada es la de la instrucción correspondiente, identificada por su fecha y hora (UTC). Las fechas de commit son las de Git.

## Resultado de la comparación

| Resultado | Normas | Detalle |
| --- | --- | --- |
| Permanecen | Todas las instrucciones con texto exacto desde el 29-10 | Las redacciones entregadas el 30-10 y el 02-11 están en los archivos. En Git ningún texto se quitó y luego volvió a aparecer |
| Reemplazadas por una instrucción posterior | ADN-005 (30-10 → 02-11), ADN-001, ADN-006, ADN-007 (02), VOZ-002, VOZ-003, VOZ-004, VOZ-006, VOZ-007 | Los textos anteriores salieron por instrucción expresa; están en Git |
| Desaparecidas sin instrucción | Ninguna | — |
| Implementadas con ajustes no aprobados | CON-005, CON-006, CON-008, VOZ-001, VOZ-002, VOZ-004, VOZ-006, VOZ-007 | Ver «Desviaciones»: textos o rótulos redactados por IA y reformulaciones |
| No verificables | Correcciones del 29-09 al 28-10 | Son anteriores al repositorio (creado el 29-10). Solo se pueden contrastar con las instrucciones de esa etapa, que en su mayoría no traían texto exacto |
| Publicadas | Ninguna de las anteriores | El sitio publicado (libro-de-marca.keyonsia.com) sirve la versión del 29-10 (`b90f9b7`): por eso allí se ven las redacciones anteriores |

## 01 · ADN · `marca/adn.html`

| Código | Subcapítulo | Ancla | Estado actual | Operación | Redacción aprobada | Implementación | Validación visual | Commit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KYN-MRK-ADN-001 | 1.1 Esencia de marca | #esencia | Vigente | Sustituir «Cómo trabajamos», «Por qué lo hacemos» y el cierre | Instrucción 2026-11-02 16:50 | Implementada. Énfasis del cierre añadido por IA | Pendiente | `2294087` |
| KYN-MRK-ADN-002 | 1.2 Propósito de marca | #proposito | Vigente | Conservar sin cambios | Instrucción 2026-11-02 16:50 | Sin cambios desde el 29-10 | Pendiente | `c3e33d7` |
| KYN-MRK-ADN-003 | 1.2.3 Espectro de personalización | #espectro | Vigente | Conservar sin cambios | Instrucción 2026-11-02 16:50 | Sin cambios | Pendiente | `c3e33d7` |
| KYN-MRK-ADN-004 | 1.3 Origen y visión global | #origen | Vigente | Conservar sin cambios | Instrucción 2026-11-02 16:50 | Sin cambios | Pendiente | `c3e33d7` |
| KYN-MRK-ADN-005 | 1.4.1 Filosofía operativa | #filosofia | Vigente | Sustituir los dos párrafos | 2026-10-30 06:17, reemplazada por 2026-11-02 16:50 | Implementada la del 02-11. Énfasis añadido por IA | Pendiente | `8747573`, `2294087` |
| KYN-MRK-ADN-006 | 1.4.2 Propuesta de valor | #propuesta | Vigente | Sustituir introducción y cinco promesas | Instrucción 2026-11-02 16:50 | Implementada. Énfasis de la introducción añadido por IA | Pendiente | `2294087` |
| KYN-MRK-ADN-007 | 1.5 Principios de marca | #principios | Vigente | Sustituir solo el texto del principio 02 | Instrucción 2026-11-02 16:50 | Implementada en tres párrafos dentro de la celda | Pendiente. La celda queda más larga que las demás (ver composición) | `2294087` |

## 02 · Concepto · `marca/cielo.html`, `marca/metaforas.html`, `marca/composicion.html`

| Código | Subcapítulo | Ancla | Estado actual | Operación | Redacción aprobada | Implementación | Validación visual | Commit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KYN-MRK-CON-001 | 2.1 El concepto central | cielo.html#simbolo | Vigente | Sustituir solo la regla de cierre | Instrucción 2026-11-02 16:50. El cambio de título pedido el 30-10 nunca recibió texto | Implementada. Resaltado parcial añadido por IA | Pendiente | `2294087` |
| KYN-MRK-CON-002 | 2.1.1 Jerarquía de cielos | cielo.html#jerarquia | Vigente | Incorporar precisión sobre proporciones | Instrucción 2026-11-02 16:50 | Implementada con el rótulo «(Las proporciones)», puesto por IA | Pendiente | `2294087` |
| KYN-MRK-CON-003 | 2.1.2 Diario de Cielos | cielo.html#diario | Vigente | Ninguna | — | Sin cambios | Pendiente | `c3e33d7` |
| KYN-MRK-CON-004 | 2.2 Sistema de metáforas | metaforas.html#condiciones | Vigente | Revisar la explicación de presencia humana | Instrucción 2026-11-02 16:50 (texto de tres párrafos) | Implementada. El texto se repartió entre la descripción y el criterio del paso 04 | Pendiente | `2294087` |
| KYN-MRK-CON-005 | 2.2 Formalidad según canal | metaforas.html#canal | Vigente | Añadir referencia a los principios contextuales | Recomendación sin texto exacto (2026-11-02 16:50) | **Propuesta**: la frase la redactó IA | Pendiente | `2294087` |
| KYN-MRK-CON-006 | 2.3 Reglas de composición | composicion.html#reglas | Vigente | Párrafo de alcance; corregir la razón de las imágenes de banco | Párrafo de alcance: texto de Keyons, 2026-11-02 16:50. Razón de las imágenes de banco: recomendación | Alcance implementado. Razón de las imágenes de banco: **propuesta adaptada por IA**. Título «Cielo propio» (30-10) implementado | Pendiente | `8747573`, `2294087` |
| KYN-MRK-CON-007 | 2.4 Regla del contraste | composicion.html#contraste | Vigente | Ninguna | — | Sin cambios | Pendiente | `c3e33d7` |
| KYN-MRK-CON-008 | 2.5 Anti-referentes | composicion.html#anti | Vigente | Cambiar el criterio de imágenes «lisas» | Instrucción 2026-11-02 16:50 («Lo que evitamos», «En Keyons» y la nota) | Implementada. El rótulo «Lo hecho sin autor» es **propuesta de IA**. El espaciado pedido el 30-10 sigue aplicado | Pendiente | `2294087` |
| KYN-MRK-CON-009 | 2.6 Herencia estética | composicion.html#herencia | Vigente | Ninguna | — | Sin cambios | Pendiente | `c3e33d7` |

## 03 · Principios de diseño · `marca/principios.html`

| Código | Subcapítulo | Ancla | Estado actual | Operación | Redacción aprobada | Implementación | Validación visual | Commit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KYN-MRK-DIS-001 | 3.1 Identidad y criterio | #criterio | Vigente | Sustituir la entrada | Instrucción 2026-10-30 06:17 | Implementada | Pendiente | `8747573` |
| KYN-MRK-DIS-002 | 3.2 Roles definidos | #capas | Vigente | Nuevo título; agregar «Productos con estética predeterminada»; sustituir «Marca exclusiva del cliente» | Título: 2026-10-30 06:17. Textos: 2026-11-02 16:50 | Implementada. La nota que remitía a las cuatro capas salió al eliminarse Interfaces | Pendiente | `8747573`, `2294087`, `9bcaf2d` |
| KYN-MRK-DIS-003 | 3.3 Calma y expresión | #calma | Vigente | Nuevo título; quitar imágenes; sustituir explicaciones y cierre | Título: 2026-10-30 06:17. Sin imágenes: 2026-10-30 15:47. Textos: 2026-11-02 16:50 | Implementada. Resaltado del cierre añadido por IA | Pendiente. Texto visible de 50 a 185 palabras | `8747573`, `f29d231`, `2294087` |
| KYN-MRK-DIS-004 | 3.4 Según contexto | #contexto | Vigente | Nuevo título y entrada; agregar «Dentro de una misma experiencia» | 2026-10-30 06:17 y 2026-11-02 16:50 | Implementada | Pendiente | `8747573`, `2294087` |
| KYN-MRK-DIS-005 | 3.5 Claridad primero | #comprension | Vigente | Nuevo título; ilustración; agregar «Claridad ante las dificultades» | 2026-10-30 06:17, 15:47 y 2026-11-02 16:50 | Implementada | Pendiente | `8747573`, `f29d231`, `2294087` |
| KYN-MRK-DIS-006 | 3.6 Calidad sin firma visible | (sin sección) | Descontinuada | Quitar de Principios | Instrucción 2026-10-30 06:17 | ID reservado; texto en Git | — | `8747573` |

## 04 · Voz · `marca/voz.html`, `marca/vocabulario.html`, `marca/trato.html`

La instrucción del 2026-11-02 se entregó como «propuesta de corrección para revisión y aprobación antes de implementarla en producción». Está implementada en local, sin publicar, y su estado es **Propuesta** hasta que se apruebe.

| Código | Subcapítulo | Ancla | Estado actual | Operación | Redacción aprobada | Implementación | Validación visual | Commit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KYN-MRK-VOZ-001 | 4.1 Esencia de la voz | voz.html#modos | Vigente | Incorporar «La voz según su aplicación» | Propuesta 2026-11-02 16:50 | Implementada. Los cuatro rótulos «(Canales de Keyons)», «(Interfaces de Keyons)», «(Marcas de clientes)» y «(Estela)» son **IA** | Pendiente | `2294087` |
| KYN-MRK-VOZ-002 | 4.2 Reglas de escritura | voz.html#reglas | Vigente | Nuevo título, entrada, cuatro principios, consistencia y cierre | Propuesta 2026-11-02 16:50 | Implementada. Los tres rótulos de «Criterio de consistencia» son **IA** | Pendiente. Texto visible de 186 a 397 palabras | `2294087` |
| KYN-MRK-VOZ-003 | 4.3 Vocabulario propio | vocabulario.html#propio | Vigente | Entrada y tres definiciones | Propuesta 2026-11-02 16:50 | Implementada | Pendiente | `2294087` |
| KYN-MRK-VOZ-004 | 4.4 Vocabulario que evitamos | vocabulario.html#evita | Vigente | Entrada, tres alternativas y criterio final | Propuesta 2026-11-02 16:50. «Nos apasiona» se quitó por instrucción del 30-10 | Implementada con **reformulación de IA**: las tres alternativas pasaron a infinitivo y una frase cambió | Pendiente | `8747573`, `2294087` |
| KYN-MRK-VOZ-005 | 4.5 El trato | trato.html#usted | Vigente | Sustituir la excepción de Estela; agregar marcas de clientes e inglés | Propuesta 2026-11-02 16:50 | Implementada | Pendiente | `2294087` |
| KYN-MRK-VOZ-006 | 4.6 Primera o tercera persona | trato.html#persona | Vigente | Nuevo título y texto principal; ejemplos; consistencia | Propuesta 2026-11-02 16:50 | Implementada con **notas cortas redactadas por IA** en el ejemplo; el texto completo pasó a las listas | Pendiente. Texto visible de 112 a 276 palabras | `2294087` |
| KYN-MRK-VOZ-007 | 4.7 De lo técnico a lo humano | trato.html#traduccion | Vigente | Entrada, cuatro principios, nueve entradas del glosario y relación con productos | Propuesta 2026-11-02 16:50 | Implementada. Los tres rótulos de «Relación con la comunicación de productos» son **IA** | Pendiente | `2294087` |

## Desviaciones respecto del texto exacto

Ninguna se ha corregido todavía: esperan la decisión de Keyons.

| Código | Qué se implementó | Texto entregado |
| --- | --- | --- |
| CON-005 | «El canal no es el único criterio: también importa lo que la persona necesita comprender o hacer al recibir la pieza. El principio general está en KYN-MRK-DIS-004, Intensidad según contexto.» | Ninguno: solo la recomendación de añadir una referencia |
| CON-006 | «Nunca imágenes de banco genéricas: Keyons prioriza imágenes con procedencia, dirección artística y una relación auténtica con su narrativa.» | Recomendación: «La razón profesional sería que Keyons prioriza imágenes con procedencia, dirección artística y una relación auténtica con su narrativa» |
| CON-008 | Rótulo «Lo hecho sin autor» | El rótulo anterior era «Lo hecho por IA, sin autor»; el cambio no se pidió |
| VOZ-004 | «Explicar qué servicios…», «Indicar qué puede adaptarse… En productos SaaS, diferenciar…», «Presentar beneficios previstos… Las proyecciones se identifican como estimaciones, no como garantías.» | «Explicamos qué servicios…», «Indicamos qué puede adaptarse… En productos SaaS diferenciamos…», «Presentamos beneficios previstos… Las proyecciones deben identificarse como estimaciones y no como garantías.» |
| VOZ-006 | Notas del ejemplo: «Keyons se presenta como entidad.» y «La empresa habla directamente con su público.» | Las notas son resúmenes de IA; el texto entregado está completo en las listas «dónde» |
| VOZ-001, VOZ-002, VOZ-007, CON-002 | Rótulos entre paréntesis para cada bloque nuevo | Los textos entregados no traían esos rótulos |
| ADN-001, ADN-005, ADN-006, CON-001, DIS-003 y entradas de Voz | Negritas y resaltado celeste | Los textos se entregaron sin énfasis; la diagramación los añadió |

## Composición

| Código | Problema | Alternativa propuesta (sin aprobar) |
| --- | --- | --- |
| ADN-007 | El principio 02 tiene tres párrafos entre seis de una o dos frases | `propuestas/editorial/`, caso 04 |
| DIS-003 | De 50 a 185 palabras visibles | `propuestas/editorial/`, caso 01 |
| VOZ-002 | De 186 a 397 palabras visibles | `propuestas/editorial/`, caso 02 |
| VOZ-006 | De 112 a 276 palabras visibles | `propuestas/editorial/`, caso 03 |

La propuesta editorial pliega texto en «Norma completa». Las nuevas reglas de este registro piden no convertir explicaciones en desplegables de forma automática, así que se mantiene como propuesta para revisar norma por norma.

## Pendientes de decisión

1. **Aprobación de Voz:** aprobar o corregir la propuesta de Voz del 2026-11-02 (VOZ-001 a 007).
2. **Desviaciones:** conservar o revertir cada desviación de la tabla anterior.
3. **CON-006:** la prohibición absoluta de crear imágenes con IA desde cero no se ha cambiado y requiere aprobación específica. El título «Cuatro reglas sin excepción» contradice el nuevo párrafo de alcance.
4. **Correcciones del 29-09 al 28-10:** si un párrafo de esa etapa debería decir otra cosa, entregar la redacción exacta para registrarla y aplicarla.

## Cómo se mantiene este registro

1. **Una instrucción por cambio.** Cada instrucción editorial indica ID, ubicación, operación y texto exacto. Se aplica solo eso.
2. **Después de aplicar:**
   - `python tools/verificar.py --aprobar "ID · instrucción AAAA-MM-DD"` registra la nueva redacción en `data/referencia-contenido.json`;
   - la fila de este registro se actualiza con el commit.
3. **Antes de cada commit** corre `tools/verificar.py`. Detiene el commit si una norma falta o vuelve a una redacción anterior a la aprobada.
4. **Validación:** pasa a «Validada» solo cuando Keyons revisa la página en escritorio y móvil.
