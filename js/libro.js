/* ═══════════════════════════════════════════════════════════════
   KEYONS · MANUAL DE MARCA · comportamiento
   Funciona abriendo los archivos directamente, sin servidor.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  const NAV = window.KEYONS_NAV || [];
  const body = document.body;
  const ROOT = (body.dataset.root || '.').replace(/\/$/, '');
  const PAGE = body.dataset.page || '';
  const AREA = body.dataset.area || '';
  const IS_HOME = body.classList.contains('is-home');
  const url = (h) => ROOT + '/' + h;
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const $ = (id) => document.getElementById(id);

  const ic = (d, cls = '') => `<svg class="${cls}" viewBox="0 0 16 16" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${d}</svg>`;
  const I = {
    search: '<circle cx="7" cy="7" r="4.6"/><path d="m10.4 10.4 3.2 3.2"/>',
    chev: '<path d="m6 3.5 4.5 4.5L6 12.5"/>',
    right: '<path d="M3 8h10M9.2 4.2 13 8l-3.8 3.8"/>',
    left: '<path d="M13 8H3M6.8 4.2 3 8l3.8 3.8"/>',
    up: '<path d="M8 13V3M4.2 6.8 8 3l3.8 3.8"/>',
    check: '<path d="M3 8.5 6.2 12 13 4.5"/>'
  };
  const LOGO = '<svg viewBox="0 0 1080 1080" aria-hidden="true"><path d="M640.8,418.74h-114.75c6.09,15.64,13.97,28.56,24.93,39.18,7.37.01,15.88-8.08,24.73-7.55v41.57c-8.85.62-17.36-7.41-24.74-7.41-10.44,9.97-18.92,23.62-24.87,39.21h114.7v39.38h-201.52c-.03-1.13-.05-2.49-.05-3.63,0-43.3,35.25-72.17,69.63-88.27-34.11-15.75-69.63-44.93-69.63-88.23,0-1.14.02-2.51.05-3.63h201.52v39.38Z"/><path d="M425.72,559.46c0,1.13-.02,2.55-.05,3.67h-77.4c-1.47-18.79-10.36-50.84-27.66-72.3h-31.42v72.3h-65.05v-247.85h65.05v136.29h31.43c17.3-21.46,26.18-53.43,27.65-72.22h77.4c.03,1.13.05,2.47.05,3.6,0,43.31-35.94,72.76-69.79,88.25,34.21,16.01,69.79,44.95,69.79,88.26Z"/><path d="M640.79,581.04v183.68h-65.24l-71.08-111.51v111.51h-65.24v-183.68h65.24l71.08,111.51v-111.51h65.24Z"/><path d="M855.83,563.13v-183.78h-77.48c-1.59,21.81-2.8,69.74-23.27,75.25-20.47-5.5-21.68-53.44-23.27-75.25h-77.51s0,2.99,0,2.99c0,55.66,45.12,83.15,100.77,83.15h0c23.14,0,44.46-4.75,61.46-14.31v72.65h0v23.09c-4.38-12.94-12.47-22.91-29.44-23.19h-132.8v39.39h201.54-.02Z"/><path d="M719.09,597.28v55.91s114.19,0,114.19,0c12.47,0,22.57,10.17,22.57,22.71v66.1c0,12.54-10.1,22.71-22.57,22.71h-178.98v-39.37h107.45c16.9.28,24.95,10.17,29.31,23.13v-55.91h-115.07c-11.98,0-21.69-9.77-21.69-21.83v-67.88c0-12.05,9.71-21.82,21.69-21.82h179.86v39.37h-107.45c-16.9-.28-24.95-10.17-29.31-23.13Z"/><path d="M245.84,581.04c-11.98,0-21.69,9.71-21.69,21.69v134.99h0v5.3c0,11.98,9.71,21.69,21.69,21.69h158.18c11.98,0,21.69-9.71,21.69-21.69v-140.29c0-11.98-9.71-21.69-21.69-21.69h-158.18ZM289.2,725.44v-104.94h71.49v104.85l-71.49.09Z"/></svg>';
  const STATUS = { v: 'Vigente', b: 'Borrador', p: 'Por definir' };
  const SKEY = { v: 'vigente', b: 'borrador', p: 'pendiente' };
  const dot = (s = 'p') => `<span class="dot dot--${SKEY[s]}" title="${STATUS[s]}" aria-label="${STATUS[s]}"></span>`;
  const slug = (c) => 'cap-' + c.n;
  const base = (h) => (h || '').split('#')[0];
  const hash = (h) => (h || '').split('#')[1] || '';

  /* Índice plano: buscador y paginador */
  const flat = [];
  const seq = [];
  NAV.forEach((a) => {
    seq.push({ t: a.t, href: a.href, path: 'Área' });
    a.ch.forEach((c) => {
      let sub = '';
      c.items.forEach((it) => {
        if (it.sub) { sub = it.sub; return; }
        if (it.grp) return;
        const path = [a.t, c.n + ' ' + c.t, sub].filter(Boolean).join(' · ');
        flat.push({ t: it.t, href: it.href, s: it.s || 'p', path });
        if (it.href && !seq.some((x) => base(x.href) === base(it.href))) seq.push({ t: hash(it.href) ? (sub || c.t) : it.t, href: base(it.href), path: c.n + ' ' + c.t });
      });
    });
  });
  flat.unshift(...NAV.map((a) => ({ t: a.t, href: a.href, s: 'b', path: 'Área del manual' })));

  /* ─── Cabecera · misma especificación que el sitio web ─── */
  const top = $('topbar');
  if (top) {
    /* El logotipo lleva al inicio: el menú solo nombra las áreas */
    const links = NAV.map((a) => ({ t: a.t, h: a.href, cur: a.id === AREA }));
    const linkHtml = (cls) => links.map((l) => `<a class="${cls}" href="${url(l.h)}"${l.cur ? ' aria-current="true"' : ''}>${l.t}</a>`).join('');
    /* Nubes: anchos 200–420 px, opacidad 20–45 %, desenfoque 12–24 px, recorrido 44–82 s */
    const clouds = [[200, .32, 12, 44, 8], [420, .2, 24, 82, -6], [280, .45, 16, 58, 30], [340, .26, 20, 70, -18], [240, .38, 14, 52, 46], [380, .22, 22, 76, 14]]
      .map(([w, o, b, d, y], i) => `<span class="haze" style="width:${w}px;height:${Math.round(w * .38)}px;top:${y}px;opacity:${o};filter:blur(${b + 10}px);animation-duration:${d}s;animation-delay:-${(i * 13.7 + d * .37).toFixed(1)}s"></span>`).join('');
    top.className = 'hdr' + (IS_HOME ? ' hdr--home' : '');
    top.innerHTML = `
      <div class="hdr__bg">${IS_HOME ? `<div class="hdr__clouds" aria-hidden="true">${clouds}</div>` : ''}</div>
      <div class="hdr__in">
        <nav class="hdr__links" aria-label="Áreas del manual">${linkHtml('hdr__link')}</nav>
        <a class="hdr__logo" href="${url('index.html')}" aria-label="Keyons · volver a la portada">${LOGO}</a>
        <div class="hdr__right">
          <button class="hdr__search" type="button" data-search aria-label="Buscar en el manual (Ctrl K)">${ic(I.search)}<span>Buscar</span><kbd>Ctrl K</kbd></button>
        </div>
        <button class="hdr__burger" type="button" aria-label="Abrir menú" aria-expanded="false">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path class="b1" d="M4 7h16"/><path class="b2" d="M4 12h16"/><path class="b3" d="M4 17h16"/></svg>
        </button>
      </div>
      <div class="hdr__panel">
        <nav aria-label="Áreas del manual">${linkHtml('')}</nav>
        <div class="hdr__panel-foot"><button class="hdr__panel-search" type="button" data-search>${ic(I.search)}Buscar en el manual</button></div>
      </div>`;
    const burger = top.querySelector('.hdr__burger');
    const setOpen = (o) => { top.classList.toggle('is-open', o); burger.setAttribute('aria-expanded', o); burger.setAttribute('aria-label', o ? 'Cerrar menú' : 'Abrir menú'); };
    burger.addEventListener('click', () => setOpen(!top.classList.contains('is-open')));
    top.querySelector('.hdr__panel').addEventListener('click', (e) => { if (e.target.closest('a,button')) setOpen(false); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setOpen(false); });
    if (IS_HOME) {
      const hero = document.querySelector('.hero');
      const check = () => top.classList.toggle('is-solid', !hero || hero.getBoundingClientRect().bottom <= top.offsetHeight);
      addEventListener('scroll', check, { passive: true });
      check();
    }
  }

  /* ─── Referencias que llevan a su sección ───
     Cada «6.15», «capítulo 11» o «(14)» del texto se vuelve un enlace a esa sección. */
  {
    const sx = document.createElement('script');
    sx.src = (document.body.dataset.root || '.') + '/js/secciones.js';
    sx.onload = () => {
      const S = window.KEYONS_SECS || {}, C = window.KEYONS_CAPS || {}, root = (document.body.dataset.root || '.') + '/';
      const N = window.KEYONS_NORMAS || [], byH = {}, byId = {};
      N.forEach((o) => { byH[o.h] = o; byId[o.id] = o; });
      const base = decodeURI(new URL(root, location.href).pathname), here = decodeURI(location.pathname).slice(base.length);
      document.querySelectorAll('section.ed[id] > .ed__label').forEach((lb) => {
        const o = byH[`${here}#${lb.parentElement.id}`];
        if (!o || o.e !== 'vigente') return;
        const num = lb.firstElementChild;
        num.dataset.n = num.textContent; num.textContent = o.id; num.classList.add('ed__code');
        num.dataset.copy = o.id; num.dataset.copyMsg = 'ID copiado · ' + o.id; num.title = 'Copiar el ID de esta norma';
      });
      document.querySelectorAll('[data-normas]').forEach((box) => {
        const list = box.querySelector('.kidx__list'), q = box.querySelector('.kidx__q');
        const draw = (key) => {
        const rows = [...N].sort((a, b) => (a.e === b.e ? (key === 't' ? a.t.localeCompare(b.t, 'es') : a.n.split('.').map(Number).reduce((x, y, i) => x || y - (b.n.split('.').map(Number)[i] || 0), 0)) : a.e === 'vigente' ? -1 : 1));
        list.innerHTML = rows.map((o) => `<a class="kidx__r${o.e === 'vigente' ? '' : ' is-off'}" href="${root}${o.h}" data-q="${(o.id + ' ' + o.n + ' ' + o.t).toLowerCase()}"><b>${o.id}</b><span class="kidx__n">${o.n}</span><span class="kidx__t">${o.t}</span>${o.e === 'vigente' ? '' : '<span class="kidx__e">[DESCONTINUADA]</span>'}</a>`).join('');
        q.dispatchEvent(new Event('input'));
        };
        box.querySelectorAll('[data-ks]').forEach((b) => b.addEventListener('click', () => {
          box.querySelectorAll('[data-ks]').forEach((o) => o.setAttribute('aria-pressed', String(o === b))); draw(b.dataset.ks);
        }));
        q.addEventListener('input', () => { const v = q.value.trim().toLowerCase(); list.querySelectorAll('.kidx__r').forEach((r) => { r.hidden = !!v && !r.dataset.q.includes(v); }); });
        draw('id');
      });
      const area = document.querySelector('.content') || document.body;
      const skip = 'a, button, svg, code, pre, script, style, .ed__label, .crumbs, .portal, h1, .chart, .side, nav, label, [role="tab"], .kcode, [data-normas]';
      const re = /(KYN-MRK-[A-Z]{2,4}-\d{3})|(cap[ií]tulos?\s+)(\d{1,2})(?!\d|[.,]\d)|(?<![\d.,\w])(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)(?!\d|,\d|\s?%|\.\d|:\d)|\((\d{1,2})\)/g;
      const walk = document.createTreeWalker(area, NodeFilter.SHOW_TEXT, { acceptNode: (n) => (n.parentElement.closest(skip) || !/\d/.test(n.data)) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT });
      const nodes = []; while (walk.nextNode()) nodes.push(walk.currentNode);
      nodes.forEach((n) => {
        const t = n.data; let m, last = 0, frag = null;
        re.lastIndex = 0;
        while ((m = re.exec(t))) {
          let href = null, pre = '', label = m[0], post = '';
          if (m[1] && byId[m[1]]) { href = byId[m[1]].h; label = m[1]; }
          else if (m[3] && C[String(+m[3])]) { href = C[String(+m[3])]; pre = m[2]; label = m[3]; }
          else if (m[4] && S[m[4]]) { href = S[m[4]]; label = (byH[href] && byH[href].e === 'vigente') ? byH[href].id : m[4]; }
          else if (m[5] && C[String(+m[5])]) { href = C[String(+m[5])]; pre = '('; label = m[5]; post = ')'; }
          if (!href) continue;
          frag = frag || document.createDocumentFragment();
          frag.appendChild(document.createTextNode(t.slice(last, m.index) + pre));
          const a = document.createElement('a'); a.className = 'xref'; a.href = root + href; a.textContent = label;
          frag.appendChild(a); if (post) frag.appendChild(document.createTextNode(post));
          last = m.index + m[0].length;
        }
        if (frag) { frag.appendChild(document.createTextNode(t.slice(last))); n.replaceWith(frag); }
      });
    };
    document.head.appendChild(sx);
  }

  /* ─── Cielo con Ráfaga (js/keyons-cielo.js) ───
     El mismo módulo en la portada y en cada encabezado de capítulo; solo cambia el cielo de cada fondo.
     Regla del módulo: no se reescribe el shader ni el campo de ráfaga, solo la configuración. */
  const cielos = [];
  const heroEl = document.querySelector('.hero');
  if (heroEl) cielos.push([heroEl, 'mediodia', 'portada']);
  document.querySelectorAll('.portal').forEach((p) => {
    if (p.matches('.portal--photo, .portal--img')) return;
    const sky = p.matches('.portal--cielo') ? 'mediodia' : p.matches('.portal--salmon') ? 'atardecer' : 'noche';
    cielos.push([p, sky, document.body.dataset.page || location.pathname, true]);
  });
  if (cielos.length) {
    const s = document.createElement('script');
    s.src = (document.body.dataset.root || '.') + '/js/keyons-cielo.js';
    /* En los subencabezados el viento avanza 1,5 altos de encabezado por minuto, sin importar su proporción ni su cielo:
       antes un encabezado bajo corría y uno de noche casi no se movía. Solo se ajusta la configuración, no el módulo. */
    const SUB_SPEED = 1.5;
    s.onload = () => cielos.forEach(([el, sky, seed, sub], i) => {
      let key = sky;
      if (sub) {
        const K = window.KeyonsCielo.SKIES, r = el.getBoundingClientRect(), asp = r.width / Math.max(r.height, 1);
        key = `${sky}-sub${i}`;
        K[key] = Object.assign({}, K[sky], { ws: SUB_SPEED / asp, clouds: Object.assign({}, K[sky].clouds, sky === 'noche' ? { alpha: .72 } : {}) });
      }
      el.classList.add('has-cielo'); window.KeyonsCielo.mount(el, { sky: key, seed });
    });
    document.head.appendChild(s);
  }

  /* 11.5 · al tocar un número se destacan la parte y su nota */
  document.querySelectorAll('[data-anat]').forEach((box) => {
    const set = (k) => {
      box.classList.toggle('has-on', !!k);
      box.querySelectorAll('[data-k]').forEach((el) => el.classList.toggle('is-on', !!k && el.dataset.k === k));
    };
    const pick = (e) => { const el = e.target.closest('[data-k]'); if (el) set(el.dataset.k); };
    box.addEventListener('pointerover', pick);
    box.addEventListener('click', pick);
    box.addEventListener('focusin', pick);
    box.addEventListener('pointerleave', () => set(''));
    box.addEventListener('focusout', (e) => { if (!box.contains(e.relatedTarget)) set(''); });
  });

  /* Volver arriba */
  document.addEventListener('click', (e) => {
    const t = e.target.closest('[data-top]');
    if (!t) return;
    e.preventDefault();
    scrollTo({ top: 0, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  });

  /* Índice de palabras: al pasar sobre una palabra se enciende su definición */
  document.querySelectorAll('[data-index]').forEach((ix) => {
    const notes = document.getElementById(ix.dataset.index);
    if (!notes) return;
    const set = (n) => {
      [ix, notes].forEach((el) => el.classList.toggle('is-hover', !!n));
      ix.querySelectorAll('[data-n]').forEach((w) => w.classList.toggle('is-on', w.dataset.n === n));
      notes.querySelectorAll('[data-n]').forEach((w) => w.classList.toggle('is-on', w.dataset.n === n));
    };
    [ix, notes].forEach((el) => {
      el.addEventListener('mouseover', (e) => { const w = e.target.closest('[data-n]'); set(w ? w.dataset.n : null); });
      el.addEventListener('mouseleave', () => set(null));
    });
  });

  /* Selector de palabras (3.3): una lista que crece y un panel con la palabra elegida */
  document.querySelectorAll('[data-lexi]').forEach((lx) => {
    const tabs = [...lx.querySelectorAll('[role="tab"]')];
    const panel = lx.querySelector('.lexi__panel');
    const w = lx.querySelector('.lexi__w'), d = lx.querySelector('.lexi__d'), c = lx.querySelector('.lexi__count');
    const pad = (n) => String(n).padStart(2, '0');
    let cur = 0;
    const pick = (i, focus) => {
      cur = (i + tabs.length) % tabs.length;
      tabs.forEach((t, k) => { t.setAttribute('aria-selected', k === cur); t.tabIndex = k === cur ? 0 : -1; });
      w.textContent = tabs[cur].dataset.w; d.textContent = tabs[cur].dataset.d;
      c.textContent = `(${pad(cur + 1)} / ${pad(tabs.length)})`;
      panel.classList.remove('is-swap'); void panel.offsetWidth; panel.classList.add('is-swap');
      const list = tabs[cur].parentElement, t = tabs[cur];
      if (list.scrollHeight > list.clientHeight) list.scrollTop = Math.max(0, t.offsetTop - list.offsetTop - list.clientHeight / 2 + t.offsetHeight / 2);
      if (list.scrollWidth > list.clientWidth) list.scrollLeft = Math.max(0, t.offsetLeft - list.offsetLeft - 8);
      if (focus) t.focus({ preventScroll: true });
    };
    lx.addEventListener('click', (e) => {
      const t = e.target.closest('[role="tab"]');
      if (t) return pick(tabs.indexOf(t));
      const s = e.target.closest('[data-step]');
      if (s) pick(cur + Number(s.dataset.step));
    });
    lx.addEventListener('keydown', (e) => {
      if (!e.target.matches('[role="tab"]')) return;
      const k = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 }[e.key];
      if (k) { e.preventDefault(); pick(cur + k, true); }
    });
    tabs.forEach((t, k) => { t.setAttribute('aria-selected', k === 0); t.tabIndex = k === 0 ? 0 : -1; });
  });

  /* Códigos de color en RGB (por defecto), HEX o CMYK */
  {
    let mode = 'hex';
    try { mode = localStorage.getItem('k-fmt3') || 'hex'; } catch (_) {}
    const rgbOf = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));
    const val = (h, m) => {
      if (m === 'hex') return h.toUpperCase();
      const [r, g, b] = rgbOf(h);
      if (m === 'rgb') return `${r}, ${g}, ${b}`;
      const R = r / 255, G = g / 255, B = b / 255, K = 1 - Math.max(R, G, B);
      if (K >= 1) return 'C0 M0 Y0 K100';
      const c = (v) => Math.round(((1 - v - K) / (1 - K)) * 100);
      return `C${c(R)} M${c(G)} Y${c(B)} K${Math.round(K * 100)}`;
    };
    const apply = () => {
      document.querySelectorAll('[data-hex]').forEach((el) => {
        const v = val(el.dataset.hex, mode);
        el.dataset.copy = mode === 'rgb' ? `rgb(${v})` : v;
        el.querySelectorAll('.cv').forEach((c) => { c.textContent = v; });
      });
      document.querySelectorAll('[data-fmt]').forEach((b) => b.setAttribute('aria-pressed', b.dataset.fmt === mode));
    };
    document.addEventListener('click', (e) => {
      const b = e.target.closest('[data-fmt]');
      if (!b) return;
      mode = b.dataset.fmt;
      try { localStorage.setItem('k-fmt3', mode); } catch (_) {}
      apply();
    });
    if (document.querySelector('[data-hex]')) apply();
  }

  /* Versiones del logotipo: tres combinaciones, copia del SVG y descarga */
  {
    const COMBOS = [
      { fg: '#10122A', bg: '#F4F4F4', a: 'Azul Noche', b: 'Blanco Keyons', slug: 'azul-noche' },
      { fg: '#F4F4F4', bg: '#10122A', a: 'Blanco Keyons', b: 'Azul Noche', slug: 'blanco-keyons' },
      { fg: '#729BDD', bg: '#F4F4F4', a: 'Azul Cielo', b: 'Blanco Keyons', slug: 'azul-cielo' },
    ];
    const NAMES = { logo: 'logotipo', iso: 'isotipo', est: 'logotipo-insignia' };
    const save = (blob, name) => {
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob); a.download = name;
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(a.href), 1500);
    };
    document.querySelectorAll('[data-combos]').forEach((card) => {
      const sym = document.getElementById('k-' + card.dataset.mark);
      if (!sym) return;
      const [x, y, w, h] = sym.getAttribute('viewBox').split(/\s+/).map(Number);
      const stage = card.querySelector('.vstage'), mark = card.querySelector('.vstage__mark');
      const nameEl = card.querySelector('.vbar__name'), dots = card.querySelectorAll('.vbar__dots i'), count = card.querySelector('.vbar__count');
      const svgOf = (c, bg, pad, W, H) => {
        const vb = `${x - pad} ${y - pad} ${w + 2 * pad} ${h + 2 * pad}`;
        const size = W ? ` width="${W}" height="${H}"` : '';
        const rect = bg ? `<rect x="${x - pad}" y="${y - pad}" width="${w + 2 * pad}" height="${h + 2 * pad}" fill="${c.bg}"/>` : '';
        return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}"${size}>${rect}<g fill="${c.fg}">${sym.innerHTML}</g></svg>`;
      };
      let i = 0, t = null, hold = false, vis = false;
      const set = (n) => {
        i = (n + COMBOS.length) % COMBOS.length;
        const c = COMBOS[i];
        stage.style.backgroundColor = c.bg; stage.style.color = c.fg;
        stage.classList.toggle('is-dark', c.bg === '#10122A');
        dots[0].style.background = c.fg; dots[1].style.background = c.bg;
        nameEl.innerHTML = `${c.a} <span>sobre ${c.b}</span>`;
        count.textContent = `0${i + 1} / 0${COMBOS.length}`;
        mark.dataset.copy = svgOf(c, false, 0);
        mark.dataset.copyMsg = `SVG copiado · ${card.dataset.name} en ${c.a}`;
        clearTimeout(t);
        if (vis && !hold && !matchMedia('(prefers-reduced-motion: reduce)').matches) t = setTimeout(() => set(i + 1), 4500);
      };
      card.addEventListener('click', (e) => {
        const s = e.target.closest('[data-cstep]');
        if (s) return set(i + Number(s.dataset.cstep));
        const d = e.target.closest('[data-dl]');
        if (!d) return;
        const c = COMBOS[i], file = `keyons-${NAMES[card.dataset.mark]}-${c.slug}`;
        if (d.dataset.dl === 'svg') return save(new Blob([svgOf(c, false, 0)], { type: 'image/svg+xml' }), file + '.svg');
        const jpg = d.dataset.dl === 'jpg', pad = jpg ? w * 0.25 : w * 0.04;
        const W = 2400, H = Math.round(W * (h + 2 * pad) / (w + 2 * pad));
        const img = new Image();
        const src = URL.createObjectURL(new Blob([svgOf(c, jpg, pad, W, H)], { type: 'image/svg+xml' }));
        img.onload = () => {
          const cv = document.createElement('canvas'); cv.width = W; cv.height = H;
          const ctx = cv.getContext('2d');
          if (jpg) { ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H); }
          ctx.drawImage(img, 0, 0, W, H);
          URL.revokeObjectURL(src);
          cv.toBlob((b) => save(b, `${file}.${jpg ? 'jpg' : 'png'}`), jpg ? 'image/jpeg' : 'image/png', 0.95);
        };
        img.src = src;
      });
      card.addEventListener('mouseenter', () => { hold = true; clearTimeout(t); });
      card.addEventListener('mouseleave', () => { hold = false; set(i); });
      card.addEventListener('focusin', () => { hold = true; clearTimeout(t); });
      card.addEventListener('focusout', () => { hold = false; set(i); });
      if ('IntersectionObserver' in window) new IntersectionObserver(([en]) => { vis = en.isIntersecting; set(i); }, { threshold: .5 }).observe(card);
      set(0);
    });
  }

  /* Tipografía: los pesos se prueban sobre la muestra */
  document.querySelectorAll('[data-weights]').forEach((list) => {
    const plate = list.closest('.plate');
    const targets = plate.querySelectorAll('.plate__glyph, .plate__abc');
    const btns = [...list.querySelectorAll('[data-w]')];
    let cur = btns.find((b) => b.getAttribute('aria-pressed') === 'true') || btns[0];
    const show = (b) => targets.forEach((el) => { el.style.fontWeight = b.dataset.w; el.style.fontStyle = b.hasAttribute('data-i') ? 'italic' : 'normal'; });
    btns.forEach((b) => {
      b.addEventListener('click', () => { cur = b; btns.forEach((o) => o.setAttribute('aria-pressed', o === b)); show(b); });
    });
    show(cur);
  });

  /* Probador tipográfico */
  document.querySelectorAll('[data-tester]').forEach((tb) => {
    const LV = {
      display: ['tsx--display', 'TASA Orbiter 500 · 52–128 px · espaciado −4 %'],
      title: ['tsx--title', 'Jakarta 500 · 30–44 px · espaciado −3 % · Gris titular'],
      lead: ['tsx--lead', 'Jakarta 400 · 18–20 px · interlineado 1.55'],
      body: ['tsx--body', 'Jakarta 400 · 16–17 px · interlineado 1.65'],
      kicker: ['kicker tsx--kicker', 'TASA Orbiter 500 · 13 px · mayúsculas · espaciado +8 %'],
    };
    const inp = tb.querySelector('.tester__in'), out = tb.querySelector('.tester__out'), meta = tb.querySelector('.tester__meta');
    let lv = 'display';
    const draw = () => { out.textContent = inp.value || ' '; out.className = 'tester__out ' + LV[lv][0]; meta.textContent = LV[lv][1]; };
    inp.addEventListener('input', draw);
    tb.querySelectorAll('[data-lv]').forEach((b) => b.addEventListener('click', () => {
      lv = b.dataset.lv; tb.querySelectorAll('[data-lv]').forEach((o) => o.setAttribute('aria-pressed', o === b)); draw();
    }));
    draw();
  });

  /* Escalas tonales: flechas que avanzan de a varias fichas */
  document.addEventListener('click', (e) => {
    const b = e.target.closest('[data-sstep]');
    if (!b) return;
    const row = b.closest('.scale').querySelector('.scale__row');
    row.scrollBy({ left: Number(b.dataset.sstep) * row.clientWidth * .75, behavior: 'smooth' });
  });

  /* Catálogo de íconos: elegir, copiar, colorear y descargar */
  document.querySelectorAll('[data-icat]').forEach((cat) => {
    const tiles = [...cat.querySelectorAll('.ict')];
    const big = cat.querySelector('.icat__big'), nm = cat.querySelector('.icat__name'), file = cat.querySelector('.icat__file');
    const rev = cat.querySelector('.icat__rev'), q = cat.querySelector('.icat__q'), count = cat.querySelector('.icat__count');
    const heads = [...cat.querySelectorAll('.icat__h')], chipBar = cat.querySelector('.icat__chips'), view = cat.querySelector('.icat__view');
    let fcat = '';
    let col = '#10122A', bg = '#F4F4F4', cur = tiles.find((t) => t.dataset.n === 'inicio') || tiles[0];
    const svgOf = (t, size) => {
      let s = t.querySelector('svg').outerHTML
        .replace('class="ic"', 'xmlns="http://www.w3.org/2000/svg"').replace(' aria-hidden="true"', '')
        .replace(/ pathLength="1"/g, '').replace(/currentColor/g, col)
        .replace(/stroke="#F4F4F4" class="ko-s"/g, `stroke="${bg}"`).replace(/fill="#F4F4F4" class="ko-f"/g, `fill="${bg}"`);
      if (size) s = s.replace('<svg ', `<svg width="${size}" height="${size}" `);
      return s;
    };
    const save = (blob, name) => {
      const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = name;
      document.body.appendChild(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(a.href), 1500);
    };
    const select = (t, doCopy) => {
      cur = t;
      tiles.forEach((x) => x.classList.toggle('is-sel', x === t));
      big.innerHTML = t.querySelector('svg').outerHTML;
      big.classList.remove('is-anim'); void big.offsetWidth; big.classList.add('is-anim');
      nm.textContent = t.dataset.n; file.textContent = `icon-${t.dataset.n}-32.svg`;
      if (rev) rev.hidden = !t.classList.contains('is-rev');
      if (doCopy) {
        copy(svgOf(t), `SVG copiado · ${t.dataset.n}`);
        const r = view.getBoundingClientRect();
        if (r.bottom < 80 || r.top > innerHeight) view.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    };
    cat.addEventListener('click', (e) => {
      const t = e.target.closest('.ict'); if (t) return select(t, true);
      const c = e.target.closest('[data-ic]');
      if (c) {
        col = c.dataset.ic; bg = c.dataset.bg;
        cat.style.setProperty('--ic-c', col); cat.style.setProperty('--ic-ko', bg);
        cat.classList.toggle('is-dark', bg === '#10122A');
        cat.querySelectorAll('[data-ic]').forEach((o) => o.setAttribute('aria-pressed', o === c));
        return;
      }
      if (e.target.closest('[data-icopy]')) return copy(svgOf(cur), `SVG copiado · ${cur.dataset.n}`);
      const d = e.target.closest('[data-idl]');
      if (!d) return;
      const name = `icon-${cur.dataset.n}-32`;
      if (d.dataset.idl === 'svg') return save(new Blob([svgOf(cur)], { type: 'image/svg+xml' }), name + '.svg');
      const jpg = d.dataset.idl === 'jpg', S = 512, pad = jpg ? 96 : 0;
      const img = new Image(), src = URL.createObjectURL(new Blob([svgOf(cur, S)], { type: 'image/svg+xml' }));
      img.onload = () => {
        const cv = document.createElement('canvas'); cv.width = cv.height = S + 2 * pad;
        const ctx = cv.getContext('2d');
        if (jpg) { ctx.fillStyle = bg; ctx.fillRect(0, 0, cv.width, cv.height); }
        ctx.drawImage(img, pad, pad, S, S); URL.revokeObjectURL(src);
        cv.toBlob((b) => save(b, `${name}.${jpg ? 'jpg' : 'png'}`), jpg ? 'image/jpeg' : 'image/png', .95);
      };
      img.src = src;
    });
    const filter = () => {
      const v = q.value.trim().toLowerCase(); let k = 0;
      tiles.forEach((t) => {
        const on = (!fcat || t.dataset.cat === fcat) && (!v || t.dataset.n.includes(v) || t.dataset.num === v);
        t.hidden = !on; if (on) k += 1;
      });
      heads.forEach((h) => { h.hidden = !tiles.some((t) => !t.hidden && t.dataset.cat === h.dataset.cat); });
      count.textContent = `${k} ${k === 1 ? 'ícono' : 'íconos'}`;
    };
    q.addEventListener('input', filter);
    if (chipBar) chipBar.addEventListener('click', (e) => {
      const b = e.target.closest('[data-icf]'); if (!b) return;
      fcat = b.dataset.icf;
      chipBar.querySelectorAll('[data-icf]').forEach((o) => o.setAttribute('aria-pressed', o === b));
      filter();
    });
    select(cur, false);
  });

  /* Cifras que cuentan desde cero */
  const countUp = (el) => {
    const to = Number(el.dataset.count), t0 = performance.now(), dur = 1100;
    const step = (t) => { const p = Math.min(1, (t - t0) / dur); el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(step); };
    el.textContent = '0'; requestAnimationFrame(step);
  };

  /* Pestañas (3.7): índice de temáticas con su lista */
  document.querySelectorAll('[data-tabs]').forEach((tb) => {
    const tabs = [...tb.querySelectorAll('[role="tab"]')];
    const pick = (i, focus) => {
      tabs.forEach((t, k) => {
        const on = k === i, p = document.getElementById(t.getAttribute('aria-controls'));
        t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1; p.hidden = !on;
        if (on) { p.classList.remove('is-swap'); void p.offsetWidth; p.classList.add('is-swap'); }
      });
      if (focus) tabs[i].focus();
    };
    tb.addEventListener('click', (e) => { const t = e.target.closest('[role="tab"]'); if (t) pick(tabs.indexOf(t)); });
    tb.addEventListener('keydown', (e) => {
      const i = tabs.indexOf(e.target), k = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
      if (i > -1 && k) { e.preventDefault(); pick((i + k + tabs.length) % tabs.length, true); }
    });
  });

  /* Gráficos de datos: cada dato muestra su valor al pasar el cursor o al enfocarlo */
  if (document.querySelector('.chart--int')) {
    const tip = document.createElement('div');
    tip.className = 'ctip'; tip.setAttribute('aria-hidden', 'true');
    document.body.appendChild(tip);
    let last = null;
    const show = (el, x, y) => {
      if (el !== last) {
        const [a, b] = el.dataset.tip.split('|');
        tip.replaceChildren(Object.assign(document.createElement('b'), { textContent: a }));
        if (b) tip.appendChild(Object.assign(document.createElement('span'), { textContent: b }));
        last = el;
      }
      tip.style.left = `${x}px`; tip.style.top = `${y}px`; tip.classList.add('is-on');
    };
    const hide = () => { tip.classList.remove('is-on'); last = null; };
    document.addEventListener('pointermove', (e) => {
      const el = e.target.closest && e.target.closest('.chart--int [data-tip]');
      if (el) show(el, e.clientX, e.clientY); else if (last) hide();
    });
    document.addEventListener('focusin', (e) => {
      const el = e.target.closest && e.target.closest('.chart--int [data-tip]');
      if (!el) return;
      const r = el.getBoundingClientRect(); show(el, r.left + r.width / 2, r.top);
    });
    document.addEventListener('focusout', hide);
    addEventListener('scroll', hide, { passive: true });
  }

  /* Dibujo al entrar en pantalla: retículas, áreas de protección y diagramas */
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const draws = document.querySelectorAll('[data-draw]');
    if (draws.length) {
      document.documentElement.classList.add('anim');
      const dio = new IntersectionObserver((ents) => ents.forEach((en) => {
        if (en.isIntersecting) {
          en.target.classList.add('is-drawn'); dio.unobserve(en.target);
          en.target.querySelectorAll('[data-count]').forEach(countUp);
        }
      }), { threshold: .35 });
      draws.forEach((d) => dio.observe(d));
    }
  }

  /* Carrusel (4.5): una ficha a la vez, avanza sola cada 5 s mientras está en pantalla */
  document.querySelectorAll('[data-slider]').forEach((sl) => {
    const track = sl.querySelector('.mslide__track'), items = [...track.children], count = sl.querySelector('.mslide__count');
    const auto = !matchMedia('(prefers-reduced-motion: reduce)').matches, every = Number(sl.dataset.interval) || 5000;
    sl.style.setProperty('--dur', every + 'ms');
    const pad = (n) => String(n).padStart(2, '0');
    let i = 0, t = null, visible = false, hold = false;
    const run = () => {
      clearTimeout(t); sl.classList.remove('is-run');
      if (!auto || !visible || hold) return;
      void sl.offsetWidth; sl.classList.add('is-run');
      t = setTimeout(() => go(i + 1), every);
    };
    const go = (n) => {
      i = (n + items.length) % items.length;
      track.style.transform = `translateX(-${i * 100}%)`;
      items.forEach((it, k) => it.setAttribute('aria-hidden', k !== i));
      count.textContent = `(${pad(i + 1)} / ${pad(items.length)})`;
      if (auto) items[i].querySelectorAll('[data-count]').forEach(countUp);
      run();
    };
    sl.addEventListener('click', (e) => { const b = e.target.closest('[data-step]'); if (b) go(i + Number(b.dataset.step)); });
    sl.addEventListener('keydown', (e) => { const k = { ArrowRight: 1, ArrowLeft: -1 }[e.key]; if (k) { e.preventDefault(); go(i + k); } });
    const pause = (v) => { hold = v; sl.classList.toggle('is-paused', v); if (v) clearTimeout(t); else run(); };
    sl.addEventListener('mouseenter', () => pause(true)); sl.addEventListener('mouseleave', () => pause(false));
    sl.addEventListener('focusin', () => pause(true)); sl.addEventListener('focusout', () => pause(false));
    if ('IntersectionObserver' in window) new IntersectionObserver(([en]) => { visible = en.isIntersecting; run(); }, { threshold: .4 }).observe(sl);
    go(0);
  });

  /* ─── Lateral ─── */
  const secNum = (it, c, k) => {
    const h = hash(it.href);
    if (h && base(it.href) === PAGE) {
      const lb = document.getElementById(h)?.querySelector('.ed__label span');
      if (lb) return lb.textContent.trim();
    }
    return `${parseInt(c.n, 10)}.${k}`;
  };
  const chapters = (area) => area.ch.map((c) => {
    const open = c.items.some((it) => base(it.href) === PAGE);
    let k = 0;
    const items = c.items.map((it) => {
      if (it.sub) return `<div class="nav-sub">${esc(it.sub)}</div>`;
      if (it.grp) return `<div class="nav-grp">${esc(it.grp)}</div>`;
      k += 1;
      const num = secNum(it, c, k);
      const cls = 'nav-item' + (it.deep ? ' is-deep' : '') + (it.href ? '' : ' is-empty');
      const cur = it.href === PAGE || (hash(it.href) && base(it.href) === PAGE && (location.hash ? location.hash === '#' + hash(it.href) : c.items.find((x) => x.href) === it));
      return it.href
        ? `<a class="${cls}" href="${url(it.href)}"${hash(it.href) ? ` data-sec="${hash(it.href)}"` : ''}${cur ? ' aria-current="page"' : ''} title="${esc(it.t)}"><span class="nav-item__n">${num}</span><span class="nav-item__t">${esc(it.st || it.t)}</span>${dot(it.s)}</a>`
        : `<span class="${cls}" title="${esc(it.t)} · página aún no construida"><span class="nav-item__n">${num}</span><span class="nav-item__t">${esc(it.st || it.t)}</span>${dot(it.s)}</span>`;
    }).join('');
    return `<div class="nav-ch" aria-expanded="${open}">
      <button class="nav-ch__btn" type="button" title="${esc(c.n + ' ' + c.t)}"><span class="nav-ch__num">${c.n}</span><span>${esc(c.t)}</span>${ic(I.chev)}</button>
      <div class="nav-list">${items}</div></div>`;
  }).join('');
  const area = NAV.find((x) => x.id === AREA);
  const side = $('side');
  if (side && area) {
    side.innerHTML = `<div class="side__head"><a class="side__area" href="${url(area.href)}"${PAGE === area.href ? ' aria-current="page"' : ''} title="${esc(area.t)}"><span class="kicker">${esc(area.t)}</span></a>`
      + `<button class="side__toggle" type="button" aria-label="Contraer el menú lateral" aria-pressed="false"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M10 3.5 5.5 8l4.5 4.5"/></svg></button></div>`
      + chapters(area)
      + `<div class="side__legend"><span>${dot('v')} Vigente</span><span>${dot('b')} Borrador</span><span>${dot('p')} Por definir</span></div>`;
    const setMin = (on) => {
      body.classList.toggle('side-min', on);
      const t = side.querySelector('.side__toggle');
      t.setAttribute('aria-pressed', on);
      t.setAttribute('aria-label', on ? 'Expandir el menú lateral' : 'Contraer el menú lateral');
      try { localStorage.setItem('k-side', on ? 'min' : 'full'); } catch (_) {}
    };
    try { if (localStorage.getItem('k-side') === 'min') setMin(true); } catch (_) {}
    side.addEventListener('click', (e) => {
      if (e.target.closest('.side__toggle')) return setMin(!body.classList.contains('side-min'));
      const b = e.target.closest('.nav-ch__btn');
      if (b) b.parentElement.setAttribute('aria-expanded', b.parentElement.getAttribute('aria-expanded') === 'true' ? 'false' : 'true');
    });
    /* Barra de capítulo para móvil: abre el lateral como cajón */
    let cur = null;
    area.ch.forEach((c) => c.items.forEach((it) => { if (!cur && base(it.href) === PAGE) cur = [c, hash(it.href) ? { t: 'Secciones' } : it]; }));
    const bar = document.createElement('button');
    bar.type = 'button';
    bar.className = 'chapbar';
    bar.innerHTML = ic('<path d="M2.5 4.5h11M2.5 8h11M2.5 11.5h7"/>') + (cur ? `${cur[0].n} ${esc(cur[0].t)} <span>· ${esc(cur[1].t)}</span>` : `${esc(area.t)} <span>· capítulos</span>`);
    bar.addEventListener('click', () => body.classList.add('nav-open'));
    document.querySelector('.doc').before(bar);
    const scrim = document.createElement('div');
    scrim.className = 'scrim';
    scrim.addEventListener('click', () => body.classList.remove('nav-open'));
    body.appendChild(scrim);
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') body.classList.remove('nav-open'); });
    /* Secciones de un capítulo: el lateral sigue la lectura */
    const secLinks = [...side.querySelectorAll('[data-sec]')].filter((l) => base(l.getAttribute('href').replace(ROOT + '/', '')) === PAGE);
    if (secLinks.length) {
      side.addEventListener('click', (e) => { if (e.target.closest('[data-sec]')) body.classList.remove('nav-open'); });
      const so = new IntersectionObserver((ents) => ents.forEach((en) => {
        if (en.isIntersecting) secLinks.forEach((l) => (l.dataset.sec === en.target.id ? l.setAttribute('aria-current', 'page') : l.removeAttribute('aria-current')));
      }), { rootMargin: '-35% 0px -60% 0px' });
      secLinks.forEach((l) => { const t = document.getElementById(l.dataset.sec); if (t) so.observe(t); });
    }
  }

  /* ─── Portada: índice del manual ─── */
  const ag = $('areas-grid');
  if (ag) {
    ag.innerHTML = NAV.filter((a) => !a.noCard).map((a) => `
      <article class="area">
        <div class="area__color grad grad--${a.color}" aria-hidden="true"></div>
        <div class="area__body">
          <h3 class="t-h3">${esc(a.t)}</h3>
          <p class="t-sm">${esc(a.d)}</p>
          <ul class="area__list">${a.ch.map((c) => `<li><a href="${url(a.href)}#${slug(c)}"><span>${c.n}</span>${esc(c.t)}${dot(c.s)}</a></li>`).join('')}</ul>
          <div class="area__foot"><span class="paren">(${a.ch.length} ${a.ch.length === 1 ? 'capítulo' : 'capítulos'})</span>
            <a class="btn-icon" href="${url(a.href)}" aria-label="Abrir ${esc(a.t)}">${ic(I.right)}</a></div>
        </div>
      </article>`).join('');
  }

  /* Carrusel de áreas en la portada */
  document.addEventListener('click', (e) => {
    const b = e.target.closest('[data-cstep]');
    if (!b) return;
    const row = document.getElementById(b.dataset.target);
    if (row) row.scrollBy({ left: Number(b.dataset.cstep) * row.clientWidth * .68, behavior: 'smooth' });
  });

  /* Filtro desplegable: un botón a la izquierda de la búsqueda abre las opciones */
  document.querySelectorAll('[data-fpop]').forEach((pop) => {
    const btn = pop.querySelector('.fpop__btn'), panel = pop.querySelector('.fpop__panel'), val = pop.querySelector('.fpop__val');
    const close = () => { panel.hidden = true; btn.setAttribute('aria-expanded', 'false'); };
    btn.addEventListener('click', (e) => { e.stopPropagation(); const open = panel.hidden; panel.hidden = !open; btn.setAttribute('aria-expanded', String(open)); });
    panel.addEventListener('click', (e) => {
      const o = e.target.closest('button'); if (!o) return;
      if (val) val.textContent = o.dataset.label || o.textContent;
      if (!pop.hasAttribute('data-fpop-multi')) close();
    });
    document.addEventListener('click', (e) => { if (!pop.contains(e.target)) close(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
  });

  /* Galería de fotografía: filtros, búsqueda, ficha con descargas y tratamientos de marca */
  document.querySelectorAll('[data-gal]').forEach((gal) => {
    const cards = [...gal.querySelectorAll('.gph')], q = gal.querySelector('.gal__q'), count = gal.querySelector('.gal__count');
    const sel = {};
    gal.querySelectorAll('[data-gf]').forEach((b) => { sel[b.dataset.gf.split(':')[0]] = ''; });
    /* Carrusel de la galería (Recursos): la imagen actual al frente, la siguiente asoma; avanza sola y con las flechas */
    const gsl = gal.querySelector('[data-gsl]');
    const slide = gsl && (() => {
      const track = gsl.querySelector('.gsl__track'), info = gsl.querySelector('.gsl__info'), nb = gsl.querySelector('.gsl__n b'), nt = gsl.querySelector('.gsl__n span');
      let k = 0, t = null, auto = !matchMedia('(prefers-reduced-motion: reduce)').matches, vis = false;
      const list = () => cards.filter((c) => !c.hidden);
      const pad = (n) => String(n).padStart(2, '0');
      const go = (n) => {
        const v = list(); if (!v.length) return;
        k = (n + v.length) % v.length;
        const c = v[k];
        track.style.transform = `translate3d(${-c.offsetLeft}px,0,0)`;
        cards.forEach((x) => x.classList.toggle('is-cur', x === c));
        nb.textContent = pad(k + 1); nt.textContent = '/ ' + pad(v.length);
        gsl.style.setProperty('--p', ((k + 1) / v.length * 100).toFixed(2) + '%');
        info.innerHTML = c.querySelector('.gph__info').innerHTML;
        clearTimeout(t); if (auto && vis) t = setTimeout(() => go(k + 1), 5000);
      };
      const stop = () => { auto = false; clearTimeout(t); };
      gsl.querySelectorAll('[data-gs]').forEach((b) => b.addEventListener('click', () => { stop(); go(k + Number(b.dataset.gs)); }));
      gsl.addEventListener('keydown', (e) => { const d = { ArrowRight: 1, ArrowLeft: -1 }[e.key]; if (d) { e.preventDefault(); stop(); go(k + d); } });
      let sx = null;
      gsl.addEventListener('pointerdown', (e) => { sx = e.clientX; });
      gsl.addEventListener('pointerup', (e) => { if (sx !== null && Math.abs(e.clientX - sx) > 60) { stop(); go(k + (e.clientX < sx ? 1 : -1)); } sx = null; });
      gsl.addEventListener('mouseenter', () => clearTimeout(t));
      gsl.addEventListener('mouseleave', () => { if (auto && vis) t = setTimeout(() => go(k + 1), 5000); });
      if ('IntersectionObserver' in window) new IntersectionObserver(([en]) => { vis = en.isIntersecting; go(k); }, { threshold: .3 }).observe(gsl);
      addEventListener('resize', () => go(k));
      requestAnimationFrame(() => go(0));
      return { go, stop, vis: list };
    })();
    const view = (v) => { gal.dataset.view = v; gal.querySelectorAll('[data-gv]').forEach((o) => o.setAttribute('aria-pressed', String(o.dataset.gv === v))); };
    gal.querySelectorAll('[data-gv]').forEach((b) => b.addEventListener('click', () => view(b.dataset.gv)));
    setTimeout(() => {   // ?tipo=cielo abre la galería ya filtrada
      new URLSearchParams(location.search).forEach((v, k) => { const b = gal.querySelector(`[data-gf="${k}:${v}"]`); if (b) b.click(); });
    }, 0);
    const filter = () => {
      const v = (q.value || '').trim().toLowerCase(); let k = 0;
      cards.forEach((c) => {
        const on = Object.keys(sel).every((g) => !sel[g] || c.dataset[g] === sel[g]) && (!v || c.dataset.q.includes(v));
        c.hidden = !on; if (on) k += 1;
      });
      const [u1, u2] = (gal.dataset.unit || 'imagen|imágenes').split('|');
      count.textContent = `${k} ${k === 1 ? u1 : u2}`;
      if (v || Object.values(sel).some(Boolean)) view('grid');   // al filtrar, se ven todas en retícula
      if (slide) slide.go(0);
    };
    q.addEventListener('input', filter);
    const allB = gal.querySelector('[data-gall]');
    const syncAll = () => { const n = Object.values(sel).filter(Boolean).length; if (allB) allB.setAttribute('aria-pressed', String(!n)); return n; };
    if (allB) allB.addEventListener('click', () => {
      Object.keys(sel).forEach((g) => { sel[g] = ''; });
      gal.querySelectorAll('[data-gf]').forEach((o) => o.setAttribute('aria-pressed', 'false'));
      syncAll(); gal.querySelector('.fpop__val').textContent = ''; filter();
    });
    gal.querySelectorAll('[data-gf]').forEach((b) => b.addEventListener('click', () => {
      const [g, v] = b.dataset.gf.split(':');
      sel[g] = sel[g] === v ? '' : v;
      gal.querySelectorAll(`[data-gf^="${g}:"]`).forEach((o) => o.setAttribute('aria-pressed', String(!!sel[g] && o === b)));
      const n = syncAll();
      gal.querySelector('.fpop__val').textContent = n ? String(n) : '';
      filter();
    }));
    const dlg = gal.querySelector('.gal__dlg'), img = dlg.querySelector('.gal__big'), meta = dlg.querySelector('.gal__meta'), wshRow = dlg.querySelector('.gal__wsh');
    let cur = null;
    const show = (c) => {
      cur = c;
      img.style.backgroundImage = c.dataset.src ? `url(${c.dataset.src})` : '';
      img.classList.toggle('is-ph', !c.dataset.src);
      img.dataset.fx = ''; img.dataset.wsh = 'r';
      dlg.querySelectorAll('button[data-fx]').forEach((o) => o.setAttribute('aria-pressed', o.dataset.fx === ''));
      dlg.querySelectorAll('button[data-wsh]').forEach((o) => o.setAttribute('aria-pressed', o.dataset.wsh === 'r'));
      if (wshRow) wshRow.hidden = true;
      meta.innerHTML = c.querySelector('.gph__info, .gph__meta').innerHTML;
      dlg.hidden = false; document.body.style.overflow = 'hidden';
    };
    const hide = () => { dlg.hidden = true; document.body.style.overflow = ''; };
    cards.forEach((c) => c.addEventListener('click', () => {
      if (slide && !c.classList.contains('is-cur')) { slide.stop(); slide.go(slide.vis().indexOf(c)); return; }
      show(c);
    }));
    const save = (blob, name) => {
      const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = name;
      document.body.appendChild(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(a.href), 1500);
    };
    dlg.addEventListener('click', (e) => {
      if (e.target === dlg || e.target.closest('[data-gclose]')) return hide();
      const ws = e.target.closest('button[data-wsh]');
      if (ws) {
        img.dataset.wsh = ws.dataset.wsh; img.dataset.fx = 'win';
        dlg.querySelectorAll('button[data-wsh]').forEach((o) => o.setAttribute('aria-pressed', o === ws));
        dlg.querySelectorAll('button[data-fx]').forEach((o) => o.setAttribute('aria-pressed', o.dataset.fx === 'win'));
        return;
      }
      const fx = e.target.closest('button[data-fx]');
      if (fx) {
        img.dataset.fx = fx.dataset.fx; dlg.querySelectorAll('button[data-fx]').forEach((o) => o.setAttribute('aria-pressed', o === fx));
        if (wshRow) wshRow.hidden = fx.dataset.fx !== 'win';
        return;
      }
      if (e.target.closest('[data-gcred]') && cur) return copy(cur.dataset.cred, gal.dataset.credMsg || 'Crédito copiado');
      const dl = e.target.closest('[data-gdl]');
      if (!dl || !cur || !cur.dataset.src) return;
      const name = 'keyons-' + cur.querySelector('.gph__info b, .gph__meta b').textContent.split(' · ')[0].toLowerCase().normalize('NFD').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
      const R = { post: [1080, 1080], story: [1080, 1920], deck: [1920, 1080] }[dl.dataset.gdl];
      if (!R) { const a = document.createElement('a'); a.href = cur.dataset.src; a.download = name; document.body.appendChild(a); a.click(); a.remove(); return; }
      const im = new Image();
      im.onload = () => {
        const cv = document.createElement('canvas'); [cv.width, cv.height] = R;
        const k = Math.max(R[0] / im.width, R[1] / im.height), w = im.width * k, h = im.height * k;
        cv.getContext('2d').drawImage(im, (R[0] - w) / 2, (R[1] - h) / 2, w, h);
        cv.toBlob((b) => save(b, `${name}-${dl.dataset.gdl}.jpg`), 'image/jpeg', 0.92);
      };
      im.src = cur.dataset.src;
    });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !dlg.hidden) hide(); });
  });

  /* 18.1 · Tipos de presentación: pestañas que mueven la estrella entre formal y libre */
  document.querySelectorAll('[data-ptype]').forEach((pt) => {
    const tabs = [...pt.querySelectorAll('[data-pt]')];
    const pick = (b) => {
      tabs.forEach((o) => o.setAttribute('aria-selected', String(o === b)));
      pt.querySelectorAll('[data-pp]').forEach((p) => { p.hidden = p.dataset.pp !== b.dataset.pt; });
      pt.style.setProperty('--x', b.dataset.x + '%');
    };
    tabs.forEach((b, i) => {
      b.addEventListener('click', () => pick(b));
      b.addEventListener('keydown', (e) => {
        const d = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
        if (d) { const n = tabs[(i + d + tabs.length) % tabs.length]; n.focus(); pick(n); }
      });
    });
  });

  /* 18.4 · Storytelling: tambor de números, texto y estrella sobre el arco */
  document.querySelectorAll('[data-story]').forEach((st) => {
    const nums = [...st.querySelectorAll('.story__reel span')], reel = st.querySelector('.story__reel');
    const ps = [...st.querySelectorAll('[data-sp]')], pts = [...st.querySelectorAll('[data-sgo]')], sr = st.querySelector('.story__star');
    let k = 0, t = null, vis = false, auto = !matchMedia('(prefers-reduced-motion: reduce)').matches;
    const set = (n) => {
      k = (n + ps.length) % ps.length;
      const h = nums[0].offsetHeight || 88;
      reel.style.transform = `translateY(${(1 - k) * h}px)`;
      nums.forEach((s, i) => s.classList.toggle('is-on', i === k));
      ps.forEach((p, i) => { p.hidden = i !== k; });
      pts.forEach((p, i) => p.classList.toggle('is-on', i === k));
      st.querySelectorAll(':scope > [data-sky]').forEach((sk, i) => sk.classList.toggle('is-on', i === k));
      if (ps[k].dataset.ink) st.dataset.ink = ps[k].dataset.ink;
      const c = pts[k].querySelector('circle');
      sr.style.transform = `translate(${c.getAttribute('cx')}px,${c.getAttribute('cy')}px)`;
      clearTimeout(t);
      if (auto && vis) t = setTimeout(() => set(k + 1), 5000);
    };
    const stop = () => { auto = false; clearTimeout(t); };
    st.addEventListener('click', (e) => {
      const b = e.target.closest('[data-stl]'), g = e.target.closest('[data-sgo]');
      if (b) { stop(); set(k + Number(b.dataset.stl)); }
      if (g) { stop(); set(Number(g.dataset.sgo)); }
    });
    st.addEventListener('keydown', (e) => {
      const d = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 }[e.key];
      if (d) { e.preventDefault(); stop(); set(k + d); }
    });
    if ('IntersectionObserver' in window) new IntersectionObserver(([en]) => { vis = en.isIntersecting; set(k); }, { threshold: .5 }).observe(st);
    set(0);
  });

  /* 18.2 · Método: el riel se llena al bajar y marca los pasos ya recorridos */
  document.querySelectorAll('[data-mtd]').forEach((m) => {
    const list = m.querySelector('.mtd__l'), rail = m.querySelector('.mtd__rail'), steps = [...m.querySelectorAll('.mtd__s')];
    let raf = 0;
    const upd = () => {
      raf = 0;
      const r = list.getBoundingClientRect(), mid = innerHeight * .55;
      const p = Math.max(0, Math.min(1, (mid - r.top - 28) / (r.height - 56)));
      rail.style.setProperty('--p', (p * 100).toFixed(1) + '%');
      steps.forEach((s) => s.classList.toggle('is-on', s.getBoundingClientRect().top + 28 < mid));
    };
    addEventListener('scroll', () => { if (!raf) raf = requestAnimationFrame(upd); }, { passive: true });
    upd();
  });

  /* 18.3 · Fórmula de la idea central: cada parte se ilumina en el ejemplo */
  document.querySelectorAll('[data-fml]').forEach((f) => {
    const hot = (n) => f.querySelectorAll('[data-part]').forEach((e) => e.classList.toggle('is-hot', !!n && e.dataset.part === n));
    f.querySelectorAll('.fml__chip, .fml__ex [data-part]').forEach((c) => {
      c.addEventListener('mouseenter', () => hot(c.dataset.part));
      c.addEventListener('focus', () => hot(c.dataset.part));
      c.addEventListener('mouseleave', () => hot(''));
      c.addEventListener('blur', () => hot(''));
    });
    f.querySelectorAll('[data-fx-ex]').forEach((b) => b.addEventListener('click', () => {
      f.querySelectorAll('[data-fx-ex]').forEach((o) => o.setAttribute('aria-pressed', String(o === b)));
      f.querySelectorAll('[data-ex]').forEach((e) => { e.hidden = e.dataset.ex !== b.dataset.fxEx; });
    }));
  });

  /* 18.5 · Escribir para la pantalla: pestañas Pantalla y Voz */
  document.querySelectorAll('[data-wr2]').forEach((w) => {
    w.querySelectorAll('[data-wk]').forEach((b) => b.addEventListener('click', () => {
      w.querySelectorAll('[data-wk]').forEach((o) => o.setAttribute('aria-pressed', String(o === b)));
      w.querySelectorAll('[data-ws]').forEach((s) => { s.hidden = s.dataset.ws !== b.dataset.wk; });
    }));
  });

  /* 9.6 · Texturas: filtro por cielo y búsqueda dentro del carrusel */
  document.querySelectorAll('[data-texf]').forEach((tf) => {
    const figs = [...tf.querySelectorAll('.tex')], q = tf.querySelector('.texf__q'), n = tf.querySelector('.texf__count'), car = tf.querySelector('.texs--car');
    let fase = '', tipo = '';
    const run = () => {
      const v = q.value.trim().toLowerCase();
      let k = 0;
      figs.forEach((f) => { const on = (!fase || f.dataset.fase === fase) && (!tipo || f.dataset.tipo === tipo) && (!v || f.dataset.q.includes(v)); f.hidden = !on; if (on) k += 1; });
      n.textContent = `${k} ${k === 1 ? 'pieza' : 'piezas'}`;
      if (car) car.scrollTo({ left: 0 });
    };
    tf.querySelectorAll('[data-tf]').forEach((b) => b.addEventListener('click', () => {
      fase = b.dataset.tf;
      tf.querySelectorAll('[data-tf]').forEach((o) => o.setAttribute('aria-pressed', String(o === b)));
      run();
    }));
    tf.querySelectorAll('[data-tt]').forEach((b) => b.addEventListener('click', () => {
      tipo = b.dataset.tt;
      tf.querySelectorAll('[data-tt]').forEach((o) => o.setAttribute('aria-pressed', String(o === b)));
      run();
    }));
    q.addEventListener('input', run);
  });

  /* 18.7 · Color y ritmo */
  document.querySelectorAll('[data-rhythm]').forEach((rh) => {
    const cap = rh.querySelector('.rhythm__cap'), base = cap.textContent;
    rh.querySelectorAll('[data-rk]').forEach((b) => b.addEventListener('click', () => {
      rh.querySelectorAll('[data-rk]').forEach((o) => o.setAttribute('aria-pressed', String(o === b)));
      rh.querySelectorAll('[data-rs]').forEach((s) => { s.hidden = s.dataset.rs !== b.dataset.rk; });
      rh.querySelectorAll('[data-rb]').forEach((s) => { s.hidden = s.dataset.rb !== b.dataset.rk; });
      cap.textContent = base;
    }));
    const show = (e) => { const r = e.target.closest('.rh'); if (r) cap.textContent = r.dataset.cap; };
    rh.addEventListener('mouseover', show);
    rh.addEventListener('focusin', show);
    rh.addEventListener('mouseleave', () => { cap.textContent = base; });
  });

  /* 18.10 · Plantillas: al pasar el cursor, la tarjeta hojea sus diapositivas */
  document.querySelectorAll('[data-cyc]').forEach((box) => {
    const ims = [...box.querySelectorAll('img')];
    let i = 0, t = null;
    const show = (n) => { i = n % ims.length; ims.forEach((im, j) => im.classList.toggle('is-on', j === i)); };
    const card = box.closest('.tpl__c') || box;
    card.addEventListener('mouseenter', () => { clearInterval(t); show(1); t = setInterval(() => show(i + 1), 1100); });
    card.addEventListener('mouseleave', () => { clearInterval(t); show(0); });
  });

  /* 18.12 · Lista de verificación: cuenta lo marcado y lo recuerda en este navegador */
  document.querySelectorAll('[data-chk]').forEach((ck) => {
    const KEY = 'keyons-chk-' + location.pathname;
    const boxes = [...ck.querySelectorAll('input[type="checkbox"]')];
    const sum = () => {
      const n = boxes.filter((b) => b.checked).length;
      ck.querySelector('.chk__n b').textContent = n;
      ck.querySelector('.chk__bar').style.setProperty('--p', (100 * n / boxes.length) + '%');
      try { localStorage.setItem(KEY, JSON.stringify(boxes.map((b) => b.checked))); } catch (_) {}
    };
    try { const s = JSON.parse(localStorage.getItem(KEY) || '[]'); boxes.forEach((b, i) => { b.checked = !!s[i]; }); } catch (_) {}
    boxes.forEach((b) => b.addEventListener('change', sum));
    ck.querySelector('.chk__reset').addEventListener('click', () => { boxes.forEach((b) => { b.checked = false; }); sum(); });
    sum();
  });

  /* ─── Página de área ───
     Cada capítulo: número grande, título, descripción y sus páginas
     agrupadas en columnas por subcategoría. */
  const ap = $('area-page');
  if (ap && area) {
    const pages = area.ch.reduce((n, c) => n + c.items.filter((x) => x.t).length, 0);
    const pg = (it) => it.href
      ? `<a class="pg" href="${url(it.href)}">${esc(it.t)}${ic(I.right)}${dot(it.s)}</a>`
      : `<span class="pg">${esc(it.t)}${dot(it.s)}</span>`;
    const cols = (c) => {
      const groups = [];
      c.items.forEach((it) => {
        if (it.sub) groups.push({ t: it.sub, items: [] });
        else { if (!groups.length) groups.push({ t: '', items: [] }); groups[groups.length - 1].items.push(it); }
      });
      /* Sin subcategorías: se reparten en columnas de hasta 4 páginas */
      if (groups.length === 1 && !groups[0].t) {
        const all = groups[0].items, per = Math.max(3, Math.ceil(all.length / 3));
        groups.length = 0;
        for (let k = 0; k < all.length; k += per) groups.push({ t: '', items: all.slice(k, k + per) });
      }
      return groups.map((g) => `<div>${g.t ? `<p class="chap__col-t">${esc(g.t)}</p>` : ''}${g.items.map((it) => it.grp ? `<p class="chap__grp">${esc(it.grp)}</p>` : pg(it)).join('')}</div>`).join('');
    };
    const badge = (st) => `<span class="badge badge--${SKEY[st]}">${ic({ v: I.check, b: '<circle cx="8" cy="8" r="5.6"/><path d="M8 2.4v11.2"/>', p: '<circle cx="8" cy="8" r="5.6"/>' }[st])}${STATUS[st]}</span>`;
    ap.innerHTML = `
      <header class="page-head">
        <h1 class="t-h1">${esc(area.t)}</h1>
        <p class="t-lead">${esc(area.d)}</p>
        <div class="facts">
          <div><span class="paren">(Capítulos)</span><b>${area.ch[0].n}–${area.ch[area.ch.length - 1].n}</b></div>
          <div><span class="paren">(Páginas)</span><b>${pages}</b></div>
          <div><span class="paren">(Color)</span><b>${esc(area.colorName)}</b></div>
        </div>
      </header>
      <div class="band grad grad--${area.color}" aria-hidden="true"></div>
      ${area.ch.map((c) => `
        <section class="chap" id="${slug(c)}">
          <div class="chap__head">
            <span class="chap__n">${c.n}</span>
            <div><h2 class="chap__t">${esc(c.t)}</h2><p class="t-body chap__d">${esc(c.d || '')}</p></div>
            <div class="chap__meta">${badge(c.s || 'p')}<span class="paren">(${c.items.filter((x) => x.t).length} páginas)</span></div>
          </div>
          <div class="chap__cols">${cols(c)}</div>
        </section>`).join('')}`;
    /* El contenido se genera después de cargar: se respeta el ancla de la URL */
    if (location.hash) { const t = document.querySelector(location.hash); if (t) requestAnimationFrame(() => t.scrollIntoView()); }
  }

  /* ─── Paginador automático ─── */
  const pg = $('pager');
  if (pg) {
    const k = seq.findIndex((x) => base(x.href) === PAGE);
    const prev = k > 0 ? seq[k - 1] : { t: 'Portada', href: 'index.html' };
    const next = k >= 0 && k < seq.length - 1 ? seq[k + 1] : null;
    pg.className = 'pager';
    pg.innerHTML = `<a href="${url(prev.href)}"><span class="paren">(Anterior)</span><span class="pager__t">${ic(I.left)}${esc(prev.t)}</span></a>`
      + (next ? `<a href="${url(next.href)}"><span class="paren">(Siguiente)</span><span class="pager__t">${esc(next.t)}${ic(I.right)}</span></a>` : '<span></span>');
  }

  /* ─── Índice de la página + resaltado al desplazar ─── */
  const toc = $('toc');
  if (toc) {
    const secs = [...document.querySelectorAll('.content [data-toc]')];
    toc.innerHTML = `<div class="toc__t">(En esta página)</div>` + secs.map((s) => `<a href="#${s.id}">${esc(s.dataset.toc)}</a>`).join('');
    const links = [...toc.querySelectorAll('a')];
    const io = new IntersectionObserver((ents) => ents.forEach((en) => {
      if (en.isIntersecting) links.forEach((l) => l.classList.toggle('is-active', l.hash === '#' + en.target.id));
    }), { rootMargin: '-20% 0px -70% 0px' });
    secs.forEach((s) => io.observe(s));
  }

  /* ─── Regla de esquinas en grupos ───
     Una esquina es curva si mira a otro recuadro del grupo (hay uno a su lado o encima/debajo);
     si no mira a nadie, es exterior y va recta. Un recuadro solo queda con las cuatro rectas. */
  const cornerBox = (box) => {
    const r = box.dataset.corners ? box.dataset.corners + 'px' : 'var(--r-component)';
    const kids = [...box.children].filter((c) => c.offsetWidth && c.offsetHeight && getComputedStyle(c).position !== 'absolute');
    const R = kids.map((c) => c.getBoundingClientRect());
    const ov = (a0, a1, b0, b1) => Math.min(a1, b1) - Math.max(a0, b0) > 2;
    kids.forEach((c, i) => {
      const q = R[i], o = R.filter((_, j) => j !== i);
      const L = o.some((p) => p.right <= q.left + 2 && ov(p.top, p.bottom, q.top, q.bottom));
      const Rt = o.some((p) => p.left >= q.right - 2 && ov(p.top, p.bottom, q.top, q.bottom));
      const T = o.some((p) => p.bottom <= q.top + 2 && ov(p.left, p.right, q.left, q.right));
      const B = o.some((p) => p.top >= q.bottom - 2 && ov(p.left, p.right, q.left, q.right));
      const v = [L || T, Rt || T, Rt || B, L || B].map((x) => (x ? r : '0')).join(' ');
      c.style.borderRadius = v; c.style.setProperty('--crn', v);   // --crn, para la imagen de adentro
    });
  };
  const cornersAll = () => document.querySelectorAll('[data-corners]').forEach(cornerBox);
  let crT; const cornersSoon = () => { cancelAnimationFrame(crT); crT = requestAnimationFrame(() => requestAnimationFrame(cornersAll)); };
  cornersAll(); addEventListener('load', cornersAll); addEventListener('resize', cornersSoon);
  document.addEventListener('click', cornersSoon); document.addEventListener('input', cornersSoon);
  if ('ResizeObserver' in window) { const ro = new ResizeObserver(cornersSoon); document.querySelectorAll('[data-corners]').forEach((b) => ro.observe(b)); }

  /* ─── Carruseles de una pieza a la vez: colecciones (9.7) e íconos (10.5) ───
     Avanzan solos, se pausan con el cursor y responden a flechas y teclado. */
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const carousel = (el, sel, ms, onGo) => {
    const n = el.querySelectorAll(sel).length; let k = 0, t;
    const go = (i) => { k = (i + n) % n; onGo(k); };
    const play = () => { clearInterval(t); if (!still) t = setInterval(() => go(k + 1), ms); };
    el.addEventListener('keydown', (e) => { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); go(k + (e.key === 'ArrowRight' ? 1 : -1)); play(); } });
    let seen = false, inview = !('IntersectionObserver' in window);
    const run = () => { clearInterval(t); if (inview) play(); };
    el.addEventListener('mouseenter', () => clearInterval(t)); el.addEventListener('mouseleave', run);
    if (!inview) new IntersectionObserver(([en]) => { inview = en.isIntersecting; if (inview && !seen) { seen = true; go(0); } run(); }, { threshold: .35 }).observe(el);
    go(0); run();
    return { go: (i) => { go(i); run(); }, at: () => k };
  };
  document.querySelectorAll('[data-cstk]').forEach((el) => {
    const sets = el.querySelectorAll('.cstk__set'), its = el.querySelectorAll('.cstk__it'), nb = el.querySelector('.cstk__n b');
    const c = carousel(el, '.cstk__set', 6000, (k) => {
      sets.forEach((s, j) => s.classList.toggle('is-on', j === k));
      its.forEach((s, j) => { s.hidden = j !== k; });
      nb.textContent = String(k + 1).padStart(2, '0');
    });
    el.querySelectorAll('[data-cs]').forEach((b) => b.addEventListener('click', () => c.go(c.at() + Number(b.dataset.cs))));
  });
  document.querySelectorAll('[data-icar]').forEach((el) => {
    const ss = el.querySelectorAll('.icar__s'), its = el.querySelectorAll('.icar__it'), bs = el.querySelectorAll('[data-ci]');
    const c = carousel(el, '.icar__s', 3600, (k) => {
      ss.forEach((s, j) => s.classList.toggle('is-on', j === k));
      its.forEach((s, j) => { s.hidden = j !== k; });
      bs.forEach((b, j) => { b.classList.remove('is-on'); void b.offsetWidth; b.classList.toggle('is-on', j === k); });
      el.querySelector('.icar__stage').style.background = getComputedStyle(ss[k]).getPropertyValue('--bg');
    });
    bs.forEach((b) => b.addEventListener('click', () => c.go(Number(b.dataset.ci))));
  });

  /* ─── Retícula dinámica de líneas (lgrid) ───
     Las líneas internas solo van donde un recuadro mira a otro: sin borde izquierdo en la primera columna real. */
  const lgridAll = () => document.querySelectorAll('[data-lgrid]').forEach((g) => {
    const kids = [...g.children], R = kids.map((c) => c.getBoundingClientRect());
    kids.forEach((c, i) => c.classList.toggle('is-l0', !R.some((p, j) => j !== i && p.right <= R[i].left + 2 && Math.min(p.bottom, R[i].bottom) - Math.max(p.top, R[i].top) > 2)));
  });
  lgridAll(); addEventListener('load', lgridAll); addEventListener('resize', cornersSoon); addEventListener('resize', () => requestAnimationFrame(lgridAll));

  /* ─── Ráfaga (9.6): la fase del cielo se elige con los botones ─── */
  document.querySelectorAll('[data-raf]').forEach((r) => {
    if (still) { const sv = r.querySelector('svg'); if (sv && sv.pauseAnimations) sv.pauseAnimations(); }
    r.querySelectorAll('[data-rph]').forEach((b) => b.addEventListener('click', () => {
      r.dataset.ph = b.dataset.rph;
      r.querySelectorAll('[data-rph]').forEach((o) => o.setAttribute('aria-pressed', String(o === b)));
    }));
  });

  /* ─── Ráfagas (9.6): el cursor las empuja como el viento y vuelven solas a su lugar ───
     Mismo gesto que el hover de los encabezados: lo que se mueve es la forma, con fricción. */
  document.querySelectorAll('[data-rfp][data-flow]').forEach((p) => {
    const sv = p.querySelector('svg');
    let boost = 0, lx = null, ly = null, lt = 0, raf = 0;
    const tick = (t) => {
      const dt = Math.min((t - lt) / 1000, .05); lt = t;
      boost *= Math.exp(-dt / 1.4);
      if (sv.setCurrentTime && sv.getCurrentTime) sv.setCurrentTime(sv.getCurrentTime() + boost * dt);
      raf = boost > .02 ? requestAnimationFrame(tick) : 0;
    };
    p.addEventListener('pointermove', (e) => {
      if (lx !== null) boost = Math.min(4, boost + Math.hypot(e.clientX - lx, e.clientY - ly) * .02);
      lx = e.clientX; ly = e.clientY;
      if (!raf) { lt = performance.now(); raf = requestAnimationFrame(tick); }
    });
    p.addEventListener('pointerleave', () => { lx = ly = null; });
    if (still && sv.pauseAnimations) sv.pauseAnimations();
    else if ('IntersectionObserver' in window) new IntersectionObserver(([en]) => { if (sv.pauseAnimations) en.isIntersecting ? sv.unpauseAnimations() : sv.pauseAnimations(); }).observe(p);
  });
  document.querySelectorAll('[data-rfp][data-push]').forEach((p) => {
    const g = p.querySelector('.rfp__push'), sv = p.querySelector('svg');
    let ox = 0, oy = 0, lx = null, ly = null, lt = 0, raf = 0;
    const tick = (t) => {
      const dt = Math.min((t - lt) / 1000, .05); lt = t;
      const k = Math.exp(-dt / 1.3); ox *= k; oy *= k;
      g.setAttribute('transform', `translate(${ox.toFixed(2)} ${oy.toFixed(2)}) skewX(${(-ox * .25).toFixed(2)})`);
      raf = Math.abs(ox) + Math.abs(oy) > .05 ? requestAnimationFrame(tick) : 0;
    };
    p.addEventListener('pointermove', (e) => {
      const r = p.getBoundingClientRect(), x = (e.clientX - r.left) / r.width * 300, y = (e.clientY - r.top) / r.height * 400;
      if (lx !== null) { ox = Math.max(-28, Math.min(28, ox + (x - lx) * .22)); oy = Math.max(-28, Math.min(28, oy + (y - ly) * .22)); }
      lx = x; ly = y;
      if (!raf) { lt = performance.now(); raf = requestAnimationFrame(tick); }
    });
    p.addEventListener('pointerleave', () => { lx = ly = null; });
    if (still && sv.pauseAnimations) sv.pauseAnimations();
    else if ('IntersectionObserver' in window) new IntersectionObserver(([en]) => { if (sv.pauseAnimations) en.isIntersecting ? sv.unpauseAnimations() : sv.pauseAnimations(); }).observe(p);
  });

  /* ─── Rótulos sin paréntesis: «(Ilustrativa)» se lee «Ilustrativa» ─── */
  document.querySelectorAll('.content .paren').forEach((p) => {
    const t = p.textContent.trim(), m = t.match(/^\((.+)\)$/);
    if (m && p.children.length === 0) p.textContent = m[1];
  });

  /* ─── 7.6 · una regla a la vez: la lista a la izquierda, su demostración a la derecha ─── */
  document.querySelectorAll('[data-rview]').forEach((rv) => {
    const bs = rv.querySelectorAll('[data-rv]'), its = rv.querySelectorAll('.rview__it');
    const go = (k) => { bs.forEach((b, i) => b.setAttribute('aria-pressed', String(i === k))); its.forEach((it, i) => { it.hidden = i !== k; }); };
    bs.forEach((b, i) => { b.addEventListener('click', () => go(i)); b.addEventListener('mouseenter', () => go(i)); b.addEventListener('focus', () => go(i)); });
  });

  /* ─── Viñetas en damero ───
     Círculo y cuadrado se intercalan por fila y por columna, según cómo se acomodan en pantalla.
     El manual es documentación larga: van en Azul Noche (Blanco Keyons sobre oscuro), como pide 9.1. */
  const VA_D = 'M10 0a10 10 0 1 0 0 20a10 10 0 1 0 0-20ZM7.76 6h4.48A1.76 1.76 0 0 1 14 7.76v4.48A1.76 1.76 0 0 1 12.24 14H7.76A1.76 1.76 0 0 1 6 12.24V7.76A1.76 1.76 0 0 1 7.76 6Z';
  const VB_D = 'M1.1 1.1h17.8v17.8H1.1ZM10 5.55a4.45 4.45 0 1 0 0 8.9a4.45 4.45 0 1 0 0-8.9Z';
  const BSEL = 'svg path[d^="M10 0a10 10 0 1 0"], svg path[d^="M1.1 1.1h17.8v17.8"]';
  const checker = () => {
    const groups = new Map();
    document.querySelectorAll(BSEL).forEach((p) => {
      if (p.closest('#vinetas, [data-vkeep], .propuesta')) return;   // los ejemplos de 9.1 muestran combinaciones a propósito
      let it = p.closest('li') || p.closest('svg').parentElement;
      while (it.parentElement && it.parentElement !== document.body && it.parentElement.querySelectorAll(BSEL).length === 1) it = it.parentElement;
      const box = it.parentElement;
      if (!groups.has(box)) groups.set(box, []);
      groups.get(box).push([it, p]);
    });
    groups.forEach((arr) => {
      const pos = arr.map(([it]) => ({ top: it.offsetTop, left: it.offsetLeft, width: it.offsetWidth }));   // sin transformaciones
      const shown = pos.some((r) => r.width);
      const tops = [];
      pos.forEach((r) => { if (!tops.some((t) => Math.abs(t - r.top) < 6)) tops.push(r.top); });
      tops.sort((a, b) => a - b);
      arr.forEach(([it, p], i) => {
        let k = i % 2;
        if (shown) {
          const r = pos[i], row = tops.findIndex((t) => Math.abs(t - r.top) < 6);
          const col = pos.filter((o) => Math.abs(o.top - r.top) < 6 && o.left < r.left - 2).length;
          k = (row + col) % 2;
        }
        p.setAttribute('d', k ? VB_D : VA_D);
        const c = it.closest('.is-dark, .portal, .vdk') ? 'var(--k-blanco)' : 'var(--k-noche)';
        it.style.setProperty('--vc', c);
        p.closest('svg').style.color = c;
      });
    });
  };
  checker();
  addEventListener('load', checker);
  let chkT; addEventListener('resize', () => { clearTimeout(chkT); chkT = setTimeout(checker, 150); });

  /* ─── Aparición al desplazar ───
     Los bloques entran suavemente a medida que llegan a la pantalla. */
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const targets = [...document.querySelectorAll('.ed, .chap, .dsec, .area, .acar, .sec-head, .cols, .band, .rings, .matrix, .pgrid, .promises, .cstack, .tbl-wrap, .zig__item, .step, .chan, .pairs, .entry')].filter((t) => !t.parentElement.closest('.acar'));
    const ro = new IntersectionObserver((ents) => ents.forEach((en) => {
      if (en.isIntersecting) { en.target.classList.add('is-in'); ro.unobserve(en.target); }
    }), { rootMargin: '0px 0px -8% 0px', threshold: .08 });
    targets.forEach((t) => { if (t.getBoundingClientRect().top > innerHeight) { t.classList.add('reveal'); ro.observe(t); } });
  }

  /* ─── Buscador ─── */
  const sb = document.createElement('div');
  sb.className = 'search';
  sb.setAttribute('role', 'dialog');
  sb.setAttribute('aria-modal', 'true');
  sb.setAttribute('aria-label', 'Buscar en el manual');
  sb.innerHTML = `<div class="search__box">
      <div class="search__field"><input type="search" placeholder="Buscar: factura, esquinas, Azul Cielo…" aria-label="Buscar"></div>
      <div class="search__res" role="listbox"></div>
      <div class="search__foot"><span><kbd>Flechas</kbd>Moverte</span><span><kbd>Enter</kbd>Abrir</span><span><kbd>Esc</kbd>Cerrar</span></div>
    </div>`;
  body.appendChild(sb);
  const input = sb.querySelector('input');
  const res = sb.querySelector('.search__res');
  let sel = 0, hits = [];
  const norm = (s) => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  const draw = () => {
    const q = norm(input.value.trim());
    hits = (q ? flat.filter((f) => norm(f.t + ' ' + f.path).includes(q)) : flat.filter((f) => f.href)).slice(0, 12);
    sel = Math.min(sel, Math.max(hits.length - 1, 0));
    res.innerHTML = hits.length ? hits.map((h, i) => {
      const inner = `<span class="r-body"><span class="r-t">${esc(h.t)}</span><br><span class="r-path">${esc(h.path)}</span></span>${dot(h.s)}`;
      const c = i === sel ? ' is-sel' : '';
      return h.href ? `<a class="${c}" href="${url(h.href)}" role="option">${inner}</a>` : `<div class="r${c}" role="option" aria-disabled="true">${inner}</div>`;
    }).join('') : `<div class="search__empty">Nada con ese nombre todavía.</div>`;
  };
  const open = () => { sb.classList.add('is-open'); input.value = ''; sel = 0; draw(); setTimeout(() => input.focus(), 10); };
  const close = () => sb.classList.remove('is-open');
  input.addEventListener('input', () => { sel = 0; draw(); });
  const mark = () => res.querySelectorAll('[role="option"]').forEach((el, k) => el.classList.toggle('is-sel', k === sel));
  res.addEventListener('mousemove', (e) => {
    const o = e.target.closest('[role="option"]');
    if (!o) return;
    const k = [...res.querySelectorAll('[role="option"]')].indexOf(o);
    if (k !== sel) { sel = k; mark(); }
  });
  sb.addEventListener('click', (e) => { if (e.target === sb) close(); });
  document.addEventListener('click', (e) => { if (e.target.closest('[data-search]')) open(); });
  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); sb.classList.contains('is-open') ? close() : open(); return; }
    if (!sb.classList.contains('is-open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowDown') { e.preventDefault(); sel = Math.min(sel + 1, hits.length - 1); mark(); }
    if (e.key === 'ArrowUp') { e.preventDefault(); sel = Math.max(sel - 1, 0); mark(); }
    if (e.key === 'Enter' && hits[sel] && hits[sel].href) location.href = url(hits[sel].href);
  });

  /* ─── Copiar al portapapeles ─── */
  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.setAttribute('role', 'status');
  body.appendChild(toast);
  let tt;
  const say = (m) => { toast.innerHTML = ic(I.check) + esc(m); toast.classList.add('is-on'); clearTimeout(tt); tt = setTimeout(() => toast.classList.remove('is-on'), 1800); };
  const copy = async (text, msg) => {
    try { await navigator.clipboard.writeText(text); } catch (_) {
      const t = document.createElement('textarea'); t.value = text; body.appendChild(t); t.select();
      try { document.execCommand('copy'); } catch (__) {} t.remove();
    }
    say(msg);
  };
  document.addEventListener('click', (e) => {
    const s = e.target.closest('[data-copy]');
    if (s) copy(s.dataset.copy, s.dataset.copyMsg || 'Copiado · ' + s.dataset.copy);
    const c = e.target.closest('[data-copy-code]');
    if (c) copy(c.closest('.code').querySelector('pre').innerText, 'Código copiado');
  });
})();
