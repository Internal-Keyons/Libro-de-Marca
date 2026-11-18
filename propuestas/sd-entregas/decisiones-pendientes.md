# Decisiones pendientes · Sistema de Diseño

Fase A, 2026-11-18. Todo sigue en borrador en `biblioteca-p1-p4`. Este expediente prepara las decisiones y **ninguna se aplicó**: los botones, los colores y los requisitos aprobados quedan como están.

## 1 · Acción principal: comparación y propuesta de tokens

### Lo que existe hoy

| Fuente | Qué dice o qué hace | Dónde |
| --- | --- | --- |
| Regla aprobada | **Producto e interfaz:** acción principal en Azul Cielo con texto Azul Noche (6,5:1). **Piezas de marca** (libro, sitio, presentaciones): Salmón Tierra, una por pantalla. Las demás acciones usan el botón sólido Azul Noche o el de contorno | `reglas-visuales.md` 1.6 (C01) |
| Tabla de variantes | «Principal de producto»: Cielo con texto Noche; al pasar el cursor, Blanco Keyons con borde Cielo, y se endereza. «Principal de marca»: Salmón con texto Noche (P1 pendiente) | `reglas-visuales.md` 4.2 |
| Libro de Marca, página Funcionales | «Cielo para actuar, blanco para apoyar»: los tonos de Azul Cielo PUEDEN usarse para acciones | `fundamentos/color/funcionales.html` 7.16 |
| Código de los libros | Solo existe la principal de marca: `--btn-primary-bg` Salmón, `--btn-primary-fg` Noche | `css/tokens.css:150-151`, `css/libro.css:109, 120` |
| Kit del Laboratorio | `--lab-cta` Salmón y `lx-btn--primary` Salmón, **dentro de interfaces de producto** | `css/laboratorio-kit.css:23-24, 133` |
| Capítulo 12 del Sistema de Diseño | Remite a «Acción y superficies» y propone `--color-action` sin valor | `tools/sd/m04_componentes.py` (CPE-001) |

**Diagnóstico.** La regla aprobada ya separa los dos casos. La contradicción está en la implementación:
- Los libros nunca necesitaron la principal de producto, por eso no existe en el código.
- El kit del Laboratorio usa la principal de marca en interfaces de producto, al revés de lo que manda 1.6.

### Propuesta: tokens funcionales (sin aplicar)

| Token | Valor propuesto | Contraste | Estado |
| --- | --- | --- | --- |
| `--color-action` | `var(--k-cielo)` #729BDD | — | Reposo |
| `--color-on-action` | `var(--k-noche)` | 6,52:1 sobre Cielo | Texto e ícono |
| `--color-action-hover-bg` | `var(--color-bg)` Blanco Keyons | Noche sobre Blanco 16,7:1 | Al pasar el cursor (4.2), con radio 0 |
| `--color-action-hover-border` | `var(--k-cielo)` | — | Borde de 1,5 px (`--line-w-control`) al pasar el cursor |
| `--color-action-pressed` | Igual que en reposo, con escala al 97 % (4.1) | — | Presionado |
| `--color-action-disabled` | Opacidad al 50 % (4.1) | Sin requisito de contraste en deshabilitado (WCAG 1.4.3) | Deshabilitado |
| `--color-focus` | Ver la sección 2 | — | Foco |
| `--color-action-brand` | `var(--k-salmon)`, el actual `--btn-primary-bg` | Noche sobre Salmón 4,87:1 | Solo piezas de marca |

**Estado de procesamiento (falta en todos los botones).** Se propone:
- el botón conserva su ancho y cambia el texto por la acción en curso («Guardando…»);
- un indicador de 16 px a la izquierda;
- `aria-busy="true"` y `aria-disabled="true"`, con el doble envío bloqueado.

Es un comportamiento nuevo y requiere su aprobación.

**Para decidir:**
1. ¿Se crean estos tokens con la principal de producto en Cielo, como ya dice 1.6?
2. En la Fase B, ¿el kit del Laboratorio pasa a usar la principal de producto?

## 2 · Color del foco

| Superficie | Anillo Azul Noche (2 px, a 3 px) | Anillo Azul Cielo |
| --- | --- | --- |
| Blanco Keyons #F4F4F4 | 16,72:1 | 2,56:1 (no alcanza 3:1) |
| Blanco puro #FFFFFF | 18,39:1 | 2,82:1 (no alcanza) |
| Cielo 100 #E0E7F1 | 14,77:1 | — |
| Cielo 200 #C6D5EC (ítem seleccionado del menú) | 12,37:1 | — |
| Azul Cielo #729BDD (botón principal de producto) | 6,52:1 | — |
| Salmón Tierra #CE635D (botón de marca) | 4,87:1 | — |
| Azul Noche #10122A (banda oscura, botón sólido) | 1:1, invisible | 6,52:1 |

El mínimo de WCAG 2.2 para un indicador de foco es de 3:1 frente a lo que lo rodea (1.4.11).

**Propuesta (sin aplicar):**
- `--color-focus: var(--k-noche)` en el tema claro, que ya es lo que pinta el anillo global de `libro.css:22` y lo que manda 4.5.
- `--color-focus-inverse: var(--k-blanco)` (16,7:1) sobre superficies Azul Noche.
- Como alternativa, Azul Cielo sobre Noche (6,52:1).
- El anillo va separado 3 px del control, y por eso sobre un botón relleno se mide contra la superficie que lo rodea, no contra el botón.

**A corregir con su aprobación:** seis componentes dibujan el foco en Cielo sobre fondos claros, con 2,56:1: `.tsel`, `.nvl`, `.rtec__h`, `.cond summary`, `.story` y `.sd-demo__opts`.

## 3 · Tamaño táctil

| Fuente | Valor | Carácter |
| --- | --- | --- |
| WCAG 2.2 AA · 2.5.8 | 24 × 24 px CSS como mínimo, o espacio libre suficiente alrededor | **Requisito.** Excepciones: enlaces dentro de un texto, controles del navegador, un control equivalente que cumple y presentaciones esenciales |
| WCAG 2.2 AAA · 2.5.5 | 44 × 44 px CSS | Nivel superior, con las mismas excepciones |
| Preferencia Keyons (propuesta) | 44 × 44 px CSS en los controles táctiles principales cuando el espacio lo permite | **Preferencia de diseño, no obligación.** Hoy la cumplen el kit del Laboratorio (`lx-btn` con 44 px mínimo) y las aplicaciones móviles. En tablas densas y barras de herramientas de escritorio rige el mínimo de 24 px |

Se documentaría en ACC-008 con nivel DEBERÍA para la preferencia y DEBE para los 24 px. Requiere su aprobación.

## 4 · Duplicaciones: fuente principal y referencias

| Responsabilidad compartida | Normas | Fuente principal propuesta | Qué queda en la otra |
| --- | --- | --- | --- |
| Cuándo se valida un campo (al escribir, al salir, al enviar, al corregir) | CPE-006 (13 Entradas) y PAT-003 (16 Formularios) | **CPE-006**, que tiene la tabla completa por momento | PAT-003 conserva solo lo propio del formulario completo: los valores correctos se conservan y los errores del servidor van junto a su campo. La fila «Momento» ya remite a CPE-006 |
| Ampliación al 200 %, adaptación a 320 px y espaciado de texto | FUI-010 (09 Tipografía) y ACC-003 (22 Adaptación) | **ACC-003**, para los criterios y la prueba | FUI-010 conserva las decisiones tipográficas: unidades relativas, cajas que crecen y medida de lectura. Su tabla de criterios WCAG pasaría a remitir a ACC-003, y su verificación se uniría con la de ACC-003 |

Los dos casos conservan los cuatro códigos, sus requisitos (textos suyos) y la relación en el registro. Solo cambia dónde se desarrolla el detalle.

**Para decidir:** ¿aprueba las dos fuentes principales?

## 5 · Cambios de redacción en la Guía 05

Las filas nuevas de «Composición normativa según el contenido» y «Sistema de diagramación» llevan sus textos. Hubo tres tipos de ajuste:
- **Para que ninguna oración empiece con «No»:**
  - «No diferencies automáticamente requisito y aplicación únicamente cambiando el color» → «El requisito y su aplicación NO DEBEN distinguirse solo por el color del párrafo».
  - «No utilices márgenes excesivos para simular jerarquía» → «Un margen amplio nunca reemplaza la jerarquía».
  - «No crees un bloque separado…» → «Lo que puede integrarse en el bloque anterior se integra, sin un bloque ni un subtítulo propios».
  - «No utilices desplegables simplemente porque existe un helper» → «Un plegable se elige por la función del contenido, nunca por la herramienta que lo genera».
- **Nivel en mayúscula** donde su texto pedía una obligación: DEBE, DEBEN, NO DEBE, PUEDEN.
- **Oraciones de más de 25 palabras divididas** en dos.

## 6 · Verificaciones con cambio de significado

| Norma | Antes | Después | Motivo |
| --- | --- | --- | --- |
| PEX-001 y SPR-002 · Sin decoración | «la tarea se entiende y se completa igual» | «la persona completa la tarea en el mismo tiempo y sin preguntas nuevas» | «Se entiende» no es observable. El tiempo y las preguntas sí |
| CPE-009 · Quitar un contenedor | «Se quita un contenedor y se lee su contenido» → «si la información se entiende igual, el contenedor se elimina» | «Se quita un contenedor y una persona completa la tarea con su contenido» → «la persona agrupa y encuentra la información igual que antes; en ese caso, el contenedor se elimina» | El resultado era una decisión, no un hecho |
| CNT-003 · Interpretación | «las personas las interpretan correctamente» | «cada persona describe la función de cada etiqueta y acción tal como la define el producto» | «Correctamente» no dice contra qué se compara |
| IAE-007 · Historial | «se entiende qué hizo, cuándo y con qué resultado» | «la persona dice qué hizo el agente, cuándo y con qué resultado, sin ayuda» | Observable |
| MOV-004 · Tres modos | «la información esencial se entiende en los tres» | «en los tres modos, la persona identifica la misma información esencial» | Observable |
| ARQ-006 · Recorrido | «se llega al mismo destino, con el mismo comportamiento» | «se llega al mismo destino y el resultado es el esperado» | Acompaña el principio nuevo: el mecanismo puede variar y la expectativa se conserva |
| ARQ-012 · Consultas reales | (condición) nombre parcial, sin tildes y con un error | Se suma «con un identificador escrito de otra forma» | Cubre la fila nueva de identificadores |
| PEX-017 · Fallo | — | Prueba nueva: «Se provoca un fallo al guardar un formulario completo» → «los datos escritos siguen en el formulario y el mensaje ofrece reintentar» | Cubre la fila nueva «Si la operación falla» |
| ARQ-002 · Tarea real | — | Prueba nueva: «Se pide completar una tarea real eligiendo su destino en el menú» → «la persona elige el destino correcto al primer intento» | Usted pidió comprobar la comprensión con tareas reales |

**Cambios sin efecto en el significado:**
- **Mayúscula inicial:** se agregó en las 28 celdas de «Qué se espera» de las tablas de validación. La genera `may()` en `tools/sd/base.py`.
- **Formato:** en las notas breves y los plegables, la minúscula después de «Resultado esperado:» es correcta y quedó igual.
- **Los otros 170 resultados:** no se tocaron.

## 7 · `CLAUDE.md`: dos líneas que chocan con el pedido de la Fase B

| Línea actual | Propuesta |
| --- | --- |
| «No crees maquetas de interfaz en ningún capítulo hasta que Keylin te pase la hoja de componentes aprobada. Mientras tanto, el «Ejemplo de aplicación» va solo como texto» | «En los capítulos del Sistema de Diseño, las demostraciones reutilizan los componentes reales de la Biblioteca y muestran sus variantes y estados. Se marca qué valores están aprobados y cuáles son propuesta. Las pantallas completas de ejemplo siguen fuera hasta la hoja de componentes» |
| «Los formularios todavía no tienen reglas. Si hace falta uno, preguntá antes de diseñarlo» | «Los campos y controles del capítulo 13 se demuestran con la implementación existente (búsqueda y kit del Laboratorio). Un formulario completo nuevo se consulta antes de diseñarlo» |

No lo cambié. Usted decide.

---

## 8 · Normas con requisito redactado por Claude: texto literal

Siguen en borrador. **Requieren su aprobación:** el requisito de cada una, porque lo redacté yo, y en ACC-001 la nueva redacción. Las decisiones, los ejemplos y las verificaciones son propuesta, como en todo el Sistema de Diseño.

#### KYN-SDI-PEX-016 · Prevención de errores

**Titular:** Prevención de errores frecuentes

**Entrada:** Se aplica a los datos y las acciones donde las personas se equivocan con frecuencia: la interfaz evita el error antes de tener que corregirlo.

- **Requisito:** La interfaz DEBERÍA prevenir los errores frecuentes mediante opciones válidas, valores sugeridos y formatos comprensibles antes de que la persona los cometa.
- **Opciones válidas:** Solo se ofrecen las opciones posibles: fechas existentes, cantidades dentro del rango y estados permitidos.
- **Formatos:** El formato esperado se ve antes de escribir, en la etiqueta o en la ayuda del campo, según Etiquetas identificables, en 13 Entradas.
- **Acciones de riesgo:** Se separan de las frecuentes y llevan su protección, según Contexto antes de actuar.
- **Verificación (grupo):**
  - Errores frecuentes: Se registran los errores más frecuentes de una prueba con personas. Resultado esperado: cada uno tiene una medida preventiva o una razón documentada para no tenerla.

#### KYN-SDI-PEX-017 · Control de la persona

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

#### KYN-SDI-PEX-018 · Reconocer antes que recordar

**Titular:** Opciones y datos previos a la vista

**Entrada:** Se aplica a las tareas de varios pasos o pantallas: lo que la persona necesita para seguir está a la vista.

- **Requisito:** La interfaz DEBERÍA mostrar las opciones, los datos previos y el contexto necesario, en lugar de exigir que la persona los recuerde entre pantallas.
- **Opciones:** Listas y sugerencias en lugar de códigos que hay que escribir de memoria.
- **Datos previos:** Lo que la persona eligió en un paso sigue a la vista en el siguiente.
- **Recientes:** Búsquedas y elementos recientes disponibles cuando la tarea se repite.
- **Verificación (breve):**
  - Recorrido: Se recorre una tarea de varios pasos sin papel ni notas. Resultado esperado: ningún paso pide un dato que la persona vio o eligió antes y que ya no está a la vista.

#### KYN-SDI-ARQ-017 · Acceso directo y rutas no disponibles

**Titular:** Enlaces directos y rutas no disponibles

**Entrada:** Se aplica a toda dirección interna que se guarda o se comparte: lleva a su página o a una salida clara, como cualquier otra entrada.

- **Requisito:** Las rutas internas DEBEN permitir abrir directamente una página autorizada cuando el producto admita navegación mediante enlaces.
- **Requisito:** Cuando una ruta no exista, no esté disponible o carezca de autorización, el sistema DEBE comunicar la situación y ofrecer una salida apropiada, sin revelar información restringida.
- **Tabla «Qué ve la persona según la ruta que abre»:**
  - Ruta autorizada: La página completa, con la sección activa marcada según Ubicación actual. | Navega como desde el menú.
  - Ruta inexistente: Un mensaje de página no encontrada, dentro del producto y con su navegación. | Un enlace al inicio o a la sección más cercana, y la búsqueda si existe.
  - Sin autorización: Un mensaje de acceso no disponible, sin datos de la página pedida. | Volver o solicitar acceso, según el producto.
  - Sesión vencida: El inicio de sesión, que conserva la dirección pedida. | Al entrar, la persona llega a la página que buscaba.
- **Información restringida y mensajes (plegable):** Información restringida: Cuando confirmar que un recurso existe ya revela información, la respuesta es la misma que para una ruta inexistente. · Texto del mensaje: Qué pasó y cómo continuar, según Errores comprensibles, en 24 Mensajes. · Ubicación: La página de error conserva la navegación general y solo marca una sección si corresponde.
- **Verificación (tecnica):**
  - Cuatro rutas: Se abren directamente una ruta válida, una inexistente, una no autorizada y una con la sesión vencida. Resultado esperado: la página correcta o un mensaje con salida, sin datos restringidos en el título, el mensaje ni el código. Tras iniciar sesión, se llega a la página pedida.

#### KYN-SDI-CPE-004 · Menú de acciones

**Titular:** Menú de acciones ocasionales

**Entrada:** Se aplica cuando un elemento tiene más acciones de las que caben o conviene mostrar: lo ocasional se agrupa sin esconder lo necesario.

- **Qué va en el menú:** Las acciones secundarias de un elemento PUEDEN agruparse en un menú cuando son ocasionales o no caben. La acción frecuente o principal queda visible, según Navegación visible, en 05 Navegación.
- **Botón:** El botón que abre el menú DEBE nombrar su función. Lleva el ícono de más opciones y un nombre accesible con su objeto: «Más acciones para la factura 2026-118», con aria-haspopup y aria-expanded.
- **Teclado (plegable):** Abrir: Enter, Espacio o flecha abajo abren el menú y el foco pasa a la primera opción. · Recorrer: Las flechas recorren las opciones; Inicio y Fin van a la primera y a la última. · Cerrar: Escape cierra el menú y el foco vuelve al botón. Elegir una opción lo cierra y ejecuta la acción.
- **Verificación (tecnica):**
  - Teclado: Se abre el menú, se recorre y se cierra solo con teclado. Resultado esperado: el foco sigue el recorrido descrito y vuelve al botón al cerrar.
  - Lector de pantalla: Se abre el menú con NVDA o VoiceOver. Resultado esperado: se anuncian el menú, su estado y cada opción.

#### KYN-SDI-PAT-010 · Estados vacíos y de espera

**Titular:** Estados vacíos y de espera

**Entrada:** Se aplica a listas sin contenido y a operaciones que tardan: ninguna pantalla queda sin explicación.

- **Requisito:** Un estado vacío DEBE explicar por qué no hay contenido y ofrecer el siguiente paso.
- **Requisito:** Una espera DEBE indicar que el sistema está trabajando.
- **Tabla «Estados vacíos y de espera»:**
  - Vacío por primera vez: Para qué sirve el espacio: «Aún no hay solicitudes». | Crear la primera.
  - Vacío por filtros: Que los filtros no tienen coincidencias (Búsquedas sin resultados). | Quitar filtros.
  - Espera breve: Un indicador en el lugar de la acción. | —
  - Espera larga: Qué está haciendo el sistema y, si se conoce, el avance (Resultado visible). | Cancelar, si se puede.
- **Notas técnicas (plegable):** Anuncio: Los cambios de estado se anuncian en una región role="status", sin mover el foco. · Umbral: El tiempo a partir del cual una espera es larga es una hipótesis que hay que validar (UIX-021 proponía 400 ms y 3 s).
- **Verificación (tecnica):**
  - Cuatro casos: Se fuerzan una lista vacía por primera vez, una búsqueda vacía, una espera corta y una espera larga. Resultado esperado: ninguno queda en blanco ni sin una acción posible.
  - Lector de pantalla: Se provoca una espera con un lector de pantalla activo. Resultado esperado: se anuncia que el sistema está trabajando y, después, el resultado.

#### KYN-SDI-SPR-004 · Navegación predeterminada

**Titular:** Patrón de navegación de los productos SaaS

**Entrada:** Define la estructura de navegación común de los productos SaaS de Keyons: se aprende una vez y sirve en todos.

- **Requisito:** Los productos SaaS de Keyons DEBERÍAN usar el patrón de navegación predeterminado, salvo que su estructura justifique otro.
- **Tabla «Patrón predeterminado (propuesta)»:**
  - Navegación principal: Lateral, con grupos que se abren y se pueden contraer. | Panel que cubre la pantalla, abierto desde un botón con nombre.
  - Cabecera: Nombre del producto, búsqueda global y cuenta. | Título de la pantalla, menú y búsqueda.
  - Ubicación: Sección activa marcada y ruta desde el tercer nivel. | Título y ruta abreviada.
- **Origen (plegable):** Por qué aquí: 05 Navegación define las reglas generales sin imponer un patrón; esta norma fija el predeterminado. Requisito y patrón redactados por Claude; requieren aprobación.
- **Verificación (breve):**
  - Dos productos: Se comparan dos productos SaaS. Resultado esperado: tienen la misma estructura de navegación, con sus destinos propios.

#### KYN-SDI-GOB-003 · Protocolo previo al lanzamiento

**Titular:** Protocolo previo al lanzamiento

**Entrada:** Se aplica antes de lanzar cada producto o versión: la misma revisión visual, funcional, de uso y de accesibilidad.

- **Requisito:** Antes del lanzamiento, cada producto DEBERÍA completar la verificación visual, funcional, de usabilidad y de accesibilidad, con su registro firmado.
- **Origen (plegable):** UIX: Recupera UIX-047 y UIX-050 como referencia; el número mínimo de participantes y los firmantes requieren aprobación.
- **Verificación (tecnica):**
  - Expediente: Se revisa el expediente del lanzamiento. Resultado esperado: tiene las cinco evidencias del protocolo, cada una con su resultado.

#### KYN-SDI-ACC-001 · Referencia de conformidad

**Titular:** WCAG 2.2 AA como referencia de conformidad

**Entrada:** Define el mínimo de accesibilidad de todo producto web de Keyons: WCAG 2.2 nivel AA, comprobado con herramientas y con personas.

- **Requisito:** Los productos web de Keyons DEBEN diseñarse y verificarse tomando WCAG 2.2 nivel AA como objetivo mínimo de accesibilidad.
- **Alcance:** Todas las pantallas, estados y documentos que el producto genera.
- **Declaración:** Cada producto registra su nivel alcanzado y las excepciones justificadas, con su plan de corrección (44 Validación).
- **Verificación (breve):**
  - Revisión doble: Se revisa cada pantalla con una herramienta automática y, después, a mano con teclado y lector de pantalla. Resultado esperado: ningún criterio AA queda incumplido; la herramienta sola no alcanza para darlo por cumplido.

