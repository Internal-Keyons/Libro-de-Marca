# Conciliación de instrucciones · noviembre de 2026

Registro interno del encargo «Conciliación definitiva de instrucciones y consolidación de los dos libros».

- **Rama:** `consolidacion`, creada desde `sistema-diseno` (`e1d7590`). Esa rama ya incluye `main` (`6ef2db1`).
- **Para recuperar el estado anterior:** volver a cualquiera de esos dos commits.
- **Publicación:** nada se publica a producción hasta revisar el conjunto.

## A.1 · Estado al empezar

| Elemento | Estado |
|---|---|
| Libro de Marca | 29 capítulos y 133 normas registradas: 132 vigentes y 1 descontinuada (DIS-006). La verificación pasa sin errores. |
| Fundamentos | Capítulos 06 a 16. El 11, Criterios visuales, tiene 16 normas VIS. Movimiento (15) y Accesibilidad (16) aún no tienen página. |
| Rondas RV9 a RV11 | Aplicadas y aprobadas en `data/referencia-contenido.json`. |
| Sistema de Diseño | 12 módulos y 45 capítulos. El capítulo 01, Principios compartidos, tiene contenido (Borrador); los otros 44 están por definir. |
| Normas propias del Sistema de Diseño | Ninguna emitida. El prefijo `KYN-SDI` quedó propuesto en una ronda anterior y nunca se emitió. |
| Referencias a `antipatrones.html` | En `data/normas.json`, `js/secciones.js`, `js/nav-data.js` y en las páginas de los módulos 06, 11, 05 y 12 del Sistema de Diseño (se regeneran). |

### Decisiones abiertas al empezar

- El estado Error de COL-014 sigue en «Terracota suave».
- Los tratamientos atmosféricos de ILU-007 siguen marcados como «Por validar».
- Las etapas de los «Arcos de método» (ESP-007) no se han contrastado con la documentación de Prisma.
- Los valores de tracking −3 % y −5 % siguen pendientes de validación.

## A.2 · Cómo se resolvió cada discrepancia

1. **Tramas en los capítulos.** La instrucción F.1 resuelve la duda de ILU-007: la trama identifica al libro en su portada y en sus encabezados de nivel libro. Los portales de capítulo y los subencabezados dejan de llevarla.
2. **Normas VIS.** Se aplicaron tres casos:
   - **Trasladadas:** la sección completa pasa junto a su norma de destino. Conserva su ID y su texto aprobado.
   - **Integradas:** el destino ya incorpora su contenido por mandato de este encargo (VIS-001 en TYP-005, VIS-002 en 8.8 y VIS-007 en TYP-006). El ID queda en el registro con estado «integrada» y apunta a la norma que lo contiene.
   - **En integración:** el destino todavía no existe (VIS-011 en Movimiento, VIS-015 en el Sistema de Diseño). Quedan visibles y verificables en la página de trazabilidad, fuera de Fundamentos.
3. **Estado «En revisión»** en el Sistema de Diseño: el usuario lo retiró del libro, así que se usa Borrador.
4. **Textos que este encargo no trae.** Por ejemplo, los capítulos 02 y 03 del Sistema de Diseño. Se construye la estructura y se marca «Pendiente de redacción». No se inventan normas.
5. **Numeración visible.** Al salir el capítulo 11, del 12 al 29 bajan un número. Los ID no cambian. Los enlaces antiguos `#cap-NN` siguen funcionando porque `was` admite varios números anteriores.

## Mapa de normas VIS

| Norma | Destino | Tratamiento |
|---|---|---|
| VIS-001 | TYP-005 · Etiquetas de contexto | Integrada |
| VIS-002 | 8.8 · Tracking | Integrada |
| VIS-003 | 10.5 · Jerarquía y densidad | Trasladada (10.5.1) |
| VIS-004 | 10.6 · Patrones de composición | Trasladada (10.6.1) |
| VIS-005 | COL-009 · Gradientes | Trasladada (7.9.1) |
| VIS-006 | 9.2 · Sistema de radios y curvaturas | Trasladada (9.2.1) |
| VIS-007 | TYP-006 · criterio 04, Énfasis | Integrada |
| VIS-008 | ICO-003 · Uso | Trasladada (12.3.1) |
| VIS-009 | 10.5 · Jerarquía y densidad | Trasladada (10.5.2) |
| VIS-010 | 10.2 · Simetría y asimetría | Trasladada (10.2.1) |
| VIS-011 | Movimiento | En integración |
| VIS-012 | COL-005 · Combinaciones y contraste | Trasladada (7.5.1) |
| VIS-013 | VOZ-004 · Vocabulario que evitamos | Trasladada (4.4.1) |
| VIS-014 | 10.4 · Ritmo y equilibrio | Trasladada (10.4.1) |
| VIS-015 | Sistema de Diseño · Principios de experiencia | En integración |
| VIS-016 | 10.8 · Identidad visual aplicada | Trasladada (10.8.1) |

## Resultados por etapa

| Etapa | Commit | Resultado |
|---|---|---|
| A | (este documento) | Estado inicial y criterios de conciliación registrados |
| B | `d8eb92a` | Fundamentos consolidado; normas VIS trasladadas o integradas; capítulos 12 a 29 renumerados a 11 a 28; alias de rutas y búsqueda normativa |
| C | `fe00aae` | Capítulo 08 Tipografía según C.1 a C.12 |
| D | `abc8fcb` | Títulos ILU, flecha oficial en ILU-002 y precisiones de ILU-007 |
| E | `f749b7e` | Ancho, cierre del buscador, portada, carrusel continuo y desbordes en móvil |
| F | `8a92ee0` | Trama solo en portadas con atmósfera; propuesta `KYN-SDI`; capítulos 02 y 03 del Sistema de Diseño |
| G | (validación) | 0 errores en el registro; 0 enlaces rotos en 99 páginas; sin desbordes en 375, 768, 1440 y 1920 px |

## Índice anterior y nuevo

| Antes | Después |
|---|---|
| 06 Identidad | 06 Identidad |
| 07 Color | 07 Color |
| 08 Tipografía | 08 Tipografía |
| 09 Forma y espacio (7 normas) | 09 Geometría y espacio (ESP-001 a 003 y VIS-006) |
| 10 Composiciones (4 normas) | 10 Composición y diagramación (CMP, ESP-004 a 007, cinco VIS y 10.8 Ejemplos) |
| 11 Criterios visuales (16 normas) | Sale de Fundamentos. La trazabilidad queda en 28 Referencia |
| 12 Elementos gráficos | 11 Elementos gráficos |
| 13 Iconografía | 12 Iconografía |
| 14 Datos | 13 Datos y visualización |
| 15 Movimiento | 14 Movimiento |
| 16 Accesibilidad | 15 Accesibilidad visual |
| 17 a 29 (Modos, Aplicaciones, Recursos) | 16 a 28 |

Los enlaces antiguos `#cap-NN` y las rutas anteriores de las normas trasladadas redirigen a su ubicación vigente.

## Normas conservadas, integradas y pendientes

- **Conservadas en su lugar, con título de materia actualizado:** ESP-001 a 003, CMP-001 a 004, TYP-001 a 007 e ILU-001 a 009.
- **Trasladadas sin cambiar su ID:**
  - ESP-004 a 007;
  - VIS-003, 004, 005, 006, 008, 009, 010, 012, 013, 014 y 016.
- **Integradas:**
  - VIS-001 en TYP-005;
  - VIS-002 en Tracking (8.8);
  - VIS-007 en TYP-006.
- **En integración:**
  - VIS-011, porque Movimiento aún no tiene página;
  - VIS-015, porque su destino está en el Sistema de Diseño.

## Valores V1 pendientes de aprobación

- **Configuraciones tipográficas:**
  - institucional: 52, 36, 24, 20 y 16 px;
  - invertida: 20, 44, 18 y 16 px;
  - expresiva: 80, 44, 27, 20 y 16 px.
- **Lectura prolongada:** cuerpo de 16 a 18 px, interlineado de 1,5 a 1,65 y líneas de 55 a 75 caracteres.
- **Impresión:**
  - documentos: cuerpo de 11 a 12 pt;
  - presentaciones: cuerpo de 20 a 28 pt, verificando los tamaños cercanos a 18 pt;
  - brochures: escala según el formato y la distancia de lectura.
- **Tracking:** −3 % y −5 % en titulares de TASA Orbiter siguen en evaluación. La lectura en 0 % y las etiquetas en mayúsculas en +8 % quedan como vigentes.

## Listo para aprobación editorial

- **Textos del encargo, aplicados tal cual:**
  - Tipografía (C.4 a C.11);
  - ILU-002 e ILU-007;
  - los cuatro pasos de la portada.
- **Textos redactados al implementar, por revisar:**
  - leyendas de 10.8 Ejemplos de aplicación;
  - leyendas de las demostraciones de TYP-006;
  - leyenda «Alcance» de TYP-001;
  - textos breves de la página de trazabilidad;
  - descripciones de capítulo de 09, 10 y 11;
  - textos de los capítulos 02 y 03 del Sistema de Diseño (solo estructura y referencias).

## Observaciones

- **Azul Cielo sobre blanco** da 2,82:1. Basta para las muestras decorativas del catálogo de tramas, pero no para trazos que comuniquen información, que piden 3:1. Esto aplica a los gráficos de datos, cuyas condiciones de lectura define el capítulo Datos.
- **Tuteo en la portada:** el paso 04 dice «consulta», tal como lo trae el encargo; el resto del libro usa «usted».
- **Desbordes en móvil que ya existían:** se corrigieron tres, en Isotipo, Paleta base y Elementos gráficos.
