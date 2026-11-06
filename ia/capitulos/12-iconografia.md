---
manual: "Libro de Marca Keyons"
version: "0.1"
fecha: "2026-11-06"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
capitulo: "12"
titulo: "Iconografía"
area: "Fundamentos"
estado: "borrador"
rutas: ["/fundamentos/iconografia/iconos.html"]
normas: ["KYN-MRK-ICO-001", "KYN-MRK-ICO-002", "KYN-MRK-ICO-003", "KYN-MRK-VIS-004", "KYN-MRK-ICO-004", "KYN-MRK-ICO-005", "KYN-MRK-ICO-006"]
referencias: ["KYN-MRK-COL-014", "KYN-MRK-ICO-001", "KYN-MRK-ICO-002", "KYN-MRK-ICO-003", "KYN-MRK-ICO-004", "KYN-MRK-ICO-005", "KYN-MRK-ICO-006", "KYN-MRK-VIS-004"]
---

# Capítulo 12 · Iconografía

Estado: borrador · Clave: iconografia · Ruta: `/fundamentos/iconografia/iconos.html` · Número anterior: 10, 13

Estilo de trazo, tamaños según contexto y catálogo.

**Contenido del capítulo**

- Retícula · borrador · `/fundamentos/iconografia/iconos.html#reticula`
- Familias y variantes · borrador · `/fundamentos/iconografia/iconos.html#familias`
- Uso · borrador · `/fundamentos/iconografia/iconos.html#uso`
- Animación · borrador · `/fundamentos/iconografia/iconos.html#animacion`
- Catálogo · borrador · `/fundamentos/iconografia/iconos.html#catalogo`
- Entrega técnica · borrador · `/fundamentos/iconografia/iconos.html#entrega`

## Iconografía

Rótulo: Capítulo 12 · Fundamentos · Fuente: `/fundamentos/iconografia/iconos.html`

Una familia de íconos sobre una misma retícula, lista para copiar y descargar.

## KYN-MRK-ICO-001 · 12.1 Retícula

Número: 12.1 · ID: `KYN-MRK-ICO-001` · Estado: vigente · Fuente: `/fundamentos/iconografia/iconos.html#reticula`

### Lienzo de 32, área viva de 28

Todos los íconos de interfaz se dibujan sobre la misma retícula. **Comparten lienzo, margen, grosor y guías**, por eso se ven de una misma familia.

- Lienzo de 32 px · Con 2 px de margen en cada lado: el dibujo vive en 28 × 28 px.
- Trazo de 2,5 px · El mismo en todos los íconos, sin trazos residuales.
- Formas guía · Círculo de 24, cuadrado de 22 y rectángulos de 26 × 20 y 20 × 26 px. Cada ícono usa la que se parece a su silueta, para que todos pesen igual a la vista.
- Terminaciones · Rectas, con uniones en ángulo. Sin texto ni números dentro del ícono.

**(¿Quién usa las guías?)**
Quien dibuja un ícono nuevo. Para usarlos en código basta el SVG del catálogo; a 16, 20 o 24 px todo se escala en proporción.

**(Íconos anchos)**
Nube, interruptor o lista caben en la familia: usan el rectángulo de 26 × 20 px, el mismo trazo y van centrados en vertical. Lo que rompe la familia no es el ancho, es el grosor o el estilo.

## KYN-MRK-ICO-002 · 12.2 Familias y variantes

Número: 12.2 · ID: `KYN-MRK-ICO-002` · Estado: vigente · Fuente: `/fundamentos/iconografia/iconos.html#familias`

### Dos familias, dos variantes

La familia define el uso; la variante, el estado. **En una misma vista no se mezclan.**

**(Interfaz · contorno)**
La variante por defecto: navegación, acciones y contenido.

**(Interfaz · sólida)**
Solo para el estado activo o seleccionado, y siempre como pareja de un ícono de contorno.

**(Ilustrativa)**
Más expresiva, para piezas de marca y estados vacíos. Retícula de 64 px y trazo de 2 px. Aquí van cohete, flor, planta o varita. Por desarrollar.

**(Marca o sistema)**
El isotipo { } es identidad y sigue las reglas del logotipo; «guardar» o «editar» son sistema y siguen esta retícula.

## KYN-MRK-ICO-003 · 12.3 Uso

Número: 12.3 · ID: `KYN-MRK-ICO-003` · Estado: vigente · Fuente: `/fundamentos/iconografia/iconos.html#uso`

### Tamaño, texto y contexto

Un ícono comunica mejor acompañado. **Solo, debe ser inequívoco.**

- Tamaños · 16, 20, 24 y 32 px. Debajo de 16 se pierde el trazo.
- Con texto · Ícono y etiqueta a 8 px de distancia, alineados al centro.
- Sin texto · Solo para acciones universales; siempre con nombre accesible.
- Estados · Éxito, error, advertencia, información, carga y bloqueo usan los colores de KYN-MRK-COL-014 y van con texto cuando son críticos.
- Agentes de IA · Estela y los demás agentes usan su avatar en la conversación y un ícono solo en espacios mínimos.
- Redes y servicios externos · Versión original del servicio, monocroma en Azul Noche o Blanco y al mismo tamaño óptico. Nunca se redibujan.

## KYN-MRK-VIS-004 · 12.3.1 Iconografía de relleno

Número: 12.3.1 · ID: `KYN-MRK-VIS-004` · Estado: vigente · Fuente: `/fundamentos/iconografia/iconos.html#vis-004`

### Un ícono tiene que ayudar a entender

No introducir íconos **únicamente para decorar** textos o títulos.

Los íconos deben favorecer orientación, comprensión, identificación o expresión visual justificada. Los íconos expresivos pueden utilizarse cuando existe una intención visual justificada.

> Recurso visual: Ejemplo dibujado: Nuestra visión · Crecimiento · Procesos

**(Uso incorrecto)**
**Un ícono genérico junto a cada titular** Una bombilla, un cohete o un engranaje que no dicen nada del contenido.

> Recurso visual: Ejemplo dibujado: Enviar solicitud · Acción · Norma vigente · Estado · Propuesta comercial · Categoría

**(Alternativa mejor)**
**Un ícono con función** El ícono identifica una acción, un estado o una categoría.

## KYN-MRK-ICO-004 · 12.4 Animación

Número: 12.4 · ID: `KYN-MRK-ICO-004` · Estado: vigente · Fuente: `/fundamentos/iconografia/iconos.html#animacion`

### Siempre en la misma dirección

Todos los íconos usan **la misma animación: aparecen desde el centro y se asientan en 550 ms**, para que la familia se mueva como una sola. Pase el cursor por el catálogo para verla.

**(Interfaz)**
Micro y funcional: 150 a 450 ms. Se anima al aparecer o al confirmar una acción, nunca en bucle.

**(Ilustrativa)**
Más expresiva, hasta 1,2 s. Se entrega como Lottie o SVG animado.

## KYN-MRK-ICO-005 · 12.5 Cómo se usan

Número: 12.5 · ID: `KYN-MRK-ICO-005` · Estado: vigente · Fuente: `/fundamentos/iconografia/iconos.html#catalogo`

### Tres colores, un solo trazo

Los íconos de la marca se usan en **tres colores y nunca en otros**. El trazo es siempre el mismo; lo que cambia es el fondo sobre el que viven.

Globo · #10122A

#### Azul Noche

El color de todos los días, sobre fondos claros.

Asterisco · #729BDD

#### Azul Cielo

Para destacar un ícono o marcar un estado activo.

Chat · #F4F4F4

#### Blanco Keyons

Sobre Azul Noche o sobre cielos profundos.

- Un color por vista · En una misma pantalla o pieza, todos los íconos comparten color.
- Con su etiqueta · Ícono y texto a 8 px, alineados al centro. Solo, si la acción es universal.
- Tamaños · 16, 20, 24 y 32 px. Se escala en proporción; el trazo no se engrosa.
- Estados · Éxito, error o advertencia usan los colores de estado de KYN-MRK-COL-014, nunca un color nuevo.

**(Archivo y catálogo)**
Cada ícono se pide por su nombre, por ejemplo keyons-buscar-noche.svg. El catálogo completo, para elegir el color, copiar el SVG o descargarlo en SVG, PNG o JPG, está en [Recursos](/recursos/iconos.html).

## KYN-MRK-ICO-006 · 12.6 Entrega técnica

Número: 12.6 · ID: `KYN-MRK-ICO-006` · Estado: vigente · Fuente: `/fundamentos/iconografia/iconos.html#entrega`

### Nombres y versiones claras

Cada archivo dice qué es y para qué tamaño. **El sistema crece sin romperse.**

| (Tema) | Regla |
|---|---|
| Nombre de archivo | `icon-{nombre}-{tamaño}.svg` · ej. icon-flecha-derecha-24.svg |
| Variantes | Sufijo `-solido` para la variante sólida |
| Carpetas | interfaz/ · ilustrativa/ · externos/ |
| Versiones | Semánticas: 1.0.0 · cambios menores suman el segundo número |
| Formatos | SVG para producto y web; PNG a 2× para documentos |
