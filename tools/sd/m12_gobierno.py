"""Módulo 12 · Gobierno (GOB): 44 Validación (Bloque 3). 42, 43 y 45 van en el Bloque 4.
Requisitos: textos de Keylin (docs/sd/fuente-keylin-2026-11-17.md). «Evidencia registrada» no se emite aquí: es la misma obligación
que PEX-014 (03) y se cita. GOB-003 (protocolo previo al lanzamiento) recupera UIX-047 y UIX-050 con un requisito redactado por
Claude; requiere aprobación. Gobierno: responsabilidades, procedimiento, aprobación, evidencia y trazabilidad.
"""
from .base import N, req, stack, matriz, pasos, detalle, c, L, norma, seccion, R, validacion, dims

MOD = 'calidad-gobierno'
C44 = 'validacion-de-calidad'
def n44(nid, nombre, k, *a, **kw): return norma(nid, nombre, '12.03', MOD, C44, k, *a, **kw)


CAP44 = [
    n44('KYN-SDI-GOB-001', 'Tareas reales', 1, 'Tareas representativas en las evaluaciones',
        'Se aplica a toda evaluación de un producto: <strong>se prueba con lo que las personas hacen de verdad</strong>.', [
        req(N('Las evaluaciones deben utilizar tareas representativas de los perfiles que operarán el producto.', 'debe')),
        stack([('Tareas', [f'Las frecuentes y las críticas de cada perfil ({R("KYN-SDI-PEX-007", "Diseñar para quienes utilizan el producto")}), con datos realistas.']),
               ('Participantes', ['Personas del perfil, no el equipo del proyecto.']),
               ('Evidencia', [f'Los resultados distinguen observaciones, problemas, hipótesis y decisiones, según Evidencia diferenciada de {L("03")}.'])]),
        detalle([
            ('Entregable', [
                ('Plan de prueba', 'Perfiles, tareas, criterios de éxito y método.'),
                ('Informe', 'Tareas completadas, errores, dificultades y decisiones, con su evidencia.')])]),
    ], verif=[('Plan de prueba', 'Se revisan las tareas del plan de evaluación.', 'cada una corresponde a una tarea documentada de un perfil.')], ver='breve',
       origen=['Tareas reales (base)', 'Evidencia registrada (base; se cita PEX-014)', 'UIX-047'],
       responsabilidad='Las evaluaciones usan tareas representativas y registran su evidencia.', corto='Tareas reales'),

    n44('KYN-SDI-GOB-002', 'Problemas críticos', 2, 'Defectos críticos antes del lanzamiento',
        'Se aplica a los defectos que impiden completar una tarea esencial: <strong>se resuelven o bloquean el lanzamiento</strong>.', [
        req(N('Los defectos que impidan completar tareas esenciales de forma segura deben resolverse o contar con una decisión explícita de bloqueo antes del lanzamiento correspondiente.', 'debe')),
        matriz('Gravedad de un problema (propuesta)', [('Qué significa', ''), ('Qué se hace', '')], [
            ('Crítico', ['Impide completar una tarea esencial o la hace insegura.', 'Se resuelve o bloquea el lanzamiento, con decisión registrada.']),
            ('Grave', ['La tarea se completa con mucha dificultad o errores.', 'Se resuelve antes del lanzamiento o con fecha comprometida.']),
            ('Menor', ['Molestia que no impide la tarea.', 'Se planifica.'])]),
        detalle([
            ('Aprobación', [
                ('Quién decide', f'La decisión de bloqueo o excepción la toman los responsables definidos en {L("42")}.')])]),
    ], verif=[('Registro', 'Se revisa el registro de problemas de un lanzamiento.', 'cada problema crítico tiene su resolución o su decisión de bloqueo, con fecha y responsable.')], ver='breve',
       origen=['Problemas críticos (base)'], responsabilidad='Los defectos críticos se resuelven o bloquean el lanzamiento con decisión explícita.', corto='Problemas críticos'),

    n44('KYN-SDI-GOB-003', 'Protocolo previo al lanzamiento', 3, 'Protocolo previo al lanzamiento',
        'Se aplica antes de lanzar cada producto o versión: <strong>la misma revisión visual, funcional, de uso y de accesibilidad</strong>.', [
        req(N('Antes del lanzamiento, cada producto debería completar la verificación visual, funcional, de usabilidad y de accesibilidad, con su registro firmado.', 'deberia')),
        pasos([('Visual', 'Revisión contra el sistema: tokens, componentes y patrones.', 'Evidencia', 'Capturas de escritorio y móvil.'),
               ('Funcional', 'Estados, errores y recuperación de cada tarea.', 'Evidencia', 'Lista de casos probados.'),
               ('Usabilidad', 'Prueba con personas reales del perfil (desde UIX-047, que pedía al menos cinco).', 'Evidencia', 'Informe con tareas y problemas.'),
               ('Accesibilidad', f'WCAG 2.2 AA, automática y manual ({L("20")} a {L("22")}).', 'Evidencia', 'Resultados y excepciones.'),
               ('Aprobación', 'Registro firmado por los responsables.', 'Evidencia', 'Decisión de lanzamiento.')]),
        detalle([
            ('Origen', [
                ('UIX', 'Recupera UIX-047 y UIX-050 como referencia; el número mínimo de participantes y los firmantes requieren aprobación.')])]),
    ], verif=[('Expediente', 'Se revisa el expediente del lanzamiento.', 'tiene las cinco evidencias del protocolo, cada una con su resultado.')], ver='tecnica',
       origen=['Verificación visual, funcional, de usabilidad y de accesibilidad (descripción del capítulo; requisito redactado por Claude)', 'UIX-047', 'UIX-050'],
       responsabilidad='Cada lanzamiento completa la verificación visual, funcional, de usabilidad y de accesibilidad.', corto='Protocolo'),

    seccion('ejemplo', '44', 'Ejemplo de aplicación', 'Una prueba antes de lanzar',
            'Antes de lanzar, cinco administradores reales completan <strong>las tareas frecuentes del producto</strong> y sus problemas quedan registrados con su decisión.', [
        stack([('Verificación del capítulo', ['Registrar finalización de tareas, errores, dificultades y resultados de las correcciones.'])]),
    ]),
]

CAPITULOS = [
    ('12', '12.03', C44, CAP44, None),
]
