"""Sistema de Diseño · capítulos redactados con normas propias (KYN-SDI).

Uso:  python tools/sd_capitulos.py
Después: python tools/niveles.py --aplicar  ·  python tools/sistema_diseno.py  ·  python tools/biblioteca.py

Escribe:
- data/sd-capitulos/<capítulo>.html: las secciones del capítulo, que tools/sistema_diseno.py pega en su página;
- data/sistema-diseno.json: los subcapítulos del capítulo pasan a ser sus normas (nombre corto, ID y estado);
- propuestas/matriz-normativa-sd-01-06.md: la matriz normativa, generada desde data/sd-normas.json.

Fuente de los códigos: data/sd-normas.json (borrador = emitido con página; reservado = número apartado, sin página).
Criterios (Keylin, 2026-11-17, y Guía 05 «Implementación editorial de capítulos»):
- Cada norma abre como el resto de la Biblioteca: rótulo (ID y nombre corto), titular, una entrada y sus requisitos en filas
  con nivel (.sdn). Después, solo lo que su contenido necesita: decisiones por elemento (.ed__stack), comparación (.matrix),
  secuencia (.steps), correcto e incorrecto (.redline), detalle a pedido (.caso) y verificación ejecutable (.chk).
- Los requisitos son los textos de Keylin; decisiones, comportamientos, excepciones, verificaciones, titulares y entradas
  son propuesta de Claude en borrador.
- Los niveles los lleva solo el requisito: N(texto, nivel) de tools/normativa.py.
- Las medidas y la apariencia quedan en sus capítulos (07–15, 20–22, 37); aquí se citan.
Primer capítulo: 05 Navegación (referencia de calidad, a revisión antes de seguir con 01–04 y 06).
"""
import html
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normativa import N, registrar   # noqa: E402

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = json.load(io.open(os.path.join(ROOT, 'data', 'sd-normas.json'), encoding='utf-8'))
NORMAS = {n['id']: n for n in REG['normas']}
esc = lambda t: html.escape(t, quote=False)
I = '        '


def P(*ps, cls=''):
    c = f' class="{cls}"' if cls else ''
    return ''.join(f'<p{c}>{p}</p>' for p in ps)


def sub(t): return f'{I}<h3 class="ed__sub">{esc(t)}</h3>'
def prosa(*ps): return f'{I}<div class="prosa">{P(*ps)}</div>'
def req(*ps):
    """Requisitos de la norma en filas, cada uno con su nivel (modelo del capítulo 01)"""
    return f'{I}<div class="sdn">' + ''.join(f'<div class="sdn__r"><p class="sdn__t">{p}</p></div>' for p in ps) + '</div>'
def stack(filas): return f'{I}<div class="ed__stack">' + ''.join(f'<div><span class="paren">({esc(k)})</span>{P(*ps)}</div>' for k, ps in filas) + '</div>'
def matriz(etq, cols, filas):
    head = ('<div class="matrix__row matrix__head" role="row"><span class="matrix__k" role="columnheader"></span>'
            + ''.join(f'<span class="matrix__lvl" role="columnheader">{esc(t)}<small>{esc(s)}</small></span>' for t, s in cols) + '</div>')
    rows = ''.join(f'<div class="matrix__row" role="row"><span class="matrix__k" role="rowheader">{esc(k)}</span>'
                   + ''.join(f'<span class="matrix__v" role="cell">{v}</span>' for v in vs) + '</div>' for k, vs in filas)
    return f'{I}<div class="matrix" role="table" aria-label="{esc(etq)}">{head}{rows}</div>'
def pasos(items):
    """Secuencia (.steps): (título, descripción, rótulo, criterio)"""
    return (f'{I}<div class="steps">' + ''.join(
        f'<div class="step"><span class="step__n">{k:02d}</span><div><p class="step__t">{esc(t)}</p><p class="step__d">{d}</p></div>'
        f'<div class="step__c"><span class="paren">({esc(r)})</span><p>{c}</p></div></div>' for k, (t, d, r, c) in enumerate(items, 1)) + '</div>')
def contraste(items):
    """Correcto e incorrecto (.redline): lo que se evita, tachado, y la forma correcta"""
    return f'{I}<div class="redline">' + ''.join(f'<div class="redline__i"><p class="redline__no">{n}</p><p class="redline__yes">{s}</p></div>' for n, s in items) + '</div>'
FLECHA = '<svg class="caso__x" viewBox="0 0 16 16" aria-hidden="true"><path d="m3.5 6 4.5 4.5L12.5 6" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>'
def detalle(grupo, items):
    """Detalle a pedido (acordeón .caso): (título, [(rótulo, texto)])"""
    out = ''.join(f'<details class="caso" name="{grupo}"><summary><span class="caso__n">{k:02d}</span><span class="caso__t">{esc(t)}</span>{FLECHA}</summary>'
                  f'<div class="caso__c"><dl>' + ''.join(f'<div><dt class="caso__k">{esc(r)}</dt><dd>{x}</dd></div>' for r, x in filas) + '</dl></div></details>'
                  for k, (t, filas) in enumerate(items, 1))
    return f'{I}<div class="casos">{out}</div>'
def verificar(items):
    """Verificación ejecutable (.chk, lista de comprobación del libro): (prueba, condición y resultado esperado)"""
    lis = ''.join(f'<li><label><input type="checkbox"><span class="chk__box" aria-hidden="true"></span><span><b>{esc(t)}</b>{d}</span></label></li>' for t, d in items)
    return (f'{I}<div class="ed__wide"><div class="chk" data-chk><div class="chk__head"><p class="chk__n"><b>0</b> de {len(items)}</p><div class="chk__bar"><i></i></div>'
            f'<button class="chk__reset" type="button">Reiniciar</button></div><ul class="chk__l">{lis}</ul></div></div>')
def c(t): return f'<code>{esc(t)}</code>'
def cap(href, t): return f'<a class="xref" href="{href}">{esc(t)}</a>'


def norma(nid, ancla, titular, entrada, partes):
    n = NORMAS[nid]
    assert n['estado'] != 'reservado', f'{nid} está reservado: no se publica'
    assert n['ruta'].endswith('#' + ancla), (nid, n['ruta'])
    return (f'\n    <!-- {nid} · {n["nombre"]} -->\n    <section class="ed" id="{ancla}">\n'
            f'      <div class="ed__label sdn-label"><span class="ed__code" data-copy="{nid}" data-copy-msg="ID copiado · {nid}" title="Copiar el ID de esta norma">{nid}</span><span>{esc(n["nombre"])}</span></div>\n'
            f'      <div>\n{I}<h2 class="ed__title">{esc(titular)}</h2>\n{I}<p class="ed__lead">{entrada}</p>\n' + '\n'.join(partes) + '\n      </div>\n    </section>\n')


def seccion(sid, num, corto, titular, entrada, partes):
    return (f'\n    <!-- {corto} -->\n    <section class="ed" id="{sid}">\n      <div class="ed__label"><span>{num}</span><span>{esc(corto)}</span></div>\n'
            f'      <div>\n{I}<h2 class="ed__title">{esc(titular)}</h2>\n{I}<p class="ed__lead">{entrada}</p>\n' + '\n'.join(partes) + '\n      </div>\n    </section>\n')


# ═════════════ Capítulo 05 · Navegación ═════════════
# Reglas generales para navegación lateral, superior, pestañas, rutas jerárquicas y navegación móvil.
# El capítulo no impone un patrón: el predeterminado de los productos SaaS lo define 37 Product Default.
P37 = cap('../sistemas-producto/keyons-product-default.html', '37 Product Default')
P22 = cap('../accesibilidad-adaptacion/adaptacion-de-la-experiencia.html', '22 Adaptación')
P21 = cap('../accesibilidad-adaptacion/accesibilidad-operativa.html', '21 Operación')
P08 = cap('../fundamentos-interfaz/color-funcional.html', '08 Color funcional')
P14 = cap('../componentes-estados/componentes-de-estructura.html', '14 Estructura')
P04 = cap('arquitectura-de-informacion.html', '04 Información')

C05 = [
    norma('KYN-SDI-ARQ-005', 's-02-02-01', 'La persona sabe dónde está y cómo seguir',
          'Ubicarse permite decidir el siguiente paso: <strong>la sección activa y su grupo orientan</strong> sin que la persona tenga que recordar el camino.', [
        req(N('La navegación debe permitir reconocer en qué sección se encuentra la persona y cómo acceder a las demás áreas autorizadas.', 'debe'),
            N('La sección activa debe distinguirse visualmente y mantener una relación comprensible con sus secciones superiores cuando existan.', 'debe')),
        stack([('Sección activa', [f'Se marca con dos señales a la vez: una de forma, como una barra, un fondo o un subrayado, y otra de color o de peso. Su apariencia la definen {P08} y {P14}.']),
               ('Página actual', [f'El enlace de la página abierta lleva {c("aria-current=" + chr(34) + "page" + chr(34))}, una vez en cada navegación donde aparece.']),
               ('Grupo superior', ['El grupo que contiene la página queda abierto o señalado. Desde el tercer nivel, una ruta jerárquica muestra el camino completo.']),
               ('Al navegar', ['El indicador, el título visible, el título de la pestaña del navegador y la ruta cambian a la vez. Si la página cambia sin recargarse, el foco pasa al título principal.'])]),
        sub('Según el tipo de navegación'),
        detalle('ubicacion-tipos', [
            ('Navegación lateral o superior', [('Sección activa', 'El destino de la página abierta lleva el indicador.'),
                                               ('Grupo', 'En la lateral, el grupo de la página queda abierto; en la superior, su grupo queda señalado en la barra.')]),
            ('Pestañas', [('Entre páginas', f'Cada pestaña es un enlace; la activa lleva {c("aria-current=" + chr(34) + "page" + chr(34))}.'),
                          ('Dentro de una página', f'Cambian un panel sin cambiar de página: usan el patrón de pestañas, con {c("aria-selected")}.')]),
            ('Ruta jerárquica', [('Estructura', f'Un {c("<nav>")} con nombre accesible («Ruta») y una lista ordenada, del nivel más general al actual.'),
                                 ('Último nivel', f'Nombra la página actual y lleva {c("aria-current=" + chr(34) + "page" + chr(34))}.')]),
            ('Navegación móvil', [('Menú cerrado', 'El título de la pantalla nombra la sección, y la ruta se abrevia al nivel superior inmediato.'),
                                  ('Menú abierto', 'El destino activo se ve marcado y su grupo, abierto.')]),
            ('Pantallas sin navegación general', [('Cuáles', 'Los flujos de un paso, los diálogos y el inicio de sesión.'),
                                                  ('Qué conservan', 'Su título visible y una salida.')])]),
        sub('Verificación'),
        verificar([('Prueba con personas', 'Desde una pantalla de segundo o tercer nivel, abierta con un enlace directo, la persona nombra la sección y el grupo y llega a otra sección principal sin ayuda.'),
                   ('Tiempo de ubicación', 'Se registra cuánto tarda en ubicarse. Cinco segundos es la hipótesis inicial de prueba, no un requisito.'),
                   ('Escala de grises', 'Con la pantalla en escala de grises, la sección activa sigue distinguiéndose.'),
                   ('Lector de pantalla', 'Al recorrer la navegación, el enlace activo se anuncia como «página actual».'),
                   ('Código', f'Cada navegación tiene un solo enlace con {c("aria-current")}, y corresponde a la página abierta.'),
                   ('Cambio de página', 'Al ir a otro destino, el indicador, el título y la ruta cambian a la vez.')]),
    ]),
    norma('KYN-SDI-ARQ-006', 's-02-02-02', 'Cada destino conserva su nombre y su lugar',
          'La navegación se aprende una vez: <strong>un nombre y un destino estables</strong> convierten cada recorrido en un hábito.', [
        req(N('Los elementos navegables deben mantener nombres, destinos y comportamientos consistentes en todo el producto.', 'debe'),
            N('Las funciones principales deberían conservar una ubicación y denominación consistentes entre las pantallas equivalentes.', 'deberia')),
        stack([('Nombre', [f'Un destino se llama igual en el menú, la ruta, el título de la página y los enlaces que llevan a él. Su redacción sigue Nombres comprensibles, en {P04}.']),
               ('Enlace o botón', ['Un enlace lleva a otro lugar; un botón ejecuta una acción en el mismo lugar. Cada control conserva su tipo en todas las pantallas.']),
               ('Otra pestaña', ['Los enlaces abren en la misma pestaña. El que abre otra pestaña o sale del producto lo anuncia con el ícono «abrir externo» y un texto accesible.'])]),
        sub('Ejemplos'),
        contraste([('Menú «Solicitudes» y título «Gestión de trámites»', 'Menú, ruta y título dicen «Solicitudes».'),
                   ('«Exportar» descarga en un listado y abre un diálogo en otro', '«Exportar» abre el mismo diálogo en todos los listados.'),
                   ('Un texto subrayado que guarda cambios', 'Guardar es un botón; el texto subrayado solo lleva a otro lugar.'),
                   ('«Configuración» cambia de lugar entre módulos', '«Configuración» ocupa la misma posición en todos los módulos.')]),
        sub('Verificación'),
        prosa('Se arma un inventario de destinos con su nombre en el menú, la ruta y el título. Después se recorre la misma tarea desde dos áreas autorizadas.',
              'Resultado esperado: ninguna diferencia de nombre, destino o comportamiento.'),
    ]),
    norma('KYN-SDI-ARQ-007', 's-02-02-03', 'Toda función necesaria tiene una señal a la vista',
          'Una función se usa cuando se encuentra: <strong>cada función necesaria tiene una señal visible</strong> para el puntero, el teclado y el tacto.', [
        req(N('Las funciones necesarias no deben depender exclusivamente de interacciones ocultas o de pasar el cursor sobre una zona sin señal.', 'no-debe')),
        matriz('Interacciones ocultas y su alternativa visible', [('Como única vía', 'Lo que se evita'), ('Alternativa visible', 'Lo que se diseña')], [
            ('Pasar el cursor', ['Un menú o una acción que solo aparece al pasar el cursor.', 'Aparece también con el foco del teclado y con un toque. Escape lo cierra sin mover el puntero.']),
            ('Gestos', ['Deslizar o mantener presionado para editar o eliminar.', 'Un botón o un menú de opciones visible en el elemento.']),
            ('Atajos de teclado', ['Una función que solo tiene atajo.', 'Un control visible; el atajo se muestra como ayuda.']),
            ('Destinos que no caben', ['Destinos fuera de la pantalla, sin aviso.', 'Un control «Más» que indica que hay más destinos.']),
            ('Íconos solos', ['Un ícono suelto como única señal de un destino principal.', 'Nombre visible en los destinos principales; en los demás, nombre accesible y etiqueta con el foco y el cursor.'])]),
        sub('Verificación'),
        prosa('Se completan las tareas principales tres veces: solo con teclado, solo con toques y solo con puntero.',
              'Resultado esperado: todas se completan, y ninguna función necesaria aparece solo con el cursor o con un gesto.'),
    ]),
    norma('KYN-SDI-ARQ-008', 's-02-02-04', 'Cada control dice qué hace y en qué estado está',
          'Quien navega con teclado o lector de pantalla recibe la misma información que quien mira: <strong>función, estado y ubicación de cada control</strong>.', [
        req(N('Los controles de navegación deben comunicar su función y estado mediante señales comprensibles y accesibles.', 'debe')),
        stack([('Semántica primero', [f'Se usan los elementos que ya resuelven la función: {c("<nav>")}, {c("<a href>")}, {c("<button>")} y listas. Con más de un {c("<nav>")}, cada uno lleva un nombre: «Principal», «Ruta», «Secciones». ARIA completa lo que el HTML no expresa.']),
               ('Enlace o botón', [f'{c("<a href>")} para ir a otro lugar y {c("<button>")} para abrir, cerrar o expandir. Un {c("div")} o un {c("span")} con clic quedan fuera, porque no anuncian su función ni reciben el foco.']),
               ('Expansión', [f'El botón de un grupo o un menú lleva {c("aria-expanded")} con su estado y {c("aria-controls")} con el panel que abre. La flecha acompaña al estado, que se anuncia sin ella.']),
               ('Nombre', [f'Cada control nombra su destino o su acción. Un botón con solo ícono lleva ese nombre en {c("aria-label")}.']),
               ('Foco', [f'El foco se ve completo en cada control, sin quedar debajo de una cabecera fija. Su apariencia la define {P21}.'])]),
        sub('Teclado y foco según el tipo de menú'),
        detalle('foco-menus', [
            ('Grupo desplegable dentro de la navegación', [('Al abrir', 'Enter o Espacio en el botón lo abren. El foco queda en el botón y el siguiente Tab entra en sus destinos.'),
                                                          ('Al cerrar', 'Enter o Espacio de nuevo. El foco sigue en el botón.')]),
            ('Menú desplegable sobre el contenido', [('Al abrir', 'Enter o Espacio lo abren y el foco pasa al primer destino.'),
                                                     ('Al cerrar', 'Escape lo cierra y el foco vuelve al botón. También se cierra cuando el foco sale del menú o la persona toca fuera.')]),
            ('Panel que cubre la pantalla, habitual en móvil', [('Al abrir', f'El foco pasa al primer elemento del panel. El contenido de fondo queda inactivo ({c("inert")}) y Tab recorre solo el panel.'),
                                                                ('Al cerrar', 'Escape, el botón Cerrar o un toque fuera lo cierran. El foco vuelve al botón que lo abrió.')]),
            ('Navegación larga', [('Al cargar la página', 'El enlace «Ir al contenido» es lo primero que alcanza el teclado.'),
                                  ('Al activarlo', 'El foco pasa al inicio del contenido principal.')])]),
        sub('Verificación'),
        verificar([('Lector de pantalla', 'Cada navegación se anuncia con su nombre, y cada botón de grupo, como «expandido» o «contraído».'),
                   ('Teclado', 'Tab llega a cada control en el orden visual. Enter abre, Escape cierra y el foco vuelve al botón.'),
                   ('Foco a la vista', 'En cada paso, el foco se ve completo, sin quedar debajo de una cabecera fija.'),
                   ('Código', f'Ningún {c("div")} o {c("span")} hace de enlace o de botón, y todo control tiene nombre accesible.'),
                   ('Revisión automática', 'Una herramienta de accesibilidad, como axe o Lighthouse, no reporta errores de nombre, rol ni estado.'),
                   ('Ampliación', 'Al 200 %, nombres y estados siguen visibles y legibles.')]),
    ]),
    norma('KYN-SDI-ARQ-009', 's-02-02-05', 'La presentación cambia; los destinos se mantienen',
          'La persona cambia de dispositivo sin volver a aprender: <strong>los mismos destinos, con los mismos nombres</strong>, en cualquier tamaño de pantalla.', [
        req(N('La navegación puede modificar su presentación según el espacio disponible, conservando acceso a las funciones esenciales.', 'puede'),
            N('La navegación debe conservar acceso a sus destinos esenciales cuando cambia de escritorio a móvil.', 'debe')),
        matriz('Qué se mantiene y qué cambia entre tamaños de pantalla', [('Se mantiene', 'En todos los tamaños'), ('Cambia', 'Según el espacio')], [
            ('Destinos', ['Los destinos esenciales, con el mismo nombre y en el mismo orden.', 'Cuántos se ven a la vez; los secundarios pasan a «Más».']),
            ('Formato', ['Un control visible para cada destino.', 'Navegación lateral, superior, barra inferior, pestañas o panel.']),
            ('Ubicación', ['La sección activa y el título de la página.', 'La ruta jerárquica se abrevia al nivel superior inmediato.']),
            ('Controles', ['Nombre accesible, estado y orden de foco.', f'El tamaño de los objetivos táctiles, según {P22}.'])]),
        prosa(f'El formato predeterminado de los productos SaaS lo define {P37}.'),
        sub('Verificación'),
        prosa('Se listan los destinos esenciales en escritorio y se buscan a 320 px de ancho y con ampliación del 400 %.',
              'Resultado esperado: están todos, con el mismo nombre, y ninguno exige desplazamiento horizontal.'),
    ]),
    norma('KYN-SDI-ARQ-010', 's-02-02-06', 'Volver a una lista devuelve el trabajo donde quedó',
          'Revisar un registro y seguir con la lista es una sola tarea: <strong>el sistema conserva el contexto</strong> para retomarla donde quedó.', [
        req(N('Cuando se vuelve desde un detalle a un listado, el sistema debería conservar filtros, búsqueda y posición cuando sean relevantes para continuar la tarea.', 'deberia')),
        pasos([('Abrir', 'La persona abre un registro desde un listado filtrado, ordenado o con una búsqueda.', 'Decisión', 'La consulta, los filtros, el orden y la página quedan en la dirección (URL).'),
               ('Volver', 'Regresa con el control Volver de la interfaz o con el del navegador.', 'Decisión', 'Los dos llevan al mismo listado, en el mismo estado.'),
               ('Retomar', 'El listado muestra la misma búsqueda, los mismos filtros y el mismo orden.', 'Decisión', 'La posición se restaura y el foco vuelve al registro abierto.')]),
        stack([('Excepciones', ['Si el registro se eliminó o ya no cumple los filtros, el listado se recupera igual y avisa del cambio. Una sesión nueva empieza con el listado en su estado inicial.'])]),
        sub('Verificación'),
        prosa('Se abre el registro número 15 de un listado filtrado y ordenado, y se vuelve con los dos controles. Después se recarga el listado.',
              'Resultado esperado: mismos filtros, orden, página y posición, con el foco en ese registro; al recargar, los filtros siguen aplicados.'),
    ]),
    seccion('ejemplo', '05', 'Ejemplo de aplicación', 'Una solicitud dentro de Administración',
            'Si una pantalla pertenece a Administración › Solicitudes, <strong>el menú señala la sección activa</strong> y la persona puede regresar al listado sin perder innecesariamente su contexto.', [
        stack([('Ubicación', ['El menú marca Administración y, dentro, Solicitudes. La ruta muestra Administración › Solicitudes › Solicitud 2026-118.']),
               ('Nombres', ['«Solicitudes» se llama igual en el menú, la ruta y el título del listado.']),
               ('En móvil', ['El panel de navegación conserva los mismos destinos, y la ruta se abrevia a «Solicitudes».']),
               ('Regreso', ['Al volver de la solicitud, el listado conserva el filtro «Pendientes», el orden y la posición.'])]),
    ]),
]

CAPITULOS = [
    # (módulo, capítulo, archivo del capítulo, secciones, descripción corta propuesta)
    ('02', '02.02', 'estructura-de-navegacion', C05,
     'Cómo se reconoce la ubicación, se recorren los destinos y se retoma el trabajo, en cualquier forma de navegación.'),
]


def matriz_md():
    filas = ['| Código | Cap. | Nombre corto | Estado | Textos de origen | Responsabilidad | Se cita en lugar de repetirse |', '| --- | --- | --- | --- | --- | --- | --- |']
    for n in REG['normas']:
        filas.append(f"| {n['id']} | {n['capitulo']} | {n['nombre']} | {n['estado']} | {' · '.join(n['origen'])} | {n['responsabilidad']} | {n['cita'] or '—'} |")
    return ('# Matriz normativa del Sistema de Diseño · capítulos 01 a 06\n\n'
            'Generada por `tools/sd_capitulos.py` desde `data/sd-normas.json` (fuente única de los códigos). No se edita a mano.\n\n'
            '- **borrador:** código emitido, con página y en el buscador. Hoy, solo el capítulo 05 Navegación.\n'
            '- **reservado:** número apartado para el capítulo pendiente. Sin página, sin buscador y sin estado vigente ni implementado.\n'
            '- Un código corresponde a una responsabilidad normativa diferenciable. Los textos base y de ampliación que expresaban la misma obligación se unieron, también entre capítulos.\n'
            '- Las normas UIX conservan su ID. Su destino está en `propuestas/auditoria-uix-2026-11-17.md`.\n\n'
            + '\n'.join(filas) + '\n\n'
            '## Uniones entre capítulos\n\n'
            '| Textos | Queda en | Motivo |\n| --- | --- | --- |\n'
            '| Regreso sin pérdida (05) · Recuperación y Recuperación del contexto (06) | ARQ-010 (05) | Las tres piden conservar consulta, filtros y posición al volver. 06 la cita |\n'
            '| Hipótesis y evidencia (02) · Evidencia diferenciada (03) | PEX-014 (03) | Distinguir hipótesis de evidencia es una sola obligación |\n'
            '| Sin competencia visual innecesaria (01) · Expresión proporcionada (11) | PEX-001 (01) | La misma prohibición. 11 la cita cuando se construya |\n'
            '| Continuidad del trabajo (02) · Contexto conservado (17) | 17 Flujos de trabajo | Conservar el progreso es propio de los flujos. 02 no lo repite |\n'
            '| Comportamiento previsible (01) · Acciones previsibles (05) | Las dos | 01 regula toda función; 05 aplica el principio a nombres, destinos y lugares de la navegación |\n'
            '| Contexto antes de actuar (01) · Consecuencias claras (19) | PEX-006 (01) | 19 la integra o la cita cuando se construya |\n'
            '| Estado comprensible (01) · Resultado visible (15) | Las dos | 01 fija el principio; 15 define los componentes |\n'
            '| Evidencia diferenciada (03) · Evidencia registrada (44) | PEX-014 (03) | La misma obligación. 44 la cita |\n')


def main():
    sd = json.load(io.open(os.path.join(ROOT, 'data', 'sistema-diseno.json'), encoding='utf-8'))
    for mod, capn, slug, secs, dc in CAPITULOS:
        dst = os.path.join(ROOT, 'data', 'sd-capitulos', slug + '.html')
        io.open(dst, 'w', encoding='utf-8', newline='\n').write(
            f'    <!-- Capítulo {capn} · generado por tools/sd_capitulos.py desde data/sd-normas.json. No se edita a mano. En borrador. -->'
            + ''.join(secs))
        m = next(x for x in sd['modulos'] if x['n'] == mod)
        cp = next(x for x in m['capitulos'] if x['n'] == capn)
        nums = [n for n in REG['normas'] if n['estado'] != 'reservado' and n['ruta'].split('#')[0].endswith('/' + slug + '.html')]
        cp['subcapitulos'] = [{'n': n['ruta'].split('#s-')[1].replace('-', '.'), 't': n['nombre'], 'estado': n['estado'], 'st': n['nombre'], 'norma': n['id']} for n in nums]
        cp['estado'] = 'borrador'
        cp['dc'] = dc
        registrar(os.path.relpath(dst, ROOT).replace(os.sep, '/'))
    io.open(os.path.join(ROOT, 'data', 'sistema-diseno.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(sd, ensure_ascii=False, indent=1) + '\n')
    io.open(os.path.join(ROOT, 'propuestas', 'matriz-normativa-sd-01-06.md'), 'w', encoding='utf-8', newline='\n').write(matriz_md())
    print('ok ·', ', '.join(s for _, _, s, _, _ in CAPITULOS))


if __name__ == '__main__':
    main()
