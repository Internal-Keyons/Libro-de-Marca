# Arquitectura de la Biblioteca · infraestructura compartida, estilos independientes

2026-11-12 · Documento interno.

## Qué se comparte

| Capa | Archivo | Qué contiene | Quién lo usa |
|---|---|---|---|
| Registro | `data/libros.json` → `tools/biblioteca.py` | Los seis libros: nombre, trama, ruta, acceso, estado, prefijo y presentación | Selector, portada, Guía, buscador |
| Comportamiento | `js/libro.js` | Selector de libros, cabecera, menú lateral, índices, buscador, referencias KYN, estados, carruseles | Todos los libros |
| Índice de cada libro | `js/nav-data.js` (Marca), `js/nav-sistema-diseno.js` (generado) | Áreas, capítulos y secciones | `js/libro.js` |
| Buscador | `js/busqueda-indice.js` (generado) | Libros con acceso abierto | `js/libro.js` |
| Normas | `data/normas.json`, `js/secciones.js`, `data/sistema-diseno.json` | IDs y rutas | Referencias y buscador |
| Valores | `css/tokens.css` | Color, escala, espacio, radios, movimiento | Todas las hojas |
| Componentes base | `css/libro.css` | Componentes comunes en presentación documental | Todos los libros |

## Qué es propio de cada libro

| Libro | Hoja propia | Regla |
|---|---|---|
| 01 Marca y Experiencia | `css/marca.css` | Solo la cargan las páginas del Libro de Marca. |
| 02 Sistema de Diseño | `css/sistema-diseno.css` | Solo la cargan sus páginas; cada selector va con prefijo `sd-`/`sdl-`/`sdx-` o `html[data-libro="sistema-diseno"]`. |

Reglas de trabajo:
- Un cambio visual que vale solo para un libro va en la hoja de ese libro, nunca en `libro.css`.
- `libro.css` no tiene reglas `[data-libro="…"]` de un libro concreto.
- Un cambio en `libro.css` alcanza a todos los libros: se trata como cambio general y se revisa en los dos.
- Las normas de identidad viven en el Libro de Marca (`KYN-MRK`). El Sistema de Diseño las cita con su ID y desarrolla su aplicación en interfaces; no las copia.
- Ningún libro copia páginas, menús ni hojas de otro: comparten componentes por `js/libro.js` y `css/libro.css`.

## Presentaciones

Cada libro declara `presentacion` en `data/libros.json`; la página la recibe en `html[data-presentacion]`.

- **Documental:** el diseño actual (`css/libro.css`). Hoy la usan los dos libros abiertos.
- **Editorial:** futura y sin desarrollar. Cuando se construya, vivirá en `css/presentacion-editorial.css`, con cada selector acotado a `html[data-presentacion="editorial"]`, y solo la cargarán los libros que la declaren. La presentación documental no cambia.

## Comprobaciones

`python tools/verificar.py` falla si:
- una página del Libro de Marca carga la hoja del Sistema de Diseño, o al revés;
- una página del Sistema de Diseño no carga su hoja;
- `libro.css` tiene reglas de un libro concreto;
- un selector de `sistema-diseno.css` no está acotado.

Prueba de aislamiento hecha el 2026-11-12: en `fundamentos/tipografia/sistema.html` (Libro 01) se cargó además `css/sistema-diseno.css` y se compararon los estilos calculados de 465 elementos: 0 diferencias.
