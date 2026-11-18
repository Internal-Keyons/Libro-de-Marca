"""Bloque 4 · Módulo 09 IA y Estela (IAE): 30 Principios de IA, 31 Conversación, 32 Agentes y 33 Confianza segura.
Requisitos: textos base de Keylin. Estela se cita del Libro de Marca (capítulo 05); las UIX 014 a 020 y 032 a 043 se usan como
referencia evaluada, sin convertir sus afirmaciones en obligaciones nuevas.
"""
from .base import N, req, stack, matriz, detalle, c, L, M, norma, seccion, R, validacion, dims

MOD = 'ia-estela'
def n30(nid, nombre, k, *a, **kw): return norma(nid, nombre, '09.01', MOD, 'principios-de-experiencia-con-ia', k, *a, **kw)
def n31(nid, nombre, k, *a, **kw): return norma(nid, nombre, '09.02', MOD, 'interfaz-conversacional-de-estela', k, *a, **kw)
def n32(nid, nombre, k, *a, **kw): return norma(nid, nombre, '09.03', MOD, 'agentes-y-ejecucion-de-acciones', k, *a, **kw)
def n33(nid, nombre, k, *a, **kw): return norma(nid, nombre, '09.04', MOD, 'seguridad-y-confianza-en-ia', k, *a, **kw)


CAP30 = [
    n30('KYN-SDI-IAE-001', 'Transparencia', 1, 'Contenido y acciones generados por IA',
        'Se aplica a todo resultado de capacidades de inteligencia artificial: <strong>la persona sabe de dónde viene</strong>.', [
        req(N('Las personas deben poder distinguir qué contenido o acción proviene de capacidades de inteligencia artificial cuando esa distinción afecta la comprensión o decisión.', 'debe')),
        matriz('Cómo se distingue', [('Señal', ''), ('Ejemplo', '')], [
            ('Contenido generado', ['Etiqueta «Propuesta de Estela» y el ícono de Estela.', 'Un resumen generado.']),
            ('Dato completado por el sistema', ['Marca de sugerencia hasta que la persona lo confirma.', 'Un campo autocompletado.']),
            ('Modo de trabajo', ['Indicador visible de copiloto (espera aprobación) o automático (desde UIX-017).', 'Un agente que concilia pagos.'])]),
    ], verif=[('Distinción', 'Se pide a la persona que señale qué contenido de la pantalla viene de la IA.', 'lo señala sin ayuda.')], ver='breve',
       origen=['Transparencia (base)', 'UIX-017'], responsabilidad='Se distingue lo que proviene de la IA cuando afecta la decisión.', corto='Transparencia'),

    n30('KYN-SDI-IAE-002', 'Incertidumbre', 2, 'Información generada no verificada',
        'Se aplica a la información que produce la IA: <strong>la confianza se comunica</strong>, no se supone.', [
        req(N('El sistema no debe presentar como verificada información generada que no ha sido comprobada.', 'no-debe')),
        matriz('Niveles de confianza (desde UIX-016, propuesta)', [('Etiqueta', ''), ('Qué hace la persona', '')], [
            ('Verificado', ['Dato comprobado contra una fuente.', 'Lo usa.']),
            ('Revisar', ['Resultado probable.', 'Lo revisa antes de usarlo.']),
            ('Requiere validación', ['Resultado incierto.', 'Lo valida una persona.'])]),
        detalle([
            ('Notas', [
                ('Señal', f'Etiqueta, color e ícono, sin porcentajes crudos por defecto.')])]),
    ], rel=['KYN-SDI-FUI-005'], verif=[('Resultados', 'Se prueban resultados correctos, inciertos e incompletos.', 'cada uno muestra su nivel de confianza.')], ver='breve',
       origen=['Incertidumbre (base)', 'UIX-016', 'UIX-018'], responsabilidad='La información generada sin comprobar no aparece como verificada.', corto='Incertidumbre'),

    n30('KYN-SDI-IAE-003', 'Control humano', 3, 'Supervisión según el riesgo',
        'Se aplica a las decisiones automatizadas: <strong>la supervisión crece con el riesgo</strong>.', [
        req(N('Las decisiones automatizadas deben incorporar el nivel de supervisión y autorización correspondiente a su riesgo.', 'debe')),
        matriz('Supervisión según el riesgo (desde UIX-014, propuesta)', [('Supervisión', ''), ('Ejemplo', '')], [
            ('Bajo y reversible', ['Automático, con registro y deshacer.', 'Ordenar una bandeja.']),
            ('Medio', ['Propuesta que la persona confirma.', 'Clasificar un pago.']),
            ('Alto o irreversible', [f'Aprobación explícita con contexto.', 'Emitir una devolución.'])]),
    ], rel=['KYN-SDI-PAT-011'], verif=[('Acciones de riesgo', 'Se pide a la IA una acción de riesgo alto.', 'la acción espera la aprobación de una persona antes de ejecutarse.')], ver='tecnica',
       origen=['Control humano (base)', 'UIX-014', 'UIX-015'], responsabilidad='Las decisiones automatizadas tienen la supervisión que corresponde a su riesgo.', corto='Control humano'),
]

CAP31 = [
    n31('KYN-SDI-IAE-004', 'Contexto útil', 1, 'Contexto de la conversación',
        'Se aplica a las conversaciones con Estela: <strong>conserva lo necesario</strong> dentro de los permisos.', [
        req(N('La conversación debe conservar el contexto necesario dentro de los límites de permisos y privacidad aplicables.', 'debe')),
        matriz('Memoria de la conversación (desde UIX-034 y UIX-035, propuesta)', [('Qué recuerda', ''), ('Control de la persona', '')], [
            ('Sesión', ['Lo dicho en la conversación actual.', 'Se borra al cerrarla.']),
            ('Persistente', ['Preferencias que la persona aceptó guardar.', 'Ver y olvidar en cualquier momento.'])]),
    ], verif=[('Cambio de tema', 'Se mantiene una conversación larga que cambia de dirección.', 'Estela conserva lo pertinente y nunca mezcla datos de otras personas.')], ver='grupo',
       origen=['Contexto útil (base)', 'UIX-034', 'UIX-035'], responsabilidad='La conversación conserva el contexto necesario dentro de permisos y privacidad.', corto='Contexto'),

    n31('KYN-SDI-IAE-005', 'Preguntas pertinentes', 2, 'Preguntas de Estela',
        'Se aplica cuando a Estela le falta información: <strong>pregunta solo lo necesario para avanzar</strong>.', [
        req(N('Estela debería solicitar únicamente la información adicional necesaria para avanzar con precisión.', 'deberia')),
        stack([('Personalidad', [f'Curiosa: comprende antes de responder.']),
               ('Una a la vez', ['Las preguntas se hacen de a una, con opciones cuando ayudan.'])]),
    ], rel=['KYN-MRK-EST-002'], verif=[('Solicitudes ambiguas', 'Se hace a Estela una solicitud ambigua.', 'responde con una pregunta que resuelve la ambigüedad.')], ver='grupo',
       origen=['Preguntas pertinentes (base)'], responsabilidad='Estela solo pide la información necesaria para avanzar.', corto='Preguntas'),

    n31('KYN-SDI-IAE-006', 'Respuesta accionable', 3, 'Información, recomendación y acción en las respuestas',
        'Se aplica a cada respuesta de Estela: <strong>se distingue lo que informa, lo que recomienda y lo que hace</strong>.', [
        req(N('Las respuestas deben distinguir información, recomendaciones y acciones que el sistema realmente puede ejecutar.', 'debe')),
        stack([('Acciones', ['Las que Estela puede ejecutar aparecen como botones; las demás, como pasos para la persona.']),
               ('Límites', [f'Cuando no sabe o no puede, lo dice y ofrece una alternativa.'])]),
    ], rel=['KYN-MRK-EST-003'], verif=[('Respuestas', 'Se revisa una muestra de respuestas.', 'cada una separa lo informativo de lo que se puede ejecutar.')], ver='grupo',
       origen=['Respuesta accionable (base)', 'UIX-042', 'UIX-043'], responsabilidad='Las respuestas distinguen información, recomendaciones y acciones ejecutables.', corto='Respuesta'),
    validacion('09.02', 'interfaz-conversacional-de-estela', 'El capítulo se comprueba con <strong>conversaciones reales y largas</strong>, que cambian de tema e incluyen solicitudes ambiguas.'),
]

CAP32 = [
    n32('KYN-SDI-IAE-007', 'Responsabilidad identificable', 1, 'Acciones visibles de los agentes',
        'Se aplica a lo que un agente ejecuta en el producto: <strong>se ve qué hace y con qué resultado</strong>.', [
        req(N('Las acciones visibles ejecutadas por agentes deben permitir comprender qué se está haciendo y cuál fue su resultado.', 'debe')),
        stack([('Estado', [f'En curso, terminado, fallido o en espera de aprobación.']),
               ('Registro', [f'Cada acción queda en el historial con su resultado.'])]),
    ], rel=['KYN-SDI-PAT-012', 'KYN-SDI-PEX-004'], verif=[('Historial', 'Se revisa el historial de un agente.', 'la persona dice qué hizo el agente, cuándo y con qué resultado, sin ayuda.')], ver='breve',
       origen=['Responsabilidad identificable (base)'], responsabilidad='Las acciones de los agentes son comprensibles y registradas.', corto='Responsabilidad'),

    n32('KYN-SDI-IAE-008', 'Límites de actuación', 2, 'Permisos de los agentes',
        'Se aplica a todo agente: <strong>los permisos valen también para él</strong>.', [
        req(N('Los agentes no deben ejecutar acciones fuera de sus permisos o autorizaciones.', 'no-debe')),
        stack([('Permisos', [f'Los del rol que lo autorizó, nunca más amplios.']),
               ('Aprobación', [f'Las acciones de riesgo esperan aprobación.'])]),
    ], rel=['KYN-SDI-IAE-003', 'KYN-SDI-PEX-008'], verif=[('Intento', 'Se pide al agente una acción fuera de sus permisos.', 'la rechaza y explica por qué.')], ver='tecnica',
       origen=['Límites de actuación (base)'], responsabilidad='Los agentes actúan solo dentro de sus permisos.', corto='Límites'),

    n32('KYN-SDI-IAE-009', 'Identidad pública consistente', 3, 'Estela como identidad pública',
        'Define cómo se presentan las capacidades coordinadas de IA: <strong>una sola identidad, Estela</strong>, sin exponer la arquitectura.', [
        req(N('La experiencia puede presentar a Estela como identidad pública de capacidades coordinadas, sin exponer innecesariamente su arquitectura interna.', 'puede')),
        stack([('Identidad', [f'Su nombre y su {M("KYN-MRK-EST-005", "expresión visual")} son los del Libro de Marca.'])]),
    ], verif=[('Consistencia', 'Se compara la presentación de Estela en dos productos.', 'se presenta y se comporta igual en ambos.')], ver='breve',
       origen=['Identidad pública consistente (base)'], responsabilidad='Estela es la identidad pública de las capacidades coordinadas.', corto='Identidad'),
]

CAP33 = [
    n33('KYN-SDI-IAE-010', 'Confianza calibrada', 1, 'Indicadores de confianza calibrados',
        'Se aplica a todo indicador de confianza de la IA: <strong>cada nivel tiene su evidencia</strong>.', [
        req(N('Los indicadores de confianza deben corresponder al significado y evidencia definidos para cada estado.', 'debe')),
        stack([('Definición', [f'Cada nivel tiene su criterio técnico documentado.'])]),
    ], rel=['KYN-SDI-IAE-002'], verif=[('Muestra', 'Se revisa una muestra de resultados con su nivel de confianza.', 'el nivel mostrado coincide con su criterio.')], ver='breve',
       origen=['Confianza calibrada (base)'], responsabilidad='Los indicadores de confianza corresponden a su evidencia.', corto='Confianza'),

    n33('KYN-SDI-IAE-011', 'Verificación humana', 2, 'Información para aprobar',
        'Se aplica cuando una decisión de la IA requiere aprobación: <strong>la persona tiene a la vista lo necesario para evaluarla</strong>.', [
        req(N('Cuando una decisión requiera aprobación, el sistema debe presentar información suficiente para evaluarla antes de continuar.', 'debe')),
        stack([('Panel de explicación (desde UIX-020)', ['Resumen en lenguaje claro, datos usados y fuentes, a pedido.'])]),
    ], verif=[('Aprobación', 'Se pide a la persona que apruebe o rechace una propuesta y explique por qué.', 'lo explica con la información mostrada.')], ver='breve',
       origen=['Verificación humana (base)', 'UIX-019', 'UIX-020'], responsabilidad='Las aprobaciones muestran la información para evaluar.', corto='Verificación'),

    n33('KYN-SDI-IAE-012', 'Privacidad', 3, 'Privacidad entre personas en la IA',
        'Se aplica a respuestas, sugerencias y fuentes de la IA: <strong>el contexto de cada persona es solo suyo</strong>.', [
        req(N('Las interfaces de IA no deben revelar contenido o contexto de otros usuarios sin autorización.', 'no-debe')),
        stack([('Fuentes', ['Las fuentes consultadas se muestran según la sensibilidad del sector (desde UIX-032).']),
               ('Modelos externos', ['El cliente puede restringir qué datos pasan por modelos externos (desde UIX-036).'])]),
    ], verif=[('Perfiles cruzados', 'Se usan dos perfiles distintos con las mismas consultas.', 'ninguno recibe datos del otro en respuestas, sugerencias ni fuentes.')], ver='tecnica',
       origen=['Privacidad (base)', 'UIX-032', 'UIX-033', 'UIX-036'], responsabilidad='La IA no revela contenido o contexto de otras personas.', corto='Privacidad'),
]

CAPITULOS = [
    ('09', '09.01', 'principios-de-experiencia-con-ia', CAP30, None),
    ('09', '09.02', 'interfaz-conversacional-de-estela', CAP31, None),
    ('09', '09.03', 'agentes-y-ejecucion-de-acciones', CAP32, None),
    ('09', '09.04', 'seguridad-y-confianza-en-ia', CAP33, None),
]
