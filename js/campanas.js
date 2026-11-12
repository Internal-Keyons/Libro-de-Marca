/* ═══════════════════════════════════════════════════════════════
   KEYONS · LIBRO DE MARCA · Archivo de campañas (21.3)
   Lee js/campanas-datos.js. Vista de tarjetas con buscador y tres filtros
   (Tipo de campaña, Año y Estado) y una ficha por campaña.
   Los materiales enlazan a su fuente original (Galería, Texturas, Íconos,
   Plantillas, Presentaciones): el archivo no duplica archivos.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  const box = document.querySelector('[data-camp]');
  if (!box) return;
  const ROOT = (document.body.dataset.root || '.').replace(/\/$/, '');
  const url = (h) => ROOT + '/' + h;
  const esc = (s) => String(s == null ? '' : s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const DATA = (window.KEYONS_CAMPANAS || []).slice().sort((a, b) => (b.anio || 0) - (a.anio || 0));
  const FUENTE = {
    galeria: (m) => ({ h: 'recursos/galeria.html?q=' + encodeURIComponent(String(m.ref || '').toLowerCase()), lib: 'Galería de imágenes' }),
    texturas: (m) => ({ h: 'recursos/texturas.html#' + (m.ref || 'texturas'), lib: 'Texturas' }),
    iconos: (m) => ({ h: 'recursos/iconos.html#' + (m.ref || 'catalogo'), lib: 'Íconos' }),
    plantillas: (m) => ({ h: 'recursos/plantillas.html#' + (m.ref || 'plantillas'), lib: 'Plantillas' }),
    presentaciones: (m) => ({ h: 'aplicaciones/presentaciones.html#' + (m.ref || 'plantillas'), lib: 'Presentaciones' }),
    campana: (m) => ({ h: m.archivo || '', lib: 'Archivo de la campaña', dl: true }),
  };
  const grid = box.querySelector('.camp__grid'), vacio = box.querySelector('.camp__empty'), sinDatos = box.querySelector('.camp__none');
  const q = box.querySelector('.camp__q'), count = box.querySelector('.camp__count'), panel = box.querySelector('.fpop__panel');
  const GRUPOS = [['tipo', 'Tipo de campaña'], ['anio', 'Año'], ['estado', 'Estado']];
  const sel = { tipo: new Set(), anio: new Set(), estado: new Set() };

  /* Filtros: las opciones salen de las campañas registradas */
  panel.innerHTML = '<div class="fpop__row fpop__all"><button type="button" data-call aria-pressed="true">Todas las campañas</button></div>'
    + GRUPOS.map(([g, t]) => {
      const vals = [...new Set(DATA.map((c) => String(c[g] || '')).filter(Boolean))].sort((a, b) => (g === 'anio' ? b - a : a.localeCompare(b, 'es')));
      return `<p class="fpop__h">${t}</p><div class="fpop__row">${vals.length ? vals.map((v) => `<button type="button" data-cf="${g}:${esc(v)}">${esc(v)}</button>`).join('') : '<span class="camp__nada">Sin opciones todavía</span>'}</div>`;
    }).join('');

  const fecha = (d) => { if (!d) return ''; const [y, m, dd] = d.split('-'); return `${dd}/${m}/${y}`; };
  const portada = (c) => `<span class="camp__img"${c.portada ? ` style="background-image:url('${esc(url(c.portada))}')"` : ''}></span>`;
  const tarjeta = (c, i) => `<button class="camp__c" type="button" data-ci="${i}">${portada(c)}<span class="camp__t">${esc(c.nombre)}</span>`
    + `<span class="camp__m">${esc(c.tipo)} · ${esc(c.anio)}</span><span class="camp__s">${esc(c.estado)}</span></button>`;
  const dibujar = () => {
    const v = (q.value || '').trim().toLowerCase();
    const n = Object.values(sel).reduce((t, x) => t + x.size, 0);
    box.querySelector('.fpop__val').textContent = n ? `· ${n}` : '';
    const call = panel.querySelector('[data-call]'); if (call) call.setAttribute('aria-pressed', String(!n));
    const vis = DATA.map((c, i) => [c, i]).filter(([c]) => Object.keys(sel).every((g) => !sel[g].size || sel[g].has(String(c[g])))
      && (!v || [c.id, c.nombre, c.tipo, c.anio, c.estado, c.concepto, c.objetivo, (c.canales || []).join(' '), c.responsable].join(' ').toLowerCase().includes(v)));
    grid.innerHTML = vis.map(([c, i]) => tarjeta(c, i)).join('');
    count.textContent = `${vis.length} ${vis.length === 1 ? 'campaña' : 'campañas'}`;
    sinDatos.hidden = DATA.length > 0;
    vacio.hidden = !DATA.length || vis.length > 0;
    grid.hidden = !vis.length;
  };
  q.addEventListener('input', dibujar);
  panel.addEventListener('click', (e) => {
    const b = e.target.closest('button'); if (!b) return;
    if (b.hasAttribute('data-call')) { Object.values(sel).forEach((x) => x.clear()); panel.querySelectorAll('[data-cf]').forEach((o) => o.setAttribute('aria-pressed', 'false')); }
    else if (b.dataset.cf) { const [g, v] = b.dataset.cf.split(':'); if (sel[g].has(v)) sel[g].delete(v); else sel[g].add(v); b.setAttribute('aria-pressed', String(sel[g].has(v))); }
    dibujar();
  });
  box.querySelectorAll('[data-cclear]').forEach((b) => b.addEventListener('click', () => {
    Object.values(sel).forEach((x) => x.clear()); q.value = ''; panel.querySelectorAll('[data-cf]').forEach((o) => o.setAttribute('aria-pressed', 'false')); dibujar();
  }));

  /* Ficha de la campaña */
  const dlg = box.querySelector('.camp__dlg'), cuerpo = dlg.querySelector('.camp__ficha');
  let antes = null;
  const abrir = (c) => {
    const fila = (k, v) => (v ? `<div><dt>${k}</dt><dd>${v}</dd></div>` : '');
    const mats = (c.materiales || []).map((m) => {
      const f = (FUENTE[m.fuente] || (() => ({ h: '', lib: '' })))(m);
      return `<li>${f.h ? `<a class="xref" href="${esc(url(f.h))}"${f.dl ? ' download' : ''}>${esc(m.t)}</a>` : esc(m.t)}<span>${esc(f.lib)}</span></li>`;
    }).join('');
    cuerpo.innerHTML = `<p class="camp__k">${esc(c.id)}</p><h3 class="camp__h" id="camp-t">${esc(c.nombre)}</h3><dl class="camp__d">`
      + fila('Concepto', esc(c.concepto)) + fila('Objetivo', esc(c.objetivo))
      + fila('Fechas', [fecha(c.inicio), fecha(c.fin)].filter(Boolean).join(' – ')) + fila('Canales', esc((c.canales || []).join(', ')))
      + fila('Responsable', esc(c.responsable)) + fila('Estado', esc(c.estado)) + fila('Condiciones de uso', esc(c.condiciones))
      + `</dl>${mats ? `<p class="camp__k">Materiales relacionados</p><ul class="camp__mat">${mats}</ul>` : ''}`;
    antes = document.activeElement; dlg.hidden = false; dlg.querySelector('[data-cclose]').focus();
  };
  const cerrar = () => { dlg.hidden = true; if (antes) antes.focus(); };
  grid.addEventListener('click', (e) => { const b = e.target.closest('[data-ci]'); if (b) abrir(DATA[Number(b.dataset.ci)]); });
  dlg.addEventListener('click', (e) => { if (e.target === dlg || e.target.closest('[data-cclose]')) cerrar(); });
  document.addEventListener('keydown', (e) => {
    if (dlg.hidden) return;
    if (e.key === 'Escape') cerrar();
    if (e.key === 'Tab') {   // el foco queda dentro de la ficha
      const f = [...dlg.querySelectorAll('a, button')]; if (!f.length) return;
      if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
      else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
    }
  });
  dibujar();
})();
