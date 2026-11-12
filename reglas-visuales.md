# Reglas visuales Keyons

**Versión:** 0.1 · borrador para aprobación de Keylin Mendoza López
**Fecha:** 2026-11-09
**Origen:** Hoja de decisiones · Libro de marca Keyons (cada regla indica su fila: C01, T03, R07…)

Este archivo es la fuente única de las reglas visuales. Lo leen personas y cualquier IA antes de diseñar o programar. Si una página del libro, un comentario en el CSS o un ejemplo dice otra cosa, manda este archivo.

## Cómo se lee

- **DEBE / NO DEBE:** obligatorio. No se rompe sin una excepción registrada (sección 8).
- **PUEDE:** permitido, a criterio de quien diseña.
- Todo valor se usa desde su token (`var(--token)`), nunca escrito a mano.
- Los contrastes están medidos sobre Blanco Keyons #F4F4F4, salvo que se diga otro fondo.

## Alcance

- **Incluye:** libro de marca (Marca, Fundamentos, Modos, Aplicaciones, Recursos) y todo lo digital con identidad Keyons.
- **No incluye todavía:** los capítulos del Sistema de Diseño ni el Laboratorio. No se toman como referencia visual hasta que Keylin los edite.
- **No incluye todavía:** formularios (anillos de foco y error, B04). Se definen cuando se diseñe el primer formulario real.

## Pendientes (Keylin decide; mientras tanto vale el valor por defecto)

| N.º | Pendiente | Valor por defecto mientras tanto |
| --- | --- | --- |
| P1 | Botón Salmón con texto blanco: opción A, C, D o E | A: #CE635D con texto Azul Noche (4,9:1) |
| P2 | Subtítulo bajo un título pequeño (R04): el Gris titular no pasa contraste por debajo de 24 px | Subtítulos de menos de 24 px en gris terciario |
| P3 | Divisores: tres tipos de línea (sección 5.2) | La propuesta de 5.2 |
| P4 | Variantes de cielo numeradas (sección 1.8). Tres degradados actuales usan colores que no están entre los ingredientes de su cielo | Se conservan como están, marcados «a revisar» |
| P5 | B01 y B02 estaban mal descritos en la hoja. Esta versión sigue lo que hoy sale en pantalla (sección 4) | Lo que sale en pantalla |

---

## 1 · Color

### 1.1 Paleta base

| Nombre | HEX | Token | Función |
| --- | --- | --- | --- |
| Blanco Keyons | #F4F4F4 | `--k-blanco` | Fondo principal y espacio negativo |
| Azul Noche | #10122A | `--k-noche` | Texto principal, fondos oscuros, autoridad |
| Azul Cielo | #729BDD | `--k-cielo` | Color primario: superficies, señales, acción en producto |
| Salmón Tierra | #CE635D | `--k-salmon` | Acento cálido de identidad |
| Salmón Atardecer | #E99D9E | `--k-atardecer` | Acento claro, solo sobre Azul Noche |
| Superficie | #FFFFFF | `--k-puro` | Superficie elevada |

### 1.2 Escalas (C03, C04)

- Hay **tres escalas**: Azul Noche, Azul Cielo y Salmón Tierra, de 100 a 900 con medios pasos (150, 250…), interpoladas en OKLab.
- La escala de Azul Noche es la **única escala neutra**. La escala «Gris Keyons» se elimina.
- La escala oficial de Azul Noche es la del libro (800 #1D1F38 · 700 #3E3F53 · 600 #555667 · 500 #6C6D7B). Reemplaza la escala anterior (800 #2B2D42…).
- NO DEBE crearse un gris fuera de la escala de Azul Noche.

### 1.3 Grises de texto (C03)

Los niveles se separan por saltos grandes de contraste para que los textos no se vean del mismo tono. Cada nivel es un paso de la escala de Azul Noche.

| Nivel | Token semántico | Paso | HEX | Contraste | Uso |
| --- | --- | --- | --- | --- | --- |
| 1 · principal | `--color-text` | noche-900 | #10122A | 16,7:1 | Todo texto de lectura |
| 2 · secundario | `--color-text-2` | noche-650 | #494A5D | 7,9:1 | Texto de apoyo |
| 3 · terciario | `--color-text-3` | noche-500 | #6C6D7B | 4,6:1 | Rótulos, fechas, metadatos, números pequeños |
| Titular atenuado | `--color-text-title-muted` | noche-450 | #82838F | 3,4:1 | Solo titulares de 24 px o más (R10) |
| 4 · deshabilitado | `--color-text-disabled` | noche-350 | #A4A4AD | 2,2:1 | Solo deshabilitado; nunca texto que haya que leer |

- DEBE usarse siempre el token semántico, nunca el paso de escala directo.
- NO DEBE usarse opacidad para atenuar texto (por ejemplo, Azul Noche al 55 %). Se usa el nivel que corresponda.

### 1.4 Reglas de uso del color (7.4)

1. Sobre fondo claro, el texto DEBE ir en Azul Noche o en un gris de texto.
2. Azul Cielo y Salmón Tierra NO DEBEN apoyarse uno sobre otro: ni elemento Salmón sobre fondo Cielo, ni al revés.
3. Cuando conviven, Azul Cielo DEBE ocupar más superficie que Salmón Tierra. Salmón domina solo en piezas expresivas donde la calidez es el mensaje.
4. Salmón Atardecer DEBE usarse solo sobre Azul Noche (8,6:1).
5. Azul Cielo NO DEBE usarse para texto sobre Blanco Keyons (2,6:1). Solo superficies, líneas y señales.

| Texto sobre fondo | Contraste | Uso |
| --- | --- | --- |
| Noche sobre Blanco | 16,7:1 | Todo |
| Noche sobre Cielo | 6,5:1 | Todo |
| Noche sobre Salmón | 4,9:1 | Todo |
| Cielo sobre Noche | 6,5:1 | Todo |
| Atardecer sobre Noche | 8,6:1 | Todo |
| Blanco sobre Salmón | 3,8:1 | Solo texto de 19 px bold o más, y logotipo |
| Cielo sobre Blanco | 2,6:1 | Nunca texto |

### 1.5 Salmón Tierra (C02)

- Es el acento cálido de la marca: temperatura humana y contrapeso al celeste.
- NO DEBE comunicar error, pérdida, rechazo ni ningún estado negativo. El error usa el badge de error (1.7).

### 1.6 Acción principal (C01)

- **Producto e interfaz:** la acción principal DEBE ser Azul Cielo con texto Azul Noche (6,5:1).
- **Piezas de marca** (libro, sitio, presentaciones): la acción principal DEBE ser Salmón Tierra, y DEBE haber como máximo una por pantalla.
- Las demás acciones DEBEN usar el botón sólido Azul Noche o el de contorno.

### 1.7 Estados

| Estado | Fondo | Token |
| --- | --- | --- |
| Éxito | Verde tierra suave #D5E0D2 | `--color-status-success` |
| Advertencia | Mostaza suave #F4E8C1 | `--color-status-warning` |
| Error | Terracota suave #F0D0CB | `--color-status-error` |
| Información | Cielo suave #C6D5EC | `--color-status-info` |
| Revisión | Lila suave #D9D6ED | `--color-status-review` |
| Bloqueo | Naranja suave #F5D8B8 | `--color-status-locked` |
| Neutro | Gris suave #E0E1E5 | `--color-status-neutral` |

- Texto e ícono de un estado DEBEN ir en Azul Noche; el color vive en el fondo (R08).
- Un estado DEBE comunicarse también con forma, ícono o texto, no solo con color.

### 1.8 Cielos (C06, C07)

- Hay **cinco cielos oficiales**: Amanecer, Mediodía, Atardecer, Noche y Galaxia. Cada uno es una escena distinta.
- Cada cielo tiene **ingredientes fijos** (su lista de colores) y PUEDE tener **variantes numeradas** (`--sky-amanecer-02`, `-03`…). La variante 01 es la oficial.
- Toda variante DEBE construirse solo con los ingredientes de su cielo. (P4: tres variantes actuales no cumplen; quedan marcadas «a revisar».)
- Ingredientes de Amanecer: #FFEBB1 · **#FFCE49** · #FED8B5 · #E99D9E · #729BDD · #2A4275 · #10122A · #B2BFE5 · #D4DBA5 · #A8C2A0. (Se corrige #FFCE86 por #FFCE49, que es el que usa el degradado.)
- Frecuencia: Mediodía, 40 a 50 % de las piezas expresivas; Galaxia, 5 a 10 %.
- Los degradados de cada área del libro NO son cielos: se llaman `--area-*` (C07).

### 1.9 Degradados (7.9)

1. DEBEN construirse en casa. NO DEBEN usarse degradados, imágenes ni ilustraciones de galería.
2. El color más luminoso DEBE ir donde estaría la fuente de luz.
3. Las transiciones DEBEN ser suaves: varias paradas, sin bandas.
4. DEBE haber una zona densa y una tranquila.
5. Se usan de tres a seis colores del cielo dominante.

### 1.11 Grises en gráficos

Los gráficos usan dos grises de la escala Azul Noche, cada uno con su función:

| Token | Paso | HEX | Uso |
| --- | --- | --- | --- |
| `--chart-gris` | noche-200 | #C6C7CB | Un dato que se muestra en gris (Esferas en órbita, la parte gris de la Medialuna) |
| `--chart-vacio` | noche-150 | #DDDDDF | Lo que no tiene dato o queda fuera de foco: el resto de las unidades, la parte vacía de una barra, los meses que acompañan al protagonista |

- Un gris de dato DEBE ser `--chart-gris`; un fondo sin dato DEBE ser `--chart-vacio`, para que nunca se confundan.
- NO DEBE usarse Azul Cielo claro como gris.

### 1.12 Portadas de los libros

- La portada de cada libro (selector de la Biblioteca y miniatura de la cabecera) DEBE ser Azul Cielo liso (`--cover-bg`) con su trama en línea blanca (`--cover-line`; al pasar el cursor, `--cover-line-hover`).
- NO DEBE llevar degradado. Los libros en preparación se atenúan con el mismo color.

### 1.10 Valores sueltos (C08)

- Todo color DEBE salir de un token.
- La única excepción son los ejemplos de «No hacer», que PUEDEN mostrar colores fuera de paleta.

---

## 2 · Tipografía

### 2.1 Familias

- **Plus Jakarta Sans:** lectura, interfaz, títulos de ítem, cifras operativas (con cifras tabulares en tablas).
- **TASA Orbiter:** titulares de exhibición, portadas y cifras editoriales.
- NO DEBE usarse una tercera familia, salvo monoespaciada para código.

### 2.2 Escala de lectura (T01)

Solo cinco tamaños para lectura e interfaz: **12 · 14 · 16 · 20 · 24 px**.

| Nivel | Tamaño | Peso | Interlineado | Tracking | Color |
| --- | --- | --- | --- | --- | --- |
| Título menor (ítem, categoría) | 20 px | 600 | 1,2 | −0,02 em | Azul Noche |
| Entrada | 20 px | 400 | 1,5 | 0 | Azul Noche |
| Cuerpo | 16 px | 400 | 1,6 | 0 | Azul Noche |
| Pequeño | 14 px | 400 | 1,55 | 0 | Gris de texto 2 o 3 |
| Rótulo | 12 px | 500 | 1,4 | 0 | Gris de texto 3 |

- NO DEBEN usarse 9, 10, 11, 13, 15, 17 ni 18 px. Se pasa al tamaño de la escala más cercano.
- Los pasos responsivos de lectura saltan de un tamaño de la escala al siguiente; nunca quedan entre dos.

### 2.3 Escala de exhibición (T02, T03, T04)

Cuatro tamaños, fluidos entre un piso y un techo:

| Token | Rango | Familia y peso | Interlineado | Tracking | Uso |
| --- | --- | --- | --- | --- | --- |
| `--fs-title-s` | 32 px | Plus Jakarta Sans 500 | 1,1 | −0,03 em | Título de bloque |
| `--fs-title` | 32 → 44 px | Plus Jakarta Sans 500 | 1,08 | −0,03 em | Título de sección, en Gris titular |
| `--fs-display-m` | 52 → 80 px | TASA Orbiter 500 | 0,95 | −0,03 em | Titular editorial |
| `--fs-display` | 56 → 128 px | TASA Orbiter 500 | 0,9 | −0,05 em | Portada y declaración principal |

- El display NO DEBE pasar de 128 px.

### 2.4 Tracking (T05, T06)

Solo seis valores:

| Token | Valor | Uso |
| --- | --- | --- |
| `--tr-0` | 0 | Lectura, datos, tablas |
| `--tr-1` | −0,02 em | Plus Jakarta Sans de 20 a 24 px |
| `--tr-2` | −0,03 em | Plus Jakarta Sans desde 32 px; TASA Orbiter de 52 a 79 px |
| `--tr-3` | −0,05 em | TASA Orbiter desde 80 px |
| `--tr-kicker` | +0,02 em | Kicker |
| `--tr-caps` | +0,05 em | Texto de botón en mayúsculas |

### 2.5 Kicker (ya decidido, T07)

- Plus Jakarta Sans 700, 12 px, mayúsculas, tracking +0,02 em, interlineado 1, Azul Noche.
- Lleva la estrella de marca de 12 px a la izquierda. NO DEBE repetirse a la derecha.
- Separador entre niveles: punto medio, sin punto final.

### 2.6 Títulos y texto

- **R04 · Un solo color:** un título DEBE ir en un solo color. PUEDE destacarse una parte en Azul Noche solo cuando la frase lo justifica. Con título pequeño y subtítulo, el título va en Azul Noche y el subtítulo en Gris titular si mide 24 px o más; si mide menos, en gris terciario (P2).
- **R05 · Destacado:** dentro del texto se destaca con semibold en Azul Noche. La idea clave se marca con Azul Cielo, sin comillas ni recuadros.
- **R18 · Semibold:** el semibold DEBE usarse solo en dos casos: la frase destacada de cada entrada (una por entrada) y los rótulos en recuadro blanco sobre una imagen, que van pegados al borde izquierdo, sin margen. Nada más va en semibold: filas, listas y enunciados, en peso regular.
- **R06 · Enlaces:** letra Azul Noche, subrayado Azul Cielo. «Leer más» va sin contenedor; el subrayado aparece solo al pasar el cursor.
- **R10 · Gris titular:** solo en titulares de 24 px o más. Números y rótulos pequeños van en gris terciario.
- **R11 · Renglones:** un título que no cabe DEBE ir en dos renglones equilibrados y NO DEBE cortarse. Un párrafo NO DEBE terminar con una palabra suelta en el último renglón.
- Un párrafo desarrolla una sola idea y ocupa como máximo cuatro líneas en la columna de lectura (10.5).

---

## 3 · Forma y espacio

### 3.1 Regla de esquinas

- Un elemento solo DEBE llevar esquinas rectas.
- En un conjunto de dos o más elementos, el lado que toca el límite del conjunto termina recto y el que mira a otro elemento se curva.
- Los controles de una línea (botón, campo, badge, buscador) DEBEN ser píldora (F01, F02).

### 3.2 Radios (F03)

El radio de una esquina curva sale del **lado corto** del elemento:

| Lado corto | Token | Radio |
| --- | --- | --- |
| Menos de 24 px | `--r-micro` | 3 px |
| 24 a 64 px | `--r-control` | 12 px |
| 64 a 200 px | `--r-component` | 18 px |
| 200 a 400 px | `--r-card` | 30 px |
| Más de 400 px | `--r-block` | 50 px |

- En elementos anidados, el radio interior se toma como el radio exterior menos el relleno, y se comprueba a la vista.

### 3.3 Separaciones (F04)

| Token | Valor | Entre |
| --- | --- | --- |
| `--gap-fusion` | 0 | Partes de un mismo ítem |
| `--gap-list` | 12 px | Ítems del mismo tipo en secuencia |
| `--gap` | 24 px | Valor por defecto |
| `--gap-component` | 48 px | Componentes |
| `--gap-section` | 64 px | Grupos distintos |

- Todo espacio DEBE ser múltiplo de 4 y salir de la escala `--s1` a `--s32`.

### 3.4 Medida de lectura (F05)

- Los párrafos DEBEN medir de 600 a 640 px (`--measure`).
- Tablas, demostraciones y diagramas PUEDEN usar todo el ancho disponible.

### 3.5 Composición editorial

- **R01 · Sin cajas por defecto:** la información se ordena con rótulo a la izquierda, contenido a la derecha, líneas finas y espacio negativo. Una tarjeta solo cuando agrupa algo.
- **R02 · Viñetas:** miden 20 px y dejan 20 px hasta el texto. En listas de color alternan círculo y cuadrado, en secuencia Azul Cielo → Salmón Tierra. Las listas cortas van en Azul Noche.
- **R03 · Sin tachados:** lo que no se usa va en gris o con la etiqueta «Antes».
- **R12 · Menús desplegables:** ventana recta, hacia abajo y pegada al campo.
- **R13 · Tablas:** filete Cielo arriba y abajo, columnas separadas por barras continuas de 4 px en Cielo 200.
- Entre dos bloques hay una sola línea divisoria (10.5). Si un bloque cierra con su línea y el siguiente abre con la suya, el anterior cierra sin línea. El libro lo aplica solo en toda página (`js/libro.js`) y `tools/lineas-dobles.js` lo comprueba.
- **R15 · Subtítulo y lista:** una lista que va bajo un subtítulo DEBE empezar a 32 px de él (`--s8`). NO DEBE quedar pegada al subtítulo.
- **R16 · Dos capas por norma:** en el libro, cada norma DEBE mostrar solo su capa de lectura: lo importante y lo obligatorio, corto y explicado.
  - Cada norma DEBE seguir este orden (Sistema de Diseño, capítulo 01 Principios comunes):
    1. Rótulo: el ID en gris terciario de 12 px y debajo el nombre corto en 14 px, sin estado.
    2. Titular.
    3. Fundamento: la entrada de 20 px, con una sola frase destacada.
    4. Norma: filas con su nivel a la izquierda y el enunciado a la derecha, en 16 px, peso regular, con un máximo de dos renglones.
  - **Tres niveles: Debe, Debería y Puede.** Cada enunciado empieza con un cuadrado de 8 px (`--lvl-mark`), del mismo tamaño y colores que el punto de estado. La palabra del nivel va dentro de la frase, en mayúscula: «Cada pantalla DEBE tener una acción principal…».
    - Debe: cuadrado lleno en Azul Noche. Obligatorio, sin excepciones.
    - Debería: cuadrado a medias en Azul Noche. Lo que se hace por defecto; otra solución necesita un motivo escrito.
    - Puede: cuadrado de contorno gris. Una alternativa permitida, a elección.
  - El nivel NO DEBE ser la primera palabra del enunciado ni ir en una etiqueta aparte.
  - **Debe y No debe:** por defecto se usa Debe, en positivo y con precisión suficiente para cerrar el límite («solo», «únicamente»). No debe es la excepción, cuando la prohibición necesita fuerza explícita y el positivo queda forzado. Usa la marca de Debe y NO DEBE aparecer como un nivel aparte en las leyendas.
  - Cada marca muestra su significado al pasar el cursor o con el foco: la etiqueta de los gráficos (`.ctip`), en Azul Noche con texto Blanco Keyons de 12 px y sombra `--shadow-2`.
  - **Leyendas:** el menú lateral muestra solo los niveles de norma. Los estados (Vigente, Borrador, Por definir) se explican en la portada de cada libro, en una franja horizontal sobre el carrusel.
  - Un bloque que es una lista va como lista corta; uno que es una secuencia, como pasos numerados.
  - El texto normativo completo NO DEBE ir en la página, ni abierto, ni en un acordeón, ni enlazado desde las normas. Es para usar con IA y vive en la versión md, que genera `tools/exportar.py`.
  - **Menú lateral de todo libro de la Biblioteca:** DEBE tener los mismos dos ítems, con el mismo nombre, ícono y estilo: «Descargar PDF» y «Normas para IA». Cada uno descarga el contenido de su libro.
  - NO DEBE haber un botón de descarga dentro de los capítulos.
- **R17 · Referencias entre normas:** NO DEBE haber bloques «Normas relacionadas» ni «Relacionado». Una referencia a otra norma va dentro del texto, con enlace («según la norma de revelación progresiva»).
- **R19 · Índices:** cada ítem de un índice DEBE usar el nombre corto de su sección (Esencia, Propósito, Marco biocognitivo), NO el titular.
- **R20 · Lectura continua:** cuando una sección necesita varios párrafos seguidos, sin filas ni datos, el texto DEBE ir lineal: subtítulo con su línea de grupo y párrafos cortos de 16 px, interlineado 1,65, separados por 20 px (`--s5`), en la medida de lectura (`--measure`).
  - Cada párrafo desarrolla una idea y ocupa como máximo cuatro renglones.
  - La idea clave PUEDE marcarse con Azul Cielo dentro del texto, una sola por bloque.
  - Se usa cuando el contenido es texto. Si la información tiene partes, pasos o datos, va en el componente que corresponde.

---

## 4 · Botones

Esta sección describe lo que hoy sale en pantalla (P5).

### 4.1 Base común (R07)

- Plus Jakarta Sans 700, 14 px, mayúsculas, tracking +0,05 em.
- Relleno de 16 × 40 px. Píldora. Borde de 1,5 px.
- Transición de 300 ms. Presionado: escala al 97 %. Deshabilitado: opacidad al 50 %.
- NO DEBE ponerse en negrita al pasar el cursor.
- Ícono de 20 px con trazo de 1,6 px. La flecha se desplaza 4 px en su dirección al pasar el cursor.
- **Se enderezan al contacto:** solo los botones de acción (principal y sólido) pierden la curva al pasar el cursor (radio 0).

### 4.2 Variantes

| Variante | Reposo | Al pasar el cursor | ¿Se endereza? |
| --- | --- | --- | --- |
| Principal de producto | Fondo Azul Cielo, texto Azul Noche | Fondo Blanco Keyons, borde Azul Cielo | Sí |
| Principal de marca | Fondo Salmón Tierra, texto Azul Noche (P1) | Fondo Blanco Keyons, borde Salmón Tierra | Sí |
| Sólido | Fondo Azul Noche, texto Blanco Keyons | Fondo Azul Cielo, texto Azul Noche | Sí |
| Contorno | Sin fondo, borde Azul Cielo 1,5 px, texto Azul Noche | Fondo Azul Noche, texto Blanco Keyons | No |
| Ícono | Círculo de 36 px, borde 1 px Gris Plata al 70 %, ícono gris terciario | Fondo Azul Noche, ícono blanco | No |
| Texto | 14 px, 500, gris terciario | Azul Noche; la flecha se desplaza 4 px | No |
| Cristal (sobre imagen o cielo) | Blanco al 10 %, borde blanco al 30 %, desenfoque de 12 px, texto blanco | Blanco al 20 % | No |

- El botón de texto pasa de Azul Noche al 55 % (3,97:1, no alcanza) a gris terciario (4,6:1), como manda R10.
- Un control que se llena de Azul Noche al pasar el cursor DEBE perder su borde: el relleno ya marca el límite (botones SVG, PNG y JPG de LOG-001, filtros, chips).

### 4.3 Botón de barrido (B03)

- Lo usan Buscar y Lab en la cabecera: un solo botón, sin anillo. En reposo, sin borde.
- Al pasar el cursor, el relleno barre de izquierda a derecha, termina en blanco y DEBE aparecer un borde Azul Noche de 1,5 px (`--line-w-control`).
- Las otras tres versiones anteriores quedan eliminadas.

### 4.4 Halo (R09)

- El halo de color DEBE usarse solo para estados (error, aprobado, requerido). NO DEBE ser decorativo.

### 4.5 Foco

- El anillo de foco (2 px Azul Noche) DEBE aparecer solo al navegar con el teclado: Tab, flechas, Inicio o Fin.
- Un clic, un toque o una tecla suelta (Shift, Windows, Ctrl, Alt, por ejemplo al tomar una captura) NO DEBEN mostrarlo.
- Los campos de texto conservan su indicador de foco siempre.
- `js/libro.js` marca la navegación con teclado (`data-kbd`) y cada estilo de foco del CSS se escribe como `[data-kbd] X:focus-visible`.

---

## 5 · Cristal, líneas, tramas y sombras

### 5.1 Cristal (V01, V02, V03)

- El cristal está permitido solo cuando cumple una función: leer sobre una imagen o un cielo, o separar una capa. NO DEBE usarse como adorno.
- Hay **dos intensidades de desenfoque**: 12 px (`--blur-1`, controles sobre imagen) y 22 px (`--blur-2`, cristal acanalado y ventana esmerilada). NO DEBE usarse otra.
- **Cristal acanalado** (firma): desenfoque de 22 px, velo blanco al 6 % y una línea de 1 px cada 50 px. Sin brillo ni resplandor.
- **Trama de cada libro:** Marca y Experiencia, líneas verticales; Sistema de Diseño, retícula horizontal y vertical. Sobre Azul Noche la línea se mantiene y el sombreado pasa a oscuro.
- **Ventana esmerilada:** cielo esmerilado afuera, nítido adentro, con el desenfoque de 22 px.

### 5.2 Líneas (V04, P3)

Tres tipos de línea, cada uno con su función:

| Tipo | Grosor | Color | Función |
| --- | --- | --- | --- |
| Fila | 1 px | Cielo 100 #E0E7F1 | Separa ítems del mismo grupo |
| Grupo | 1 px | Azul Noche | Abre un grupo; va sobre todo subtítulo |
| Estructura | 4 px | Cielo 200 #C6D5EC | Columnas de tablas y bloques estructurales |

- El color dice el nivel; el grosor solo marca estructura.
- Todo subtítulo de sección (`.ed__sub`) DEBE abrir con la línea de grupo, sin importar lo que venga debajo: filas, párrafos, listas o un ejemplo. Si el bloque anterior cierra con su línea, ese cierre se quita (3.5, una sola línea).
- NO DEBE crearse un cuarto tipo de línea. Si hace falta más separación, se usa espacio.
- Los bordes de controles miden de 1 a 1,5 px.

### 5.3 Sombras (V05)

Las sombras se usan cuando comunican elevación: algo que flota sobre el resto (menús desplegables, paneles, ventanas, la píldora activa del menú, el panel de Estela) y la profundidad atmosférica. Son siempre suaves, gaussianas, en Azul Noche con baja opacidad, nunca negras. Hay tres niveles con token. NO DEBEN usarse como adorno ni en todas las tarjetas.

| Token | Valor | Uso |
| --- | --- | --- |
| `--shadow-1` | 0 1px 2px rgba(16,18,42,.06), 0 4px 12px -2px rgba(16,18,42,.08) | Píldora activa, controles flotantes |
| `--shadow-2` | 0 8px 24px -6px rgba(16,18,42,.14) | Menús y desplegables |
| `--shadow-3` | 0 20px 50px -20px rgba(16,18,42,.28) | Ventanas y paneles; es la sombra que ya tenía el cristal |

---

## 6 · Íconos

- Lienzo de 32 px y área viva de 28 px. Trazo de 2,5 px en el lienzo de 32, que escala en proporción: 1,6 px a 20 px (M01). Así coinciden el catálogo y el código.
- Terminaciones rectas, uniones en ángulo. Sin texto ni números dentro del ícono.
- Tamaños: 16, 20, 24 y 32 px. NO DEBE usarse por debajo de 16 px.
- Colores: Azul Noche, Azul Cielo o Blanco Keyons. Un solo color por vista.
- Con texto, a 8 px de distancia y alineado al centro.
- Interfaz: contorno por defecto; sólido solo para activo o seleccionado.

---

## 7 · Movimiento

**Principio:** el movimiento de Keyons se siente como viento, no como líquido.

| Token | Valor | Uso |
| --- | --- | --- |
| `--m-fast` | 180 ms | Color y fondo al pasar el cursor |
| `--m-base` | 300 ms | Transformaciones, botones, íconos de interfaz |
| `--m-slow` | 520 ms | Entradas de bloques y transiciones de página |
| `--m-icon` | 550 ms | Animación de íconos en catálogo e ilustrativos (M02) |

| Curva | Uso |
| --- | --- |
| `--e-out` | Entradas y cambios de color |
| `--e-io` | Firma de movimiento Keyons: transformaciones |
| `--spring-lift` | Resorte de elevación (uso a documentar en la limpieza) |
| `--spring-line` | Resorte de líneas (uso a documentar en la limpieza) |

- NO DEBEN usarse otras duraciones (320, 420, 500, 515 ms pasan a la más cercana).
- Los íconos de interfaz se animan al aparecer o al confirmar; nunca en bucle.
- **Pasos con salto:** en una secuencia de pasos con arcos (portada del Sistema de Diseño), un punto Azul Cielo de 8 px recorre cada arco en `--m-slow` con `--e-io`. Al aterrizar aparece el texto de ese paso con `--m-base` y el arco queda marcado.
  - Se reproduce una sola vez, al entrar en pantalla.
  - Con movimiento reducido, todo se ve sin animación.
- **R14 · Aparición al desplazar:** la información entra a medida que se lee, con una sola animación de entrada para todo el libro.

---

## 8 · Excepciones registradas

Toda excepción a una regla DEBE anotarse aquí. Un comentario en el CSS no cuenta como excepción.

| N.º | Regla | Dónde | Motivo | Aprobó | Fecha |
| --- | --- | --- | --- | --- | --- |
| E1 | 3.5 · Carruseles | Estela 5.1 (dos dimensiones y Prisma) y Elementos gráficos 11.8 | Piloto de los puntos de carrusel: círculo y cuadrado alternados de 10 px (`--mark-car`); el activo se llena con el tiempo y la marca salta al siguiente cambiando de forma (`--m-base`, `--e-io`). Si se aprueba, pasa a regla para todos los carruseles | Pendiente | 2026-11-11 |
