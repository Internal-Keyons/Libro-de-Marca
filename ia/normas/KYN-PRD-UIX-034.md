---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-11"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-034"
titulo: "Memoria conversacional en tres niveles con controles diferenciados"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-034 · Memoria conversacional en tres niveles con controles diferenciados

Todo agente conversacional Keyons implementa exactamente tres niveles de memoria conversacional, cada uno con controles diferenciados para el usuario. Esta estructura protege al usuario contra acumulación silenciosa de datos personales y preserva transparencia sobre qué recuerda el sistema.

* **Nivel A — Memoria de sesión (default activada):** el asistente recuerda todo lo hablado dentro de la sesión activa. Al cerrar sesión o iniciar nueva conversación, la memoria de sesión se limpia automáticamente. Es el default más seguro y predecible.  
* **Nivel B — Memoria persistente por usuario (opt-in explícito):** el asistente recuerda preferencias del usuario entre sesiones ("prefiero respuestas en formato lista"). Requiere activación explícita por el usuario. La memoria es siempre visible al usuario y editable o eliminable en cualquier momento.  
* **Nivel C — Contexto de tenant (compartido dentro de la empresa cliente):** información configurada por el administrador del tenant como contexto siempre presente para el asistente ("somos clínica dermatológica, no ofrezcas servicios estéticos generales"). Vive en la configuración del tenant.
