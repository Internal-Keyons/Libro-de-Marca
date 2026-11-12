---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-11"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-023"
titulo: "Protocolo de fallo del sistema con ruta alternativa obligatoria"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-023 · Protocolo de fallo del sistema con ruta alternativa obligatoria

Cuando un componente automatizado por IA o una integración externa falla, la interfaz **DEBE** ofrecer al menos una ruta alternativa manual visible en el mismo componente donde ocurrió el fallo. Esta regla es dura y no admite excepciones por complejidad técnica.

#### ***Ejemplos de aplicación obligatoria***

* Si la verificación automática de pago con SINPE falla, el usuario **DEBE** poder adjuntar comprobante manualmente en el mismo momento y en el mismo componente, sin abandonar la pantalla.  
* Si el agente de IA no puede clasificar un lead, el usuario **DEBE** poder clasificarlo manualmente con opciones predefinidas visibles en el mismo componente.  
* Si la extracción automática de datos de un documento falla, el usuario **DEBE** poder ingresar los datos manualmente en el mismo flujo, sin reiniciar la operación.

Cuando técnicamente sea imposible ofrecer ruta alternativa manual en el momento, el mensaje **DEBE** indicar tiempo estimado de restablecimiento del servicio ("vuelve a intentar en 5 minutos") y no dejar al usuario en callejón sin salida.
