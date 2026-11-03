---
manual: "Libro de Marca Keyons"
version: "0.1"
fecha: "2026-11-03"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-MRK-VIS-006"
titulo: "Geometría genérica"
numero: "11.6"
estado: "vigente"
capitulo: "11 Criterios visuales"
area: "Fundamentos"
fuente: "/fundamentos/criterio/antipatrones.html#vis-006"
referencias: ["KYN-MRK-ESP-001", "KYN-MRK-ESP-002"]
citada_por: []
---

# KYN-MRK-VIS-006 · Geometría genérica

Número: 11.6 · Estado: vigente · Capítulo: 11 Criterios visuales · Fuente: `/fundamentos/criterio/antipatrones.html#vis-006`

##### La geometría Keyons, no un radio para todo

**(Problema)**
Todo redondeado por igual, como en cualquier plantilla.

**(Criterio)**
La geometría de los elementos debe responder a su función y relación compositiva.
No aplicar el mismo radio a botones, campos, imágenes y contenedores únicamente por uniformidad.
En las composiciones de Keyons se aplica el principio de contenedores individuales rectos y agrupaciones con combinaciones justificadas de esquinas rectas y curvas.

> Recurso visual: Ejemplo dibujado: Cielo propio · Ver capítulo

**(Uso incorrecto)**
**El mismo radio en todo** Imagen, contenedor y botón con idéntico redondeo.

> Recurso visual: Ejemplo dibujado: Cielo propio · Ver capítulo

**(Alternativa mejor)**
La imagen y el texto forman un conjunto: exterior recto, interior curvo. El botón conserva su geometría curva.

- **Excepciones**: Los botones conservan su geometría curva. Las variantes y estados funcionales se especifican en el Sistema de Diseño. Las etiquetas y badges utilizan la geometría correspondiente a su función y variante documentada.
- **Relación**: KYN-MRK-ESP-001 (Regla de esquinas) y KYN-MRK-ESP-002 (Radios).
