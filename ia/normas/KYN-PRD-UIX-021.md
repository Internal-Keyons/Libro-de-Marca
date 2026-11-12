---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-021"
titulo: "Protocolo de espera y percepción de responsividad"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-021 · Protocolo de espera y percepción de responsividad

La percepción de responsividad de un sistema se decide en los primeros 400 milisegundos (umbral de Doherty). Superado ese umbral, el usuario transita de confianza tácita a duda activa; si nada visible confirma que el sistema procesa, la duda escala a asunción de fallo. Keyons rige su comportamiento en espera por este principio operativo: el sistema DEBE comunicar procesamiento antes de que la duda del usuario aparezca, no después.

#### ***Umbrales de comunicación obligatoria***

| Umbral | Respuesta obligatoria de la interfaz |
| :---- | :---- |
| 0 a 0.4 seg | Nada visible. Percibido como instantáneo. |
| 0.4 a 1 seg | Microanimación sutil de feedback (cambio de color, movimiento mínimo). Confirma que la acción se registró. |
| 1 a 3 seg | Loader claro y visible en el componente donde ocurre la acción, sin cubrir el resto de la interfaz. |
| 3 a 10 seg | Loader + mensaje humano descriptivo del estado ("Consultando 3 fuentes...", no "Loading..."). |
| Más de 10 seg | Loader + mensaje humano + estimación de tiempo restante + opción de cancelar o realizar otra tarea en paralelo. |

Superar 30 segundos sin resolución activa protocolo de fallo del modelo conforme a KYN-PRD-UIX-023. Sistemas que dejan al usuario en pantalla estática superior a 3 segundos sin retroalimentación pierden porcentaje material de tasa de finalización en flujos operativos, y Keyons no admite ese costo por default en ningún producto. Criterio de aceptación pre-lanzamiento: un evaluador externo debe poder identificar en cada punto de espera del flujo qué está haciendo el sistema y cuánto falta.
