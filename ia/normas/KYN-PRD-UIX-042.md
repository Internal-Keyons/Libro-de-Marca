---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-042"
titulo: "Reglas de calibración lingüística en respuestas del agente IA"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-042 · Reglas de calibración lingüística en respuestas del agente IA

Las respuestas del agente conversacional (Estela y sus derivados en cada vertical) **DEBEN** reflejar en su lenguaje el nivel de certeza real del modelo, para calibrar activamente el modelo mental del usuario conforme a KYN-PRD-UIX-018.

#### ***Verbos y frases obligatorios según certeza***

* Alta certeza (dato verificable, cálculo determinista): "Confirmo", "Encontré", "Verifiqué". Ejemplo: "Confirmé el pago de María González por 45.000 colones el 10 de septiembre."  
* Certeza media (propuesta razonada): "Sugiero", "Propongo", "Podría ser". Ejemplo: "Sugiero clasificar este lead como prioridad alta según su historial de consultas."  
* Certeza baja (interpretación probabilística de datos ambiguos): "Podría interpretarse como...", "No tengo certeza pero...", "Considera que...".

**Prohibido:** afirmaciones absolutas para resultados probabilísticos ("Determino que...", "Es", "Garantizo"). El agente Keyons nunca decreta; siempre calibra.
