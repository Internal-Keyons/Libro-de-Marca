---
manual: "Libro de Marca Keyons"
version: "0.1"
fecha: "2026-11-11"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
capitulo: "09"
titulo: "Geometría y espacio"
area: "Fundamentos"
estado: "vigente"
rutas: ["/fundamentos/forma/espacio.html"]
normas: ["KYN-MRK-ESP-001", "KYN-MRK-ESP-002", "KYN-MRK-VIS-003", "KYN-MRK-ESP-003"]
referencias: ["KYN-MRK-ESP-001", "KYN-MRK-ESP-002", "KYN-MRK-ESP-003", "KYN-MRK-VIS-003"]
---

# Capítulo 09 · Geometría y espacio

Estado: vigente · Clave: forma · Ruta: `/fundamentos/forma/espacio.html` · Número anterior: 08

El lenguaje geométrico de Keyons: esquinas, radios y espacio.

**Contenido del capítulo**

- **Geometría**
- Lenguaje geométrico Keyons · vigente · `/fundamentos/forma/espacio.html#esquinas`
- Sistema de radios y curvaturas · vigente · `/fundamentos/forma/espacio.html#radios`
- Proporciones · por definir
- **Espacio y ritmo**
- Sistema de espaciado · vigente · `/fundamentos/forma/espacio.html#espaciado`
- Contenedores · por definir
- Elevación · por definir

## Geometría y espacio

Rótulo: Capítulo 09 · Fundamentos · Fuente: `/fundamentos/forma/espacio.html`

Las reglas invisibles que ordenan cada pieza: esquinas, radios, espacio y retícula.

## KYN-MRK-ESP-001 · 9.1 Lenguaje geométrico

Número: 9.1 · ID: `KYN-MRK-ESP-001` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#esquinas`

### Exterior recto, interior curvo

La geometría de Keyons distingue entre **contenedores independientes y conjuntos visuales**.

Un contenedor aislado utiliza esquinas rectas como tratamiento base. Cuando varios elementos forman un conjunto reconocible, pueden combinarse esquinas exteriores rectas e interiores curvas para expresar su relación.

**(Fila)**
En un conjunto horizontal, las esquinas exteriores son rectas y las interiores pueden curvarse cuando refuerzan la agrupación.

> Recurso visual: Gráfico SVG en línea · «Fila de tres recuadros»

**(Pila)**
Se aplica el mismo principio en vertical, respetando los límites exteriores del conjunto.

> Recurso visual: Gráfico SVG en línea · «Pila de tres recuadros»

**(Cuadrícula)**
La combinación de esquinas responde a la organización visual. No todas las cuadrículas requieren curvas interiores.

> Recurso visual: Gráfico SVG en línea · «Cuadrícula de cuatro recuadros»

**(Un contenedor)**
Las cuatro esquinas permanecen rectas cuando el elemento se presenta de forma independiente.

**(Botones y badges)**
Los botones mantienen una geometría curva, diferenciada de los contenedores. Las variantes, estados y transiciones funcionales se especifican en el Sistema de Diseño.
Los badges se rigen por su función y variante documentada, sin asumir automáticamente una geometría universal para todas las etiquetas.

## KYN-MRK-ESP-002 · 9.2 Radios y curvaturas

Número: 9.2 · ID: `KYN-MRK-ESP-002` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#radios`

### El radio responde a la función

Los radios se seleccionan según **la función del elemento, su tamaño y su relación** con otros componentes.

El tamaño puede orientar la elección, pero no determina automáticamente que una superficie grande deba tener esquinas más redondeadas.

**r-micro**
3 px

**(Tamaño de referencia)**
Menos de 24 px
**(Se usa en)**
Barras de datos, chips internos, marcas pequeñas

**r-control**
12 px

**(Tamaño de referencia)**
24 a 64 px
**(Se usa en)**
Campos, fichas de color, segmentos

**r-component**
18 px

**(Tamaño de referencia)**
64 a 200 px
**(Se usa en)**
Tarjetas y recuadros de contenido

**r-card**
30 px

**(Tamaño de referencia)**
200 a 400 px
**(Se usa en)**
Paneles y tarjetas grandes

**r-block**
50 px

**(Tamaño de referencia)**
Más de 400 px
**(Se usa en)**
Secciones y bloques de página

**(Anidados)**
Cuando un contenedor curvo contiene otro elemento, los radios y el espacio interior deben mantener una relación visual coherente, evitando encuentros irregulares.
La fórmula del radio exterior menos el relleno puede utilizarse como referencia geométrica, pero debe comprobarse visualmente y no aplicarse de manera automática en todos los casos.

**(En código)**
Siempre con su variable: `var(--r-card)`, nunca con un número suelto.

## KYN-MRK-VIS-003 · 9.2.1 Geometría genérica

Número: 9.2.1 · ID: `KYN-MRK-VIS-003` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#vis-003`

### La geometría Keyons, no un radio para todo

La geometría de los elementos debe responder a **su función y relación compositiva**.

No aplicar el mismo radio a botones, campos, imágenes y contenedores únicamente por uniformidad.

En las composiciones de Keyons se aplica el principio de contenedores individuales rectos y agrupaciones con combinaciones justificadas de esquinas rectas y curvas.

> Recurso visual: Ejemplo dibujado: Cielo propio · Ver capítulo

**(Uso incorrecto)**
**El mismo radio en todo** Imagen, contenedor y botón con idéntico redondeo.

> Recurso visual: Ejemplo dibujado: Cielo propio · Ver capítulo

**(Alternativa mejor)**
**Radios según la función** La imagen y el texto forman un conjunto: exterior recto, interior curvo. El botón conserva su geometría curva.

## KYN-MRK-ESP-003 · 9.3 Sistema de espaciado

Número: 9.3 · ID: `KYN-MRK-ESP-003` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#espaciado`

### Todo se mide en múltiplos de 4

La escala de espaciado utiliza **incrementos de 4 px** para organizar márgenes, separaciones y rellenos de forma consistente.

Sus valores son referencias para construir relaciones espaciales claras. La escala no sustituye las necesidades específicas de tipografía, bordes, adaptación responsive o representación gráfica.

s1 · 4 px · Entre ícono y su borde
s2 · 8 px · Ícono y texto
s3 · 12 px · Entre elementos de una lista
s4 · 16 px · Dentro de controles
s5 · 20 px
s6 · 24 px · Dentro de tarjetas
s8 · 32 px · Entre bloques relacionados
s10 · 40 px
s12 · 48 px · Entre componentes
s16 · 64 px · Entre grupos de contenido
s20 · 80 px
s24 · 96 px · Entre secciones
s32 · 128 px · Aire de sección

**(Criterio de uso)**
Las separaciones se eligen según la relación entre los elementos y la densidad necesaria. No es obligatorio utilizar grandes espacios en todos los contextos ni comprimir una composición para mostrar más información.
Cuando la escala no resuelva una necesidad técnica justificada, la excepción debe documentarse en el sistema correspondiente.
