# Sistema de Diseño · estructura técnica

Documentación de desarrollo. No se publica con el sitio.

- **Rama:** `sistema-diseno`, abierta desde `main` en `4773622`.
- **Punto de recuperación:** `respaldo-2026-11-02e`.
- **Ruta:** `/sistema-diseno/` (portada en `sistema-diseno/index.html`).

## Arquitectura documental V1

**Libro → módulo → capítulo → subcapítulo → norma.**
- **Estructura:** 12 módulos, 45 capítulos y 135 subcapítulos, según la instrucción del 2026-11-02.
- **Numeración:** la documental (01.02.03) indica la ubicación y no es el código de una norma. Los códigos (`KYN-SDI-…`) son permanentes y van aparte.

| Nivel | Dónde se ve |
| --- | --- |
| Módulos | Cada módulo es un área, como en el Libro de Marca: tarjeta en la portada, entrada del menú y página de área `sistema-diseno/<módulo>.html` |
| Capítulos | Página de área del módulo, lateral y tarjeta |
| Subcapítulos | Página de capítulo `sistema-diseno/<módulo>/<capítulo>.html`, con ancla `#s-01-02-03`, y lateral |
| Normas | Se agregarán dentro de cada subcapítulo con la estructura de `plantilla.html` |

**Estados:** Estructura definida, Contenido pendiente, Borrador, En revisión, Vigente y Descontinuado. Hoy los 45 capítulos están en «Estructura definida» y los 135 subcapítulos en «Contenido pendiente». Nada está vigente.

## Nombres cortos y trama

- **Nombres cortos (propuesta, 2026-11-02):** el menú, las tarjetas y el lateral usan nombres de una línea, como el Libro de Marca. Están en `data/sistema-diseno.json`:
  - `st`, nombre corto de módulos, capítulos y subcapítulos;
  - `dc`, descripción corta de la tarjeta del módulo.

  Los títulos completos aprobados siguen en las páginas.
- **Trama:** el libro declara `KEYONS_BOOK.id = 'sistema-diseno'` y `libro.js` lo escribe en `<html data-libro>`. La trama es la retícula horizontal y vertical, en el encabezado de portada, los portales de capítulo y las franjas de área.

## Cómo se mantiene

1. **Fuente única:** `data/sistema-diseno.json` (módulos, capítulos, subcapítulos, estados y normas de Marca relacionadas).
2. **Para regenerar,** después de cambiar el JSON, ejecutar:

   ```
   python tools/sistema_diseno.py
   ```

   El generador escribe `js/nav-sistema-diseno.js`, las 12 páginas de área de módulo y las 45 de capítulo.
3. **Archivos a mano:** la portada (`index.html`) y `plantilla.html` se editan a mano.
4. **Código compartido:** `js/libro.js` lee `KEYONS_BOOK` (id, portada, enlaces del menú, estados, leyenda, nombres de nivel, `cardShort` y `areaFull`). Sin esa declaración, el Libro de Marca no cambia.
5. **Estilos:** `css/sistema-diseno.css` guarda solo lo que Marca no tiene (estados nuevos, listas de capítulos y subcapítulos, ejemplo interactivo).
6. **Referencias a Marca:** un ID `KYN-MRK-…` se enlaza a su norma del Libro de Marca. No se duplica el texto.

## Pendientes de decisión

1. **Prefijo de normas:** `KYN-SDI` y los códigos de módulo (PEX, ARQ, FUI, CPE, PAT, ACC, CNT, DAV, IAE, SPR, MOV, GOB) son provisionales.
2. **Identidades de los cuatro contextos:** los valores del ejemplo interactivo son de muestra.
3. **Registro y exportación propios:** aún no existen para este libro.
4. **Interfaces del Libro de Marca:**
   - el área ya había salido del índice por la instrucción del 2026-11-02;
   - `interfaces/*.html` siguen como páginas de redirección;
   - en esta ejecución no se trasladó contenido.
5. **Integración a `main`:** se hace solo con aprobación. Todo lo que entra a `main` se publica.
