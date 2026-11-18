# Bloques 0 y 1 · 17 de noviembre de 2026 · borrador

## Bloque 0 · Libro de Marca

| Cambio | Tipo | Dónde | Regla |
| --- | --- | --- | --- |
| Marcador de cada ítem: ícono, número, viñeta o sin marcador, según el significado | General | `reglas-visuales.md` 3.5 | R26 (nueva). R02 la cita |
| 16.1 Principios y 17.1 Principios: viñetas | Aplicación de R26 | Corporativo y Expresivo | R26 |
| 17.5 Recursos: íconos del catálogo (cámara, formas, capas, flecha en giro, perfil) | Aplicación de R26 | Expresivo | R26 |
| 16.4: salen la barra y los nombres; quedan las tres columnas con su título | Local | Corporativo | — |
| Equilibrios de Estela: textos nuevos; sale el cierre DEBE «Estos principios deben mantenerse…» | Texto de Keylin | Estela 5.2 | — |
| Respuesta de Estela en gris del texto y cursiva | Local | Estela 5.3 | Excepción E2 |
| Acordeón único con el diseño de ADN-006 | General | Estela 5.3, Sistema de Diseño, ADN, Paleta base, Elementos gráficos | R27 (nueva) |

### Acordeón único

- `details` y `summary` son el único control. El + es un `span` decorativo con `aria-hidden`. Ningún `summary` del sitio tiene un botón adentro (revisado en todas las páginas).
- `js/libro.js` ya no abre el primer ítem al aparecer en pantalla.
- Se quitó el `open` fijo de ADN-006, Paleta base y Elementos gráficos.
- Los ítems no se excluyen entre sí: se quitó el atributo `name` de los escenarios.

| Prueba con interacción real (Estela 5.3) | Resultado |
| --- | --- |
| Al llegar a la sección, ¿se abre algo solo? | No: 0 de 8 abiertos |
| Enter sobre el primer título | Se abre |
| Tab al segundo y Espacio | Se abre; el primero sigue abierto |
| Foco visible | Anillo de 2 px |
| El + pasa a − al abrir | Sí |
| Anuncio «expandido» y «contraído» con lector de pantalla | **Pendiente:** no hay lector de pantalla en este equipo. `details` y `summary` lo exponen de forma nativa, pero falta comprobarlo con NVDA o VoiceOver |

### Inventario de R26 (propuestas, sin aplicar)

| Dónde | Hoy | Según R26 | Propuesta |
| --- | --- | --- | --- |
| Estela 5.2, rasgos | Íconos | Conceptos de personalidad, no gráficos | Keylin pidió conservar los íconos (2026-11-17). Sin cambio |
| Estela 5.2, equilibrios | Íconos | Igual que los rasgos | Sin cambio, por la misma indicación |
| ADN-007, Siete principios | Números | Enumeración que el título anuncia | Correcto |
| CMP-004, Ritmo y equilibrio | Números | Enumeración de criterios | Correcto |
| COR-004, cuatro preguntas | Números | El título anuncia cuántas son | Correcto |

## Bloque 1 · Capítulo 05 Navegación (revisión)

Normas: ARQ-005 a ARQ-010 con los mismos códigos, y **ARQ-017 Acceso directo y rutas no disponibles** (nueva). Antes de emitirla se comprobó que no figuraba en el registro, la matriz ni la auditoría.

### Correcciones de Keylin

| Pedido | Qué se hizo |
| --- | --- |
| Nombres coherentes, no idénticos | ARQ-006: «coherente en significado; puede abreviarse o precisarse». El ejemplo y la verificación cambian |
| Foco según el tipo de cambio | ARQ-005, «Foco según el tipo de cambio»: página nueva (el foco queda donde lo deja el navegador; «Ir al contenido» es lo primero que alcanza el teclado, sin forzar el foco), vista sin recargar, filtro o pestaña de panel, y panel |
| Patrones accesibles distintos | ARQ-008: tabla de cuatro patrones (página actual, pestaña seleccionada, grupo expandible, panel modal) y teclado por tipo de menú |
| Contexto conservado sin imponer la URL | ARQ-010: depende de la tarea, la privacidad y la seguridad. La URL es una opción, no un requisito |
| Orden adaptable entre dispositivos | ARQ-009: el orden puede cambiar si mejora el uso y los destinos se reconocen |
| Revisión automática más pruebas manuales | ARQ-008: la revisión automática es necesaria, pero no alcanza; se suman teclado, NVDA y VoiceOver |
| Tamaño de los objetivos | ARQ-009 distingue WCAG AA 2.5.8 (24 × 24 px CSS, con excepciones), AAA 2.5.5 (44 × 44 px) y la preferencia Keyons propuesta (44 × 44 px, requiere aprobación). La auditoría UIX se corrigió |

### Vacíos completados

| Tema | Dónde |
| --- | --- |
| Estados de navegación (texto de Keylin) | ARQ-008: tres requisitos y las filas «Estados visuales» y «Sección activa» |
| Acceso directo y rutas no disponibles | ARQ-017, con la tabla de cuatro situaciones: autorizada, inexistente, sin autorización y sesión vencida |
| Cambios pendientes al navegar | ARQ-010: fila que cita 16 Formularios y 17 Flujos |
| Panel móvil | ARQ-009, acordeón «Panel de navegación móvil»: estados, `inert`, cierre, retorno del foco, cambio de tamaño y movimiento reducido |

### Edición

- Las entradas quedaron en una frase y no repiten el requisito.
- La lectura principal muestra el requisito y dos o tres decisiones; lo técnico, los casos límite y la verificación van en el acordeón.
- Los requisitos tienen la medida de lectura del libro (600 px), en todo el Sistema de Diseño.

### Cobertura del capítulo 05

| Responsabilidad | Estado |
| --- | --- |
| Ubicación, sección activa y grupo superior | Desarrollada |
| Nombres, destinos y comportamiento coherentes | Desarrollada |
| Funciones visibles para puntero, teclado y tacto | Desarrollada |
| Estados, semántica y foco de los controles | Desarrollada |
| Adaptación entre dispositivos y panel móvil | Desarrollada |
| Regreso con contexto | Desarrollada |
| Acceso directo y rutas no disponibles | Desarrollada |
| Patrón predeterminado de navegación SaaS | Pendiente (37 Product Default) |
| Apariencia de los indicadores | Pendiente (08 Color funcional y 14 Estructura) |
| Tamaño táctil propio de Keyons (44 px) | Requiere aprobación (22 Adaptación) |
| Prueba con lector de pantalla real | Pendiente |

**Estado del capítulo:** borrador con contenido, no capítulo terminado: tiene responsabilidades esenciales pendientes en otros capítulos.

### Pruebas

| Prueba | Resultado |
| --- | --- |
| `verificar.py` | 0 errores |
| Detector de líneas dobles (05, Corporativo, Expresivo, Estela, ADN, Paleta base, Elementos gráficos) | 0 en todas |
| Enlaces del 05 | Todos llevan a páginas existentes |
| Buscador | Encuentra ARQ-005 a 010 y ARQ-017; los reservados no aparecen |
| Capturas | `propuestas/capturas-2026-11-17c/` (Bloque 0) |

### Archivos

- `tools/sd/base.py` y `tools/sd/m02_arquitectura.py` (nuevos);
- `tools/sd_capitulos.py`, `tools/expresion.py` y `tools/estela.py`;
- `css/libro.css`, `css/marca.css` y `css/sistema-diseno.css`;
- `js/libro.js`;
- `reglas-visuales.md`;
- las páginas regeneradas y `data/sd-normas.json`.

### Requiere aprobación

1. Los textos que redactó Claude en el 05.
2. El código ARQ-017.
3. La preferencia de 44 px.
4. Quitar el cierre DEBE de los equilibrios (pedido por Keylin, se deja anotado).
