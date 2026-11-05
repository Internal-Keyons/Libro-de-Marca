# Gobierno normativo de la Biblioteca Keyons

**Estado:** En revisión, versión 0.1. Es una propuesta preparada por un agente de IA y requiere aprobación humana antes de adquirir vigencia.

**Implementación:** rama `consolidacion`, sin publicar.

---

## 1. Fuente común

Una sola fuente, `data/gobierno.json`, alimenta la web y la representación para IA.

`tools/gobierno.py` genera a partir de ella:

| Archivo | Contenido |
|---|---|
| `recursos/gobierno.html` | Página del capítulo 28 (Referencia) |
| `ia/gobierno.json` | Convenciones y dimensiones de cada norma, para agentes |
| `data/autoridad.json` | Dimensiones de cada norma; conserva los valores ya aprobados |
| `js/autoridad.js` | Estado y versión que la web muestra bajo el ID de cada norma, en un rótulo discreto |
| `data/clasificacion-propuesta.json` y `docs/CLASIFICACION_NORMATIVA.md` | Inventario y clasificación propuesta; no modifica ningún texto |

`llms.txt` remite primero a las convenciones de autoridad, que son el paso 1 de la ruta para agentes de IA.

## 2. Inventario de las convenciones existentes

| Convención | Dónde estaba | Se conserva | Observación |
|---|---|---|---|
| ID permanente `KYN-MRK-XXX-###` | `data/normas.json`, `tools/normas.py` | Sí | Formato común: `KYN-<LIBRO>-<ÁREA>-###` |
| Prefijo `KYN-SDI` | `docs/SISTEMA_DE_DISENO_NORMAS.md` | Sí, como propuesta | Sigue sin emitir |
| Prefijo `KYN-PRD` | Manual de Producto | Sí | Identificadores históricos |
| Alias y traslados (redirección de enlaces viejos) | `tools/normas.py`, `js/secciones.js` | Sí | Resuelven referencias tras mover normas |
| Estado «integrada» | `tools/normas.py` (`INTEGRADAS`) | Sí | Estado adicional; equivale a Descontinuada con destino |
| Estados documentales: Vigente, Borrador, Por definir, Estructura definida, En revisión, Descontinuado | `js/libro.js` (`STATUS`) | Sí | Borrador, Por definir y Estructura definida equivalen a En revisión |
| Aprobación de contenido | `tools/verificar.py --aprobar`, `data/referencia-contenido.json` | Sí | Registra el texto aprobado, sin responsable ni fecha |
| Exportación para IA | `tools/exportar.py`, `ia/` | Sí | Se sumó `ia/gobierno.json` |
| Permisos | `tools/exportar.py`: «por definir» | Sí | Sin control de acceso hoy |

## 3. Discrepancias para revisión y aprobación

1. **Género del estado.**
   - `js/libro.js` dice «Descontinuado» (masculino).
   - El gobierno usa «Descontinuada», porque concuerda con «norma».
   - Hay que unificar.
2. **Responsable de aprobación.** No está designado.
   - La propuesta es que sean los Co-Editores Generales, que KYN-MRK-ILU-005 ya cita como autoridad.
   - `data/autoridad.json` registra `responsable: null` hasta la aprobación.
3. **Fecha de aprobación.** El registro de contenido guarda el texto aprobado, pero no la fecha ni quién aprueba. Ambos campos quedan vacíos.
4. **Versión.** Ninguna norma tenía versión. Se asignó 1.0 a las vigentes y 0.1 al resto, como punto de partida.
5. **Ámbitos.**
   - Ninguna norma declaraba ámbito.
   - La propuesta por área está en `docs/CLASIFICACION_NORMATIVA.md`.
   - `data/autoridad.json` los mantiene vacíos hasta su aprobación.
6. **Niveles de obligación.**
   - Los textos usan «debe», «nunca», «puede» y verbos en infinitivo, sin mayúsculas normativas.
   - La clasificación propuesta detectó 219 requisitos y 37 ambigüedades.
   - **Los textos aprobados no se modificaron.** Las mayúsculas normativas se aplicarán solo a los fragmentos que se aprueben.
7. **Referencias internas de requisito** (`KYN-MRK-COL-004.2`). Es un formato nuevo y queda por aprobar.
8. **Permisos de consulta.**
   - La Biblioteca es estática y pública.
   - Ni la búsqueda filtrada por permisos ni la ruta E (terceros autorizados) pueden cumplirse sin un servicio de autenticación.
9. **Contradicciones entre normas y código.** Hay siete; están listadas en `docs/CLASIFICACION_NORMATIVA.md` y en `docs/AUDITORIA_NORMAS_VS_UI.md`.

## 4. Navegación común (primera implementación)

**Cabecera:**
- **Izquierda:** el control «Índice» (en móvil, ícono con el nombre accesible «Abrir índice») y el selector del libro actual con los seis libros. Los que no están disponibles aparecen «En preparación», sin enlace.
- **Centro:** el logotipo, que lleva a la portada de la Biblioteca.
- **Derecha:** la búsqueda, que ahora también encuentra los libros.

**El control «Índice» tiene una sola función:**
- En escritorio, muestra u oculta el lateral y recuerda la elección.
- En móvil y en las portadas, abre el índice como panel.

**Lateral:**
- Todas las áreas o módulos del libro, con el área y el capítulo actuales abiertos y las demás plegadas.
- Al final, la leyenda de estados y los enlaces secundarios.
- En móvil empieza con «Libro actual» y «Cambiar libro».

**Accesibilidad:**
- `aria-expanded` y `aria-controls` en el índice, en el selector, en cada área y en cada capítulo.
- `aria-current="page"` en el destino actual.
- Escape cierra el panel y devuelve el foco al control.
- Al elegir un destino, el panel se cierra.
- `#indice` abre el índice al cargar la página.

**Sin cambios:** tipografías, colores, logotipo, tamaños y animaciones de la cabecera.
