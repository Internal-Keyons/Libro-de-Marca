/* ═══════════════════════════════════════════════════════════════
   KEYONS · MANUAL DE MARCA · comportamiento
   Funciona abriendo los archivos directamente, sin servidor.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  const NAV = window.KEYONS_NAV || [];
  /* Libro: cada manual de la Biblioteca declara su portada, su menú y sus enlaces secundarios.
     Sin declaración se usan los valores del Libro de Marca. */
  const BOOK = window.KEYONS_BOOK || {};
  const HOME = BOOK.home || 'inicio.html';
  const body = document.body;
  const ROOT = (body.dataset.root || '.').replace(/\/$/, '');
  const PAGE = body.dataset.page || '';
  const AREA = body.dataset.area || '';
  const IS_HOME = body.classList.contains('is-home');
  const url = (h) => ROOT + '/' + h;
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const $ = (id) => document.getElementById(id);

  /* Foco solo con teclado (reglas-visuales 4.5): Tab, flechas, Inicio y Fin encienden el anillo; un clic o un toque lo apagan.
     Shift, Windows, Ctrl o Alt solos (por ejemplo, para una captura de pantalla) no lo encienden. */
  const KBD = ['Tab', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'Home', 'End', 'PageUp', 'PageDown'];
  document.addEventListener('keydown', (e) => { if (KBD.includes(e.key) && !e.metaKey && !e.ctrlKey && !e.altKey) document.documentElement.setAttribute('data-kbd', ''); }, true);
  document.addEventListener('pointerdown', () => document.documentElement.removeAttribute('data-kbd'), true);

  const ic = (d, cls = '') => `<svg class="${cls}" viewBox="0 0 16 16" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${d}</svg>`;
  const I = {
    search: '<circle cx="7" cy="7" r="4.6"/><path d="m10.4 10.4 3.2 3.2"/>',
    chev: '<path d="m6 3.5 4.5 4.5L6 12.5"/>',
    right: '<path d="M3 8h10M9.2 4.2 13 8l-3.8 3.8"/>',
    left: '<path d="M13 8H3M6.8 4.2 3 8l3.8 3.8"/>',
    up: '<path d="M8 13V3M4.2 6.8 8 3l3.8 3.8"/>',
    check: '<path d="M3 8.5 6.2 12 13 4.5"/>',
    down: '<path d="M8 2.5v8M4.6 7.4 8 10.8l3.4-3.4M3 13.5h10"/>',
    code: '<path d="M5.5 4.5 2 8l3.5 3.5M10.5 4.5 14 8l-3.5 3.5"/>'
  };
  const LOGO = '<svg viewBox="0 0 1080 1080" aria-hidden="true"><path d="M640.8,418.74h-114.75c6.09,15.64,13.97,28.56,24.93,39.18,7.37.01,15.88-8.08,24.73-7.55v41.57c-8.85.62-17.36-7.41-24.74-7.41-10.44,9.97-18.92,23.62-24.87,39.21h114.7v39.38h-201.52c-.03-1.13-.05-2.49-.05-3.63,0-43.3,35.25-72.17,69.63-88.27-34.11-15.75-69.63-44.93-69.63-88.23,0-1.14.02-2.51.05-3.63h201.52v39.38Z"/><path d="M425.72,559.46c0,1.13-.02,2.55-.05,3.67h-77.4c-1.47-18.79-10.36-50.84-27.66-72.3h-31.42v72.3h-65.05v-247.85h65.05v136.29h31.43c17.3-21.46,26.18-53.43,27.65-72.22h77.4c.03,1.13.05,2.47.05,3.6,0,43.31-35.94,72.76-69.79,88.25,34.21,16.01,69.79,44.95,69.79,88.26Z"/><path d="M640.79,581.04v183.68h-65.24l-71.08-111.51v111.51h-65.24v-183.68h65.24l71.08,111.51v-111.51h65.24Z"/><path d="M855.83,563.13v-183.78h-77.48c-1.59,21.81-2.8,69.74-23.27,75.25-20.47-5.5-21.68-53.44-23.27-75.25h-77.51s0,2.99,0,2.99c0,55.66,45.12,83.15,100.77,83.15h0c23.14,0,44.46-4.75,61.46-14.31v72.65h0v23.09c-4.38-12.94-12.47-22.91-29.44-23.19h-132.8v39.39h201.54-.02Z"/><path d="M719.09,597.28v55.91s114.19,0,114.19,0c12.47,0,22.57,10.17,22.57,22.71v66.1c0,12.54-10.1,22.71-22.57,22.71h-178.98v-39.37h107.45c16.9.28,24.95,10.17,29.31,23.13v-55.91h-115.07c-11.98,0-21.69-9.77-21.69-21.83v-67.88c0-12.05,9.71-21.82,21.69-21.82h179.86v39.37h-107.45c-16.9-.28-24.95-10.17-29.31-23.13Z"/><path d="M245.84,581.04c-11.98,0-21.69,9.71-21.69,21.69v134.99h0v5.3c0,11.98,9.71,21.69,21.69,21.69h158.18c11.98,0,21.69-9.71,21.69-21.69v-140.29c0-11.98-9.71-21.69-21.69-21.69h-158.18ZM289.2,725.44v-104.94h71.49v104.85l-71.49.09Z"/></svg>';
  /* Estados documentales. El Sistema de Diseño suma los suyos y cambia el nombre de algunos (KEYONS_BOOK.status) */
  const STATUS = Object.assign({ v: 'Vigente', b: 'Borrador', p: 'Por definir', e: 'Estructura definida', r: 'En revisión', d: 'Descontinuado' }, BOOK.status || {});
  const SKEY = { v: 'vigente', b: 'borrador', p: 'pendiente', e: 'estructura', r: 'revision', d: 'descontinuado' };
  const LEGEND = BOOK.legend || ['v', 'b', 'p'];
  /* Nombres de los niveles en la página de área: Marca cuenta capítulos y páginas; el Sistema de Diseño, módulos y capítulos */
  const W = Object.assign({ ch: 'Capítulos', pg: 'Páginas', pgs: 'páginas' }, BOOK.words || {});
  const counted = (it) => it.t && !it.idx;
  const dot = (s = 'p') => `<span class="dot dot--${SKEY[s]}" role="img" title="${STATUS[s]}" aria-label="${STATUS[s]}"></span>`;
  /* Niveles de norma · reglas-visuales R16: tres niveles; «No debe» usa la marca de Debe */
  const LEVEL = { debe: 'Debe', deberia: 'Debería', puede: 'Puede' };
  const LEVEL_TIP = {
    debe: 'Obligatorio, sin excepciones. «No debe» usa esta misma marca.',
    deberia: 'Lo que se hace por defecto. Otra solución necesita un motivo escrito.',
    puede: 'Una alternativa permitida, a elección.'
  };
  const lvl = (k) => `<span class="nvl" tabindex="0" data-lvl="${k}" aria-label="${LEVEL[k]}: ${LEVEL_TIP[k]}"><i class="nvl__m nvl__m--${k}" aria-hidden="true"></i>${LEVEL[k]}</span>`;
  /* Ancla estable por clave: el número de capítulo puede cambiar, la clave no */
  const slug = (c) => 'cap-' + (c.k || c.n);
  const base = (h) => (h || '').split('#')[0];
  const hash = (h) => (h || '').split('#')[1] || '';

  /* Los seis libros de la Biblioteca. Generado por tools/biblioteca.py desde data/libros.json: no se edita a mano.
     on: se puede abrir (acceso); e: estado editorial de su contenido. Un libro abierto puede estar en construcción. */
  /* libros:inicio */
  const LIBROS = [
    { id: 'marca', t: 'Marca y Experiencia', c: 'Marca', tr: 'v', h: 'inicio.html', on: true, e: 'disponible', el: 'Disponible' },
    { id: 'sistema-diseno', t: 'Sistema de Diseño', c: 'Diseño', tr: 'g', h: 'sistema-diseno/index.html', on: true, e: 'construccion', el: 'En construcción' },
    { id: 'producto', t: 'Producto e Ingeniería', c: 'Producto', tr: 'x', e: 'preparacion', el: 'En preparación' },
    { id: 'ventas', t: 'Ventas y Crecimiento', c: 'Ventas', tr: 'd', e: 'preparacion', el: 'En preparación' },
    { id: 'servicio', t: 'Servicio al Cliente', c: 'Servicio', tr: 'c', e: 'preparacion', el: 'En preparación' },
    { id: 'cultura', t: 'Cultura y Operaciones', c: 'Cultura', tr: 'h', e: 'preparacion', el: 'En preparación' },
  ];
  /* libros:fin */
  /* Trama oficial de cada libro, dibujada en línea fina: v verticales, h horizontales, d diagonales,
     x diagonales cruzadas, g retícula, c curvas concéntricas */
  const trama = (k) => {
    /* Centradas en el lienzo: la línea central pasa por el medio, sin desplazarse hacia un lado */
    const L = [], S = 10, D = 14;
    if (k === 'v' || k === 'g') for (let i = -8; i <= 8; i++) L.push(`M${80 + i * S} 0V100`);
    if (k === 'h' || k === 'g') for (let i = -5; i <= 5; i++) L.push(`M0 ${50 + i * S}H160`);
    if (k === 'd' || k === 'x') for (let i = -9; i <= 9; i++) { const x = 80 + i * D; L.push(`M${x - 50} 100L${x + 50} 0`); }
    if (k === 'x') for (let i = -9; i <= 9; i++) { const x = 80 + i * D; L.push(`M${x - 50} 0L${x + 50} 100`); }
    if (k === 'c') for (let r = 10; r < 190; r += S) L.push(`M${80 - r} 100A${r} ${r} 0 0 1 ${80 + r} 100`);
    return `<svg viewBox="0 0 160 100" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><path d="${L.join('')}" fill="none" stroke="currentColor" stroke-width="1" vector-effect="non-scaling-stroke"/></svg>`;
  };
  /* Nubes: anchos 200–420 px, opacidad 20–45 %, desenfoque 12–24 px, recorrido 44–82 s */
  const nubes = () => [[200, .32, 12, 44, 8], [420, .2, 24, 82, -6], [280, .45, 16, 58, 30], [340, .26, 20, 70, -18], [240, .38, 14, 52, 46], [380, .22, 22, 76, 14]]
    .map(([w, o, b, d, y], i) => `<span class="haze" style="width:${w}px;height:${Math.round(w * .38)}px;top:${y}px;opacity:${o};filter:blur(${b + 10}px);animation-duration:${d}s;animation-delay:-${(i * 13.7 + d * .37).toFixed(1)}s"></span>`).join('');
  const BOOK_ID = BOOK.id || 'marca';
  /* La Guía es un recurso común, no un séptimo libro: ningún libro queda como «actual» y la cabecera nombra la Biblioteca sin trama */
  const EN_GUIA = BOOK_ID === 'biblioteca';
  const LIBRO = EN_GUIA ? { id: 'biblioteca', t: 'Biblioteca Keyons', c: 'Biblioteca', tr: '', h: 'index.html', on: true } : (LIBROS.find((b) => b.id === BOOK_ID) || LIBROS[0]);

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
  flat.unshift(...LIBROS.filter((b) => b.on).map((b) => ({ t: b.t, href: b.h, s: 'v', lib: b.id, path: b.el })));

  /* Cada libro de la Biblioteca lleva su trama en encabezados y subencabezados (css: --trama) */
  document.documentElement.dataset.libro = (window.KEYONS_BOOK || {}).id || 'marca';

  /* ─── Cabecera · misma especificación que el sitio web ─── */
  const top = $('topbar');
  if (top) {
    const clouds = nubes();
    top.className = 'hdr' + (IS_HOME ? ' hdr--home' : '');
    top.innerHTML = `
      <div class="hdr__bg">${IS_HOME ? `<div class="hdr__clouds" aria-hidden="true">${clouds}</div>` : ''}</div>
      <div class="hdr__in">
        <div class="hdr__left">
          <button class="hdr__book" type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="bks" aria-label="${esc(LIBRO.t)} · Cambiar de libro"><span class="hdr__book-art bks__art">${trama(LIBRO.tr)}</span><span class="hdr__book-t">${esc(LIBRO.t)}</span><span class="hdr__book-c">${esc(LIBRO.c)}</span>${ic(I.chev)}</button>
        </div>
        <a class="hdr__logo" href="${url(LIBRO.h || 'index.html')}" aria-label="${esc(LIBRO.t)} · Portada">${LOGO}</a>
        <div class="hdr__right">
          ${BOOK_ID === 'sistema-diseno' ? `<a class="hdr__lab" href="${url('sistema-diseno/laboratorio.html')}" aria-label="Laboratorio de Interfaces"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 3.5h6M10 3.5v6L4.8 18.3A1.9 1.9 0 0 0 6.4 21h11.2a1.9 1.9 0 0 0 1.6-2.7L14 9.5v-6"/><path d="M7.4 15.5h9.2"/></svg><span>Lab</span></a>` : ''}
          <button class="hdr__search" type="button" data-search aria-label="Buscar en la Biblioteca (Ctrl K)">${ic(I.search)}<span>Buscar</span><kbd>Ctrl K</kbd></button>
        </div>
      </div>`;
    /* Selector global de libros: vista completa, como el cambio de perfiles.
       En móvil sube desde abajo; en escritorio aparece con una transición editorial discreta. */
    const CH = '<svg class="ic" viewBox="0 0 32 32" aria-hidden="true"><path transform="matrix(1,0,0,-1,13.4475,25.0231)" d="M0 0-1.987 1.846 4.184 8.489C4.454 8.779 4.454 9.234 4.185 9.525L-1.989 16.206 .002 18.046 6.177 11.366C7.402 10.04 7.399 7.966 6.171 6.643Z" fill="currentColor"/></svg>';
    const tile = (b, cls) => {
      const inner = `<span class="bks__art">${trama(b.tr)}</span><span class="bks__n">${esc(b.t)}</span>${b.on ? (b.e === 'disponible' ? '' : `<span class="bks__s">${esc(b.el)}</span>`) : `<span class="bks__s">${esc(b.el)}</span>`}`;
      return b.on ? `<a class="${cls}" href="${url(b.h)}"${b.id === BOOK_ID ? ' aria-current="true"' : ''}>${inner}</a>` : `<span class="${cls} is-off" aria-disabled="true">${inner}</span>`;
    };
    const bks = document.createElement('div');
    bks.className = 'bks'; bks.id = 'bks'; bks.hidden = true;
    bks.setAttribute('role', 'dialog'); bks.setAttribute('aria-modal', 'true'); bks.setAttribute('aria-labelledby', 'bks-t');
    bks.innerHTML = `<div class="bks__panel">
      <div class="bks__top"><h2 class="bks__h" id="bks-t">Biblioteca Keyons</h2><button class="bks__x" type="button" aria-label="Cerrar">${ic('<path d="M4 4l8 8M12 4l-8 8"/>')}</button></div>
      ${EN_GUIA ? '' : `<div class="bks__cur">${tile(LIBRO, 'bks__card')}<span class="bks__k">Libro actual</span></div>`}
      <ul class="bks__list${EN_GUIA ? ' bks__list--todos' : ''}">${LIBROS.filter((b) => b !== LIBRO).map((b) => `<li>${tile(b, 'bks__it')}</li>`).join('')}</ul>
      <a class="bks__guide" href="${url('guia/index.html')}">Guía de la Biblioteca</a>
      <nav class="bks__rows" aria-label="Biblioteca">
        <a href="${url('index.html')}"><span>Portada de la Biblioteca</span>${CH}</a>
        <button type="button" data-search><span>Buscar en la Biblioteca</span>${CH}</button>
      </nav>
    </div>`;
    body.appendChild(bks);
    const bk = top.querySelector('.hdr__book');
    let bkT = 0;
    const setBooks = (o, back) => {
      clearTimeout(bkT);
      bk.setAttribute('aria-expanded', String(o));
      if (o) {
        bks.hidden = false; body.classList.add('bks-open');
        requestAnimationFrame(() => requestAnimationFrame(() => bks.classList.add('is-in')));
        setTimeout(() => (bks.querySelector('.bks__card') || bks.querySelector('a.bks__it') || bks.querySelector('.bks__x')).focus({ preventScroll: true }), 60);
      } else {
        bks.classList.remove('is-in'); body.classList.remove('bks-open');
        bkT = setTimeout(() => { bks.hidden = true; }, 420);
        if (back !== false) bk.focus({ preventScroll: true });
      }
    };
    /* Ctrl+K o «Buscar en la Biblioteca» con el selector abierto: se cierra y la búsqueda queda encima, sin dos ventanas apiladas */
    window.KEYONS_CERRAR_LIBROS = () => { if (!bks.hidden) setBooks(false, false); };
    bk.addEventListener('click', () => setBooks(true));
    bks.querySelector('.bks__x').addEventListener('click', () => setBooks(false));
    bks.addEventListener('click', (e) => { if (e.target === bks) setBooks(false); if (e.target.closest('[data-search]')) setBooks(false, false); });
    document.addEventListener('keydown', (e) => {
      if (bks.hidden) return;
      if (e.key === 'Escape') setBooks(false);
      if (e.key === 'Tab') {
        const f = [...bks.querySelectorAll('a, button')];
        if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
        else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
      }
    });
    if (IS_HOME) {
      const hero = document.querySelector('.hero');
      const check = () => top.classList.toggle('is-solid', !hero || hero.getBoundingClientRect().bottom <= top.offsetHeight);
      addEventListener('scroll', check, { passive: true });
      check();
    }
  }

  /* ─── Referencias que llevan a su sección ───
     Cada ID (KYN-MRK-COL-014), «capítulo 14» o «(14)» del texto se vuelve un enlace a esa sección. */
  {
    const sx = document.createElement('script');
    sx.src = (document.body.dataset.root || '.') + '/js/secciones.js';
    sx.onload = () => {
      const S = window.KEYONS_SECS || {}, C = window.KEYONS_CAPS || {}, root = (document.body.dataset.root || '.') + '/';
      const N = window.KEYONS_NORMAS || [], byH = {}, byId = {};
      N.forEach((o) => { if (!byH[o.h] || o.e === 'vigente') byH[o.h] = o; byId[o.id] = o; });
      const base = decodeURI(new URL(root, location.href).pathname), here = decodeURI(location.pathname).slice(base.length);
      const moved = (window.KEYONS_ALIAS || {})[here + location.hash];
      if (moved) { location.replace(root + moved); return; }
      /* El buscador también encuentra cada norma por su ID, su código corto, su título, su título interior y sus nombres anteriores */
      N.forEach((o) => {
        if (o.e === 'descontinuada') return;
        const corto = o.id.replace('KYN-MRK-', '');
        flat.push({ t: o.t, href: o.h, s: o.e === 'vigente' ? 'v' : 'b', norma: true,
          path: o.id + (o.en ? ' · integrada en ' + o.en : '') + (o.a && o.a.length ? ' · ' + o.a[o.a.length - 1] : ''),
          k: [o.id, corto, o.n, ...(o.a || [])].join(' ') });
      });
      document.querySelectorAll('section.ed[id] > .ed__label').forEach((lb) => {
        const o = byH[`${here}#${lb.parentElement.id}`];
        /* Toda norma con ID lo muestra en su rótulo, también en borrador (un capítulo sin ID no existe) */
        if (!o || !['vigente', 'borrador'].includes(o.e)) return;
        const num = lb.firstElementChild;
        num.dataset.n = num.textContent; num.textContent = o.id; num.classList.add('ed__code');
        num.dataset.copy = o.id; num.dataset.copyMsg = 'ID copiado · ' + o.id; num.title = 'Copiar el ID de esta norma';
      });
      /* Autoridad normativa: estado y versión de cada norma, discretos, desde data/autoridad.json */
      const sa = document.createElement('script');
      sa.src = root + 'js/autoridad.js';
      sa.onload = () => document.querySelectorAll('.ed__label .ed__code').forEach((c) => {
        const a = (window.KEYONS_AUT || {})[c.dataset.copy];
        if (a && !c.parentElement.querySelector('.ed__auth')) c.parentElement.insertAdjacentHTML('beforeend', `<span class="ed__auth">${esc(a[0])} · v${esc(a[1])}</span>`);
      });
      document.head.appendChild(sa);
      document.querySelectorAll('[data-normas]').forEach((box) => {
        const list = box.querySelector('.kidx__list'), q = box.querySelector('.kidx__q');
        /* El encabezado de cada grupo es la familia (o la letra); la fila solo lleva su número */
        const fams = {};
        document.querySelectorAll('.kcodes li, #nomenclatura li').forEach((li) => { const b = li.querySelector('b'), t = li.querySelector('span'); if (b && t) fams[b.textContent.trim()] = t.textContent.trim(); });
        const num = (x) => x.split('.').map(Number);
        const cmp = (a, b) => { const p = num(a.n), q = num(b.n); for (let i = 0; i < Math.max(p.length, q.length); i++) { const d = (p[i] || 0) - (q[i] || 0); if (d) return d; } return 0; };
        const fila = (o, alfa) => {
          const [, , f, c] = o.id.split('-');
          const off = o.e === 'descontinuada' || o.e === 'integrada';
          return `<a class="kidx__r${off ? ' is-off' : ''}" href="${root}${o.h}" title="${o.id}" data-q="${(o.id + ' ' + o.n + ' ' + o.t).toLowerCase()}"><b>${alfa ? f + '-' + c : c}</b><span class="kidx__t">${o.t}</span><span class="kidx__n">${off ? '[DESCONTINUADA]' : o.n}</span></a>`;
        };
        const draw = (key) => {
          const alfa = key === 't', gr = new Map();
          [...N].sort(alfa ? (a, b) => a.t.localeCompare(b.t, 'es') : cmp).forEach((o) => {
            const k = alfa ? o.t.normalize('NFD')[0].toUpperCase() : o.id.split('-')[2];
            if (!gr.has(k)) gr.set(k, []);
            gr.get(k).push(o);
          });
          list.classList.toggle('kidx__list--a', alfa);
          list.innerHTML = [...gr].map(([k, os]) => `<div class="kidx__g"><h4 class="kidx__h"><i>/</i>${k}</h4><p class="kidx__f">${alfa ? os.length + (os.length === 1 ? ' norma' : ' normas') : 'KYN-MRK-' + k + (fams[k] ? ' · ' + fams[k] : '')}</p><div class="kidx__rows">${os.map((o) => fila(o, alfa)).join('')}</div></div>`).join('');
          q.dispatchEvent(new Event('input'));
        };
        box.querySelectorAll('[data-ks]').forEach((b) => b.addEventListener('click', () => {
          box.querySelectorAll('[data-ks]').forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
          draw(b.dataset.ks);
        }));
        q.addEventListener('input', () => { const v = q.value.trim().toLowerCase(); list.querySelectorAll('.kidx__r').forEach((r) => { r.hidden = !!v && !r.dataset.q.includes(v); }); list.querySelectorAll('.kidx__g').forEach((g) => { g.hidden = !g.querySelector('.kidx__r:not([hidden])'); }); const nn = list.querySelectorAll('.kidx__r:not([hidden])').length, ct = box.querySelector('.kidx__count'); if (ct) ct.textContent = nn + (nn === 1 ? ' norma' : ' normas'); list.scrollLeft = 0; list.dispatchEvent(new Event('scroll')); });
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
          /* Los números de capítulo solo se enlazan dentro del Libro de Marca; los ID KYN-MRK se enlazan desde cualquier libro */
          else if (BOOK.home) continue;
          else if (m[3] && C[String(+m[3])]) { href = C[String(+m[3])]; pre = m[2]; label = m[3]; }
          /* Un número suelto («6.15») ya no se enlaza: las citas se escriben por ID. Así «WCAG 2.1» o «6.5 : 1» no apuntan a una norma */
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
    /* Un portal --plano muestra solo el color de su área, sin cielo animado */
    if (p.matches('.portal--photo, .portal--img, .portal--plano')) return;
    const sky = p.matches('.portal--cielo') ? 'mediodia' : p.matches('.portal--salmon') ? 'atardecer' : 'noche';
    cielos.push([p, sky, document.body.dataset.page || location.pathname, true]);
  });
  /* Muestras de cielo dentro del contenido (ESP-006, Secuencia Prisma): el mismo cielo en código, una fase por muestra */
  document.querySelectorAll('[data-cielo]').forEach((el) => cielos.push([el, el.dataset.cielo, 'muestra-' + el.dataset.cielo]));
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

  /* Tipografía: la escala editable (8.2), el probador (8.3) y las referencias V1 leen KEYONS_TIPO */
  const TIPO = window.KEYONS_TIPO;
  const tNum = (v) => String(v).replace('.', ',');
  const tPct = (v) => (v > 0 ? '+' : v < 0 ? '−' : '') + tNum(Math.abs(v)) + ' %';
  const tLv = (k) => {
    if (!TIPO) return null;
    const n = TIPO.niveles.find((x) => x.k === k);
    if (n) return n;
    const r = TIPO.roles[k];
    return { ...TIPO.niveles.find((x) => x.k === r.base), ...(r.peso ? { peso: r.peso } : {}) };
  };
  const tName = (k) => { const n = TIPO.niveles.find((x) => x.k === k); return n ? n.n : TIPO.roles[k].n; };
  const tRango = (n) => (n.min === n.max ? `${n.min} px` : `${n.min} a ${n.max} px`);

  /* Menú desplegable de la casa (el mismo del formulario): reemplaza visualmente a un select, que conserva el estado */
  const CHEV = '<svg viewBox="0 0 32 32" aria-hidden="true"><path transform="matrix(1,0,0,-1,13.4475,25.0231)" d="M0 0-1.987 1.846 4.184 8.489C4.454 8.779 4.454 9.234 4.185 9.525L-1.989 16.206 .002 18.046 6.177 11.366C7.402 10.04 7.399 7.966 6.171 6.643Z" fill="currentColor"/></svg>';
  function kdd(sel) {
    const lab = sel.closest('label'), name = lab ? lab.querySelector('.paren').textContent.replace(/[()]/g, '') : '';
    const d = document.createElement('div');
    d.className = 'kdd';
    d.innerHTML = `${name ? `<span class="kdd__t">${esc(name)}</span>` : ''}<button class="kdd__btn" type="button" aria-haspopup="listbox" aria-expanded="false" aria-label="${esc(name)}"><span class="kdd__v"></span><span class="kdd__ch">${CHEV}</span></button><ul class="kdd__list" role="listbox" aria-label="${esc(name)}"></ul>`;
    (lab || sel).after(d);
    if (lab) lab.hidden = true;
    const btn = d.querySelector('.kdd__btn'), list = d.querySelector('.kdd__list'), val = d.querySelector('.kdd__v');
    const paint = () => {
      val.textContent = sel.options[sel.selectedIndex] ? sel.options[sel.selectedIndex].text : '';
      list.innerHTML = [...sel.options].map((o, i) => `<li class="kdd__o" role="option" data-i="${i}" aria-selected="${i === sel.selectedIndex}">${esc(o.text)}</li>`).join('');
    };
    const open = (on) => {
      if (on) document.querySelectorAll('.kdd.is-open').forEach((x) => { if (x !== d) { x.classList.remove('is-open'); x.querySelector('.kdd__btn').setAttribute('aria-expanded', 'false'); } });
      d.classList.toggle('is-open', on); btn.setAttribute('aria-expanded', String(on));
    };
    btn.addEventListener('click', () => open(!d.classList.contains('is-open')));
    list.addEventListener('click', (e) => {
      const o = e.target.closest('.kdd__o');
      if (!o) return;
      sel.selectedIndex = Number(o.dataset.i); sel.dispatchEvent(new Event('change')); paint(); open(false); btn.focus();
    });
    d.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') { open(false); btn.focus(); }
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault();
        sel.selectedIndex = Math.min(sel.options.length - 1, Math.max(0, sel.selectedIndex + (e.key === 'ArrowDown' ? 1 : -1)));
        sel.dispatchEvent(new Event('change')); paint();
      }
    });
    document.addEventListener('click', (e) => { if (!d.contains(e.target) && d.classList.contains('is-open')) open(false); });
    sel.addEventListener('kdd:sync', paint);
    paint();
  }
  /* Cualquier select marcado data-kdd toma el desplegable de la casa (Laboratorio de Interfaces) */
  document.querySelectorAll('select[data-kdd]').forEach(kdd);


  /* 8.2 · Escriba un tamaño en cualquier nivel: todos los demás se escalan en la misma proporción.
     Lo que cae fuera de la escala de lectura (12 · 14 · 16 · 20 · 24 · 32) o del rango de exhibición queda marcado. */
  const PEN = '<svg class="szc__pen" viewBox="0 0 32 32" aria-hidden="true"><path d="M20.5 6.5l5 5L12 25H7v-5z" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linejoin="miter"/><path d="M17.5 9.5l5 5" fill="none" stroke="currentColor" stroke-width="2.5"/></svg>';
  const ESCALA = [12, 14, 16, 20, 24, 32];
  const enEscala = (n, v) => (n.min === n.max ? ESCALA.includes(v) : v >= n.min && v <= n.max);
  document.querySelectorAll('[data-escala]').forEach((g) => {
    if (!TIPO) return;
    g.innerHTML = TIPO.niveles.map((n) => `<div class="szc" data-k="${n.k}"><span class="szc__k">${n.n}</span><p class="szc__v"><input type="text" inputmode="numeric" maxlength="3" value="${n.min}" aria-label="${n.n}, tamaño en px"><sup>px</sup>${PEN}</p><p class="szc__m">${TIPO.familias[n.f]} · <span>${tRango(n)}</span></p></div>`).join('');
    const reset = document.createElement('button');
    reset.type = 'button'; reset.className = 'szc-reset'; reset.textContent = 'Restablecer'; reset.hidden = true;
    g.after(reset);
    const fit = (i) => { if (!CSS.supports('field-sizing', 'content')) i.style.width = `${Math.max(1, i.value.length) + 0.15}ch`; };
    const cells = [...g.querySelectorAll('.szc')];
    const mark = (c, n, v) => {
      const out = !enEscala(n, v);
      c.classList.toggle('is-out', out);
      c.querySelector('.szc__m span').textContent = out ? (n.min === n.max ? 'Fuera de la escala' : `Fuera del rango ${tRango(n)}`) : tRango(n);
    };
    const apply = (src, v) => {
      const k = v / tLv(src.dataset.k).min;
      cells.forEach((c) => {
        const n = tLv(c.dataset.k), i = c.querySelector('input');
        const nv = c === src ? v : Math.round(n.min * k);
        if (c !== src) { i.value = nv; fit(i); }
        mark(c, n, nv);
      });
      reset.hidden = k === 1;
    };
    cells.forEach((c) => {
      const i = c.querySelector('input');
      fit(i);
      i.addEventListener('input', () => {
        i.value = i.value.replace(/\D/g, ''); fit(i);
        const v = parseInt(i.value, 10);
        if (v > 0) apply(c, v);
      });
      c.querySelector('.szc__pen').addEventListener('click', () => i.focus());
      i.addEventListener('blur', () => { if (!i.value) { i.value = tLv(c.dataset.k).min; fit(i); apply(c, +i.value); } });
    });
    reset.addEventListener('click', () => {
      cells.forEach((c) => {
        const i = c.querySelector('input'), n = tLv(c.dataset.k);
        c.classList.remove('is-out'); c.querySelector('.szc__m span').textContent = tRango(n);
        i.value = n.min; fit(i);
      });
      reset.hidden = true;
    });
  });

  /* 8.2 · Lectura prolongada: valores de referencia */
  document.querySelectorAll('[data-lectura] [data-l]').forEach((d) => {
    const v = TIPO && TIPO.lectura[d.dataset.l];
    if (!v) return;
    d.textContent = d.dataset.l === 'cuerpo' ? (v[0] === v[1] ? `${v[0]} px` : `${v[0]}–${v[1]} px`) : `${tNum(v[0])}–${tNum(v[1])}`;
  });

  /* 8.3 · Referencias V1 a la vista: una tabla por jerarquía */
  document.querySelectorAll('[data-tipo-v1]').forEach((box) => {
    if (!TIPO) return;
    const row = (k, vals) => `<div class="matrix__row" role="row"><span class="matrix__k" role="rowheader">${tName(k)}</span>${vals.map((v) => `<span class="matrix__v" role="cell">${v} px</span>`).join('')}</div>`;
    const head = (cols) => `<div class="matrix__row matrix__head" role="row"><span class="matrix__k" role="columnheader">(Nivel)</span>${cols.map((c) => `<span class="matrix__lvl" role="columnheader">${c}</span>`).join('')}</div>`;
    const c = TIPO.v1['trad-contenida'], e = TIPO.v1['trad-expresiva'], inv = TIPO.v1['inv-contenida'], ie = TIPO.v1['inv-expresiva'];
    const [t1, t2] = box.querySelectorAll('.tv1__t');
    t1.insertAdjacentHTML('afterend', `<div class="matrix" role="table" aria-label="Jerarquía tradicional">${head(['Contenida', 'Expresiva'])}${c.map(([k, px]) => row(k, [px, e.find((x) => x[0] === k)[1]])).join('')}</div>`);
    t2.insertAdjacentHTML('afterend', `<div class="matrix" role="table" aria-label="Jerarquía editorial invertida">${head(['Contenida', 'Expresiva'])}${inv.map(([k, px]) => row(k, [px, ie.find((x) => x[0] === k)[1]])).join('')}</div>`);
  });

  /* 8.3 · Probador: nivel, peso, interlineado y tracking; jerarquía, intensidad y organización */
  document.querySelectorAll('[data-tester]').forEach((tb) => {
    if (!TIPO) return;
    const LVK = { display: 'display', title: 'titulo', lead: 'entrada', body: 'cuerpo', kicker: 'kicker' };
    const CLS = { display: 'tsx--display', title: 'tsx--title', lead: 'tsx--lead', body: 'tsx--body', kicker: 'kicker tsx--kicker' };
    const OPT = { w: [400, 500, 600, 700], lh: [0.93, 1, 1.1, 1.2, 1.3, 1.4, 1.55, 1.6, 1.65], ls: [8, 0, -1.5, -2, -3, -4, -5] };
    const LAB = { w: String, lh: tNum, ls: tPct };
    const q = (x) => tb.querySelector(x);
    const out = q('.tester__out'), comp = q('.tester__comp'), sizes = q('.tester__sizes');
    const txt = () => out.textContent.trim() || ' ';   // el ejemplo se escribe en el lugar (clic para escribir)
    Object.keys(OPT).forEach((k) => { const s = q(`[data-ex="${k}"]`); if (s) s.innerHTML = OPT[k].map((v) => `<option value="${v}">${LAB[k](v)}</option>`).join(''); });
    let lv = 'display';
    const EX = {};
    const setLv = () => {
      const n = tLv(LVK[lv]);
      EX.w = n.peso; EX.lh = n.lh; EX.ls = n.tr;
      ['w', 'lh', 'ls'].forEach((k) => { const s = q(`[data-ex="${k}"]`); if (s) { s.value = String(EX[k]); s.dispatchEvent(new Event('kdd:sync')); } });
    };
    const draw = () => {
      const n = tLv(LVK[lv]);
      out.className = 'tester__out ' + CLS[lv];
      out.style.fontWeight = EX.w; out.style.lineHeight = EX.lh; out.style.letterSpacing = `${EX.ls / 100}em`;
      q('[data-tx="f"]').textContent = TIPO.familias[n.f] + (n.mayus ? ' · mayúsculas' : '');
      q('[data-tx="px"]').textContent = tRango(n).replace(' a ', '–');
    };
    /* Composición de muestra: cada combinación con las fuentes oficiales */
    const CF = { j: 'trad', i: 'contenida', o: 'breve' };
    const TX = {
      titulo: 'Un mismo cielo, ningún horizonte igual', subtitulo: 'Cómo trabajamos', contexto: 'Quiénes somos',
      entrada: 'Los retos se repiten en cualquier industria, pero ninguna empresa los enfrenta desde el mismo horizonte.',
      cuerpo: 'Primero entendemos su operación; después construimos con su equipo y medimos cada mejora.',
      cierre: 'El cielo siempre está presente: una pieza sin cielo no es una pieza Keyons.',
    };
    const MOD = [['Diagnóstico', 'Primero entendemos su operación.'], ['Construcción', 'Después construimos con su equipo.'], ['Medición', 'Medimos cada mejora.']];
    const sizesFor = (j, i) => TIPO.v1[`${j}-${i}`];
    const el = (k, px, txt, cls = '') => {
      const n = tLv(k), tr = n.trDesde && px >= n.trDesde ? n.trMax : n.tr;
      return `<p class="tcx tcx--${k}${cls}" style="font-size:${px}px;font-weight:${n.peso};line-height:${n.lh};letter-spacing:${tr / 100}em">${esc(txt)}</p>`;
    };
    const drawComp = () => {
      if (!comp) return;
      const px = Object.fromEntries(sizesFor(CF.j, CF.i)), pro = txt();
      const used = [];
      const put = (k, txt, cls) => { if (!used.includes(k)) used.push(k); return el(k, px[k], txt, cls); };
      let h = '';
      if (CF.j === 'trad') {
        h += put('display', pro);
        if (CF.o === 'breve') h += put('entrada', TX.entrada);
        if (CF.o === 'lectura') h += put('titulo', TX.titulo) + put('subtitulo', TX.subtitulo) + put('entrada', TX.entrada) + `<div class="tcx__col">${put('cuerpo', TX.cuerpo)}${put('cuerpo', TX.cierre)}</div>`;
        if (CF.o === 'modular') h += `<div class="tcx__mods">${MOD.map(([t, d]) => `<div>${put('subtitulo', t)}${put('cuerpo', d)}</div>`).join('')}</div>`;
      } else {
        h += put('contexto', TX.contexto) + put('declaracion', pro);
        if (CF.o === 'lectura') h += put('entrada', TX.entrada) + `<div class="tcx__col">${put('cuerpo', TX.cuerpo)}${put('cuerpo', TX.cierre)}</div>`;
        if (CF.o === 'modular') h += `<div class="tcx__mods">${MOD.map(([t, d]) => `<div>${put('contexto', t)}${put('cuerpo', d)}</div>`).join('')}</div>`;
      }
      comp.className = `tester__comp tcx-${CF.j} tcx-${CF.o}`;
      comp.innerHTML = h;
      if (sizes) sizes.innerHTML = used.map((k) => `<span>${tName(k)} <b>${px[k]} px</b></span>`).join('');
    };
    tb.querySelectorAll('[data-ex]').forEach((s) => s.addEventListener('change', () => { EX[s.dataset.ex] = Number(s.value); draw(); }));
    tb.querySelectorAll('[data-cf]').forEach((s) => s.addEventListener('change', () => { CF[s.dataset.cf] = s.value; drawComp(); }));
    out.addEventListener('input', () => { if (out.textContent.length > 120) out.textContent = out.textContent.slice(0, 120); drawComp(); });
    out.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); out.blur(); } });   // una sola línea de texto
    tb.querySelectorAll('[data-lv]').forEach((b) => b.addEventListener('click', () => {
      lv = b.dataset.lv; tb.querySelectorAll('[data-lv]').forEach((o) => o.setAttribute('aria-pressed', o === b)); setLv(); draw();
    }));
    setLv(); draw(); drawComp();
    tb.querySelectorAll('select.tsel').forEach(kdd);
  });

  /* 8.8 · Tracking: si una muestra no cabe completa, se ve una variante a la vez */
  document.querySelectorAll('.trk').forEach((trk) => {
    const tabs = trk.parentElement.querySelector('.trk__tabs');
    if (!tabs) return;
    trk.dataset.v = '1';
    const fit = () => {
      if (tabs.hasAttribute('data-always')) { trk.classList.add('is-one'); tabs.hidden = false; return; }
      trk.classList.remove('is-one');
      const over = [...trk.querySelectorAll('.trk__s')].some((s) => s.scrollWidth > s.parentElement.clientWidth + 1);
      trk.classList.toggle('is-one', over); tabs.hidden = !over;
    };
    tabs.querySelectorAll('[data-trk]').forEach((b) => b.addEventListener('click', () => {
      trk.dataset.v = b.dataset.trk; tabs.querySelectorAll('[data-trk]').forEach((o) => o.setAttribute('aria-pressed', String(o === b)));
    }));
    fit(); addEventListener('load', fit); let ft; addEventListener('resize', () => { clearTimeout(ft); ft = setTimeout(fit, 150); });
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

  /* Viñetas: elegir un color permitido y copiar la forma en SVG */
  document.querySelectorAll('[data-vtool]').forEach((vt) => {
    let col = '#729BDD', name = 'Azul Cielo';
    vt.addEventListener('click', (e) => {
      const c = e.target.closest('[data-vc]');
      if (c) {
        col = c.dataset.vc; name = c.textContent.trim();
        vt.style.setProperty('--vt-c', col); vt.classList.toggle('is-dark', c.dataset.bg === '#10122A');
        vt.querySelectorAll('[data-vc]').forEach((o) => o.setAttribute('aria-pressed', String(o === c)));
        return;
      }
      const v = e.target.closest('[data-vf]'); if (!v) return;
      const svg = v.querySelector('svg').outerHTML.replace('viewBox="-2 -2 24 24" aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" width="20" height="20"').replace('currentColor', col);
      copy(svg, `SVG copiado · viñeta ${v.dataset.vf}, ${v.dataset.vn}, ${name}`);
    });
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
    /* Recorrido continuo: la primera diapositiva se repite al final (oculta para lectores de pantalla)
       y, al terminar la transición, el carrusel vuelve a la original sin que se note el regreso */
    const N = items.length;
    const clone = items[0].cloneNode(true);
    clone.setAttribute('aria-hidden', 'true'); clone.inert = true; clone.classList.add('is-clone');
    track.appendChild(clone);
    let pos = 0;
    const place = (p, anim) => {
      track.style.transition = anim && auto ? '' : 'none';
      track.style.transform = `translateX(-${p * 100}%)`;
      if (!(anim && auto)) void track.offsetWidth;
      pos = p;
    };
    track.addEventListener('transitionend', (e) => { if (e.target === track && pos === N) place(0, false); });
    const go = (n) => {
      if (n >= N) { place(N, true); i = 0; if (!auto) place(0, false); }
      else if (n < 0) { place(N, false); place(N - 1, true); i = N - 1; }
      else { place(n, true); i = n; }
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
    if (it.n) return it.n;
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
    const lid = `nav-ch-${area.id}-${c.k || c.n}`;
    return `<div class="nav-ch" aria-expanded="${open}">
      <button class="nav-ch__btn" type="button" aria-expanded="${open}" aria-controls="${lid}" title="${esc(c.n + ' ' + c.t)}"><span class="nav-ch__num">${c.n}</span><span>${esc(c.t)}</span>${ic(I.chev)}</button>
      <div class="nav-list" id="${lid}">${items}</div></div>`;
  }).join('');
  const area = NAV.find((x) => x.id === AREA);
  /* ─── Índice lateral del libro ───
     Áreas o módulos → capítulos → grupos → páginas y normas. En escritorio vive junto al contenido y el control
     «Índice» lo muestra u oculta; en móvil y en las portadas es un panel que se abre sobre la página. */
  const side = $('side');
  if (side) {
  const alt = BOOK.alt || [['Descargar PDF', 'documental/libro-de-marca-keyons.pdf', 'down', true], ['Normas para IA', 'ia/index.html', 'code']];
  const areaHtml = (a, i) => {
    const on = a === area;
    return `<div class="nav-area${on ? ' is-current' : ''}"><div class="nav-area__head">`
      + `<a class="nav-area__link" href="${url(a.href)}"${PAGE === a.href ? ' aria-current="page"' : ''}>${esc(a.t)}</a>`
      + `<button class="nav-area__btn" type="button" aria-expanded="${on}" aria-controls="nav-area-${i}" aria-label="${esc(a.t)}: ${on ? 'contraer' : 'desplegar'} capítulos">${ic(I.chev)}</button></div>`
      + `<div class="nav-area__body" id="nav-area-${i}"${on ? '' : ' hidden'}>${chapters(a)}</div></div>`;
  };
  side.innerHTML = `<nav class="side__tree" aria-label="Índice de ${esc(LIBRO.t)}">${NAV.map(areaHtml).join('')}</nav>`
    /* En el menú lateral, solo los niveles de norma; los estados se explican en la portada (reglas-visuales R16) */
    + `<div class="side__legend">${Object.keys(LEVEL).map(lvl).join('')}</div>`
    + `<div class="side__alt">${alt.map(([t, h, d, dl]) => `<a href="${url(h)}"${dl ? ' download' : ''}>${d ? ic(I[d] || d) : ''}${esc(t)}</a>`).join('')}</div>`
    /* Contraer: un control de panel al pie del menú, distinto de los chevrones de áreas y capítulos */
    + `<div class="side__foot"><button class="side__toggle" type="button" aria-pressed="false" aria-label="Contraer el menú lateral" title="Contraer el menú"><svg viewBox="0 0 20 20" aria-hidden="true"><rect x="2.75" y="3.75" width="14.5" height="12.5" rx="2.5"/><path class="side__toggle-l" d="M7.75 4.5v11"/></svg><span>Contraer menú</span></button></div>`;
  const setMin = (on) => {
    body.classList.toggle('side-min', on);
    const t = side.querySelector('.side__toggle');
    t.setAttribute('aria-pressed', String(on));
    t.setAttribute('aria-label', on ? 'Expandir el menú lateral' : 'Contraer el menú lateral');
    t.title = on ? 'Expandir el menú' : 'Contraer el menú';
    t.querySelector('span').textContent = on ? 'Expandir menú' : 'Contraer menú';
    try { localStorage.setItem('k-side', on ? 'min' : 'full'); } catch (_) {}
  };
  try { if (localStorage.getItem('k-side') === 'min') setMin(true); } catch (_) {}
  body.classList.remove('side-off');
  const setDrawer = (o, back) => {
    body.classList.toggle('nav-open', o);
    if (o) (side.querySelector('[aria-current="page"]') || side.querySelector('a, button')).focus({ preventScroll: true });
    else if (back) { const b = document.querySelector('.chapbar'); if (b) b.focus(); }
  };
  const scrim = document.createElement('div');
  scrim.className = 'scrim';
  scrim.addEventListener('click', () => setDrawer(false, true));
  body.appendChild(scrim);
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && body.classList.contains('nav-open')) setDrawer(false, true); });
  /* Abrir un área o un capítulo pliega los demás: solo queda a la vista lo que se está consultando */
  const setArea = (ab, o) => { ab.setAttribute('aria-expanded', String(o)); $(ab.getAttribute('aria-controls')).hidden = !o; };
  const setCh = (cb, o) => { cb.setAttribute('aria-expanded', String(o)); cb.parentElement.setAttribute('aria-expanded', String(o)); };
  side.addEventListener('click', (e) => {
    if (e.target.closest('.side__toggle')) return setMin(!body.classList.contains('side-min'));
    const ab = e.target.closest('.nav-area__btn');
    if (ab) {
      const o = ab.getAttribute('aria-expanded') !== 'true';
      if (o) side.querySelectorAll('.nav-area__btn[aria-expanded="true"]').forEach((x) => { if (x !== ab) setArea(x, false); });
      setArea(ab, o);
      return;
    }
    const cb = e.target.closest('.nav-ch__btn');
    if (cb) {
      if (body.classList.contains('side-min')) setMin(false);
      const o = cb.getAttribute('aria-expanded') !== 'true';
      if (o) side.querySelectorAll('.nav-ch__btn[aria-expanded="true"]').forEach((x) => { if (x !== cb) setCh(x, false); });
      setCh(cb, o);
      return;
    }
    /* Al elegir un destino en el panel, el panel se cierra y la ruta activa se conserva */
    if (e.target.closest('a') && body.classList.contains('nav-open')) setDrawer(false);
  });
  /* Enlace directo al índice abierto en móvil: …#indice */
  if (location.hash === '#indice' && !matchMedia('(min-width: 901px)').matches) setDrawer(true);
  if (area) {
    /* Barra de capítulo para móvil: abre el índice como panel */
    let cur = null;
    area.ch.forEach((c) => c.items.forEach((it) => { if (!cur && base(it.href) === PAGE) cur = [c, hash(it.href) ? { t: 'Secciones' } : it]; }));
    const bar = document.createElement('button');
    bar.type = 'button';
    bar.className = 'chapbar';
    bar.setAttribute('aria-controls', 'side');
    bar.innerHTML = ic('<path d="M2.5 4.5h11M2.5 8h11M2.5 11.5h7"/>') + (cur ? `${cur[0].n} ${esc(cur[0].t)}${cur[1].t === cur[0].t ? '' : ` <span>· ${esc(cur[1].t)}</span>`}` : `${esc(area.t)} <span>· capítulos</span>`);
    bar.addEventListener('click', () => setDrawer(true));
    document.querySelector('.doc').before(bar);
    /* Secciones de un capítulo: el lateral sigue la lectura */
    const secLinks = [...side.querySelectorAll('[data-sec]')].filter((l) => base(l.getAttribute('href').replace(ROOT + '/', '')) === PAGE);
    if (secLinks.length) {
      const so = new IntersectionObserver((ents) => ents.forEach((en) => {
        if (en.isIntersecting) secLinks.forEach((l) => (l.dataset.sec === en.target.id ? l.setAttribute('aria-current', 'page') : l.removeAttribute('aria-current')));
      }), { rootMargin: '-35% 0px -60% 0px' });
      secLinks.forEach((l) => { const t = document.getElementById(l.dataset.sec); if (t) so.observe(t); });
    }
  }

  }

  /* ─── Portada: índice del manual ─── */
  const ag = $('areas-grid');
  if (ag) {
    ag.innerHTML = NAV.filter((a) => !a.noCard).map((a) => `
      <article class="area">
        <div class="area__color grad grad--${a.color}" aria-hidden="true"></div>
        <div class="area__body">
          <h3 class="t-h3">${esc(BOOK.cardShort ? a.t : (a.full || a.t))}</h3>
          <p class="t-sm">${esc(a.cd || a.d)}</p>
          <ul class="area__list">${a.ch.map((c) => `<li><a href="${url(a.href)}#${slug(c)}"><span>${c.n}</span>${esc(c.t)}${dot(c.s)}</a></li>`).join('')}</ul>
          <div class="area__foot"><span class="paren">(${a.ch.length} ${a.ch.length === 1 ? 'capítulo' : 'capítulos'})</span>
            <a class="area__go" href="${url(a.href)}" aria-label="Abrir ${esc(a.t)}">${ic(I.right)}</a></div>
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
    const pages = area.ch.reduce((n, c) => n + c.items.filter(counted).length, 0);
    /* El mismo nombre corto del menú lateral (una línea); el completo queda en el title */
    const pgT = (it) => (BOOK.areaFull ? it.t : (it.st || it.t));
    const pg = (it) => it.href
      ? `<a class="pg" href="${url(it.href)}" title="${esc(it.t)}">${esc(pgT(it))}${ic(I.right)}${dot(it.s)}</a>`
      : `<span class="pg" title="${esc(it.t)}">${esc(pgT(it))}${dot(it.s)}</span>`;
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
    const badge = (st) => `<span class="badge badge--${SKEY[st]}">${ic({ v: I.check, b: '<circle cx="8" cy="8" r="5.6"/><path d="M8 2.4v11.2"/>', p: '<circle cx="8" cy="8" r="5.6"/>', e: '<path d="M2.5 4.5h11M2.5 8h11M2.5 11.5h7"/>', r: '<circle cx="8" cy="8" r="5.6"/><circle cx="8" cy="8" r="1.6"/>', d: '<circle cx="8" cy="8" r="5.6"/><path d="M4 12 12 4"/>' }[st])}${STATUS[st]}</span>`;
    ap.innerHTML = `
      <header class="page-head">
        <h1 class="t-h1">${esc(area.full || area.t)}</h1>
        <p class="t-lead">${esc(area.d)}</p>
        <div class="facts">
          <div><span class="paren">(${W.ch})</span><b>${area.ch[0].n}–${area.ch[area.ch.length - 1].n}</b></div>
          <div><span class="paren">(${W.pg})</span><b>${pages}</b></div>
          <div><span class="paren">(Color)</span><b>${esc(area.colorName)}</b></div>
        </div>
      </header>
      <div class="band grad grad--${area.color}" aria-hidden="true"></div>
      ${area.ch.map((c) => `
        <section class="chap" id="${slug(c)}">
          <div class="chap__head">
            <span class="chap__n">${c.n}</span>
            <div><h2 class="chap__t">${esc(c.full || c.t)}</h2><p class="t-body chap__d">${esc(c.d || '')}</p></div>
            <div class="chap__meta">${badge(c.s || 'p')}<span class="paren">(${c.items.filter(counted).length} ${W.pgs})</span></div>
          </div>
          <div class="chap__cols">${cols(c)}</div>
        </section>`).join('')}`;
    /* El contenido se genera después de cargar: se respeta el ancla de la URL */
    /* Enlaces anteriores a la renumeración (#cap-06): llevan al capítulo que tenía ese número */
    const old = /^#cap-(\d\d)$/.exec(location.hash);
    const was = old && area.ch.find((c) => [].concat(c.was || []).includes(old[1]));
    if (was) history.replaceState(null, '', '#' + slug(was));
    if (location.hash) { const t = document.getElementById(location.hash.slice(1)); if (t) requestAnimationFrame(() => t.scrollIntoView()); }
  }

  /* ─── Paginador automático ─── */
  const pg = $('pager');
  if (pg) {
    const k = seq.findIndex((x) => base(x.href) === PAGE);
    const prev = k > 0 ? seq[k - 1] : { t: 'Portada', href: HOME };
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
    const play = () => { clearInterval(t); if (!still && ms) t = setInterval(() => go(k + 1), ms); };   // ms 0: sin avance automático
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
  /* Puntos de carrusel (reglas-visuales 8, piloto): al cambiar, la marca salta del punto anterior al nuevo y toma su forma */
  const msVar = (v) => parseFloat(getComputedStyle(document.documentElement).getPropertyValue(v)) || 300;
  const saltar = (nav, de, a) => {
    if (still || !de || de === a || !nav.animate) return;
    let g = nav.querySelector('.pt__go');
    if (!g) { g = document.createElement('span'); g.className = 'pt__go'; g.setAttribute('aria-hidden', 'true'); nav.appendChild(g); }
    const n = nav.getBoundingClientRect(), x = (b) => { const r = b.querySelector('i').getBoundingClientRect(); return r.left - n.left; };
    const forma = (b) => getComputedStyle(b.querySelector('i')).borderRadius;
    g.animate([
      { transform: `translateX(${x(de)}px)`, borderRadius: forma(de), opacity: 1 },
      { transform: `translateX(${x(a)}px) translateY(-6px) scale(.8)`, offset: .5, opacity: 1 },
      { transform: `translateX(${x(a)}px)`, borderRadius: forma(a), opacity: 1 },
      { transform: `translateX(${x(a)}px)`, borderRadius: forma(a), opacity: 0 }
    ], { duration: msVar('--m-base') * 1.4, easing: getComputedStyle(document.documentElement).getPropertyValue('--e-io').trim() || 'ease-in-out' });
  };
  document.querySelectorAll('[data-icar]').forEach((el) => {
    const ss = el.querySelectorAll('.icar__s'), its = el.querySelectorAll('.icar__it'), bs = el.querySelectorAll('[data-ci]');
    const ms = el.dataset.ms !== undefined ? Number(el.dataset.ms) : 3600, nav = el.querySelector('.icar__nav--pt');
    el.style.setProperty('--car-ms', ms + 'ms');
    let prev = null;
    const c = carousel(el, '.icar__s', ms, (k) => {
      ss.forEach((s, j) => s.classList.toggle('is-on', j === k));
      its.forEach((s, j) => { s.hidden = j !== k; });
      bs.forEach((b, j) => { b.classList.remove('is-on'); void b.offsetWidth; b.classList.toggle('is-on', j === k); });
      if (nav) { saltar(nav, prev, bs[k]); prev = bs[k]; }
      el.querySelector('.icar__stage').style.background = getComputedStyle(ss[k]).getPropertyValue('--bg');
    });
    bs.forEach((b) => b.addEventListener('click', () => c.go(Number(b.dataset.ci))));
  });
  /* ESP-004 · cada retícula muestra primero su estructura y, al entrar en pantalla, la misma composición con texto real */
  document.querySelectorAll('.lvx__fig').forEach((f) => {
    if (!f.querySelector('.lvx__tx')) return;
    if (still || !('IntersectionObserver' in window)) { f.classList.add('is-tx'); return; }
    const io = new IntersectionObserver(([e]) => { if (e.isIntersecting) { io.disconnect(); setTimeout(() => f.classList.add('is-tx'), msVar('--m-slow') * 2); } }, { threshold: .6 });
    io.observe(f);
  });
  /* ILU-007 · tarjetas en fila: el texto del estilo activo a la izquierda; avanza con los puntos, las flechas o un clic en otra tarjeta */
  document.querySelectorAll('[data-tcar]').forEach((el) => {
    const cs = el.querySelectorAll('.tcar__c'), its = el.querySelectorAll('.tcar__it'), bs = el.querySelectorAll('[data-ci]');
    const tr = el.querySelector('.tcar__track'), nav = el.querySelector('.icar__nav--pt');
    el.style.setProperty('--car-ms', '0ms');
    let prev = null;
    const c = carousel(el, '.tcar__c', 0, (k) => {
      cs.forEach((x, j) => x.classList.toggle('is-on', j === k));
      its.forEach((x, j) => { x.hidden = j !== k; });
      bs.forEach((b, j) => b.classList.toggle('is-on', j === k));
      if (nav) { saltar(nav, prev, bs[k]); prev = bs[k]; }
      tr.style.transform = `translateX(${-cs[k].offsetLeft}px)`;
    });
    bs.forEach((b) => b.addEventListener('click', () => c.go(Number(b.dataset.ci))));
    cs.forEach((x, j) => x.addEventListener('click', () => c.go(j)));
    addEventListener('resize', () => { tr.style.transform = `translateX(${-cs[c.at()].offsetLeft}px)`; });
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

  /* ─── Ráfagas (ILU-006): el viento del encabezado sobre la forma y los colores de cada ráfaga ───
     js/keyons-rafaga.js reproduce el campo de ráfaga del cielo: el cursor dispersa la materia
     y el viento la recompone. Sin WebGL queda el SVG original. */
  const rfps = document.querySelectorAll('[data-rfp]');
  if (rfps.length) {
    const go = () => rfps.forEach((p) => window.KeyonsRafaga.mount(p));
    if (window.KeyonsRafaga) go();
    else { const sc = document.createElement('script'); sc.src = (document.body.dataset.root || '.') + '/js/keyons-rafaga.js'; sc.onload = go; document.head.appendChild(sc); }
    /* Clic o Enter: copia el SVG de la ráfaga, limpio (sin el polvo animado), para usarlo en Figma, Illustrator o código */
    const svgOf = (p) => {
      const sv = p.querySelector('svg'); if (!sv) return '';
      const c = sv.cloneNode(true);
      c.querySelectorAll('.rfp__dust,animate,animateMotion,animateTransform').forEach((n) => n.remove());
      ['aria-hidden', 'style', 'class'].forEach((a) => c.removeAttribute(a));
      c.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
      const vb = (c.getAttribute('viewBox') || '0 0 300 400').split(/\s+/);
      c.setAttribute('width', vb[2]); c.setAttribute('height', vb[3]);
      return new XMLSerializer().serializeToString(c).replace(/ xmlns:xlink="[^"]*"/, '');
    };
    rfps.forEach((p) => {
      const n = (p.querySelector('.rfp__t') || {}).firstChild;
      p.classList.add('is-copy'); p.tabIndex = 0; p.setAttribute('role', 'button');
      p.setAttribute('aria-label', 'Copiar el SVG de la ráfaga' + (n ? ' ' + n.textContent.trim() : ''));
      const run = () => copy(svgOf(p), 'SVG copiado');
      p.addEventListener('click', run);
      p.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); run(); } });
    });
  }

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
  const aparecer = (targets) => {
    if (!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const ro = new IntersectionObserver((ents) => ents.forEach((en) => {
      if (en.isIntersecting) { en.target.classList.add('is-in'); ro.unobserve(en.target); }
    }), { rootMargin: '0px 0px -8% 0px', threshold: .08 });
    targets.forEach((t) => { if (t.getBoundingClientRect().top > innerHeight) { t.classList.add('reveal'); ro.observe(t); } });
  };
  aparecer([...document.querySelectorAll('.ed, .chap, .dsec, .area, .acar, .sec-head, .cols, .band, .rings, .matrix, .pgrid, .promises, .cstack, .tbl-wrap, .zig__item, .step, .chan, .pairs, .entry')].filter((t) => !t.parentElement.closest('.acar')));

  /* ─── Buscador de la Biblioteca ───
     Busca en todos los libros con acceso abierto: js/busqueda-indice.js, generado por tools/biblioteca.py
     desde data/libros.json, los mapas de cada libro y los registros de normas. Mientras el índice carga,
     o si no carga, busca en el libro actual. Cada resultado dice de qué libro viene. */
  const sb = document.createElement('div');
  sb.className = 'search';
  sb.setAttribute('role', 'dialog');
  sb.setAttribute('aria-modal', 'true');
  sb.setAttribute('aria-label', 'Buscar en la Biblioteca');
  sb.innerHTML = `<div class="search__box">
      <div class="search__field"><input type="search" placeholder="Buscar: factura, esquinas, Azul Cielo…" aria-label="Buscar en la Biblioteca" role="combobox" aria-autocomplete="list" aria-expanded="true" aria-controls="search-res" autocomplete="off"></div>
      <div class="search__res" id="search-res" role="listbox" aria-label="Resultados"></div>
      <p class="sr-only" role="status" aria-live="polite"></p>
      <div class="search__foot"><span><kbd>Flechas</kbd>Moverse</span><span><kbd>Enter</kbd>Abrir</span><span><kbd>Esc</kbd>Cerrar</span></div>
    </div>`;
  body.appendChild(sb);
  const input = sb.querySelector('input');
  const res = sb.querySelector('.search__res');
  const live = sb.querySelector('[role="status"]');
  const LIB = Object.fromEntries(LIBROS.map((b) => [b.id, b.t]));
  let sel = 0, hits = [], todo = null, falla = false, pedido = false, antes = null;
  const local = () => flat.map((f) => ({ t: f.t, h: f.href, b: f.norma ? 'marca' : (f.lib || BOOK_ID), p: f.path, s: f.s, k: f.k || '', n: !!f.norma }));
  const cargar = () => {
    if (pedido) return; pedido = true;
    const sx = document.createElement('script');
    sx.src = url('js/busqueda-indice.js');
    sx.onload = () => { const B = window.KEYONS_BUSQUEDA; if (B && B.items) { todo = B.items; Object.assign(LIB, B.libros || {}); } else falla = true; if (sb.classList.contains('is-open')) draw(); };
    sx.onerror = () => { falla = true; if (sb.classList.contains('is-open')) draw(); };
    document.head.appendChild(sx);
  };
  const norm = (s) => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  const draw = () => {
    const q = norm(input.value.trim());
    const pool = todo || local();
    const propio = (h) => (h.b === BOOK_ID ? 1 : 0);
    hits = (q
      ? pool.filter((f) => norm(f.t + ' ' + f.p + ' ' + (f.k || '') + ' ' + (LIB[f.b] || '')).includes(q))
        .sort((a, b) => ((norm(b.k || '').includes(q) && b.n) - (norm(a.k || '').includes(q) && a.n)) || (propio(b) - propio(a)))
      : pool.filter((f) => f.h && !f.n && f.b === BOOK_ID))
      .filter((f, i, all) => !f.h || all.findIndex((g) => g.h === f.h) === i).slice(0, 12);
    sel = Math.min(sel, Math.max(hits.length - 1, 0));
    res.innerHTML = hits.length ? hits.map((h, i) => {
      const lib = LIB[h.b] ? `<span class="r-lib">${esc(LIB[h.b])}</span> · ` : '';
      const inner = `<span class="r-body"><span class="r-t">${esc(h.t)}</span><br><span class="r-path">${lib}${esc(h.p || '')}</span></span>${dot(h.s)}`;
      const c = i === sel ? ' is-sel' : '';
      return h.h ? `<a class="${c.trim()}" id="sr-${i}" href="${url(h.h)}" role="option" aria-selected="${i === sel}" tabindex="-1">${inner}</a>`
        : `<div class="r${c}" id="sr-${i}" role="option" aria-selected="${i === sel}" aria-disabled="true">${inner}</div>`;
    }).join('') : `<div class="search__empty">Sin resultados para «${esc(input.value.trim())}». Pruebe con otra palabra o con el ID de una norma.</div>`;
    const aviso = falla ? '<div class="search__empty">La búsqueda en toda la Biblioteca está fuera de servicio por ahora. Estos resultados son de este libro.</div>' : '';
    if (aviso) res.insertAdjacentHTML('afterbegin', aviso);
    if (hits.length) input.setAttribute('aria-activedescendant', 'sr-' + sel); else input.removeAttribute('aria-activedescendant');
    live.textContent = q ? (hits.length ? `${hits.length} resultado${hits.length === 1 ? '' : 's'}` : 'Sin resultados') : '';
  };
  const open = () => {
    if (window.KEYONS_CERRAR_LIBROS) window.KEYONS_CERRAR_LIBROS();
    const a = document.activeElement;
    antes = a && a !== body && !a.closest('.bks') ? a : document.querySelector('.hdr__search');
    cargar();
    sb.classList.add('is-open'); input.value = ''; sel = 0; draw(); setTimeout(() => input.focus(), 10);
  };
  const close = () => {
    sb.classList.remove('is-open');
    if (antes && document.contains(antes)) antes.focus({ preventScroll: true });
  };
  input.addEventListener('input', () => { sel = 0; draw(); });
  const mark = () => {
    res.querySelectorAll('[role="option"]').forEach((el, k) => { el.classList.toggle('is-sel', k === sel); el.setAttribute('aria-selected', String(k === sel)); });
    if (hits.length) { input.setAttribute('aria-activedescendant', 'sr-' + sel); const el = document.getElementById('sr-' + sel); if (el) el.scrollIntoView({ block: 'nearest' }); }
  };
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
    if (e.key === 'Escape') { e.preventDefault(); close(); }
    /* El foco queda dentro del buscador: las flechas recorren los resultados y Tab vuelve al campo */
    if (e.key === 'Tab') { e.preventDefault(); input.focus(); }
    if (e.key === 'ArrowDown') { e.preventDefault(); sel = Math.min(sel + 1, hits.length - 1); mark(); }
    if (e.key === 'ArrowUp') { e.preventDefault(); sel = Math.max(sel - 1, 0); mark(); }
    if (e.key === 'Enter' && hits[sel] && hits[sel].h) { e.preventDefault(); location.href = url(hits[sel].h); }
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
  /* Acordeones: el primer ítem se abre cuando el acordeón entra en pantalla, para que se entienda la interacción */
  document.querySelectorAll('.promises').forEach((acc) => {
    const first = acc.querySelector('details');
    if (!first) return;
    acc.querySelectorAll('details[open]').forEach((d) => d.removeAttribute('open'));
    if (!('IntersectionObserver' in window)) { first.open = true; return; }
    const io = new IntersectionObserver((es) => {
      if (es.some((e) => e.isIntersecting)) { setTimeout(() => { first.open = true; }, 450); io.disconnect(); }
    }, { rootMargin: '0px 0px -35% 0px' });
    io.observe(acc);
  });


  /* Carrusel horizontal: varias piezas a la vista, con el pie de los demás carruseles */
  document.querySelectorAll('[data-hcar]').forEach((c) => {
    const vivos = () => [...c.children].filter((x) => !x.hidden);
    let items = vivos();
    const wrap = document.createElement('div');
    wrap.className = 'hcar__wrap';
    c.before(wrap); wrap.append(c);
    wrap.insertAdjacentHTML('beforeend', `<div class="mslide__foot hcar__foot"><span class="mslide__count">(01 / ${String(items.length).padStart(2, '0')})</span><span class="mslide__bar" aria-hidden="true"><i></i></span><div class="mslide__nav"><button class="btn-text" type="button" data-hs="-1" aria-label="Anterior"><svg class="go-l" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 8H3M6.8 4.2 3 8l3.8 3.8"/></svg>Anterior</button><button class="btn-text" type="button" data-hs="1" aria-label="Siguiente">Siguiente<svg class="go-r" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9.2 4.2 13 8l-3.8 3.8"/></svg></button></div></div>`);
    const count = wrap.querySelector('.mslide__count'), bar = wrap.querySelector('.mslide__bar i');
    const step = () => { items = vivos(); return items[1] ? items[1].offsetLeft - items[0].offsetLeft : c.clientWidth; };
    const upd = () => {
      const i = Math.round(c.scrollLeft / step()), max = c.scrollWidth - c.clientWidth;
      items.forEach((x, j) => x.classList.toggle('is-cur', j === i));
      count.textContent = `(${String(Math.min(items.length, i + 1)).padStart(2, '0')} / ${String(items.length).padStart(2, '0')})`;
      bar.style.transform = `scaleX(${max > 0 ? Math.max(0.08, c.scrollLeft / max) : 1})`;
      wrap.querySelector('[data-hs="-1"]').disabled = c.scrollLeft < 4;
      wrap.querySelector('[data-hs="1"]').disabled = c.scrollLeft > max - 4;
    };
    wrap.querySelectorAll('[data-hs]').forEach((b) => b.addEventListener('click', () => c.scrollBy({ left: step() * Number(b.dataset.hs), behavior: 'smooth' })));
    c.addEventListener('scroll', upd, { passive: true });
    addEventListener('resize', upd);
    upd();
  });

  /* REF-001: cada parte del ID se resalta por turno y una línea la une con su significado */
  document.querySelectorAll('[data-kexa]').forEach((st) => {
    const segs = [...st.querySelectorAll('.kex [data-k]')], ans = [...st.querySelectorAll('[data-a]')], svg = st.querySelector('.kexa__l');
    svg.innerHTML = segs.map(() => '<path/>').join('');
    const ps = [...svg.children];
    const quieto = matchMedia('(prefers-reduced-motion: reduce)').matches;
    const dibujar = () => {
      const B = st.getBoundingClientRect();
      svg.setAttribute('viewBox', `0 0 ${B.width} ${B.height}`);
      const caja = (e) => { const r = e.getBoundingClientRect(), l = r.left - B.left, t = r.top - B.top; return { l, t, r: l + r.width, b: t + r.height, cx: l + r.width / 2, my: t + r.height / 2 }; };
      ps.forEach((p, i) => {
        const a = caja(ans[i]), g = caja(segs[i]);
        p.setAttribute('d', [
          `M${a.cx} ${a.b + 6}V${g.my}H${g.l - 8}`,
          `M${g.cx} ${g.b + 6}V${a.my}H${a.r + 10}`,
          `M${g.cx} ${g.t - 6}V${a.my}H${a.l - 10}`,
          `M${g.r + 8} ${g.my}H${a.cx}V${a.t - 6}`][i]);
      });
    };
    let k = 0, t = 0, visto = false;
    const pintar = (n) => { k = n; [segs, ans, ps].forEach((l) => l.forEach((x, i) => x.classList.toggle('is-on', i === n))); };
    const seguir = () => { clearInterval(t); if (quieto || !visto) return; t = setInterval(() => pintar((k + 1) % segs.length), 2800); };
    if (quieto) [segs, ans, ps].forEach((l) => l.forEach((x) => x.classList.add('is-on'))); else pintar(0);
    dibujar(); addEventListener('resize', dibujar); if (document.fonts && document.fonts.ready) document.fonts.ready.then(dibujar);
    if ('ResizeObserver' in window) new ResizeObserver(dibujar).observe(st);
    [...segs, ...ans].forEach((x) => x.addEventListener('pointerenter', () => { clearInterval(t); if (!quieto) pintar(+(x.dataset.k ?? x.dataset.a)); }));
    st.addEventListener('pointerleave', seguir);
    new IntersectionObserver((e) => { visto = e[0].isIntersecting; seguir(); }, { threshold: .3 }).observe(st);
  });

  /* Acordeón: una fila abierta a la vez */
  document.querySelectorAll('[data-acord]').forEach((ac) => {
    const fs = ac.querySelectorAll('.acord__f');
    fs.forEach((f) => f.querySelector('.acord__b').addEventListener('click', () => {
      fs.forEach((x) => { const on = x === f; x.classList.toggle('is-open', on); x.querySelector('.acord__b').setAttribute('aria-expanded', String(on)); });
    }));
  });

  /* Comparativos: la explicación vive detrás de la tarjeta y se consulta con «Leer más» */
  const girar = (f) => {
    const cap = f.querySelector('figcaption'), face = f.querySelector('.vdemo__s, .gl, .lvx__fig, .xmp__stage');
    if (!cap || !face || f.querySelector('.flip__btn')) return;
    const lab = cap.querySelector('.paren, b, .lvx__t');
    f.classList.add('flip');
    const card = document.createElement('div');
    card.className = 'flip__card';
    face.before(card); card.append(face);
    const back = document.createElement('div');
    back.className = 'flip__back';
    back.append(...cap.childNodes);
    card.append(back);
    cap.remove();
    if (lab) { const t = document.createElement('span'); t.className = 'flip__tag'; t.textContent = lab.textContent.replace(/[()]/g, ''); card.append(t); }
    card.insertAdjacentHTML('beforeend', '<button class="flip__btn" type="button" aria-expanded="false"><span>Leer más</span><svg viewBox="0 0 32 32" aria-hidden="true"><path transform="matrix(1,0,0,-1,9.2835,16)" stroke-width="2.5" stroke-linecap="butt" fill="none" stroke="currentColor" d="M0 0L13.433 0"/><path transform="matrix(1,0,0,-1,16,9.283501)" stroke-width="2.5" stroke-linecap="butt" fill="none" stroke="currentColor" d="M0 0L0 -13.433"/></svg></button>');
    const btn = card.querySelector('.flip__btn');
    btn.addEventListener('click', () => {
      const on = !f.classList.contains('is-flip');
      f.classList.toggle('is-flip', on); btn.setAttribute('aria-expanded', String(on));
      btn.querySelector('span').textContent = on ? 'Volver' : 'Leer más';
    });
    /* Cuando la tarjeta sale de la pantalla, el lector ya terminó con ella: vuelve sola a su cara principal */
    if ('IntersectionObserver' in window) new IntersectionObserver((es) => es.forEach((e) => {
      if (!e.isIntersecting && f.classList.contains('is-flip')) { f.classList.remove('is-flip'); btn.setAttribute('aria-expanded', 'false'); btn.querySelector('span').textContent = 'Leer más'; }
    })).observe(f);
  };
  document.querySelectorAll('.vdemo__i, .glass2 > figure, .lvx__i, .xmp__fig').forEach((f) => girar(f));
  /* Recursos técnicos (29) copia estas funciones tal cual: el código del catálogo es el del libro */
  window.KeyonsEfectos = { trama, nubes, aparecer, girar };

  /* Titulares largos en dos renglones: el corte va después de la coma o el punto y coma */
  document.querySelectorAll('.ed__title').forEach((t) => {
    if (t.children.length || t.textContent.length < 34) return;
    const m = t.textContent.match(/^(.{8,}?[,;])\s+(.{8,})$/);
    if (!m) return;
    const antes = t.textContent;
    t.innerHTML = `${esc(m[1])}<br>${esc(m[2])}`;
    /* reglas-visuales 2.6 (R11): dos renglones. Si el corte deja tres, el titular vuelve a cortarse solo.
       Se mide con la tipografía ya cargada, que es más ancha que la de reserva */
    const medir = () => { if (t.getBoundingClientRect().height > 2.5 * parseFloat(getComputedStyle(t).lineHeight)) t.textContent = antes; };
    (document.fonts ? document.fonts.ready : Promise.resolve()).then(medir);
  });
  /* Sin palabras sueltas: la primera palabra de cada oración no queda sola al final de un renglón,
     y el último renglón de un párrafo nunca es una sola palabra */
  document.querySelectorAll('main p, main li, main dd').forEach((p) => {
    if (p.closest('input, textarea, [contenteditable], .tester__out, .tcx, .trk') || parseFloat(getComputedStyle(p).fontSize) > 24 || p.clientWidth < 260) return;
    const w = document.createTreeWalker(p, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (w.nextNode()) nodes.push(w.currentNode);
    nodes.forEach((n, i) => {
      let v = n.nodeValue.replace(/(^|[.!?:;»]\s+)([¿¡«]?[A-ZÁÉÍÓÚÑ][\wáéíóúñ]{0,5}) (?=\S)/g, '$1$2 ');
      if (i === nodes.length - 1) v = v.replace(/ (\S+\s*)$/, ' $1');
      if (v !== n.nodeValue) n.nodeValue = v;
    });
  });

  /* Una sola línea entre dos bloques · reglas-visuales 3.5
     Si un bloque cierra con su línea y el siguiente abre con la suya, sin nada entre ellas, el anterior cierra
     sin línea. Vale para cualquier par de componentes, también los que se agreguen después.
     Se mide con la posición de maquetación (offsetTop), que no cambia con la animación de entrada. */
  {
    const raiz = document.querySelector('main');
    const caja = (e) => {
      while (e && !(e instanceof HTMLElement)) e = e.parentElement;
      if (!e || !e.offsetParent) return null;
      let x = 0, y = 0;
      for (let p = e; p; p = p.offsetParent) { x += p.offsetLeft; y += p.offsetTop; }
      return { t: y, b: y + e.offsetHeight, l: x, r: x + e.offsetWidth };
    };
    const quitadas = [];
    const unaLinea = () => {
      quitadas.splice(0).forEach((e) => { e.style.borderBottomColor = ''; });
      if (!raiz) return;
      const lineas = [], cont = [];
      raiz.querySelectorAll('*').forEach((e) => {
        if (e.closest('.side, .toc, .portal, .hero, nav, [hidden]')) return;
        const cs = getComputedStyle(e), k = caja(e);
        if (!k || cs.visibility === 'hidden') return;
        const lado = (s) => parseFloat(cs[`border${s}Width`]) > 0 && cs[`border${s}Style`] !== 'none' && cs[`border${s}Color`] !== 'rgba(0, 0, 0, 0)';
        /* Una caja, con borde a ambos lados, no es una línea divisoria */
        if (k.r - k.l >= 120 && !(lado('Left') && lado('Right'))) {
          if (lado('Top')) lineas.push({ y: k.t, l: k.l, r: k.r, e, abre: true });
          if (lado('Bottom')) lineas.push({ y: k.b, l: k.l, r: k.r, e, abre: false });
        }
        if (/^(IMG|CANVAS|VIDEO|PICTURE)$/.test(e.tagName) || [...e.childNodes].some((n) => n.nodeType === 3 && /\S/.test(n.data))) cont.push(k);
      });
      /* Un SVG no tiene offsetTop: se mide en pantalla; los que no se ven (símbolos, filtros) no cuentan */
      raiz.querySelectorAll('svg').forEach((s) => {
        const r = s.getBoundingClientRect();
        if (r.width > 1 && r.height > 1) cont.push({ t: r.top + scrollY, b: r.bottom + scrollY, l: r.left + scrollX, r: r.right + scrollX });
      });
      lineas.sort((a, b) => a.y - b.y);
      lineas.forEach((a, i) => {
        if (a.abre) return;
        const b = lineas.slice(i + 1).find((x) => x.abre && x.y - a.y > 1 && Math.min(a.r, x.r) - Math.max(a.l, x.l) > 0.6 * Math.min(a.r - a.l, x.r - x.l));
        if (!b || b.y - a.y > 140) return;
        const l = Math.max(a.l, b.l), r = Math.min(a.r, b.r);
        if (cont.some((c) => c.b > a.y + 1 && c.t < b.y - 1 && c.r > l && c.l < r)) return;
        a.e.style.borderBottomColor = 'transparent';
        quitadas.push(a.e);
      });
    };
    let espera;
    const programar = () => { clearTimeout(espera); espera = setTimeout(unaLinea, 120); };
    (document.fonts ? document.fonts.ready : Promise.resolve()).then(programar);
    addEventListener('load', programar);
    addEventListener('resize', programar);
  }

  /* Pasos con salto (portada del Sistema de Diseño): un punto recorre cada arco y, al aterrizar,
     aparece el texto de ese paso. Ritmo de viento: --m-slow por salto con --e-io; una sola vez (reglas-visuales 7) */
  document.querySelectorAll('.lbw__steps').forEach((ol) => {
    const lis = [...ol.children];
    if (!lis.length || matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window) || !CSS.supports('offset-path', 'path("M0 0")')) return;
    const css = getComputedStyle(document.documentElement);
    const dur = parseFloat(css.getPropertyValue('--m-slow')) || 520;
    const ease = css.getPropertyValue('--e-io').trim() || 'ease-in-out';
    ol.classList.add('is-anim');
    const dot = document.createElement('span');
    dot.className = 'lbw__dot'; dot.setAttribute('aria-hidden', 'true');
    ol.appendChild(dot);
    const arco = (li) => {
      const h = parseFloat(getComputedStyle(li, '::after').height) || 96;
      const x0 = li.offsetLeft, x1 = x0 + li.offsetWidth, y = li.offsetTop + li.offsetHeight;
      return `path("M ${x0} ${y} A ${li.offsetWidth / 2} ${h} 0 0 1 ${x1} ${y}")`;
    };
    const saltar = async () => {
      dot.classList.add('is-on');
      for (const li of lis) {
        dot.style.offsetPath = arco(li);
        await dot.animate([{ offsetDistance: '0%' }, { offsetDistance: '100%' }], { duration: dur, easing: ease, fill: 'forwards' }).finished;
        li.classList.add('is-shown', 'is-done');
      }
      dot.classList.remove('is-on');
    };
    new IntersectionObserver((es, io) => es.forEach((e) => { if (e.isIntersecting) { io.disconnect(); saltar(); } }), { threshold: .5 }).observe(ol);
  });

  /* Leyenda de estados en la portada: Vigente, Borrador y Por definir, en una franja sobre el carrusel (reglas-visuales R16) */
  document.querySelectorAll('[data-estados]').forEach((el) => {
    el.innerHTML = LEGEND.map((k) => `<span>${dot(k)} ${STATUS[k]}</span>`).join('');
  });

  /* Niveles de norma: la marca muestra su significado en una etiqueta al pasar el cursor o con el foco (reglas-visuales R16) */
  {
    document.querySelectorAll('.nvl[data-lvl]').forEach((el) => {
      if (!el.hasAttribute('tabindex')) el.tabIndex = 0;
      if (!el.hasAttribute('aria-label') && LEVEL_TIP[el.dataset.lvl]) el.setAttribute('aria-label', `${el.textContent.trim() || LEVEL[el.dataset.lvl]}: ${LEVEL_TIP[el.dataset.lvl]}`);
    });
    let tip = null;
    const poner = (el) => {
      const k = el.dataset.lvl;
      if (!LEVEL_TIP[k]) return;
      if (!tip) { tip = document.createElement('div'); tip.className = 'ctip ctip--nvl'; tip.setAttribute('aria-hidden', 'true'); document.body.appendChild(tip); }
      tip.replaceChildren(Object.assign(document.createElement('b'), { textContent: el.textContent.trim() || LEVEL[k] }),
        Object.assign(document.createElement('span'), { textContent: LEVEL_TIP[k] }));
      const r = el.getBoundingClientRect();
      tip.style.left = `${Math.min(Math.max(r.left + r.width / 2, 130), innerWidth - 130)}px`;
      tip.style.top = `${r.top}px`;
      tip.classList.add('is-on');
    };
    const quitar = () => tip && tip.classList.remove('is-on');
    document.addEventListener('mouseover', (e) => { const el = e.target.closest('.nvl'); if (el) poner(el); });
    document.addEventListener('mouseout', (e) => { if (e.target.closest('.nvl') && !e.relatedTarget?.closest?.('.nvl')) quitar(); });
    document.addEventListener('focusin', (e) => { const el = e.target.closest('.nvl'); if (el) poner(el); });
    document.addEventListener('focusout', quitar);
    addEventListener('scroll', quitar, { passive: true });
  }

})();
