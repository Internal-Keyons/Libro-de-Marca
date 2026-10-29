"""Formulario de evaluación del Taller de nivelación 02 · Genia 2026 (Keyons e Ingenya).

Uso:  python tools/genia_taller02.py

Toma la plantilla tools/genia_taller02.html, le pone los íconos del catálogo del libro
de marca y las preguntas, y escribe propuestas/genia-taller-02/ (index.html de producción, demo.html y presentacion.html)
más el zip para desarrollo.
No forma parte del manual: es insumo para el capítulo de interfaces.
"""
import json
import os
import re
import shutil
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'propuestas', 'genia-taller-02')
cat = open(os.path.join(ROOT, 'recursos', 'iconos.html'), encoding='utf-8').read()


def icon(n):
    return re.search(r'data-n="%s"[^>]*>(<svg.*?</svg>)' % n, cat, re.S).group(1).replace('class="ic"', 'class="ico"')


# Preguntas a partir del material de la sesión, con las correcciones de la revisión de calidad
Q = [
    {'k': 'El caso SOL-017', 't': 'u',
     'q': 'El equipo recibe el pedido: «El cliente solicita el estado de la entrega SOL-017». Antes de escribir el prompt, ¿qué le están pidiendo realmente?',
     'o': ['Un resumen de todos los documentos adjuntos, por fecha.',
           'Saber qué está listo, qué está pendiente y si se puede confirmar la fecha de entrega.',
           'Una nueva fecha de entrega, propuesta por la IA a partir del cronograma.',
           'La lista de responsables que participan en el proyecto.'], 'a': 1,
     'w': 'El pedido define el resultado: qué está listo, qué falta y si la fecha se puede confirmar. Un resumen de todo, sin ese foco, no responde al cliente.'},
    {'k': 'Test de calidad', 't': 'r',
     'q': 'Relacione cada pregunta del test con el criterio que evalúa.',
     'rows': ['¿Coinciden avances, fechas, responsables y aprobaciones con los documentos?',
              '¿Distingue lo propuesto de lo aprobado, sin inventar fechas ni responsables?',
              '¿Presenta una matriz clara de hallazgos, evidencias, acciones y confirmaciones?',
              '¿Cita fuente, versión y estado, e identifica contradicciones?'],
     'o': ['Resultado', 'Contexto', 'Datos', 'Reglas', 'Salida', 'Validación'], 'a': [2, 3, 4, 5],
     'w': 'Cada criterio sale del pedido: los datos se cotejan con los documentos, las reglas evitan inventar, la salida define el formato y la validación exige fuentes.'},
    {'k': 'Test de calidad', 't': 'u',
     'q': 'Gemini califica su respuesta con seis «Sí» de seis. ¿Qué significa?',
     'o': ['Que está lista para enviarla al cliente sin cambios.',
           'Que cumple los seis criterios del test, pero requiere revisión humana antes de usarse.',
           'Que la IA garantiza que todos los datos son correctos.',
           'Que debe repetir el test en otro chat para confirmarlo.'], 'a': 1,
     'w': 'El test de Gemini es una ayuda: la IA también puede equivocarse al calificar. Quien decide si la respuesta sirve es usted.'},
    {'k': 'Test de calidad', 't': 'u',
     'q': 'Una pregunta del test se cumple solo en parte. ¿Cómo se responde?',
     'o': ['Sí, porque cumple lo principal.',
           'No: si el cumplimiento es parcial, la respuesta es No.',
           'Se cuenta como medio punto.',
           'Se omite y se califica sobre cinco.'], 'a': 1,
     'w': 'Un cumplimiento parcial es un «No». Así cada «No» señala con precisión lo que falta mejorar en el prompt.'},
    {'k': 'Mejorar la respuesta', 't': 'm',
     'q': '¿Cuáles son técnicas para mejorar una respuesta sin empezar de cero?',
     'o': ['Pedir solo lo que falta, en el mismo chat.',
           'Pedirle que separe hechos de supuestos.',
           'Borrar la conversación y escribir un prompt el doble de largo.',
           'Dividir la tarea por etapas: extraer, analizar y redactar.',
           'Aceptar la respuesta si suena segura.',
           'Pedirle que pregunte lo necesario antes de responder.'], 'a': [0, 1, 3, 5],
     'w': 'Se trabaja sobre el primer resultado: completar, separar hechos de supuestos, dividir la tarea o pedir que pregunte primero. Un prompt más largo no es mejor por eso, y una respuesta que suena segura no siempre tiene respaldo.'},
    {'k': 'Datos del cliente', 't': 'u',
     'q': 'Antes de pegar en Gemini un informe con datos de un cliente, ¿qué corresponde hacer?',
     'o': ['Pegarlo tal cual: la cuenta corporativa protege la información.',
           'Cambiar nombres, correos y montos reales por etiquetas o datos ficticios.',
           'Quitar solo los montos y dejar los nombres.',
           'Pedirle a Gemini que no guarde la conversación.'], 'a': 1,
     'w': 'Los nombres, correos y montos reales de clientes se cambian por etiquetas, como [Cliente A], o por datos ficticios antes de usarlos con la IA.'},
    {'k': 'El ciclo', 't': 'o',
     'q': 'Ordene los pasos del ciclo para trabajar con la IA.',
     'o': ['Defina el resultado que necesita.',
           'Pida con un prompt claro y completo.',
           'Revise la respuesta con el test.',
           'Ajuste lo que falta en el mismo chat.',
           'Guarde el prompt que funcionó.'],
     'w': 'Es un ciclo, no una receta: se define, se pide, se revisa, se ajusta y se guarda lo que funcionó. Cada vuelta mejora el resultado.'},
    {'k': 'NotebookLM', 't': 'u',
     'q': 'NotebookLM responde con números de cita. ¿Qué hace usted?',
     'o': ['Confiar en la respuesta: si tiene cita, es correcta.',
           'Abrir la cita y comprobar en el documento que el texto respalda lo afirmado.',
           'Ignorar las citas y revisar solo la redacción.',
           'Pedirle a Gemini que confirme la respuesta.'], 'a': 1,
     'w': 'Las citas permiten verificar, pero no garantizan por sí solas que la respuesta sea correcta. Se abre el número y se compara con el documento.'},
    {'k': 'Gems y NotebookLM', 't': 'r',
     'q': 'Relacione cada elemento con lo que hace.',
     'rows': ['Las fuentes de una Gem', 'Las instrucciones de una Gem', 'NotebookLM', 'Un notebook y una Gem'],
     'o': ['Definen cómo trabaja la asistente.',
           'Definen qué sabe la asistente.',
           'Consulta los documentos cargados y señala la fuente.',
           'No se conectan solos: las fuentes se cargan en cada uno.',
           'Se actualizan solos con los archivos de Drive.'], 'a': [1, 0, 2, 3],
     'w': 'Fuentes: qué sabe. Instrucciones: cómo trabaja. NotebookLM sirve para consultar y verificar fuentes, y crear un notebook no conecta sus documentos con la Gem.'},
    {'k': 'Prueba A · VERA', 't': 'm',
     'q': 'Le pregunta a VERA: «¿Puedo incluir nombres, correos y montos reales de un cliente en Gemini?». ¿Qué debe cumplir su respuesta?',
     'o': ['Dice con claridad si se puede o no.',
           'Indica el documento y el apartado de donde sale la regla.',
           'Autoriza una excepción si el informe es urgente.',
           'Propone una alternativa segura, como usar etiquetas.',
           'Responde que, en general, no debería haber problema.'], 'a': [0, 1, 3],
     'w': 'Una regla sin fuente no es una regla. VERA responde con claridad, cita documento y apartado, propone una alternativa segura y no inventa permisos ni autoriza en nombre de Ingenya.'},
]


# Su opinión: encuesta opcional y anónima al final, sobre el taller y quienes lo impartimos
FB = [
    {'t': 's', 'q': '¿Qué tan aplicables son las herramientas y conceptos del taller en su trabajo diario?',
     'lo': 'Nada aplicable', 'hi': 'Totalmente aplicable'},
    {'t': 'u', 'q': '¿Cómo califica la claridad, el dominio del tema y la apertura del facilitador?',
     'o': [['Excelente', 'Dominio total y muy claro'], ['Bueno', 'Claro y seguro'],
           ['Regular', 'Aceptable, pero puede mejorar'], ['Muy flojo', 'Confuso o poco preparado']]},
    {'t': 's', 'q': '¿Qué le pareció la calidad del material y el contenido visual?', 'lo': 'Muy malo', 'hi': 'Excelente'},
    {'t': 'u', 'q': '¿Cómo evalúa el manejo del tiempo y el ritmo del taller?',
     'o': [['Ritmo perfecto', 'Ágil y bien aprovechado'], ['Bueno', 'Estuvo bien, se entendió todo'],
           ['Un poco pesado', 'Mucho contenido en poco tiempo'], ['Mal organizado', 'Faltó tiempo o se sintió eterno']]},
    {'t': 'x', 'q': '¿Qué fue lo que más le aportó y qué sugerencia nos daría para mejorar?',
     'ph': 'Escriba aquí sus comentarios'},
]


# Íconos del catálogo del libro de marca que usa el formulario (también van sueltos en el zip, en assets/iconos/)
ICONOS = [('{IC_PREG}', 'portapapeles'), ('{IC_TIEMPO}', 'alarma'), ('{IC_INTENTO}', 'salir'), ('{IC_CHECK}', 'check'),
          ('{IC_X}', 'cerrar'), ('{IC_ERR}', 'cerrar-solido'), ('{IC_MAS}', 'mas'), ('{IC_MENOS}', 'menos'),
          ('{IC_BACK}', 'flecha-izquierda'), ('{IC_R}', 'flecha-derecha'), ('{IC_UP}', 'flecha-arriba'), ('{IC_DOWN}', 'flecha-abajo'),
          ('{IC_CH}', 'chevron-derecha'), ('{IC_DL}', 'descargar')]
# El agarre del ordenamiento no está en el catálogo: seis puntos dibujados en el formulario
AGARRE = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 18" width="18" height="18" fill="#10122A">'
          + ''.join(f'<circle cx="{x}" cy="{y}" r="1.6"/>' for y in (3.5, 9, 14.5) for x in (6, 12)) + '</svg>\n')


def icon_file(n):
    """El ícono como archivo SVG suelto: en Azul Noche y con currentColor, para cambiarle el color con CSS."""
    return icon(n).replace('<svg class="ico" viewBox="0 0 32 32" aria-hidden="true">',
                           '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" color="#10122A">') + '\n'


def render(a_path, img_path, demo=False):
    """demo=False: formulario de producción, sin las vistas de muestra ni el aviso simulado de intento único."""
    h = open(os.path.join(ROOT, 'tools', 'genia_taller02.html'), encoding='utf-8').read()
    for k, n in ICONOS:
        h = h.replace(k, icon(n))
    h = (h.replace('{DATA}', json.dumps(Q, ensure_ascii=False)).replace('{FB}', json.dumps(FB, ensure_ascii=False))
         .replace('{A}', a_path).replace('{IMG}', img_path))
    h = re.sub(r'/\*DEMO\*/.*?/\*FIN DEMO\*/\n?', '', h, flags=re.S) if not demo else h.replace('/*DEMO*/', '').replace('/*FIN DEMO*/', '')
    # El cielo del libro va dentro del archivo (sin dependencias); se inserta al final para no tocar su código
    return h.replace('{CIELO}', open(os.path.join(ROOT, 'js', 'keyons-cielo.js'), encoding='utf-8').read().strip())


VISTAS = [('Inicio', ''), ('Selección única', 'q'), ('Selección múltiple', 'm'), ('Ordenamiento', 'o'),
          ('Relación con desplegables', 'r'), ('Aviso de intento único', 'error'), ('Gracias', 'done'),
          ('Tiempo agotado', 'timeout'), ('Explicaciones', 'rev'), ('Su opinión', 'fb')]


def showcase(zip_href):
    rows = ''.join(f'''
<section class="row"><h2>{t}</h2>
  <div class="pair">
    <div class="dev"><p>Computadora · 1280 px</p><div class="desk"><iframe src="demo.html{'#' + q if q else ''}" name="{q}" title="{t} en computadora" loading="lazy"></iframe></div></div>
    <div class="dev"><p>Celular · 390 px</p><div class="phone"><div><iframe src="demo.html{'#' + q if q else ''}" name="{q}" title="{t} en celular" loading="lazy"></iframe></div></div></div>
  </div>
</section>''' for t, q in VISTAS)
    dl = (f'<a class="dl" href="{zip_href}" download>Descargar zip <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2.5v8M4.5 7 8 10.5 11.5 7M3 13.5h10"/></svg></a>'
          if zip_href else '')
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Taller de nivelación 02 · Propuesta</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--noche:#10122A;--blanco:#F4F4F4;--t3:#6B6D7E}}
*{{box-sizing:border-box;margin:0}}
body{{background:#E9EAEE;color:var(--noche);font-family:'Plus Jakarta Sans',system-ui,sans-serif;padding:48px 40px 80px}}
h1{{font-size:28px;font-weight:500;letter-spacing:-.02em}}
.sub{{margin-top:8px;max-width:72ch;font-size:14px;line-height:1.6;color:var(--t3)}}
.row{{margin-top:48px}}
.row h2{{font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--t3)}}
.pair{{display:flex;flex-wrap:wrap;align-items:flex-start;gap:40px;margin-top:16px}}
.dev p{{margin-bottom:10px;font-size:12px;color:var(--t3)}}
.desk{{width:calc(1280px * .62);height:calc(820px * .62);overflow:hidden;background:#fff;box-shadow:0 0 0 1px rgba(16,18,42,.12),0 30px 60px -40px rgba(16,18,42,.5)}}
.desk iframe{{width:1280px;height:820px;border:0;transform:scale(.62);transform-origin:0 0}}
.phone{{width:calc(390px * .78 + 20px);height:calc(844px * .78 + 20px);padding:10px;border-radius:44px;background:var(--noche);box-shadow:0 30px 60px -40px rgba(16,18,42,.6)}}
.phone div{{width:100%;height:100%;overflow:hidden;border-radius:34px;background:#fff}}
.phone iframe{{width:390px;height:844px;border:0;transform:scale(.78);transform-origin:0 0}}
.top{{display:flex;align-items:flex-start;justify-content:space-between;gap:24px;flex-wrap:wrap}}
.dl{{display:inline-flex;align-items:center;gap:10px;height:46px;padding:0 24px;border-radius:999px;background:#10122A;color:#F4F4F4;font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;text-decoration:none;transition:background-color .25s,color .25s}}
.dl:hover{{background:#729BDD;color:#10122A}}
.dl svg{{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}}
</style>
</head>
<body>
<div class="top"><div><h1>Taller de nivelación 02 · Genia 2026 · propuesta con la marca Keyons</h1>
<p class="sub">Interactivo: se puede escribir, comenzar, responder y finalizar. Cuatro tipos de pregunta: única, múltiple, orden y relación. Para ver el aviso de intento único, use un correo que contenga «usado».</p></div>{dl}</div>
{rows}
</body>
</html>
'''


LEEME = '''Taller de nivelación 02 · Genia 2026 · Formulario de evaluación (Keyons e Ingenya)
Sesión 02 · Contexto con criterio · Darle conocimiento a VERA

ARCHIVOS
- index.html: el formulario, listo para publicar. Empieza en la pantalla de inicio. HTML, CSS y JavaScript en un solo archivo.
- assets/: tipografía TASA Orbiter (licencia OFL incluida) y logotipos. index.html los busca en esta carpeta.
- demo.html y presentacion.html: solo para revisar el diseño. demo.html es el mismo formulario con vistas de muestra
  (#q, #m, #o, #r, #error, #done, #timeout, #rev, #fb); presentacion.html las muestra en computadora y celular. No van a producción.

PUBLICAR
1. Borrar el botón «Descargar zip» del inicio: en index.html está entre los comentarios «▼ ELIMINAR ANTES DE PUBLICAR ▼»
   y «▲ FIN DEL BLOQUE PARA ELIMINAR ▲» (el bloque <div class="dlzip"> en el HTML y su estilo .dlzip en el CSS).
   Solo sirve para revisar la propuesta y no afecta nada más.
2. Subir index.html y la carpeta assets/ a cualquier servidor estático (o abrir index.html directo en el navegador para probar).
Sin configurar nada, el formulario funciona completo pero no guarda resultados.

ÍCONOS
Todos salen del catálogo de íconos del manual de marca Keyons (32 × 32, trazo de 2,5) y ya van dentro de index.html.
Sueltos, en assets/iconos/, por si se necesitan aparte: portapapeles, alarma, salir, check, cerrar, cerrar-solido, mas,
menos, flecha-izquierda, flecha-derecha, flecha-arriba, flecha-abajo, chevron-derecha y descargar. Usan currentColor
(Azul Noche por defecto). agarre.svg es el agarre de seis puntos del ordenamiento; no está en el catálogo.

CONECTAR CON EL SERVIDOR (lo único que se edita)
Dentro de index.html, en el script principal, la constante CONFIG:
  const CONFIG = { inicio: '', resultado: '', opinion: '', taller: 'Taller de nivelación 02', minutos: 15 };
Cada dirección recibe un POST con JSON (Content-Type: application/json):

1. inicio: al tocar «Comenzar».
   Envía:    {"nombre": "Ana Solís", "correo": "ana@empresa.com"}
   Responde: {"permitido": true}  o  {"permitido": false} si ese correo ya usó su único intento.
   Si el servidor no responde, se avisa al participante y no comienza.

2. resultado: al finalizar o cuando se agota el tiempo. Se reintenta tres veces si falla.
   Envía: {"taller", "nombre", "correo", "nota" (0 a 10, con medios puntos), "tiempo_agotado" (true/false),
           "inicio" y "fin" (fecha ISO), "respuestas": [{"id" (1 a 10), "tipo" (u, m, o, r), "pregunta",
           "respuesta" (textos elegidos; en relación, una lista de {fila, opcion}; null si no respondió), "puntos" (1, 0,5 o 0)}]}

3. opinion: encuesta opcional del final. Se anuncia como anónima: guardarla aparte, sin relacionarla con el correo.
   Envía: {"taller", "respuestas": [{"pregunta", "respuesta"}]}  (escalas de 1 a 5, el texto de la opción o el comentario; null si la omitió)

Recomendado en el servidor: registrar la hora de inicio en «inicio» y no aceptar resultados fuera del tiempo,
y decidir si recargar la página cuenta como intento (el navegador pide confirmar antes de salir durante las preguntas).

CONTENIDO
- Preguntas: constante BASE. u única (a = índice correcto) · m múltiple (a = índices correctos) ·
  o ordenamiento (o = pasos en el orden correcto) · r relación (rows = filas, o = opciones, a = opción correcta por fila).
- Encuesta: constante FB. s escala 1 a 5 · u una opción · x comentario libre.
- Al comenzar, el orden de preguntas, opciones y filas se mezcla para cada participante.

CALIFICACIÓN
- 1 punto si la respuesta es correcta.
- 0,5 si acierta la mitad o más: en múltiple, sin marcar incorrectas; en orden, pasos en su lugar; en relación, filas.
- 0 en los demás casos y sin responder. Nota de 0 a 10.

DETALLES
- Plus Jakarta Sans se carga desde Google Fonts; TASA Orbiter, desde assets/.
- Encabezado: el cielo con Ráfaga del manual de marca (KeyonsCielo v1.1, WebGL) va dentro del primer script.
  No se modifica el shader, solo su configuración. Sin WebGL queda un degradado celeste.
- Desplegables propios (role="listbox"): mouse, flechas, Enter y Esc.
- Ordenamiento: arrastrar con mouse o dedo (agarre o mantener presionado) y flechas como alternativa.
'''


def main():
    os.makedirs(OUT, exist_ok=True)
    shutil.copy(os.path.join(ROOT, 'propuestas', 'genia-formulario', 'ingenya-color.png'), os.path.join(OUT, 'ingenya-color.png'))
    for old in ('formulario.html', 'ingenya-blanco.png'):   # nombres de versiones anteriores
        if os.path.exists(os.path.join(OUT, old)):
            os.remove(os.path.join(OUT, old))
    zip_path = os.path.join(ROOT, 'propuestas', 'genia-taller-02.zip')
    pages = {'index.html': render('../../assets/', ''), 'demo.html': render('../../assets/', '', demo=True),
             'presentacion.html': showcase('../genia-taller-02.zip')}
    for name, html in pages.items():
        open(os.path.join(OUT, name), 'w', encoding='utf-8').write(html)

    A = os.path.join(ROOT, 'assets')
    files = {
        'assets/fonts/TASAOrbiter-VariableFont_wght.ttf': os.path.join(A, 'fonts', 'TASAOrbiter-VariableFont_wght.ttf'),
        'assets/logos/estrella.svg': os.path.join(A, 'logos', 'estrella.svg'),
        'assets/logos/favicon.svg': os.path.join(A, 'logos', 'favicon.svg'),
        'assets/logos/keyons-negro.svg': os.path.join(A, 'logos', 'keyons-negro.svg'),
        'assets/logos/ingenya-color.png': os.path.join(OUT, 'ingenya-color.png'),
    }
    ofl = os.path.join(A, 'fonts', 'OFL.txt')
    if os.path.exists(ofl):
        files['assets/fonts/OFL.txt'] = ofl
    d = 'genia-taller-02/'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr(d + 'index.html', render('assets/', 'assets/logos/'))
        z.writestr(d + 'demo.html', render('assets/', 'assets/logos/', demo=True))
        z.writestr(d + 'presentacion.html', showcase(''))
        z.writestr(d + 'LEEME.txt', LEEME)
        for _, n in ICONOS:
            z.writestr(f'{d}assets/iconos/{n}.svg', icon_file(n))
        z.writestr(d + 'assets/iconos/agarre.svg', AGARRE)
        for arc, path in files.items():
            z.write(path, d + arc)
    print('ok', OUT, os.path.getsize(zip_path))


if __name__ == '__main__':
    main()
