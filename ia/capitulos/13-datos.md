---
manual: "Libro de Marca Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
capitulo: "13"
titulo: "Datos y visualización"
area: "Fundamentos"
estado: "borrador"
rutas: ["/fundamentos/datos/graficos.html"]
normas: ["KYN-MRK-DAT-001", "KYN-MRK-DAT-002", "KYN-MRK-DAT-003", "KYN-MRK-DAT-004", "KYN-MRK-DAT-005"]
referencias: ["KYN-MRK-COL-014", "KYN-MRK-DAT-001", "KYN-MRK-DAT-002", "KYN-MRK-DAT-003", "KYN-MRK-DAT-004", "KYN-MRK-DAT-005"]
---

# Capítulo 13 · Datos y visualización

Estado: borrador · Clave: datos · Ruta: `/fundamentos/datos/graficos.html` · Número anterior: 11, 14

Gráficos que comunican con rigor: principios, color, tipografía y estructura.

**Contenido del capítulo**

- Principios · borrador · `/fundamentos/datos/graficos.html#principios`
- Sistema cromático · borrador · `/fundamentos/datos/graficos.html#paleta`
- Tipografía en gráficos · borrador · `/fundamentos/datos/graficos.html#tipografia`
- Tipos de gráfico · borrador · `/fundamentos/datos/graficos.html#tipos`
- Estructura · borrador · `/fundamentos/datos/graficos.html#estructura`

## Datos y visualización

Rótulo: Capítulo 13 · Fundamentos · Fuente: `/fundamentos/datos/graficos.html`

Hacer visible lo que importa, sin decorarlo.

## KYN-MRK-DAT-001 · 13.1 Principios

Número: 13.1 · ID: `KYN-MRK-DAT-001` · Estado: vigente · Fuente: `/fundamentos/datos/graficos.html#principios`

### Exactitud, claridad y utilidad

Los gráficos Keyons convierten información en **conocimiento comprensible**.

#### Cada decisión visual tiene una función

- Facilitar comparaciones.
- Mostrar cambios.
- Comunicar proporciones.
- Explicar relaciones.
- Identificar patrones.
- Destacar resultados.
- Mostrar avances.
- Comparar lo actual con lo propuesto.

#### Reglas fundamentales

**(DEBE · Calidad)**
La calidad del gráfico se determina por su exactitud, claridad, utilidad y coherencia visual.

**(DEBE · Integridad de los datos)**
La representación visual conserva las proporciones y relaciones reales de la información.

**(DEBE · Escalas adecuadas)**
Las barras de magnitud parten de cero. Las líneas y otras representaciones utilizan escalas que permiten interpretar correctamente las variaciones, con límites visibles y contexto suficiente.

**(DEBE · Contexto verificable)**
Cada visualización identifica qué representa, sus unidades, su período y su fuente cuando corresponda.

**(DEBE · Comparabilidad)**
Los gráficos utilizados para comparar alternativas mantienen criterios, unidades y escalas equivalentes.

**(DEBERÍA · Prioridad informativa)**
Cada gráfico comunica una conclusión principal o facilita responder una pregunta concreta.

**(PUEDE · Expresión visual)**
La identidad Keyons puede expresarse mediante composición editorial, tipografía, color, geometría, líneas y tramas, siempre que conserve la precisión de los datos.

Detrás de cada número hay personas: el gráfico lo recuerda, no lo decora.

## KYN-MRK-DAT-002 · 13.2 Sistema cromático

Número: 13.2 · ID: `KYN-MRK-DAT-002` · Estado: vigente · Fuente: `/fundamentos/datos/graficos.html#paleta`

### Tres paletas, según el significado

Las paletas se organizan según el significado de los datos: **categórica, secuencial y divergente**. Estas tres familias responden a funciones estadísticas diferentes.

Las fuentes cromáticas proceden de la paleta corporativa y sus escalas, complementadas por colores funcionales autorizados cuando corresponda.

Esta organización amplía la clasificación histórica «paleta base, monocromática y suave»: la clasificación histórica describe familias de colores; la nueva describe para qué se utiliza cada familia.

#### Colores corporativos disponibles

| (Color) | Referencia | Función |
|---|---|---|
| Azul Noche | #10122A | Texto, estructura, fondos profundos y contrastes |
| Blanco Keyons | #F4F4F4 | Fondo, espacio negativo y superficies claras |
| Azul Cielo | #729BDD | Acento principal y color protagonista |
| Salmón Tierra | #CE635D | Contraste cálido y categorías destacadas |
| Salmón Atardecer | #E99D9E | Acento claro sobre Azul Noche |

#### Condiciones cromáticas

**(Azul Cielo)**
Es el color principal de referencia para gráficos corporativos.
Su escala funcional se organiza del 100 al 900, con base 500 en #729BDD. Utilizar la escala oficial existente en el proyecto.
Los tonos claros y oscuros permiten representar magnitudes, relaciones y jerarquías según el contexto.

**(Azul Noche)**
Proporciona estructura, legibilidad y contraste.
Se utiliza para texto principal, títulos, cifras, ejes, contornos y superficies oscuras cuando corresponde.

**(Salmón Tierra)**
Es el salmón oscuro. Puede destacar una categoría o establecer un contraste cálido entre series.
Su significado cromático debe conservarse independiente de los estados desfavorables. NO DEBE utilizarse para comunicar por sí mismo errores, pérdidas, resultados negativos o alertas críticas.

**(Salmón Atardecer)**
Es el salmón claro. Su aplicación característica es sobre Azul Noche, donde consigue una relación de contraste adecuada.
Es una opción para destacar cifras protagonistas y elementos expresivos en composiciones oscuras.

#### Paleta categórica

Para distinguir series sin orden entre sí. Parte de la paleta base corporativa.

#### Paleta secuencial

Para magnitudes ordenadas, del claro al profundo en pasos parejos. La de Azul Cielo es la de uso diario.

#### Paleta divergente

Azul Noche, Azul Cielo, Lavanda, Salmón Tierra, Salmón Atardecer, Blanco Keyons, Amarillo claro de los cielos y Ámbar de los cielos.

Nota
Esta combinación conserva la relación entre los azules de la identidad y los tonos cálidos de los cielos. Los dos extremos representan direcciones diferentes respecto al centro. Su significado depende de los datos y se comunica mediante etiquetas y unidades.

**(DEBE · Referencia central)**
Cada gráfico divergente identifica el valor que separa las dos direcciones de variación.

**(DEBE · Orden cromático)**
La progresión respeta el orden de la escala y mantiene una correspondencia consistente con los intervalos numéricos representados.

**(DEBE · Contraste)**
Los textos, cifras y elementos funcionales se presentan con el contraste requerido para su lectura. Azul Noche es la referencia tipográfica sobre los tonos complementarios claros.

**(PUEDE · Expresión editorial)**
Las ilustraciones e infografías pueden utilizar estos colores con mayor libertad compositiva, conservando los significados estadísticos cuando representan datos.

#### Aplicaciones

**(Gráficos corporativos)**
Utilizar la paleta divergente para desviaciones, diferencias respecto a referencias y variaciones bidireccionales.

**(Informes y presentaciones)**
La composición puede destacar los extremos y la referencia central mediante tipografía, espacio, posición y valores numéricos.

**(Infografías)**
La paleta puede expresar relaciones entre dos condiciones, manteniendo información suficiente para comprender las diferencias.

**(Ilustraciones)**
Los colores complementarios de los cielos pueden utilizarse en composiciones expresivas, de acuerdo con las normas de identidad visual Keyons.

**(Dashboards)**
El Sistema de Diseño establecerá su implementación técnica, adaptación responsive, tokens, leyendas, estados y accesibilidad.

#### Colores semánticos

Los colores semánticos pertenecen a estados como éxito, advertencia, error, información y estado crítico.

Nota
La paleta semántica se utiliza para comunicar estados, mientras que las paletas estadísticas representan categorías, magnitudes y diferencias.

Nota
Para pérdidas, errores y resultados desfavorables se utiliza el color semántico correspondiente, acompañándolo de texto, símbolo o indicador explícito. La definición técnica de esos colores procede del catálogo semántico oficial del proyecto (KYN-MRK-COL-014).

## KYN-MRK-DAT-003 · 13.3 Tipografía en gráficos

Número: 13.3 · ID: `KYN-MRK-DAT-003` · Estado: vigente · Fuente: `/fundamentos/datos/graficos.html#tipografia`

### Los números pesan igual que las barras

Cada texto del gráfico tiene su nivel. **Toda cifra usa números tabulares.**

**(Etiqueta)**
(Horas recuperadas · Enero a junio 2026)
Jakarta 500 · 12 px, gris. Dice qué se mide y cuándo.

**(Cifra protagonista)**
+38 %
TASA Orbiter 400 · 40 a 96 px. Una por gráfico.

**(Lectura)**
Menos trabajo repetitivo en seis meses, por persona.
Jakarta 400 · 14 px. Explica la cifra en una frase.

**(Ejes y valores)**
Ene Feb Mar Abr May Jun
Jakarta 500 · 12 px, números tabulares.

**(Fuente)**
Fuente: Diagnóstico Keyons, 15 entrevistas, 2026
Jakarta 400 · 12 px, gris nivel 3.

| (Formato) | Español | Inglés |
|---|---|---|
| Miles | 1.000 | 1,000 |
| Decimales | 3,5 | 3.5 |
| Porcentaje | 45 % | 45% |
| Moneda | ₡ 1.500 | $ 1,500 |
| Cifras grandes | 1,2 M | 1.2M |

## KYN-MRK-DAT-004 · 13.4 Tipos de gráfico

Número: 13.4 · ID: `KYN-MRK-DAT-004` · Estado: vigente · Fuente: `/fundamentos/datos/graficos.html#tipos`

### El gráfico correcto según el dato

Formas planas, líneas finas y un solo protagonista. **Pensados para tableros y presentaciones**: al pasar el cursor sobre un dato se ve su valor.

(Comparar)

Columnas de puntos

Cada punto es una unidad. El protagonista en Azul Cielo; el resto en gris.

> Recurso visual: Gráfico SVG en línea · «Columnas de puntos: agosto es el mes con más horas recuperadas» · Textos: E / F / M / A / M / J / J / A / S / O / N / D · Al pasar el cursor: Ene: 24 horas recuperadas / Feb: 32 horas recuperadas / Mar: 28 horas recuperadas / Abr: 40 horas recuperadas / May: 36 horas recuperadas / Jun: 48 horas recuperadas / Jul: 32 horas recuperadas / Ago: 60 horas recuperadas / Set: 44 horas recuperadas / Oct: 36 horas recuperadas / Nov: 52 horas recuperadas / Dic: 40 horas recuperadas

(Comparar)

Tallos

Más livianos que una barra: un trazo fino rematado con una estrella. Para series largas.

> Recurso visual: Gráfico SVG en línea · «Líneas verticales: agosto es el mes con más solicitudes resueltas» · Textos: E / F / M / A / M / J / J / A / S / O / N / D · Al pasar el cursor: Ene: 12 solicitudes resueltas / Feb: 16 solicitudes resueltas / Mar: 14 solicitudes resueltas / Abr: 20 solicitudes resueltas / May: 18 solicitudes resueltas / Jun: 24 solicitudes resueltas / Jul: 16 solicitudes resueltas / Ago: 30 solicitudes resueltas / Set: 22 solicitudes resueltas / Oct: 18 solicitudes resueltas / Nov: 26 solicitudes resueltas / Dic: 20 solicitudes resueltas

(Avance)

Barra de avance

Un porcentaje contra el total. El último tramo se aclara para mostrar que sigue en curso.

> Recurso visual: Gráfico SVG en línea · «Barra segmentada al 38 %» · Textos: 0 / 25 / 50 / 75 / 100 · Al pasar el cursor: Avance: 38 % del diagnóstico / Pendiente: 62 %

(Proporción)

Medialuna

Hasta cuatro partes de un total, con relleno plano y contraste: un tono claro, uno profundo y Salmón para lo que falta.

> Recurso visual: Gráfico SVG en línea · «Medialuna: proporción de agentes en uso, en piloto y sin iniciar» · Textos: en uso diario / 48 % / en piloto / 36 % / sin iniciar / 16 % · Al pasar el cursor: 48 %: Agentes en uso diario / 36 %: Agentes en piloto / 16 %: Agentes sin iniciar

(Peso)

Círculos en secuencia

De mayor a menor, tangentes y apoyados en la misma línea. El área de cada círculo es proporcional a su valor.

> Recurso visual: Gráfico SVG en línea · «Círculos en secuencia: dónde se va el tiempo del equipo» · Textos: Tareas repetitivas · 48 % / Reuniones · 24 % / Correo · 16 % / Análisis · 12 % · Al pasar el cursor: Tareas repetitivas: 48 % del tiempo del equipo / Reuniones: 24 % del tiempo del equipo / Correo: 16 % del tiempo del equipo / Análisis: 12 % del tiempo del equipo

(Ranking)

Barras en orden

De mayor a menor, en colores planos y sin espacio entre barras. La cifra a la izquierda; el texto, dentro de la barra.

> Recurso visual: Gráfico SVG en línea · «Barras en orden: qué motiva a los equipos a adoptar la IA» · Textos: 55 % / Menos tareas repetitivas / 49 % / Aprender algo nuevo / 43 % / Más equilibrio de trabajo / 41 % / Reconocimiento de su equipo / 37 % / Mejor salario · Al pasar el cursor: Menos tareas repetitivas: 55 % de las personas / Aprender algo nuevo: 49 % de las personas / Más equilibrio de trabajo: 43 % de las personas / Reconocimiento de su equipo: 41 % de las personas / Mejor salario: 37 % de las personas

(Proporción)

Burbujas 80/20

Contornos en gris para el conjunto; Azul Cielo solo para lo que importa. Las cifras viven fuera de las burbujas.

> Recurso visual: Gráfico SVG en línea · «Burbujas: el 20 % de los procesos produce el 80 % del retrabajo» · Textos: 20 % / de los procesos, en Azul Cielo / 80 % / del retrabajo de la operación · Al pasar el cursor: Facturación: 31 % del retrabajo / Inventario: 12 % / Reportes: 9 %

(Varias cifras)

Cifras en bloques

Varias cifras de un mismo tema, cada una unida por una línea a un bloque de color plano.

> Recurso visual: Gráfico SVG en línea · «Cifras conectadas por líneas guía a bloques de color plano» · Textos: 63 % / usa IA en su trabajo / 70 % / usa agentes de IA / 2,2 h / ahorradas por semana / 39 % / teme perder su puesto · Al pasar el cursor: 63 %: usa IA en su trabajo / 70 %: usa agentes de IA / 2,2 h: ahorradas por semana / 39 %: teme perder su puesto

(Varias cifras)

Cifras en círculos

La misma idea con círculos superpuestos, para cifras que se cruzan entre sí.

> Recurso visual: Gráfico SVG en línea · «Cifras conectadas por líneas guía a círculos superpuestos» · Textos: 63 % / usa IA en su trabajo / 70 % / usa agentes de IA / 2,2 h / ahorradas por semana / 39 % / teme perder su puesto · Al pasar el cursor: 63 %: usa IA en su trabajo / 70 %: usa agentes de IA / 2,2 h: ahorradas por semana / 39 %: teme perder su puesto

(Comparar grupos)

Esferas en órbita

Cada grupo es un círculo plano, tangente al siguiente; el gris es la referencia. Las cifras se conectan con una línea guía.

> Recurso visual: Gráfico SVG en línea · «Esferas en órbita: cuántos equipos ya prueban la IA, por grupo» · Textos: 51 % / promedio de la región / ya prueba la IA / 65 % / de los equipos en / Costa Rica / 66 % / del sector / financiero · Al pasar el cursor: 51 %: promedio de la región ya prueba la IA / 65 %: de los equipos en Costa Rica / 66 %: del sector financiero

**(Interacción)**
En tableros, cada dato muestra su valor al pasar el cursor o al enfocarlo con el teclado; los demás se atenúan.

**(Movimiento)**
Al entrar en pantalla, el gráfico se dibuja una sola vez en menos de un segundo. Nunca en bucle.

#### Lo que no se usa

01
Pastel con muchas porciones
Más de cuatro ya no se comparan a simple vista.

02
Donut y radar
Distorsionan las proporciones.

03
3D, brillos y sombras
Nunca, en ningún formato.

04
Pictogramas
Íconos repetidos para contar cantidades.

## KYN-MRK-DAT-005 · 13.5 Estructura

Número: 13.5 · ID: `KYN-MRK-DAT-005` · Estado: vigente · Fuente: `/fundamentos/datos/graficos.html#estructura`

### Siete partes antes de publicar

**Un número sin contexto es un dato suelto.** Cada gráfico lleva estas siete partes; toque un número para ver la suya.

Las tareas repetitivas bajaron un 38 % en seis meses

(Horas por persona · Enero a junio 2026)

−38 %

> Recurso visual: Gráfico SVG en línea · «Horas de trabajo repetitivo por persona, de enero a junio, frente a la meta de 27 horas» · Textos: Ene / Feb / Mar / Abr / May / Jun / Meta: 27 h / Meta cumplida · Al pasar el cursor: Enero: 39 h / Febrero: 36 h / Marzo: 33 h / Abril: 30 h / Mayo: 28 h / Junio: 24 h · meta cumplida

Fuente: Diagnóstico Keyons, 15 entrevistas, 2026
62 personas: todo el equipo de operaciones

1. 01 · **Título que afirma** · La conclusión, no el tema.
2. 02 · **Unidad y período** · Qué se mide y cuándo.
3. 03 · **Cifra** · El dato protagonista, uno solo.
4. 04 · **Fuente** · Quién lo midió y con qué alcance.
5. 05 · **Nota humana** · Las personas detrás del número.
6. 06 · **Referencia** · Meta, promedio o año anterior.
7. 07 · **Firma** · El isotipo, en la esquina inferior derecha.

#### Gráficos en presentaciones

Cada diapositiva de datos debe tener una conclusión o una pregunta reconocible. El gráfico dispone del espacio suficiente para mantener la lectura de ejes, categorías y valores.

**(Retícula)**
Organiza titular, gráfico, dato destacado, fuente y contexto complementario.

**(Aplicaciones)**
Comparaciones entre alternativas, indicadores de negocio, evolución, resultados de investigación, diagnósticos y proyecciones claramente identificadas.

**(Expresión)**
Una diapositiva expresiva puede dar gran protagonismo a una cifra mediante TASA Orbiter, color y espacio. Las representaciones estadísticas conservan sus proporciones y escalas.
La identidad Keyons se construye con jerarquía, retícula, tipografía, color y recursos gráficos aplicados con criterio.

Keyons vende diagnóstico y rigor: sus gráficos también.
