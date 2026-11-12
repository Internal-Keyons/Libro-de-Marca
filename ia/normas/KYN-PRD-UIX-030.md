---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-030"
titulo: "Jerarquía de urgencia de notificaciones y prohibición de fatiga por alertas"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-030 · Jerarquía de urgencia de notificaciones y prohibición de fatiga por alertas

Todo evento del sistema que requiera atención del usuario se clasifica en uno de cuatro niveles de urgencia según su impacto operativo real. Cada nivel tiene modalidad de notificación asignada. Prohibido escalar niveles arbitrariamente para "asegurar que el usuario vea" un evento; la escalada arbitraria genera fatiga por alertas y termina provocando que el usuario ignore incluso las alertas críticas legítimas.

| Nivel | Modalidad de notificación | Ejemplos |
| :---- | :---- | :---- |
| Rutinario | Solo cambio visual sutil o texto discreto. Sin interrupción del flujo. | Confirmación de guardado automático, actualización menor de datos, indicador de sincronización. |
| Importante | Texto más icono con contraste moderado. Puede requerir acción pero no bloquea flujo. | Alerta de límite de plan cerca de agotarse, recordatorio de tarea pendiente, invitación a completar perfil. |
| Crítico | Texto, icono, animación breve y opcionalmente sonido corto. Requiere atención inmediata pero no bloquea el sistema. | Pago fallido en operación crítica, límite de plan alcanzado, error en integración operativa activa. |
| Catastrófico | Modal bloqueante con todas las modalidades activas y opción única de acción. Bloquea toda otra interacción hasta resolverse. | Pérdida total de conectividad durante transacción irreversible, brecha de seguridad detectada, fallo crítico de infraestructura. |

#### ***Reglas de agrupación inteligente***

* Alertas del mismo tipo generadas en secuencia rápida se agrupan automáticamente en una única notificación consolidada.  
* El sonido se usa con moderación extrema, siempre configurable por el usuario (activar/desactivar).  
* Ningún vertical puede tener más de 5 notificaciones rutinarias visibles simultáneamente en la interfaz principal. Excedentes se consolidan en centro de notificaciones.
