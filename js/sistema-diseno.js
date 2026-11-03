/* ═══════════════════════════════════════════════════════════════
   KEYONS · SISTEMA DE DISEÑO · comportamiento propio
   Se carga después de js/libro.js, que ya arma cabecera, lateral,
   buscador, página de área y paginador con js/nav-sistema-diseno.js.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  const NAV = window.KEYONS_NAV || [];
  const mods = NAV[0] ? NAV[0].ch : [];
  const ROOT = (document.body.dataset.root || '.').replace(/\/$/, '');
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const href = (c) => ROOT + '/' + ((c.items.find((it) => it.href) || {}).href || NAV[0].href);
  const ST = { v: ['vigente', 'Vigente'], b: ['borrador', 'Borrador'], p: ['pendiente', 'Por definir'] };

  /* Índice de la portada: la rejilla numerada de Marca, desde el mismo mapa que el lateral */
  document.querySelectorAll('[data-sd-index]').forEach((box) => {
    box.innerHTML = mods.map((c) => {
      const [k, t] = ST[c.s || 'p'];
      return `<div><a href="${href(c)}"><div class="cols__n">${c.n}</div><p class="t-h4">${esc(c.t)}</p><p class="t-sm">${esc(c.d)}</p></a>`
        + `<p class="sd-st"><span class="dot dot--${k}" aria-hidden="true"></span>${t}</p></div>`;
    }).join('');
  });

  /* Códigos provisionales de módulo, con la lista de normas de Marca */
  document.querySelectorAll('[data-sd-codes]').forEach((box) => {
    box.innerHTML = mods.map((c) => `<a class="kidx__r" href="${href(c)}"><b>KYN-SDI-${c.k}</b><span class="kidx__n">${c.n}</span><span class="kidx__t">${esc(c.t)}</span></a>`).join('');
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
