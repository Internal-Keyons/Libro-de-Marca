# Sistema de Diseño · estructura técnica

Documentación de desarrollo. No se publica con el sitio.

- **Rama:** `sistema-diseno`, abierta desde `main` en `4773622`.
- **Punto de recuperación:** `respaldo-2026-11-02e`.
- **Ruta:** `/sistema-diseno/` (portada en `sistema-diseno/index.html`).

## Cómo funciona

El Sistema de Diseño usa el mismo código que el Libro de Marca (`js/libro.js`) con su propio índice.

| Archivo | Función |
| --- | --- |
| `js/nav-sistema-diseno.js` | Índice del libro: un área, doce módulos. Reemplaza a `js/nav-data.js` en sus páginas. Declara `KEYONS_BOOK`: portada, menú por módulos y enlaces secundarios |
| `js/libro.js` | Lee `KEYONS_BOOK`. Sin esa declaración, el Libro de Marca funciona igual que antes |
| `js/sistema-diseno.js` | Índice de la portada, códigos de módulo y ejemplo interactivo |
| `css/sistema-diseno.css` | Solo lo que Marca no tiene (índice de doce módulos y ejemplo interactivo), con prefijo `sd-` |
| `sistema-diseno/*.html` | Portada, página de área (`modulos.html`), doce módulos y plantilla de norma |

- **Diseño:** es el mismo del Libro de Marca.
  - Portada con cielo y vidrio; portal de capítulo en cada módulo; página de área generada.
  - Rejillas `.cols`, secciones `.ed` y lista de normas `.kidx`.
  - Los nombres de los módulos se ven completos en el lateral.

- **Referencias a Marca:** un ID `KYN-MRK-…` escrito en el texto se enlaza a su norma del Libro de Marca. En este libro no se enlazan los números de capítulo.
- **Fuera del registro de Marca:** `tools/normas.py`, `tools/verificar.py` y `tools/exportar.py` siguen trabajando solo con el Libro de Marca.

## Cómo se agrega una norma

1. En la página del módulo, una sección `<section class="ed" id="clave">` con la estructura de `sistema-diseno/plantilla.html`.
2. En `js/nav-sistema-diseno.js`, un ítem dentro del módulo con `href: 'sistema-diseno/modulo.html#clave'` y su estado.
3. Una fila en el índice de normas del módulo (`.sd-norms`), con su código, título y estado.

## Pendientes de decisión

1. **Prefijo de normas:** `KYN-SDI` y los códigos de módulo (PEX, ARQ, FUI, CPE, PAT, ACC, CNT, DAV, IAE, SPR, MOV, GOB) son provisionales.
2. **Identidades de los cuatro contextos:** los valores del ejemplo interactivo son de muestra.
3. **Registro y exportación propios:** aún no existen para este libro.
4. **Interfaces del Libro de Marca:**
   - el área ya había salido del índice por la instrucción del 2026-11-02;
   - `interfaces/*.html` siguen como páginas de redirección;
   - en esta ejecución no se trasladó contenido.
5. **Integración a `main`:** se hace solo con aprobación. Todo lo que entra a `main` se publica.
