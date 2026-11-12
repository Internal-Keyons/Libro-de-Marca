---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-046"
titulo: "Modalidades de feedback multimodal según urgencia y contexto"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-046 · Modalidades de feedback multimodal según urgencia y contexto

El feedback del sistema al usuario se ajusta al nivel de urgencia del evento y al contexto operativo, aplicando escalada progresiva de modalidades sin sobrecargar sensorialmente al operador.

* **Feedback rutinario (urgencia baja):** solo texto o cambio visual sutil. Ejemplo: confirmación de guardado automático de un formulario.  
* **Feedback importante (urgencia media):** texto más icono con contraste moderado. Ejemplo: alerta de límite de plan cerca de agotarse.  
* **Feedback crítico (urgencia alta):** texto, icono, animación breve y opcionalmente sonido corto. Ejemplo: pago fallido en operación crítica de facturación.  
* **Feedback catastrófico (urgencia máxima):** modal bloqueante con las tres modalidades activas y opción única de acción. Ejemplo: pérdida total de conectividad durante la transacción.

El sonido se usa con moderación extrema y siempre configurable por el usuario. En contextos móviles el sonido puede reemplazarse por vibración. La escalada multimodal debe justificarse por la urgencia operativa real, nunca por preferencia estética del diseñador.
