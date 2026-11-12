---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-019"
titulo: "Explicabilidad activada por materialidad del impacto"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-019 · Explicabilidad activada por materialidad del impacto

La explicación de por qué el sistema tomó una decisión (Explainable AI) NO se muestra por default en toda decisión automatizada, porque sobrecarga innecesariamente al usuario. La explicabilidad se rige por tres niveles graduales según la materialidad del impacto de la decisión sobre el usuario o sobre terceros.

* **Nivel Nulo (sin explicación visible):** Aplica a decisiones automáticas de bajo impacto (sugerir texto, ordenar lista, autocompletar campo, resaltar coincidencia). No se muestra explicación ni botón para pedirla.  
* **Nivel Bajo Demanda (explicación disponible si el usuario pregunta):** Aplica a decisiones medias donde el usuario podría razonablemente querer entender el razonamiento. Botón discreto "¿Por qué?" que abre panel con explicación al pedirlo.  
* **Nivel Obligatorio (explicación siempre visible junto a la decisión):** Aplica a decisiones que afectan materialmente al usuario o a terceros (denegar solicitud, clasificar como riesgo, aprobar crédito, alterar estado comercial, priorizar caso crítico) y siempre a acciones bajo Zona Amarilla de KYN-PRD-PRI-013 con HITL Nivel 3 o 4. La explicación es parte visible del componente, no bajo demanda.

Cada vertical Keyons declara en su Ficha Estándar de Producto qué tipos de decisión aplican a cada nivel de explicabilidad.
