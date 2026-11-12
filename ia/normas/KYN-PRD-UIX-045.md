---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-045"
titulo: "Frontera obligatoria entre elementos personalizables y elementos fijos"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-045 · Frontera obligatoria entre elementos personalizables y elementos fijos

En cada producto Keyons, la interfaz contiene dos tipos de elementos claramente diferenciados por naturaleza. Esta frontera **DEBE** declararse formalmente antes del lanzamiento del producto.

#### ***Elementos personalizables por el cliente (administrador del tenant)***

Elementos que el administrador del tenant **PUEDE** modificar desde el panel de configuración del vertical, para adaptar la interfaz a su operación. Ejemplos típicos: items visibles del menú lateral, orden de columnas de tablas, campos visibles en formularios, dashboards activos y su orden, activación o desactivación de módulos opcionales.

#### ***Elementos fijos estandarizados por Keyons (no personalizables)***

Elementos que no pueden modificarse desde la configuración del tenant, porque su personalización comprometería la solidez, seguridad o coherencia del producto. Ejemplos típicos: comportamiento del agente Estela, lógica de HITL por nivel, sistema de comunicación de confianza del modelo, estructura de mensajes de error, presencia obligatoria de rollback, elementos de la firma UX Keyons declarados en KYN-PRD-UIX-012.

Cada vertical Keyons declara en su Ficha Estándar de Producto la lista de elementos personalizables y la lista de elementos fijos. Sin esta declaración, el vertical no puede lanzarse comercialmente. La modificación de un elemento fijo por solicitud puntual de un cliente NO se ejecuta por soporte de Keyons sin RFC formal aprobado por los Aprobadores Generales conforme a KYN-PRD-GOB-015.
