# Buscador de la Biblioteca y permisos de lectura

Intervención P4 · 2026-11-12. Documento interno.

## Cómo funciona

- `tools/biblioteca.py` genera `js/busqueda-indice.js` desde `data/libros.json`, los índices de cada libro (`js/nav-data.js`, `js/nav-sistema-diseno.js`) y los registros de normas (`js/secciones.js` y `data/sistema-diseno.json`).
- El índice reúne **solo los libros con `acceso: "abierto"`**. Los libros en preparación no aportan títulos, fragmentos ni metadatos.
- Solo entran enlaces a anclas que existen. Un subcapítulo sin sección escrita aparece en los resultados sin enlace, con su estado.
- `js/libro.js` carga el índice la primera vez que se abre el buscador (Ctrl+K o «Buscar»). Mientras carga, o si falla, busca en el libro actual y lo avisa.
- Cada resultado muestra el libro del que viene y abre la sección directamente.

## Permisos: dependencia pendiente

Hoy la Biblioteca **no tiene control de acceso**. Todo lo publicado es público, y el buscador puede mostrarlo sin riesgo.

Cuando un libro tenga lectura restringida:
- su contenido **no puede entrar** en `js/busqueda-indice.js`, porque ese archivo es público y cualquiera puede leerlo;
- el buscador necesitará un índice servido por el servidor después de comprobar la identidad de la persona, que devuelva solo lo que esa persona puede leer;
- ocultar resultados en el navegador **no es seguridad**: los datos seguirían descargándose.

Hasta que exista ese servidor, un libro restringido se marca con `acceso` distinto de `"abierto"` en `data/libros.json` y queda fuera del índice.

## Regenerar

```
python tools/normas.py
python tools/sistema_diseno.py
python tools/biblioteca.py
python tools/gobierno.py
python tools/verificar.py
```
