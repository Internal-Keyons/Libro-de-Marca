---
manual: "Libro de Marca Keyons"
version: "0.1"
fecha: "2026-11-02"
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

##### El radio depende del tamaño

Se elige mirando **el lado más corto del recuadro**: entre más grande, más radio. Cada ejemplo está en pareja porque, por la regla de esquinas, solo curvan las esquinas que se miran.

**r-micro**
3 px

**(Lado corto)**
Menos de 24 px
**(Se usa en)**
Barras de datos, chips internos, marcas pequeñas

**r-control**
12 px

**(Lado corto)**
24 a 64 px
**(Se usa en)**
Campos, fichas de color, segmentos

**r-component**
18 px

**(Lado corto)**
64 a 200 px
**(Se usa en)**
Tarjetas y recuadros de contenido

**r-card**
30 px

**(Lado corto)**
200 a 400 px
**(Se usa en)**
Paneles y tarjetas grandes

**r-block**
50 px

**(Lado corto)**
Más de 400 px
**(Se usa en)**
Secciones y bloques de página

**(Anidados)**
Un recuadro dentro de otro usa el radio exterior menos el relleno. Si el resultado es menor que 3 px, va recto.

**(En código)**
Siempre con su variable: `var(--r-card)`, nunca con un número suelto.
