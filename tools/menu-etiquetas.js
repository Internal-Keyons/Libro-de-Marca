/* Detector de etiquetas del menú lateral · Guía 05 «Sistema de diagramación» (toda etiqueta del menú se ve completa, en un renglón).
   Uso: en una página del libro servida localmente, abrir la consola y ejecutar
     await import('/tools/menu-etiquetas.js').then((m) => m.revisar())
   Mide cada capítulo e ítem del índice del libro abierto (st o t) con la letra y el ancho reales del menú.
   Devuelve [] si todas caben; si no, la lista de etiquetas que se cortarían, para crearles una etiqueta corta. */

export function revisar(doc = document) {
  const side = doc.querySelector('#side');
  const nav = doc.defaultView.KEYONS_NAV;
  if (!side || !nav) return ['Sin menú lateral en esta página'];
  const vis = (sel) => [...side.querySelectorAll(sel)].filter((e) => e.offsetParent);
  const it = vis('.nav-item__t')[0];
  const ch = vis('.nav-ch__btn *').find((e) => !e.children.length && e.textContent.trim().length > 2 && !/^\d+$/.test(e.textContent.trim()));
  const fuera = [];
  const prueba = (e, t) => {
    if (!e) return false;
    const antes = e.textContent;
    e.textContent = t;
    const r = e.scrollWidth > e.clientWidth + 1 || e.getClientRects().length > 1;
    e.textContent = antes;
    return r;
  };
  for (const a of nav) {
    for (const c of a.ch || []) {
      if (prueba(ch, c.st || c.t)) fuera.push({ tipo: 'capítulo', n: c.n, etiqueta: c.st || c.t });
      for (const i of c.items || []) if (prueba(it, i.st || i.t)) fuera.push({ tipo: 'ítem', n: c.n, etiqueta: i.st || i.t, titulo: i.t });
    }
  }
  return fuera;
}
