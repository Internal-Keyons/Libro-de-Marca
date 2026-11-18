# Revisión editorial, funcional y normativa del Sistema de Diseño · Fase A

2026-11-18 · rama `biblioteca-p1-p4` · todo en borrador · sin publicar en `main` y sin exportaciones (PDF o Markdown).

**Entregables de esta fase**

| Entregable | Archivo |
| --- | --- |
| Este informe | `propuestas/sd-entregas/revision-editorial.md` |
| Inventario de lo construido | `propuestas/sd-entregas/inventario-sistema.md`. Versión inicial antes de corregir; al final, qué cambió |
| Decisiones pendientes | `propuestas/sd-entregas/decisiones-pendientes.md`. Acción principal, foco, 44 px, duplicaciones, cambios de redacción, verificaciones con cambio de significado, `CLAUDE.md` y el texto literal de las 9 normas redactadas por Claude |
| Capturas | `propuestas/capturas-sd-revision/`. Ocho pares de antes y después a 1440 px, y hojas de escritorio y de móvil de los capítulos 01, 05 y 06 |

**Fuentes de referencia**
- Las imágenes 1 a 21 se revisaron.
- Los cuatro PDF se leyeron.
- De los tres videos solo pude ver los títulos: «Intro to variables», «Variables for typography» y «Prototype with variables». Su contenido no está en este trabajo.

---

## 1 · Capturas de antes y después

| N.º | Imagen de Keylin | Captura | Qué cambió |
| --- | --- | --- | --- |
| 1 | Validación del capítulo 01 | `01-validacion-del-capitulo.jpg` | El rótulo de cada prueba queda sin enlace. La columna «Qué se espera» empieza con mayúscula. Una norma con dos o más pruebas suma el rótulo de cada una («Control de la persona · Reversión»). PEX-017 suma la prueba «Fallo» |
| 2 | PEX-017 | `02-pex-017-cancelar-deshacer-decidir.jpg` | La tabla «Salida según la operación» muestra qué se ofrece antes y después de confirmar en cuatro tipos de operación. Se agregan la aprobación de la persona, qué pasa cuando la operación falla y por qué el mecanismo cambia. Quedan dos enlaces: Recuperación e IA pasan al registro como relación |
| 3 | PEX-004 | `03-pex-004-estado-de-cada-accion.jpg` | El requisito y la tabla quedan a 32 px, sin doble línea. La columna «Dónde se desarrolla» conserva sus enlaces porque existe para eso (aviso justificado) |
| 4 | PEX-001 | `04-pex-001-proposito-y-prioridad.jpg` | El requisito y su decisión van en el mismo color de lectura. El plegable y la nota de verificación comparten una línea |
| 5 | ARQ-002 | `05-arq-002-nombres-reconocibles.jpg` | Filas con criterios concretos: vocabulario de los perfiles, etiqueta de menú frente a título de página, siglas y un concepto con un solo nombre. Se suma la prueba «Tarea real» |
| 6 | ARQ-005 | `06-arq-005-ubicacion-y-seccion-activa.jpg` | «Según el tipo de navegación» pasa de plegable a filas visibles. «Pantallas sin navegación general» se integra como una fila. Quedan plegados solo el foco (técnico) y la verificación, sin doble línea |
| 7 | ARQ-006 | `07-arq-006-acciones-previsibles.jpg` | Separa significado (siempre), tipo de control (siempre) e interacción (puede variar). El ejemplo de «Exportar» se corrigió: siempre entrega un archivo, y el mecanismo cambia con el tamaño del listado |
| 8 | ARQ-012 | `08-arq-012-campos-coincidencias-orden.jpg` | Titular nuevo: «Campos, coincidencias y orden de la búsqueda». La entrada es funcional. Se agregan campos consultables según la tarea y los permisos, coincidencias, tildes e identificadores, un orden configurable por producto y la diferencia entre buscar, filtrar y ordenar |

**Móvil.** Las hojas `hoja-*-movil.jpg` muestran los capítulos 01, 05 y 06 a 375 px. Las tablas conservan sus dos columnas y las filas se apilan.

## 2 · Comparación con las cinco referencias del Libro de Marca

| Referencia | Criterio que aporta | Cómo se aplicó en el Sistema de Diseño |
| --- | --- | --- |
| 9 · ADN-001 Esencia | Filas con rótulo y párrafo en un solo color de lectura y separaciones parejas | Las filas normativas pasan al color principal y quedan a 32 px del requisito, con una sola línea |
| 10 · ADN-003 Personalización | Una tabla que compara de verdad dos columnas, con rótulos de fila breves | PEX-017 usa una tabla «antes y después de confirmar», porque compara lo mismo en cuatro casos |
| 11 · ADN-007 Siete principios | Retícula con número solo donde hay enumeración | Se mantiene: el Sistema de Diseño no agrega retículas por variedad |
| 12 · ADN-006 Cinco promesas | Acordeón para ítems equivalentes, sin número | Los plegables quedan solo para contenido complementario (foco, notas técnicas, verificación larga). El contenido para aplicar la norma queda visible (ARQ-005) |
| 13 · CON-004 Cinco condiciones | Criterio junto a cada ítem, sin repetir el enunciado | Las dimensiones integradas (PEX-001, ARQ-006) ponen el requisito y su decisión en la misma fila, sin repetirlos |

El Sistema de Diseño conserva lo que el Libro de Marca usa menos: tablas de estados, notas técnicas y validación agrupada. Los dos libros comparten tipografía, color de lectura, líneas y proximidad.

## 3 · Enlaces

| Medida | Antes | Después |
| --- | --- | --- |
| Enlaces visibles dentro de las 151 normas | 183 | 155 |
| Enlaces en las secciones «Validación del capítulo» | 31 | 2. Los dos están en la entrada del texto, no en la tabla, y llevan a especificaciones útiles (44 Validación y 24 Mensajes) |
| Dependencias en el registro (`relaciones` de `data/sd-normas.json`) | — | 114, en 73 normas |

**Fuente única de las dependencias.**
- Las dependencias se escriben solo en los módulos `tools/sd/m*.py`: las referencias `R()` del texto, más `rel=[…]` para las que salieron de la página.
- `tools/sd_capitulos.py` las copia al registro y se detiene si una relación no tiene destino.
- `tools/sd_revisar.py` lo vuelve a comprobar.

**Eliminados de la página y conservados como relación**

| Norma | Enlace que salió | Motivo |
| --- | --- | --- |
| Validación de los capítulos 01, 06, 13, 16, 17, 25, 29 y 31 | Rótulo de cada prueba | Repetía el nombre de una norma de la misma página |
| PEX-001 | Diseño por tarea | La fila ya dice la decisión: «primero lo que exige una decisión del día» |
| PEX-003 | Menú de acciones (en el ejemplo) | El ejemplo se entiende solo |
| PEX-005 | Decisiones justificadas (en la verificación) | El resultado ya es observable sin abrir otra norma |
| PEX-007 | 20, 21 y 22 (tres enlaces) | Quedó uno solo: «los capítulos 20 a 22 de Accesibilidad» |
| PEX-017 | Reversibilidad · Control humano | Ahora la norma explica el principio. Recuperación e IA quedan como relación |
| ARQ-002 | Consistencia | El criterio está escrito en la fila |
| ARQ-005 | 08 Color funcional · 14 Estructura · Adaptación | La fila describe la señal; el foco del diálogo ya está explicado |
| ARQ-006 | Nombres comprensibles | La decisión está escrita en la fila |
| ARQ-012 | Resultados autorizados | La fila «Campos consultables» ya incluye los permisos |
| FUI-002 | 38 White-label | Remitía a algo pendiente |
| FUI-014 | Densidad y ayudas (dos enlaces en una oración) | Queda uno, al Libro de Marca |
| CPE-001 | 05 Navegación | La oración ya explica botón y enlace |
| PAT-011 | 01 Principios comunes | Se escribió qué se muestra antes de ejecutar |
| DAV-007 | Cuatro enlaces iguales a «Tipos de gráfico» | Queda uno solo, en una fila propia |
| SPR-001 | Cinco enlaces a capítulos | Los nombres de los capítulos quedan como texto. Se conserva «Navegación predeterminada», de la misma página |
| SPR-009 | Cuatro enlaces a capítulos | El texto nombra los capítulos |

**Reubicados con una oración que explica la decisión** (el enlace queda, pero ya no es lo único de la fila):
- CPE-012 Redacción
- PAT-001 Confirmar
- PAT-003 Momento
- PAT-006 Eliminar
- SPR-008 Navegación
- SPR-011 Roles
- SPR-012 Límites

**Se conservan.** Los que llevan a una especificación necesaria para implementar, por ejemplo:
- Jerarquía de acciones (PEX-001);
- Acciones destructivas (PEX-017);
- el patrón de pestañas (ARQ-005);
- el cuadro combinado (ARQ-012);
- las columnas «Dónde se desarrolla» (PEX-004) y «Libro de Marca» (FUI-004).

Los estados aprobados de los enlaces (R06) no cambiaron.

## 4 · Normas cuyo contenido funcional mejoró

El texto completo anterior y el nuevo, en las mismas cinco normas, está en el anexo A.

| Norma | Antes | Después |
| --- | --- | --- |
| PEX-017 | Tres filas generales y dos enlaces | Tabla de salidas para cuatro tipos de operación, más la aprobación de la persona, qué pasa cuando la operación falla y por qué el mecanismo cambia. Tres pruebas |
| ARQ-002 | Tres filas breves | Cuatro criterios concretos y dos pruebas, una con tareas reales |
| ARQ-005 | Tres plegables seguidos más la verificación | Filas visibles por tipo de navegación. Pliegan solo el foco y la verificación |
| ARQ-006 | Un ejemplo que hacía obligatorio el mismo diálogo | Significado, control e interacción distinguidos, y el ejemplo corregido |
| ARQ-012 | Orden fijo («primero exactas») y una entrada interpretativa | Criterios configurables por producto y una entrada funcional |

**Otros seis resultados de verificación** se reescribieron para que describan un hecho observable: PEX-001, SPR-002, CPE-009, CNT-003, IAE-007 y MOV-004. Están en `decisiones-pendientes.md`, sección 6.

## 5 · Diagramación corregida en los generadores

| Problema | Causa | Corrección |
| --- | --- | --- |
| Requisito y decisión en dos tonos | `dims()` marcaba el requisito con su propio color y `.ed__stack p` iba en gris de lectura | `dims()` usa las filas comunes. En el Sistema de Diseño, las filas y la prosa van en `--color-text` (`css/sistema-diseno.css`). Los rótulos, las entradas y las notas conservan el gris. El Libro de Marca no cambia |
| Unos 114 px y dos líneas entre el requisito y sus filas | `.ed__stack` sumaba su margen de bloque (`--s16`) a la línea inferior de `.sdn` | `.sdn + .ed__stack`: sin margen, con una sola línea y el relleno de fila (`--s8`) |
| El requisito y su tabla, separados como dos bloques | `.matrix{margin-top:--s16}` más la línea de `.sdn` | `.sdn + .matrix`: `--s8`, con una sola línea (la fuerte de la tabla) |
| Dos líneas a 40 px entre las filas y un plegable, entre dos plegables, y entre un plegable y la verificación | Cada bloque traía su margen y su línea | Una sola línea, con las reglas de proximidad de `css/libro.css`. Cada `details` y `summary` sigue intacto |
| Plegables por costumbre | `detalle()` se usaba para contenido necesario | ARQ-005 pasa a filas visibles. Las normas con tres plegables (ARQ-008 y ARQ-009) son técnicas y se conservan |
| Enlaces en la validación | `validacion()` ponía un enlace por fila | Rótulo sin enlace |
| Resultado en minúscula dentro de la tabla | El resultado se escribe como continuación de «Resultado esperado:» | `may()` pone la mayúscula solo en la celda |
| Nombres de elementos HTML como texto | CPE-008 escribía «details y summary» | Ahora van como código |

**Lo que no cambió:**
- **Separaciones globales:** ninguna nueva. Cada corrección es una secuencia concreta de bloques que hoy solo aparece en el Sistema de Diseño; se verificó que no existe en los otros libros.
- **Tokens:** ninguno nuevo.
- **Valores de CSS:** ningún valor suelto.

**Reglas publicadas en la Guía 05** (sin códigos nuevos; textos suyos, con los ajustes de la sección 5 de decisiones):
- en «Composición normativa según el contenido»: Referencias, Color del texto, y Celdas y resultados;
- en «Sistema de diagramación»: Proximidad, y Visible o plegable.

## 6 · Decisiones pendientes

Todas están en `decisiones-pendientes.md`:
1. Tokens de la acción principal. La regla 1.6 ya separa producto (Cielo) y marca (Salmón); el kit del Laboratorio la contradice.
2. Foco: Azul Noche en el tema claro y Blanco sobre Noche. Las seis excepciones en Cielo tienen 2,56:1.
3. Tamaño táctil: 44 × 44 px como preferencia, frente al mínimo AA de 24 × 24 px.
4. Fuentes principales para CPE-006 / PAT-003 y FUI-010 / ACC-003.
5. Las nueve normas con requisito redactado por Claude, con su texto literal.
6. Los cambios de significado en las verificaciones.
7. Las dos líneas de `CLAUDE.md`.

## 7 · Cobertura de las 151 normas

| Estado | Normas |
| --- | --- |
| Desarrolladas | 77 |
| Parciales | 46 |
| Pendientes | 14 |
| Requieren aprobación | 14 |

**Ningún capítulo está terminado.**
- Las normas reescritas (PEX-017, ARQ-002, ARQ-005, ARQ-006 y ARQ-012) ganaron contenido. Solo PEX-017 sigue en «requiere aprobación», porque su requisito lo redacté yo.
- Las otras cuatro cuentan como desarrolladas.

**Verificaciones por forma de presentación:**

| Forma | Normas |
| --- | --- |
| Nota breve | 73 |
| Validación del capítulo | 46 |
| Plegable técnico | 29 |
| Referencia | 3 |

El detalle por norma está en el anexo B.

## 8 · Archivos modificados y verificaciones

**Archivos**
- **Guía 05:** `data/gobierno.json`. `guia/index.html` e `ia/gobierno.json` los genera `tools/gobierno.py`.
- **Generadores:**
  - `tools/sd/base.py`: `dims`, `validacion`, `may` y `rel`;
  - `tools/sd_capitulos.py`: relaciones al registro;
  - `tools/sd_revisar.py`: controles nuevos.
- **Módulos:** `m01`, `m02`, `m02b`, `m03`, `m03b`, `m04`, `m05`, `m07`, `m09`, `m10` y `m10b` (contenido, enlaces y relaciones).
- **Estilos:**
  - `css/sistema-diseno.css`: color de lectura y proximidad del requisito;
  - `css/libro.css`: proximidad de filas, plegables y nota.
- **Justificaciones:** `tools/sd/revision-justificada.json` (dos avisos de enlaces justificados).
- **Generados:** `data/sd-normas.json`, `data/sd-capitulos/*.html`, `data/sistema-diseno.json`, `docs/niveles/niveles.json`, las páginas `sistema-diseno/**` y `propuestas/matriz-normativa-sd-01-06.md`.
- **Entregas:** `propuestas/sd-entregas/` (este informe, el inventario y las decisiones) y `propuestas/capturas-sd-revision/`.

**Verificaciones ejecutadas**

| Verificación | Resultado |
| --- | --- |
| `python tools/verificar.py` | 0 errores |
| `python tools/sd_revisar.py` | 0 errores · 0 para revisión · 15 avisos justificados |
| Controles nuevos | Celdas con oración en minúscula, enlaces en la validación, relaciones sin destino, resultados no observables y densidad de enlaces |
| Voz: oraciones que empiezan con «No» o tienen más de 25 palabras en el texto nuevo | 0 |
| `tools/lineas-dobles.js` en el Sistema de Diseño | `{}` |
| `tools/menu-etiquetas.js` | `[]` |
| Desborde horizontal en los 45 capítulos | 0 a 375 px y 0 a 768 px |
| Códigos y anclas frente al último commit | Sin cambios |
| `exportar.py` | Sin ejecutar |
| Lector de pantalla real (NVDA o VoiceOver) | Sin probar: no hay uno en este equipo |

**Prueba por tipo de norma, en escritorio y móvil**

| Tipo de norma | Norma |
| --- | --- |
| Un requisito | ARQ-002 |
| Varios requisitos | PEX-001 |
| Tabla | PEX-004 |
| Decisión por contexto | ARQ-006 |
| Detalles técnicos | ARQ-005 |
| Validación agrupada | Capítulo 01 |

**Páginas para revisar en pantalla** (recargue con Ctrl + F5):
- Sistema de Diseño:
  - 01 Principios comunes: PEX-001, PEX-004, PEX-017 y la validación;
  - 04 Información: ARQ-002;
  - 05 Navegación: ARQ-005 y ARQ-006;
  - 06 Búsqueda: ARQ-012;
  - 37 Product Default: SPR-001.
- Guía 05.

---

## Anexo A · Texto anterior y nuevo de las cinco normas

### PEX-017

**Antes**

##### KYN-SDI-PEX-017 · Control de la persona

**Titular:** Cancelar, deshacer y decidir

**Entrada:** Se aplica a las acciones reversibles y a lo que el sistema propone: la última decisión es de la persona.

- **Requisito:** La persona DEBE poder cancelar, deshacer o corregir las acciones reversibles y decidir sobre lo que el sistema propone.
- **Deshacer:** Toda acción reversible ofrece deshacer en el mismo lugar, según Reversibilidad, en 18 Recuperación.
- **Propuestas del sistema:** Lo que el sistema completa o sugiere se presenta como propuesta para revisar, según Control humano, en 30 Principios de IA.
- **Procesos largos:** Se pueden cancelar o pausar cuando el proceso lo permite, y se informa qué quedó hecho.
- **Verificación (grupo):**
  - Reversión: Se ejecuta cada acción reversible y se deshace. Resultado esperado: el estado anterior vuelve completo.
  - Propuestas: Se revisan los datos que completa el sistema antes de confirmar. Resultado esperado: cada uno se puede cambiar antes de confirmarlo.


**Después**

##### KYN-SDI-PEX-017 · Control de la persona

**Titular:** Cancelar, deshacer y decidir

**Entrada:** Se aplica a toda operación que la persona inicia y a lo que el sistema completa o sugiere: cada operación ofrece la salida que corresponde a su efecto, antes y después de confirmarla.

- **Requisito:** La persona DEBE poder cancelar, deshacer o corregir las acciones reversibles y decidir sobre lo que el sistema propone.
- **Aprobación de la persona:** Una propuesta necesita aprobación explícita cuando cambia datos de otras personas, envía algo fuera del producto o tiene efecto económico o legal.
- **Si la operación falla:** Lo que la persona escribió o eligió se conserva. El mensaje dice qué se guardó y ofrece reintentar.
- **Según la operación:** El mecanismo depende del efecto de cada operación. Un listado puede deshacer una eliminación y un pago, en cambio, pide confirmación previa.
- **Tabla «Salida según la operación»:**
  - Acción reversible: Cancelar cierra sin cambios. | Deshacer en el mismo lugar, mientras el cambio no afecte a otras personas o sistemas. Después, la corrección es una acción nueva que queda registrada.
  - Acción irreversible: El botón nombra la consecuencia, como «Eliminar definitivamente», y la confirmación dice qué se pierde. | Sin deshacer. La protección según el riesgo la define Acciones destructivas, en 12 Acciones.
  - Proceso largo: Cancelar antes de iniciar. | Cancelar o pausar cuando el sistema puede detenerlo sin dejar datos a medias. Al hacerlo, informa qué quedó hecho y qué no.
  - Propuesta del sistema: Lo completado o sugerido queda editable y marcado como propuesta. | Se corrige como cualquier dato propio.
- **Verificación (grupo):**
  - Reversión: Se ejecuta cada acción reversible y se deshace. Resultado esperado: el estado anterior vuelve completo.
  - Propuestas: Se revisan los datos que completa el sistema antes de confirmar. Resultado esperado: cada uno se puede cambiar antes de confirmarlo.
  - Fallo: Se provoca un fallo al guardar un formulario completo. Resultado esperado: los datos escritos siguen en el formulario y el mensaje ofrece reintentar.


### ARQ-002

**Antes**

##### KYN-SDI-ARQ-002 · Nombres comprensibles

**Titular:** Nombres reconocibles para secciones y destinos

**Entrada:** Se aplica a categorías, secciones y destinos: cada nombre usa el vocabulario de quien trabaja con el producto.

- **Requisito:** Las categorías, secciones y elementos de navegación DEBEN utilizar denominaciones que las personas puedan reconocer según su contexto de trabajo.
- **Vocabulario:** El de los perfiles, en lugar del vocabulario del código o de la base de datos.
- **Un concepto, un nombre:** El mismo concepto se nombra igual en todo el producto, según Consistencia, en 23 Escritura.
- **Siglas:** Solo las que el perfil usa a diario.
- **Verificación (grupo):**
  - Comprensión: Se muestra cada nombre de sección sin contexto y se pide decir qué se espera encontrar. Resultado esperado: lo que la persona espera coincide con el contenido de la sección.


**Después**

##### KYN-SDI-ARQ-002 · Nombres comprensibles

**Titular:** Nombres reconocibles para secciones y destinos

**Entrada:** Se aplica al nombrar menús, categorías, secciones y funciones: cada nombre usa el vocabulario de quien trabaja con el producto.

- **Requisito:** Las categorías, secciones y elementos de navegación DEBEN utilizar denominaciones que las personas puedan reconocer según su contexto de trabajo.
- **Vocabulario:** Los nombres salen de las palabras que los perfiles usan en su trabajo, recogidas en entrevistas, documentos y solicitudes reales. El vocabulario del código o de la base de datos queda fuera de la interfaz.
- **Etiqueta y título:** La etiqueta del menú es corta y nombra el destino. El título de la página puede precisarlo sin cambiar su sentido: menú «Solicitudes» y título «Solicitudes pendientes».
- **Siglas:** Solo las que el perfil usa a diario. Las demás se escriben completas, y una sigla nueva aparece completa la primera vez.
- **Un concepto, un nombre:** El mismo concepto conserva su nombre en el menú, los títulos, los botones y los mensajes de todo el producto.
- **Verificación (grupo):**
  - Comprensión: Se muestra cada nombre de sección sin contexto y se pide decir qué se espera encontrar. Resultado esperado: lo que la persona espera coincide con el contenido de la sección.
  - Tarea real: Se pide completar una tarea real eligiendo su destino en el menú. Resultado esperado: la persona elige el destino correcto al primer intento.


### ARQ-005

**Antes**

##### KYN-SDI-ARQ-005 · Ubicación actual

**Titular:** Ubicación y sección activa

**Entrada:** Se aplica a toda forma de navegación: la persona reconoce dónde está y cómo llegar a otra sección, sin recordar el camino.

- **Ubicación:** La navegación DEBE permitir reconocer en qué sección se encuentra la persona y cómo acceder a las demás áreas autorizadas. El título de la página nombra la sección y la navegación muestra los demás destinos autorizados. Desde el tercer nivel, una ruta jerárquica muestra el camino.
- **Sección activa:** La sección activa DEBE distinguirse visualmente y mantener una relación comprensible con sus secciones superiores cuando existan. Se marca con una señal de forma, como una barra, un fondo o un subrayado, y otra de color o de peso. Su grupo superior queda abierto o señalado. La apariencia la definen 08 Color funcional y 14 Estructura.
- **Al navegar:** El indicador, el título y la ruta cambian juntos, y el foco se ubica según el tipo de cambio.
- **Según el tipo de navegación (plegable):** Lateral o superior: El destino de la página abierta lleva el indicador. En la lateral, su grupo queda abierto; en la superior, señalado en la barra. · Pestañas: Las que llevan a otra página son enlaces y la activa lleva aria-current="page". Las que cambian un panel en la misma página siguen el patrón de pestañas de Identificación de controles. · Ruta jerárquica: Un <nav> con nombre accesible («Ruta») y una lista ordenada, del nivel más general al actual. El último nivel nombra la página y lleva aria-current. · Móvil: El título de la pantalla nombra la sección y la ruta se abrevia al nivel superior inmediato. Al abrir el menú, el destino activo se ve marcado.
- **Foco según el tipo de cambio (plegable):** Página nueva completa: El foco queda donde lo deja el navegador, al inicio del documento. El enlace «Ir al contenido» es lo primero que alcanza el teclado, sin recibir el foco automáticamente. · Vista nueva sin recargar: El foco pasa al título principal de la vista. Si la tarea necesita que el foco se quede donde estaba, una región en vivo anuncia el cambio. · Filtro, orden o pestaña de panel: El foco queda en el control que se usó. Si el resultado cambia fuera de la vista, se anuncia. · Panel o diálogo: El foco entra al abrir y vuelve al control que lo abrió al cerrar, según Adaptación por dispositivo.
- **Pantallas sin navegación general (plegable):** Cuáles: Los flujos de un paso, los diálogos y el inicio de sesión. · Qué conservan: Su título visible y una salida.
- **Verificación (tecnica):**
  - Con personas: Se abre con un enlace directo una pantalla de segundo o tercer nivel. Se pide nombrar la sección y el grupo, y llegar a otra sección principal. Se registra el tiempo; cinco segundos es la hipótesis inicial de prueba, no un requisito. Resultado esperado: la persona lo logra sin ayuda.
  - Escala de grises: Se ve la pantalla en escala de grises. Resultado esperado: la sección activa sigue distinguiéndose.
  - Lector de pantalla: Se recorre la navegación con NVDA o VoiceOver. Resultado esperado: el enlace activo se anuncia como «página actual».
  - Cambio de destino: Se prueba cada tipo de cambio de destino. Resultado esperado: el indicador, el título, la ruta y el foco se comportan como indica «Foco según el tipo de cambio».


**Después**

##### KYN-SDI-ARQ-005 · Ubicación actual

**Titular:** Ubicación y sección activa

**Entrada:** Se aplica a toda forma de navegación: la persona reconoce dónde está y cómo llegar a otra sección, sin recordar el camino.

- **Ubicación:** La navegación DEBE permitir reconocer en qué sección se encuentra la persona y cómo acceder a las demás áreas autorizadas. El título de la página nombra la sección y la navegación muestra los demás destinos autorizados. Desde el tercer nivel, una ruta jerárquica muestra el camino.
- **Sección activa:** La sección activa DEBE distinguirse visualmente y mantener una relación comprensible con sus secciones superiores cuando existan. Se marca con una señal de forma, como una barra, un fondo o un subrayado, y otra de color o de peso. Su grupo superior queda abierto o señalado.
- **Al navegar:** El indicador, el título y la ruta cambian juntos, y el foco se ubica según el tipo de cambio.
- **Lateral o superior:** El destino de la página abierta lleva el indicador. En la lateral, su grupo queda abierto; en la superior, señalado en la barra.
- **Pestañas:** Las que llevan a otra página son enlaces y la activa lleva aria-current="page". Las que cambian un panel en la misma página siguen el patrón de pestañas de Identificación de controles.
- **Ruta jerárquica:** Un <nav> con nombre accesible («Ruta») y una lista ordenada, del nivel más general al actual. El último nivel nombra la página y lleva aria-current.
- **Móvil:** El título de la pantalla nombra la sección y la ruta se abrevia al nivel superior inmediato. Al abrir el menú, el destino activo se ve marcado.
- **Sin navegación general:** Los flujos de un paso, los diálogos y el inicio de sesión conservan su título visible y una salida.
- **Foco según el tipo de cambio (plegable):** Página nueva completa: El foco queda donde lo deja el navegador, al inicio del documento. El enlace «Ir al contenido» es lo primero que alcanza el teclado, sin recibir el foco automáticamente. · Vista nueva sin recargar: El foco pasa al título principal de la vista. Si la tarea necesita que el foco se quede donde estaba, una región en vivo anuncia el cambio. · Filtro, orden o pestaña de panel: El foco queda en el control que se usó. Si el resultado cambia fuera de la vista, se anuncia. · Panel o diálogo: El foco entra al abrir y vuelve al control que lo abrió al cerrar.
- **Verificación (tecnica):**
  - Con personas: Se abre con un enlace directo una pantalla de segundo o tercer nivel. Se pide nombrar la sección y el grupo, y llegar a otra sección principal. Se registra el tiempo; cinco segundos es la hipótesis inicial de prueba, no un requisito. Resultado esperado: la persona lo logra sin ayuda.
  - Escala de grises: Se ve la pantalla en escala de grises. Resultado esperado: la sección activa sigue distinguiéndose.
  - Lector de pantalla: Se recorre la navegación con NVDA o VoiceOver. Resultado esperado: el enlace activo se anuncia como «página actual».
  - Cambio de destino: Se prueba cada tipo de cambio de destino. Resultado esperado: el indicador, el título, la ruta y el foco se comportan como indica «Foco según el tipo de cambio».


### ARQ-006

**Antes**

##### KYN-SDI-ARQ-006 · Acciones previsibles

**Titular:** Nombres, destinos y comportamientos estables

**Entrada:** Se aplica a todo elemento navegable: cada destino conserva su nombre, su lugar y su comportamiento en todo el producto.

- **Nombre y comportamiento:** Los elementos navegables DEBEN mantener nombres, destinos y comportamientos consistentes en todo el producto. Un destino se nombra de forma coherente en el menú, la ruta y el título; se abrevia o se precisa sin cambiar de significado, según Nombres comprensibles, en 04 Información. Un enlace lleva a otro lugar y un botón ejecuta una acción, en todas las pantallas.
- **Ubicación:** Las funciones principales DEBERÍAN conservar una ubicación y denominación consistentes entre las pantallas equivalentes. En todos los listados de un módulo, «Exportar» ocupa la misma posición.
- **Otra pestaña o salida del producto (plegable):** Comportamiento: Los enlaces abren en la misma pestaña. · Excepción: El enlace que abre otra pestaña o sale del producto lo anuncia con el ícono «abrir externo» y un texto accesible.
- **Verificación (breve):**
  - Inventario: Se listan los destinos con su nombre en el menú, la ruta y el título. Resultado esperado: cada variante conserva el significado del destino.
  - Recorrido: Se completa la misma tarea desde dos áreas autorizadas. Resultado esperado: se llega al mismo destino, con el mismo comportamiento.


**Después**

##### KYN-SDI-ARQ-006 · Acciones previsibles

**Titular:** Nombres, destinos y comportamientos estables

**Entrada:** Se aplica a todo elemento navegable y a las funciones que se repiten entre pantallas: la persona anticipa qué ocurrirá, aunque el mecanismo cambie según los datos.

- **Significado y comportamiento:** Los elementos navegables DEBEN mantener nombres, destinos y comportamientos consistentes en todo el producto. El significado se conserva siempre. Un destino se nombra igual en el menú, la ruta y el título, y se abrevia o se precisa sin cambiar de sentido. El tipo de control también se conserva: un enlace lleva a otro lugar y un botón ejecuta una acción. La interacción puede variar según los datos, la tarea y su complejidad, siempre que el resultado sea el que la persona espera.
- **Ubicación:** Las funciones principales DEBERÍAN conservar una ubicación y denominación consistentes entre las pantallas equivalentes. En los listados de un módulo, «Exportar» ocupa la misma posición y conserva su nombre.
- **Otra pestaña o salida del producto (plegable):** Comportamiento: Los enlaces abren en la misma pestaña. · Excepción: El enlace que abre otra pestaña o sale del producto lo anuncia con el ícono «abrir externo» y un texto accesible.
- **Verificación (breve):**
  - Inventario: Se listan los destinos con su nombre en el menú, la ruta y el título. Resultado esperado: cada variante conserva el significado del destino.
  - Recorrido: Se completa la misma tarea desde dos áreas autorizadas. Resultado esperado: se llega al mismo destino y el resultado es el esperado.


### ARQ-012

**Antes**

##### KYN-SDI-ARQ-012 · Resultados pertinentes

**Titular:** Campos y orden de los resultados

**Entrada:** Define qué datos usa la búsqueda y en qué orden muestra lo que encuentra: se encuentra por lo que la persona recuerda.

- **Requisito:** La búsqueda DEBE utilizar los campos y contenidos relevantes para la tarea, respetando los permisos de acceso.
- **Campos:** Nombre, código, identificación y los datos que el perfil usa para recordar un registro.
- **Coincidencia parcial:** Encuentra por parte del texto, sin distinguir mayúsculas ni tildes.
- **Orden:** Primero las coincidencias exactas; después, las más recientes o las más usadas, según la tarea.
- **Permisos:** El límite de lo que se busca lo define Resultados autorizados.
- **Autocompletado (plegable):** Cuándo: En listas conocidas: clientes, productos, direcciones. · Comportamiento: Las sugerencias aparecen al escribir; las flechas las recorren, Enter elige y Escape cierra. Sigue el patrón de cuadro combinado de 13 Entradas.
- **Errores de escritura (plegable):** Sugerencia: Cuando el producto lo permite, se ofrece la forma correcta: «¿Quiso decir…?».
- **Verificación (grupo):**
  - Consultas reales: Se buscan registros con nombre parcial, sin tildes y con un error de escritura. Resultado esperado: el registro buscado aparece entre los primeros resultados.


**Después**

##### KYN-SDI-ARQ-012 · Resultados pertinentes

**Titular:** Campos, coincidencias y orden de la búsqueda

**Entrada:** Define qué datos consulta la búsqueda, cómo compara lo que se escribe y en qué orden presenta lo encontrado: cada producto configura estos criterios según sus tareas y permisos.

- **Requisito:** La búsqueda DEBE utilizar los campos y contenidos relevantes para la tarea, respetando los permisos de acceso.
- **Campos consultables:** Los que el perfil usa para reconocer un registro: nombre, código, identificación y los datos propios de la tarea. Cada producto define la lista, y la búsqueda consulta solo lo que el perfil puede ver.
- **Coincidencias:** La exacta y la parcial cuentan: una parte del nombre encuentra el registro completo.
- **Tildes, mayúsculas e identificadores:** Las tildes y las mayúsculas se ignoran. Un identificador se compara sin espacios, guiones ni puntos, y así «001-234» y «001234» encuentran el mismo registro.
- **Orden:** Cada producto define sus criterios y los documenta: coincidencia exacta, uso reciente, frecuencia o fecha. Una tarea de consulta suele empezar por la coincidencia exacta; una bandeja de trabajo, por lo más reciente.
- **Buscar, filtrar y ordenar:** Buscar encuentra registros por lo que se escribe. Filtrar reduce el conjunto con criterios conocidos, como el estado o la fecha. Ordenar cambia la secuencia sin quitar registros, y cada uno se muestra por separado.
- **Autocompletado (plegable):** Cuándo: En listas conocidas: clientes, productos, direcciones. · Comportamiento: Las sugerencias aparecen al escribir; las flechas las recorren, Enter elige y Escape cierra. Sigue el patrón de cuadro combinado de 13 Entradas.
- **Errores de escritura (plegable):** Sugerencia: Cuando el producto lo permite, se ofrece la forma correcta: «¿Quiso decir…?».
- **Verificación (grupo):**
  - Consultas reales: Se buscan registros con nombre parcial, sin tildes, con un identificador escrito de otra forma y con un error de escritura. Resultado esperado: el registro buscado aparece entre los primeros resultados.


## Anexo B · Cobertura por norma

Criterio: las cinco preguntas de control (qué se decide, cuándo, qué comportamiento, qué condiciones cambian la decisión y cómo se comprueba). Tener titular, requisito y verificación no basta para contar como desarrollada.

| Código | Cap. | Nombre | Cobertura | Motivo o responsabilidad incompleta | Verificación |
| --- | --- | --- | --- | --- | --- |
| PEX-001 | 01 | La tarea primero | desarrollada | — | Nota breve |
| PEX-002 | 01 | Claridad antes que novedad | requiere aprobación | Contiene una propuesta: (propuesta | Nota breve |
| PEX-003 | 01 | Complejidad justificada | desarrollada | — | Nota breve |
| PEX-004 | 01 | Estado comprensible | desarrollada | — | Validación del capítulo |
| PEX-005 | 01 | Comportamiento previsible | desarrollada | — | Nota breve |
| PEX-006 | 01 | Contexto antes de actuar | desarrollada | — | Validación del capítulo |
| PEX-016 | 01 | Prevención de errores | requiere aprobación | Requisito redactado por Claude | Validación del capítulo |
| PEX-017 | 01 | Control de la persona | requiere aprobación | Requisito redactado por Claude | Validación del capítulo |
| PEX-018 | 01 | Reconocer antes que recordar | requiere aprobación | Requisito redactado por Claude | Nota breve |
| PEX-007 | 02 | Diseñar para quienes utilizan el producto | desarrollada | — | Validación del capítulo |
| PEX-008 | 02 | Roles y permisos | desarrollada | — | Plegable técnico |
| PEX-009 | 02 | Uso ocasional y frecuente | desarrollada | — | Validación del capítulo |
| PEX-010 | 03 | Decisiones justificadas | desarrollada | — | Nota breve |
| PEX-011 | 03 | Prisma como metodología | desarrollada | — | Nota breve |
| PEX-012 | 03 | Diseño por capas | desarrollada | — | Nota breve |
| PEX-013 | 03 | Diseño basado en resultados | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Referencia |
| PEX-014 | 03 | Evidencia diferenciada | desarrollada | — | Nota breve |
| PEX-015 | 03 | Evaluación posterior | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| ARQ-001 | 04 | Organización comprensible | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Validación del capítulo |
| ARQ-002 | 04 | Nombres comprensibles | desarrollada | — | Validación del capítulo |
| ARQ-003 | 04 | Jerarquía identificable | desarrollada | — | Nota breve |
| ARQ-004 | 04 | Información progresiva | desarrollada | — | Nota breve |
| ARQ-005 | 05 | Ubicación actual | desarrollada | — | Plegable técnico |
| ARQ-006 | 05 | Acciones previsibles | desarrollada | — | Nota breve |
| ARQ-007 | 05 | Navegación visible | desarrollada | — | Plegable técnico |
| ARQ-008 | 05 | Identificación de controles | desarrollada | — | Plegable técnico |
| ARQ-009 | 05 | Adaptación por dispositivo | requiere aprobación | Contiene una propuesta: Propuesta: | Plegable técnico |
| ARQ-010 | 05 | Regreso sin pérdida | desarrollada | — | Plegable técnico |
| ARQ-017 | 05 | Acceso directo y rutas no disponibles | requiere aprobación | Requisito redactado por Claude | Plegable técnico |
| ARQ-011 | 06 | Alcance identificable | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| ARQ-012 | 06 | Resultados pertinentes | desarrollada | — | Validación del capítulo |
| ARQ-013 | 06 | Resultados comprensibles | desarrollada | — | Validación del capítulo |
| ARQ-014 | 06 | Filtros visibles | desarrollada | — | Validación del capítulo |
| ARQ-015 | 06 | Sin resultados | desarrollada | — | Validación del capítulo |
| ARQ-016 | 06 | Resultados autorizados | desarrollada | — | Plegable técnico |
| FUI-001 | 07 | Fuente única de valores | desarrollada | — | Validación del capítulo |
| FUI-002 | 07 | Roles semánticos | requiere aprobación | Contiene una propuesta: Se propone | Nota breve |
| FUI-003 | 07 | Cambios controlados | desarrollada | — | Validación del capítulo |
| FUI-004 | 08 | Color con función | desarrollada | — | Nota breve |
| FUI-005 | 08 | Estados semánticos | desarrollada | — | Validación del capítulo |
| FUI-006 | 08 | Separación de significados | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Validación del capítulo |
| FUI-007 | 08 | Contraste | requiere aprobación | Contiene una propuesta: Requiere aprobación | Plegable técnico |
| FUI-008 | 09 | Sistema tipográfico | desarrollada | — | Nota breve |
| FUI-009 | 09 | Jerarquía consistente | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| FUI-010 | 09 | Legibilidad | desarrollada | — | Validación del capítulo |
| FUI-011 | 09 | Truncamiento | desarrollada | — | Validación del capítulo |
| FUI-012 | 10 | Espaciado compartido | requiere aprobación | Contiene una propuesta: (propuesta | Nota breve |
| FUI-013 | 10 | Agrupación semántica | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Validación del capítulo |
| FUI-014 | 10 | Composición adaptable | desarrollada | — | Validación del capítulo |
| FUI-015 | 11 | Iconos funcionales | desarrollada | — | Nota breve |
| FUI-016 | 11 | Identidad visual | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| FUI-017 | 11 | Expresión proporcionada | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| CPE-001 | 12 | Jerarquía de acciones | desarrollada | — | Nota breve |
| CPE-002 | 12 | Estados de los controles | desarrollada | — | Plegable técnico |
| CPE-003 | 12 | Acciones destructivas | desarrollada | — | Nota breve |
| CPE-004 | 12 | Menú de acciones | requiere aprobación | Requisito redactado por Claude | Plegable técnico |
| CPE-005 | 13 | Etiquetas identificables | desarrollada | — | Validación del capítulo |
| CPE-006 | 13 | Validación útil | desarrollada | — | Validación del capítulo |
| CPE-007 | 13 | Control apropiado | desarrollada | — | Validación del capítulo |
| CPE-008 | 14 | Contenedores con función | pendiente | Hoja de componentes (apariencia) | Plegable técnico |
| CPE-009 | 14 | Jerarquía estable | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| CPE-010 | 14 | Diálogos | desarrollada | — | Plegable técnico |
| CPE-011 | 15 | Resultado visible | desarrollada | — | Validación del capítulo |
| CPE-012 | 15 | Mensajes pertinentes | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Validación del capítulo |
| CPE-013 | 15 | Atención proporcionada | pendiente | Niveles de urgencia (propuesta desde UIX) | Nota breve |
| PAT-001 | 16 | Flujo comprensible | desarrollada | — | Validación del capítulo |
| PAT-002 | 16 | Prevención de pérdidas | desarrollada | — | Validación del capítulo |
| PAT-003 | 16 | Validación proporcionada | desarrollada | — | Validación del capítulo |
| PAT-004 | 17 | Secuencia y progreso | desarrollada | — | Validación del capítulo |
| PAT-005 | 17 | Contexto conservado | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Validación del capítulo |
| PAT-006 | 17 | Terminación clara | desarrollada | — | Validación del capítulo |
| PAT-007 | 18 | Ruta de salida | desarrollada | — | Validación del capítulo |
| PAT-008 | 18 | Reversibilidad | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| PAT-009 | 18 | Persistencia | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Validación del capítulo |
| PAT-010 | 18 | Estados vacíos y de espera | requiere aprobación | Requisito redactado por Claude | Plegable técnico |
| PAT-011 | 19 | Autorización | desarrollada | — | Plegable técnico |
| PAT-012 | 19 | Trazabilidad | desarrollada | — | Nota breve |
| ACC-001 | 20 | Referencia de conformidad | requiere aprobación | Requisito redactado por Claude | Nota breve |
| ACC-002 | 20 | Información perceptible | desarrollada | — | Validación del capítulo |
| ACC-003 | 20 | Lectura adaptable | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Validación del capítulo |
| ACC-004 | 21 | Teclado | desarrollada | — | Plegable técnico |
| ACC-005 | 21 | Foco identificable | desarrollada | — | Plegable técnico |
| ACC-006 | 21 | Tiempo y movimiento | desarrollada | — | Plegable técnico |
| ACC-007 | 22 | Diseño adaptable | desarrollada | — | Plegable técnico |
| ACC-008 | 22 | Interacciones accesibles | desarrollada | — | Nota breve |
| ACC-009 | 22 | Variaciones de uso | desarrollada | — | Nota breve |
| CNT-001 | 23 | Lenguaje funcional | desarrollada | — | Nota breve |
| CNT-002 | 23 | Consistencia | pendiente | Glosario de cada producto | Nota breve |
| CNT-003 | 23 | Brevedad útil | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| CNT-004 | 24 | Errores comprensibles | desarrollada | — | Nota breve |
| CNT-005 | 24 | Confirmaciones específicas | desarrollada | — | Nota breve |
| CNT-006 | 24 | Información segura | desarrollada | — | Plegable técnico |
| CNT-007 | 25 | Lenguaje adecuado | pendiente | Idiomas que se ofrecen | Validación del capítulo |
| CNT-008 | 25 | Consistencia lingüística | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Validación del capítulo |
| CNT-009 | 25 | Espacio variable | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Validación del capítulo |
| DAV-001 | 26 | Lectura y comparación | desarrollada | — | Plegable técnico |
| DAV-002 | 26 | Herramientas proporcionadas | desarrollada | — | Validación del capítulo |
| DAV-003 | 26 | Acciones identificables | desarrollada | — | Validación del capítulo |
| DAV-007 | 27 | Representación apropiada | desarrollada | — | Nota breve |
| DAV-008 | 27 | Color de datos | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| DAV-009 | 27 | Interpretación accesible | desarrollada | — | Plegable técnico |
| DAV-010 | 28 | Contexto suficiente | desarrollada | — | Nota breve |
| DAV-011 | 28 | Estados fundamentados | pendiente | Responsables de umbrales por producto | Nota breve |
| DAV-012 | 28 | Actualización visible | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| DAV-004 | 29 | Diseño por tarea | desarrollada | — | Validación del capítulo |
| DAV-005 | 29 | Jerarquía informativa | desarrollada | — | Validación del capítulo |
| DAV-006 | 29 | Profundidad de consulta | desarrollada | — | Validación del capítulo |
| IAE-001 | 30 | Transparencia | desarrollada | — | Nota breve |
| IAE-002 | 30 | Incertidumbre | pendiente | Niveles de confianza (propuesta desde UIX) | Nota breve |
| IAE-003 | 30 | Control humano | pendiente | Niveles de supervisión por riesgo | Plegable técnico |
| IAE-004 | 31 | Contexto útil | pendiente | Memoria persistente | Validación del capítulo |
| IAE-005 | 31 | Preguntas pertinentes | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Validación del capítulo |
| IAE-006 | 31 | Respuesta accionable | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Validación del capítulo |
| IAE-007 | 32 | Responsabilidad identificable | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| IAE-008 | 32 | Límites de actuación | desarrollada | — | Plegable técnico |
| IAE-009 | 32 | Identidad pública consistente | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| IAE-010 | 33 | Confianza calibrada | pendiente | Criterio de cada nivel de confianza | Nota breve |
| IAE-011 | 33 | Verificación humana | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| IAE-012 | 33 | Privacidad | desarrollada | — | Plegable técnico |
| SPR-005 | 34 | Infraestructura común | pendiente | Lista de la firma UX | Nota breve |
| SPR-006 | 34 | Variaciones justificadas | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| SPR-007 | 34 | Compatibilidad | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Referencia |
| SPR-008 | 35 | Navegación y propósito | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| SPR-009 | 35 | Interacción accesible | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| SPR-010 | 36 | Eficiencia operativa | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| SPR-011 | 36 | Permisos y contexto | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| SPR-001 | 37 | Experiencia predeterminada | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| SPR-002 | 37 | Sobriedad operativa | desarrollada | — | Nota breve |
| SPR-003 | 37 | Personalización controlada | desarrollada | — | Plegable técnico |
| SPR-004 | 37 | Navegación predeterminada | requiere aprobación | Requisito redactado por Claude | Nota breve |
| SPR-012 | 38 | Identidad del cliente | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| SPR-013 | 38 | Calidad funcional | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Plegable técnico |
| SPR-014 | 38 | Ausencia de firma | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| MOV-001 | 39 | Movimiento funcional | pendiente | Curvas y duraciones por componente (tokens) | Nota breve |
| MOV-002 | 39 | Duración proporcionada | pendiente | Duraciones máximas (tokens) | Nota breve |
| MOV-003 | 40 | Expresión con propósito | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| MOV-004 | 40 | Comprensión independiente | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| MOV-005 | 41 | Sonido | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| MOV-006 | 41 | Háptica | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| MOV-007 | 41 | Alternativas | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| GOB-004 | 42 | Fuente única | pendiente | Roles de aprobación | Nota breve |
| GOB-005 | 42 | Estado visible | pendiente | Roles de aprobación y versión | Nota breve |
| GOB-006 | 43 | Uso de componentes canónicos | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Plegable técnico |
| GOB-007 | 43 | Excepciones justificadas | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| GOB-008 | 43 | Entrega comprobable | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Referencia |
| GOB-001 | 44 | Tareas reales | desarrollada | — | Nota breve |
| GOB-002 | 44 | Problemas críticos | desarrollada | — | Nota breve |
| GOB-003 | 44 | Protocolo previo al lanzamiento | requiere aprobación | Requisito redactado por Claude | Plegable técnico |
| GOB-009 | 45 | Componentes documentados | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| GOB-010 | 45 | Ejemplos funcionales | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
| GOB-011 | 45 | Versionado | parcial | Requisito, decisiones breves y verificación; falta desarrollo de comportamientos o casos | Nota breve |
