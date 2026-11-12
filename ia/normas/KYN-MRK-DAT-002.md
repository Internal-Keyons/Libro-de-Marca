---
manual: "Libro de Marca Keyons"
version: "0.1"
fecha: "2026-11-12"
permisos: "por definir; se asignarán con la Biblioteca Keyons"
id: "KYN-MRK-DAT-002"
titulo: "Sistema cromático"
numero: "13.2"
estado: "vigente"
capitulo: "13 Datos y visualización"
area: "Fundamentos"
fuente: "/fundamentos/datos/graficos.html#paleta"
referencias: ["KYN-MRK-COL-014"]
citada_por: []
---

# KYN-MRK-DAT-002 · Sistema cromático

Número: 13.2 · Estado: vigente · Capítulo: 13 Datos y visualización · Fuente: `/fundamentos/datos/graficos.html#paleta`

##### Tres paletas, según el significado

Las paletas se organizan según el significado de los datos: **categórica, secuencial y divergente**. Estas tres familias responden a funciones estadísticas diferentes.

Las fuentes cromáticas proceden de la paleta corporativa y sus escalas, complementadas por colores funcionales autorizados cuando corresponda.

Esta organización amplía la clasificación histórica «paleta base, monocromática y suave»: la clasificación histórica describe familias de colores; la nueva describe para qué se utiliza cada familia.

###### Colores corporativos disponibles

| (Color) | Referencia | Función |
|---|---|---|
| Azul Noche | #10122A | Texto, estructura, fondos profundos y contrastes |
| Blanco Keyons | #F4F4F4 | Fondo, espacio negativo y superficies claras |
| Azul Cielo | #729BDD | Acento principal y color protagonista |
| Salmón Tierra | #CE635D | Contraste cálido y categorías destacadas |
| Salmón Atardecer | #E99D9E | Acento claro sobre Azul Noche |

###### Condiciones cromáticas

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

###### Paleta categórica

Para distinguir series sin orden entre sí. Parte de la paleta base corporativa.

###### Paleta secuencial

Para magnitudes ordenadas, del claro al profundo en pasos parejos. La de Azul Cielo es la de uso diario.

###### Paleta divergente

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

###### Aplicaciones

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

###### Colores semánticos

Los colores semánticos pertenecen a estados como éxito, advertencia, error, información y estado crítico.

Nota
La paleta semántica se utiliza para comunicar estados, mientras que las paletas estadísticas representan categorías, magnitudes y diferencias.

Nota
Para pérdidas, errores y resultados desfavorables se utiliza el color semántico correspondiente, acompañándolo de texto, símbolo o indicador explícito. La definición técnica de esos colores procede del catálogo semántico oficial del proyecto (KYN-MRK-COL-014).
