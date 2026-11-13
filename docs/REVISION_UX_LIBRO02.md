# Libro 02 · Sistema de Diseño · revisión de la estructura de UX

Documento interno · 2026-11-13. Solo es una recomendación: la estructura del Libro 02 no cambia hasta que Keylin lo decida.
Fuentes: `data/sistema-diseno.json` (12 módulos, 45 capítulos) y la tabla «Dónde va cada norma» de `normas-ux-sistema-diseno.md` (KYN-PRD-UIX, que conservan su ID).

## Tabla por capítulo

| Área › capítulo | Función | Temas de UX que cubre | Vacíos o duplicaciones | Ajuste recomendado |
| --- | --- | --- | --- | --- |
| Experiencia › 01 Principios comunes | Principios que rigen toda decisión de producto | Claridad, coherencia, control, diseño honesto, firma UX (UIX-001, 005, 006, 012, 013) | — | Ninguno |
| Experiencia › 02 Personas y contextos | Quién usa el producto, para qué y con cuánta carga | Perfiles, contextos, necesidades, carga cognitiva (UIX-007, 008, 009) | **Falta la investigación**: cómo se conoce a las personas antes de diseñar | Sumar «Investigación» como primer subcapítulo |
| Experiencia › 03 Elecciones verificadas | Hipótesis, criterios e indicadores de experiencia | Criterios UX e indicadores (UIX-003, 048) | Los indicadores se repiten con 44 Validación | 03 define qué se mide; 44 cómo se prueba. Escribirlo en ambas entradas |
| Arquitectura › 04 Información | Organización del contenido | Arquitectura de información (UIX-028) | — | Ninguno |
| Arquitectura › 05 Navegación | Cómo se recorre el producto | Navegación y orientación | — | Ninguno |
| Arquitectura › 06 Búsqueda | Encontrar y ubicarse | Búsqueda, filtros, ubicación y contexto | «Filtros» también está en 26 Tablas | 06 para filtros globales; 26 para filtros dentro de una tabla |
| Fundamentos › 07 a 11 | Base visual funcional (tokens, color, tipografía, espacio, recursos) | Legibilidad y jerarquía aplicadas | Riesgo de repetir el Libro de Marca (COL, TYP, ESP, ICO) | Cada capítulo cita la norma de Marca y documenta solo su traducción a interfaz |
| Componentes › 12 a 15 | Comportamiento de cada componente y sus estados | Interacciones y control, retroalimentación, espera (progreso) | Faltan los siete estados de componente (propuesta P5) | Ubicar los estados en 12 a 15 cuando se apruebe P5 |
| Patrones › 16 Formularios | Captura de datos | Validación, ayuda, pasos | — | Ninguno |
| Patrones › 17 Flujos de trabajo | Tareas completas | Recorridos y tareas (UIX-027, 031, 044) | **Onboarding y aprendizaje** viven escondidos aquí (UIX-044) | Sumar «Primeros pasos» como subcapítulo de 17, sin crear capítulo nuevo |
| Patrones › 18 Recuperación | Errores, vacíos y reintentos | Errores, espera, recuperación (UIX-021 a 026) | **Errores** también en 24 Mensajes y 33 Confianza | 18 decide el comportamiento; 24 la redacción; 33 los errores de la IA |
| Patrones › 19 Procesos críticos | Acciones sensibles | Confirmaciones, permisos, trazabilidad (UIX-014, 015) | — | Ninguno |
| Accesibilidad › 20 a 22 | Percepción, operación y adaptación | Accesibilidad, multidispositivo (UIX-038, 039) | — | Ninguno |
| Contenido › 23 Escritura | UX Writing | Etiquetas, instrucciones, brevedad (UIX-041) | — | Ninguno |
| Contenido › 24 Mensajes | Textos de sistema | Confirmaciones, errores, advertencias (UIX-040) | Ver 18 | Ver 18 |
| Contenido › 25 Localización | Idiomas y terminología | Idiomas, regiones, terminología | **«Voz y tono» repite el Libro 01** (VOZ-001 a 007) | Cambiar a «Voz en producto»: cita VOZ y solo agrega lo propio de la interfaz |
| Datos › 26 a 29 | Tablas, gráficos, cifras y dashboards | Lectura de datos (UIX-037) | **«Paletas categóricas» repite DAT-002** | 27 cita DAT-001 a 005 y documenta solo la interacción |
| IA y Estela › 30 a 33 | Interacción humano-IA | Transparencia, control, conversación, agentes, confianza (UIX-016 a 020, 032 a 036, 042, 043) | Identidad visual de Estela es del Libro 01 (cap. 05 y 30) | 31 «Identidad de Estela» se limita a su comportamiento en interfaz |
| Productos › 34 a 38 | Cómo cada familia de producto aplica el sistema | Base compartida, sitio web, herramientas, Product Default, white-label (UIX-045, 052) | **36 Herramientas › «Identidad visual»** y **35 Sitio web** pueden repetir el Libro 01 (ahora 18 Digital en Aplicaciones) | 35 y 36 documentan solo lo funcional y citan el Libro 01 para la identidad |
| Movimiento › 39 a 41 | Movimiento funcional y sensorial | Transiciones, retroalimentación, atajos | «Movimiento atmosférico» (40) puede repetir el capítulo 14 del Libro 01 | 40 cita el capítulo 14 y documenta solo su uso en interfaz |
| Gobierno › 42 a 45 | Calidad, implementación y documentación | **Pruebas de usabilidad**, regresiones y mejora continua (44) | Ver 03 | Ver 03 |

## Cobertura de los 13 temas pedidos

| Tema | Dónde vive | Estado |
| --- | --- | --- |
| Investigación y comprensión de usuarios | — | **Vacío**: sumar a 02 |
| Contextos, perfiles y necesidades | 02 | Cubierto |
| Arquitectura de información | 04 | Cubierto |
| Navegación y orientación | 05, 06 | Cubierto |
| Recorridos, tareas y flujos | 02, 17 | Cubierto |
| Interacciones y control del usuario | 01 (Control), 12 a 15, 30 | Cubierto |
| Carga cognitiva y atención | 02 | Cubierto |
| Errores, espera, éxito y recuperación | 15, 18, 24 | Cubierto; repartir funciones (ver 18) |
| Accesibilidad y multidispositivo | 20 a 22 | Cubierto |
| UX Writing y contenido funcional | 23, 24 | Cubierto |
| Onboarding y aprendizaje | 17 (UIX-044) | **Sin lugar visible**: sumar a 17 |
| Interacción humano-IA | 30 a 33 | Cubierto |
| Pruebas, métricas y mejora continua | 03, 44 | Cubierto; separar funciones |

## Libro 02 y Libro 05
- **Libro 02:** la experiencia dentro del producto, es decir, lo que la persona hace en la pantalla.
- **Libro 05 · Servicio al Cliente:** la experiencia de atención y acompañamiento (soporte, implementación y relación con el cliente).
- Los mensajes del producto (24) y la atención humana se citan entre sí, sin duplicarse.

## Estructura corregida (solo donde hay mejora real)
Ningún capítulo nuevo. Tres cambios dentro de capítulos existentes, con títulos breves:
1. **02 Personas y contextos:** suma «Investigación».
2. **17 Flujos de trabajo:** suma «Primeros pasos».
3. **25 Localización:** «Voz y tono» pasa a «Voz en producto».

Además, cuatro notas de alcance para escribir cuando se redacten:
- 03 y 44 (qué se mide y cómo se prueba);
- 18, 24 y 33 (errores);
- 27 (cita DAT);
- 35, 36 y 40 (citan el Libro 01).

Las KYN-PRD-UIX conservan su ID y su capítulo; ninguna cambia de lugar.
