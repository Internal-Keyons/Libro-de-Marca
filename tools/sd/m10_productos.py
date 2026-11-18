"""Módulo 10 · Productos (SPR): 37 Product Default (Bloque 3). 34, 35, 36 y 38 van en el Bloque 4.
Requisitos: textos de Keylin (docs/sd/fuente-keylin-2026-11-17.md). El patrón de navegación predeterminado (SPR-004) y la
configuración permitida son propuesta de Claude y requieren aprobación: el 05 Navegación remite aquí esa decisión.
"""
from .base import N, req, stack, matriz, detalle, c, L, M, norma, seccion

MOD = 'sistemas-producto'
C37 = 'keyons-product-default'
def n37(nid, nombre, k, *a, **kw): return norma(nid, nombre, '10.04', MOD, C37, k, *a, **kw)


CAP37 = [
    n37('KYN-SDI-SPR-001', 'Experiencia predeterminada', 1, 'Product Default parte de los componentes canónicos',
        'Un producto Keyons <strong>empieza completo</strong>, no desde cero.', [
        req(N('Los productos que utilizan Keyons Product Default deben aplicar los componentes funcionales canónicos y el tema visual predeterminado aprobado.', 'debe')),
        stack([('Qué incluye', [f'Los tokens ({L("07")}), los componentes de {L("12")} y {L("13")}, los patrones de {L("16")} a {L("18")} y la navegación de SPR-004.']),
               ('Estado del tema', ['El tema visual predeterminado está pendiente de aprobación; mientras tanto se usan los tokens actuales.'])]),
        detalle([
            ('Verificación', [
                ('Inventario', 'Cada pantalla del producto usa componentes canónicos; las piezas propias tienen su justificación registrada (PEX-010).')])]),
    ], origen=['Experiencia predeterminada (base)'], responsabilidad='Los productos Default aplican los componentes canónicos y el tema aprobado.', corto='Predeterminada'),

    n37('KYN-SDI-SPR-002', 'Sobriedad operativa', 2, 'Lo frecuente se ve contenido y claro',
        'El uso diario pide <strong>calma y jerarquía</strong>.', [
        req(N('Las interfaces de uso frecuente deberían priorizar superficies contenidas, claridad y jerarquía antes que recursos expresivos.', 'deberia')),
        matriz('Intensidad según la pantalla', [('Superficie', ''), ('Recursos expresivos', '')], [
            ('Operación diaria', ['Blanco, grises y Azul Noche; color solo con función.', 'Ninguno, salvo el que tenga función.']),
            ('Bienvenida y estados vacíos', ['Contenida, con un acento.', f'Puntuales, según los momentos vivos de {M("KYN-MRK-UI-002")}.']),
            ('Recorridos de presentación', ['Más libre.', 'Fotografía o ilustración que acompaña.'])]),
        detalle([
            ('Verificación', [
                ('Retirar lo decorativo', 'Al quitar los recursos decorativos de una pantalla operativa, la tarea se entiende igual.')])]),
    ], origen=['Sobriedad operativa (base)', 'Estética neutral premium (descripción del capítulo)'],
       responsabilidad='Las interfaces frecuentes priorizan superficies contenidas, claridad y jerarquía.', corto='Sobriedad',
       cita='Libro de Marca, capítulo 18 Digital (UI-001 y UI-002), en borrador'),

    n37('KYN-SDI-SPR-003', 'Personalización controlada', 3, 'Lo que se personaliza no rompe lo que funciona',
        'Personalizar <strong>sin perder accesibilidad ni consistencia</strong>.', [
        req(N('Las variaciones permitidas deben conservar la accesibilidad, consistencia y comportamiento funcional del producto.', 'debe')),
        matriz('Qué se puede personalizar (propuesta)', [('Se puede', ''), ('Queda fijo', '')], [
            ('Identidad', ['Logotipo y nombre del cliente en la cabecera.', 'Comportamiento de los componentes.']),
            ('Color', ['El color de acento, si cumple el contraste (FUI-007).', 'Colores de estado y de error.']),
            ('Contenido', ['Textos de bienvenida y ayudas.', 'Mensajes de error y de sistema.']),
            ('Densidad', ['Modo cómodo o denso por defecto.', 'Escala espacial y tipográfica.'])]),
        detalle([
            ('Verificación', [
                ('Tema de prueba', 'Se aplica una personalización completa y se repiten las pruebas de contraste y de teclado.')])]),
    ], origen=['Personalización controlada (base)', 'Opciones de configuración (descripción del capítulo)', 'UIX-045'],
       responsabilidad='Las variaciones permitidas conservan accesibilidad, consistencia y comportamiento.', corto='Personalización',
       cita='38 White-label regula los productos sin firma Keyons'),

    n37('KYN-SDI-SPR-004', 'Navegación predeterminada', 4, 'Un patrón de navegación común para los productos SaaS',
        'Una estructura conocida <strong>en todos los productos</strong>.', [
        req(N('Los productos SaaS de Keyons deberían usar el patrón de navegación predeterminado, salvo que su estructura justifique otro.', 'deberia')),
        matriz('Patrón predeterminado (propuesta)', [('Escritorio', ''), ('Móvil', '')], [
            ('Navegación principal', ['Lateral, con grupos que se abren y se pueden contraer.', 'Panel que cubre la pantalla, abierto desde un botón con nombre.']),
            ('Cabecera', ['Nombre del producto, búsqueda global y cuenta.', 'Título de la pantalla, menú y búsqueda.']),
            ('Ubicación', ['Sección activa marcada y ruta desde el tercer nivel.', 'Título y ruta abreviada.'])]),
        detalle([
            ('Origen', [
                ('Por qué aquí', f'{L("05")} define las reglas generales sin imponer un patrón; esta norma fija el predeterminado. Requisito y patrón redactados por Claude; requieren aprobación.')]),
            ('Verificación', [
                ('Dos productos', 'Se comparan dos productos SaaS: misma estructura de navegación, con sus destinos propios.')])]),
    ], origen=['Patrón SaaS (decisión pendiente del capítulo 05; requisito redactado por Claude)'],
       responsabilidad='Los productos SaaS usan el patrón de navegación predeterminado o justifican otro.', corto='Navegación'),

    seccion('ejemplo', '37', 'Ejemplo de aplicación', 'Dos productos, una base',
            'Dos productos SaaS comparten <strong>componentes, navegación y comportamiento</strong>, y cada uno muestra sus propios destinos.', [
        stack([('Verificación del capítulo', ['Aplicar el sistema a diferentes productos y comprobar continuidad visual y funcional.'])]),
    ]),
]

CAPITULOS = [
    ('10', '10.04', C37, CAP37, None),
]
