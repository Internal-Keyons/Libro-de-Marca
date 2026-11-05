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

  /* ── Vista técnica: medidas del mismo componente ── */
  var SEL = '.lx-card,.lx-btn,.lx-input,.lx-select,.lx-textarea,.lx-badge,.lx-kpi,.lx-table,.lx-nav,.lx-alert,.lx-tabs,.lx-h1,.lx-h2,.lx-h3,.lx-grid,.lx-empty';
  var px = function (v) { return Math.round(parseFloat(v) || 0); };
  function overlay() {
    document.querySelectorAll('.lx-ov').forEach(function (n) { n.remove(); });
    if (!tecnica) return;
    var sx = window.scrollX, sy = window.scrollY, n = 0;
    document.querySelectorAll(SEL).forEach(function (el) {
      if (n > 60) return;
      var r = el.getBoundingClientRect(); if (!r.width || !r.height) return;
      var cs = getComputedStyle(el), o = document.createElement('div'); n++;
      o.className = 'lx-ov';
      o.style.cssText = 'left:' + (r.left + sx) + 'px;top:' + (r.top + sy) + 'px;width:' + r.width + 'px;height:' + r.height + 'px';
      var t = Math.round(r.width) + '×' + Math.round(r.height);
      var rr = function (v) { v = px(v); return v > 999 ? 'píldora' : v; };
      var rad = rr(cs.borderTopLeftRadius) + '/' + rr(cs.borderTopRightRadius) + '/' + rr(cs.borderBottomRightRadius) + '/' + rr(cs.borderBottomLeftRadius);
      if (/^(píldora\/){3}píldora$/.test(rad)) rad = 'píldora';
      if (rad !== '0/0/0/0') t += ' · r ' + rad;
      var pad = [cs.paddingTop, cs.paddingRight, cs.paddingBottom, cs.paddingLeft].map(px);
      if (pad.some(Boolean)) t += ' · p ' + pad.join(' ');
      if (cs.display.indexOf('grid') > -1 || cs.display.indexOf('flex') > -1) { if (px(cs.columnGap) || px(cs.rowGap)) t += ' · gap ' + px(cs.rowGap) + '/' + px(cs.columnGap); }
      if (/lx-h|lx-btn|lx-badge/.test(el.className)) t += ' · ' + px(cs.fontSize) + ' px ' + cs.fontWeight;
      if (el.classList.contains('lx-grid')) t += ' · ' + cs.gridTemplateColumns.split(' ').length + ' col';
      var b = document.createElement('b'); b.textContent = t; o.appendChild(b);
      body.appendChild(o);
    });
  }

  /* ── Comprobaciones ── */
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
    return null;   // fondo de imagen o cielo animado: el contraste se revisa a ojo
  }
  var SCALE = [12, 14, 16, 20, 24];
  function checks() {
    var W = window.innerWidth, touch = W < 1025, items = [];
    var ovs = document.querySelectorAll('.lx-ov'); ovs.forEach(function (o) { o.style.display = 'none'; });   // las medidas no cuentan como contenido
    var texts = [].filter.call(document.querySelectorAll('body *'), function (el) {
      if (el.closest('.lx-ov,#lx-sky,script,style,svg')) return false;
      var r = el.getBoundingClientRect(); if (!r.width || !r.height) return false;
      return [].some.call(el.childNodes, function (n) { return n.nodeType === 3 && n.textContent.trim(); });
    });
    var sizes = {}, minF = 99, lowC = 0, sample = '';
    texts.forEach(function (el) {
      var cs = getComputedStyle(el), f = parseFloat(cs.fontSize);
      sizes[Math.round(f * 2) / 2] = 1; minF = Math.min(minF, f);
      var fg = lum(cs.color), bg = bgOf(el);
      if (fg && bg !== null && bg !== undefined) {
        var hi = Math.max(fg.l, bg) + .05, lo = Math.min(fg.l, bg) + .05, ratio = hi / lo;
        var big = f >= 24 || (f >= 18.66 && +cs.fontWeight >= 600);
        if (ratio < (big ? 3 : 4.5)) { lowC++; if (!sample) sample = el.textContent.trim().slice(0, 32); }
      }
    });
    var S = Object.keys(sizes).map(Number).sort(function (a, b) { return a - b; });
    var close = [];
    for (var i = 1; i < S.length; i++) if (S[i] - S[i - 1] < 2) close.push(S[i - 1] + ' y ' + S[i]);
    var off = S.filter(function (s) { return s < 32 && SCALE.indexOf(s) < 0; });
    items.push({ k: 'Legibilidad', ok: minF >= 12, d: 'El texto más pequeño mide ' + Math.round(minF * 10) / 10 + ' px (mínimo 12).' });
    items.push({ k: 'Contraste', ok: lowC === 0, d: lowC ? lowC + ' textos por debajo de 4,5:1' + (sample ? ', por ejemplo «' + sample + '»' : '') + '.' : 'Todos los textos legibles sobre su fondo.' });
    items.push({ k: 'Jerarquía', ok: !close.length, d: close.length ? 'Tamaños demasiado parecidos: ' + close.join(', ') + ' px.' : S.length + ' tamaños, cada uno se distingue del siguiente.' });
    items.push({ k: 'Escala Keyons', ok: !off.length, warn: !!off.length, d: off.length ? 'Fuera de la escala 12 · 14 · 16 · 20 · 24 · 32: ' + off.join(', ') + ' px.' : 'Todo el texto de lectura usa la escala.' });
    var ctrls = [].filter.call(document.querySelectorAll('a[href],button,input,select,textarea,[role="button"],[tabindex]'), function (el) { return el.getBoundingClientRect().width && !el.closest('.lx-ov'); });
    var minT = touch ? 44 : 24, small = [];
    ctrls.forEach(function (el) {
      var t = el.closest('label') || el, r = t.getBoundingClientRect();
      if (Math.min(r.width, r.height) < minT - .5) small.push((el.textContent || el.getAttribute('aria-label') || el.tagName).trim().slice(0, 20));
    });
    items.push({ k: 'Áreas táctiles', ok: !small.length, d: small.length ? small.length + ' controles miden menos de ' + minT + ' px' + (small[0] ? ' («' + small[0] + '»)' : '') + '.' : 'Todos los controles miden al menos ' + minT + ' px.' });
    var noName = ctrls.filter(function (el) {
      if (el.getAttribute('aria-label') || el.getAttribute('title')) return false;
      if (/^(INPUT|SELECT|TEXTAREA)$/.test(el.tagName)) return !(el.id && document.querySelector('label[for="' + el.id + '"]')) && !el.closest('label') && !el.getAttribute('placeholder');
      return !el.textContent.trim();
    }).length;
    var posTab = document.querySelectorAll('[tabindex]:not([tabindex="0"]):not([tabindex="-1"])').length;
    items.push({ k: 'Foco y nombres', ok: !noName && !posTab, d: noName || posTab ? (noName ? noName + ' controles sin nombre accesible. ' : '') + (posTab ? posTab + ' con tabindex positivo.' : '') : 'Orden natural y cada control con nombre.' });
    var over = root.scrollWidth - W;
    items.push({ k: 'Sin desbordes', ok: over <= 1, d: over > 1 ? 'El contenido se sale ' + Math.round(over) + ' px a lo ancho.' : 'Nada se sale del ancho de ' + W + ' px.' });
    var solo = [].filter.call(document.querySelectorAll('.lx-card'), function (c) { return !c.parentElement.classList.contains('lx-group'); });
    var round = solo.filter(function (c) { return parseFloat(getComputedStyle(c).borderTopLeftRadius) > 0; }).length;
    items.push({ k: 'Geometría', ok: !round, warn: !!round, d: round ? round + ' tarjetas aisladas con esquinas curvas: la regla pide cuatro rectas.' : 'Tarjetas aisladas rectas; en grupo, exterior recta e interior curva.' });
    ovs.forEach(function (o) { o.style.display = ''; });
    post({ type: 'checks', items: items, w: W });
  }

  var tm = 0;
  function refresh() { clearTimeout(tm); tm = setTimeout(function () { overlay(); checks(); }, 120); }
  window.addEventListener('message', function (e) {
    var m = e.data || {};
    if (m.type === 'vars') { applyVars(m.vars, m.attrs); refresh(); }
    if (m.type === 'tecnica') { tecnica = !!m.on; overlay(); }
  });
  window.addEventListener('resize', refresh);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(refresh);
  post({ type: 'ready' });
  refresh();
})();
