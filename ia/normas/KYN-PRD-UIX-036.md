---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-11"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-036"
titulo: "Restricciones del cliente sobre procesamiento con LLMs externos"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-036 · Restricciones del cliente sobre procesamiento con LLMs externos

Los clientes corporativos **PUEDEN** configurar restricciones a nivel de módulo dentro del vertical para impedir que datos altamente confidenciales pasen por modelos de lenguaje externos (Google Gemini, Anthropic Claude, OpenAI GPT). En módulos restringidos, el sistema usa exclusivamente procesamiento determinista o modelos ejecutados en infraestructura controlada por el cliente cuando aplique la modalidad de despliegue conforme a KYN-PRD-MED-023.

La restricción se declara en la configuración administrativa del tenant, con banner informativo visible al usuario final que indica: "Este módulo procesa datos localmente por política de tu empresa". Esta transparencia calibra el modelo mental del usuario sobre qué hace el sistema con datos sensibles.
