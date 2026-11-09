/* Keyons · Laboratorio de Interfaces · runtime del escenario
   Corre dentro del iframe aislado (sandbox sin mismo origen). Habla con la página
   del Laboratorio solo por postMessage:
     recibe  {type:'vars', vars, attrs}  → aplica la exploración sobre la base
             {type:'tecnica', on}         → dibuja o quita la vista técnica
     envía   {type:'checks', items, device}
   No modifica nada fuera de este escenario. */
(function () {
  'use strict';
  var root = document.documentElement, body = document.body;
  var tecnica = false, attrsNow = {}, cieloMounted = null;
  var post = function (m) { try { parent.postMessage(m, '*'); } catch (e) {} };

  function applyVars(vars, attrs) {
    Object.keys(vars || {}).forEach(function (k) {
      if (vars[k] === null || vars[k] === '') root.style.removeProperty(k); else root.style.setProperty(k, vars[k]);
    });
    attrsNow = attrs || {};
    ['nav', 'cols', 'anim', 'glass'].forEach(function (k) {
      if (attrsNow[k]) body.setAttribute('data-' + k, attrsNow[k]); else body.removeAttribute('data-' + k);
    });
    sky(attrsNow.cielo);
    if (attrsNow.anim && /entrada/.test(attrsNow.anim)) {   // repetir la entrada para verla
      body.removeAttribute('data-anim'); void body.offsetWidth; body.setAttribute('data-anim', attrsNow.anim);
    }
  }

  /* Cielo animado de fondo: el mismo módulo del encabezado (solo configuración) */
  function sky(name) {
    var host = document.getElementById('lx-sky');
    if (!name) { if (host) host.remove(); cieloMounted = null; body.classList.remove('lx-cielo'); return; }
    if (cieloMounted === name) return;
    if (host) host.remove();
    host = document.createElement('div'); host.id = 'lx-sky';
    host.style.cssText = 'position:fixed;inset:0;z-index:-1;pointer-events:none';
    body.prepend(host); body.classList.add('lx-cielo'); cieloMounted = name;
    if (window.KeyonsCielo) window.KeyonsCielo.mount(host, { sky: name, seed: 'laboratorio', hover: 'none' });
  }

  /* ── Vista técnica y guía de retícula: capas sobre el mismo componente ──
     capas: medidas, radios, tokens, jerarquía. La guía de retícula sigue ESP-004 (y 7 + 5 de CMP-003)
     y también puede verse mientras se diseña. */
  var capas = { medidas: false, radios: false, tokens: false, jerarquia: false }, guia = '';
  var SEL = '.lx-card,.lx-btn,.lx-input,.lx-select,.lx-textarea,.lx-badge,.lx-kpi,.lx-table,.lx-nav,.lx-alert,.lx-tabs,.lx-grid,.lx-empty';
  var TXT = 'h1,h2,h3,h4,.lx-h1,.lx-h2,.lx-h3,.lx-lead,.lx-num,.lx-kicker,p,.lx-meta,.lx-small,b,label';
  var px = function (v) { return Math.round(parseFloat(v) || 0); };
  var TOK = null;
  function tokenMap() {
    if (TOK) return TOK; TOK = {};
    [].forEach.call(document.styleSheets, function (sh) {
      var rules; try { rules = sh.cssRules; } catch (e) { return; }
      [].forEach.call(rules || [], function (r) {
        if (r.selectorText !== ':root' || !r.style) return;
        for (var i = 0; i < r.style.length; i++) {
          var n = r.style[i]; if (n.indexOf('--k-') !== 0) continue;
          var v = r.style.getPropertyValue(n).trim(); if (!/^#[0-9a-f]{6}$/i.test(v)) continue;
          var k = parseInt(v.slice(1), 16), rgb = 'rgb(' + (k >> 16) + ', ' + ((k >> 8) & 255) + ', ' + (k & 255) + ')';
          if (!TOK[rgb]) TOK[rgb] = n;
        }
      });
    });
    return TOK;
  }
  function gridSpec(W) {
    var base = W < 760 ? { cols: 4, m: 16, g: 16 } : W < 1100 ? { cols: 8, m: 32, g: 24 } : { cols: 12, m: 64, g: 24, max: 1520 };
    if (guia === '12' || guia === '7-5') base.cols = 12;
    if (guia === '8') base.cols = 8;
    if (guia === '4') base.cols = 4;
    return base;
  }
  function drawGuide() {
    var old = document.getElementById('lx-guide'); if (old) old.remove();
    if (!guia) return;
    var W = root.clientWidth, H = Math.max(root.scrollHeight, window.innerHeight), s = gridSpec(W);
    var inner = Math.min(W - 2 * s.m, s.max || 1e9), left = (W - inner) / 2, cw = (inner - (s.cols - 1) * s.g) / s.cols;
    var g = document.createElement('div'); g.id = 'lx-guide'; g.className = 'lx-guide';
    g.style.cssText = 'height:' + H + 'px';
    for (var i = 0; i < s.cols; i++) {
      var c = document.createElement('i');
      c.style.cssText = 'left:' + (left + i * (cw + s.g)) + 'px;width:' + cw + 'px';
      g.appendChild(c);
    }
    var b = document.createElement('b'); b.textContent = (guia === '7-5' ? '7 + 5 de 12' : s.cols + ' columnas') + ' · margen ' + s.m + ' · medianil ' + s.g; g.appendChild(b);
    body.appendChild(g);
  }
  function overlay() {
    document.querySelectorAll('.lx-ov').forEach(function (n) { n.remove(); });
    drawGuide();
    if (!tecnica || !(capas.medidas || capas.radios || capas.tokens || capas.jerarquia)) return;
    var sx = window.scrollX, sy = window.scrollY, n = 0, tm = capas.tokens ? tokenMap() : null;
    var put = function (el, t) {
      if (!t || n > 80) return;
      var r = el.getBoundingClientRect(); if (!r.width || !r.height) return;
      var o = document.createElement('div'); n++;
      o.className = 'lx-ov';
      o.style.cssText = 'left:' + (r.left + sx) + 'px;top:' + (r.top + sy) + 'px;width:' + r.width + 'px;height:' + r.height + 'px';
      var b = document.createElement('b'); b.textContent = t; o.appendChild(b); body.appendChild(o);
    };
    document.querySelectorAll(SEL).forEach(function (el) {
      var cs = getComputedStyle(el), r = el.getBoundingClientRect(), t = [];
      if (capas.medidas) {
        t.push(Math.round(r.width) + '×' + Math.round(r.height));
        var pad = [cs.paddingTop, cs.paddingRight, cs.paddingBottom, cs.paddingLeft].map(px);
        if (pad.some(Boolean)) t.push('p ' + pad.join(' '));
        if ((cs.display.indexOf('grid') > -1 || cs.display.indexOf('flex') > -1) && (px(cs.columnGap) || px(cs.rowGap))) t.push('gap ' + px(cs.rowGap) + '/' + px(cs.columnGap));
        if (el.classList.contains('lx-grid')) t.push(cs.gridTemplateColumns.split(' ').length + ' col');
      }
      if (capas.radios) {
        var rr = function (v) { v = px(v); return v > 999 ? 'píldora' : v; };
        var rad = [cs.borderTopLeftRadius, cs.borderTopRightRadius, cs.borderBottomRightRadius, cs.borderBottomLeftRadius].map(rr).join('/');
        if (/^(píldora\/){3}píldora$/.test(rad)) rad = 'píldora';
        t.push('r ' + rad);
      }
      if (tm) { var bg = tm[cs.backgroundColor]; if (bg) t.push('fondo ' + bg); var fg = tm[cs.color]; if (fg) t.push('texto ' + fg); }
      put(el, t.join(' · '));
    });
    if (capas.jerarquia) document.querySelectorAll(TXT).forEach(function (el) {
      if (el.closest('.lx-ov,#lx-guide,#lx-marks,script,style,svg')) return;
      if (![].some.call(el.childNodes, function (k) { return k.nodeType === 3 && k.textContent.trim(); })) return;
      var cs = getComputedStyle(el); put(el, px(cs.fontSize) + '/' + cs.fontWeight + ' · ' + cs.fontFamily.split(',')[0].replace(/['"]/g, ''));
    });
  }

  /* ── Comprobaciones con evidencia ──
     Cada resultado dice qué se midió, en qué elemento, contra qué criterio y cómo corregirlo.
     Dos niveles que no se mezclan: WCAG 2.2 AA (normativo) y Ergonomía/identidad Keyons (recomendación).
     Lo que no se puede medir leyendo tamaño, color o atributos va a Revisión manual o queda Sin verificar. */
  function lum(c) {
    var m = c.match(/[\d.]+/g); if (!m) return null;
    var a = m.length > 3 ? +m[3] : 1;
    var f = m.slice(0, 3).map(function (v) { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); });
    return { l: .2126 * f[0] + .7152 * f[1] + .0722 * f[2], a: a };
  }
  function bgOf(el) {
    while (el && el !== document) {
      var cs = getComputedStyle(el), b = lum(cs.backgroundColor);
      if (b && b.a > .6) return b.l;
      if (cs.backgroundImage && cs.backgroundImage !== 'none' && el !== body) return null;
      el = el.parentElement;
    }
    return document.getElementById('lx-sky') ? null : null;   // sin color propio ni del cuerpo: no hay evidencia
  }
  var marks = [];
  function mark(el) { var i = marks.indexOf(el); if (i < 0) { marks.push(el); i = marks.length - 1; } return i; }
  function label(el) {
    var t = (el.getAttribute('aria-label') || el.textContent || el.getAttribute('placeholder') || el.tagName).replace(/\s+/g, ' ').trim();
    return (t.length > 34 ? t.slice(0, 33) + '…' : t) || el.tagName.toLowerCase();
  }
  function where(el) {
    var parts = [], e = el;
    while (e && e !== body && parts.length < 3) { var c = (e.className || '').toString().split(' ').filter(function (x) { return x.indexOf('lx-') === 0; })[0]; parts.unshift(c ? '.' + c : e.tagName.toLowerCase()); e = e.parentElement; }
    return parts.join(' › ');
  }
  function status(items, hasManual) {
    if (!items.length) return 'sin';
    if (items.some(function (x) { return x.ok === false; })) return 'no';
    if (hasManual || items.some(function (x) { return x.ok === null; })) return 'manual';
    return 'cumple';
  }
  var SCALE = [12, 14, 16, 20, 24];
  function checks() {
    var W = root.clientWidth, R = []; marks = [];
    var ovs = document.querySelectorAll('.lx-ov,#lx-guide,#lx-marks'); ovs.forEach(function (o) { o.style.display = 'none'; });
    var texts = [].filter.call(document.querySelectorAll('body *'), function (el) {
      if (el.closest('.lx-ov,#lx-guide,#lx-marks,#lx-sky,script,style,svg')) return false;
      var r = el.getBoundingClientRect(); if (!r.width || !r.height) return false;
      return [].some.call(el.childNodes, function (n) { return n.nodeType === 3 && n.textContent.trim(); });
    });
    var ctrls = [].filter.call(document.querySelectorAll('a[href],button,input:not([type="hidden"]),select,textarea,[role="button"],[tabindex]:not([tabindex="-1"])'), function (el) { return el.getBoundingClientRect().width && !el.closest('.lx-ov'); });

    /* 1 · Contraste del texto · WCAG 2.2 AA 1.4.3 */
    var it = [];
    texts.forEach(function (el) {
      var cs = getComputedStyle(el), f = parseFloat(cs.fontSize), fg = lum(cs.color), bg = bgOf(el);
      var big = f >= 24 || (f >= 18.66 && +cs.fontWeight >= 700), need = big ? 3 : 4.5;
      if (!fg) return;
      if (bg === null) { it.push({ i: mark(el), e: label(el), u: where(el), v: 'fondo con imagen o degradado', x: need + ':1', ok: null }); return; }
      var ratio = (Math.max(fg.l, bg) + .05) / (Math.min(fg.l, bg) + .05);
      it.push({ i: mark(el), e: label(el), u: where(el), v: ratio.toFixed(2).replace('.', ',') + ':1', x: need.toString().replace('.', ',') + ':1', ok: ratio >= need - .005 });
    });
    R.push({ id: 'contraste', k: 'Contraste del texto', nivel: 'wcag', ref: 'WCAG 2.2 · 1.4.3', norma: 'KYN-MRK-VIS-008', req: 'Texto normal 4,5:1; texto grande (24 px, o 18,66 px en negrita) 3:1.', met: 'Color del texto frente al primer fondo opaco de sus contenedores.', items: it, fix: 'Use Azul Noche sobre fondos claros o Blanco Keyons sobre fondos oscuros, o cambie el fondo del contenedor.' });

    /* 2 · Tamaño del objetivo · WCAG 2.2 AA 2.5.8 (24 × 24 con excepciones) */
    it = [];
    var rects = ctrls.map(function (el) { var t = el.matches('input[type="checkbox"],input[type="radio"]') && el.closest('label') ? el.closest('label') : el; return { el: el, r: t.getBoundingClientRect() }; });
    rects.forEach(function (o) {
      var el = o.el, r = o.r, w = Math.round(r.width), h = Math.round(r.height);
      var inline = el.tagName === 'A' && getComputedStyle(el).display === 'inline' && el.parentElement && /^(P|LI|SPAN|TD)$/.test(el.parentElement.tagName);
      if (inline) { it.push({ i: mark(el), e: label(el), u: where(el), v: w + ' × ' + h + ' px, enlace en el texto', x: 'excepción «en línea»', ok: true }); return; }
      if (w >= 24 && h >= 24) { it.push({ i: mark(el), e: label(el), u: where(el), v: w + ' × ' + h + ' px', x: '24 × 24 px', ok: true }); return; }
      var cx = r.left + r.width / 2, cy = r.top + r.height / 2, near = rects.some(function (p) { if (p === o) return false; var dx = p.r.left + p.r.width / 2 - cx, dy = p.r.top + p.r.height / 2 - cy; return Math.sqrt(dx * dx + dy * dy) < 24; });
      it.push({ i: mark(el), e: label(el), u: where(el), v: w + ' × ' + h + ' px' + (near ? '' : ', con espacio suficiente alrededor'), x: '24 × 24 px o espaciado de 24 px', ok: !near });
    });
    R.push({ id: 'objetivo', k: 'Tamaño del objetivo', nivel: 'wcag', ref: 'WCAG 2.2 · 2.5.8', req: 'Cada control mide al menos 24 × 24 px CSS, salvo excepciones: espaciado suficiente, enlace dentro del texto o control nativo.', met: 'Tamaño real de cada control (o de su etiqueta) y distancia al control más cercano.', items: it, fix: 'Aumente el alto o el relleno del control, o sepárelo de los demás.' });

    /* 3 · Ergonomía táctil Keyons · recomendación de 44 px (criterio AAA 2.5.5) */
    it = [];
    if (W < 1025) rects.forEach(function (o) { var w = Math.round(o.r.width), h = Math.round(o.r.height); it.push({ i: mark(o.el), e: label(o.el), u: where(o.el), v: w + ' × ' + h + ' px', x: '44 × 44 px', ok: w >= 44 && h >= 44 ? true : 'rec' }); });
    R.push({ id: 'tactil', k: 'Ergonomía táctil', nivel: 'keyons', ref: 'Keyons · basada en WCAG 2.5.5 (AAA)', req: 'En tableta y móvil, los controles miden 44 × 44 px para tocarlos con comodidad. Es una recomendación, no un requisito AA.', met: W < 1025 ? 'Tamaño real de cada control a ' + W + ' px.' : 'Se comprueba en Tableta o Móvil.', items: it, fix: 'Lleve el control a 44 px de alto en anchos táctiles.', sinMsg: 'Pruebe en Tableta o Móvil: a ' + W + ' px no aplica.' });

    /* 4 · Nombre accesible · WCAG 2.2 4.1.2 */
    it = [];
    ctrls.forEach(function (el) {
      var n = el.getAttribute('aria-label') || el.getAttribute('aria-labelledby') || el.getAttribute('title') || (el.id && document.querySelector('label[for="' + el.id + '"]')) || el.closest('label') || (!/^(INPUT|SELECT|TEXTAREA)$/.test(el.tagName) && el.textContent.trim());
      it.push({ i: mark(el), e: label(el), u: where(el), v: n ? 'tiene nombre' : 'sin nombre', x: 'nombre accesible', ok: !!n });
    });
    R.push({ id: 'nombre', k: 'Nombre de cada control', nivel: 'wcag', ref: 'WCAG 2.2 · 4.1.2', req: 'Cada control expone un nombre que lo identifica.', met: 'Texto visible, aria-label, aria-labelledby, title o etiqueta asociada.', items: it, fix: 'Agregue texto visible o aria-label al control.' });

    /* 5 · Etiquetas de formulario · WCAG 2.2 1.3.1 y 3.3.2 */
    it = [];
    document.querySelectorAll('input:not([type="hidden"]),select,textarea').forEach(function (el) {
      var lab = (el.id && document.querySelector('label[for="' + el.id + '"]')) || el.closest('label') || el.getAttribute('aria-labelledby');
      it.push({ i: mark(el), e: label(el), u: where(el), v: lab ? 'etiqueta asociada' : (el.getAttribute('placeholder') ? 'solo texto de ejemplo' : 'sin etiqueta'), x: 'etiqueta visible asociada', ok: !!lab });
    });
    R.push({ id: 'etiquetas', k: 'Etiquetas de los campos', nivel: 'wcag', ref: 'WCAG 2.2 · 1.3.1 y 3.3.2', req: 'Cada campo tiene una etiqueta visible asociada; el texto de ejemplo no la reemplaza.', met: 'label[for], label que envuelve el campo o aria-labelledby.', items: it, fix: 'Agregue un label con for igual al id del campo.', sinMsg: 'No hay campos en pantalla.' });

    /* 6 · Texto alternativo · WCAG 2.2 1.1.1 */
    it = [];
    document.querySelectorAll('img').forEach(function (el) { var a = el.getAttribute('alt'); it.push({ i: mark(el), e: el.getAttribute('src') || 'imagen', u: where(el), v: a === null ? 'sin alt' : a ? '«' + a.slice(0, 30) + '»' : 'alt vacío (decorativa)', x: 'alt presente', ok: a === null ? false : null }); });
    R.push({ id: 'alt', k: 'Texto alternativo', nivel: 'wcag', ref: 'WCAG 2.2 · 1.1.1', req: 'Cada imagen tiene alt; si informa, el alt la describe; si decora, va vacío.', met: 'Presencia del atributo alt. Si describe bien la imagen lo decide una persona.', items: it, fix: 'Agregue alt a la imagen.', sinMsg: 'No hay imágenes en pantalla.' });

    /* 7 · Orden del foco · WCAG 2.2 2.4.3 (solo se descarta lo medible: tabindex positivo) */
    it = [];
    document.querySelectorAll('[tabindex]').forEach(function (el) { var t = +el.getAttribute('tabindex'); if (t > 0) it.push({ i: mark(el), e: label(el), u: where(el), v: 'tabindex=' + t, x: 'sin tabindex positivo', ok: false }); });
    if (!it.length && ctrls.length) it.push({ i: mark(ctrls[0]), e: ctrls.length + ' controles', u: 'documento', v: 'sin tabindex positivo', x: 'orden lógico al recorrer con Tab', ok: null });
    R.push({ id: 'foco', k: 'Orden del foco', nivel: 'wcag', ref: 'WCAG 2.2 · 2.4.3', req: 'El foco recorre los controles en un orden que conserva el sentido.', met: 'Se descarta el tabindex positivo; el orden real se comprueba recorriendo con el teclado.', items: it, fix: 'Quite el tabindex positivo y ordene el HTML como se lee.' });

    /* 8 · Sin desplazamiento horizontal · WCAG 2.2 1.4.10 (se mide en Móvil) */
    it = [];
    if (W <= 400) { var over = root.scrollWidth - W; it.push({ i: mark(body), e: 'página', u: 'documento', v: over > 1 ? 'se sale ' + Math.round(over) + ' px' : 'sin desplazamiento', x: 'nada se sale a ' + W + ' px', ok: over <= 1 }); }
    R.push({ id: 'reflow', k: 'Sin desplazamiento horizontal', nivel: 'wcag', ref: 'WCAG 2.2 · 1.4.10', req: 'A 320 px de ancho CSS el contenido se lee sin desplazarse a los lados.', met: W <= 400 ? 'Ancho del contenido frente al ancho de ' + W + ' px.' : 'Se comprueba en Móvil.', items: it, fix: 'Permita que tablas y filas se apilen o se desplacen dentro de su propio contenedor.', sinMsg: 'Pruebe en Móvil: a ' + W + ' px no se mide.' });

    /* 9 · Tamaño mínimo del texto · Keyons TYP-002 */
    var sizes = {}; it = [];
    texts.forEach(function (el) { var f = parseFloat(getComputedStyle(el).fontSize); sizes[Math.round(f * 2) / 2] = (sizes[Math.round(f * 2) / 2] || 0) + 1; if (f < 12) it.push({ i: mark(el), e: label(el), u: where(el), v: Math.round(f * 10) / 10 + ' px', x: '12 px o más', ok: 'rec' }); });
    if (!it.length && texts.length) it.push({ i: mark(texts[0]), e: texts.length + ' textos', u: 'documento', v: 'el menor mide ' + Math.min.apply(null, Object.keys(sizes).map(Number)) + ' px', x: '12 px o más', ok: true });
    R.push({ id: 'minimo', k: 'Tamaño mínimo del texto', nivel: 'keyons', ref: 'Keyons', norma: 'KYN-MRK-TYP-002', req: 'Ningún texto mide menos de 12 px.', met: 'Tamaño calculado de cada texto visible.', items: it, fix: 'Lleve el texto a 12 px o más.' });

    /* 10 · Escala y jerarquía · Keyons TYP-002 */
    var S = Object.keys(sizes).map(Number).sort(function (a, b) { return a - b; }), off = S.filter(function (s) { return s < 32 && SCALE.indexOf(s) < 0; }), close = [];
    for (var j = 1; j < S.length; j++) if (S[j] - S[j - 1] < 2) close.push(S[j - 1] + ' y ' + S[j] + ' px');
    it = S.map(function (s) { return { i: null, e: s + ' px', u: sizes[s] + ' textos', v: SCALE.indexOf(s) > -1 || s >= 32 ? 'en la escala' : 'fuera de la escala', x: '12 · 14 · 16 · 20 · 24 · 32', ok: SCALE.indexOf(s) > -1 || s >= 32 ? true : 'rec' }; });
    close.forEach(function (c) { it.push({ i: null, e: c, u: 'tamaños vecinos', v: 'difieren menos de 2 px', x: 'diferencia clara', ok: 'rec' }); });
    R.push({ id: 'escala', k: 'Escala y jerarquía', nivel: 'keyons', ref: 'Keyons', norma: 'KYN-MRK-TYP-002', req: 'El texto de lectura usa 12 · 14 · 16 · 20 · 24 · 32 y dos niveles nunca se parecen.', met: 'Tamaños calculados de todo el texto visible.', items: it, fix: 'Use solo tamaños de la escala; si dos niveles se parecen, sepárelos un paso.' });

    /* 11 · Familias tipográficas · Keyons TYP-001 */
    var fams = {}; texts.forEach(function (el) { var f = getComputedStyle(el).fontFamily.split(',')[0].replace(/['"]/g, '').trim(); fams[f] = 1; });
    it = Object.keys(fams).map(function (f) { var ok = f === 'Plus Jakarta Sans' || f === 'TASA Orbiter'; return { i: null, e: f, u: 'familia', v: ok ? 'familia Keyons' : 'familia externa', x: 'Plus Jakarta Sans o TASA Orbiter', ok: ok || 'rec' }; });
    R.push({ id: 'familias', k: 'Familias tipográficas', nivel: 'keyons', ref: 'Keyons', norma: 'KYN-MRK-TYP-001', req: 'El texto usa las familias Keyons.', met: 'Primera familia calculada de cada texto.', items: it, fix: 'Vuelva a Plus Jakarta Sans o TASA Orbiter.' });

    /* 12 · Geometría · Keyons ESP-001 */
    it = [];
    document.querySelectorAll('.lx-card').forEach(function (c) { if (c.parentElement.classList.contains('lx-group')) return; var r = px(getComputedStyle(c).borderTopLeftRadius); it.push({ i: mark(c), e: label(c), u: where(c), v: 'radio ' + r + ' px', x: 'tarjeta aislada: 0 px', ok: r === 0 ? true : 'rec' }); });
    R.push({ id: 'geometria', k: 'Esquinas de las tarjetas', nivel: 'keyons', ref: 'Keyons', norma: 'KYN-MRK-ESP-001', req: 'Una tarjeta aislada lleva sus cuatro esquinas rectas; dentro de un grupo, exterior recta e interior curva.', met: 'Radio calculado de cada tarjeta fuera de un grupo.', items: it, fix: 'Quite el radio de la tarjeta aislada o agrúpela.', sinMsg: 'No hay tarjetas aisladas.' });

    /* 13 · Retícula · Keyons ESP-004 */
    it = [].map.call(document.querySelectorAll('[data-lx-free]'), function (el) { return { i: mark(el), e: label(el), u: where(el), v: 'movido libre: ' + (el.style.translate || ''), x: 'alineado a la retícula', ok: 'rec' }; });
    if (!it.length) it.push({ i: null, e: 'todos los bloques', u: 'documento', v: 'ningún bloque movido fuera', x: 'alineado a la retícula', ok: true });
    R.push({ id: 'reticula', k: 'Alineación a la retícula', nivel: 'keyons', ref: 'Keyons', norma: 'KYN-MRK-ESP-004', req: 'Los bloques se alinean a la retícula del ancho de prueba.', met: 'Bloques movidos con el ajuste a la retícula apagado.', items: it, fix: 'Elija el bloque y use «Volver a la retícula».' });

    /* 14 · Movimiento · Keyons VIS-007 (y preferencia de movimiento reducido) */
    it = [];
    document.querySelectorAll('body *').forEach(function (el) {
      if (el.closest('.lx-ov,#lx-guide,#lx-sky')) return;
      var cs = getComputedStyle(el); if (cs.animationName === 'none' || !parseFloat(cs.animationDuration)) return;
      var d = Math.round(parseFloat(cs.animationDuration) * 1000);
      it.push({ i: mark(el), e: label(el), u: where(el), v: d + ' ms', x: '200 a 520 ms y respeta movimiento reducido', ok: d >= 200 && d <= 1040 ? null : 'rec' });
    });
    R.push({ id: 'movimiento', k: 'Movimiento', nivel: 'keyons', ref: 'Keyons', norma: 'KYN-MRK-VIS-007', req: 'El movimiento orienta, es sereno y se detiene con la preferencia de movimiento reducido.', met: 'Animaciones activas y su duración. Si orienta y es cómodo lo decide una persona.', items: it, fix: 'Acorte o quite la animación, o actívela solo al interactuar.', sinMsg: 'No hay animaciones en pantalla.' });

    /* 15 · Una acción principal por pantalla · Keyons COL-002 */
    it = [];
    var prims = [].filter.call(document.querySelectorAll('.lx-btn--primary'), function (el) { return el.getBoundingClientRect().width; });
    if (prims.length) prims.forEach(function (el, n) { it.push({ i: mark(el), e: label(el), u: where(el), v: prims.length + ' acciones principales', x: 'una por pantalla', ok: prims.length === 1 ? true : (n === 0 ? true : 'rec') }); });
    R.push({ id: 'principal', k: 'Una acción principal', nivel: 'keyons', ref: 'Keyons', norma: 'KYN-MRK-COL-002', req: 'Salmón Tierra marca una sola acción por pantalla: la principal.', met: 'Botones principales visibles en pantalla.', items: it, fix: 'Deje una acción principal y pase las demás a Contorno o Texto.', sinMsg: 'No hay botones principales en pantalla.' });

    R.forEach(function (c) {
      var hasRec = c.items.some(function (x) { return x.ok === 'rec'; });
      c.estado = !c.items.length ? 'sin' : c.items.some(function (x) { return x.ok === false; }) ? 'no' : hasRec ? 'rec' : c.items.some(function (x) { return x.ok === null; }) ? 'manual' : 'cumple';
      if (c.estado === 'sin' && !c.sinMsg) c.sinMsg = 'No hay elementos para comprobar.';
    });
    ovs.forEach(function (o) { o.style.display = ''; });
    post({ type: 'checks', items: R, w: window.innerWidth });
  }
  function highlight(i) {
    var el = marks[i]; if (!el) return;
    el.scrollIntoView({ block: 'center', behavior: 'smooth' });
    el.setAttribute('data-lx-hl', ''); setTimeout(function () { el.removeAttribute('data-lx-hl'); }, 2200);
  }

  /* ── Edición directa (sin costo): seleccionar bloques, reescribir textos, duplicar, borrar, mover ──
     Con «Ajustar a la retícula» encendido, mover cambia el orden y el ancho en columnas;
     apagado, el bloque se arrastra libre y queda marcado como fuera de norma. */
  var editar = false, snap = true, sel = null, drag = null;
  var BLOCK = '.lx-main > *, .lx-grid > *, .lx-group > *, .lx-stack > *, .lx-top > *, .lx-row > *, .lx-nav > a';
  var TEXT = 'h1,h2,h3,h4,p,b,li,td,th,label,.lx-btn,.lx-badge,.lx-small,.lx-meta,.lx-kicker,.lx-num';
  function blockOf(el) { while (el && el !== body) { if (el.matches && el.matches(BLOCK)) return el; el = el.parentElement; } return null; }
  function info(el) {
    if (!el) return null;
    var cs = getComputedStyle(el), p = el.parentElement, grid = p && p.classList.contains('lx-grid');
    var span = grid ? (parseInt((el.style.getPropertyValue('--span') || cs.getPropertyValue('--span')), 10) || null) : null;
    var kind = el.classList.contains('lx-btn') ? 'btn' : el.classList.contains('lx-card') ? 'card' : el.classList.contains('lx-badge') ? 'badge' : 'block';
    var variant = kind === 'btn' ? (el.classList.contains('lx-btn--primary') ? 'primary' : el.classList.contains('lx-btn--outline') ? 'outline' : 'ghost')
      : kind === 'badge' ? (['ok', 'warn', 'err', 'info'].filter(function (v) { return el.classList.contains('lx-badge--' + v); })[0] || 'neutral') : '';
    var r = el.getBoundingClientRect();
    return { tag: el.tagName.toLowerCase(), cls: (el.className || '').toString().split(' ').filter(function (c) { return c.indexOf('lx-') === 0; }).slice(0, 3).join(' '),
      w: Math.round(r.width), h: Math.round(r.height), grid: grid, span: span, kind: kind, variant: variant, free: !!el.dataset.lxFree };
  }
  function select(el) {
    if (sel) sel.removeAttribute('data-lx-sel');
    sel = el; if (sel) sel.setAttribute('data-lx-sel', '');
    post({ type: 'sel', info: info(sel) });
  }
  function serialize() {
    var c = body.cloneNode(true);
    c.querySelectorAll('script,#lx-sky,.lx-ov,#lx-guide,#lx-marks').forEach(function (n) { n.remove(); });
    c.querySelectorAll('[data-lx-sel]').forEach(function (n) { n.removeAttribute('data-lx-sel'); });
    c.querySelectorAll('[contenteditable]').forEach(function (n) { n.removeAttribute('contenteditable'); });
    return c.innerHTML.trim();
  }
  function changed() { post({ type: 'html', html: serialize(), libres: document.querySelectorAll('[data-lx-free]').length }); refresh(); }
  function cmd(c, v) {
    if (!sel) return;
    var p = sel.parentElement;
    if (c === 'dup') { var d = sel.cloneNode(true); d.removeAttribute('data-lx-sel'); sel.after(d); select(d); }
    if (c === 'del') { var n = sel.nextElementSibling || sel.previousElementSibling; sel.remove(); select(n && blockOf(n)); }
    if (c === 'up' && sel.previousElementSibling) p.insertBefore(sel, sel.previousElementSibling);
    if (c === 'down' && sel.nextElementSibling) p.insertBefore(sel.nextElementSibling, sel);
    if (c === 'span' && p.classList.contains('lx-grid')) {
      var cols = parseInt(getComputedStyle(p).gridTemplateColumns.split(' ').length, 10) || 12;
      var cur = parseInt(sel.style.getPropertyValue('--span') || getComputedStyle(sel).getPropertyValue('--span'), 10) || cols;
      sel.style.setProperty('--span', Math.max(1, Math.min(cols, cur + v)));
    }
    if (c === 'variant') {
      if (sel.classList.contains('lx-btn')) { ['primary', 'outline', 'ghost'].forEach(function (k) { sel.classList.remove('lx-btn--' + k); }); sel.classList.add('lx-btn--' + v); }
      if (sel.classList.contains('lx-badge')) { ['ok', 'warn', 'err', 'info'].forEach(function (k) { sel.classList.remove('lx-badge--' + k); }); if (v !== 'neutral') sel.classList.add('lx-badge--' + v); }
    }
    if (c === 'snapback') { sel.style.removeProperty('translate'); sel.removeAttribute('data-lx-free'); }
    post({ type: 'sel', info: info(sel) }); changed();
  }
  /* Un enlace o un formulario de la maqueta nunca navegan: sacarían el diseño del escenario */
  document.addEventListener('click', function (e) { var a = e.target.closest && e.target.closest('a[href]'); if (a) e.preventDefault(); }, true);
  document.addEventListener('submit', function (e) { e.preventDefault(); }, true);
  document.addEventListener('click', function (e) {
    if (!editar) return;
    if (!e.target.closest('[contenteditable="true"]')) e.preventDefault();
    var b = blockOf(e.target); if (b) select(b);
  }, true);
  document.addEventListener('dblclick', function (e) {
    if (!editar) return;
    var t = e.target.closest(TEXT); if (!t) return;
    t.setAttribute('contenteditable', 'true'); t.focus();
    t.addEventListener('blur', function done() { t.removeAttribute('contenteditable'); t.removeEventListener('blur', done); changed(); });
  });
  document.addEventListener('pointerdown', function (e) {
    if (!editar || snap || e.target.closest('[contenteditable="true"]')) return;
    var bk = blockOf(e.target); if (!bk) return;
    if (bk !== sel) select(bk);
    var t = (sel.style.translate || '0px 0px').split(' ').map(parseFloat);
    drag = { x: e.clientX - (t[0] || 0), y: e.clientY - (t[1] || 0) }; e.preventDefault();
  });
  document.addEventListener('pointermove', function (e) {
    if (!drag || !sel) return;
    sel.style.translate = Math.round(e.clientX - drag.x) + 'px ' + Math.round(e.clientY - drag.y) + 'px';
    sel.setAttribute('data-lx-free', '');
  });
  document.addEventListener('pointerup', function () { if (drag) { drag = null; post({ type: 'sel', info: info(sel) }); changed(); } });

  /* Agregar una pieza del kit: debajo de lo seleccionado o al final */
  function insert(html) {
    var box = document.createElement('div'); box.innerHTML = html;
    var el = box.firstElementChild; if (!el) return;
    if (sel && sel.parentElement) sel.after(el);
    else { var m = document.querySelector('.lx-main'); if (!m) { m = document.createElement('main'); m.className = 'lx-main'; body.prepend(m); } m.appendChild(el); }
    var b = blockOf(el) || el;
    if (editar) select(b);
    b.scrollIntoView({ block: 'center' });
    changed();
  }

  /* Señalar: se raya sobre el diseño y se reporta qué elementos quedaron debajo. Solo viaja texto, no una imagen. */
  var marcar = false, stroke = null, marked = [];
  function layer() {
    var v = document.getElementById('lx-marks');
    if (!v) { v = document.createElementNS('http://www.w3.org/2000/svg', 'svg'); v.id = 'lx-marks'; body.appendChild(v); }
    v.style.height = Math.max(root.scrollHeight, window.innerHeight) + 'px';
    return v;
  }
  function clearMarks() { var v = document.getElementById('lx-marks'); if (v) v.remove(); marked = []; }
  function pathOf(el) {
    var parts = [], e = el;
    while (e && e !== body && parts.length < 6) { var i = 1, p = e; while ((p = p.previousElementSibling)) i++; parts.unshift(e.tagName.toLowerCase() + ':nth-child(' + i + ')'); e = e.parentElement; }
    return 'body > ' + parts.join(' > ');
  }
  function noteAt(x, y) {
    var v = document.getElementById('lx-marks'); if (v) v.style.display = 'none';
    var el = document.elementFromPoint(x, y); if (v) v.style.display = '';
    if (!el || el === body || el === root) return;
    var b = el.closest('.lx-btn,.lx-badge,.lx-input,.lx-card,.lx-table,.lx-alert,.lx-nav,h1,h2,h3,h4,p,li') || blockOf(el) || el;
    if (marked.some(function (m) { return m.el === b; }) || marked.length >= 10) return;
    marked.push({ el: b, e: label(b), u: where(b), s: pathOf(b) });
  }
  function postMarks() { post({ type: 'marks', items: marked.map(function (m) { return { e: m.e, u: m.u, s: m.s }; }) }); }
  document.addEventListener('pointerdown', function (e) {
    if (!marcar) return;
    e.preventDefault();
    var v = layer(), p = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    stroke = { p: p, d: 'M' + e.pageX + ' ' + e.pageY, n: 0 }; p.setAttribute('d', stroke.d); v.appendChild(p); noteAt(e.clientX, e.clientY);
  }, true);
  document.addEventListener('pointermove', function (e) {
    if (!stroke) return;
    stroke.d += 'L' + e.pageX + ' ' + e.pageY; stroke.p.setAttribute('d', stroke.d);
    if (++stroke.n % 4 === 0) noteAt(e.clientX, e.clientY);
  }, true);
  document.addEventListener('pointerup', function () { if (stroke) { stroke = null; postMarks(); } }, true);
  document.addEventListener('click', function (e) { if (marcar) { e.preventDefault(); e.stopPropagation(); } }, true);

  var tm = 0;
  function refresh() { clearTimeout(tm); tm = setTimeout(function () { overlay(); checks(); }, 120); }
  window.addEventListener('message', function (e) {
    var m = e.data || {};
    if (m.type === 'vars') { applyVars(m.vars, m.attrs); refresh(); }
    if (m.type === 'tecnica') { tecnica = !!m.on; if (m.capas) capas = m.capas; overlay(); }
    if (m.type === 'guia') { guia = m.v || ''; overlay(); }
    if (m.type === 'hl') highlight(m.i);
    if (m.type === 'check') checks();
    if (m.type === 'tool') { editar = m.v === 'sel'; marcar = m.v === 'mark'; body.classList.toggle('lx-editing', editar); body.classList.toggle('lx-marking', marcar); if (!editar) select(null); }
    if (m.type === 'insert') insert(m.html);
    if (m.type === 'marks-clear') clearMarks();
    if (m.type === 'snap') { snap = !!m.on; body.classList.toggle('lx-free', !snap); }
    if (m.type === 'cmd') cmd(m.c, m.v);
  });
  window.addEventListener('resize', refresh);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(refresh);
  post({ type: 'ready' });
  refresh();
})();
