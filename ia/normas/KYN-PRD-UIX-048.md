---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-048"
titulo: "Métricas UX obligatorias de éxito por producto"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-048 · Métricas UX obligatorias de éxito por producto

Todo vertical Keyons **DEBE** monitorear continuamente las siguientes métricas UX de éxito durante la Fase Galaxia. Los resultados alimentan las decisiones de mejora del producto y el aprendizaje sistemático entre proyectos.

* **Tasa de completitud de flujos críticos:** Porcentaje de usuarios que inician y completan cada flujo operativo principal del producto (alta de cliente, procesamiento de pago, exportación de reporte). Umbral mínimo aceptable: 85%.  
* **Tiempo a primera acción exitosa (Time to First Value):** Tiempo transcurrido desde el primer login hasta que el usuario completa su primera acción operativa exitosa. Umbral orientador: menos de 10 minutos para verticales estándar.  
* **Tasa de abandono en flujos multi-paso:** Porcentaje de usuarios que abandonan cada paso intermedio de un flujo multi-paso. Los pasos con abandono superior a 25% se rediseñan.  
* **Frecuencia de uso de rollback:** Cantidad de veces que los usuarios usan mecanismos de reversión. Frecuencia alta puede indicar problema de diseño en la acción original que motiva la reversión.  
* **Satisfacción cualitativa:** Encuesta breve tras primeras 4 semanas de uso con NPS interno del producto y campo abierto de comentarios. Frecuencia trimestral en fase Galaxia.

Las métricas se registran en el sistema de observabilidad UX de Keyons (Polaris) y se revisan formalmente en cada ciclo de revisión conforme a KYN-PRD-GOB-016. Umbrales específicos por vertical se declaran en la Ficha Estándar de Producto.
