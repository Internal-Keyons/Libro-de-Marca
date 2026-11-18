# Inventario de lo construido · Biblioteca Keyons

**Fase A.** Versión inicial del 2026-11-18, tomada antes de cualquier corrección. Se actualiza al final de la ronda (ver «Después de la Fase A»).

**Cómo se hizo**
- Los valores salen del código: `css/tokens.css`, `css/libro.css`, `css/marca.css`, `css/sistema-diseno.css`, `css/laboratorio-kit.css`, `js/libro.js` y las páginas del Libro de Marca. Ninguno se deduce de una captura.
- Cuando una regla tiene varias capas, se cita la que gana en pantalla.
- Las imágenes 14 a 21 y los PDF de Figma («Cómo crear tu sistema de diseño», «Qué es un sistema de diseño», «Cómo impulsar la adopción», «Cómo seguir el ROI») sirvieron para ordenar el inventario: fundamentos, componentes con variantes, tamaños y estados, y documentación por propiedades. Ningún valor sale de ellos.
- De los tres videos solo pude leer los títulos: «Intro to variables», «Variables for typography» y «Prototype with variables». No vi su contenido y no lo uso.

## Clasificación

| Clase | Qué significa |
| --- | --- |
| **Aprobado** | Existe y una regla de `reglas-visuales.md` o de la Guía lo respalda. Se documenta y se reutiliza sin rediseñarlo |
| **Sin especificar** | Existe y funciona, pero ninguna regla lo describe. Se recuperan sus valores reales |
| **A corregir** | Existe, pero contradice una regla o se duplica. Se propone la corrección antes de tocarlo |
| **Falta** | No existe. Se propone una especificación compatible |

**Escala de estado** (la de Keylin): documentado, especificado visualmente, implementado, verificado o aprobado. En las tablas se abrevia D, EV, I, V o A, y una pieza puede tener varias marcas.

---

## 1 · Tipografía → capítulo 09

| Elemento | Ubicación | Implementación original | Clase | Estado | Reutilizable |
| --- | --- | --- | --- | --- | --- |
| Familia de lectura | `<link>` de Google Fonts en cada página | Plus Jakarta Sans 400·500·600·700 | Aprobado (2.1) | D·I·A | Sí |
| Familia de exhibición | `tokens.css:8-13` | TASA Orbiter variable 400–800, `assets/fonts/` | Aprobado (2.1) | D·I·A | Sí |
| Pilas | `tokens.css:95-97` | `--font-display`, `--font-sans`, `--font-mono` | Aprobado | I | Sí |
| Escala de lectura | `tokens.css:100-101, 228` | `--fs-12/14/16/20/24/32`; `--fs-20-24` y `--fs-24-32` crecen desde 1200 px | Aprobado (2.2, T01). La regla nombra 5 tamaños y el código tiene 6 (32) | D·I·A | Sí |
| Escala de exhibición | `reglas-visuales.md` 2.3 | `--fs-title-s`, `--fs-title`, `--fs-display-m`, `--fs-display` | **Falta en el código.** Los títulos usan `clamp()` sueltos | D | Se toma el valor real de cada `clamp()` |
| Tracking | `tokens.css:126-132` | `--tr-0`…`--tr-3`, `--tr-kicker`, `--tr-caps` | **A corregir:** los tokens existen, pero el código todavía escribe valores sueltos | D·I | Sí |
| Nueve niveles editoriales | `fundamentos/tipografia/sistema.html` (8.2) | Display 52–128 · Título de sección 32–44 · Subtítulo 24 · Título menor 20 · Entrada 20 · Cuerpo 16 · Pequeño 14 · Rótulo 12 · Kicker 12 | Aprobado (Libro de Marca) | D·EV·A | Base del 09 |
| Titular de página | `libro.css:25` `.t-display` | Orbiter 500, `clamp(52px,8.6vw,128px)`, interlineado .93, −.04em | Sin especificar como token | I | Sí |
| Título de sección | `libro.css:733` `.ed__title` | 500, `clamp(32px,3.2vw,44px)`, 1.1, −.03em, Gris titular, máx. 760 | Aprobado (R10) | I·A | Sí |
| Entrada | `libro.css:734, 4777, 6179` `.ed__lead` | 20 px, 1.55, `--color-text-2`, máx. 600 | Aprobado | I·A | Sí |
| Subtítulo de bloque | `libro.css:1142, 4862, 5572` `.ed__sub` | 20 px, 500, 1.35, −.01em, línea de grupo Azul Noche (5.2) | Aprobado | I·A | Sí |
| Cuerpo | `libro.css:10, 816, 5994` | 16 px; 1.6 en `body` y 1.65 en filas y prosa | Aprobado (2.2: 1,6) | I·A | Sí |
| Rótulo | `libro.css:43` `.paren` | 12 px, 500, gris 2 o 3 según el contexto | Aprobado (2.2) | I·A | Sí |
| Kicker | `libro.css:4135` | 700, 12 px, interlineado 1, mayúsculas, +.02em, estrella de 12 px | Aprobado (2.5) | I·A | Sí |
| Texto de tabla | `libro.css:784-787, 898` | Encabezado 14/600 gris 3 · rótulo de fila 12 gris 3 · celda 16 | Aprobado (R13) | I·A | Sí |
| Código | `libro.css:481, 1880` | Mono 14/1.75 en bloque; .92em Azul Noche en línea | Sin especificar | I | Sí |
| Probador y fichas | `fundamentos/tipografia/sistema.html` (`szc`, `tester`, `plate`, `trk`) | Fichas de tamaño, probador vivo, láminas de glifos y pestañas de tracking | Aprobado (Libro de Marca) | EV·I | **Sí: patrón de muestra para el 09** |
| Jerarquía H1–H6 | — | El libro usa h1 (portada), h2 (`.ed__title`) y h3 (`.ed__sub`) | **Falta** para productos: la relación entre H1–H6 y la escala visual | — | — |

## 2 · Color → capítulos 07 y 08

| Elemento | Ubicación | Implementación original | Clase | Estado | Reutilizable |
| --- | --- | --- | --- | --- | --- |
| Primitivos | `tokens.css:21-26` | Noche #10122A · Blanco #F4F4F4 · Cielo #729BDD · Salmón #CE635D · Atardecer #E99D9E · Puro #FFFFFF | Aprobado (1.1) | D·EV·I·A | Sí |
| Escalas | `tokens.css:29-43` | Cielo 100–900, Gris, Noche y Salmón con medios pasos (OKLab) | Aprobado (1.2) | D·EV·I·A | Sí (`fundamentos/color/escalas.html`, `tone`) |
| Grises de texto | `tokens.css:46-49, 68-71` | `--color-text` #10122A · `-2` #4B4D60 · `-3` #6B6D7E · titular #8B8C92 · deshabilitado #A8AAB5 | **A corregir:** 1.3 manda #494A5D / #6C6D7B / #82838F / #A4A4AD. La página Funcionales (7.14) muestra los valores del código | D·EV·I | Se cierra la diferencia antes de mostrarla en el 08 |
| Superficies | `tokens.css:64-66` | `--color-bg` Blanco · `--color-surface` Puro · `--color-inverse` Noche | Aprobado | I | Sí |
| Bordes | `tokens.css` | `--color-border` Cielo 100 · `--color-border-strong` Cielo 200 | Aprobado (5.2) | I | Sí |
| Estados | `tokens.css:85-92`; `fundamentos/color/funcionales.html` 7.15 | Éxito #D5E0D2 · Advertencia #F4E8C1 · Error #F0D0CB · Información #C6D5EC · Revisión #D9D6ED · Neutro #E0E1E5 · Bloqueo #F5D8B8 | Aprobado (1.7). Error en terracota, nunca Salmón Tierra | D·EV·I·A | Sí (`states`, `badge`) |
| Enlace | `tokens.css:161-166`; `libro.css:3240-3245` | Noche, 1 px a 4 px; al pasar el cursor, Noche 500 y 2 px | Aprobado (R06, 2026-11-17) | D·I·A | Sí |
| Foco | `tokens.css:83`; `libro.css:21-22` | El anillo global es de 2 px Azul Noche, a 3 px, solo con teclado. **`--color-focus` vale Cielo** | **A corregir:** el token contradice 4.5. Seis excepciones usan Cielo: `.tsel`, `.nvl`, `.rtec__h`, `.cond`, `.story`, `.sd-demo__opts` | I | Ver decisiones pendientes |
| Acción | `tokens.css:150-160` | `--btn-primary-bg` Salmón · sólido Noche (al pasar el cursor, Cielo) · contorno con borde Cielo | Aprobado para **piezas de marca** (1.6). **Falta** la variante de producto (Cielo con texto Noche, 1.6) | I | Ver decisiones pendientes |
| Muestras de color | `fundamentos/color/*.html` (`palette`, `gray`, `tone`, `cmpx`, `states`) | Fichas con HEX copiable, contraste y matriz de pares | Aprobado (R24) | EV·I | **Sí: patrón de muestra para el 08** |
| Uso funcional por superficie | — | — | **Falta:** la vista que muestra superficie, texto, borde, acción, selección, foco y deshabilitado juntos | — | — |

## 3 · Espacio, forma y retícula → capítulo 10

| Elemento | Ubicación | Implementación original | Clase | Estado | Reutilizable |
| --- | --- | --- | --- | --- | --- |
| Escala de espacio | `tokens.css:104-105` | `--s1` 4 · `s2` 8 · `s3` 12 · `s4` 16 · `s5` 20 · `s6` 24 · `s8` 32 · `s10` 40 · `s12` 48 · `s16` 64 · `s20` 80 · `s24` 96 · `s32` 128 | Aprobado (3.3, múltiplos de 4) | D·EV·I·A | Sí (`fundamentos/forma/espacio.html`, `spc`) |
| Separaciones con nombre | `tokens.css:108-111` | `--gap` 24 · `--gap-fusion` 0 · `--gap-list` 12 · `--gap-section` 64 | Aprobado. **Falta `--gap-component` 48** (3.3) | D·I | Sí |
| Radios | `tokens.css:114-115` | 0 · 3 · 12 · 18 · 30 · 50 · píldora | Aprobado (3.1, 3.2) | D·EV·I·A | Sí (`rdemo`) |
| Medida de lectura | `tokens.css:124` | `--measure` 600 px | Aprobado (3.4) | D·I·A | Sí |
| Retícula editorial | `libro.css:729, 742-747, 4773` | `.ed`: 200 px de metadatos más 1fr, separación de 64. Una columna desde 1000 px | Sin especificar como token | I | Sí, para la documentación (no es la retícula de un SaaS) |
| Retícula del documento | `libro.css:341-343, 370, 4770` | `.doc` de 1600 máx.: 288 · 1fr · 232. Desde 1280, 272 · 1fr. Desde 900, una columna con menú en cajón de `min(320px,88vw)` | Sin especificar | I | Referencia para la navegación adaptable |
| Relleno del contenido | `libro.css:382, 4772` | 48/64/96 · 40/40/80 desde 1100 · 32/16/64 desde 760 | Sin especificar | I | Sí |
| Cortes de pantalla | `libro.css` | 760 (112 usos) · 900 (93) · 600 · 1100 · 1000 · 1179 · 1280 · 1200 | **A corregir:** sin tokens y con cortes vecinos (760/767, 600/640) | I | Se consolidan en la Fase B |
| Desenfoque | `tokens.css:182` | `--glass-blur` 24. El código usa 8, 12, 14, 16, 22, 24 y 36 | **A corregir:** 5.1 pide `--blur-1` 12 y `--blur-2` 22 | I | — |
| Sombras | `tokens.css:186-188` | `--shadow-1/2/3` | Aprobado (5.3) | I·A | Sí |
| Retícula de producto | `css/laboratorio-kit.css` (`--lab-cols` 12, `--lab-gap` 24, `--lab-maxw` 1200) | Solo en el Laboratorio | **Falta** como especificación aprobada | I | Insumo para el 10 |

## 4 · Botones y acciones → capítulo 12

| Elemento | Ubicación | Implementación original | Clase | Estado | Reutilizable |
| --- | --- | --- | --- | --- | --- |
| `.btn` base | `libro.css:98-123` y **`3226`** | Primera capa: 14 px, 700, mayúsculas, .05em, 16 × 40, borde de 1 px. **En pantalla gana la de la línea 3226: 12 px, .06em, 11 × 22, separación de 8** | **A corregir:** 4.1 pide 14 px, 16 × 40 y borde de 1,5 px | I | Sí, después de cerrar la diferencia |
| Principal de marca | `libro.css:109, 120`; tokens 150-151 | Salmón con texto Noche. Al pasar el cursor: radio 0, fondo Blanco y borde Salmón | Aprobado (4.2, P1 pendiente) | I·A | Sí |
| Principal de producto | `reglas-visuales.md` 4.2 y 1.6 | Cielo con texto Noche. Al pasar el cursor: Blanco con borde Cielo | **Falta en el código** | D | — |
| Sólido | `libro.css:110, 121` | Noche con texto Blanco. Al pasar el cursor: Cielo con texto Noche y radio 0 | Aprobado | I·A | Sí |
| Contorno | `libro.css:3158, 3739, 3883` | Borde Cielo de 1,5 px hacia dentro. Al pasar el cursor, fondo Noche | Aprobado (4.2). Tiene tres capas en el CSS | I | Se consolidan en una |
| Cristal | `libro.css:113-116` | Blanco al 10 %, borde al 30 %, desenfoque de 12 | Aprobado (4.2) | I·A | Solo sobre imagen |
| Texto | `libro.css:128` | 14/500, Noche al 55 %, flecha de 16 px | **A corregir:** 4.2 y 1.3 piden gris terciario, sin opacidad | I | — |
| Ícono | `libro.css:142, 3738, 3878, 4229` | Círculo de 36 px (32 en móvil), borde Gris Plata al 70 %, ícono gris 3. Al pasar el cursor, fondo Noche | Aprobado (4.2) | I·A | Sí |
| Barrido (Buscar, Lab) | `libro.css:5492, 5767-5780, 5949, 6105`; `js/libro.js:136` | 37 px de alto, 8 × 20, píldora, 14/500, barrido de 420 ms y borde Noche de 1,5 px al pasar el cursor. Círculo de 40 px desde 1179 | Aprobado (4.3, B03) | I·A | Sí |
| Chips y conmutadores | `libro.css:5676` (`.rtec__bar`); `sistema-diseno.css:28-31` | Mínimo 36 de alto, 6 × 16, píldora y `aria-pressed` | Sin especificar. Hay dos versiones | I | Se elige una |
| Controles del menú | `libro.css:5447, 5152`; `js/libro.js:1040, 1053-1063` | «Contraer menú» con 40 px y `aria-pressed`; «Descargar PDF» y «Normas para IA» de 14 px | Aprobado (R16) | I·A | Solo para la Biblioteca |
| Estado de procesamiento | — | — | **Falta** en todos los botones | — | — |
| Kit del Laboratorio | `laboratorio-kit.css:132-140` | `lx-btn` de 44 px mínimo, 0 × 24, píldora, 14/600. **El principal es Salmón** | **A corregir:** duplica `.btn` y contradice 1.6 (en producto, la acción va en Cielo) | I | Se unifica con `.btn` |
| Página de pruebas | `sistema-diseno/laboratorio-componentes.html` | `btn btn--primary/--outline`, `lb-*` y `badge` | Sin especificar. El laboratorio no es referencia visual | I | Solo como insumo |

## 5 · Entradas y controles → capítulo 13

| Elemento | Ubicación | Implementación original | Clase | Estado | Reutilizable |
| --- | --- | --- | --- | --- | --- |
| Campo de búsqueda | `libro.css:530-547`; `js/libro.js:1778-1856` | 16 px, 16 × 24, píldora, borde de 1 px. Con el foco, borde fuerte y sin anillo (4.5). Resultados en `listbox`, con ↑ ↓, Enter y Esc, y una región `aria-live` | Aprobado (4.5) | I·V | Patrón del cuadro combinado |
| Tokens de campo | `tokens.css:222-224` | `--field-radius` píldora · halo de foco de 5 px Cielo 200 · halo de error de 5 px terracota | Sin especificar (los formularios no tienen reglas) | I | Sí, si se aprueban |
| Kit del Laboratorio | `laboratorio-kit.css` | `lx-field` (con `.is-error`), `lx-input`, `lx-select`, `lx-textarea` (48 px), `lx-check`, `lx-switch`, `lx-tabs` (`aria-selected`) | Sin especificar y no es referencia (CLAUDE.md) | I | **Insumo principal del 13** |
| Página de pruebas | `laboratorio-componentes.html` | `lb-field`, `lb-select`, `lb-radio`, `lb-states` | Sin especificar | I | Insumo |
| Selector desplegable | `libro.css:5256`; `js/libro.js:600-622` (`.kdd`) | `aria-haspopup=listbox`, Esc, ↑ ↓ y ventana cuadrada (R12) | Aprobado (R12) | I | Sí |
| Casilla, opción e interruptor del libro | — | — | **Falta** fuera del Laboratorio | — | — |
| Control de fecha | — | — | **Falta** | — | — |

## 6 · Otros componentes → capítulos 14 y 15 y la composición del Sistema de Diseño

| Elemento | Ubicación | Implementación original | Clase | Estado | Reutilizable |
| --- | --- | --- | --- | --- | --- |
| Acordeón | `libro.css:647-655, 4866, 6159-6177` | `details`/`summary`, 1fr + 36, signo + en `.btn-icon`, sin número | Aprobado (R27) | I·A | Sí |
| Detalle simple | `libro.css:6182-6193` | `.det`: 16 px, gris 2 que pasa a Noche al abrir, signo de 16 | Aprobado (Guía 05) | I·A | Sí |
| Tabla | `libro.css:779-795, 4139-4141, 4170`; `js/libro.js:693` | 200 · 1fr · 1fr, celdas de 20, barras Cielo 200 de 4 px, `role=table`. Dos columnas desde 900 | Aprobado (R13) | I·A | Sí |
| Filas | `libro.css:813-817, 6176` | `.ed__stack`: filas de 32 con línea de 1 px y medida de 600 | Aprobado | I·A | Sí |
| Retícula de tarjetas | `libro.css:822-833, 6153` | `.pgrid` de 3 columnas (`--2`, `--4`), barras Cielo 200 y celda vacía | Aprobado (R23) | I·A | Sí |
| Pasos | `libro.css:956-963` | `.steps`: 56 · 1.1fr · .9fr | Aprobado | I·A | Sí |
| Antes y después | `libro.css:1041, 3362-3366` | `.redline`: gris 3 sin tachado y flecha Noche | Aprobado (R03) | I·A | Sí |
| Nota de cierre | `libro.css:5564-5569` | `.ed__more` con rótulo y línea superior | Aprobado | I·A | Sí |
| Menú lateral | `libro.css:357-364, 5144, 5252, 5521-5525` | Ítem de 14 px. Al pasar el cursor, Cielo 100; el actual, Cielo 200 y 600 | Aprobado | I·A | Referencia para la navegación |
| Diálogo | `libro.css:5208-5243`; `js/libro.js:149-187` | Selector de libros: `role=dialog`, `aria-modal`, Esc y foco atrapado. Hoja inferior en móvil | Sin especificar como componente | I·V | **Sí: base del diálogo** |
| Pestañas | `js/libro.js:387-410, 900-910, 1313` | `[role=tab]` con flechas | Sin especificar | I | Sí |
| Ayuda emergente | `libro.css:2123, 5964` | `.ctip`: Noche, 12 px, 8 × 12, radio 0 | Sin especificar | I | Sí |
| Marca de nivel | `libro.css:5956-5963, 6117`; `js/libro.js:2100-2121` | Cuadrado de 8 px en tres estados, `tabindex=0` | Aprobado (R16) | I·A | Solo para normas |
| Insignias | `libro.css:158-164` | 12/600, píldora, colores de estado | Aprobado (1.7) | I·A | Sí |
| Indicador de carga | — | — | **Falta** (existe `lx-skel` en el Laboratorio) | — | — |
| Alerta | — | — | **Falta** en el libro (existe `lx-alert` en el Laboratorio) | — | — |

## 7 · Comportamiento y accesibilidad

| Elemento | Ubicación | Implementación original | Clase |
| --- | --- | --- | --- |
| Foco solo con teclado | `js/libro.js:24-31` | `data-kbd` al usar Tab o flechas; se quita al usar el puntero | Aprobado (4.5) |
| Movimiento | `tokens.css:141-143` | 180 / 300 / 520 ms y dos curvas | Aprobado (7). **A corregir:** quedan 420, 500, 515 y 360 ms sueltos |
| Movimiento reducido | `libro.css` (20 reglas) | Desactiva las animaciones | Aprobado |
| Móvil | `libro.css` | Ver los cortes de pantalla (sección 3) | Aprobado por uso |

## 8 · Contradicciones que necesitan decisión

1. **Grises de texto:** el código y la página Funcionales no coinciden con 1.3 (§2).
2. **Botón base:** la capa de la línea 3226 contradice 4.1 (§4).
3. **Botón de texto:** usa opacidad, contra 4.2 y 1.3 (§4).
4. **`--color-focus`:** es Cielo, contra 4.5, más seis excepciones en Cielo (§2).
5. **Acción principal:** 1.6 ya separa producto (Cielo) y marca (Salmón). El código solo tiene la de marca, y el kit del Laboratorio usa Salmón en interfaces de producto (§4).
6. **`CLAUDE.md`:** dice «sin maquetas hasta la hoja de componentes» y «formularios sin reglas». Eso choca con el pedido de demostraciones reales para el 12 y el 13.

Las propuestas para cerrarlas están en `decisiones-pendientes.md`. No se aplica ninguna sin la aprobación de Keylin.

---

## Después de la Fase A

**Implementación original:** todo lo listado arriba, sin cambios salvo lo que sigue. Ningún botón, color, token, tipografía ni componente aprobado fue modificado.

### Correcciones aplicadas en esta fase

| Elemento | Antes | Ahora | Dónde |
| --- | --- | --- | --- |
| Color de lectura del Sistema de Diseño | Filas y prosa en `--color-text-2`; requisito en `--k-noche` | Filas, prosa y requisito en `--color-text`. Rótulos, entradas y notas, en gris | `css/sistema-diseno.css` (Guía 05 · Color del texto) |
| Requisito seguido de filas | 64 px de margen y dos líneas | Una línea y el relleno de fila `--s8` | `css/sistema-diseno.css` (Guía 05 · Proximidad) |
| Requisito seguido de tabla | 64 px y dos líneas | `--s8` y la línea fuerte de la tabla | `css/sistema-diseno.css` |
| Filas, plegables y nota de verificación | Dos líneas a 40 px entre cada uno | Una sola línea | `css/libro.css` (secuencias que hoy solo aparecen en el Sistema de Diseño) |
| Tabla de validación | Rótulo con enlace y resultado en minúscula | Rótulo sin enlace y resultado con mayúscula | `tools/sd/base.py` (`validacion`, `may`) |
| Dependencias normativas | Solo como enlaces en el texto | Enlaces necesarios más `relaciones` en el registro, generadas desde los módulos | `tools/sd/base.py` (`rel`), `tools/sd_capitulos.py` |

### Ampliación pendiente (Fase B)

La Fase B depende de su revisión de este inventario y de las decisiones de `decisiones-pendientes.md` que afectan la implementación: acción principal, foco y 44 px.

| Capítulo | Qué se va a mostrar | Qué se reutiliza | Qué decide antes |
| --- | --- | --- | --- |
| 09 Tipografía | Los nueve niveles con su muestra real y valores; la relación entre H1–H6 y la escala visual; escritorio frente a móvil donde los valores cambian (`--fs-20-24`, `--fs-24-32`, `clamp()` de títulos); cifras y tablas; truncamiento | Fichas `szc` y probador `tester` de `fundamentos/tipografia/sistema.html` | Si se crean los tokens de exhibición de 2.3 con los valores reales de los `clamp()` |
| 07 y 08 Tokens y color | Primitivos y semánticos con su función; una misma variable aplicada en varios elementos; superficies, texto, bordes, acción, selección, foco y deshabilitado con sus pares de contraste | Fichas `gray`, `tone`, `cmpx` y `states` del Libro de Marca | Grises de 1.3 frente al código; `--color-focus`; tokens de acción |
| 10 Espacio y retícula | La escala `--s*`; contenedores y anchos; una retícula viva que se adapta (la `.ed` y una de producto de 12 columnas, a partir del kit) | Barras `spc`, demostración de radios `rdemo` y retícula `.ed` | La retícula de producto, que solo existe en el Laboratorio |
| 12 Botones y acciones | `.btn` (marca y sólido), contorno, ícono, texto y barrido, en vivo, con sus estados normal, al pasar el cursor, foco, presionado y deshabilitado; procesamiento como propuesta | `.btn` y `.btn-icon` del libro, como implementación canónica única; el Laboratorio la usaría en lugar de `lx-btn` | Principal de producto; diferencia entre la línea 3226 y 4.1; botón de texto |
| 13 Entradas y controles | Campo con ayuda y error, casilla, opción, interruptor y selector, en vivo y accesibles | Búsqueda (`listbox` y teclado), `.kdd` y el kit `lx-*` en una sola fuente | Las dos líneas de `CLAUDE.md` sobre maquetas y formularios |

Cada pieza llevará su estado: documentada, especificada visualmente, implementada, verificada o aprobada.
