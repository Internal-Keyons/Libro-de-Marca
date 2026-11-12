---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-024"
titulo: "Estructura tripartita obligatoria de mensajes de error"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-024 · Estructura tripartita obligatoria de mensajes de error

Todo mensaje de error visible al usuario final **DEBE** cumplir la siguiente estructura fija de tres partes. Los códigos técnicos crudos ("Error 502", "NullPointerException", stack traces) están estrictamente prohibidos en la capa visible al usuario.

* **Parte 1 — Qué pasó (lenguaje humano):** Frase corta que describe la situación sin jerga técnica. Ejemplo: "El asistente no pudo verificar el pago en tiempo real."  
* **Parte 2 — Por qué (una línea máximo):** Explicación breve de la causa comprensible por un usuario no técnico. Ejemplo: "Conexión con SINPE interrumpida.  
* **Parte 3 — Qué hacer ahora (acción concreta con botón visible):** Botón o enlace de acción inmediata que resuelve la situación. Ejemplo: "Adjuntar comprobante manualmente.

Esta estructura tripartita convierte el momento de error, que es el momento de mayor vulnerabilidad emocional del usuario, en un momento de recuperación guiada y sensación de control. Es uno de los elementos de la firma UX Keyons conforme a KYN-PRD-UIX-012.
