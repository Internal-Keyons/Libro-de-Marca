# Correcciones de diagramaci√≥n ¬∑ 17 de noviembre de 2026 ¬∑ borrador

## Qu√© cambi√≥

| Problema | Correcci√≥n | Tipo |
| --- | --- | --- |
| Recuadros de foco despu√©s de un clic | Comprobado en la vista previa: tras hacer clic en un bot√≥n y pulsar una flecha para desplazar la p√°gina, el navegador por s√≠ solo marca el foco (`:focus-visible`). `js/libro.js` enciende el anillo solo con Tab, o con flechas, Inicio, Fin o AvP√°g dentro de un control que las usa: pesta√±as, men√∫, opciones, campos o carruseles. Con Tab, el anillo se sigue viendo | General |
| Recuadros en las capturas | Las capturas de escritorio y m√≥vil se hacen sin pantalla (Edge sin foco); las del panel se toman despu√©s de quitar el foco. Ninguna captura de esta entrega tiene bordes de foco | Herramienta |
| Ancho de lectura en el Sistema de Dise√±o | Una sola medida (`--measure`, 600 px) para el texto corrido de los dos libros: entradas, p√°rrafos, filas, requisitos y cuerpo de la serie y del detalle. Tablas, c√≥digo y componentes conservan su ancho | General |
| Etiquetas del men√∫ cortadas | Inventario abajo. Detector nuevo: `tools/menu-etiquetas.js` devuelve `[]` en Marca y en el Sistema de Dise√±o | General |
| Todo se ve√≠a como acorde√≥n de serie | Componente nuevo, el detalle plegable simple (`.det`): un r√≥tulo sin n√∫mero y un + peque√±o sin c√≠rculo. La serie (ADN-006) queda para varios √≠tems recorribles | General |
| ¬´la luz¬ª partida (Estela 5.5) | Solo en la entrada (`.ed__lead`), cada rengl√≥n se llena antes de cortar; el resto del texto conserva `pretty`. Se revis√≥ a 1440 y 375 px: ninguna entrada termina con una palabra sola | Local del componente |
| Respuesta de Estela | Comilla al inicio y al final, unidas a su palabra; sin cursiva; 20 px entre filas | Local |
| Salm√≥n Atardecer (COR-003) | ¬´Expresi√≥n seg√∫n el contexto¬ª | Texto de Keylin |

## Reglas publicadas

En la Gu√≠a de la Biblioteca, secci√≥n 05, el bloque nuevo **¬´Sistema de diagramaci√≥n¬ª** re√∫ne:
- los patrones editoriales;
- los marcadores de √≠tems;
- la diferencia entre serie y detalle;
- el ancho de lectura;
- las etiquetas del men√∫;
- el foco;
- los cortes de l√≠nea.

`reglas-visuales.md` cita la Gu√≠a y guarda solo los valores.

## Intro del √°rea Expresi√≥n

- **Qu√© se sirve:** la rama `biblioteca-p1-p4`, en el commit 7bd1e53 y los siguientes, desde el servidor local.
- **En esa versi√≥n:** `modos/index.html` no tiene la intro; la frase abre 16.4 Intensidad.
- **Si todav√≠a la ve:** est√° viendo una versi√≥n anterior. Puede ser la cach√© del navegador (Ctrl + F5) o un sitio publicado desde otra rama, como `main`, que no recibi√≥ estos cambios.

## Etiquetas cortas del men√∫

**Marca** (las dem√°s ya ten√≠an su etiqueta corta):

| T√≠tulo | Etiqueta |
| --- | --- |
| Criterios de comunicaci√≥n | Comunicaci√≥n |
| Formatos y aplicaciones | Formatos |

**Sistema de Dise√±o:**

| T√≠tulo | Etiqueta |
| --- | --- |
| Claridad antes que novedad | Claridad primero |
| Complejidad justificada | Complejidad |
| Comportamiento previsible | Previsibilidad |
| Contexto antes de actuar | Contexto previo |
| Reconocer antes que recordar | Reconocer |
| Dise√±ar para quienes utilizan el producto | Personas reales |
| Uso ocasional y frecuente | Frecuencia de uso |
| Decisiones justificadas | Decisiones |
| Prisma como metodolog√≠a | Prisma |
| Dise√±o basado en resultados | Resultados |
| Evidencia diferenciada | Evidencia |
| Organizaci√≥n comprensible | Organizaci√≥n |
| Nombres comprensibles | Nombres |
| Informaci√≥n progresiva | Detalle a pedido |
| Identificaci√≥n de controles | Controles |
| Adaptaci√≥n por dispositivo | Adaptaci√≥n |
| Acceso directo y rutas no disponibles | Acceso directo |
| Resultados pertinentes | Pertinencia |
| Resultados comprensibles | Resultados claros |
| Resultados autorizados | Permisos |
| Colores de interacci√≥n | Interacci√≥n |
| Indicadores de progreso | Progreso |
| Contraste y legibilidad | Contraste |
| Sin depender del color | M√°s que color |
| Preferencias del sistema | Preferencias |
| Diferentes capacidades | Capacidades |
| Aprobaciones y registro | Aprobaciones |
| Est√°ndares UX comunes | Est√°ndares UX |
| Est√©tica neutral premium | Est√©tica neutral |
| Identidades de clientes | Identidades |
| Transiciones funcionales | Transiciones |
| Movimiento atmosf√©rico | Atm√≥sfera |

El nombre completo sigue en la p√°gina y aparece al pasar el cursor sobre la etiqueta.

## Detalle plegable simple

- **D√≥nde se aplica:** en las seis p√°ginas del Sistema de Dise√±o, 01 a 06, para verificaci√≥n, entregable, notas t√©cnicas, excepciones y evidencia.
- **La serie desplegable** queda en Estela 5.3 (escenarios), ADN-006, Paleta base y Elementos gr√°ficos.

## Patrones por norma

Revisi√≥n uso por uso, sin conversiones autom√°ticas. Lo que se conserv√≥ y por qu√©:
- **Secuencias reales:** Prisma (cinco fases en orden) y Regreso sin p√©rdida (abrir, volver, retomar).
- **Ejemplos de correcci√≥n de ARQ-002 y ARQ-006:** comparan la forma a corregir con la correcta.
- **Capas de PEX-012:** numeradas, porque marcan el orden de atenci√≥n dentro de Anochecer. Una fila aclara que no son fases de Prisma.

| Norma | Patrones |
| --- | --- |
| KYN-SDI-ARQ-001 OrganizaciÛn comprensible | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-ARQ-002 Nombres comprensibles | Apertura normativa ∑ Filas normativas ∑ Correcto e incorrecto (comparaciÛn) ∑ Detalle plegable simple |
| KYN-SDI-ARQ-003 JerarquÌa identificable | Apertura normativa ∑ Tabla o comparaciÛn ∑ Detalle plegable simple |
| KYN-SDI-ARQ-004 InformaciÛn progresiva | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-ARQ-011 Alcance identificable | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-ARQ-012 Resultados pertinentes | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-ARQ-013 Resultados comprensibles | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-ARQ-014 Filtros visibles | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-ARQ-015 Sin resultados | Apertura normativa ∑ Tabla o comparaciÛn ∑ Detalle plegable simple |
| KYN-SDI-ARQ-016 Resultados autorizados | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-PEX-010 Decisiones justificadas | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-PEX-011 Prisma como metodologÌa | Apertura normativa ∑ Secuencia (especializada) ∑ Detalle plegable simple |
| KYN-SDI-PEX-012 DiseÒo por capas | Apertura normativa ∑ Filas normativas ∑ RetÌcula numerada (especializada) ∑ Detalle plegable simple |
| KYN-SDI-PEX-013 DiseÒo basado en resultados | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-PEX-014 Evidencia diferenciada | Apertura normativa ∑ Tabla o comparaciÛn ∑ Detalle plegable simple |
| KYN-SDI-PEX-015 EvaluaciÛn posterior | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-ARQ-005 UbicaciÛn actual | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-ARQ-006 Acciones previsibles | Apertura normativa ∑ Filas normativas ∑ Correcto e incorrecto (comparaciÛn) ∑ Detalle plegable simple |
| KYN-SDI-ARQ-007 NavegaciÛn visible | Apertura normativa ∑ Tabla o comparaciÛn ∑ Detalle plegable simple |
| KYN-SDI-ARQ-008 IdentificaciÛn de controles | Apertura normativa ∑ Filas normativas ∑ Tabla o comparaciÛn ∑ Detalle plegable simple |
| KYN-SDI-ARQ-009 AdaptaciÛn por dispositivo | Apertura normativa ∑ Tabla o comparaciÛn ∑ Detalle plegable simple |
| KYN-SDI-ARQ-010 Regreso sin pÈrdida | Apertura normativa ∑ Filas normativas ∑ Secuencia (especializada) ∑ Detalle plegable simple |
| KYN-SDI-ARQ-017 Acceso directo y rutas no disponibles | Apertura normativa ∑ Tabla o comparaciÛn ∑ Detalle plegable simple |
| KYN-SDI-PEX-007 DiseÒar para quienes utilizan el producto | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-PEX-008 Roles y permisos | Apertura normativa ∑ Tabla o comparaciÛn ∑ Detalle plegable simple |
| KYN-SDI-PEX-009 Uso ocasional y frecuente | Apertura normativa ∑ Tabla o comparaciÛn ∑ Detalle plegable simple |
| KYN-SDI-PEX-001 La tarea primero | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-PEX-002 Claridad antes que novedad | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-PEX-003 Complejidad justificada | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-PEX-004 Estado comprensible | Apertura normativa ∑ Tabla o comparaciÛn ∑ Detalle plegable simple |
| KYN-SDI-PEX-005 Comportamiento previsible | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-PEX-006 Contexto antes de actuar | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-PEX-016 PrevenciÛn de errores | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-PEX-017 Control de la persona | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |
| KYN-SDI-PEX-018 Reconocer antes que recordar | Apertura normativa ∑ Filas normativas ∑ Detalle plegable simple |

## Pruebas

| Prueba | Resultado |
| --- | --- |
| `verificar.py` | 0 errores |
| L√≠neas dobles (Estela, Corporativo, 01, 03, 05 y 06 del Sistema de Dise√±o) | 0. La Gu√≠a conserva 6 avisos que ya exist√≠an antes de este cambio |
| `menu-etiquetas.js` | `[]` en Marca y en el Sistema de Dise√±o |
| Foco: clic y luego flecha | Sin anillo. Con Tab, el anillo es visible |
| Respuesta de Estela | Sin cursiva, gris del texto, dos comillas, 20 px |
| Entradas en Estela a 1440 y 375 px | ¬´la luz¬ª entera; ninguna entrada termina con una palabra sola |
| Ancho de lectura en el 05 | Requisitos, filas, entrada y detalle de 600 px o menos |
| Pendiente | Prueba con lector de pantalla real (NVDA o VoiceOver) |

Capturas en `propuestas/capturas-2026-11-17d/`.
