# Estética real del Libro de Marca Keyons

**Qué es:** los parámetros que el código aplica hoy (rama `consolidacion`, commit `3075e26`). No describe lo que dicen las normas. Los valores salen de los estilos computados en el navegador a 1440 px de ancho y de `css/tokens.css`, `css/libro.css` y `css/sistema-diseno.css`. Con esto se puede recrear la estética en otro proyecto.

---

## 1. Color

### Paleta base

| Uso | Nombre | HEX | Dónde aparece |
|---|---|---|---|
| Fondo de página | Blanco Keyons | `#F4F4F4` | `body`, fondo general |
| Superficies | Blanco puro | `#FFFFFF` | tarjetas, muestras, menús desplegables, paneles |
| Texto principal | Azul Noche | `#10122A` | texto, negritas, botones sólidos, logotipo |
| Señal | Azul Cielo | `#729BDD` | subrayados, foco de campos, puntos activos, flechas de hover |
| Acento cálido | Salmón Tierra | `#CE635D` | botón principal, viñetas en piezas de color; casi ausente en la interfaz del manual |
| Acento sobre oscuro | Salmón Atardecer | `#E99D9E` | solo sobre Azul Noche |

### Escala Azul Cielo (líneas y superficies suaves)

| Token | HEX | Uso |
|---|---|---|
| `cielo-100` | `#E0E7F1` | todas las líneas finas (1 px), hover de menús, rótulos «Uso incorrecto / Alternativa mejor» |
| `cielo-200` | `#C6D5EC` | divisor fuerte de sección (1 px sobre cada `.ed`), barras de 4 px en tablas y cabeceras de bloques, selección de texto, fondo del ítem activo del menú lateral |
| `cielo-700` | `#496192` | hover de enlaces cruzados |

### Grises de texto (códigos propios, no opacidades)

| Nivel | Token | HEX | Uso |
|---|---|---|---|
| 1 | gris-1 | `#10122A` | texto fuerte, negritas, valores |
| 2 | gris-2 | `#4B4D60` | párrafos, entradas, cierres |
| 3 | gris-3 | `#6B6D7E` | rótulos, metadatos, encabezados de tabla, migas |
| Titular | gris-titular | `#8B8C92` | títulos de sección (`h2`) |
| 4 | gris-4 | `#A8AAB5` | deshabilitado, bordes de botones de icono |

### Estados (fondos pastel con texto Azul Noche)

| Estado | HEX |
|---|---|
| Éxito | `#D5E0D2` |
| Advertencia | `#F4E8C1` |
| Error | `#F0D0CB` |
| Información | `#C6D5EC` |
| Revisión | `#D9D6ED` |
| Bloqueo | `#F5D8B8` |
| Neutro | `#E0E1E5` |

### Resaltado y selección

| Elemento | Valor |
|---|---|
| Resaltado de cierre (`.hl`) | fondo `rgba(114,155,221,.3)`, padding `.04em .22em`, sin radio, `box-decoration-break:clone` |
| Selección de texto | fondo `#C6D5EC` |
| Foco | `outline: 2px solid #10122A; outline-offset: 3px` |

### Cielos (degradados oficiales)

Hay cinco variables, `--sky-amanecer`, `--sky-mediodia`, `--sky-atardecer`, `--sky-noche` y `--sky-galaxia`. Cada una combina dos a cuatro `radial-gradient` con punto focal y un `linear-gradient` vertical de base. Los valores están en `css/tokens.css`.

---

## 2. Tipografía

### Familias

| Familia | Rol | Pesos cargados |
|---|---|---|
| Plus Jakarta Sans | todo el texto de lectura e interfaz | 400, 500, 600, 700, itálica 400 |
| TASA Orbiter (variable 400 a 800) | solo el display de portadas y encabezados de capítulo, el probador tipográfico y las muestras | — |

### Jerarquía real de las páginas

| Elemento | Familia | Tamaño | Peso | Interlineado | Tracking | Color |
|---|---|---|---|---|---|---|
| Display de encabezado de capítulo (`.t-display`) | TASA | `clamp(52px, 8.6vw, 128px)`, 92 px a 1440 | 500 | 0,93 a 0,98 | −0,04em | Noche sobre cielo, Blanco sobre oscuro |
| Título de sección (`.ed__title`) | Jakarta | `clamp(30px, 3.2vw, 44px)` | 500 | 1,1 | −0,03em | `#8B8C92` |
| Entrada (`.ed__lead`) | Jakarta | `clamp(18px, 1.5vw, 20px)` | 400 | 1,55 | 0 | `#4B4D60` |
| Negrita dentro de entrada o texto | Jakarta | — | 600 | — | — | `#10122A` |
| Subtítulo interno (`.ed__sub`) | Jakarta | 18 px | 500 | 1,35 | −0,01em | `#10122A` |
| Texto de filas (`.ed__stack p`) | Jakarta | 17 px | 400 | 1,65 | — | `#4B4D60` |
| Cierre (`.ed__close`) | Jakarta | `clamp(20px, 1.8vw, 24px)` | 400 | 1,5 | — | `#4B4D60`, con resaltado `.hl` en Noche |
| Nota (`.ed__more`) | Jakarta | 16 px | 400 | 1,65 | — | `#4B4D60` |
| Rótulo (`.paren`, `dt`, etiquetas) | Jakarta | 13 px (12 en tablas y menús) | 400 a 500 | 1,6 | — | `#6B6D7E` |
| Código de norma (`.ed__code`) | Jakarta | 12 px | 400 | 1,4 | +0,03em | `#6B6D7E` |
| Kicker (estrella + texto) | **Jakarta** | 12 a 13 px | **700** | 1 | +0,02em | Noche; Blanco sobre oscuro |
| Encabezado de tabla (`.matrix__lvl`) | Jakarta | 15 px | 600 | 1,6 | −0,01em | `#6B6D7E` |
| Valor de tabla (`.matrix__v`) | Jakarta | 15 px | 400 | 1,6 | — | `#10122A` |
| Rótulo de fila de tabla (`.matrix__k`) | Jakarta | 13 px | 400 | — | — | `#6B6D7E` |
| Título de ítem (pasos, patrones) | Jakarta | 18 a 20 px | 500 | 1,25 a 1,3 | −0,01em | `#10122A` |
| Viñeta de lista (`.vlist li`) | Jakarta | 15 px | 400 | 1,6 | — | `#10122A` |
| Menú lateral, capítulo | Jakarta | 15 px | 600 | — | — | `#10122A` |
| Menú lateral, ítem | Jakarta | 14 px | 400; 600 si está activo | 1,35 | — | `#4B4D60` |
| Menú lateral, grupo | Jakarta | 11 px, MAYÚSCULAS | 700 | — | +0,02em | `#6B6D7E` |

### Reglas tipográficas del código

- **Ajuste de líneas:**
  - `h1`, `h2`, `h3`: `text-wrap: balance`.
  - Párrafos: `text-wrap: pretty`.
- **Titulares de 34 caracteres o más:** se cortan en dos renglones después de la coma o el punto y coma.
- **Espacios no separables:**
  - La primera palabra corta de cada oración, hasta 6 letras, se une a la siguiente.
  - Las dos últimas palabras de un párrafo se unen.
  - No se aplica en textos de más de 24 px ni en columnas de menos de 260 px.
- **Cifras:** tabulares en tablas, contadores y numeraciones (`font-variant-numeric: tabular-nums`).
- **Fuente única de datos:** `js/tipografia-datos.js` alimenta la escala editable, el probador y las tablas de referencia.

---

## 3. Espaciado y retícula

### Escala (base 4)

`4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64 · 80 · 96 · 128` px, como tokens `--s1` a `--s32`.

### Página

| Elemento | Valor |
|---|---|
| Documento (`.doc`) | `max-width: 1600px`, centrado |
| Menú lateral | 288 px de ancho, sticky, `padding: 40px 0 64px`, línea derecha de 1 px `cielo-100` |
| Contenido (`.content`) | `padding: 48px 64px 96px`; 40 px por lado bajo 1100 px; 16 px en móvil |
| Capítulo | `max-width: 1180px`, alineado a la izquierda |
| Cabecera | 112 px de alto, fija, alineada al ancho del documento, padding lateral de 16 a 24 px |

### Sección (`.ed`)

| Elemento | Valor |
|---|---|
| Rejilla | dos columnas: rótulo de 200 px, sticky, y contenido, con 64 px de separación |
| Espaciado vertical | `padding: 32px 0 128px` |
| Divisor superior | 1 px `cielo-200` |
| Móvil | una columna; rótulo arriba; `padding-bottom` de 80 px |

### Medidas de lectura

| Texto | Ancho máximo |
|---|---|
| Entrada y filas | 600 px |
| Cierre y notas | 640 px |
| Título de sección | 760 px |

### Ritmo vertical

| Bloque | Separación superior |
|---|---|
| Título → entrada | 32 px |
| Bloques de demostración | 40 a 48 px |
| Subtítulo interno | 80 px |
| Filas (`ed__stack > div`) | 32 px arriba y abajo, cada una con línea de 1 px `cielo-100` |
| Cierre | 64 px |

---

## 4. Geometría

- **Radios** (tokens):

  | Token | Valor |
  |---|---|
  | `micro` | 3 px |
  | `control` | 12 px |
  | `component` | 18 px |
  | `card` | 30 px |
  | `block` | 50 px |
  | `pill` | 9999 px |

- **Regla de esquinas:** en un grupo de dos o más piezas, el borde que toca el límite del conjunto es recto y el que mira a otra pieza es curvo. Una pieza sola va recta. Por ejemplo:

  | Grupo | Pieza | `border-radius` |
  |---|---|---|
  | Par horizontal | izquierda | `0 30px 30px 0` |
  | | derecha | `30px 0 0 30px` |
  | Pila vertical | arriba | `0 0 30px 30px` |
  | | abajo | `30px 30px 0 0` |
  | Trío | central | redondeada en las cuatro esquinas |

- **Radios por tamaño:**
  - Tarjetas de demostración (~370 × 300 px): 30 px.
  - Fichas de estado: 18 px.
  - Paneles de menú desplegable: 12 px.
  - Opciones del menú: 8 px.
- **Píldora:** botones, buscador, rótulos, menús desplegables (botón) y pestañas.
- **Rectos (radio 0):** encabezados de capítulo, muestras de impresión en carrusel y renglones de muestra (barras grises de esqueleto).
- **Sombras:** casi no hay. Los contenedores se delimitan con un borde interior de 1 px `cielo-100` (`box-shadow: inset 0 0 0 1px #E0E7F1`). Solo los menús desplegables flotantes llevan sombra: `0 0 0 1px rgba(16,18,42,.06), 0 2px 6px rgba(16,18,42,.05), 0 24px 48px -16px rgba(16,18,42,.28)`.

---

## 5. Líneas

| Línea | Valor |
|---|---|
| Fina (separa filas y tablas) | 1 px `#E0E7F1` (`cielo-100`) |
| De sección | 1 px `#C6D5EC` (`cielo-200`) |
| De tabla entre columnas | **4 px `#C6D5EC`** a la izquierda de cada celda de valor |
| De bloque (carrusel LOG-010, DIS-003, cabeceras de patrón) | 4 px `#C6D5EC` arriba |
| De paso a paso (Sistema de Diseño) | 1 px `cielo-200`, vertical u horizontal, uniendo círculos numerados |
| Barra de progreso de carrusel | 1 px `cielo-100`; el relleno en Azul Cielo crece de izquierda a derecha |

---

## 6. Contenedores y componentes

### Tarjeta de muestra

| Propiedad | Valor |
|---|---|
| Fondo | `#FFFFFF` |
| Borde interior | 1 px `cielo-100` |
| Relleno | 24 a 40 px |
| Radio | según la regla de esquinas |

### Comparativo con texto detrás

- **Tarjeta:** dos tarjetas de igual altura, 8 px entre ellas, cada una de 240 a 300 px de alto.
- **Rótulo:**
  - Arriba a la izquierda (16 px, 20 px).
  - Píldora `cielo-100` de 12 px, con relleno de 4 por 10 px.
- **Botón «Leer más»:**
  - Abajo a la derecha, sin contenedor: ícono «más» del catálogo (18 px, trazo 2,5) y texto de 13 px, peso 500, Noche.
  - Al pasar el cursor, el texto se subraya en Cielo.
  - Al abrir, el «más» gira 45° y el texto pasa a «Volver».
- **Reverso:**
  - Fondo blanco, relleno de 40 px.
  - Título de 16 px, peso 600, Noche; texto de 16 px, interlineado 1,6, `#4B4D60`.
  - Aparece con un fundido de 0,35 s.

### Comparativo en columnas (`.cmpx`)

- **Columnas:** rótulos (`minmax(120px, .7fr)`) y dos columnas enmarcadas con 1 px `cielo-200`.
- **Cabecera:** 56 px; la columna correcta lleva fondo `cielo-200`.
- **Muestra:** 220 px de alto.
- **Filas:** de 64 px, separadas por líneas `cielo-100`, con texto de 15 px en `#6B6D7E`.

### Filas de reglas (`.ed__stack`)

El formato base del libro: rótulo de 13 px en `#6B6D7E`, texto de 17 px en `#4B4D60` y línea `cielo-100` entre filas.

### Tablas (`.matrix`)

- Primera columna de 200 px.
- Cabecera de 72 px de alto.
- Celdas con relleno de 20 a 24 px.
- Separación de 4 px `cielo-200` entre columnas.
- Línea inferior de 1 px `cielo-100`.

### Carrusel

| Tipo | Comportamiento |
|---|---|
| Horizontal (`.hcar`) | `scroll-snap`; dos piezas a la vista con 12 px de separación (tres en tramas, una en impresión); en móvil, cada pieza ocupa el 84 % |
| De diapositivas (`.mslide`) | una a la vista, avance automático de 3,2 s con barra de tiempo |

**Pie común:**
- Contador `(01 / 07)` de 13 px en `#6B6D7E`.
- Barra de 1 px `cielo-100`.
- Botones «Anterior» y «Siguiente» de 14 px, peso 500, Noche al 55 %; al pasar el cursor, 100 % y la flecha se desplaza 4 px.

### Acordeón (`details.promise`)

- **Fila:** grilla de 56 px (número), título y 36 px (botón).
- **Botón:** circular de 36 px.
- **Título:** 18 px, peso 500.
- **Texto:** 16 px, interlineado 1,65.
- **Apertura:** empieza cerrado; el primer ítem se abre solo, 450 ms después de entrar en pantalla.

### Menú desplegable (`.kdd`)

- **Título:** encima, fuera del botón, 12 px en `#6B6D7E`.
- **Botón:**
  - Píldora blanca, borde interior de 1 px `cielo-100`, alto de 40 px.
  - Valor de 13 px, peso 500, en `#4B4D60`.
  - Chevron del catálogo (14 px) girado 90°; 270° al abrir.
- **Al abrir o con foco:** borde de 1 px Cielo, sin halo.
- **Panel:** blanco, radio de 12 px, relleno de 6 px, sombra flotante, aparece con `translateY(-6px) scale(.985)` → 0 en 0,18 a 0,24 s.
- **Opciones:**
  - 14 px, relleno de 9 por 12 px, radio de 8 px.
  - Hover en `#F4F4F4`; la opción elegida, fondo `cielo-100` y peso 600.
  - Sin marca de verificación.
- **Probador:** seis menús del mismo ancho en una rejilla de seis columnas (tres bajo 900 px, dos bajo 520 px).

### Pestañas y segmentos

- Píldoras de 12 px, peso 500, relleno de 5 por 12 a 14 px.
- **Inactivas:** borde interior de 1 px `cielo-200` y texto `#4B4D60`.
- **Activa:** fondo Noche y texto Blanco.

### Insignias (`.badge`)

Píldora con relleno de 8 × 14 px, texto de 13 px, peso 600, Noche, fondo del color de estado y separación de 8 px con el ícono.

### Puntos de estado (`.dot`)

| Estado | Apariencia |
|---|---|
| Vigente | círculo de 8 px en Noche |
| Borrador | mitad Noche, mitad vacío, con aro de 1,5 px |
| Pendiente | aro de 1,5 px en `#A8AAB5` |

---

## 7. Botones

| Tipo | Reposo | Hover |
|---|---|---|
| Principal | píldora Salmón con texto Noche; 14 px, peso 700, MAYÚSCULAS, tracking +0,05em; relleno de 16 × 40 px | se endereza (radio 0), fondo Blanco y borde Salmón |
| Sólido | Noche con texto Blanco | radio 0, fondo Cielo y texto Noche |
| Contorno | transparente, borde interior de 1 px `cielo-200` | fondo Noche y texto Blanco |
| Cristal | `rgba(255,255,255,.1)`, borde `rgba(255,255,255,.3)`, desenfoque de 12 px, texto de 14 px, peso 500, sin mayúsculas | sin cambio de forma |
| De texto | 14 px, peso 500, Noche al 55 %, flecha de 16 px | 100 %; la flecha se mueve 4 px en su dirección |
| De ícono | círculo de 36 px, borde de 1 px `#A8AAB5` al 70 %, ícono de 20 px | relleno Noche e ícono blanco |
| Buscador de la cabecera | píldora con borde de 1,33 px Noche, relleno de 8 × 20 px, 14 px, peso 500 | — |

**Al pulsar:** todos los botones se reducen a `scale(.97)`.

---

## 8. Iconografía

- **Catálogo oficial** (`recursos/iconos.html`):
  - Lienzo de 32 px, área viva de 28 px, trazo de 2,5 px.
  - Remates rectos (`butt`) o cuadrados según el ícono.
  - Los íconos de relleno usan `fill="currentColor"`.
- **Uso en la interfaz:**
  - Ícono «más» de los comparativos.
  - Chevron de los menús desplegables.
  - Ícono de salida de la cabecera.
  - Los íconos del catálogo, con animación de trazo al pasar el cursor.
- **Flechas de navegación** (migas, menú lateral, botones de texto, buscador): **no salen del catálogo**. Son íconos de línea de 16 px con trazo de 1,6 px (`--icon-stroke`), remates redondeados.
- **Lápiz de edición en la escala:** 18 px, trazo de 2,5 px, Azul Cielo al 80 %; dibujado ad hoc.

---

## 9. Viñetas

| Propiedad | Valor |
|---|---|
| Formas | A: círculo con vacío cuadrado. B: cuadrado con vacío circular. Alternan siempre y abren con el círculo. |
| Tamaño en listas | 16 px |
| Color en el manual | Azul Noche (la variable `--vc` es Salmón por defecto) |
| Lista (`.vlist`) | dos columnas con 40 px de separación |
| Cada ítem | 12 px de relleno vertical, línea superior de 1 px `cielo-100`, texto de 15 px Noche, 12 px entre viñeta y texto |
| Selector de color (ILU-001) | anillo de 5 px del tono claro del color elegido, pegado a la muestra |

---

## 10. Tramas y texturas

- **Trama de encabezado:** líneas verticales finas sobre el cielo del encabezado de capítulo (`.portal__arcs`), con nubes encima.
- **Catálogo de tramas:**
  - Líneas de 1 px en Azul Noche sobre blanco, en mosaicos de 6 px.
  - Trazo «a mano»: filtro SVG `feTurbulence` (fractalNoise, `baseFrequency` .045, 2 octavas, `seed` 7) con `feDisplacementMap` de escala 1,8.
- **Rellenos de gráficos:** los mismos patrones de 6 px con el mismo filtro; las etiquetas no se deforman.
- **Grano:** textura SVG `fractalNoise` (`baseFrequency` .85, 3 octavas), disponible como `--grain`.

---

## 11. Filtros, cristal y nubes

- **Cristal:**

  | Parte | Valor |
  |---|---|
  | Fondo | `rgba(255,255,255,.24)`; fuerte `rgba(244,244,244,.62)` |
  | Borde | `rgba(255,255,255,.5)` |
  | Desenfoque | 24 px |
  | Sombra | `0 20px 50px -20px rgba(16,18,42,.28)` |

- **Cabecera:** fondo `rgba(244,244,244,.9)` con desenfoque de 16 px. En la portada, `rgba(114,155,221,.35)` con desenfoque de 36 px, que vuelve al anterior al hacer scroll.
- **Nubes en encabezados (todos los libros):**
  - **Forma:** cuatro `radial-gradient` blancos con alfa de .45 a .85.
  - **Opacidad en reposo:** .32 sobre cielo y .14 sobre oscuro.
  - **Al pasar el cursor:**
    - Opacidad .62 sobre cielo y .3 sobre oscuro.
    - Escala a 1,04 y sube 1 %.
    - Transición de 1,2 s en opacidad y 1,8 s en escala, curva `e-out`.
- **Viento:** el cielo de los encabezados se mueve con paralaje, con nubes calculadas y líneas curvadas por el gesto del cursor (canvas).

---

## 12. Movimiento

| Elemento | Valor |
|---|---|
| Duraciones | 180, 300 y 520 ms |
| Curvas | `e-out cubic-bezier(.22,.61,.36,1)` para entradas; `e-io cubic-bezier(.65,.05,.36,1)` para transformaciones (firma Keyons) |
| Aparición de secciones | `opacity 0 → 1` y `translateY(18px → 0)` en 0,8 s `e-out` al entrar en pantalla |
| Hover de enlaces y menú | cambio de color en 180 ms |
| Cartas | fundido de 0,35 s |
| Menús | 0,18 a 0,24 s |
| Movimiento reducido | con `prefers-reduced-motion` se desactivan transiciones y animaciones |

---

## 13. Hovers

| Elemento | Hover |
|---|---|
| Enlace cruzado (`.xref`) | siempre subrayado Cielo de 1,5 px con separación de 3 a 4 px; el texto pasa a `cielo-700` y el subrayado toma el color del texto |
| Ítem del menú lateral | fondo `cielo-100`, texto Noche, píldora abierta a la derecha (`0 9999px 9999px 0`) |
| Ítem activo del menú lateral | fondo `cielo-200`, peso 600 |
| Migas | de `#6B6D7E` a Noche |
| Tarjetas | sin elevación ni sombra |
| Ícono del catálogo | animación de trazo dibujado de 0,45 a 0,75 s |
| Logotipo de la cabecera | `scale(1.05)` en 300 ms |

---

## 14. Encabezado de capítulo (portal)

- **Tamaño:** alto `clamp(380px, 40vw, 540px)`, sin radio, ancho del capítulo; 96 px de separación inferior.
- **Fondo:** cielo fotográfico o degradado (Mediodía en Fundamentos); Azul Noche plano en el Sistema de Diseño.
- **Texto:**
  - Abajo a la izquierda, con 40 px de margen.
  - Kicker de 13 px; display TASA de 92 px a 1440.
  - Bajada de 17 px, interlineado 1,55, con un ancho máximo de 580 px.
- **Capas:** trama de líneas y nubes con hover.

---

## 15. Sistema de Diseño: prueba de diagramación natural (capítulo 01)

- **Bloque partido** (7/5; 5/7 en la variante invertida):
  - Muestra dentro de un panel blanco con radio según la regla de esquinas y relleno de 32 px.
  - A su lado, una lista de tres pasos con círculos numerados de 40 px:
    - fondo `cielo-100`, y el central en Noche con número blanco;
    - unidos por una línea de 1 px `cielo-200`.
- **Variante ancha:** panel arriba y tres pasos en columnas, unidos por una línea horizontal.
- **Par de lectura:** «Ejemplo de aplicación» y «Comprobación» en dos columnas. Títulos de 18 px, peso 500, Noche; texto de 16 px, interlineado 1,65.
- **Declaración del propósito:** título de `clamp(36px, 4.4vw, 60px)`.
