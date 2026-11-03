---
manual: "Libro de Marca Keyons"
version: "0.1"
fecha: "2026-11-03"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
capitulo: "09"
titulo: "Forma y espacio"
area: "Fundamentos"
estado: "vigente"
rutas: ["/fundamentos/forma/espacio.html"]
normas: ["KYN-MRK-ESP-001", "KYN-MRK-ESP-002", "KYN-MRK-ESP-003", "KYN-MRK-ESP-004", "KYN-MRK-ESP-005", "KYN-MRK-ESP-006", "KYN-MRK-ESP-007"]
referencias: ["KYN-MRK-ADN-001", "KYN-MRK-ADN-003", "KYN-MRK-COL-002", "KYN-MRK-COL-004", "KYN-MRK-CON-006", "KYN-MRK-DAT-001", "KYN-MRK-ESP-001", "KYN-MRK-ESP-002", "KYN-MRK-ESP-003", "KYN-MRK-ESP-004", "KYN-MRK-ESP-005", "KYN-MRK-ESP-006", "KYN-MRK-ESP-007", "KYN-MRK-LOG-001", "KYN-MRK-LOG-006", "KYN-MRK-VOZ-003"]
---

# Capítulo 09 · Forma y espacio

Estado: vigente · Clave: forma · Ruta: `/fundamentos/forma/espacio.html` · Número anterior: 08

Interior curvo, exterior recto. Radio y separación.

**Contenido del capítulo**

- Regla de esquinas · borrador · `/fundamentos/forma/espacio.html#esquinas`
- Radios · borrador · `/fundamentos/forma/espacio.html#radios`
- Espaciado · borrador · `/fundamentos/forma/espacio.html#espaciado`
- Retícula y responsive · borrador · `/fundamentos/forma/espacio.html#reticula`
- Densidad · borrador · `/fundamentos/forma/espacio.html#densidad`
- Patrones de contenido · borrador · `/fundamentos/forma/espacio.html#patrones`
- Diagramas de información · borrador · `/fundamentos/forma/espacio.html#diagramas`

## Forma y espacio

Rótulo: Capítulo 09 · Fundamentos · Fuente: `/fundamentos/forma/espacio.html`

Las reglas invisibles que ordenan cada pieza: esquinas, radios, espacio y retícula.

## KYN-MRK-ESP-001 · 9.1 Regla de esquinas

Número: 9.1 · ID: `KYN-MRK-ESP-001` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#esquinas`

### Exterior recto, interior curvo

La geometría de Keyons distingue entre **contenedores independientes y conjuntos visuales**.

Un contenedor aislado utiliza esquinas rectas como tratamiento base. Cuando varios elementos forman un conjunto reconocible, pueden combinarse esquinas exteriores rectas e interiores curvas para expresar su relación.

**(Fila)**
En un conjunto horizontal, las esquinas exteriores son rectas y las interiores pueden curvarse cuando refuerzan la agrupación.

> Recurso visual: Gráfico SVG en línea · «Fila de tres recuadros»

**(Pila)**
Se aplica el mismo principio en vertical, respetando los límites exteriores del conjunto.

> Recurso visual: Gráfico SVG en línea · «Pila de tres recuadros»

**(Cuadrícula)**
La combinación de esquinas responde a la organización visual. No todas las cuadrículas requieren curvas interiores.

> Recurso visual: Gráfico SVG en línea · «Cuadrícula de cuatro recuadros»

**(Un contenedor)**
Las cuatro esquinas permanecen rectas cuando el elemento se presenta de forma independiente.

**(Botones y badges)**
Los botones mantienen una geometría curva, diferenciada de los contenedores. Las variantes, estados y transiciones funcionales se especifican en el Sistema de Diseño.
Los badges se rigen por su función y variante documentada, sin asumir automáticamente una geometría universal para todas las etiquetas.

## KYN-MRK-ESP-002 · 9.2 Radios

Número: 9.2 · ID: `KYN-MRK-ESP-002` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#radios`

### El radio responde a la función

Los radios se seleccionan según **la función del elemento, su tamaño y su relación** con otros componentes.

El tamaño puede orientar la elección, pero no determina automáticamente que una superficie grande deba tener esquinas más redondeadas.

**r-micro**
3 px

**(Tamaño de referencia)**
Menos de 24 px
**(Se usa en)**
Barras de datos, chips internos, marcas pequeñas

**r-control**
12 px

**(Tamaño de referencia)**
24 a 64 px
**(Se usa en)**
Campos, fichas de color, segmentos

**r-component**
18 px

**(Tamaño de referencia)**
64 a 200 px
**(Se usa en)**
Tarjetas y recuadros de contenido

**r-card**
30 px

**(Tamaño de referencia)**
200 a 400 px
**(Se usa en)**
Paneles y tarjetas grandes

**r-block**
50 px

**(Tamaño de referencia)**
Más de 400 px
**(Se usa en)**
Secciones y bloques de página

**(Anidados)**
Cuando un contenedor curvo contiene otro elemento, los radios y el espacio interior deben mantener una relación visual coherente, evitando encuentros irregulares.
La fórmula del radio exterior menos el relleno puede utilizarse como referencia geométrica, pero debe comprobarse visualmente y no aplicarse de manera automática en todos los casos.

**(En código)**
Siempre con su variable: `var(--r-card)`, nunca con un número suelto.

## KYN-MRK-ESP-003 · 9.3 Espaciado

Número: 9.3 · ID: `KYN-MRK-ESP-003` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#espaciado`

### Todo se mide en múltiplos de 4

La escala de espaciado utiliza **incrementos de 4 px** para organizar márgenes, separaciones y rellenos de forma consistente.

Sus valores son referencias para construir relaciones espaciales claras. La escala no sustituye las necesidades específicas de tipografía, bordes, adaptación responsive o representación gráfica.

s1 · 4 px · Entre ícono y su borde
s2 · 8 px · Ícono y texto
s3 · 12 px · Entre elementos de una lista
s4 · 16 px · Dentro de controles
s5 · 20 px
s6 · 24 px · Dentro de tarjetas
s8 · 32 px · Entre bloques relacionados
s10 · 40 px
s12 · 48 px · Entre componentes
s16 · 64 px · Entre grupos de contenido
s20 · 80 px
s24 · 96 px · Entre secciones
s32 · 128 px · Aire de sección

**(Criterio de uso)**
Las separaciones se eligen según la relación entre los elementos y la densidad necesaria. No es obligatorio utilizar grandes espacios en todos los contextos ni comprimir una composición para mostrar más información.
Cuando la escala no resuelva una necesidad técnica justificada, la excepción debe documentarse en el sistema correspondiente.

## KYN-MRK-ESP-004 · 9.4 Retícula y responsive

Número: 9.4 · ID: `KYN-MRK-ESP-004` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#reticula`

### Un piso, no un techo

La retícula organiza relaciones, proporciones y alineaciones. Las doce columnas constituyen **una referencia versátil**, pero la estructura debe adaptarse al contenido y a las necesidades de cada experiencia.

La claridad y la coherencia son obligatorias; una distribución específica de columnas no lo es en todos los formatos.

01
Estructura funcional
Para interfaces operativas, formularios, dashboards y documentación.
**(Criterio)** · La organización debe mantener alineaciones, agrupaciones y recorridos de lectura consistentes. La cantidad de columnas se adapta a la tarea y al espacio disponible.

02
Estructura adaptable
Para sitios web, páginas informativas y experiencias comerciales.
**(Criterio)** · Las columnas, los márgenes y las proporciones se ajustan al contenido sin perder coherencia.

03
Estructura editorial
Para campañas, presentaciones, piezas culturales y composiciones expresivas.
**(Criterio)** · Se permite una mayor experimentación mediante simetría, asimetría y cambios de escala, siempre que el contenido mantenga una lectura clara.

#### Cómo se adapta

| (Pantalla) | Ancho | Columnas | Margen |
|---|---|---|---|
| Móvil | Hasta 759 px | 4 | 16 px |
| Tableta | 760 a 1099 px | 8 | 32 px |
| Escritorio | 1100 a 1439 px | 12 | 64 px |
| Amplio | Desde 1440 px | 12 | Contenido hasta 1520 px |

El responsive no es un modo: es cómo esta retícula se adapta al ancho. El medianil es de 16 px en móvil y de 24 px en el resto.

Estos rangos documentan la retícula editorial de referencia. Los productos pueden necesitar ajustes según el ancho disponible, el contenido y las necesidades de sus usuarios. Sus puntos de adaptación se definen en el Sistema de Diseño.

La retícula proporciona orden sin imponer composiciones idénticas.

## KYN-MRK-ESP-005 · 9.5 Densidad

Número: 9.5 · ID: `KYN-MRK-ESP-005` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#densidad`

### Cuánta información cabe en un espacio

La densidad visual responde al **contenido, la frecuencia de uso y la atención** que requiere cada tarea.

Una composición limpia no necesita ser siempre poco densa. Una composición informativa no debe convertirse en una acumulación de elementos.

**(Ejemplo)**
Propuesta comercial: una idea, mucho aire

#### Corporativo · densidad contenida

Prioriza una jerarquía clara, espacio negativo y una lectura cómoda.

- La cantidad de bloques, llamadas a la acción y espacios depende de la información y de las decisiones que debe tomar el lector.

**(Cuándo se usa)** Se aplica a comunicaciones institucionales, documentos, propuestas y secciones editoriales donde conviene destacar las ideas principales.

**(Ejemplo)**
Post de campaña: varios elementos sobre la retícula

#### Expresivo · intensidad organizada

Permite una mayor presencia de recursos gráficos, información y variaciones compositivas cuando el contenido lo justifica.

- La retícula proporciona estructura, pero no obliga a distribuir todos los elementos en columnas idénticas.

**(Cuándo se usa)** Campañas, blog, contenido educativo, redes, piezas culturales y talleres.

#### Interfaz · según la tarea

La densidad debe facilitar la tarea, no dificultarla. Las vistas de uso frecuente pueden presentar información compacta cuando mantienen legibilidad, orientación y controles accesibles.

**(Ejemplo)**
Pantalla de bienvenida

Densidad baja

- Bienvenida y onboarding
- Errores y estados sensibles
- Pausas en flujos largos
- Confirmaciones importantes
- Primera vez y educación

**(Ejemplo)**
Formulario estándar

Densidad media

- Formularios estándar
- Información estructurada
- Flujos transaccionales de rutina

**(Ejemplo)**
Tablero operativo

Densidad alta

- Tableros de uso diario
- Tablas de datos
- Listados largos con filtros
- Vistas de monitoreo
- Pantallas para escanear rápido

La densidad adecuada permite comprender y actuar sin añadir ruido visual.

## KYN-MRK-ESP-006 · 9.6 Patrones de contenido

Número: 9.6 · ID: `KYN-MRK-ESP-006` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#patrones`

### La forma sale del contenido

La elección de una composición comienza por **comprender el contenido** y cómo necesita recorrerlo el lector.

Los patrones son alternativas de diseño, no plantillas obligatorias.

| (El contenido es) | Patrón posible | Ejemplo |
|---|---|---|
| Reglas o principios cortos, de tres a seis | Cuadrícula de reglas | KYN-MRK-CON-006 · Reglas de composición |
| Puntos que se leen uno a uno y pueden crecer | Acordeón | KYN-MRK-COL-004 · Reglas del color |
| Pares o tríos de explicaciones | Rótulo arriba, texto debajo | KYN-MRK-ADN-001 · Esencia |
| Ítems sin jerarquía | Lista con viñetas de marca | KYN-MRK-LOG-006 · Usos incorrectos |
| Comparación entre opciones | Matriz | KYN-MRK-ADN-003 · Espectro |
| Algo que se ve: color, logo, letra | Muestra en recuadro, con la regla de esquinas | KYN-MRK-LOG-001 · Versiones |
| Muchos ítems del mismo tipo | Selector o carrusel | KYN-MRK-VOZ-003 · Vocabulario |
| Ideas de distinto peso, que se recorren libremente | Retícula dinámica de líneas | KYN-MRK-DAT-001 · Principios |
| Datos y cifras | Número grande con su lectura | 14 · Datos |
| Una nota que señala algo | Flecha orgánica | KYN-MRK-COL-002 · Colores principales |

**(Uso)**
Las asociaciones de cuadrículas, acordeones, listas, matrices, carruseles, retículas, indicadores y flechas deben interpretarse como ejemplos. Un patrón debe elegirse por su utilidad, no por la cantidad de elementos o porque aparezca en el catálogo.

**(Relación con otros capítulos)**
Este capítulo establece criterios para seleccionar composiciones. El capítulo 10, Composiciones, desarrolla cómo utilizar simetría, asimetría, retículas y ritmo editorial. El Sistema de Diseño define los patrones funcionales de interacción.

La repetición aporta consistencia cuando facilita la comprensión. La variación se utiliza cuando el contenido necesita otro ritmo o una jerarquía diferente.

## KYN-MRK-ESP-007 · 9.7 Diagramas de información

Número: 9.7 · ID: `KYN-MRK-ESP-007` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#diagramas`

### Ordenar ideas, no medirlas

Los diagramas permiten explicar **relaciones entre ideas, etapas, áreas o componentes**. Su geometría debe corresponder a la relación representada: secuencia, agrupación, jerarquía, inclusión o conexión.

Los círculos, arcos y anillos son recursos disponibles, no soluciones obligatorias para cualquier contenido.

(Proceso)

Círculos que crecen

Fases que nacen del mismo punto: cada una contiene a la anterior. La línea baja desde el nombre de la fase y una estrella marca dónde toca su círculo.

> Recurso visual: Gráfico SVG en línea · «Fases que crecen desde un mismo punto: entender, construir y medir» · Textos: Entender / la operación / 01 / Construir / con su equipo / 02 / Medir / y mejorar / 03 · Al pasar el cursor: 01 · Diagnóstico · 2 a 4 semanas: Entender la operación / 02 · Diseño · 4 a 8 semanas: Construir con su equipo / 03 · Evolución · continua: Medir y mejorar

(Avance)

Zonas que crecen

Círculos que nacen del mismo borde; cada zona contiene a la anterior. Las etiquetas salen arriba y abajo, nunca a los lados.

> Recurso visual: Gráfico SVG en línea · «Zonas que crecen: de un uso básico de la IA a una operación transformada» · Textos: Uso básico / Primeras pruebas / IA integrada / Operación transformada · Al pasar el cursor: Zona 1: Uso básico / Zona 2: Primeras pruebas / Zona 3: IA integrada / Zona 4: Operación transformada

(Niveles)

Esferas de madurez

Del nivel difuso al nítido: la claridad crece con la madurez. Una estrella marca dónde está hoy.

> Recurso visual: Gráfico SVG en línea · «Esferas de madurez: del nivel 1 difuso al nivel 5 nítido» · Textos: 1 / Inicial / 2 / Explora / 3 / Define / 4 / Integra / 5 / Optimiza / Su empresa hoy · Al pasar el cursor: Nivel 1 · Inicial: Tareas manuales y dispersas / Nivel 2 · Explora: Primeras pruebas con IA / Nivel 3 · Define: Procesos documentados / Nivel 4 · Integra: IA en el trabajo diario / Nivel 5 · Optimiza: Mejora continua medida

(Relaciones)

Arcos de método

Fases que se superponen sobre una misma línea de trabajo.

> Recurso visual: Gráfico SVG en línea · «Arcos: fases que se superponen sobre una misma línea de trabajo» · Textos: Relación / Diagnóstico / Comprensión / Planeación / Construcción / Acompañamiento / Evolución / Inmersión / Estrategia / Proyecto / Soporte · Al pasar el cursor: Inmersión: Diagnóstico y comprensión / Estrategia: Comprensión y planeación / Proyecto: De la planeación al acompañamiento / Soporte: Acompañamiento y evolución

(Alcance)

Círculos de alcance

Círculos apoyados en un mismo punto, del más cercano al más amplio, con su nombre al costado.

> Recurso visual: Figura: «Tres círculos que crecen desde un mismo punto»

Su sector
Su empresa
Su equipo

(Contexto)

Anillos de contexto

Un tema dentro de los anillos que lo rodean, del más cercano al más amplio, con una idea al centro.

> Recurso visual: Gráfico SVG en línea · «Anillos de contexto: la IA dentro de los anillos de la operación» · Textos: Cultura / Gobierno de datos / Procesos / Personas / Herramientas / La IA no opera aislada: / es parte de toda la operación, / no una pieza aparte. · Al pasar el cursor: Cultura: Anillo 1 / Gobierno de datos: Anillo 1 / Procesos: Anillo 2 / Personas: Anillo 2 / Herramientas: Anillo 3

**(Uso)**
Se utilizan cuando una representación visual permite comprender relaciones que resultarían difíciles de comunicar únicamente mediante texto. Cuando el contenido contiene valores medidos, se elige una visualización cuantitativa adecuada, conforme al capítulo 14, Datos.

**(Construcción)**
Utilizar trazos precisos, continuos y uniformes, con contraste y etiquetas legibles. Los recursos de énfasis se incorporan cuando ayudan a interpretar el contenido. No es obligatorio utilizar estrellas, círculos o indicadores decorativos.
Las medidas de trazo y texto deben comprobarse según el tamaño final y el contexto de uso.

**(Ejemplos)**
Los diagramas que presentan etapas o duraciones no deben interpretarse automáticamente como fases oficiales de la metodología Prisma o compromisos de ejecución. Si un ejemplo representa una metodología oficial, debe coincidir con su documentación vigente.
