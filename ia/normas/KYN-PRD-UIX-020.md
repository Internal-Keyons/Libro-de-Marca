---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-020"
titulo: "Estructura obligatoria del panel de explicación de decisión de IA"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-020 · Estructura obligatoria del panel de explicación de decisión de IA

Cuando la interfaz muestra explicación de una decisión (Nivel Bajo Demanda o Nivel Obligatorio conforme a KYN-PRD-UIX-019), el panel de explicación **DEBE** contener tres secciones en orden fijo, aplicando revelación progresiva.

* **Sección 1 — Explicación en lenguaje humano:** Resumen accesible del razonamiento en una o dos líneas. Ejemplo: "Clasifiqué este cliente como alto riesgo porque presenta 3 facturas vencidas en los últimos 60 días y superó el límite de crédito acordado en el contrato."  
* **Sección 2 — Fuentes o datos consultados:** Listado breve de qué información utilizó el modelo para llegar a la decisión, con enlaces al documento origen cuando aplique. Permite al usuario verificar rápidamente la validez del insumo del modelo.  
* **Sección 3 — Reglas de negocio aplicadas (bajo demanda dentro del panel):** Detalle técnico de las reglas configuradas por el cliente o por Keyons que llevaron a la clasificación. Este nivel de detalle se muestra solo si el usuario lo solicita explícitamente dentro del panel.
