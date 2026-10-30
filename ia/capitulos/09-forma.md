---
manual: "Libro de Marca Keyons"
version: "0.1"
fecha: "2026-10-30"
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

La regla que da forma a todo el sistema: **la esquina que toca el borde del grupo es recta; la que mira a otro elemento, curva.** Así un conjunto se lee como una sola pieza.

**(Fila)**
Las esquinas de los extremos van rectas; las que se miran, curvas.

> Recurso visual: Gráfico SVG en línea · «Fila de tres recuadros»

**(Pila)**
Igual, en vertical: arriba y abajo rectas, adentro curvas.

> Recurso visual: Gráfico SVG en línea · «Pila de tres recuadros»

**(Cuadrícula)**
Cada recuadro solo curva la esquina que mira al centro del grupo.

> Recurso visual: Gráfico SVG en línea · «Cuadrícula de cuatro recuadros»

**(Un recuadro solo)**
Sus cuatro esquinas son exteriores: van rectas.

**(Botones y badges)**
Son la excepción: forma de píldora completa, porque no forman grupo con el contenedor.

## KYN-MRK-ESP-002 · 9.2 Radios

Número: 9.2 · ID: `KYN-MRK-ESP-002` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#radios`

### El radio depende del tamaño

Se elige mirando **el lado más corto del recuadro**: entre más grande, más radio. Cada ejemplo está en pareja porque, por la regla de esquinas, solo curvan las esquinas que se miran.

**r-micro**
3 px

**(Lado corto)**
Menos de 24 px
**(Se usa en)**
Barras de datos, chips internos, marcas pequeñas

**r-control**
12 px

**(Lado corto)**
24 a 64 px
**(Se usa en)**
Campos, fichas de color, segmentos

**r-component**
18 px

**(Lado corto)**
64 a 200 px
**(Se usa en)**
Tarjetas y recuadros de contenido

**r-card**
30 px

**(Lado corto)**
200 a 400 px
**(Se usa en)**
Paneles y tarjetas grandes

**r-block**
50 px

**(Lado corto)**
Más de 400 px
**(Se usa en)**
Secciones y bloques de página

**(Anidados)**
Un recuadro dentro de otro usa el radio exterior menos el relleno. Si el resultado es menor que 3 px, va recto.

**(En código)**
Siempre con su variable: `var(--r-card)`, nunca con un número suelto.

## KYN-MRK-ESP-003 · 9.3 Espaciado

Número: 9.3 · ID: `KYN-MRK-ESP-003` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#espaciado`

### Todo se mide en múltiplos de 4

Una sola escala para márgenes, separaciones y rellenos. **Si una distancia no está en la escala, no se usa.**

s1 · 4 px · Entre ícono y su borde
s2 · 8 px · Ícono y texto
s3 · 12 px · Entre líneas de una lista
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

## KYN-MRK-ESP-004 · 9.4 Retícula y responsive

Número: 9.4 · ID: `KYN-MRK-ESP-004` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#reticula`

### Un piso, no un techo

Doce columnas son **la base cuando no hay dirección creativa**. Entre más libre la pieza, más se puede romper.

01
Obligatoria
Se cumple siempre.
**(Aplica a)** · Interfaz de producto, tableros, formularios, plantillas, este libro y propuestas comerciales.

02
Recomendada
Es el punto de partida: márgenes y anchos se ajustan con criterio.
**(Aplica a)** · Landing pages, páginas de nicho y correos.

03
De referencia
Ayuda a componer o se rompe con intención.
**(Aplica a)** · Redes, campañas, piezas editoriales, pitch decks únicos y materiales culturales.

#### Cómo se adapta

| (Pantalla) | Ancho | Columnas | Margen |
|---|---|---|---|
| Móvil | Hasta 759 px | 4 | 16 px |
| Tableta | 760 a 1099 px | 8 | 32 px |
| Escritorio | 1100 a 1439 px | 12 | 64 px |
| Amplio | Desde 1440 px | 12 | Contenido hasta 1520 px |

El responsive no es un modo: es cómo esta retícula se adapta al ancho. El medianil es de 16 px en móvil y de 24 px en el resto.

En los tres niveles nunca se rompen la proporción, el aire y la legibilidad.

## KYN-MRK-ESP-005 · 9.5 Densidad

Número: 9.5 · ID: `KYN-MRK-ESP-005` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#densidad`

### Cuánta información cabe en un espacio

Aire y minimalismo en lo corporativo; intensidad ordenada en lo expresivo. **La densidad no decora: anuncia el tipo de contenido que viene.**

#### Corporativo · densidad baja

Pocos elementos por bloque, mucho espacio negativo y una idea protagonista por página. Respeta el tiempo del lector.

**(Cuándo)**

Propuestas, documentos institucionales, landing principal, hero web, comunicados y este libro.

**(Regla)**

Máximo tres bloques por pantalla en escritorio. Alrededor del elemento principal, un aire igual a su tamaño. Un solo CTA por sección.

**(Ejemplo)**
Propuesta comercial: una idea, mucho aire

#### Expresivo · densidad ordenada

Más elementos e intensidad informativa, siempre sobre la retícula. Nunca cae en desorden.

**(Cuándo)**

Campañas, blog, contenido educativo, redes, piezas culturales y talleres.

**(Regla)**

Las 12 columnas sostienen la composición: seis elementos ocupan dos columnas cada uno, con su medianil. La intensidad viene de la cantidad coherente, no del amontonamiento.

**(Ejemplo)**
Post de campaña: varios elementos sobre la retícula

#### Interfaz · según la tarea

No hay una densidad única, hay una adecuada para lo que el usuario necesita hacer en cada pantalla.

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

Aire o intensidad, siempre sobre la retícula: la densidad nunca se traduce en desorden.

## KYN-MRK-ESP-006 · 9.6 Patrones de contenido

Número: 9.6 · ID: `KYN-MRK-ESP-006` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#patrones`

### La forma sale del contenido

Antes de diagramar, la pregunta es **qué tipo de contenido es**. La respuesta decide el patrón; nunca al revés.

| (El contenido es) | Se diagrama como | Ejemplo |
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

Dos patrones iguales no van seguidos: el ritmo también comunica.

## KYN-MRK-ESP-007 · 9.7 Diagramas de información

Número: 9.7 · ID: `KYN-MRK-ESP-007` · Estado: vigente · Fuente: `/fundamentos/forma/espacio.html#diagramas`

### Ordenar ideas, no medirlas

Cuando no hay cifras sino relaciones (fases, zonas, niveles o áreas), la información se diagrama. **Mismo trazo fino, etiquetas grises y una estrella para lo que importa.**

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

**(Cuándo)**
Para explicar un método, un proceso o un contexto en una propuesta, una capacitación o una pieza de marca. Si hay datos medidos, va un gráfico del capítulo 14.

**(Cómo)**
Trazo de 1 px en Azul Noche, etiquetas en gris de 11 a 13 px y una estrella en el punto que se señala. Sin degradados ni sombras.
