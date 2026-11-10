# Clasificación normativa propuesta

**Estado:** propuesta pendiente de aprobación humana. La clasificación normativa propuesta por un agente de IA requiere aprobación humana antes de adquirir vigencia.

**Método:** se recorrió el texto aprobado de cada norma (data/referencia-contenido.json) y se clasificó cada frase según sus expresiones normativas. No se modificó ningún texto. Cada requisito recibe una referencia interna (por ejemplo, `KYN-MRK-COL-004.2`) que conserva el ID principal.

## Resumen

| Dato | Valor |
|---|---|
| Normas inventariadas | 125 |
| Requisitos detectados | 226 |
| DEBE | 89 |
| NO DEBE | 84 |
| DEBERÍA | 9 |
| PUEDE | 44 |
| Requisitos con ambigüedad | 40 |
| Frases duplicadas entre normas | 0 |
| Contradicciones con el código | 7 |

## Ámbitos propuestos

Se asignaron por área de la norma. Ninguno está aprobado; `data/autoridad.json` los registra vacíos hasta su aprobación.

| Área | Ámbitos propuestos |
|---|---|
| ADN | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons, Servicios y procesos operativos |
| CMP | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons |
| COL | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons |
| CON | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons |
| DAT | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons |
| DIS | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons, Servicios y procesos operativos |
| ESP | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons |
| GAL | Identidad corporativa Keyons, Web corporativa y Biblioteca |
| ICN | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons |
| ICO | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons |
| ILU | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons |
| LOG | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons |
| PER | SaaS con identidad Keyons, Productos personalizados, Productos con identidad del cliente |
| PLA | Identidad corporativa Keyons, Web corporativa y Biblioteca |
| PRE | Identidad corporativa Keyons, Servicios y procesos operativos |
| REF | Identidad corporativa Keyons, Web corporativa y Biblioteca |
| TEX | Identidad corporativa Keyons, Web corporativa y Biblioteca |
| TYP | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons |
| VIS | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons |
| VOZ | Identidad corporativa Keyons, Web corporativa y Biblioteca, Herramientas internas, SaaS con identidad Keyons, Servicios y procesos operativos |

Las normas de calidad y experiencia KYN-MRK-VIS-008 suman Productos personalizados y Productos con identidad del cliente.

## Contradicciones entre normas y código

| Norma | Detalle |
|---|---|
| KYN-MRK-TYP-004 | El kicker se especifica en TASA Orbiter 500, 14 px, +8 %; el código lo aplica en Plus Jakarta Sans 700, 12 a 13 px, +2 %. |
| KYN-MRK-TYP-002 | El estándar de tracking (8.8) fija 0em para títulos en Plus Jakarta Sans; los títulos de sección del libro usan −3 %. |
| KYN-MRK-TYP-002 | El estándar fija −3 % de 52 a 79 px y −5 % desde 80 px para TASA Orbiter; el display del libro usa −4 %. |
| KYN-MRK-ILU-003 | Divisor de 1 px en Gris Bruma y divisor fuerte en Azul Noche al 16 %; el libro usa Azul Cielo 100 y 200, y barras de 4 px en tablas. |
| KYN-MRK-ILU-007 | El texto fija Azul Cielo y trazos uniformes para las tramas; desde la ronda 15 se muestran en Azul Noche con trazo a mano. |
| KYN-MRK-ICO-005 | Los íconos de la marca salen del catálogo; las flechas de navegación del libro son íconos de 1,6 px fuera del catálogo. |
| KYN-MRK-ESP-004 | La retícula fija contenido hasta 1520 px; el libro usa un documento de 1600 px. |

## Ambigüedades por revisar

| Referencia | Nivel propuesto | Motivo | Frase |
|---|---|---|---|
| KYN-MRK-ADN-001.1 | DEBE | «siempre» sin verbo normativo | Cada modalidad ofrece distintos niveles de adaptación y acompañamiento, siempre a partir de las necesidades reales de la operación. |
| KYN-MRK-COL-001.1 | DEBE | «siempre» sin verbo normativo | La paleta base está siempre; las demás se suman, de mayor a menor presencia, según el contexto real de cada pieza. 01Paleta base 02Cielos expresivos 03Colores f… |
| KYN-MRK-COL-001.3 | DEBE | «siempre» sin verbo normativo | La marca siempre se reconoce y aun así respira distinto según el mensaje. |
| KYN-MRK-COL-008.1 | NO DEBE | varias expresiones normativas en la misma frase | Cielos especiales Un sistema que crece Auroras, tormentas de arena, monzones o cielos volcánicos pueden sumarse como excepción, nunca como reemplazo de los cinc… |
| KYN-MRK-COL-010.2 | DEBE | «siempre» sin verbo normativo | Cuando conviven, Cielo siempre ocupa más. |
| KYN-MRK-COL-011.3 | DEBE | «siempre» sin verbo normativo | No es obligatorio que supere siempre la superficie de la paleta base. |
| KYN-MRK-CON-001.1 | DEBE | «siempre» sin verbo normativo | Cuando la marca llega a un nuevo país, suma los cielos de ese lugar, siempre con fotografías reales. |
| KYN-MRK-CON-006.1 | DEBE | varias expresiones normativas en la misma frase | Su aplicación responde al propósito de cada composición y no exige incorporar elementos figurativos o recursos expresivos cuando no aportan valor. 01Presencia h… |
| KYN-MRK-CON-006.3 | DEBE | varias expresiones normativas en la misma frase; «siempre» sin verbo normativo | (Intervención con IA)La inteligencia artificial puede participar para potenciar o extender la pieza, siempre que respete la dirección creativa y el concepto ini… |
| KYN-MRK-CON-007.1 | DEBE | «siempre» sin verbo normativo | (Lo disruptivo)Un elemento inesperado que muestra que ya no hay límites, siempre con sobriedad. |
| KYN-MRK-DAT-001.7 | DEBE | varias expresiones normativas en la misma frase; «siempre» sin verbo normativo | (PUEDE · Expresión visual)La identidad Keyons puede expresarse mediante composición editorial, tipografía, color, geometría, líneas y tramas, siempre que conser… |
| KYN-MRK-DAT-002.1 | DEBE | imperativo en infinitivo: se interpreta como DEBE | Utilizar la escala oficial existente en el proyecto.Los tonos claros y oscuros permiten representar magnitudes, relaciones y jerarquías según el contexto. |
| KYN-MRK-DAT-002.2 | DEBE | varias expresiones normativas en la misma frase | Puede destacar una categoría o establecer un contraste cálido entre series.Su significado cromático debe conservarse independiente de los estados desfavorables. |
| KYN-MRK-DIS-005.2 | DEBE | varias expresiones normativas en la misma frase | Una experiencia clara 01Dónde se está 02Qué se puede hacer 03Qué está ocurriendo 04Cómo continuar (La complejidad)Keyons debe resolver la complejidad durante el… |
| KYN-MRK-ESP-002.1 | DEBE | varias expresiones normativas en la misma frase | El tamaño puede orientar la elección, pero no determina automáticamente que una superficie grande deba tener esquinas más redondeadas. r-micro3 px (Tamaño de re… |
| KYN-MRK-ESP-004.3 | DEBE | varias expresiones normativas en la misma frase; «siempre» sin verbo normativo | La cantidad de columnas se adapta a la tarea y al espacio disponible.02Estructura adaptablePara sitios web, páginas informativas y experiencias comerciales.Las … |
| KYN-MRK-ESP-005.2 | DEBE | «siempre» sin verbo normativo | Una composición limpia no necesita ser siempre poco densa. |
| KYN-MRK-ESP-005.4 | DEBERÍA | varias expresiones normativas en la misma frase | (Ejemplo)Propuesta comercial: una idea, mucho aireCorporativo · densidad contenidaPrioriza una jerarquía clara, espacio negativo y una lectura cómoda.La cantida… |
| KYN-MRK-ICO-002.1 | DEBE | «siempre» sin verbo normativo | (Interfaz · sólida)Solo para el estado activo o seleccionado, y siempre como pareja de un ícono de contorno. |
| KYN-MRK-ICO-003.2 | DEBE | «siempre» sin verbo normativo | Debajo de 16 se pierde el trazo.Con textoÍcono y etiqueta a 8 px de distancia, alineados al centro.Sin textoSolo para acciones universales; siempre con nombre a… |
| KYN-MRK-ICO-004.1 | DEBE | «siempre» sin verbo normativo | Animación Siempre en la misma dirección Todos los íconos usan la misma animación: aparecen desde el centro y se asientan en 550 ms, para que la familia se mueva… |
| KYN-MRK-ICO-005.2 | DEBE | «siempre» sin verbo normativo | El trazo es siempre el mismo; lo que cambia es el fondo sobre el que viven. |
| KYN-MRK-ILU-001.1 | DEBE | «siempre» sin verbo normativo | Funcionan con dos ritmos independientes: la forma alterna siempre y el color varía según el modo. |
| KYN-MRK-ILU-001.2 | DEBE | «siempre» sin verbo normativo | (Por defecto)La secuencia alterna círculo y cuadrado y siempre abre con el círculo. |
| KYN-MRK-ILU-001.5 | DEBE | «siempre» sin verbo normativo | Abre siempre la secuencia Segunda en la secuencia Por defecto en lo expresivo y en modo nocturno Documentos largos y manuales, con el vacío en Blanco Keyons En … |
| KYN-MRK-ILU-002.3 | DEBE | «siempre» sin verbo normativo | (Itálica)Lo llamamos human in the loop: la persona siempre decide.Para palabras en otro idioma, títulos de obras, citas y voces de otros. |
| KYN-MRK-ILU-005.3 | DEBE | «siempre» sin verbo normativo | No se combinan entre sí dentro de una misma ventana, no se deforman y solo se rotan en ángulos cardinales.03Siempre con cieloDentro de la figura siempre hay cie… |
| KYN-MRK-ILU-006.1 | DEBE | «siempre» sin verbo normativo | Tampoco sobre fondos de color: siempre sobre Blanco Keyons o Crema. |
| KYN-MRK-ILU-008.2 | DEBE | «siempre» sin verbo normativo | Contexto humanoLuz y fondoFondos limpios e iluminación natural o de estudio, siempre consistente.Retratos corporativosFondo Azul Cielo #729BDD o un degradado de… |
| KYN-MRK-LOG-001.2 | DEBERÍA | varias expresiones normativas en la misma frase | Un bloque sólido y compacto: el nombre en dos niveles, KEY y ONS, guía la pronunciación, expresa la naturaleza modular de nuestras soluciones y dibuja una llave… |
| KYN-MRK-LOG-006.3 | DEBE | «siempre» sin verbo normativo | No reorganizarKEY y ONS van siempre en dos niveles. |
| KYN-MRK-LOG-006.4 | DEBE | «siempre» sin verbo normativo | No recortarLa palabra se muestra completa, siempre. |
| KYN-MRK-LOG-008.2 | NO DEBE | varias expresiones normativas en la misma frase | (Todavía no · Audiencias que no conocen la marca)El isotipo no debe sustituir automáticamente al nombre completo cuando el público todavía no puede reconocerlo … |
| KYN-MRK-PRE-003.1 | NO DEBE | varias expresiones normativas en la misma frase | Keyons ocupa como máximo una diapositiva, y nunca la primera.Donald MillerStoryBrand002Entre lo que es y lo que podría serLa historia alterna el hoy y el mañana… |
| KYN-MRK-PRE-011.1 | DEBE | «siempre» sin verbo normativo | Riesgo y estado Cuatro niveles, siempre con la palabra Salen de la paleta de estados (KYN-MRK-COL-014): fondo pastel, texto en Azul Noche y el ícono en su tono … |
| KYN-MRK-PRE-011.3 | DEBE | «siempre» sin verbo normativo | CríticoTerracota · #F0D0CBSe atiende antes de seguir.AltoNaranja · #F5D8B8Tiene responsable y fecha.MedioMostaza · #F4E8C1Se vigila en el documento de apoyo.Baj… |
| KYN-MRK-TYP-005.2 | DEBE | varias expresiones normativas en la misma frase | (02 · Interlineado adecuado)Los titulares pueden utilizar un interlineado compacto cuando conservan la legibilidad.Los textos de lectura requieren espacio sufic… |
| KYN-MRK-VIS-008.1 | DEBE | «siempre» sin verbo normativo | Contraste insuficiente Delicado, pero siempre legible La delicadeza visual no justifica textos, controles ni datos ilegibles. |
| KYN-MRK-VOZ-006.2 | DEBE | «siempre» sin verbo normativo | No es obligatorio comenzar siempre en tercera persona ni cambiar automáticamente después del primer párrafo. |
| KYN-MRK-VOZ-007.1 | DEBE | «siempre» sin verbo normativo | Simplificar no significa alterar el significado ni prometer capacidades que el sistema no tiene. 01Explicar qué hacePresentamos primero la función o el resultad… |

## Frases repetidas en varias normas

Ninguna.

## Requisitos por norma

| Norma | DEBE | NO DEBE | DEBERÍA | PUEDE |
|---|---|---|---|---|
| KYN-MRK-ADN-001 | 2 | 0 | 0 | 0 |
| KYN-MRK-ADN-002 | 0 | 0 | 0 | 0 |
| KYN-MRK-ADN-003 | 0 | 1 | 0 | 0 |
| KYN-MRK-ADN-004 | 0 | 0 | 0 | 0 |
| KYN-MRK-ADN-005 | 1 | 0 | 0 | 0 |
| KYN-MRK-ADN-006 | 0 | 1 | 0 | 0 |
| KYN-MRK-ADN-007 | 0 | 0 | 0 | 0 |
| KYN-MRK-CMP-001 | 0 | 0 | 0 | 0 |
| KYN-MRK-CMP-002 | 0 | 0 | 0 | 0 |
| KYN-MRK-CMP-003 | 0 | 1 | 0 | 0 |
| KYN-MRK-CMP-004 | 0 | 0 | 0 | 1 |
| KYN-MRK-COL-001 | 2 | 1 | 0 | 0 |
| KYN-MRK-COL-002 | 0 | 0 | 0 | 1 |
| KYN-MRK-COL-003 | 0 | 1 | 0 | 0 |
| KYN-MRK-COL-004 | 0 | 1 | 1 | 1 |
| KYN-MRK-COL-005 | 0 | 0 | 0 | 0 |
| KYN-MRK-COL-006 | 0 | 0 | 0 | 0 |
| KYN-MRK-COL-007 | 0 | 1 | 0 | 0 |
| KYN-MRK-COL-008 | 0 | 1 | 0 | 0 |
| KYN-MRK-COL-009 | 2 | 1 | 0 | 1 |
| KYN-MRK-COL-010 | 1 | 0 | 0 | 1 |
| KYN-MRK-COL-011 | 2 | 0 | 0 | 1 |
| KYN-MRK-COL-012 | 0 | 0 | 0 | 0 |
| KYN-MRK-COL-013 | 0 | 1 | 0 | 0 |
| KYN-MRK-COL-014 | 3 | 1 | 0 | 0 |
| KYN-MRK-COL-015 | 0 | 0 | 0 | 1 |
| KYN-MRK-CON-001 | 1 | 0 | 0 | 0 |
| KYN-MRK-CON-002 | 0 | 1 | 0 | 0 |
| KYN-MRK-CON-003 | 0 | 1 | 0 | 1 |
| KYN-MRK-CON-004 | 2 | 1 | 0 | 1 |
| KYN-MRK-CON-005 | 0 | 1 | 0 | 0 |
| KYN-MRK-CON-006 | 5 | 0 | 0 | 0 |
| KYN-MRK-CON-007 | 1 | 0 | 0 | 0 |
| KYN-MRK-CON-008 | 0 | 0 | 0 | 0 |
| KYN-MRK-CON-009 | 0 | 0 | 0 | 1 |
| KYN-MRK-DAT-001 | 6 | 0 | 1 | 0 |
| KYN-MRK-DAT-002 | 5 | 1 | 0 | 4 |
| KYN-MRK-DAT-003 | 0 | 0 | 0 | 0 |
| KYN-MRK-DAT-004 | 0 | 1 | 0 | 0 |
| KYN-MRK-DAT-005 | 1 | 0 | 0 | 1 |
| KYN-MRK-DIS-001 | 1 | 0 | 0 | 0 |
| KYN-MRK-DIS-002 | 0 | 0 | 0 | 2 |
| KYN-MRK-DIS-003 | 0 | 0 | 0 | 0 |
| KYN-MRK-DIS-004 | 1 | 1 | 0 | 2 |
| KYN-MRK-DIS-005 | 3 | 0 | 0 | 2 |
| KYN-MRK-ESP-001 | 1 | 0 | 0 | 2 |
| KYN-MRK-ESP-002 | 1 | 1 | 0 | 0 |
| KYN-MRK-ESP-003 | 1 | 0 | 0 | 0 |
| KYN-MRK-ESP-004 | 3 | 0 | 0 | 1 |
| KYN-MRK-ESP-005 | 3 | 2 | 1 | 1 |
| KYN-MRK-ESP-006 | 2 | 1 | 0 | 0 |
| KYN-MRK-GAL-001 | 0 | 0 | 0 | 0 |
| KYN-MRK-ICN-001 | 0 | 0 | 0 | 0 |
| KYN-MRK-ICO-001 | 0 | 0 | 0 | 0 |
| KYN-MRK-ICO-002 | 1 | 0 | 0 | 0 |
| KYN-MRK-ICO-003 | 2 | 1 | 0 | 0 |
| KYN-MRK-ICO-004 | 1 | 1 | 0 | 0 |
| KYN-MRK-ICO-005 | 1 | 2 | 0 | 0 |
| KYN-MRK-ICO-006 | 0 | 0 | 0 | 0 |
| KYN-MRK-ILU-001 | 4 | 1 | 0 | 0 |
| KYN-MRK-ILU-002 | 1 | 3 | 0 | 1 |
| KYN-MRK-ILU-003 | 0 | 1 | 0 | 0 |
| KYN-MRK-ILU-004 | 0 | 3 | 0 | 0 |
| KYN-MRK-ILU-005 | 1 | 3 | 0 | 1 |
| KYN-MRK-ILU-006 | 1 | 5 | 0 | 0 |
| KYN-MRK-ILU-007 | 0 | 12 | 0 | 1 |
| KYN-MRK-ILU-008 | 1 | 1 | 0 | 0 |
| KYN-MRK-ILU-009 | 0 | 1 | 0 | 1 |
| KYN-MRK-LOG-001 | 0 | 1 | 3 | 0 |
| KYN-MRK-LOG-002 | 0 | 0 | 0 | 0 |
| KYN-MRK-LOG-003 | 0 | 0 | 0 | 0 |
| KYN-MRK-LOG-004 | 0 | 0 | 0 | 0 |
| KYN-MRK-LOG-005 | 0 | 0 | 0 | 0 |
| KYN-MRK-LOG-006 | 2 | 2 | 0 | 0 |
| KYN-MRK-LOG-007 | 0 | 0 | 0 | 0 |
| KYN-MRK-LOG-008 | 0 | 1 | 0 | 2 |
| KYN-MRK-LOG-009 | 0 | 0 | 0 | 0 |
| KYN-MRK-LOG-010 | 2 | 0 | 0 | 1 |
| KYN-MRK-PER-001 | 0 | 1 | 0 | 0 |
| KYN-MRK-PER-002 | 0 | 0 | 0 | 0 |
| KYN-MRK-PER-003 | 0 | 0 | 0 | 0 |
| KYN-MRK-PER-004 | 0 | 0 | 0 | 0 |
| KYN-MRK-PLA-001 | 0 | 0 | 0 | 0 |
| KYN-MRK-PLA-002 | 0 | 0 | 0 | 0 |
| KYN-MRK-PRE-001 | 0 | 0 | 0 | 1 |
| KYN-MRK-PRE-002 | 1 | 1 | 0 | 0 |
| KYN-MRK-PRE-003 | 0 | 1 | 0 | 0 |
| KYN-MRK-PRE-004 | 0 | 0 | 0 | 0 |
| KYN-MRK-PRE-005 | 0 | 0 | 0 | 1 |
| KYN-MRK-PRE-006 | 0 | 2 | 0 | 0 |
| KYN-MRK-PRE-007 | 0 | 0 | 0 | 0 |
| KYN-MRK-PRE-008 | 0 | 0 | 0 | 0 |
| KYN-MRK-PRE-009 | 0 | 0 | 0 | 0 |
| KYN-MRK-PRE-010 | 0 | 0 | 0 | 0 |
| KYN-MRK-PRE-011 | 2 | 1 | 0 | 0 |
| KYN-MRK-PRE-012 | 0 | 2 | 0 | 0 |
| KYN-MRK-PRE-013 | 0 | 0 | 0 | 0 |
| KYN-MRK-PRE-014 | 0 | 1 | 0 | 0 |
| KYN-MRK-REF-001 | 0 | 2 | 0 | 0 |
| KYN-MRK-REF-002 | 0 | 0 | 0 | 0 |
| KYN-MRK-TEC-001 | 0 | 1 | 0 | 0 |
| KYN-MRK-TEX-001 | 0 | 0 | 0 | 0 |
| KYN-MRK-TYP-001 | 0 | 0 | 0 | 0 |
| KYN-MRK-TYP-002 | 0 | 0 | 0 | 3 |
| KYN-MRK-TYP-003 | 0 | 0 | 0 | 0 |
| KYN-MRK-TYP-004 | 0 | 0 | 0 | 0 |
| KYN-MRK-TYP-005 | 3 | 1 | 1 | 0 |
| KYN-MRK-TYP-006 | 0 | 0 | 0 | 0 |
| KYN-MRK-VIS-001 | 1 | 0 | 0 | 0 |
| KYN-MRK-VIS-002 | 1 | 0 | 0 | 1 |
| KYN-MRK-VIS-003 | 1 | 1 | 0 | 0 |
| KYN-MRK-VIS-004 | 1 | 1 | 0 | 1 |
| KYN-MRK-VIS-005 | 0 | 2 | 0 | 0 |
| KYN-MRK-VIS-006 | 1 | 0 | 0 | 0 |
| KYN-MRK-VIS-008 | 2 | 0 | 0 | 1 |
| KYN-MRK-VIS-009 | 1 | 1 | 0 | 0 |
| KYN-MRK-VIS-010 | 0 | 0 | 0 | 0 |
| KYN-MRK-VIS-012 | 1 | 2 | 0 | 0 |
| KYN-MRK-VOZ-001 | 0 | 0 | 0 | 0 |
| KYN-MRK-VOZ-002 | 1 | 1 | 0 | 0 |
| KYN-MRK-VOZ-003 | 0 | 0 | 0 | 0 |
| KYN-MRK-VOZ-004 | 0 | 0 | 0 | 1 |
| KYN-MRK-VOZ-005 | 1 | 1 | 0 | 0 |
| KYN-MRK-VOZ-006 | 2 | 0 | 1 | 0 |
| KYN-MRK-VOZ-007 | 3 | 2 | 1 | 3 |
