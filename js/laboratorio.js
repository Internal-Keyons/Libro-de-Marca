/* ═══════════════════════════════════════════════════════════════
   KEYONS · LABORATORIO DE INTERFACES
   Para cada prueba [data-lab]:
   · Vista final / Vista técnica, sobre el mismo componente: la técnica mide el DOM
     real (tamaño, radios, rellenos, espacios, tipografía, color) y lo traduce a tokens.
   · Escritorio / Tableta / Móvil: el escenario toma el ancho del dispositivo y los
     componentes se adaptan a él por consultas de contenedor.
   · Comprobaciones calculadas en cada cambio: legibilidad, proximidad, geometría,
     columnas, áreas táctiles, foco, desbordes y continuidad de la tarea.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  const root = getComputedStyle(document.documentElement);
  const px = (v) => parseFloat(v) || 0;

  /* ── Tokens: valor medido → nombre ── */
  const SP = {}, RAD = {}, COL = {};
  ['s1', 's2', 's3', 's4', 's5', 's6', 's8', 's10', 's12', 's16', 's20', 's24', 's32'].forEach((k) => { SP[px(root.getPropertyValue('--' + k))] = k; });
  ['r-micro', 'r-control', 'r-component', 'r-card', 'r-block'].forEach((k) => { RAD[px(root.getPropertyValue('--' + k))] = k; });
  const probe = document.createElement('i'); probe.style.display = 'none'; document.body.appendChild(probe);
  ['noche', 'blanco', 'puro', 'cielo', 'salmon', 'atardecer', 'cielo-100', 'cielo-200', 'est-verde', 'est-mostaza', 'est-terracota', 'est-cielo', 'est-gris', 'gris-2', 'gris-3']
    .forEach((k) => { probe.style.color = `var(--k-${k})`; const c = getComputedStyle(probe).color; if (!COL[c]) COL[c] = 'k-' + k; });
  probe.remove();
  const tSp = (v) => (v === 0 ? '0' : SP[v] ? `${SP[v]}` : `${Math.round(v)}`);
  const tRad = (v, h) => (v === 0 ? '0' : v >= h / 2 - .5 && v > 40 ? 'pill' : RAD[v] ? RAD[v] : `${Math.round(v)}`);

  const W = { esc: 'Escritorio', tab: 'Tableta', mov: 'Móvil' };
  const ICON = {
    ok: '<svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="9" fill="currentColor"/><path d="M6 10.4 8.7 13 14 7.5" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    no: '<svg viewBox="0 0 20 20" aria-hidden="true"><rect x="1" y="1" width="18" height="18" fill="currentColor"/><path d="M10 5.5v5.5M10 13.8v.2" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>',
    na: '<svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="8.25" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M6.5 10h7" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
  };
  const visible = (el) => { if (el.closest('.kdd:not(.is-open) .kdd__list')) return false; const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0 && getComputedStyle(el).visibility !== 'hidden'; };
  const INTER = 'button, a[href], input:not([type="hidden"]), select, textarea, [role="option"], [tabindex]';
  const controls = (st) => [...st.querySelectorAll(INTER)].filter((el) => !el.closest('.ilab__ov') && !el.closest('label[hidden]') && el.tagName !== 'SELECT' && visible(el));
  /* Un control táctil es su etiqueta cuando la envuelve (opción de radio) */
  const target = (el) => (el.type === 'radio' || el.type === 'checkbox') && el.closest('label') ? el.closest('label') : el;

  /* ── Comprobaciones ── */
  function checks(st, w, base) {
    const sr = st.getBoundingClientRect(), out = [];
    const all = [...st.querySelectorAll('*')].filter((el) => !el.closest('.ilab__ov') && visible(el));

    // 1 · Legibilidad: el texto más pequeño y el de lectura
    let minF = 99, bodyF = 0;
    all.forEach((el) => {
      if (![...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())) return;
      const f = px(getComputedStyle(el).fontSize); minF = Math.min(minF, f);
      if (el.matches('p, input, td, [role="cell"]')) bodyF = Math.max(bodyF, f);
    });
    out.push(['Legibilidad', minF >= 12, `Texto mínimo de ${minF} px${bodyF ? `; lectura en ${bodyF} px` : ''}.`]);

    // 2 · Proximidad: los espacios entre elementos salen de la escala de 4, y las partes de
    // un grupo quedan más cerca entre sí que los grupos (salvo contenedores con borde o fondo propio)
    const bounded = (k) => { const kc = getComputedStyle(k); return kc.backgroundColor !== 'rgba(0, 0, 0, 0)' || kc.boxShadow !== 'none' || px(kc.borderTopWidth) > 0; };
    const flow = (c) => c.display.includes('grid') || c.display.includes('flex');
    const atom = '.btn, .badge, label, .kdd__btn, .kdd__list, .kdd__o, input, figure';
    let off4 = [], inv = 0, n = 0;
    all.forEach((el) => {
      if (el.matches(atom) || el.closest('.btn, .badge, .kdd__list')) return;
      const c = getComputedStyle(el);
      if (flow(c)) ['rowGap', 'columnGap'].forEach((k) => { const v = px(c[k]); if (v > 0 && (k === 'rowGap' || c.display.includes('flex') || el.children.length > 1)) { n++; if (v % 4) off4.push(v); } });
      if (el.matches('[data-geo], .lb-card, .lb-field__e')) ['paddingTop', 'paddingLeft'].forEach((k) => { const v = px(c[k]); if (v) { n++; if (v % 4) off4.push(v); } });
      if (flow(c) && px(c.rowGap) > 0) {
        const kid = [...el.children].find((k) => { const kc = getComputedStyle(k); return flow(kc) && px(kc.rowGap) > px(c.rowGap) && k.children.length > 1 && !k.matches(atom) && !bounded(k); });
        if (kid) inv++;
      }
    });
    out.push(['Proximidad', off4.length === 0 && inv === 0, off4.length || inv
      ? `${off4.length ? `Espacios fuera de la escala de 4: ${[...new Set(off4)].join(', ')} px. ` : ''}${inv ? `${inv} grupos con partes más separadas que el conjunto.` : ''}`.trim()
      : `${n} espacios en la escala de 4; cada grupo, más unido que la distancia entre grupos.`]);

    // 3 · Geometría: aislado recto, conjunto con exteriores rectos e interiores curvos, controles curvos
    const geo = [];
    st.querySelectorAll('[data-geo="solo"]').forEach((el) => { const c = getComputedStyle(el); geo.push([c.borderTopLeftRadius, c.borderTopRightRadius, c.borderBottomRightRadius, c.borderBottomLeftRadius].every((v) => px(v) === 0)); });
    st.querySelectorAll('[data-geo="group"]').forEach((g) => {
      const kids = [...g.children].filter(visible), rs = kids.map((k) => k.getBoundingClientRect());
      const row = rs.length > 1 && Math.abs(rs[0].top - rs[1].top) < 2;
      kids.forEach((k, i) => {
        const c = getComputedStyle(k), tl = px(c.borderTopLeftRadius), tr = px(c.borderTopRightRadius), br = px(c.borderBottomRightRadius), bl = px(c.borderBottomLeftRadius);
        const first = i === 0, last = i === kids.length - 1;
        if (row) geo.push((first ? tl === 0 && bl === 0 : tl > 0 && bl > 0) && (last ? tr === 0 && br === 0 : tr > 0 && br > 0));
        else geo.push((first ? tl === 0 && tr === 0 : tl > 0 && tr > 0) && (last ? bl === 0 && br === 0 : bl > 0 && br > 0));
      });
    });
    st.querySelectorAll('.btn').forEach((b) => { if (!visible(b) || b.classList.contains('is-hover')) return; const h = b.getBoundingClientRect().height; geo.push(px(getComputedStyle(b).borderTopLeftRadius) >= h / 2 - .5); });
    st.querySelectorAll('.lb-field__i, .kdd__btn').forEach((f) => { if (visible(f)) geo.push(px(getComputedStyle(f).borderTopLeftRadius) === px(root.getPropertyValue('--r-control'))); });
    out.push(geo.length ? ['Geometría', geo.every(Boolean), `${geo.filter(Boolean).length} de ${geo.length} piezas con su geometría: contenedores rectos o en conjunto, controles curvos.`] : ['Geometría', null, 'Sin contenedores ni controles que evaluar.']);

    // 4 · Columnas: cuántas columnas usa la retícula principal y qué ancho conservan
    const cols = (el) => getComputedStyle(el).gridTemplateColumns.split(' ').filter(Boolean).map(px);
    const grids = all.filter((el) => getComputedStyle(el).display === 'grid' && el.children.length > 1 && !el.matches(atom) && !el.closest('.kdd'));
    const multi = grids.filter((g) => cols(g).length > 1).sort((a, b) => cols(b).length - cols(a).length);
    const main = multi[0] || st.querySelector('.lb-group, .lb-fields, .lb-select, .lb-table__r, .lb-grid');
    if (main && getComputedStyle(main).display === 'grid') {
      const cs = cols(main), measured = !main.matches('[data-grid], .lb-space, .lb-table__r');
      const narrow = measured ? [...main.children].filter((k) => visible(k) && k.getBoundingClientRect().width < 140).length : 0;
      out.push(['Columnas', narrow === 0, `${cs.length} ${cs.length === 1 ? 'columna' : 'columnas'} de ${Math.round(cs[0])} px${narrow ? `; ${narrow} piezas por debajo de 140 px` : ''}.`]);
    } else {
      const fl = all.find((el) => getComputedStyle(el).flexWrap === 'wrap');
      out.push(fl ? ['Columnas', true, 'Fila flexible: las piezas pasan al renglón siguiente sin comprimirse.'] : ['Columnas', null, 'Una sola pieza: sin columnas que adaptar.']);
    }

    // 5 · Áreas táctiles
    const ctl = controls(st), min = w === 'esc' ? 24 : 44;
    const small = ctl.filter((el) => { const t = target(el); return t.offsetHeight < min - .5 || t.offsetWidth < min - .5; }); // tamaño de diseño, sin la escala del estado presionado
    out.push(ctl.length ? ['Áreas táctiles', small.length === 0, `${ctl.length - small.length} de ${ctl.length} controles de ${min} px o más${w === 'esc' ? ' (puntero)' : ' (táctil)'}.`] : ['Áreas táctiles', null, 'Sin controles en esta prueba.']);

    // 6 · Foco: orden de tabulación igual al de lectura, sin tabindex positivos
    const foc = ctl.filter((el) => !el.disabled && el.tabIndex >= 0);
    const pos = foc.filter((el) => el.tabIndex > 0).length;
    let order = true;
    for (let i = 1; i < foc.length; i++) { const a = foc[i - 1].getBoundingClientRect(), b = foc[i].getBoundingClientRect(); if (b.top < a.top - 4 && b.left <= a.left) order = false; }
    out.push(foc.length ? ['Foco', pos === 0 && order, `${foc.length} elementos enfocables, en el orden de lectura. Anillo de 2 px en Azul Noche.`] : ['Foco', null, 'Sin elementos enfocables.']);

    // 7 · Sin desbordes
    const over = all.filter((el) => { const r = el.getBoundingClientRect(); return r.right > sr.right + 1 || r.left < sr.left - 1 || (el.scrollWidth > el.clientWidth + 1 && getComputedStyle(el).overflowX !== 'visible' && !el.matches('.kdd__list')); });
    out.push(['Sin desbordes', over.length === 0, over.length ? `${over.length} elementos salen del ancho de ${W[w].toLowerCase()}.` : `Todo cabe en ${Math.round(sr.width)} px.`]);

    // 8 · Continuidad de la tarea: los mismos controles en cada pantalla
    const cont = !ctl.length && !base ? null : base == null ? true : ctl.length >= base;
    out.push(['Continuidad de la tarea', cont, cont === null ? 'Sin tareas que completar en esta prueba.' : base == null ? `${ctl.length} controles disponibles: referencia para tableta y móvil.` : `${ctl.length} de ${base} controles disponibles, igual que en escritorio.`]);
    return out;
  }

  /* ── Vista técnica ── */
  function spec(st, ov) {
    ov.innerHTML = '';
    if (!st.classList.contains('is-tec')) return;
    const sr = st.getBoundingClientRect();
    st.querySelectorAll('[data-spec]').forEach((el) => {
      if (!visible(el)) return;
      const r = el.getBoundingClientRect(), c = getComputedStyle(el), inner = !!el.parentElement.closest('[data-spec]');
      const parts = [`${Math.round(r.width)}×${Math.round(r.height)}`];
      const rads = [c.borderTopLeftRadius, c.borderTopRightRadius, c.borderBottomRightRadius, c.borderBottomLeftRadius].map(px);
      if (rads.some((v) => v)) parts.push('r ' + (rads.every((v) => v === rads[0]) ? tRad(rads[0], r.height) : rads.map((v) => tRad(v, r.height)).join('·')));
      else if (el.matches('[data-geo], .lb-card')) parts.push('r 0');
      const pt = px(c.paddingTop), pl = px(c.paddingLeft);
      if (pt || pl) parts.push('p ' + (pt === pl ? tSp(pt) : `${tSp(pt)}/${tSp(pl)}`));
      const g = px(c.rowGap) || px(c.columnGap);
      if (g && (c.display.includes('grid') || c.display.includes('flex'))) parts.push('gap ' + tSp(g));
      if ([...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim()) || el.matches('input, .btn, .badge')) parts.push(`${px(c.fontSize)}/${c.fontWeight}`);
      const bg = COL[c.backgroundColor]; if (bg) parts.push(bg);
      const box = document.createElement('div');
      box.className = 'ilab__box' + (inner ? ' is-inner' : '');
      box.style.cssText = `left:${r.left - sr.left}px;top:${r.top - sr.top}px;width:${r.width}px;height:${r.height}px`;
      box.innerHTML = `<span class="ilab__tag">${parts.join(' · ')}</span>`;
      ov.appendChild(box);
      /* Retícula: las columnas reales y su medianil */
      if (el.matches('[data-grid]')) {
        let x = r.left - sr.left; const gap = px(c.columnGap);
        c.gridTemplateColumns.split(' ').map(px).forEach((w) => { const col = document.createElement('div'); col.className = 'ilab__col'; col.style.cssText = `left:${x}px;width:${w}px;top:${r.top - sr.top}px;height:${r.height}px;bottom:auto`; ov.appendChild(col); x += w + gap; });
      }
    });
  }

  /* ── Montaje de cada prueba ── */
  document.querySelectorAll('[data-lab]').forEach((sec) => {
    const st = sec.querySelector('[data-stage]');
    const frame = document.createElement('div');
    frame.className = 'ilab__frame'; frame.dataset.w = 'esc';
    st.before(frame); frame.appendChild(st);
    const ov = document.createElement('div'); ov.className = 'ilab__ov'; ov.setAttribute('aria-hidden', 'true'); st.appendChild(ov);
    const bar = document.createElement('div');
    bar.className = 'ilab__bar';
    bar.innerHTML = '<div class="ilab__seg" role="group" aria-label="Vista"><button type="button" data-v="fin" aria-pressed="true">Vista final</button><button type="button" data-v="tec" aria-pressed="false">Vista técnica</button></div>'
      + '<div class="ilab__seg" role="group" aria-label="Pantalla">' + Object.keys(W).map((k, i) => `<button type="button" data-w="${k}" aria-pressed="${i === 0}">${W[k]}</button>`).join('') + '</div>'
      + '<span class="ilab__w" aria-live="polite"></span>';
    frame.before(bar);
    const list = document.createElement('ul'); list.className = 'ilab__checks'; list.setAttribute('aria-label', 'Comprobaciones');
    frame.after(list);
    const wl = bar.querySelector('.ilab__w');
    let base = null, raf = 0;
    const run = () => {
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        const w = frame.dataset.w;
        if (w === 'esc') base = controls(st).length;
        const res = checks(st, w, w === 'esc' ? null : base);
        list.innerHTML = res.map(([t, ok, d]) => `<li class="${ok === null ? 'is-na' : ok ? 'is-ok' : 'is-no'}">${ICON[ok === null ? 'na' : ok ? 'ok' : 'no']}<b>${t}</b><span>${d}</span></li>`).join('');
        wl.textContent = `Ancho de prueba: ${Math.round(frame.getBoundingClientRect().width)} px`;
        spec(st, ov);
      });
    };
    bar.addEventListener('click', (e) => {
      const b = e.target.closest('button'); if (!b) return;
      b.parentElement.querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
      if (b.dataset.v) st.classList.toggle('is-tec', b.dataset.v === 'tec');
      if (b.dataset.w) frame.dataset.w = b.dataset.w;
      run();
    });
    frame.addEventListener('transitionend', run);
    new ResizeObserver(run).observe(st);
    st.addEventListener('click', () => setTimeout(run, 30));
    st.addEventListener('input', run);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(run);
    run();
  });
})();
