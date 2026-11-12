---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-014"
titulo: "Matriz de decisión Human-in-the-Loop por riesgo e irreversibilidad"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-014 · Matriz de decisión Human-in-the-Loop por riesgo e irreversibilidad

Toda acción ejecutable por un agente automatizado o por decisión asistida por IA **DEBE** clasificarse en uno de cuatro niveles de Human-in-the-Loop según la combinación de riesgo operativo y grado de irreversibilidad de la acción. La clasificación se declara por vertical en la Ficha Estándar de Producto conforme a KYN-PRD-FIC-002.

| Nivel | Descripción operativa | Ejemplos aplicados |
| :---- | :---- | :---- |
| Nivel 1 - Autonomía asistida | Riesgo bajo y acción completamente reversible. El sistema ejecuta; el usuario ve el resultado y puede editar libremente después sin fricción. | Sugerir texto en un campo, marcar lead como "en revisión", ordenar lista por fecha, sugerir prioridad tentativa. |
| Nivel 2 - Revisión posterior con rollback fácil | Riesgo bajo-medio, reversible en ventana corta. El sistema ejecuta y muestra la acción realizada en banner con botón de reversión visible durante 30 segundos. | Clasificar ticket automáticamente, autoetiquetar mensaje, sugerir asignación de responsable, categorizar transacción. |
| Nivel 3 - Aprobación previa obligatoria | Riesgo medio, reversible con esfuerzo. El sistema prepara la acción y muestra opciones "Aprobar / Editar / Descartar". El usuario DEBE confirmar antes de ejecutar. | Enviar correo automatizado al cliente, cambiar estado comercial de cliente, generar propuesta económica, notificar a tercero. |
| Nivel 4 - Aprobación reforzada con confirmación explícita | Riesgo alto o irreversible. Requiere confirmación explícita adicional del usuario. Registro obligatorio en log inmutable. Materializa la Zona Amarilla de KYN-PRD-PRI-013. | Aprobar crédito, procesar pago, eliminar datos de cliente, firmar contrato electrónicamente, ejecutar acción con efecto contable o legal. |

Las Zonas Rojas de KYN-PRD-PRI-013 NO se ejecutan nunca, ni siquiera con HITL Nivel 4. La elección de nivel para cada acción específica de un vertical se justifica formalmente en el expediente del proyecto según el arquetipo operativo del usuario destino declarado en KYN-PRD-UIX-007.
