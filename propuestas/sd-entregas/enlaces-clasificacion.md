# Enlaces del Sistema de Diseño: utilidad y concentración

2026-11-18 · revisión sin cambios en las páginas. Las normas siguen como quedaron en la Fase A (commit `cf9aa66`). Este documento clasifica cada enlace visible y propone, con cinco ejemplos, qué se conserva y qué se reubica. Nada se aplica hasta su revisión.

## Decisión aplicada (Keylin, 2026-11-18)

Keylin no aprobó las notas «Se desarrolla en». Las propuestas de reubicación a esa nota que siguen en este documento quedan **reemplazadas** por lo que se aplicó:

| Clase | Antes | Aplicado |
| --- | --- | --- |
| Esencial | 37 visibles | **38 visibles**, integrados en el texto: el enlace va sobre el concepto («la [confirmación] se refuerza según el riesgo»), sin frases del tipo «Lo define…» o «Según el capítulo…» |
| Complementaria | 76 visibles | **0 visibles.** Quedan en el registro (`relaciones`) |
| Trazabilidad | 42 visibles | **0 visibles.** Quedan en el registro |

Hay 38 visibles y no 37 porque uno de los enlaces esenciales se dividió al integrarlo en el texto.

**Cómo se trató cada norma**
- **Normas autosuficientes.** Donde una oración solo remitía, se escribió la decisión con contenido que ya estaba aprobado en el sistema, sin obligaciones nuevas. Donde no había nada propio, la fila se quitó.
- **Los cinco ejemplos:**
  - **PEX-004:** la tabla queda autosuficiente, sin enlaces. Su columna se llama «Cómo · En la interfaz».
  - **FUI-004:** conserva sus cinco enlaces hasta la Fase B.
  - **PAT-001:** el paso «Confirmar» se desarrolló («Muestra el resultado con su identificador… y el siguiente paso»).
  - **FUI-014:** redacción corregida, con un solo enlace (la retícula).
  - **FUI-016:** se quitaron las filas «Dónde están» y «Productos sin firma».
- **Las cinco filas que solo remitían:**
  - ACC-007 y CNT-006 tienen ahora su decisión.
  - En ARQ-008, ACC-003 y CNT-002 la fila se quitó.

**Registro y regla**
- **Registro canónico:** 180 relaciones en 103 normas, generadas desde los módulos. Ahora incluyen normas del Libro de Marca (`KYN-MRK-…`) y capítulos (`SD-NN`).
- **Guía 05, fila «Referencias»:** quedó reescrita con estos criterios.
- **`tools/sd_revisar.py`:** dejó de contar enlaces. Ahora avisa cuando una frase solo presenta un enlace.

## Criterio

| Clase | Qué significa | Dónde queda |
| --- | --- | --- |
| **Esencial** | Lleva a un valor, un patrón o una prueba que hace falta para aplicar la norma y que la página no repite (por ejemplo, el patrón de teclado de las pestañas o los colores de la acción en el Libro de Marca) | En el contexto, junto a la decisión |
| **Complementaria** | La norma se entiende y se aplica sin abrirla, pero amplía un tema vecino (redacción del mensaje, procedimiento de versionado, criterios técnicos) | En una relación secundaria discreta, fuera de la lectura principal |
| **Trazabilidad** | La oración ya dice todo. El enlace solo repite el nombre de otra norma o remite a algo sin definir | En el registro (`relaciones`), sin enlace visible |

Además se marca cada **frase que solo existe para introducir la referencia**: «Su apariencia la define…», «Se describe en…», «Ver…», «El progreso sigue…». Esas frases se reescriben con la decisión o se quitan.

## Resultado

| Clase | Enlaces |
| --- | --- |
| Esencial | 37 |
| Complementaria | 76 (74 en normas y 2 en la entrada de dos validaciones) |
| Trazabilidad | 42 |
| **Total** | **155** |

- **Frases construidas solo para introducir una referencia:** 24. Cuatro las creé yo en la Fase A, al reubicar enlaces: PAT-001 «Lo define…», PAT-006 «El nivel de protección lo define…», PAT-011 «Su nivel lo define…» y CPE-012 «…según 24 Mensajes».
- **Un error de redacción, también mío:** FUI-014 dice «con valor predeterminado según el perfil según la frecuencia de uso». Se corrige con esta revisión.

**Concentración por capítulo** (los más cargados)

| Capítulo | Enlaces | Esenciales | Complementarios | Trazabilidad |
| --- | --- | --- | --- | --- |
| 01 Principios comunes | 16 | 2 | 9 | 5 |
| 08 Color funcional | 9 | 6 | 2 | 1 |
| 05 Navegación | 8 | 3 | 4 | 1 |
| 11 Recursos visuales | 7 | 0 | 5 | 2 |
| 03 Elecciones verificadas | 6 | 1 | 2 | 3 |
| 26 Tablas | 6 | 1 | 3 | 2 |

El capítulo 01 tiene la carga más alta y la menos necesaria: solo 2 de sus 16 enlaces son esenciales. El 08, en cambio, concentra enlaces porque cita los colores del Libro de Marca en lugar de copiarlos, y eso es correcto.

## Una decisión previa: cómo se ve la relación secundaria

`CLAUDE.md` dice hoy: «Sin bloques "Normas relacionadas" ni "Relacionado": una referencia a otra norma va dentro del texto, con enlace». Su pedido de la Fase A permite reunir las referencias complementarias «en una sección secundaria discreta, sin convertirla en un bloque obligatorio». Las dos instrucciones chocan, y necesito que usted elija una.

**Propuesta.** Usar la nota de cierre que ya existe (`.ed__more`, 16 px en gris de lectura y rótulo de 12 px), con el rótulo «Se desarrolla en», y solo cuando una norma tiene dos referencias complementarias o más. Con una sola, la referencia queda en su oración, si la oración tiene contenido propio, o pasa al registro. Ningún estilo nuevo.

## Cinco ejemplos

### 1 · PEX-004 · Comunicar el estado de cada acción (4 enlaces, los 4 complementarios)

**Hoy.** La columna «Cómo · Dónde se desarrolla» describe cada estado y termina con un enlace entre paréntesis:

| Estado | Cómo |
| --- | --- |
| Procesando | Indicador en el control o en la zona afectada; texto descriptivo si la espera es larga **(Estados de espera)** |
| Terminó | Confirmación específica **(Confirmaciones)** |
| Requiere intervención | Mensaje junto al elemento afectado, con una acción **(Mensajes)** |
| Falló | Mensaje con una salida **(Ruta de salida)** |

**Diagnóstico.** Cada celda ya dice cómo se resuelve. Los cuatro enlaces subrayados en la misma columna convierten la tabla en un índice.

**Propuesta**
- **Se conserva:** la tabla, con las descripciones tal como están.
- **Se reubica:** los cuatro enlaces pasan a una nota «Se desarrolla en: Estados de espera, Confirmaciones, Mensajes y Ruta de salida», debajo de la tabla.
- **Cambia:** el subtítulo de la columna pasa de «Dónde se desarrolla» a «En la interfaz».

### 2 · FUI-004 · Función de cada color en la interfaz (5 enlaces, los 5 esenciales)

**Hoy.** La tabla asigna cada función (identidad, jerarquía, acción, estado y datos) a su norma del Libro de Marca. La celda de origen es solo el enlace.

**Diagnóstico.** Es el caso opuesto al anterior. El Sistema de Diseño cita los colores sin copiarlos, así que sin el enlace no hay valor que aplicar. La concentración se justifica.

**Propuesta**
- **Se conserva:** los cinco, en la tabla.
- **Para la Fase B:** cuando el capítulo 08 muestre las muestras de color reales, estos enlaces pasarían a ser complementarios.

### 3 · PAT-001 · Orden y agrupación de los formularios (3 enlaces: 1 esencial y 2 complementarios)

**Hoy**
- En el paso «Enviar»: «Muestra la carga y evita el doble envío **(Estados de los controles)**».
- En el paso «Confirmar», el criterio dice solo: «Lo define **Terminación clara**, en 17 Flujos de trabajo». Esta frase la escribí yo en la Fase A.
- En el plegable «Varios pasos»: «Cuando el formulario reúne decisiones distintas o es largo. El progreso sigue **17 Flujos de trabajo**».

**Diagnóstico.** El primero es esencial: dice qué estado toma el botón. Los otros dos son frases que solo existen para remitir, y el paso «Confirmar» queda sin contenido propio.

**Propuesta**
- **Se conserva:** «Estados de los controles» en su oración.
- **Se reescribe** el criterio de «Confirmar» con la decisión: «El resultado se ve y el siguiente paso queda a la mano».
- **Se quita** «El progreso sigue…».
- **Se reubica:** «Terminación clara» y «17 Flujos de trabajo» pasan a la nota «Se desarrolla en».

### 4 · FUI-014 · Retícula, densidad y esquinas (3 enlaces: 1 esencial y 2 complementarios)

**Hoy**
- «Columnas, márgenes y medianiles siguen **Retícula y responsive**».
- «Modo cómodo y modo denso, con valor predeterminado según el perfil según la frecuencia de uso, como define **Jerarquía y densidad de información**». Esta oración tiene un error mío: «según… según».
- «Radios de la escala: `--r-control` en controles, `--r-component` en componentes y `--r-card` en tarjetas **(Sistema de radios y curvaturas)**».

**Diagnóstico**
- La retícula es esencial: los valores están en el Libro de Marca.
- La densidad es complementaria.
- Los radios ya están escritos en la celda, así que su enlace solo sirve a la trazabilidad.

**Propuesta**
- **Se conserva:** el enlace a la retícula.
- **Se corrige y se reubica:** la densidad queda como «Modo cómodo y modo denso; el predeterminado depende de la frecuencia de uso del perfil», y su enlace pasa a la nota.
- **Se registra sin enlace:** el de los radios, que ya están escritos.

### 5 · FUI-016 · Recursos gráficos según la marca (3 enlaces, los 3 complementarios)

**Hoy**
- La fila «Dónde están» dice: «Iconografía, ilustración, fotografía y composición viven en el Libro de Marca; aquí se citan **(Uso, Retícula y responsive)**».
- La fila «Productos sin firma» dice: «Los recursos de cliente siguen **38 White-label**».

**Diagnóstico.** Las dos filas se escribieron solo para remitir y no le dicen al diseñador qué hacer. Es el caso de frase-índice que usted señaló.

**Propuesta**
- **Se quita** la fila «Dónde están». Sus dos enlaces pasan a la nota «Se desarrolla en».
- **Productos sin firma:** queda en el registro sin enlace. El capítulo 38 todavía no define los recursos de cliente, así que el enlace lleva a una página sin la respuesta.
- **Contenido nuevo, solo si usted lo aprueba:** la fila podría decir la decisión: «En un producto sin firma, los íconos y la composición se conservan y la identidad del cliente reemplaza la de Keyons».

## Otras filas hechas solo de referencias

Siguen el mismo criterio y no las cambié:

| Norma | Fila | Texto actual | Qué falta |
| --- | --- | --- | --- |
| ACC-007 | Cómo se reorganiza | «Según la retícula de 10 Espacio y retícula y la navegación de 05 Navegación» | Decir cómo se reorganiza (orden, columnas, menú) |
| CNT-006 | Permisos | «Ver Acceso directo y rutas no disponibles (05) y Resultados autorizados (06)» | La decisión de redacción del mensaje sin permiso |
| ARQ-008 | Panel móvil | «Se describe en Adaptación por dispositivo» | Nada propio; pasaría a la nota o al registro |
| ACC-003 | Desarrollo | «Las decisiones de texto están en Legibilidad, en 09 Tipografía» | Depende de la consolidación FUI-010 / ACC-003 que está pendiente |
| CNT-002 | Navegación | «Para nombres de secciones rige Nombres comprensibles (04 Información)» | Nada propio; pasaría al registro |

## Clasificación completa

Cada fila es un enlace visible de una norma. Los dos enlaces de las validaciones (44 Validación y 24 Mensajes, en la entrada de los capítulos 04 y 06) son complementarios y no figuran en la tabla.

| Norma | Fila | Enlace | Clase | Solo introduce la referencia | Motivo |
| --- | --- | --- | --- | --- | --- |
| PEX-001 | Acción principal | Jerarquía de acciones | Complementaria | Sí | La decisión (una sola principal) está escrita; la apariencia se consulta al implementar el botón |
| PEX-001 | Recursos gráficos | Expresión proporcionada | Trazabilidad | — | La oración ya dice la decisión completa |
| PEX-002 | Patrón propio | Evaluación posterior | Complementaria | — | Cómo se evalúa un patrón propio |
| PEX-002 | Control antes que automatización | Control de la persona | Trazabilidad | — | Misma página; la oración se entiende sola |
| PEX-003 | Lo visible | Información progresiva | Trazabilidad | — | La oración ya dice qué queda visible y qué a un paso |
| PEX-003 | Lo visible | Uso ocasional y frecuente | Complementaria | Sí | La densidad por perfil es otra decisión; la oración existe para remitir |
| PEX-004 | Procesando | Estados de espera | Complementaria | — | La celda ya describe el indicador; el enlace lleva al detalle |
| PEX-004 | Terminó | Confirmaciones | Complementaria | — | La celda ya describe la confirmación |
| PEX-004 | Requiere intervención | Mensajes | Complementaria | — | La celda ya describe el mensaje |
| PEX-004 | Falló | Ruta de salida | Complementaria | — | La celda ya describe la salida |
| PEX-005 | Entre productos | Infraestructura común | Trazabilidad | — | La oración se entiende sola |
| PEX-005 | Navegación | Acciones previsibles | Complementaria | Sí | La fila solo remite a otra norma |
| PEX-006 | Proporción | Acciones destructivas | Esencial | — | Los niveles de protección hacen falta para implementar |
| PEX-016 | Formatos | Etiquetas identificables | Trazabilidad | — | La oración ya dice dónde va el formato |
| PEX-016 | Acciones de riesgo | Contexto antes de actuar | Complementaria | — | Misma página; amplía la protección |
| PEX-017 | Acción irreversible | Acciones destructivas | Esencial | — | Los niveles de protección hacen falta para implementar |
| PEX-007 | Accesibilidad | los capítulos 20 a 22 de Accesibilidad | Complementaria | — | Criterios técnicos de accesibilidad |
| PEX-007 | Fuente | Evidencia diferenciada | Trazabilidad | — | La oración ya dice la decisión |
| PEX-008 | Validación en el servidor | Acceso directo y rutas no disponibles | Complementaria | — | Comportamiento del mensaje sin permiso |
| PEX-009 | Densidad y ayudas | 10 Espacio y retícula | Trazabilidad | — | La oración ya dice las dos densidades |
| PEX-010 | Excepciones | Excepciones justificadas | Complementaria | — | Procedimiento de registro de excepciones |
| PEX-010 | Reutilización | 34 Base compartida | Trazabilidad | — | La oración se entiende sola |
| PEX-011 | Entregable | Diseño por capas | Complementaria | — | Detalle del proceso por capas |
| PEX-011 | Aprobación | 42 Gobierno normativo | Trazabilidad | Sí | Remite a algo todavía sin definir |
| PEX-013 | Prototipos | Problemas críticos | Esencial | — | La verificación es la prueba definida en otra norma |
| PEX-015 | Extensión | 34 Base compartida | Trazabilidad | — | La oración se entiende sola |
| ARQ-001 | Agrupación | Diseñar para quienes utilizan el producto | Trazabilidad | — | La oración ya dice con qué se decide |
| ARQ-003 | Complementaria | Información progresiva | Trazabilidad | — | La oración ya nombra los controles |
| ARQ-003 | Complementaria | Jerarquía consistente | Complementaria | — | Criterio de jerarquía visual para la prueba |
| ARQ-004 | Detalle a pedido | Contenedores con función | Esencial | — | Qué contenedor usar se decide allí |
| ARQ-005 | Pestañas | Identificación de controles | Esencial | — | Patrón de teclado de las pestañas |
| ARQ-008 | Panel móvil | Adaptación por dispositivo | Complementaria | Sí | La fila solo remite a otra norma |
| ARQ-008 | Foco | Foco identificable | Esencial | Sí | La apariencia del foco hace falta para implementar; la oración existe para remitir |
| ARQ-009 | Productos SaaS | Navegación predeterminada | Complementaria | Sí | La fila solo remite al predeterminado SaaS |
| ARQ-009 | Preferencia Keyons | Interacciones accesibles | Complementaria | — | Decisión pendiente que se toma en otra norma |
| ARQ-010 | Cambios pendientes | Prevención de pérdidas | Esencial | — | Comportamiento ante cambios sin guardar |
| ARQ-017 | Ruta autorizada | Ubicación actual | Trazabilidad | — | Misma idea ya explicada en la navegación |
| ARQ-017 | Texto del mensaje | Errores comprensibles | Complementaria | — | Redacción del mensaje |
| ARQ-012 | Comportamiento | 13 Entradas | Esencial | — | Patrón de teclado del cuadro combinado |
| ARQ-013 | Muchos resultados | Herramientas proporcionadas | Complementaria | — | Herramientas de tabla |
| ARQ-014 | Al volver | Regreso sin pérdida | Esencial | Sí | Qué se conserva al volver; la fila casi no tiene contenido propio |
| ARQ-015 | Error de consulta | Ruta de salida | Complementaria | — | La celda ya dice reintentar y salida |
| ARQ-015 | Sin acceso al alcance | Resultados autorizados | Trazabilidad | — | La oración ya dice el comportamiento |
| FUI-002 | Foco | Contraste | Complementaria | — | Decisión pendiente |
| FUI-002 | Acción | Acción y superficies | Esencial | — | Valores de color de la acción en el Libro de Marca |
| FUI-002 | Estado | Estados semánticos | Complementaria | — | La celda ya nombra los estados |
| FUI-003 | Versión | Versionado | Complementaria | — | Procedimiento de versionado |
| FUI-003 | Aprobación | 42 Gobierno normativo | Trazabilidad | — | Remite a un capítulo sin detalle aplicable |
| FUI-004 | Identidad | Color en pantalla | Esencial | — | La columna asigna cada función a su norma de origen, que el Sistema de Diseño cita sin copiar |
| FUI-004 | Jerarquía | Grises tipográficos | Esencial | — | Ídem |
| FUI-004 | Acción | Acción y superficies | Esencial | — | Ídem |
| FUI-004 | Estado | Estados del sistema | Esencial | — | Ídem |
| FUI-004 | Datos | Sistema cromático | Esencial | — | Ídem |
| FUI-005 | Íconos | Cómo se usan | Complementaria | — | Catálogo de íconos |
| FUI-006 | Salmón Tierra | Reglas de uso | Complementaria | — | Reglas del Salmón Tierra |
| FUI-006 | Error | Estados semánticos | Trazabilidad | — | Misma idea ya dicha con el token |
| FUI-007 | Pares de tokens | Combinaciones | Esencial | — | Lista de combinaciones aprobadas para la prueba |
| FUI-008 | Familias | Uso por función | Complementaria | Sí | La oración ya dice el uso de cada familia |
| FUI-008 | Escala | Escala y jerarquía | Esencial | — | Fuente de la escala |
| FUI-012 | Origen | Sistema de espaciado | Esencial | — | Fuente de la escala |
| FUI-014 | Retícula | Retícula y responsive | Esencial | — | Columnas, márgenes y medianiles |
| FUI-014 | Densidad | Jerarquía y densidad de información | Complementaria | — | Densidad; la oración tiene además un error de redacción |
| FUI-014 | Esquinas | Sistema de radios y curvaturas | Complementaria | — | Los valores ya están escritos en la celda |
| FUI-015 | De estado | Estados semánticos | Trazabilidad | — | La celda se entiende sola |
| FUI-015 | Catálogo | Cómo se usan | Complementaria | — | Catálogo de íconos |
| FUI-016 | Dónde están | Uso | Complementaria | Sí | La fila existe para remitir |
| FUI-016 | Dónde están | Retícula y responsive | Complementaria | Sí | La fila existe para remitir |
| FUI-016 | Productos sin firma | 38 White-label | Complementaria | Sí | La fila solo remite |
| FUI-017 | Principio | 01 Principios comunes | Trazabilidad | Sí | La oración presenta la relación con otro principio |
| FUI-017 | Dónde sí | Sobriedad operativa | Complementaria | — | Dónde sí se usan recursos expresivos |
| CPE-001 | Destructiva | Acciones destructivas | Complementaria | — | Misma página; amplía la protección |
| CPE-001 | Apariencia | Acción y superficies | Esencial | — | Colores de la acción principal |
| CPE-002 | Foco | 21 Operación | Trazabilidad | — | El anillo ya está descrito |
| CPE-003 | Irreversible y crítica | 19 Procesos críticos | Complementaria | — | Procesos críticos |
| CPE-004 | Qué va en el menú | Navegación visible | Trazabilidad | — | La oración ya dice la decisión |
| CPE-005 | Mensaje de error | Validación útil | Complementaria | — | Misma página |
| CPE-006 | Redacción | 24 Mensajes | Complementaria | — | Redacción del mensaje |
| CPE-008 | Pestañas | Identificación de controles | Esencial | — | Patrón de teclado de las pestañas |
| CPE-008 | Diálogo | Diálogos | Trazabilidad | — | Misma página; la celda se entiende sola |
| CPE-012 | Redacción | 24 Mensajes | Complementaria | — | Redacción del mensaje |
| PAT-001 | Decisión | Estados de los controles | Esencial | — | Estados del botón al enviar |
| PAT-001 | Decisión | Terminación clara | Complementaria | Sí | El paso queda sin contenido propio; la oración existe para remitir |
| PAT-001 | Cuándo | 17 Flujos de trabajo | Complementaria | Sí | La oración existe para remitir |
| PAT-003 | Momento | Validación útil | Esencial | — | Fuente principal de cuándo se valida (propuesta: CPE-006) |
| PAT-004 | Retroceder | Contexto conservado | Trazabilidad | — | La celda ya dice el comportamiento |
| PAT-006 | Eliminar | Acciones destructivas | Esencial | Sí | Niveles de protección; la oración existe para remitir |
| PAT-007 | Permiso | Enlaces directos y rutas no disponibles | Complementaria | — | Comportamiento sin permiso |
| PAT-007 | Datos inválidos | Validación útil | Complementaria | — | Validación del campo |
| PAT-010 | Vacío por filtros | Búsquedas sin resultados | Complementaria | — | Estado vacío por filtros |
| PAT-010 | Espera larga | Resultado visible | Complementaria | — | Estado de espera |
| PAT-011 | Confirmación | Acciones destructivas | Esencial | — | Niveles de confirmación |
| PAT-011 | Intervención humana | 32 Agentes | Complementaria | — | Aprobación de acciones automatizadas |
| ACC-001 | Declaración | 44 Validación | Complementaria | — | Procedimiento de validación |
| ACC-002 | Gráfico de datos | 27 Gráficos | Complementaria | — | Accesibilidad de gráficos |
| ACC-002 | Color con significado | Estados semánticos | Trazabilidad | — | La celda ya dice la señal |
| ACC-003 | Desarrollo | 09 Tipografía | Complementaria | Sí | La fila existe para remitir |
| ACC-005 | Indicador | Contraste | Complementaria | — | Decisión pendiente |
| ACC-006 | Límites de tiempo | Prevención de pérdidas | Complementaria | — | Conservación de datos |
| ACC-006 | Animaciones | 39 Operación activa | Trazabilidad | — | La celda ya dice la preferencia |
| ACC-007 | Cómo se reorganiza | 10 Espacio y retícula | Complementaria | Sí | La fila solo remite y no dice cómo se reorganiza |
| ACC-007 | Cómo se reorganiza | 05 Navegación | Complementaria | Sí | Ídem |
| ACC-009 | Capacidades | Diseñar para quienes utilizan el producto | Trazabilidad | — | La celda ya nombra los perfiles |
| CNT-001 | Voz | Esencia de la voz | Esencial | Sí | La voz se aplica al escribir; la oración repite el nombre |
| CNT-002 | Navegación | 04 Información | Complementaria | Sí | La fila existe para remitir |
| CNT-003 | Ayudas | Información progresiva | Trazabilidad | — | La celda ya dice la decisión |
| CNT-006 | Permisos | 05 Navegación | Complementaria | Sí | La fila es «Ver…» |
| CNT-006 | Permisos | 06 Búsqueda | Complementaria | Sí | La fila es «Ver…» |
| CNT-008 | Glosario por idioma | Consistencia | Trazabilidad | — | La oración ya dice la decisión |
| DAV-001 | Texto | Truncamiento | Esencial | Sí | Cómo se trunca; la fila casi no tiene contenido propio |
| DAV-001 | Estados | Estados semánticos | Trazabilidad | — | La celda ya dice la señal |
| DAV-002 | Conservación | 05 Navegación | Complementaria | — | Conservación al volver |
| DAV-002 | Filtros activos | 06 Búsqueda | Complementaria | — | Filtros visibles |
| DAV-003 | Dónde van | Menú de acciones | Complementaria | — | La celda ya dice dónde van |
| DAV-003 | Permisos | Roles y permisos | Trazabilidad | — | La celda ya dice la decisión |
| DAV-007 | Dibujo de cada tipo | Tipos de gráfico | Esencial | — | Dibujo de cada gráfico |
| DAV-008 | Fuente única | Sistema cromático | Esencial | — | Paletas de datos |
| DAV-011 | Señal | Estados semánticos | Trazabilidad | — | La celda ya dice la señal |
| DAV-004 | Punto de partida | Diseñar para quienes utilizan el producto | Trazabilidad | — | La celda ya dice el punto de partida |
| DAV-004 | Cada indicador | 28 Indicadores | Complementaria | — | Indicadores |
| DAV-005 | Tercero | 27 Gráficos | Trazabilidad | — | La celda ya dice la decisión |
| IAE-002 | Señal | Estados semánticos | Trazabilidad | — | La celda ya dice la señal |
| IAE-003 | Alto o irreversible | Autorización | Complementaria | — | Autorización |
| IAE-005 | Personalidad | Origen y personalidad | Complementaria | — | Personalidad de Estela |
| IAE-006 | Límites | Voz y trato | Complementaria | — | Voz de Estela |
| IAE-007 | Estado | Estado comprensible | Trazabilidad | — | La celda ya nombra los estados |
| IAE-007 | Registro | Trazabilidad | Trazabilidad | — | La celda ya dice la decisión |
| IAE-008 | Permisos | Roles y permisos | Trazabilidad | — | La celda ya dice la decisión |
| IAE-008 | Aprobación | Control humano | Complementaria | — | Control humano |
| IAE-009 | Identidad | Identidad visual y expresión | Esencial | — | Identidad visual de Estela |
| IAE-010 | Definición | Incertidumbre | Complementaria | — | Niveles de incertidumbre |
| SPR-005 | Biblioteca | Cambios controlados | Complementaria | — | Cambios controlados |
| SPR-006 | Registro | Decisiones justificadas | Trazabilidad | — | La celda ya dice la decisión |
| SPR-007 | Dependencias | Cambios controlados | Esencial | — | La verificación es el procedimiento de otra norma |
| SPR-008 | Navegación | 05 Navegación | Complementaria | — | Reglas de navegación |
| SPR-008 | Identidad | Principios | Complementaria | — | Principios de marca |
| SPR-010 | Densidad | Uso ocasional y frecuente | Trazabilidad | — | La celda ya dice la decisión |
| SPR-011 | Roles | Roles y permisos | Complementaria | — | Roles y permisos |
| SPR-001 | Qué incluye | Navegación predeterminada | Trazabilidad | — | Misma página |
| SPR-002 | Bienvenida y estados vacíos | Momentos vivos | Esencial | — | Dónde se permite la expresión |
| SPR-003 | Color | Contraste | Complementaria | — | Contraste |
| SPR-004 | Por qué aquí | 05 Navegación | Trazabilidad | — | Nota de origen |
| SPR-012 | Límites | Personalización controlada | Esencial | — | Límites de la personalización |
| SPR-014 | Alcance | Modelo C · Marca blanca | Esencial | — | Modelo de marca blanca |
| MOV-002 | Preferencia | Tiempo y movimiento | Esencial | — | Duraciones con movimiento reducido |
| MOV-003 | Identidad | Animación | Esencial | — | Movimiento de marca |
| GOB-007 | Registro | Decisiones justificadas | Trazabilidad | — | La celda ya dice qué se registra |
| GOB-008 | Pruebas | Estados de los controles | Complementaria | — | Estados de los controles |
| GOB-008 | Pruebas | Componentes documentados | Esencial | — | La verificación es el procedimiento de otra norma |
| GOB-001 | Tareas | Diseñar para quienes utilizan el producto | Trazabilidad | — | La celda ya dice la decisión |
| GOB-001 | Evidencia | 03 Elecciones verificadas | Complementaria | — | Evidencia diferenciada |
| GOB-002 | Quién decide | 42 Gobierno normativo | Complementaria | — | Responsables, todavía sin definir |
| GOB-003 | Evidencia | 20 Percepción | Complementaria | — | Criterios de accesibilidad |
| GOB-003 | Evidencia | 22 Adaptación | Complementaria | — | Ídem |
