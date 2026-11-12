---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-022"
titulo: "Lenguaje humano obligatorio en mensajes de espera"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-022 · Lenguaje humano obligatorio en mensajes de espera

Cuando el tiempo de espera supera 3 segundos y se activa mensaje descriptivo conforme a KYN-PRD-UIX-021, el mensaje **DEBE** describir qué está haciendo el sistema en lenguaje humano orientado a la acción, nunca con jerga técnica ni con loaders neutros vacíos.

#### **Ejemplos correctos**

* "Consultando 3 fuentes..."  
* "Verificando pago con SINPE Móvil..."  
* "Preparando tu resumen..."  
* "Analizando 12 documentos..."

#### **Ejemplos prohibidos**

* "Loading..." (jerga técnica en inglés)  
* "Procesando request..." (jerga técnica)  
* Solo icono giratorio sin texto acompañante

En operaciones que superan 10 segundos, el mensaje descriptivo DEBE evolucionar con detalle progresivo, no permanecer estático. La mente humana interpreta un mensaje estático prolongado como señal de que el sistema colgó.
