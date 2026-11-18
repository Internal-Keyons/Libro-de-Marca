# Composición normativa según el contenido · 17 de noviembre de 2026 · borrador

**Rama:** `biblioteca-p1-p4`.
- No se publicó en `main` ni se ejecutaron exportaciones.
- Las 151 normas siguen en borrador y ningún capítulo se declara terminado.

## 1 · Qué cambió

### Reglas publicadas (fuente única: Guía 05)

**Nuevo bloque «Composición normativa según el contenido»:**
- lleva su texto en siete filas con nivel: Jerarquía, Integración, Títulos, Apartados complementarios, Verificación (Debe y Puede) y Sin relleno;
- única modificación, aprobada con el plan: «No deben depender de metáforas…» se unió a la oración anterior («…sin depender de metáforas…»), para que ninguna oración empiece con «No».

**«Sistema de diagramación»:** las filas «Marcadores» y «Serie o detalle» dicen ahora que los acordeones van sin número.

**Referencias sin copiar:**
- `CLAUDE.md` remite a los dos bloques.
- `reglas-visuales.md` actualiza R27 (sin número) y 1.8 (atardeceres en todos los libros).
- `tools/sd/base.py` cita la Guía.

### Acordeones sin número (todos los libros)

- **Libro de Marca:** ADN-006 (Cinco promesas), Estela 5.3 (escenarios), Paleta base 6.x y Gráficos 11.x.
- **Sistema de Diseño:** todas las series.
- **Cómo se ve:** el título empieza donde antes estaba el número y el cuerpo se alinea con él, a 600 px.
- **Lo que se borró:** el token `--promise-n` y las reglas de `.promise__n`.

### Subencabezados de atardecer

**Las reglas de Prisma y del atardecer tenue pasaron de `marca.css` a `libro.css`,** así que cualquier libro las hereda.

**En el Sistema de Diseño** el color de cada módulo sale del ciclo de áreas de `tools/sistema_diseno.py`:

| Color del módulo | Módulos | Encabezado |
| --- | --- | --- |
| Salmón Tierra | Fundamentos, Contenido y Movimiento | Atardecer de Prisma animado |
| Salmón Atardecer | Componentes, Datos y Gobierno | Atardecer tenue animado |
| Azul Noche y Azul Cielo | Los demás | Plano, como antes |

**Comprobación:**
- El encabezado de Corporativo sigue igual; ver la captura 09.
- La trama cuadriculada del Sistema de Diseño es su estilo propio y se conserva.

### Generador del Sistema de Diseño (`tools/sd/base.py` y `tools/sd_capitulos.py`)

**`dims()` (dimensiones integradas):**
- cada fila reúne el requisito de su dimensión, en Azul Noche y con su nivel, y su decisión de aplicación, en gris de lectura;
- reemplaza el par «lista de requisitos + filas que los repiten».

**La verificación es parte de la norma** (rótulo, condición, resultado esperado). Se presenta según su función:

| Presentación | Normas | Componente |
| --- | --- | --- |
| Nota breve | 73 | Nota de cierre con rótulo «Verificación» (`.ed__more`) |
| Plegable técnico | 29 | Detalle plegable simple «Verificación» |
| Validación del capítulo | 46 | Sección final del capítulo; tabla solo con tres pruebas o más |
| Referencia | 3 | Remite a la norma que define la prueba |

- Nada más se agrega un plegable «Verificación» por inercia.
- La fuente única de las verificaciones son los módulos `tools/sd/m*.py`; `data/sd-normas.json` las recibe al generar.

**`R()` (referencias directas):**
- llevan al ancla exacta de la norma citada, con su nombre y el capítulo;
- una referencia sin destino detiene la generación;
- en la página no aparece «pendiente»: lo no desarrollado queda en la matriz de cobertura;
- se cambiaron todos los códigos sueltos, como «(PEX-015)», por enlaces.

**Controles:**
- `simple()` dejó de agregar el plegable de verificación.
- `tools/verificar.py` comprueba la verificación en el registro.

### Control editorial nuevo (`tools/sd_revisar.py`, solo lectura)

**Errores comprobables:**
- verificación sin condición y resultado;
- requisito repetido en otra fila o en otra norma;
- registro distinto de la página;
- código o ancla perdidos;
- referencias sin resolver o códigos sueltos;
- plegable de Verificación fuera de lugar.

**Para revisión humana:**
- titulares con forma de frase;
- verificaciones parecidas al requisito;
- requisitos parecidos entre normas;
- «Casos límite» y capítulos con una sola forma de verificación.

**Resultado:** ningún titular está prohibido y el detector nunca cambia texto. Termina con **0 errores**. Los 13 avisos revisados quedaron justificados en `tools/sd/revision-justificada.json`.

## 2 · Cambios editoriales

**PEX-001** pasó a tres dimensiones con su requisito y su decisión:
- **Propósito:** Debe, con la decisión sobre el título.
- **Acción principal:** Debe, con enlace a Jerarquía de acciones.
- **Recursos gráficos:** No debe, con enlace a Expresión proporcionada.

«Casos límite» pasó a **«Aplicación según el contexto»** (consulta, varias tareas y paneles). Su verificación es una nota breve con dos condiciones.

**Los 151 titulares son directos:**
- los cinco que usted indicó, tal cual;
- los demás nombran el comportamiento, el componente o la decisión;
- la tabla completa está en el anexo A.

**Las entradas** dicen qué regula la norma y cuándo se aplica, con una frase destacada, sin repetir el titular.

**Integraciones** («dimensiones») en PEX-001, PEX-008, PEX-009, PEX-012, ARQ-001, ARQ-004, ARQ-005, ARQ-006, ARQ-008, CPE-004 y PAT-005:
- en PEX-008 la tabla de «acción sin permiso» quedó dentro de sus tres dimensiones;
- en PEX-009 la tabla ocasional y frecuente quedó dentro de sus tres requisitos.

**Repeticiones quitadas:**
- PEX-003 «Perfiles», que repetía PEX-009;
- PEX-010 «Registro», que repetía la ficha de decisión;
- PEX-008, la fila del servidor que repetía el requisito.

**Ejemplos SaaS** nuevos donde la decisión era abstracta:
- PEX-003, listado con acciones por fila y menú;
- PEX-006, eliminar 12 facturas;
- PEX-009, tabla para la administración y lista para el residente;
- ARQ-004, factura con desglose a pedido;
- los ejemplos de capítulo 09 y 10.

Ninguno se presenta como comportamiento comprobado de Pinar de Río: no hay registro de comportamientos verificados en el proyecto.

**Verificaciones reescritas** como condición y resultado esperado, sin repetir el requisito.

**Redacción:** se cortaron las oraciones de más de 25 palabras y se cambió «No se muestran errores» por «Sin mensajes de error».

## 3 · Revisión editorial completa de dos capítulos

### 01 Principios comunes (Experiencia)

- **Títulos:** antes eran frases interpretables; ahora nombran la responsabilidad. «Cancelar, deshacer y decidir» queda como verbo en plural porque nombra tres capacidades concretas.
- **Secuencia:** propósito → patrones → controles → estado → consistencia → consecuencias → prevención → control → memoria. Sigue el orden en que una persona usa una pantalla.
- **Repeticiones:** PEX-001 ya no repite sus requisitos y PEX-003 ya no repite PEX-009.
- **Jerarquía:** el requisito va en Azul Noche y su decisión en gris; las tablas solo donde se compara.
- **Composiciones:**
  - dimensiones en PEX-001;
  - tabla en PEX-004;
  - filas en las de un solo requisito.
- **Ejemplos:** PEX-003 y PEX-006.
- **Verificaciones:**
  - cuatro normas (PEX-004, 006, 016 y 017) se prueban en una sola sesión con las acciones principales, por eso van juntas en «Validación del capítulo»;
  - las demás llevan una nota breve.
- **Pendiente:** PEX-016, 017 y 018 siguen con requisitos redactados por Claude, a la espera de su aprobación.

### 05 Navegación (Arquitectura)

- **Títulos:** «Ubicación y sección activa», «Nombres, destinos y comportamientos estables», «Enlaces directos y rutas no disponibles»…
- **Secuencia:** dónde estoy → qué significa cada destino → qué se ve → cómo se anuncia → cómo se adapta → cómo vuelvo → cómo entro directo.
- **Repeticiones:** ARQ-005, 006 y 008 integraron sus requisitos en dimensiones. ARQ-008 conserva la tabla de patrones ARIA porque compara construcción y anuncio.
- **Apartados:** solo donde resuelven algo.
  - «Casos límite» queda solo en ARQ-010, por un registro eliminado o una sesión nueva al volver.
  - Las excepciones de ARQ-005 se llaman «Pantallas sin navegación general».
- **Verificaciones:** son técnicas (teclado, lector de pantalla, rutas), así que van en el plegable técnico; ARQ-006 lleva una nota breve.
- **Coherencia con la Biblioteca:** el mismo ancho de lectura, el detalle plegable simple y el enlace directo a las normas citadas (Jerarquía de acciones, Navegación predeterminada, Interacciones accesibles).

## 4 · Duplicaciones entre normas (consolidación propuesta, códigos conservados)

| Relación | Fuente principal | Cómo quedan las demás | Propuesta para su aprobación |
| --- | --- | --- | --- |
| Principios y componentes | PEX-004 (estado) | CPE-011 desarrolla los componentes y CNT-005 la redacción de la confirmación; PEX-004 los enlaza en su tabla | Ninguna: cada una cubre una capa distinta |
| Información y navegación | ARQ-002 (nombres) | ARQ-006 remite a ARQ-002 para la redacción | Ninguna |
| Estados y retroalimentación | PEX-004 | CPE-011 y PAT-010 (espera) enlazados | Ninguna |
| Errores, mensajes y recuperación | CNT-004 (texto del error) | CPE-006 (campo) y PAT-007 (salida) lo enlazan | Unir CPE-006 «Cuándo se valida» con PAT-003: hoy ambos regulan el momento de la validación |
| Accesibilidad y componentes | ACC-003 (ampliación y ajustes) | FUI-010 repite la misma prueba de 200 %, 320 px y espaciado | Que FUI-010 cite ACC-003 y conserve solo la escala tipográfica |
| Color y estados semánticos | FUI-005 | CPE-002, ACC-002, DAV-001 y DAV-009 lo enlazan | Ninguna |
| Control de la persona | PEX-017 | PAT-008 desarrolla deshacer | Ninguna; PEX-017 enlaza a PAT-008 |
| Consecuencias | PEX-006 | CPE-003 define los niveles de protección; PAT-011 la autorización | Ninguna |

Los dos casos marcados repiten requisitos escritos por usted. Por eso solo los propongo y no los cambié.

## 5 · Pruebas y resultados

| Prueba | Resultado |
| --- | --- |
| `tools/verificar.py` | 0 errores |
| `tools/sd_revisar.py` | 0 errores; 13 avisos revisados y justificados |
| Redacción (oraciones con «No» al inicio y de más de 25 palabras) | Ninguna en los textos redactados por Claude |
| Líneas dobles (`lineas-dobles.js`, todo el Sistema de Diseño) | `{}` (ninguna) |
| Etiquetas del menú (`menu-etiquetas.js`) | `[]` |
| Desborde a 375 px (45 capítulos y las páginas de Marca con acordeón) | Ninguno tras permitir que un enlace se parta dentro de una celda de tabla (`.matrix .xref`) |
| Códigos y anclas frente al último commit | Todos conservados |
| Tablas en móvil | Conservan dos columnas con el rótulo de fila encima: la relación se lee igual |
| Lector de pantalla real (NVDA o VoiceOver) | **Sin hacer**: no hay uno disponible en este equipo |

**Prueba de patrones** (normas de distinta complejidad, en escritorio y móvil):

| Tipo de norma | Norma | Captura |
| --- | --- | --- |
| Breve | SPR-006 | `hoja-base-compartida-*` |
| Con varios requisitos | PEX-001 | `01-pex-001-dimensiones` y `hoja-principios-compartidos-*` |
| Con tabla | PEX-004 | `03-pex-004-estado` |
| Con secuencia | PEX-011 | `10-pex-011-secuencia` |
| Con excepciones | CPE-003 | `07-cpe-003-norma-con-excepciones` |
| Con verificación técnica extensa | ACC-005 | `11-acc-005-verificacion-tecnica` |

**Capturas:** `propuestas/capturas-sd-composicion/`, tomadas sin foco.

## 6 · Cobertura real

| Cobertura | Normas | Criterio |
| --- | --- | --- |
| Desarrollada | 77 | Responde las cinco preguntas de control con una composición propia (tabla, secuencia, dimensiones o varias decisiones) y una verificación con condición y resultado |
| Parcial | 46 | Requisito, decisiones breves y verificación; faltan comportamientos o casos. Incluye las normas breves del Bloque 4 (34 a 45) |
| Pendiente | 14 | Depende de algo sin definir: glosarios, idiomas, niveles de confianza y de supervisión, tokens de curva, roles de aprobación, hoja de componentes… |
| Requiere aprobación | 14 | Requisitos redactados por Claude o propuestas dentro del texto |

**Límites del criterio:** «desarrollada» es contenido suficiente para tomar decisiones de diseño e implementación, no un capítulo terminado. Ningún capítulo se declara completo. La tabla por norma está en el anexo B.

## 7 · Decisiones que necesitan su aprobación

1. **Los requisitos redactados por Claude:** PEX-016 a 018, ARQ-017, CPE-004, PAT-010, SPR-004, GOB-003 y la reescritura de ACC-001.
2. **Las dos consolidaciones del punto 4:** CPE-006 con PAT-003, y FUI-010 con ACC-003.
3. **El color del foco:** `--color-focus` Azul Cielo da 2,6:1; propongo Azul Noche.
4. **El token de acción:** `--color-action` y `--color-on-action`.
5. **La preferencia táctil Keyons de 44 × 44 px.**
6. **Las propuestas marcadas:** escala tipográfica por uso, espacios por uso y prioridad entre criterios (PEX-002).
7. **Los titulares y las entradas nuevos,** redactados por Claude (anexo A).

## 8 · Páginas para revisar en pantalla

- **Guía de la Biblioteca 05:** bloques «Sistema de diagramación» y «Composición normativa según el contenido».
- **Marca:** ADN-006, Estela 5.3, Paleta base y Gráficos (acordeones sin número); Corporativo (encabezado sin cambios).
- **Sistema de Diseño:**
  - 01 Principios comunes, con PEX-001, PEX-003, PEX-004 y «Validación del capítulo»;
  - 05 Navegación;
  - 13 Entradas, con la tabla de validación;
  - 07 Tokens y 12 Acciones, con los encabezados de atardecer;
  - 34 Base compartida, la norma breve.

**Si algo «no se aplicó»:** recargue con Ctrl + F5. En la vista previa, la hoja de estilos anterior quedó en caché.

## Archivos

- **Generadores:**
  - `tools/sd/base.py`;
  - `tools/sd_capitulos.py`;
  - `tools/sd/m01_experiencia.py`, `m02_arquitectura.py`, `m02b_informacion_busqueda.py`, `m03_fundamentos.py`, `m03b_recursos_componentes.py`, `m04_componentes.py`, `m05_patrones.py`, `m06_accesibilidad.py`, `m07_contenido.py`, `m08_datos.py`, `m09_ia_estela.py`, `m10_productos.py`, `m10b_productos_movimiento_gobierno.py` y `m12_gobierno.py`;
  - `tools/estela.py`;
  - `tools/sistema_diseno.py`.
- **Control:**
  - `tools/sd_revisar.py` (nuevo);
  - `tools/sd/revision-justificada.json` (nuevo);
  - `tools/verificar.py`.
- **Estilos:**
  - `css/libro.css`;
  - `css/marca.css`;
  - `css/tokens.css`;
  - `css/sistema-diseno.css`.
- **Reglas:**
  - `data/gobierno.json` (Guía 05);
  - `reglas-visuales.md`;
  - `CLAUDE.md`.
- **Páginas a mano:** `marca/adn.html`, `fundamentos/color/paleta-base.html` y `fundamentos/elementos/graficos.html`.
- **Regenerados:**
  - `data/sd-capitulos/*`;
  - `data/sd-normas.json`;
  - `data/sistema-diseno.json`;
  - las páginas del Sistema de Diseño;
  - `marca/estela.html`;
  - `guia/index.html`;
  - el buscador.

## Anexo A · Titulares (antes y después)

| Código | Cap. | Titular anterior | Titular nuevo |
| --- | --- | --- | --- |
| PEX-001 | 01 | Cada pantalla deja claro para qué está | Propósito y prioridad de la pantalla |
| PEX-002 | 01 | Lo conocido se usa sin aprenderlo de nuevo | Patrones de interacción conocidos |
| PEX-003 | 01 | Cada control visible tiene una razón | Controles pertinentes a la tarea |
| PEX-004 | 01 | La persona sabe qué pasó con lo que hizo | Comunicar el estado de cada acción |
| PEX-005 | 01 | Lo que funciona igual se aprende una vez | Comportamientos consistentes entre pantallas |
| PEX-006 | 01 | Antes de confirmar, la persona ve qué va a cambiar | Consecuencias visibles antes de confirmar |
| PEX-016 | 01 | La interfaz evita el error antes de corregirlo | Prevención de errores frecuentes |
| PEX-017 | 01 | La persona puede detener, deshacer y decidir | Cancelar, deshacer y decidir |
| PEX-018 | 01 | La interfaz muestra lo que la persona tendría que recordar | Opciones y datos previos a la vista |
| PEX-007 | 02 | El diseño parte de quien opera el producto | Perfiles operativos como base del diseño |
| PEX-008 | 02 | Cada rol encuentra lo que le corresponde | Acciones y datos según el rol |
| PEX-009 | 02 | La experiencia se ajusta a la frecuencia de uso | Densidad y ayudas según la frecuencia de uso |
| PEX-010 | 03 | Cada decisión responde a un problema | Registro de decisiones de diseño |
| PEX-011 | 03 | Los proyectos siguen las cinco fases de Prisma | Fases de Prisma y sus entregables |
| PEX-012 | 03 | La interfaz se construye por capas | Estructura, interacción y expresión por capas |
| PEX-013 | 03 | Una propuesta se aprueba por lo que logra | Aprobación por resultados de uso |
| PEX-014 | 03 | Se distingue lo observado de lo supuesto | Observaciones, hipótesis y decisiones diferenciadas |
| PEX-015 | 03 | Los cambios se comprueban donde actúan | Evaluación de cambios antes de extenderlos |
| ARQ-001 | 04 | El contenido se agrupa como lo piensan las personas | Agrupación del contenido por tareas |
| ARQ-002 | 04 | Cada sección se nombra como la reconoce la persona | Nombres reconocibles para secciones y destinos |
| ARQ-003 | 04 | Se distingue lo principal de lo complementario | Información principal, secundaria y complementaria |
| ARQ-004 | 04 | Lo esencial a la vista; el detalle, a pedido | Información esencial y detalle progresivo |
| ARQ-005 | 05 | La persona sabe dónde está y cómo seguir | Ubicación y sección activa |
| ARQ-006 | 05 | Cada destino conserva su sentido y su lugar | Nombres, destinos y comportamientos estables |
| ARQ-007 | 05 | Toda función necesaria tiene una señal a la vista | Señales visibles para cada función |
| ARQ-008 | 05 | Cada control dice qué hace y en qué estado está | Función y estado de los controles de navegación |
| ARQ-009 | 05 | La presentación cambia; los destinos se reconocen | Navegación adaptable por dispositivo |
| ARQ-010 | 05 | Volver a una lista devuelve el trabajo donde quedó | Listados que conservan su estado al volver |
| ARQ-017 | 05 | Cada dirección lleva a un destino o a una salida | Enlaces directos y rutas no disponibles |
| ARQ-011 | 06 | Se sabe dónde busca la búsqueda | Alcance de la búsqueda |
| ARQ-012 | 06 | La búsqueda encuentra lo que la tarea necesita | Campos y orden de los resultados |
| ARQ-013 | 06 | Cada resultado se distingue de los parecidos | Datos que distinguen cada resultado |
| ARQ-014 | 06 | Los filtros activos están a la vista | Filtros activos a la vista |
| ARQ-015 | 06 | Una búsqueda vacía explica qué pasó y cómo seguir | Búsquedas sin resultados |
| ARQ-016 | 06 | La búsqueda solo muestra lo que la persona puede ver | Resultados según permisos |
| FUI-001 | 07 | Cada valor compartido vive en un token | Tokens para todo valor compartido |
| FUI-002 | 07 | El token dice para qué sirve, no qué color es | Tokens nombrados por su función |
| FUI-003 | 07 | Un token compartido se cambia con su revisión | Revisión de cambios en tokens compartidos |
| FUI-004 | 08 | Cada color de la interfaz cumple una función | Función de cada color en la interfaz |
| FUI-005 | 08 | Cada estado se reconoce sin depender del color | Estados con color y señal adicional |
| FUI-006 | 08 | El error tiene su propio color | Salmón Tierra y el color de error |
| FUI-007 | 08 | Cada combinación se lee y se distingue | Contraste mínimo de las combinaciones |
| FUI-008 | 09 | La interfaz usa la tipografía oficial | Familias, pesos y escala tipográfica |
| FUI-009 | 09 | Cada función de texto se reconoce siempre igual | Jerarquía de las funciones de texto |
| FUI-010 | 09 | El texto se lee con ampliación y en cualquier pantalla | Legibilidad con ampliación y espaciado |
| FUI-011 | 09 | Un texto acortado sigue disponible completo | Textos truncados y su valor completo |
| FUI-012 | 10 | Los espacios salen de la escala oficial | Escala espacial de los componentes |
| FUI-013 | 10 | Lo que está cerca está relacionado | Proximidad según la relación funcional |
| FUI-014 | 10 | La retícula se reorganiza sin perder nada | Retícula adaptable, densidad y esquinas |
| FUI-015 | 11 | Cada ícono cumple una función | Función de cada ícono |
| FUI-016 | 11 | Los recursos gráficos siguen las normas de la marca | Recursos gráficos según la marca |
| FUI-017 | 11 | Lo expresivo acompaña sin competir | Recursos expresivos subordinados a la tarea |
| CPE-001 | 12 | Cada grupo de decisión tiene una acción principal | Acción principal, secundaria y destructiva |
| CPE-002 | 12 | Cada control muestra en qué estado está | Estados de los controles interactivos |
| CPE-003 | 12 | La protección crece con el riesgo | Protección de las acciones destructivas |
| CPE-004 | 12 | Las acciones ocasionales se agrupan en un menú | Menú de acciones ocasionales |
| CPE-005 | 13 | Cada campo dice qué pide | Etiqueta, ayuda y error de cada campo |
| CPE-006 | 13 | El error dice dónde está y cómo corregirlo | Mensajes de error en los campos |
| CPE-007 | 13 | Cada dato usa el control que le corresponde | Control según el tipo de dato |
| CPE-008 | 14 | Cada contenedor existe por una razón | Paneles, pestañas, acordeones y diálogos |
| CPE-009 | 14 | El contenido no se fragmenta sin motivo | Contenedores necesarios |
| CPE-010 | 14 | Un diálogo dice para qué es y cómo salir | Propósito, acciones y salida de los diálogos |
| CPE-011 | 15 | Cada cambio muestra su resultado | Componentes de respuesta a una acción |
| CPE-012 | 15 | La respuesta dice lo que realmente pasó | Mensajes que explican lo ocurrido |
| CPE-013 | 15 | Cada aviso pide la atención que merece | Niveles de urgencia de las notificaciones |
| PAT-001 | 16 | El formulario sigue el orden del proceso real | Orden y agrupación de los formularios |
| PAT-002 | 16 | Lo escrito no se pierde por un accidente | Protección de lo escrito |
| PAT-003 | 16 | La validación ayuda sin interrumpir | Validación sin interrupciones |
| PAT-004 | 17 | La persona sabe en qué paso está y qué falta | Avance de los procesos de varios pasos |
| PAT-005 | 17 | Volver atrás no borra lo decidido | Decisiones conservadas al retroceder |
| PAT-006 | 17 | Al terminar, la persona sabe qué pasó y adónde ir | Resultado y siguiente paso al terminar |
| PAT-007 | 18 | Ante un error, siempre hay un camino | Salida ante errores que impiden continuar |
| PAT-008 | 18 | Lo que se puede deshacer, se ofrece deshacer | Deshacer y restaurar |
| PAT-009 | 18 | Un fallo no borra lo que estaba bien | Datos válidos que sobreviven a un fallo |
| PAT-010 | 18 | Un vacío y una espera también orientan | Estados vacíos y de espera |
| PAT-011 | 19 | Cada operación crítica comprueba quién puede hacerla | Autorización y confirmación de operaciones críticas |
| PAT-012 | 19 | Una operación crítica deja su registro | Registro de operaciones críticas |
| ACC-001 | 20 | WCAG 2.2 AA es el mínimo de todo producto web | WCAG 2.2 AA como referencia de conformidad |
| ACC-002 | 20 | El significado llega por más de un sentido | Alternativas para cada recurso sensorial |
| ACC-003 | 20 | La interfaz resiste la ampliación y los ajustes de texto | Ampliación y ajustes de presentación |
| ACC-004 | 21 | Todo lo que se hace con el puntero se hace con el teclado | Uso completo con teclado |
| ACC-005 | 21 | Siempre se ve dónde está el foco | Indicador de foco visible |
| ACC-006 | 21 | La persona controla el tiempo y el movimiento | Límites de tiempo y movimiento |
| ACC-007 | 22 | Cada pantalla funciona en cualquier tamaño | Funciones completas en cualquier ancho |
| ACC-008 | 22 | Cada objetivo se toca sin errores | Tamaño y separación de los objetivos |
| ACC-009 | 22 | El producto considera cómo y dónde se usa | Dispositivos, entradas y condiciones de uso |
| CNT-001 | 23 | Cada texto dice qué se puede hacer y qué pasará | Instrucciones y etiquetas claras |
| CNT-002 | 23 | Una acción, un nombre | Un nombre por acción y concepto |
| CNT-003 | 23 | Lo justo para comprender | Extensión de los textos de interfaz |
| CNT-004 | 24 | Un error dice qué pasó y cómo seguir | Mensajes de error |
| CNT-005 | 24 | Una confirmación dice lo que de verdad ocurrió | Mensajes de éxito |
| CNT-006 | 24 | Un mensaje no revela lo que no corresponde | Información técnica y datos restringidos en mensajes |
| CNT-007 | 25 | Cada idioma con sus formatos | Idioma, formatos y unidades |
| CNT-008 | 25 | La traducción conserva la función | Traducciones que conservan la función |
| CNT-009 | 25 | Los componentes aceptan textos más largos | Componentes que admiten textos más largos |
| DAV-001 | 26 | Una tabla se lee por filas y se compara por columnas | Encabezados, alineación y lectura de tablas |
| DAV-002 | 26 | Buscar, filtrar, ordenar y paginar cuando hace falta | Búsqueda, filtros, orden y paginación de tablas |
| DAV-003 | 26 | Las acciones de cada fila se distinguen de sus datos | Acciones por registro |
| DAV-007 | 27 | Cada relación tiene su gráfico | Tipo de gráfico según la relación |
| DAV-008 | 27 | Las paletas siguen la naturaleza de los datos | Paletas según la naturaleza de los datos |
| DAV-009 | 27 | Un gráfico se entiende sin el color | Gráficos legibles sin depender del color |
| DAV-010 | 28 | Cada indicador dice qué mide | Significado, unidad y período de cada indicador |
| DAV-011 | 28 | Los umbrales responden a criterios definidos | Criterios de los umbrales |
| DAV-012 | 28 | Se sabe cuándo se actualizó el dato | Fecha de actualización de los datos |
| DAV-004 | 29 | El tablero responde a las decisiones de quien lo usa | Tableros según las decisiones de quien los usa |
| DAV-005 | 29 | No todos los indicadores pesan lo mismo | Jerarquía de los indicadores |
| DAV-006 | 29 | Del resumen al detalle, sin perder el contexto | Del resumen al detalle |
| IAE-001 | 30 | Se distingue lo que hizo la IA | Contenido y acciones generados por IA |
| IAE-002 | 30 | Lo no verificado no se presenta como cierto | Información generada no verificada |
| IAE-003 | 30 | La supervisión crece con el riesgo | Supervisión según el riesgo |
| IAE-004 | 31 | La conversación recuerda lo necesario | Contexto de la conversación |
| IAE-005 | 31 | Estela pregunta solo lo que necesita | Preguntas de Estela |
| IAE-006 | 31 | Se distingue informar, recomendar y hacer | Información, recomendación y acción en las respuestas |
| IAE-007 | 32 | Se ve qué hace un agente y con qué resultado | Acciones visibles de los agentes |
| IAE-008 | 32 | Un agente actúa solo dentro de sus permisos | Permisos de los agentes |
| IAE-009 | 32 | Estela es la cara de las capacidades coordinadas | Estela como identidad pública |
| IAE-010 | 33 | Cada nivel de confianza significa lo que dice | Indicadores de confianza calibrados |
| IAE-011 | 33 | Para aprobar, la información a la vista | Información para aprobar |
| IAE-012 | 33 | La IA no revela lo de otras personas | Privacidad entre personas en la IA |
| SPR-005 | 34 | Los productos reutilizan lo que ya funciona | Reutilización de componentes, tokens y patrones |
| SPR-006 | 34 | Cada diferencia entre productos tiene una razón | Diferencias justificadas entre productos |
| SPR-007 | 34 | Un cambio compartido se prueba en todos | Pruebas de los cambios compartidos |
| SPR-008 | 35 | El sitio lleva a la información y a la acción | Información y acciones del sitio web |
| SPR-009 | 35 | Los formularios del sitio siguen las normas | Formularios y controles del sitio web |
| SPR-010 | 36 | Lo frecuente, en menos pasos | Eficiencia de las herramientas internas |
| SPR-011 | 36 | Cada operador ve lo de su rol | Funciones según el rol del operador |
| SPR-001 | 37 | Product Default parte de los componentes canónicos | Componentes canónicos en Product Default |
| SPR-002 | 37 | Lo frecuente se ve contenido y claro | Superficies contenidas para el uso frecuente |
| SPR-003 | 37 | Lo que se personaliza no rompe lo que funciona | Límites de la personalización |
| SPR-004 | 37 | Un patrón de navegación común para los productos SaaS | Patrón de navegación de los productos SaaS |
| SPR-012 | 38 | El cliente puede usar su propia identidad | Identidad del cliente en marca blanca |
| SPR-013 | 38 | Personalizar no rompe lo esencial | Accesibilidad y seguridad con cualquier marca |
| SPR-014 | 38 | Sin firma visible cuando el acuerdo lo pide | Firma Keyons en productos sin autoría visible |
| MOV-001 | 39 | El movimiento explica un cambio | Transiciones que explican un cambio |
| MOV-002 | 39 | El movimiento no hace esperar | Duración del movimiento |
| MOV-003 | 40 | El movimiento editorial acompaña la narrativa | Movimiento editorial con propósito |
| MOV-004 | 40 | Se entiende sin la animación | Información comprensible sin animación |
| MOV-005 | 41 | El sonido no esencial empieza apagado | Sonidos no esenciales |
| MOV-006 | 41 | La vibración confirma cuando aporta | Respuestas hápticas |
| MOV-007 | 41 | Nada importante depende solo del sonido o la vibración | Alternativas visibles al sonido y la vibración |
| GOB-004 | 42 | Cada requisito vive en un solo lugar | Fuente normativa de cada requisito |
| GOB-005 | 42 | Cada norma dice si está vigente | Estado y versión de las normas |
| GOB-006 | 43 | Se implementa con lo compartido | Implementación con componentes canónicos |
| GOB-007 | 43 | Cada desviación se documenta | Registro de excepciones |
| GOB-008 | 43 | Un componente compartido llega con sus pruebas | Pruebas de los componentes compartidos |
| GOB-001 | 44 | Se evalúa con lo que las personas hacen de verdad | Tareas representativas en las evaluaciones |
| GOB-002 | 44 | Un defecto crítico se resuelve o bloquea el lanzamiento | Defectos críticos antes del lanzamiento |
| GOB-003 | 44 | Antes de lanzar, una verificación completa | Protocolo previo al lanzamiento |
| GOB-009 | 45 | Cada componente explica cómo usarlo | Documentación de los componentes canónicos |
| GOB-010 | 45 | Ejemplos que evitan malentendidos | Ejemplos de uso correcto e incorrecto |
| GOB-011 | 45 | Cada cambio relevante deja su rastro | Versiones y notas de cambios |

## Anexo B · Cobertura por norma

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
