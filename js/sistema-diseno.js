/* ═══════════════════════════════════════════════════════════════
   KEYONS · SISTEMA DE DISEÑO · comportamiento propio
   Se carga después de js/libro.js, que ya arma cabecera, lateral,
   buscador y paginador con js/nav-sistema-diseno.js.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  const NAV = window.KEYONS_NAV || [];
  const mods = NAV[0] ? NAV[0].ch : [];
  const ROOT = (document.body.dataset.root || '.').replace(/\/$/, '');
  const PAGE = document.body.dataset.page || '';
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const href = (c) => ROOT + '/' + ((c.items.find((it) => it.href) || {}).href || NAV[0].href);

  /* Retícula de doce columnas: cada columna es un módulo y lleva a él */
  document.querySelectorAll('[data-sd-cols]').forEach((box) => {
    box.innerHTML = mods.map((c) => {
      const h = href(c), cur = h.endsWith('/' + PAGE);
      return `<a class="sd-col${cur ? ' is-cur' : ''}" href="${h}" data-n="${c.n}" data-t="${esc(c.t)}" aria-label="${c.n} ${esc(c.t)}"${cur ? ' aria-current="page"' : ''}>${c.n}</a>`;
    }).join('');
    const cap = document.querySelector('[data-sd-cap]');
    if (!cap) return;
    const rest = cap.innerHTML;
    const show = (a) => { cap.innerHTML = a ? `<span>${a.dataset.n}</span>${a.dataset.t}` : rest; };
    box.addEventListener('mouseover', (e) => show(e.target.closest('.sd-col')));
    box.addEventListener('mouseleave', () => show(null));
    box.addEventListener('focusin', (e) => show(e.target.closest('.sd-col')));
    box.addEventListener('focusout', () => show(null));
  });

  /* Índice de módulos de la portada, desde el mismo mapa que el lateral */
  const ST = { v: ['vigente', 'Vigente'], b: ['borrador', 'Borrador'], p: ['pendiente', 'Por definir'] };
  document.querySelectorAll('[data-sd-index]').forEach((box) => {
    box.innerHTML = mods.map((c) => {
      const [k, t] = ST[c.s || 'p'];
      return `<a class="sd-idx__r" href="${href(c)}"><span class="sd-idx__n">${c.n}</span><span class="sd-idx__t">${esc(c.t)}</span>`
        + `<span class="sd-idx__d">${esc(c.d)}</span><span class="sd-idx__s"><span class="dot dot--${k}" aria-hidden="true"></span>${t}</span></a>`;
    }).join('');
  });

  /* Códigos provisionales de módulo */
  const GO = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9.2 4.2 13 8l-3.8 3.8"/></svg>';
  document.querySelectorAll('[data-sd-codes]').forEach((box) => {
    box.innerHTML = mods.map((c) => `<a href="${href(c)}"><span class="sd-refs__id">KYN-SDI-${c.k}</span><span class="sd-refs__t">${c.n} ${esc(c.t)}</span>${GO}</a>`).join('');
  });

  /* Ejemplo interactivo: el mismo componente en los cuatro contextos de interfaz */
  document.querySelectorAll('[data-sd-demo]').forEach((demo) => {
    const stage = demo.querySelector('[data-ctx]');
    demo.querySelectorAll('[data-ctx-set]').forEach((b) => b.addEventListener('click', () => {
      stage.dataset.ctx = b.dataset.ctxSet;
      demo.querySelectorAll('[data-ctx-set]').forEach((o) => o.setAttribute('aria-pressed', String(o === b)));
    }));
  });
})();
