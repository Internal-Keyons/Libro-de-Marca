---
manual: "Sistema de Diseño Keyons"
version: "0.1"
fecha: "2026-11-11"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-PRD-UIX-038"
titulo: "Cumplimiento mínimo WCAG 2.2 nivel AA"
estado: "borrador"
fuente: "/normas-ux-sistema-diseno.md"
---

# KYN-PRD-UIX-038 · Cumplimiento mínimo WCAG 2.2 nivel AA

Todo producto Keyons **DEBE** cumplir con las Web Content Accessibility Guidelines versión 2.2 en nivel AA como mínimo, respetando los cuatro principios rectores del estándar: perceptible, operable, comprensible y robusto.

#### ***Requisitos técnicos operativos derivados***

* Contraste de color mínimo: relación 4.5:1 para texto normal y 3:1 para texto grande.  
* Tamaño de fuente mínimo operativo: equivalente a 16 píxeles para texto de cuerpo en interfaces web y proporcional en aplicaciones móviles.  
* Navegación completa por teclado: toda funcionalidad accesible sin uso de ratón, con indicador visual claro del elemento con foco activo.  
* Compatibilidad con lectores de pantalla: etiquetas ARIA correctas en todos los componentes interactivos y descripciones alt en imágenes con contenido significativo.  
* Indicadores no dependientes exclusivamente del color: los estados y alertas se comunican con color más icono o texto, para no excluir a usuarios daltónicos (aproximadamente 8% de hombres y 0.5% de mujeres a nivel mundial).  
* Área mínima de cada control: 24 × 24 píxeles (WCAG 2.5.8).  
* El elemento con foco nunca queda tapado por otros elementos, como cabeceras fijas o avisos (WCAG 2.4.11).  
* Autenticación sin pruebas cognitivas: el usuario no debe resolver acertijos ni recordar códigos para iniciar sesión; se permite copiar y pegar y usar gestores de contraseñas (WCAG 3.3.8).

Cada vertical Keyons declara en su Ficha Estándar de Producto el nivel WCAG cumplido y las excepciones justificadas cuando aplique. El cumplimiento se verifica en el checklist de auditoría UX pre-lanzamiento conforme a KYN-PRD-UIX-050.
