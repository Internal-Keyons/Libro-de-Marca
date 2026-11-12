---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-11"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-016"
titulo: "Comunicación tripartita de confianza del modelo"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-016 · Comunicación tripartita de confianza del modelo

La confianza del modelo IA sobre una respuesta o decisión se comunica al usuario mediante tres niveles categóricos con etiqueta orientada a la acción, color contextual e icono reconocible. Los puntajes numéricos crudos (por ejemplo "Confianza: 58%") NO se muestran por default al usuario final ni al operador, porque generan confusión analítica y parálisis de decisión. Pueden mostrarse bajo demanda en paneles de auditoría avanzada, pero nunca en la interfaz principal operativa.

| Nivel | Etiqueta | Comportamiento del sistema |
| :---- | :---- | :---- |
| Verificado (verde) | Verificado | Confianza alta. El sistema ejecuta la acción sugerida en segundo plano sin interrumpir al usuario. Confirmación visible como aviso no invasivo tras completarse. |
| Revisar (amarillo) | Revisar antes de aprobar | Confianza media. La interfaz resalta visualmente la propuesta y espera aprobación explícita del usuario antes de ejecutar. Materializa la Zona Amarilla de KYN-PRD-PRI-013. |
| Validación humana (rojo) | Requiere validación humana | Confianza baja o acción bajo zona amarilla de PRI-013. El sistema NO actúa. Escala al humano con contexto completo, opciones disponibles y datos que llevaron al escalamiento. |

La reducción a tres niveles categóricos no es simplificación estética: es aplicación operativa de la Ley de Hick, que establece que el tiempo de decisión crece logarítmicamente con el número de opciones disponibles. Tres niveles ofrecen resolución operativa suficiente sin activar parálisis analítica.
