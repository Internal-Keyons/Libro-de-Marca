---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-11"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-032"
titulo: "Visibilidad de fuentes RAG según sensibilidad regulatoria del vertical"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-032 · Visibilidad de fuentes RAG según sensibilidad regulatoria del vertical

La visibilidad de fuentes que el modelo consultó mediante Retrieval-Augmented Generation se rige según la sensibilidad regulatoria del sector del vertical, no como default universal aplicado igual a todos los productos.

* **Verticales regulados (legal, salud, financiero, contable):** Fuentes visibles obligatorias en cada respuesta que provenga de RAG, con cita al documento origen. Requisito de compliance y de protección legal del cliente profesional.  
* **Verticales no regulados (gimnasio, spa, restaurante, retail general):** Fuentes bajo demanda mediante botón "Ver fuentes" o control equivalente. El usuario final típicamente no las requiere; el operador puede consultarlas si duda.  
* **Herramientas internas Keyons:** Fuentes visibles por default. El equipo Keyons trabaja con datos operativos críticos y requiere trazabilidad completa.

Cada vertical Keyons declara formalmente su nivel de visibilidad de fuentes en su Ficha Estándar de Producto conforme a KYN-PRD-FIC-002.
