# Normas estéticas del Libro de Marca frente a la interfaz real

**Fecha y base:** 2026-11-04, rama `consolidacion`, commit `3075e26`.

**Método:** comparé lo que dicen las normas con los estilos computados en el navegador (a 1440 px) y con los tokens y hojas de estilo del proyecto.

**Estados:**

| Estado | Significado |
|---|---|
| **Coincide** | el código aplica lo que dice la norma |
| **Parcial** | se aplica con diferencias menores o solo en parte |
| **Difiere** | el código hace otra cosa |

---

## Resumen

| Ámbito | Coincide | Parcial | Difiere |
|---|---|---|---|
| Color | 5 | 2 | 2 |
| Tipografía | 5 | 2 | 4 |
| Geometría y espacio | 5 | 1 | 1 |
| Líneas y elementos gráficos | 3 | 2 | 2 |
| Iconografía | 2 | 1 | 2 |
| Movimiento y accesibilidad | 3 | 1 | 1 |

Las diferencias que más se notan a la vista:
1. **Kicker:** la norma pide TASA Orbiter; el código usa Jakarta Bold.
2. **Tracking de los títulos:** la norma pide 0 en Jakarta; el código aplica −3 %.
3. **Flechas de la interfaz:** no salen del catálogo de íconos.
4. **Líneas:** los divisores son Azul Cielo y no los grises que describe la norma.
5. **Barras de 4 px entre columnas de tabla:** la norma no las contempla.

---

## 1. Color

| Norma | Lo que dice | Lo que aplica el código | Estado |
|---|---|---|---|
| COL-001 / COL-002 Paleta base | Blanco Keyons `#F4F4F4`, Azul Noche `#10122A`, Azul Cielo `#729BDD`, Salmón Tierra `#CE635D` | Mismos HEX en `tokens.css` y en uso | **Coincide** |
| Proporción de la paleta | 50 % Blanco · 20 % Noche · 20 % Cielo · 10 % Salmón, como orientación | La interfaz es casi toda Blanco y Noche; el Cielo aparece en líneas y señales, y el Salmón casi no aparece | **Parcial** (la norma dice que la proporción orienta y no obliga) |
| «El color señala, no escribe» | Sobre fondo claro el texto va en Azul Noche | Todo el texto usa Noche o grises propios; el Cielo nunca se usa para texto de lectura | **Coincide** |
| COL-013 Grises funcionales | Cuatro grises: `#10122A`, `#4B4D60`, `#6B6D7E`, `#A8AAB5`, más divisor `#E0E7F1` | Mismos valores. Además existe un quinto gris, «titular» `#8B8C92`, usado en todos los títulos de sección | **Parcial** (el gris titular no está documentado en COL-013) |
| COL-014 Estados | Fondos pastel y texto Azul Noche | Siete fondos pastel; las insignias y fichas usan texto Noche | **Coincide** |
| Salmón Atardecer | Solo sobre Azul Noche | Solo en viñetas y piezas sobre fondo oscuro | **Coincide** |
| Salmón y Cielo no se apoyan | Sin botones Salmón sobre Cielo ni al revés | No hay casos | **Coincide** |
| Color de foco | Token `--color-focus: Azul Cielo` | Contorno de foco de 2 px en **Azul Noche** (`:focus-visible`); los campos sí usan Cielo | **Difiere** |
| VIS-008 Contraste | Comprobar el contraste según la función | Títulos de sección en `#8B8C92` sobre `#F4F4F4`: unos 3,2:1. Cumple AA para texto grande (44 px), no para texto normal | **Parcial** |

## 2. Tipografía

| Norma | Lo que dice | Lo que aplica el código | Estado |
|---|---|---|---|
| TYP-001 Familias | Plus Jakarta Sans para la lectura, TASA Orbiter para protagonismo | Igual. TASA solo en el display de los encabezados, el probador y las muestras | **Coincide** |
| TYP-002 Display | TASA 500, 52 a 128 px, interlineado 0,93 | `clamp(52px, 8.6vw, 128px)`, 500, interlineado 0,93 a 0,98 | **Coincide** |
| Tracking del display (8.8) | −3 % de 52 a 79 px, −5 % desde 80 px | −4 % fijo en `.t-display` | **Difiere** |
| TYP-002 Título de sección | Jakarta 500, 30 a 44 px | `clamp(30px, 3.2vw, 44px)`, 500 | **Coincide** |
| Tracking de los títulos Jakarta (8.8) | 0em; la jerarquía se hace con tamaño, peso, posición y espacio | −3 % en los títulos de sección, −2 % en `.t-h3` y −1 % en los subtítulos | **Difiere** |
| TYP-002 Entrada | 18 a 20 px, 400, interlineado 1,55 | Igual | **Coincide** |
| TYP-002 Cuerpo | 16 a 17 px, interlineado 1,65 | 16 px de base con interlineado 1,6; filas de texto a 17 px con 1,65 | **Parcial** |
| TYP-004 Kicker | TASA Orbiter 500, mayúsculas, 14 px, +8 %, estrella a la izquierda | **Jakarta 700**, mayúsculas, 12 a 13 px, +2 %, estrella a la izquierda | **Difiere** (familia, peso, tamaño y espaciado) |
| Reglas de composición (8.2) | Título contextual de 20 px 500 Noche; declaración de 44 px 400 en gris; entrada y cuerpo en Azul Noche | En las páginas, la entrada y el cuerpo van en `#4B4D60` (gris 2), no en Noche | **Difiere** |
| TYP-005 Énfasis | Semibold con moderación | Negrita 600 en Noche dentro de entradas y textos | **Coincide** |
| TYP-006 Cifras | Cifras tabulares en datos comparables | `tabular-nums` en tablas, contadores y numeraciones | **Coincide** |

## 3. Geometría y espacio

| Norma | Lo que dice | Lo que aplica el código | Estado |
|---|---|---|---|
| ESP-001 Regla de esquinas | Exterior recto, interior curvo; una pieza sola, recta | Se aplica en comparativos, pares, tríos, pilas (VIS-010 ya corregido), tarjetas de estado y paneles | **Coincide** |
| ESP-002 Radios | 3 / 12 / 18 / 30 / 50 px según el tamaño | Tokens idénticos. Las tarjetas de unos 370 px usan 30 px, como corresponde | **Coincide** |
| Radios en código | Siempre con variable, nunca con número suelto | Hay radios sueltos en el CSS (8 px en las opciones del menú, 3 px en las barras de muestra, `50%` en los círculos) | **Parcial** |
| ESP-003 Espaciado | Múltiplos de 4 px | Escala de 4 a 128 px. Hay excepciones sueltas: 6, 10 y 14 px en rellenos de píldoras y menús | **Coincide** (con excepciones menores) |
| ESP-004 Retícula | Contenido hasta 1520 px en escritorio amplio; márgenes de 16, 32 y 64 px | Documento de 1600 px; contenido con padding de 64, 40 y 16 px | **Difiere** (ancho de 1600 en lugar de 1520, decisión de la ronda 13) |
| Medida de lectura | 55 a 75 caracteres en lectura prolongada | Entrada y filas limitadas a 600 px (unos 60 a 70 caracteres) | **Coincide** |
| ESP-005 Densidad | Composiciones limpias con espacio negativo | Secciones con 128 px de aire al final y 32 px entre filas | **Coincide** |

## 4. Líneas y elementos gráficos

| Norma | Lo que dice | Lo que aplica el código | Estado |
|---|---|---|---|
| ILU-003 Divisor | 1 px, Gris Bruma | 1 px **Azul Cielo 100** `#E0E7F1` | **Difiere** (el criterio cambió en la ronda 12 y la norma no se actualizó) |
| ILU-003 Divisor fuerte | 1 px, Azul Noche al 16 % | 1 px Azul Cielo 200 `#C6D5EC` sobre cada sección | **Difiere** |
| Líneas entre columnas de tabla | «Todas las líneas son finas» | Barras de 4 px `cielo-200` entre columnas | **Parcial** (pedidas en una ronda anterior; la norma no lo contempla) |
| ILU-001 Viñetas | Círculo con vacío cuadrado y cuadrado con vacío circular, de 16 a 20 px; el manual usa Azul Noche | Exactamente así, a 16 px y en Noche | **Coincide** |
| ILU-004 Cristal | Opacidad entre 60 y 80 % sobre cielo real | Token `--glass-bg` al 24 % (más transparente); la cabecera al 90 % | **Parcial** |
| ILU-007 Tramas | Trazos delgados, continuos y uniformes; Azul Cielo como color de referencia; sin grano ni difuminado | Desde la ronda 15, líneas en **Azul Noche** con trazo a mano (filtro de desplazamiento) | **Difiere** (el texto de la norma sigue diciendo Azul Cielo y «uniformes»; hay que actualizarlo) |
| ILU-009 Sombras | Sombras difusas solo sobre superficies expresivas, nunca en cada contenedor | Ningún contenedor lleva sombra; solo los menús flotantes | **Coincide** |
| Resaltado de cierre | Celeste que cubre la palabra completa | `rgba(114,155,221,.3)` con `box-decoration-break:clone` | **Coincide** |

## 5. Iconografía

| Norma | Lo que dice | Lo que aplica el código | Estado |
|---|---|---|---|
| ICO-001 Retícula | Lienzo de 32, área viva de 28, trazo de 2,5 px | El catálogo cumple | **Coincide** |
| ICO-005 Colores | Tres colores, un solo trazo | Noche, Cielo y Blanco en el catálogo y en la interfaz | **Coincide** |
| Uso de íconos del catálogo | Los íconos de la marca salen del catálogo | Las flechas de las migas, el menú lateral, los botones de texto, el buscador y los botones de ícono son **íconos de línea de 1,6 px que no están en el catálogo** (token `--icon-stroke: 1.6px`) | **Difiere** |
| Tamaño mínimo | Debajo de 16 px se pierde el trazo | Las flechas de las migas miden 12 px; las del menú lateral, 14 px | **Difiere** |
| Lápiz de edición (TYP-002) | — | Dibujado con el trazo de 2,5 px, pero no existe en el catálogo | **Parcial** (conviene sumarlo al catálogo) |

## 6. Movimiento y accesibilidad

| Norma | Lo que dice | Lo que aplica el código | Estado |
|---|---|---|---|
| Firma de movimiento | Curva `e-io (.65,.05,.36,1)`; duraciones de 180, 300 y 520 ms | Tokens idénticos y en uso en botones y menús | **Coincide** |
| Hover «Ráfaga» (memoria de proyecto) | Viento para el hover, sin ondas | Encabezados con viento y nubes; los botones usan enderezado de radio y desplazamiento de flecha | **Parcial** |
| VIS-007 Movimiento | Breve en herramientas, expresivo con intención; respetar el movimiento reducido | Todas las animaciones se desactivan con `prefers-reduced-motion` | **Coincide** |
| Ampliación de texto (TYP-005, criterio 07) | Ampliar texto y espaciado sin perder contenido | Unidades `clamp` y textos sin altura fija; sin desbordes en móvil en las páginas revisadas | **Coincide** |
| Foco visible | (ver Color) | Contorno de 2 px Noche en todo elemento enfocable | **Difiere** del token (Cielo) |

---

## Decisiones pendientes para alinear normas y código

| # | Tema | Opción A | Opción B |
|---|---|---|---|
| 1 | Kicker | Cambiar el código a TASA 500, 14 px, +8 % | Ajustar la norma TYP-004 a Jakarta 700, 13 px, +2 % |
| 2 | Tracking de títulos | Poner los títulos de sección y subtítulos a 0em (8.8) | Registrar −3 % como ajuste aprobado de esos títulos |
| 3 | Tracking del display | `.t-display` a −3 % hasta 79 px y −5 % desde 80 px | Mantener −4 % y registrarlo |
| 4 | Divisores | Actualizar ILU-003 a Azul Cielo 100 y 200 | Devolver el código a Gris Bruma y Noche al 16 % |
| 5 | Barras de 4 px en tablas | Documentarlas en ILU-003 como divisor de tabla | Volver a 1 px |
| 6 | Íconos de la interfaz | Reemplazar flechas y chevrons por los del catálogo (mínimo 16 px) | Documentar una familia de interfaz de 1,6 px |
| 7 | Color de foco | Usar Cielo en el contorno de foco | Cambiar el token a Noche |
| 8 | Gris titular `#8B8C92` | Añadirlo a COL-013 | Reemplazarlo por un gris documentado |
| 9 | Tramas en Noche y a mano | Actualizar el texto de ILU-007 | — |
| 10 | Entrada y cuerpo en Noche (8.2) | Aplicarlo en todo el libro | Limitar la regla a las piezas editoriales y mantener `#4B4D60` en el manual |
| 11 | Ancho de 1520 px | Actualizar ESP-004 a 1600 px | — |
