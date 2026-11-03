---
manual: "Libro de Marca Keyons"
version: "0.1"
fecha: "2026-11-03"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-MRK-ESP-002"
titulo: "Radios"
numero: "9.2"
estado: "vigente"
capitulo: "09 Forma y espacio"
area: "Fundamentos"
fuente: "/fundamentos/forma/espacio.html#radios"
referencias: []
citada_por: ["KYN-MRK-VIS-006"]
---

# KYN-MRK-ESP-002 · Radios

Número: 9.2 · Estado: vigente · Capítulo: 09 Forma y espacio · Fuente: `/fundamentos/forma/espacio.html#radios`

##### El radio responde a la función

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
