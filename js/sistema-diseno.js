/* ═══════════════════════════════════════════════════════════════
   KEYONS · SISTEMA DE DISEÑO · comportamiento propio
   Se carga después de js/libro.js, que ya arma cabecera, lateral, tarjetas,
   buscador, páginas de área y paginador con js/nav-sistema-diseno.js.
   Aquí: códigos de módulo de la plantilla y ejemplo interactivo.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  const NAV = window.KEYONS_NAV || [];
  const mods = NAV;
  const ROOT = (document.body.dataset.root || '.').replace(/\/$/, '');
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const href = (a) => ROOT + '/' + a.href;

  /* Códigos provisionales de módulo, con la lista de normas de Marca */
  document.querySelectorAll('[data-sd-codes]').forEach((box) => {
    box.innerHTML = mods.map((c, i) => `<a class="kidx__r" href="${href(c)}"><b>KYN-SDI-${c.k}</b><span class="kidx__n">${String(i + 1).padStart(2, '0')}</span><span class="kidx__t">${esc(c.full || c.t)}</span></a>`).join('');
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
