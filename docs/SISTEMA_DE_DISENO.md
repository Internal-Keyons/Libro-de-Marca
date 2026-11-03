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
| Módulos | Portada (tarjetas en carrusel), `modulos.html` (página de área) y menú |
| Capítulos | Página de módulo `sistema-diseno/<módulo>.html` y lateral |
| Subcapítulos | Página de capítulo `sistema-diseno/<módulo>/<capítulo>.html`, con ancla `#s-01-02-03` |
| Normas | Se agregarán dentro de cada subcapítulo con la estructura de `plantilla.html` |

**Estados:** Estructura definida, Contenido pendiente, Borrador, En revisión, Vigente y Descontinuado. Hoy los 45 capítulos están en «Estructura definida» y los 135 subcapítulos en «Contenido pendiente». Nada está vigente.

## Cómo se mantiene

1. **Fuente única:** `data/sistema-diseno.json` (módulos, capítulos, subcapítulos, estados y normas de Marca relacionadas).
2. **Para regenerar,** después de cambiar el JSON, ejecutar:

   ```
   python tools/sistema_diseno.py
   ```

   El generador escribe `js/nav-sistema-diseno.js`, las 12 páginas de módulo y las 45 de capítulo.
3. **Archivos a mano:** la portada (`index.html`), `modulos.html` y `plantilla.html` se editan a mano.
4. **Código compartido:** `js/libro.js` lee `KEYONS_BOOK` (portada, menú, estados, leyenda y nombres de nivel). Sin esa declaración, el Libro de Marca no cambia.
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
