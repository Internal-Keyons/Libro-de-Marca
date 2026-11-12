/* Detector de líneas dobles · reglas-visuales 3.5 («entre dos bloques hay una sola línea divisoria»).
   Uso: en una página del libro servida localmente, abrir la consola y ejecutar
     await import('/tools/lineas-dobles.js').then((m) => m.revisarLibro())
   Abre cada página del menú en un marco oculto de 1440 px y lista los pares de líneas horizontales
   que quedan una cerca de la otra sin texto ni imagen entre ellas. */

const ANCHO = 1440;
const DISTANCIA = 96;   // dos líneas a menos de esta distancia, sin nada entre ellas, cuentan como dobles

function lineas(doc) {
  const out = [];
  const raiz = doc.querySelector('main') || doc.body;
  raiz.querySelectorAll('*').forEach((e) => {
    const cs = doc.defaultView.getComputedStyle(e);
    if (cs.display === 'none' || cs.visibility === 'hidden' || e.closest('[hidden],.side,.toc,nav,.portal,.hero')) return;
    const r = e.getBoundingClientRect();
    if (r.width < 120) return;
    /* Una caja, con borde a ambos lados, no es una línea divisoria */
    if (['Left', 'Right'].every((s) => parseFloat(cs[`border${s}Width`]) > 0 && cs[`border${s}Style`] !== 'none')) return;
    for (const lado of ['Top', 'Bottom']) {
      const w = parseFloat(cs[`border${lado}Width`]);
      if (w > 0 && cs[`border${lado}Style`] !== 'none' && cs[`border${lado}Color`] !== 'rgba(0, 0, 0, 0)') {
        out.push({ y: lado === 'Top' ? r.top : r.bottom, x1: r.left, x2: r.right, el: e, lado });
      }
    }
    if (e.tagName === 'HR') out.push({ y: r.top, x1: r.left, x2: r.right, el: e, lado: 'hr' });
  });
  return out.sort((a, b) => a.y - b.y);
}

/* Todo lo que se ve (texto e imágenes), medido una sola vez por página */
function contenido(doc) {
  const raiz = doc.querySelector('main') || doc.body, out = [];
  const w = doc.createTreeWalker(raiz, NodeFilter.SHOW_TEXT, { acceptNode: (n) => (/\S/.test(n.data) ? 1 : 2) });
  const rg = doc.createRange();
  while (w.nextNode()) {
    rg.selectNodeContents(w.currentNode);
    const r = rg.getBoundingClientRect();
    if (r.height) out.push([r.top, r.bottom, r.left, r.right]);
  }
  raiz.querySelectorAll('img,svg,canvas,video,picture').forEach((m) => {
    const r = m.getBoundingClientRect();
    if (r.height > 8) out.push([r.top, r.bottom, r.left, r.right]);
  });
  return out;
}

const hayContenido = (C, y1, y2, x1, x2) => C.some(([t, b, l, r]) => b > y1 + 1 && t < y2 - 1 && r > x1 && l < x2);

function nombre(e) {
  const sec = e.closest('section[id]');
  const c = typeof e.className === 'string' && e.className ? '.' + e.className.trim().split(/\s+/).join('.') : e.tagName.toLowerCase();
  return (sec ? '#' + sec.id + ' ' : '') + c;
}

export function revisarDoc(doc) {
  const L = lineas(doc), C = contenido(doc), dobles = [];
  for (let i = 0; i < L.length; i++) {
    for (let j = i + 1; j < L.length && L[j].y - L[i].y < DISTANCIA; j++) {
      const a = L[i], b = L[j];
      if (b.y - a.y < 1) continue;
      const solape = Math.min(a.x2, b.x2) - Math.max(a.x1, b.x1);
      if (solape < 0.6 * Math.min(a.x2 - a.x1, b.x2 - b.x1)) continue;
      if (hayContenido(C, a.y, b.y, Math.max(a.x1, b.x1), Math.min(a.x2, b.x2))) continue;
      dobles.push({ separacion: Math.round(b.y - a.y), arriba: nombre(a.el) + ' ' + a.lado, abajo: nombre(b.el) + ' ' + b.lado });
      break;
    }
  }
  return dobles;
}

export async function revisarLibro() {
  const raiz = new URL('/', location.href);
  const paginas = [...new Set((window.KEYONS_NAV || []).flatMap((a) => [a.href, ...a.ch.flatMap((c) => c.items.filter((it) => it.href).map((it) => it.href.split('#')[0]))]).filter(Boolean))];
  const informe = {};
  for (const p of paginas) {
    const f = document.createElement('iframe');
    f.style.cssText = `position:fixed;left:-${ANCHO + 100}px;top:0;width:${ANCHO}px;height:900px;border:0`;
    document.body.appendChild(f);
    await new Promise((ok) => { f.onload = ok; f.src = new URL(p, raiz).href + '?v=' + Date.now(); });
    await new Promise((ok) => setTimeout(ok, 1200));
    const d = f.contentDocument;
    d.querySelectorAll('.reveal,[data-reveal],.is-hidden-until-seen').forEach((e) => e.classList.add('is-in'));
    const r = revisarDoc(d);
    if (r.length) informe[p] = r;
    f.remove();
  }
  return informe;
}
