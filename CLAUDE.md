# Biblioteca Keyons · instrucciones para Claude

Este proyecto es la Biblioteca Keyons: un sitio que reúne los libros de Keyons. El primero es el libro de marca (libro-de-marca.keyonsia.com). Keylin Mendoza López decide todo lo visual y todo lo escrito.

## Fuente de verdad

Cuando dos fuentes no coinciden, manda la primera de esta lista:

1. `reglas-visuales.md`: las reglas, con valores, DEBE / NO DEBE y excepciones.
2. `css/tokens.css`: los valores que sostienen esas reglas.
3. El texto de las páginas del libro.
4. `css/libro.css`.

Si encontrás una contradicción, no la resuelvas por tu cuenta: avisale a Keylin y proponé cómo cerrarla.

## Alcance

- Los capítulos del Sistema de Diseño y el Laboratorio **no son referencia visual** hasta que Keylin diga que ya los editó. No copies estilos de ahí.
- Los formularios todavía no tienen reglas. Si hace falta uno, preguntá antes de diseñarlo.

## Normas en el libro: dos capas

Vale para el Sistema de Diseño y para todo capítulo que reciba normas (`reglas-visuales.md` R16 a R19).

- La página muestra solo la **capa de lectura**. Si Keylin no te pasó la capa de lectura de una norma, pedísela. No la escribas vos a partir del texto normativo.
- **Índices:** usan el nombre corto de cada ítem, no el titular.
- **Cada norma:** rótulo (ID y nombre corto), titular, fundamento con una frase destacada, y la norma en filas con su nivel: Debe, Debería o Puede. El modelo es el capítulo 01 Principios comunes y su archivo `capitulo-01-principios-comunes.md`.
- **Niveles (todos los libros, decisión de Keylin del 2026-11-12):** la palabra del nivel va dentro de la redacción, natural y en mayúscula y nunca como primera palabra: «Cada pantalla DEBE tener…». El ícono (el cuadrado de 8 px, `.nvl--fin` en `libro.css`, del mismo tamaño y colores que el punto de estado, con su etiqueta al pasar el cursor) va al final de la declaración, en línea y sin sangría, nunca junto a la palabra ni al inicio. Una declaración = un ícono. Las decisiones se registran en `data/niveles.json` (`tools/niveles.py`); «siempre» y «nunca» no se convierten solos. Cambiar un enunciado para meter el nivel es cambiar texto: se propone y Keylin lo aprueba.
  - Debe por defecto, en positivo y con precisión que cierre el límite.
  - No debe solo cuando la prohibición necesita fuerza explícita. Usa la marca de Debe y no va en las leyendas.
- **Leyendas:** en el menú lateral, solo los niveles; los estados (Vigente, Borrador, Por definir), en la franja de la portada.
- **Semibold** solo en la frase destacada de cada entrada. Nada más va en semibold.
- **La versión md es para usar con IA.**
  - No va en la página ni se enlaza desde las normas, y no hay botón de descarga dentro de los capítulos.
  - Todo libro de la Biblioteca tiene en el menú lateral los mismos dos ítems, con el mismo nombre y estilo: «Descargar PDF» y «Normas para IA». Cada uno descarga lo de su libro.
  - La genera `tools/exportar.py`: `ia/normas/<ID>.md`, `ia/sistema-diseno/<capítulo>.md` e `ia/sistema-diseno.md`.
- **Sin bloques «Normas relacionadas» ni «Relacionado»:** una referencia a otra norma va dentro del texto, con enlace.

## Interfaces de ejemplo

- No crees maquetas de interfaz en ningún capítulo hasta que Keylin te pase la hoja de componentes aprobada.
- Mientras tanto, el «Ejemplo de aplicación» va solo como texto.

## Redacción

- «Antes de escribir cualquier texto, leé reglas-de-voz.md y revisalo con su lista de la sección 9».
- Vale para una página, una norma, un rótulo, una interfaz o un mensaje. `reglas-de-voz.md` es la versión operativa del capítulo Voz y manda sobre tu costumbre.
- Las reglas que más se olvidan:
  - Trato de usted.
  - Ninguna oración empieza con «No».
  - Hasta 25 palabras por oración y 4 renglones por párrafo.
  - Voz activa y verbos precisos.
  - Comillas latinas.
  - Sin palabras gastadas ni muletillas.
  - Keyons nunca se compara con otros.
- Todo texto que escribas vos (rótulos, títulos de bloque, notas, botones) va en positivo, profesional y fácil de entender. Decí lo que hacemos, no lo que evitamos.
- Las secciones marcadas [NUEVA] de `reglas-de-voz.md` son un borrador. Aplicalas al escribir, pero no las copies al capítulo Voz del libro hasta que Keylin las apruebe.

## Protocolo de ajustes

Todo ajuste visual que Keylin pida o apruebe es una regla posible. Antes de cambiar nada:

1. **Clasificá el ajuste** y decíselo a Keylin en una línea:
   - **General:** vale para todo el libro y el producto.
   - **Local:** vale solo para esa pieza.
2. **Si es general:**
   - Escribí la regla en `reglas-visuales.md`, en su sección, con valor exacto y DEBE / NO DEBE.
   - Llevá el valor a un token en `css/tokens.css`.
   - Aplicala en **todas** las páginas donde corresponda, no solo en la que se estaba viendo. Listá las páginas que cambian.
3. **Si es local:** registrala en la sección 8 de `reglas-visuales.md` (Excepciones), con dónde, motivo y fecha.
4. **Si el ajuste contradice una regla existente:** no lo apliques como parche. Preguntale a Keylin si cambia la regla o si es una excepción.

## Prohibido

- Escribir valores sueltos en `libro.css`: colores HEX o `rgba()`, tamaños de letra, espacios, radios, duraciones o desenfoques que no salgan de un token. La única excepción son los ejemplos de «No hacer».
- Usar un comentario dentro del CSS como regla. Los comentarios solo dicen qué hace el código y citan la regla: `/* reglas-visuales 3.1 */`.
- Agregar `!important` nuevos. Si parece necesario, el problema es otro: avisá.
- Agregar selectores atados a una sola sección para corregir lo que una regla general debería resolver.
- **Cambiar textos del libro** sin permiso. Si una página dice algo distinto de `reglas-visuales.md`, proponé el texto nuevo y esperá la aprobación de Keylin.

## Antes de dar una tarea por terminada

- [ ] ¿Todo valor nuevo salió de un token?
- [ ] Si el ajuste era general, ¿quedó escrito en `reglas-visuales.md` y aplicado en todas las páginas que corresponden?
- [ ] Si era local, ¿quedó registrado como excepción?
- [ ] ¿Quedó algún texto del libro contradiciendo las reglas? Listalo con una propuesta de texto.
- [ ] ¿Le dijiste a Keylin qué páginas revisar en pantalla?

## Cómo hablarle a Keylin

- Es diseñadora y estratega creativa, no desarrolladora. Explicá en términos visuales: qué va a ver distinto y dónde.
- Antes de un cambio grande, mostrale la lista exacta de cambios y esperá su aprobación.
- Si algo no está claro, preguntá una cosa concreta en lugar de suponer.
