# Auditoría del Libro 01 · Marca y Experiencia (2026-11-12)

Documento interno (no se publica). Acompaña al informe final de la rama `biblioteca-p1-p4`.

## A · Identidad y trazabilidad

| Comprobación | Resultado |
| --- | --- |
| IDs únicos (`data/normas.json`, `data/sistema-diseno.json` y entre ambos) | Sin duplicados: 129 KYN-MRK y 52 KYN-PRD-UIX |
| Ubicación canónica | Cada norma tiene una ruta `página#ancla` única. Las rutas anteriores se conservan como alias (`KEYONS_ALIAS`). |
| Referencias `KYN-*` en el texto | Todas resuelven a una norma registrada |
| Enlaces y anclas | 109 páginas revisadas. Ningún enlace roto real: las anclas `#cap-…` las crea la página al cargar. |
| Índice y contenido | Los índices de los dos libros llevan solo a anclas existentes. Diez normas (VIS-001 a VIS-012 y otras subsecciones) no tienen entrada propia en el índice: viven dentro de la sección de su capítulo. |
| Estado y vigencia | 125 vigentes y 4 en borrador (EST-001, LOG-011, RED-001 y TYP-007). Ninguna norma en borrador pasó a vigente. |
| Versión | Las 129 tienen versión (1.0) en `data/autoridad.json` |
| Historial | Huella de cada redacción aprobada, con fecha y nota (`data/referencia-contenido.json`), más el historial de Git |
| **Metadatos sin completar (no se inventan)** | **Ámbito, responsable y fecha de aprobación están vacíos en las 129 normas**, pendientes de designar. Los ámbitos propuestos están en `data/clasificacion-propuesta.json`, sin aprobar. |
| Web, Markdown y PDF | No se regeneran en esta ronda. LOG-011, RED-001 y TYP-007 aún no están en el PDF publicado. `verificar.py` lo informa como aviso. |

**Para Polaris:** cada norma se direcciona por libro (prefijo), capítulo (`nav-data.js`), sección (`página#ancla`) e ID. Cada recurso tiene ID propio (Galería KY-###, Íconos, Texturas). No hay autenticación ni roles: eso lo resuelven Polaris y el desarrollador.

## B · Debe, Debería y Puede

- Candidatos detectados: 225.
- **Aplicados (normas confirmadas con verbo modal explícito): 88.**
  - DEBE: 46
  - NO DEBE: 11
  - DEBERÍA: 1
  - PUEDE: 30
- **No normativos (descartados): 35.** Descripciones, ejemplos, glosario, títulos o citas.
- **En borrador: 5.** Se deciden al aprobar la norma.
- **Ambiguos reales: 5.** Van en la tabla de decisiones del informe.
- **Normas confirmadas sin verbo modal: 92.** Usan «siempre», «nunca», «podrá», «se permite» o «no es obligatorio». No se convirtieron solas: necesitan una redacción aprobada (lista abajo).

La palabra quedó en mayúscula dentro de la frase, sin cambiar nada más del texto. El ícono va al final del párrafo (Caso A: una norma con su explicación; Caso B: varias normas, un párrafo cada una; Caso C: texto descriptivo sin ícono), unido a la última palabra y con «Nivel: …» como alternativa accesible. Cuatro párrafos se separaron por tener dos normas: DAT-002, ESP-005, VIS-004 y VOZ-005.

**DAT-001:** sus filas usan el formato anterior, con el nivel como rótulo («(DEBE · Calidad)»). Pasarlas al formato nuevo (palabra en la frase e ícono al final) cambia el texto: pendiente de su decisión.

### Ambiguos (decisión de Keylin)

| Norma | Declaración | Por qué es ambigua |
| --- | --- | --- |
| KYN-MRK-COL-008 | Auroras, tormentas de arena, monzones o cielos volcánicos pueden sumarse como excepción, nunca como reemplazo de los cinco cielos oficiales. | Mezcla dos fuerzas en una frase: PUEDE sumarse como excepción y nunca reemplazar a los cinco cielos (NO DEBE). Separar en dos declaraciones. |
| KYN-MRK-COL-002 | Va del acento puntual a superficies amplias, y es el único que puede tomar protagonismo en una pieza institucional. | «es el único que puede tomar protagonismo»: ¿es permiso para Azul Cielo (PUEDE) o prohibición para los demás colores (NO DEBEN)? |
| KYN-MRK-COL-011 | No es obligatorio que supere siempre la superficie de la paleta base. | «No es obligatorio que supere siempre la superficie de la paleta base»: ¿permiso (PUEDE quedar por debajo) o solo aclaración sin fuerza normativa? |
| KYN-MRK-ESP-001 | En un conjunto horizontal, las esquinas exteriores son rectas y las interiores pueden curvarse cuando refuerzan la agrupación. | Mezcla una regla implícita (las esquinas exteriores son rectas: DEBE) y una opción (las interiores PUEDEN curvarse). Separar. |
| KYN-MRK-ESP-002 | La fórmula del radio exterior menos el relleno puede utilizarse como referencia geométrica, pero debe comprobarse visualmente y no aplicarse de manera automática en todos los casos. | Mezcla PUEDE (la fórmula como referencia) y DEBE (comprobarla visualmente). Separar. |

### Normas confirmadas que necesitan redacción con verbo (una sola decisión para todas)

| Norma | Declaración |
| --- | --- |
| KYN-MRK-PRE-014 | Contraste medidoSolo grises oficiales; fotos siempre con velo. |
| KYN-MRK-PRE-014 | Salmón solo para el dato claveY nunca sobre Azul Cielo. |
| KYN-MRK-PRE-003 | Keyons ocupa como máximo una diapositiva, y nunca la primera. |
| KYN-MRK-PRE-012 | Una ventana, una fotografía o una cifra; nunca las tres. |
| KYN-MRK-PRE-012 | Aparecen al avanzarPor partes al hacer clic; nunca en bucle. |
| KYN-MRK-PRE-007 | Siempre en la misma posición. |
| KYN-MRK-PRE-006 | Lo que no cabe va a las notas, nunca a una letra más chica. |
| KYN-MRK-PRE-006 | Siempre con su fuente en el pie. |
| KYN-MRK-PRE-006 | Una cita externa necesita fuente y nunca cierra la presentación. |
| KYN-MRK-PRE-002 | Nunca se copian diapositivas viejas. |
| KYN-MRK-PRE-011 | El color nunca va solo. |
| KYN-MRK-COL-007 | Azules profundos reales, nunca violetas saturados. |
| KYN-MRK-COL-009 | Nunca gradientes, imágenes ni ilustraciones de galería. |
| KYN-MRK-COL-009 | Nunca abruptas ni bandeadas: varias paradas, blur, formas superpuestas o mallas. |
| KYN-MRK-COL-009 | Los dos se permiten si están bien hechos. |
| KYN-MRK-COL-014 | Los errores y resultados negativos utilizan rojo semántico, nunca Salmón Tierra. |
| KYN-MRK-COL-013 | El deshabilitado no necesita contraste mínimo; nunca se usa para texto que hay que leer. |
| KYN-MRK-COL-003 | Nunca reemplazan a la paleta principal. |
| KYN-MRK-COL-001 | La paleta base está siempre; las demás se suman, de mayor a menor presencia, según el contexto real de cada pieza. |
| KYN-MRK-COL-001 | Cambia su proporción según la pieza, nunca su presencia. |
| KYN-MRK-COL-010 | Cuando conviven, Cielo siempre ocupa más. |
| KYN-MRK-ESP-005 | Nunca queda suelto. |
| KYN-MRK-ESP-006 | Los círculos, arcos y anillos son recursos disponibles, no soluciones obligatorias para cualquier contenido. |
| KYN-MRK-ESP-006 | Las etiquetas salen arriba y abajo, nunca a los lados. |
| KYN-MRK-ESP-006 | No es obligatorio utilizar estrellas, círculos o indicadores decorativos. |
| KYN-MRK-ESP-004 | La claridad y la coherencia son obligatorias; una distribución específica de columnas no lo es en todos los formatos. |
| KYN-MRK-ESP-004 | Se permite una mayor experimentación mediante simetría, asimetría y cambios de escala, siempre que el contenido mantenga una lectura clara. |
| KYN-MRK-CMP-003 | La proporción, el aire y la legibilidad no se rompen nunca. |
| KYN-MRK-VIS-002 | Cuando el contenido puede organizarse mediante alineación, tipografía, espacio y separadores, no necesita encapsularse automáticamente. |
| KYN-MRK-DAT-004 | Nunca en bucle. |
| KYN-MRK-DAT-004 | Nunca, en ningún formato. |
| KYN-MRK-ILU-004 | Nunca sobre un fondo oscuro al 100 %, porque se pierde la lectura del cielo. |
| KYN-MRK-ILU-004 | Siempre con cielo real debajo, nunca con un degradado puro. |
| KYN-MRK-ILU-004 | El cristal filtra, nunca oculta. |
| KYN-MRK-ILU-002 | Lo anterior va en gris, nunca tachado. |
| KYN-MRK-ILU-002 | Nunca en recuadros ni acordeones. |
| KYN-MRK-ILU-002 | Nunca para frases completas ni como énfasis general. |
| KYN-MRK-ILU-008 | Montaña, bosque y paisaje: el lugar desde donde se mira el cielo, siempre como ancla y nunca como protagonista. |
| KYN-MRK-ILU-008 | Retratos y equipo en sesión, siempre con permiso y con luz natural. |
| KYN-MRK-ILU-008 | Luz y fondoFondos limpios e iluminación natural o de estudio, siempre consistente. |
| KYN-MRK-ILU-007 | Patrones y texturas son recursos de fondo o de superficie, nunca protagonistas. |
| KYN-MRK-ILU-007 | Construyen atmósfera, nunca ruido. |
| KYN-MRK-ILU-007 | Siempre nacen de la base y se abren hacia arriba. |
| KYN-MRK-ILU-007 | Sobre fondo oscuro o degradado de cielo, nunca sobre Blanco Keyons. |
| KYN-MRK-ILU-007 | Nunca una trama rígida. |
| KYN-MRK-ILU-007 | En fondos amplios; nunca detrás de texto largo. |
| KYN-MRK-ILU-007 | La forma contrasta con su columna: claro sobre oscuro u oscuro sobre claro, nunca dos tonos vecinos. |
| KYN-MRK-ILU-007 | Un solo color de la paleta con Blanco Keyons; nunca dos colores. |
| KYN-MRK-ILU-007 | El círculo siempre cruza la división: de un lado nítido, del otro disuelto en el difuminado. |
| KYN-MRK-ILU-007 | Se producen con código a partir de foto propia; nunca generadas por IA desde cero. |
| KYN-MRK-ILU-007 | Es terminación, nunca protagonista. |
| KYN-MRK-ILU-007 | Opacidad de 15 a 20 %, nunca más. |
| KYN-MRK-ILU-007 | Siempre del color del fondo, nunca de colores. |
| KYN-MRK-ILU-007 | Los patrones construyen atmósfera; nunca compiten con el contenido. |
| KYN-MRK-ILU-006 | Tampoco sobre fondos de color: siempre sobre Blanco Keyons o Crema. |
| KYN-MRK-ILU-006 | Nunca una mezcla de fases. |
| KYN-MRK-ILU-006 | TexturaGrano fino al 15 a 20 % de opacidad, siempre. |
| KYN-MRK-ILU-006 | Nunca geométrica ni un círculo perfecto. |
| KYN-MRK-ILU-006 | Nunca estática ni centrada. |
| KYN-MRK-ILU-006 | Orgánico, nunca mecánico. |
| KYN-MRK-ILU-006 | Se ubica en el blanco que rodea, nunca sobre la zona densa. |
| KYN-MRK-ILU-005 | Dentro de la figura siempre hay cielo real fotografiado por el equipo Keyons. |
| KYN-MRK-ILU-005 | Nunca un degradado digital puro, nunca stock, nunca una imagen generada por IA. |
| KYN-MRK-ILU-005 | Nunca menos del doble del grosor del canto. |
| KYN-MRK-ESP-003 | No es obligatorio utilizar grandes espacios en todos los contextos ni comprimir una composición para mostrar más información. |
| KYN-MRK-ESP-002 | Siempre con su variable: var(--r-card), nunca con un número suelto. |
| KYN-MRK-ICO-004 | Se anima al aparecer o al confirmar una acción, nunca en bucle. |
| KYN-MRK-ICO-005 | Los íconos de la marca se usan en tres colores y nunca en otros. |
| KYN-MRK-ICO-005 | EstadosÉxito, error o advertencia usan los colores de estado de KYN-MRK-COL-014, nunca un color nuevo. |
| KYN-MRK-ICO-002 | Solo para el estado activo o seleccionado, y siempre como pareja de un ícono de contorno. |
| KYN-MRK-ICO-003 | Sin textoSolo para acciones universales; siempre con nombre accesible. |
| KYN-MRK-ICO-003 | Nunca se redibujan. |
| KYN-MRK-LOG-008 | El isotipo podrá representar a Keyons sin el nombre cuando se autorice su autonomía conforme a los criterios establecidos en KYN-MRK-LOG-010. |
| KYN-MRK-LOG-010 | El isotipo podrá utilizarse como identificador independiente cuando exista reconocimiento comprobado entre las audiencias correspondientes y aprobación expresa de la dirección de marca. |
| KYN-MRK-LOG-006 | No reorganizarKEY y ONS van siempre en dos niveles. |
| KYN-MRK-LOG-006 | No recortarLa palabra se muestra completa, siempre. |
| KYN-MRK-LOG-001 | Nunca en Salmón. |
| KYN-MRK-LOG-001 | La primera opción siempre que el espacio lo permita. |
| KYN-MRK-TYP-002 | Las composiciones breves podrán utilizar título contextual, declaración protagonista y cuerpo. |
| KYN-MRK-TYP-002 | Los contenidos extensos podrán incorporar texto de entrada cuando ayude a organizar la lectura. |
| KYN-MRK-CON-003 | Nunca se publica un cielosin procedencia documentada. |
| KYN-MRK-CON-002 | No son cuotas obligatorias para cada documento, campaña o producto. |
| KYN-MRK-CON-002 | Nunca se fuerza un cielo solo por cambiar. |
| KYN-MRK-CON-006 | Cada pieza se contrasta con lo que no representa a la marca; si puede confundirse con otra identidad, regresa a diseño para asegurar carácter único. |
| KYN-MRK-CON-005 | (Receptor)Buscando información concreta.(Metáforas)Solo en secciones clave, nunca en la navegación. |
| KYN-MRK-CON-004 | Nace desde el boceto inicial, nunca como un filtro o adhesivo final. |
| KYN-MRK-VOZ-006 | No es obligatorio comenzar siempre en tercera persona ni cambiar automáticamente después del primer párrafo. |
| KYN-MRK-VOZ-007 | Las comparaciones ayudan a explicar conceptos complejos, siempre que no creen equivalencias incorrectas. |
| KYN-MRK-VOZ-007 | La traducción aclara, nunca reemplaza el nombre oficial. |
| KYN-MRK-REF-001 | Un identificador emitido nunca se renombra, se elimina ni se reutiliza. |
| KYN-MRK-REF-001 | El texto de la norma nunca se copia en otro documento, para que no se desactualice. |
| KYN-MRK-REF-001 | Cuando una regla de marca debe figurar en un contrato con terceros, como agencias o diseñadores externos, se redacta la cláusula completa y el ID va al final, solo como referencia administrativa. |

## C · Reglas que solo están en el código

| Categoría | Hallazgo |
| --- | --- |
| 1 · Documentada y cumplida | Radios (3.2, todos los tokens coinciden). Foco solo con teclado (4.5). Una sola línea (3.5), ahora también con líneas hechas con sombra. Grises de gráficos (1.11). Portadas lisas (1.12). Carruseles (R21). Viñetas alternadas (R02). |
| 2 · Documentada e incumplida | **Tracking (2.4):** la regla fija seis valores con tokens `--tr-0` a `--tr-3` y `--tr-caps`, pero `tokens.css` solo tiene `--tr-kicker`. `libro.css` usa 12 valores sueltos (−0,04 em, −0,025 em, −0,015 em, +0,06 em, +0,08 em…). Unificarlos cambia la apariencia: se deja para su decisión. **Corregido en esta ronda:** COL-009 tenía dos líneas seguidas, ahora resuelto por la regla general. |
| 3 · Solo en el código | Puntos de corte del responsive (600, 760, 900, 1000, 1100 y 1179 px). Tiempos de avance de los carruseles (Galería 5 s, versiones del logotipo 4,5 s, Prisma 3,6 s, dimensiones de Estela 7 s, cifras 3,2 s). Aparición al entrar en pantalla (`aparecer()`). Cristal (`--glass-*`). Atajo Ctrl+K. Propuestas de norma abajo. |
| 4 · Detalle técnico (no es norma) | Orden de carga de scripts, caché, índices generados, prefijos de clases. |
| 5 · Contradicción (decide Keylin) | **Kicker:** `reglas-visuales.md` 2.5 dice Plus Jakarta Sans 700, 12 px, +0,02 em; la página de Tipografía y `tipografia-datos.js` dicen TASA Orbiter 500, 12 px, +8 %. **Tracking de títulos:** el estándar (8.8) fija 0 para Plus Jakarta Sans y el libro usa −3 %. **Display:** el estándar fija −3 % / −5 % y el libro usa −4 %. **Divisores (ILU-003)**, **tramas (ILU-007)**, **flechas fuera del catálogo (ICO-005)** y **ancho de retícula (ESP-004: 1520 frente a 1600 px):** las mismas contradicciones que ya registra `tools/gobierno.py`. |

## Propuestas normativas (sin publicar)

1. **Puntos de corte:** documentar los cinco anchos con su función (móvil 600 y 760, tableta 900 y 1000, escritorio 1100 y 1179) y pedir que todo componente nuevo use solo esos.
2. **Avance automático de carruseles:** un tiempo por tipo (imágenes con texto, 7 s; imágenes, 4,5 s; cifras, 3,2 s); pausa al pasar el cursor; sin avance con movimiento reducido.
3. **Aparición al entrar en pantalla:** una sola vez, desplazamiento corto y opacidad, con `--m-base`; nunca con movimiento reducido.
4. **Tracking:** crear los tokens `--tr-0` a `--tr-3` y `--tr-caps` y llevar los 12 valores sueltos a la escala de seis. Cambia levemente la apariencia: decide Keylin.

## E · Exportaciones y acceso

- **Generación:** `tools/exportar.py` genera, desde las páginas oficiales, el Markdown completo (`ia/libro-de-marca.md`), uno por norma (`ia/normas/`) y el PDF completo (`--pdf`). En esta ronda no se corrió, por decisión de Keylin.
- **Niveles en Markdown y PDF:** `exportar.py` ya escribe «(Debe)», «(Debería)» o «(Puede)» al final de cada párrafo con ícono (probado en una página; no se regeneró nada).
- **Riesgo de acceso, antes de integrar Polaris:** hoy son públicos y se enlazan desde el menú lateral:
  - `documental/libro-de-marca-keyons.pdf`
  - `documental/sistema-diseno-keyons.pdf`
  - `ia/libro-de-marca.md`
  - `ia/normas/*.md`
  - `ia/sistema-diseno.md`
  - `llms.txt`
  - `data/*.json`, con el texto completo de cada sección en `referencia-contenido.json`
- **PRIORITARIO · información restringida expuesta:** en producción (`main`), la carpeta `propuestas/` se publica completa. Incluye material de cliente (formularios y presentación del taller Genia, logotipos de Ingenya y dos archivos `.zip`). La rama `biblioteca-p1-p4` ya la excluye en `.vercelignore`, pero producción no cambia hasta su aprobación. `tools/` también es público en producción.

