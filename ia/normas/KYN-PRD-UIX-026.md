---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-11"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-026"
titulo: "Diseño obligatorio de estados vacíos como oportunidad de guía"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-026 · Diseño obligatorio de estados vacíos como oportunidad de guía

Los estados vacíos NO se muestran nunca como pantalla en blanco, mensaje genérico "Sin datos" o pantalla de error. Todo estado vacío **DEBE** diseñarse como oportunidad de guía al usuario, cumpliendo tres reglas obligatorias.

* **Explicar en lenguaje humano por qué está vacío:** "Aún no tienes clientes registrados" en vez de "No hay resultados".  
* **Ofrecer al menos una acción concreta para salir del estado vacío:** Botón "Agregar tu primer cliente" o similar. La acción es siempre concreta y ejecutable desde el mismo componente.  
* **Diferenciar entre estado vacío inicial y estado vacío por filtro:** Cuando el usuario filtró y no hay resultados, el mensaje es distinto y sugiere ajustar el filtro ("Ningún cliente coincide con estos filtros. Prueba ampliar el rango de fechas.").
