---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-11"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-025"
titulo: "Reversibilidad como red de seguridad emocional operativa"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-025 · Reversibilidad como red de seguridad emocional operativa

Toda acción destructiva o significativa que el usuario pueda ejecutar por error **DEBE** ser reversible o requerir confirmación explícita antes de ejecutarse. La interfaz se diseña asumiendo que los usuarios cometerán errores; el objetivo no es evitar el error, sino permitir su corrección sin costo emocional ni operativo.

#### ***Ventana de reversibilidad según nivel HITL***

* **HITL Nivel 2 — Rollback de 30 segundos:** banner con botón "Deshacer" visible durante 30 segundos tras la ejecución.  
* **HITL Nivel 3 — Rollback durante sesión activa:** la acción es reversible hasta que el usuario cierre la sesión o la ventana operativa.  
* **HITL Nivel 4 — Rollback hasta cierre operativo del ciclo:** la acción queda registrada en log inmutable con opción explícita de reversión hasta que la acción cumpla su ciclo operativo.

La reversibilidad es aplicación operativa del principio de Aversión a la Pérdida: el impacto psicológico de una pérdida es aproximadamente el doble que el placer de una ganancia equivalente. Saber que existe red de seguridad reduce ansiedad operativa y permite al usuario delegar en agentes de IA con confianza.
