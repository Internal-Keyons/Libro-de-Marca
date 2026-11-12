---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-11"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-043"
titulo: "Manejo lingüístico de fallos y respuestas de \"no sé\" del modelo"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-043 · Manejo lingüístico de fallos y respuestas de "no sé" del modelo

Cuando el modelo no tiene información suficiente para responder con calidad, la respuesta **DEBE** ser honesta y orientar al usuario hacia una alternativa productiva. Prohibidas las respuestas evasivas, las alucinaciones para "salvar" la respuesta, o los mensajes genéricos de sistema.

#### ***Estructura obligatoria de respuesta ante limitación del modelo***

* Reconocimiento explícito de la limitación en lenguaje humano.  
* Explicación breve de la causa cuando corresponda (falta información, tema fuera de dominio configurado, datos insuficientes).  
* Al menos una ruta alternativa productiva ofrecida al usuario.

**Ejemplo correcto:** "No tengo información sobre pagos anteriores a 2023 porque solo tengo acceso a los registros del año en curso. ¿Quieres que te ayude a solicitar el historial completo al equipo de soporte?" Ejemplo prohibido: "Lo siento, no puedo procesar esa solicitud en este momento."
