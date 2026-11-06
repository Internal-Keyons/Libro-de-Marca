"""Laboratorio de Interfaces · servidor local.

Sirve el sitio como el servidor de siempre y agrega la API del Laboratorio:
  GET  /api/lab/estado             qué puede hacer el servidor (construir, guardar)
  POST /api/lab/generar            construye una interfaz con la API de Claude y las reglas de Keyons
  POST /api/lab/guardar            guarda un experimento en _lab/experimentos/ (fuera del repositorio)
  GET  /api/lab/lista              experimentos guardados y propuestas para la marca
  GET  /api/lab/experimento?id=…   un experimento
  POST /api/lab/proponer           copia un experimento a sistema-diseno/laboratorio/propuestas/
  POST /api/lab/normas             sugiere normas a partir de un experimento y las guarda como notas en _lab/notas/

Uso:
  python tools/laboratorio.py            http://127.0.0.1:4330/sistema-diseno/laboratorio.html
  python tools/laboratorio.py --demo     sin clave: devuelve un ejemplo fijo, para probar

La clave de la API se toma de ANTHROPIC_API_KEY o de un archivo .env.local en la raíz
(una línea ANTHROPIC_API_KEY=...). Ese archivo no se versiona ni se publica.
Requiere el SDK: pip install anthropic
Solo escucha en 127.0.0.1: nadie fuera de este equipo puede usarlo.
"""
import datetime
import html as H_
import http.server
import io
import json
import os
import re
import sys
import unicodedata
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXP = os.path.join(ROOT, '_lab', 'experimentos')
PROP = os.path.join(ROOT, 'sistema-diseno', 'laboratorio', 'propuestas')
NOTAS = os.path.join(ROOT, '_lab', 'notas')
PORT = int(os.environ.get('LAB_PORT', '4330'))
DEMO = '--demo' in sys.argv
MODEL = 'claude-opus-5-5'


def read(p):
    with io.open(os.path.join(ROOT, p), encoding='utf-8') as f:
        return f.read()


def api_key():
    if os.environ.get('ANTHROPIC_API_KEY'):
        return True
    p = os.path.join(ROOT, '.env.local')
    if os.path.exists(p):
        for line in io.open(p, encoding='utf-8'):
            k, _, v = line.strip().partition('=')
            if k.strip() == 'ANTHROPIC_API_KEY' and v.strip():
                os.environ['ANTHROPIC_API_KEY'] = v.strip().strip('"\'')
                return True
    return False


def sdk():
    try:
        import anthropic  # noqa: F401
        return True
    except ImportError:
        return False


def slug(s):
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode()
    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    return s[:60] or 'experimento'


def now():
    return datetime.datetime.now().isoformat(timespec='seconds')


# ── Contexto de marca: estable y en caché (no lleva fechas ni datos variables) ──
SCHEMA = {
    'type': 'object',
    'properties': {
        'titulo': {'type': 'string'},
        'resumen': {'type': 'string'},
        'html': {'type': 'string'},
        'css': {'type': 'string'},
        'js': {'type': 'string'},
        'normas': {'type': 'array', 'items': {'type': 'string'}},
    },
    'required': ['titulo', 'resumen', 'html', 'css', 'js', 'normas'],
    'additionalProperties': False,
}

INSTRUCCIONES = """Usted construye interfaces de producto para Keyons dentro del Laboratorio de Interfaces.
El resultado se muestra en un escenario aislado que ya carga tokens.css (tokens de Keyons) y el kit
css/laboratorio-kit.css. Devuelva solo el JSON pedido.

Cómo construir
- html: solo el contenido del <body>. Use los componentes del kit (prefijo lx-) que aparecen abajo.
  Para una aplicación, envuelva todo en <div class="lx-app"> con <nav class="lx-nav"> y <main class="lx-main">.
  Para una pieza suelta (un mensaje, una página de error, un formulario), use <main class="lx-main"> sin navegación.
- css: estilos adicionales mínimos. Use SIEMPRE las variables --lab-* (color, tipografía, espacio, radios,
  íconos, movimiento) y nunca valores fijos de color o de familia: así el usuario puede explorar paleta,
  tipografía, diagramación, forma, iconografía y movimiento desde los controles. Nada de @import ni recursos externos.
- js: solo si la interacción lo necesita (pestañas, filtros, validación, abrir y cerrar). JavaScript
  sencillo, sin librerías ni red. Cadena vacía si no hace falta.
- Íconos: SVG en línea con class="lx-i", viewBox="0 0 24 24", solo trazos (sin fill), al estilo del catálogo.
- Datos: use los que le den. Si no hay, invente datos de muestra creíbles y en español, nunca lorem ipsum
  salvo que se lo pidan.
- titulo: nombre breve del experimento. resumen: una o dos frases sobre lo que construyó.
  normas: los códigos KYN-MRK-… que aplicó con más peso (máximo 6).

Reglas que no se negocian
- Español, trato de «usted», frases breves; títulos que dicen la conclusión, no el tema.
- Escala tipográfica de lectura: 12 · 14 · 16 · 20 · 24 · 32 px (las variables --lab-t-* ya la siguen).
  Nunca dos tamaños que se parezcan; la jerarquía se construye con tamaño, peso, color y espacio.
- Un párrafo, una idea, máximo cuatro líneas. Listas parejas: todos los elementos de una o de dos líneas.
- Esquinas: una tarjeta aislada lleva sus cuatro esquinas rectas; dentro de un grupo (lx-group),
  exterior recta e interior curva. Botones en forma de píldora; campos con radio de control.
- Salmón Tierra y Azul Cielo nunca se apoyan uno sobre otro. Estética plana: sin sombras decorativas.
- Accesibilidad: contraste 4,5:1 en texto, áreas táctiles de 44 px, cada control con nombre, orden natural
  del foco, estados que no dependen solo del color, errores que explican qué pasó y cómo continuar.
- Responsive: el escenario se prueba a 1280, 768 y 375 px; nada debe salirse del ancho.
- Si le piden un cambio sobre una versión existente, conserve todo lo demás y cambie solo lo pedido.
"""


def contexto():
    kit = read('css/laboratorio-kit.css')
    ejemplos = read('js/laboratorio-plantillas.js')
    return [
        INSTRUCCIONES,
        '## Kit del escenario (css/laboratorio-kit.css)\n' + kit,
        '## Plantillas de referencia (cómo se combinan los componentes)\n' + ejemplos,
        '## Estética real aplicada en el proyecto\n' + read('docs/ESTETICA_REAL_KEYONS.md') if os.path.exists(os.path.join(ROOT, 'docs/ESTETICA_REAL_KEYONS.md')) else '',
        '## Tokens de Keyons\n' + read('ia/tokens.json'),
        '## Libro de Marca y Experiencia (normas vigentes)\n' + read('ia/libro-de-marca.md'),
    ]


def generar(body):
    pedido = (body.get('pedido') or '').strip()
    datos = (body.get('datos') or '').strip()
    cambio = (body.get('cambio') or '').strip()
    actual = body.get('actual') or None
    if not pedido and not cambio:
        raise ValueError('Falta el pedido.')
    if DEMO:
        return demo(pedido, cambio)
    partes = ['Pedido: ' + pedido]
    if datos:
        partes.append('Datos de ejemplo para usar:\n' + datos)
    if cambio and actual:
        partes.append('Versión actual:\n<html>\n' + (actual.get('html') or '') + '\n</html>\n<css>\n'
                      + (actual.get('css') or '') + '\n</css>\n<js>\n' + (actual.get('js') or '') + '\n</js>')
        partes.append('Cambio pedido: ' + cambio)
    out, costo = llamar('\n\n'.join(partes), SCHEMA)
    out['costo'] = costo
    return out


# Precios por millón de tokens de Claude Opus 5.5 (USD). Escribir en la caché de 1 hora cuesta el doble de la entrada.
PRECIO = {'entrada': 4.0, 'salida': 20.0, 'cache_lee': 0.20, 'cache_escribe': 8.0}


def llamar(texto, schema):
    """Una llamada a la API con las reglas de Keyons en caché de 1 hora. Devuelve (json, costo)."""
    import anthropic
    client = anthropic.Anthropic()
    system = [{'type': 'text', 'text': '\n\n'.join(x for x in contexto() if x),
               'cache_control': {'type': 'ephemeral', 'ttl': '1h'}}]
    kw = dict(
        model=MODEL,
        max_tokens=64000,
        system=system,
        output_config={'effort': 'high', 'format': {'type': 'json_schema', 'schema': schema}},
        messages=[{'role': 'user', 'content': texto}],
        betas=['server-side-fallback-2026-07-01'],
    )
    try:
        stream = client.beta.messages.stream(fallbacks='default', **kw)
    except TypeError:   # SDK anterior al parámetro: se envía igual en el cuerpo
        stream = client.beta.messages.stream(extra_body={'fallbacks': 'default'}, **kw)
    with stream as st:
        msg = st.get_final_message()
    if msg.stop_reason == 'refusal':
        raise ValueError('La API declinó el pedido. Reformúlelo e inténtelo de nuevo.')
    if msg.stop_reason == 'max_tokens':
        raise ValueError('La respuesta quedó incompleta. Pida algo más acotado.')
    text = next((b.text for b in msg.content if b.type == 'text'), '')
    u = msg.usage
    lee = getattr(u, 'cache_read_input_tokens', 0) or 0
    esc = getattr(u, 'cache_creation_input_tokens', 0) or 0
    usd = (u.input_tokens * PRECIO['entrada'] + u.output_tokens * PRECIO['salida']
           + lee * PRECIO['cache_lee'] + esc * PRECIO['cache_escribe']) / 1e6
    costo = {'usd': round(usd, 3), 'enviados': u.input_tokens + lee + esc, 'en_memoria': lee, 'recibidos': u.output_tokens}
    print(f"  llamada · {costo['enviados']} enviados ({lee} en memoria) · {costo['recibidos']} recibidos · ≈ USD {costo['usd']}")
    return json.loads(text), costo


NORMAS_SCHEMA = {'type': 'object', 'properties': {'markdown': {'type': 'string'}},
                 'required': ['markdown'], 'additionalProperties': False}


def sugerir_normas(b):
    """Propone normas a partir de lo que el experimento hace distinto. Nunca cambia el libro: escribe notas en _lab/notas/."""
    titulo = b.get('titulo') or 'Experimento'
    fuera = b.get('fuera') or []
    if DEMO:
        md = (f'# Notas para el libro · {titulo}\n\n> Modo de demostración: estas notas no vienen de la API.\n\n'
              '## Lo que se aparta de las normas\n\n'
              + ('\n'.join('- ' + x for x in fuera) or '- Nada: la exploración está dentro de norma.') + '\n')
    else:
        texto = ('Revise este experimento del Laboratorio y proponga, solo si hacen falta, normas nuevas o ajustes a normas '
                 'existentes del Libro de Marca de Keyons. No cambie nada: escriba notas para que la diseñadora decida. '
                 'Markdown en español, trato de «usted». Para cada propuesta: título, norma relacionada (código KYN-MRK-…) '
                 'o «nueva», propósito, composición, invariantes y el ejemplo del experimento que la motiva. '
                 'Termine con lo que NO conviene volver norma.\n\n'
                 f'Título: {titulo}\nLo que se aparta de las normas: {"; ".join(fuera) or "nada"}\n\n'
                 f'<html>\n{b.get("html", "")}\n</html>\n<css>\n{b.get("css", "")}\n</css>')
        out, costo = llamar(texto, NORMAS_SCHEMA)
        md = out['markdown'] + f"\n\n---\nCosto aproximado de esta sugerencia: USD {costo['usd']}.\n"
    os.makedirs(NOTAS, exist_ok=True)
    nombre = slug(titulo) + '-' + datetime.datetime.now().strftime('%Y%m%d-%H%M') + '.md'
    with io.open(os.path.join(NOTAS, nombre), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(md)
    return {'markdown': md, 'archivo': '_lab/notas/' + nombre}


def demo(pedido, cambio):
    """Un ejemplo fijo para probar el flujo sin clave ni costo."""
    titulo = 'Ejemplo de demostración'
    html = ('<main class="lx-main"><p class="lx-kicker">Demostración</p>'
            '<h1 class="lx-h2" style="margin:var(--lab-2) 0 var(--lab-8)">Así llega una construcción</h1>'
            '<div class="lx-group lx-cols"><section class="lx-card lx-kpi"><p class="lx-meta">Pedido</p>'
            f'<p class="lx-p">{H_.escape(pedido[:140]) or "Sin pedido"}</p></section><section class="lx-card lx-kpi"><p class="lx-meta">Cambio</p>'
            f'<p class="lx-p">{H_.escape(cambio[:140]) or "Ninguno todavía"}</p></section></div>'
            '<div class="lx-card lx-alert lx-alert--info lx-section"><svg class="lx-i" viewBox="0 0 24 24" aria-hidden="true">'
            '<circle cx="12" cy="12" r="9"/><path d="M12 11v5.5M12 7.5v.5"/></svg><div><b>Modo de demostración</b>'
            '<p class="lx-small">Inicie el servidor sin --demo y con su clave para construir de verdad.</p></div></div></main>')
    return {'titulo': titulo, 'resumen': 'Respuesta fija del modo de demostración.', 'html': html, 'css': '', 'js': '', 'normas': []}


def propuestas_index():
    os.makedirs(PROP, exist_ok=True)
    items = []
    for f in sorted(os.listdir(PROP)):
        if f.endswith('.json') and f != 'index.json':
            x = json.load(io.open(os.path.join(PROP, f), encoding='utf-8'))
            items.append({k: x.get(k, '') for k in ('id', 'titulo', 'estado', 'actualizado', 'origen')})
    with io.open(os.path.join(PROP, 'index.json'), 'w', encoding='utf-8', newline='\n') as fh:
        json.dump({'propuestas': items}, fh, ensure_ascii=False, indent=2)
    return items


class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def log_message(self, fmt, *args):
        if '/api/' in (args[0] if args else ''):
            super().log_message(fmt, *args)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def j(self, code, obj):
        b = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def body(self):
        n = int(self.headers.get('Content-Length') or 0)
        return json.loads(self.rfile.read(n) or b'{}')

    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        if not u.path.startswith('/api/lab/'):
            return super().do_GET()
        q = urllib.parse.parse_qs(u.query)
        try:
            if u.path == '/api/lab/estado':
                ok_key, ok_sdk = api_key(), sdk()
                aviso = '' if DEMO or (ok_key and ok_sdk) else (
                    'Falta el SDK: ejecute pip install anthropic y reinicie el servidor.' if not ok_sdk else
                    'Falta la clave: defina ANTHROPIC_API_KEY o cree .env.local con ANTHROPIC_API_KEY=... y reinicie.')
                return self.j(200, {'generar': DEMO or (ok_key and ok_sdk), 'guardar': True,
                                    'modo': 'demo' if DEMO else 'api', 'modelo': MODEL, 'aviso': aviso})
            if u.path == '/api/lab/lista':
                os.makedirs(EXP, exist_ok=True)
                exps = []
                for f in os.listdir(EXP):
                    if f.endswith('.json'):
                        x = json.load(io.open(os.path.join(EXP, f), encoding='utf-8'))
                        exps.append({k: x.get(k, '') for k in ('id', 'titulo', 'estado', 'actualizado', 'origen')})
                exps.sort(key=lambda x: x['actualizado'], reverse=True)
                return self.j(200, {'experimentos': exps, 'propuestas': propuestas_index()})
            if u.path == '/api/lab/experimento':
                i = slug((q.get('id') or [''])[0])
                return self.j(200, json.load(io.open(os.path.join(EXP, i + '.json'), encoding='utf-8')))
        except FileNotFoundError:
            return self.j(404, {'error': 'No existe ese experimento.'})
        except Exception as e:  # noqa: BLE001
            return self.j(500, {'error': str(e)})
        return self.j(404, {'error': 'Ruta desconocida.'})

    def do_POST(self):
        u = urllib.parse.urlparse(self.path)
        try:
            b = self.body()
            if u.path == '/api/lab/generar':
                return self.j(200, generar(b))
            if u.path == '/api/lab/normas':
                return self.j(200, sugerir_normas(b))
            if u.path == '/api/lab/guardar':
                os.makedirs(EXP, exist_ok=True)
                i = slug(b.get('id') or b.get('titulo'))
                if not b.get('id'):
                    base, n = i, 2
                    while os.path.exists(os.path.join(EXP, i + '.json')):
                        i, n = f'{base}-{n}', n + 1
                p = os.path.join(EXP, i + '.json')
                prev = json.load(io.open(p, encoding='utf-8')) if os.path.exists(p) else {}
                keep = ('titulo', 'estado', 'decision', 'kit', 'pedido', 'datos', 'origen', 'html', 'css', 'js', 'ex')
                x = {'id': i, 'creado': prev.get('creado') or now(), 'actualizado': now(), **{k: b.get(k, '') for k in keep}}
                with io.open(p, 'w', encoding='utf-8', newline='\n') as fh:
                    json.dump(x, fh, ensure_ascii=False, indent=2)
                return self.j(200, {'id': i})
            if u.path == '/api/lab/proponer':
                i = slug(b.get('id'))
                x = json.load(io.open(os.path.join(EXP, i + '.json'), encoding='utf-8'))
                x['estado'] = x.get('estado') or 'Enviado a revisión'
                x.pop('datos', None)   # los datos propios no se publican
                os.makedirs(PROP, exist_ok=True)
                with io.open(os.path.join(PROP, i + '.json'), 'w', encoding='utf-8', newline='\n') as fh:
                    json.dump(x, fh, ensure_ascii=False, indent=2)
                propuestas_index()
                return self.j(200, {'id': i})
        except FileNotFoundError:
            return self.j(404, {'error': 'No existe ese experimento.'})
        except ValueError as e:
            return self.j(400, {'error': str(e)})
        except Exception as e:  # noqa: BLE001
            name = type(e).__name__
            hint = {'AuthenticationError': 'La clave no es válida.', 'RateLimitError': 'Límite de uso alcanzado; espere un momento.',
                    'APIConnectionError': 'Sin conexión con la API.'}.get(name, '')
            return self.j(500, {'error': hint or f'{name}: {e}'})
        return self.j(404, {'error': 'Ruta desconocida.'})


if __name__ == '__main__':
    api_key()
    class Srv(http.server.ThreadingHTTPServer):
        request_queue_size = 128   # el navegador pide muchos archivos a la vez; con la cola de 5 se cortan conexiones
        daemon_threads = True
    srv = Srv(('127.0.0.1', PORT), H)
    modo = 'demostración' if DEMO else ('API de Claude · ' + MODEL if api_key() and sdk() else 'sin construir (falta clave o SDK)')
    print(f'Laboratorio de Interfaces · http://127.0.0.1:{PORT}/sistema-diseno/laboratorio.html · {modo}')
    srv.serve_forever()
