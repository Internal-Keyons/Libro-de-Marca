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
  const href = (c) => ROOT + '/' + ((c.items.find((it) => it.href) || {}).href || NAV[0].href).split('#')[0];
  const ST = { v: ['vigente', 'Vigente'], b: ['borrador', 'Borrador'], p: ['pendiente', 'Contenido pendiente'], e: ['estructura', 'Estructura definida'], r: ['revision', 'En revisión'], d: ['descontinuado', 'Descontinuado'] };

  /* Índice de la portada: una tarjeta por módulo, con el mismo marcado que las áreas del Libro de Marca */
  /* Mismo orden de color que las áreas del Libro de Marca: Azul Noche, Azul Cielo, Salmón Tierra, Salmón Atardecer */
  const COLORS = ['noche', 'cielo', 'salmon', 'atardecer'];
  const GO = '<svg viewBox="0 0 16 16" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8h10M9.2 4.2 13 8l-3.8 3.8"/></svg>';
  const dot = (s) => `<span class="dot dot--${(ST[s] || ST.p)[0]}" title="${(ST[s] || ST.p)[1]}" aria-label="${(ST[s] || ST.p)[1]}"></span>`;
  document.querySelectorAll('[data-sd-cards]').forEach((box) => {
    box.innerHTML = mods.map((c, i) => {
      const caps = c.items.filter((it) => !it.idx);
      return `
      <article class="area">
        <div class="area__color grad grad--${c.color || COLORS[i % COLORS.length]}" aria-hidden="true"></div>
        <div class="area__body">
          <h3 class="t-h3">${esc(c.t)}</h3>
          <p class="t-sm">${esc(c.d)}</p>
          <ul class="area__list">${caps.map((it) => `<li><a href="${ROOT}/${it.href}"><span>${it.n}</span>${esc(it.st || it.t)}${dot(it.s)}</a></li>`).join('')}</ul>
          <div class="area__foot"><span class="paren">(${caps.length} ${caps.length === 1 ? 'capítulo' : 'capítulos'})</span>
            <a class="btn-icon" href="${href(c)}" aria-label="Abrir ${esc(c.t)}">${GO}</a></div>
        </div>
      </article>`;
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
