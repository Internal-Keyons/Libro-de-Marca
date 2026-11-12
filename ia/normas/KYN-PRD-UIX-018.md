---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-018"
titulo: "Gestión de expectativas del usuario ante IA probabilística"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-018 · Gestión de expectativas del usuario ante IA probabilística

Los usuarios tienden a formar modelos mentales del software basados en experiencias previas con herramientas deterministas (una calculadora entrega el mismo resultado ante la misma entrada). Los modelos de lenguaje son probabilísticos: pueden variar entre ejecuciones. Si el modelo mental del usuario no se calibra activamente, la primera vez que el sistema responda distinto a lo esperado se genera frustración y pérdida de confianza.

#### ***Reglas de calibración del modelo mental***

* **Léxico obligatorio del agente:** El agente Keyons "sugiere", "propone", "estima". Nunca "determina", "resuelve", "garantiza", ni afirma con certeza absoluta un resultado probabilístico. La calibración lingüística del agente se detalla en KYN-PRD-UIX-042.  
* **Aviso explícito de variabilidad cuando aplique:** En respuestas donde la variabilidad entre ejecuciones puede ser material para el usuario, el sistema comunica explícitamente esa posibilidad con microcopy contextual.  
* **Distinción entre respuesta y decisión:** La interfaz distingue visualmente entre información recuperada por el sistema y propuestas generadas por el modelo IA. Ambas se muestran con tratamiento visual diferenciado para calibrar la expectativa correcta.
