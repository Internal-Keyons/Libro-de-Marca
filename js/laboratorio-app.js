/* Keyons · Laboratorio de Interfaces
   La página arma un escenario aislado (iframe con sandbox, sin mismo origen) con tokens.css,
   el kit css/laboratorio-kit.css y el runtime js/laboratorio-runtime.js, todos en línea.
   - Pedido: plantillas base o construcción desde cero con la API de Claude (servidor local).
   - Explorar: capas de variables sobre la base; nunca la modifican.
   - Guardados: experimentos en _lab/experimentos (local) y propuestas para la marca.
   Sin el servidor local, se puede explorar y ver las propuestas, pero no construir ni guardar. */
(function () {
  'use strict';
  const app = document.querySelector('[data-labx]');
  if (!app) return;
  const $ = (s, r = app) => r.querySelector(s);
  const $$ = (s, r = app) => [...r.querySelectorAll(s)];
  const ROOT = (document.body.dataset.root || '..') + '/';
  const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const ifr = $('[data-ifr]'), frame = $('[data-frame]'), stage = $('[data-stage]');

  /* ── Estado ── */
  const S = { titulo: 'Sin título', origen: '', pedido: '', datos: '', html: '', css: '', js: '', id: '', ex: {}, view: 'final', dev: 1280, server: null, checks: [] };
  const hist = [];

  /* ── Controles de Explorar: cada uno con su valor base (Keyons) ── */
  const KEYONS = ['#729BDD', '#10122A', '#CE635D', '#E99D9E', '#B2BFE5', '#F4F4F4', '#FFFFFF'];
  const G = [
    { t: 'Paleta', c: [
      { k: 'fondo', t: 'Fondo', type: 'select', base: 'blanco', o: [['blanco', 'Blanco Keyons'], ['puro', 'Blanco puro'], ['noche', 'Azul Noche'], ['amanecer', 'Cielo · Amanecer'], ['mediodia', 'Cielo · Mediodía'], ['atardecer', 'Cielo · Atardecer'], ['cielo-noche', 'Cielo · Noche'], ['galaxia', 'Cielo · Galaxia']] },
      { k: 'acento', t: 'Acento', type: 'color', base: '#729BDD', o: [['#729BDD', 'Azul Cielo'], ['#CE635D', 'Salmón Tierra'], ['#E99D9E', 'Salmón Atardecer'], ['#B2BFE5', 'Lavanda'], ['#10122A', 'Azul Noche']] },
      { k: 'cta', t: 'Botón principal', type: 'color', base: '#CE635D', o: [['#CE635D', 'Salmón Tierra'], ['#10122A', 'Azul Noche'], ['#729BDD', 'Azul Cielo'], ['#E99D9E', 'Salmón Atardecer']] },
    ] },
    { t: 'Tipografía', c: [
      { k: 'font', t: 'Familia del texto', type: 'select', base: 'jakarta', o: [['jakarta', 'Plus Jakarta Sans'], ['tasa', 'TASA Orbiter'], ['sistema', 'Sistema'], ['serif', 'Serif'], ['mono', 'Monoespaciada']] },
      { k: 'fontd', t: 'Familia de títulos', type: 'select', base: 'tasa', o: [['tasa', 'TASA Orbiter'], ['jakarta', 'Plus Jakarta Sans'], ['serif', 'Serif'], ['sistema', 'Sistema']] },
      { k: 'fs', t: 'Escala', type: 'range', base: 1, min: .875, max: 1.25, step: .125, f: (v) => '×' + v },
      { k: 'ratio', t: 'Jerarquía', type: 'range', base: 1.25, min: 1.125, max: 1.5, step: .025, f: (v) => v.toFixed(3).replace(/0+$/, '') },
      { k: 'track', t: 'Tracking', type: 'range', base: 0, min: -.03, max: .06, step: .01, f: (v) => Math.round(v * 100) + ' %' },
      { k: 'lh', t: 'Interlineado', type: 'range', base: 1.6, min: 1.3, max: 1.9, step: .05, f: (v) => v.toFixed(2) },
      { k: 'wt', t: 'Peso de títulos', type: 'select', base: '500', o: [['400', '400'], ['500', '500'], ['600', '600'], ['700', '700']] },
    ] },
    { t: 'Espaciado', c: [
      { k: 'sp', t: 'Densidad', type: 'select', base: '1', o: [['.75', 'Compacta'], ['1', 'Normal'], ['1.3', 'Amplia']] },
      { k: 'gap', t: 'Medianil', type: 'range', base: 24, min: 8, max: 48, step: 4, f: (v) => v + ' px' },
    ] },
    { t: 'Diagramación', c: [
      { k: 'nav', t: 'Navegación', type: 'select', base: 'side', o: [['side', 'Lateral'], ['top', 'Superior'], ['none', 'Sin navegación']] },
      { k: 'cols', t: 'Retícula', type: 'select', base: '12', o: [['12', '12 columnas'], ['8', '8 columnas'], ['4', '4 columnas']] },
      { k: 'maxw', t: 'Ancho máximo', type: 'select', base: '1200px', o: [['960px', '960 px'], ['1200px', '1200 px'], ['1440px', '1440 px'], ['none', 'Todo el ancho']] },
    ] },
    { t: 'Forma', c: [
      { k: 'r', t: 'Radio de componente', type: 'range', base: 18, min: 0, max: 40, step: 2, f: (v) => v + ' px' },
      { k: 'rc', t: 'Radio de control', type: 'range', base: 12, min: 0, max: 24, step: 2, f: (v) => v + ' px' },
      { k: 'shadow', t: 'Sombras', type: 'select', base: 'none', o: [['none', 'Ninguna'], ['soft', 'Suave'], ['strong', 'Marcada']] },
      { k: 'glass', t: 'Vidrio', type: 'select', base: '0', o: [['0', 'No'], ['1', 'Sí']] },
      { k: 'line', t: 'Líneas', type: 'select', base: '1px', o: [['0px', 'Sin líneas'], ['1px', '1 px'], ['2px', '2 px']] },
    ] },
    { t: 'Iconografía', c: [
      { k: 'istroke', t: 'Trazo', type: 'range', base: 1.6, min: 1, max: 2.5, step: .1, f: (v) => v.toFixed(1) },
      { k: 'isize', t: 'Tamaño', type: 'range', base: 20, min: 16, max: 28, step: 2, f: (v) => v + ' px' },
      { k: 'ifill', t: 'Estilo', type: 'select', base: 'line', o: [['line', 'Línea'], ['fill', 'Relleno']] },
    ] },
    { t: 'Movimiento', c: [
      { k: 'entrada', t: 'Entrada', type: 'select', base: '0', o: [['0', 'Sin animación'], ['1', 'Escalonada']] },
      { k: 'hover', t: 'Al pasar el cursor', type: 'select', base: '0', o: [['0', 'Sin efecto'], ['1', 'Elevar tarjetas']] },
      { k: 'dur', t: 'Duración', type: 'range', base: 320, min: 120, max: 800, step: 40, f: (v) => v + ' ms' },
      { k: 'ease', t: 'Curva', type: 'select', base: 'suave', o: [['suave', 'Suave'], ['elastica', 'Elástica'], ['lineal', 'Lineal']] },
    ] },
  ];
  const CTRL = {}; G.forEach((g) => g.c.forEach((c) => { CTRL[c.k] = c; }));
  const val = (k) => (k in S.ex ? S.ex[k] : CTRL[k].base);
  const FONTS = { jakarta: "'Plus Jakarta Sans',system-ui,sans-serif", tasa: "'TASA Orbiter','Plus Jakarta Sans',sans-serif", sistema: "system-ui,-apple-system,'Segoe UI',sans-serif", serif: "Georgia,'Times New Roman',serif", mono: "ui-monospace,Consolas,monospace" };
  const SKY = { amanecer: 'amanecer', mediodia: 'mediodia', atardecer: 'atardecer', 'cielo-noche': 'noche', galaxia: 'galaxia' };
  /* Texto sobre un color: Azul Noche o blanco, el que tenga más contraste (WCAG) */
  const rl = (hex) => { const n = parseInt(hex.slice(1), 16); return [n >> 16, (n >> 8) & 255, n & 255].map((c) => { c /= 255; return c <= .03928 ? c / 12.92 : Math.pow((c + .055) / 1.055, 2.4); }).reduce((t, c, i) => t + c * [.2126, .7152, .0722][i], 0); };
  const ink = (hex) => { const l = rl(hex), dark = (l + .05) / (rl('#10122A') + .05), light = 1.05 / (l + .05); return dark >= light ? '#10122A' : '#FFFFFF'; };

  /* Traduce los controles a variables del escenario y marca lo que sale de las normas */
  function compute() {
    const v = {}, a = {}, off = [];
    const f = val('fondo'), dark = f === 'noche' || f === 'cielo-noche' || f === 'galaxia';
    v['--lab-bg'] = f === 'puro' ? '#FFFFFF' : f === 'noche' ? '#10122A' : null;
    if (dark) Object.assign(v, { '--lab-surface': f === 'noche' ? '#1D1F38' : null, '--lab-surface-2': 'rgba(255,255,255,.1)', '--lab-text': '#F4F4F4', '--lab-text-2': 'rgba(244,244,244,.8)', '--lab-text-3': 'rgba(244,244,244,.62)', '--lab-border': 'rgba(255,255,255,.14)' });
    if (SKY[f]) { a.cielo = SKY[f]; a.glass = '1'; v['--lab-blur'] = '24px'; }
    const ac = val('acento'), cta = val('cta');
    v['--lab-accent'] = ac; v['--lab-accent-ink'] = ink(ac); v['--lab-cta'] = cta; v['--lab-cta-ink'] = ink(cta);
    if (!KEYONS.includes(ac.toUpperCase())) off.push('Acento ' + ac + ' fuera de la paleta');
    if (!KEYONS.includes(cta.toUpperCase())) off.push('Botón principal ' + cta + ' fuera de la paleta');
    if (cta.toUpperCase() === '#729BDD' && SKY[f]) off.push('Botón Azul Cielo sobre cielo: Cielo y Salmón no se apoyan uno sobre otro');
    v['--lab-font'] = FONTS[val('font')]; v['--lab-font-display'] = FONTS[val('fontd')];
    if (!['jakarta', 'tasa'].includes(val('font'))) off.push('Familia del texto fuera de las familias Keyons');
    if (!['jakarta', 'tasa'].includes(val('fontd'))) off.push('Familia de títulos fuera de las familias Keyons');
    v['--lab-fs'] = String(val('fs')); v['--lab-ratio'] = String(val('ratio'));
    if (val('fs') !== 1) off.push('Escala ×' + val('fs') + ': el texto sale de 12 · 14 · 16 · 20 · 24 · 32');
    if (val('ratio') !== 1.25) off.push('Jerarquía ' + val('ratio') + ': los niveles dejan de coincidir con TYP-002');
    v['--lab-track'] = val('track') + 'em'; if (val('track') !== 0) off.push('Tracking en texto de lectura (VIS-002)');
    v['--lab-lh'] = String(val('lh')); if (val('lh') < 1.5 || val('lh') > 1.65) off.push('Interlineado fuera de 1,5 a 1,65');
    v['--lab-w-title'] = val('wt');
    v['--lab-sp'] = val('sp'); v['--lab-gap'] = 'calc(' + val('gap') + 'px * var(--lab-sp))';
    if (![8, 12, 16, 24, 32, 40, 48].includes(val('gap'))) off.push('Medianil de ' + val('gap') + ' px fuera de la escala de espaciado');
    a.nav = val('nav') === 'side' ? '' : val('nav');
    a.cols = val('cols') === '12' ? '' : val('cols'); v['--lab-cols'] = val('cols');
    v['--lab-maxw'] = val('maxw');
    v['--lab-r'] = val('r') + 'px'; v['--lab-r-control'] = val('rc') + 'px';
    if (![0, 12, 18, 30].includes(val('r'))) off.push('Radio de componente de ' + val('r') + ' px fuera de ESP-002');
    if (![0, 12].includes(val('rc'))) off.push('Radio de control de ' + val('rc') + ' px fuera de ESP-002');
    v['--lab-shadow'] = { none: 'none', soft: '0 12px 32px -20px rgba(16,18,42,.3)', strong: '0 24px 60px -24px rgba(16,18,42,.55)' }[val('shadow')];
    if (val('shadow') !== 'none') off.push('Sombras: la estética Keyons es plana');
    if (val('glass') === '1') { a.glass = '1'; v['--lab-blur'] = '24px'; }
    v['--lab-line'] = val('line');
    v['--lab-icon-stroke'] = String(val('istroke')); v['--lab-icon'] = val('isize') + 'px'; v['--lab-icon-fill'] = val('ifill') === 'fill' ? 'currentColor' : 'none';
    if (val('istroke') !== 1.6 || val('ifill') !== 'line') off.push('Íconos con otro trazo o relleno que el del catálogo');
    a.anim = [val('entrada') === '1' ? 'entrada' : '', val('hover') === '1' ? 'hover' : ''].filter(Boolean).join(' ');
    v['--lab-dur'] = val('dur') + 'ms';
    v['--lab-ease'] = { suave: 'cubic-bezier(.22,.61,.36,1)', elastica: 'cubic-bezier(.34,1.56,.64,1)', lineal: 'linear' }[val('ease')];
    if (val('dur') < 200 || val('dur') > 520) off.push('Duración de ' + val('dur') + ' ms fuera del rango de movimiento');
    if (val('ease') === 'elastica') off.push('Curva elástica: el movimiento Keyons es sereno');
    return { v, a, off };
  }

  /* ── Escenario aislado ── */
  const RES = {};
  async function loadRes() {
    const get = async (p, n = 3) => {   // reintenta: un servidor local puede cortar una conexión
      for (let i = 0; i < n; i++) { try { const r = await fetch(ROOT + p); if (r.ok) return await r.text(); } catch (e) { /* reintento */ } }
      return '';
    };
    const [tok, kit, rt, cielo] = await Promise.all([get('css/tokens.css'), get('css/laboratorio-kit.css'), get('js/laboratorio-runtime.js'), get('js/keyons-cielo.js')]);
    let font = '';
    try {
      const b = await fetch(ROOT + 'assets/fonts/TASAOrbiter-VariableFont_wght.ttf').then((r) => r.blob());
      font = await new Promise((ok) => { const fr = new FileReader(); fr.onload = () => ok(fr.result); fr.readAsDataURL(b); });
    } catch (e) { /* sin la fuente, el escenario cae a Plus Jakarta Sans */ }
    RES.tok = tok.replace(/url\(['"]?\.\.\/assets\/fonts\/TASAOrbiter-VariableFont_wght\.ttf['"]?\)/, font ? `url('${font}')` : 'local("TASA Orbiter")');
    RES.kit = kit; RES.rt = rt; RES.cielo = cielo;
  }
  const safe = (s) => String(s || '').replace(/<\/(script|style)/gi, '<\\/$1');
  function build() {
    if (!S.html) { ifr.removeAttribute('srcdoc'); stage.classList.remove('has-doc'); return; }
    stage.classList.add('has-doc');
    ifr.srcdoc = `<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>${safe(RES.tok)}</style><style>${safe(RES.kit)}</style><style>${safe(S.css)}</style></head>
<body>${S.html}<script>${safe(RES.cielo)}<\/script><script>${safe(RES.rt)}<\/script>${S.js ? `<script>${safe(S.js)}<\/script>` : ''}</body></html>`;
  }
  const send = (m) => { try { ifr.contentWindow.postMessage(m, '*'); } catch (e) {} };
  function push() { const c = compute(); send({ type: 'vars', vars: c.v, attrs: c.a }); send({ type: 'tecnica', on: S.view === 'tecnica' }); renderChecks(); }
  window.addEventListener('message', (e) => {
    if (e.source !== ifr.contentWindow) return;
    const m = e.data || {};
    if (m.type === 'ready') push();
    if (m.type === 'checks') { S.checks = m.items || []; renderChecks(); }
  });

  /* Tamaño: el escenario mide el ancho del dispositivo y se escala para caber */
  const DEV_H = { 1280: 800, 768: 1024, 375: 760 };
  function fit() {
    const W = stage.clientWidth, D = S.dev, k = Math.min(1, W / D), H = DEV_H[D];
    ifr.style.width = D + 'px'; ifr.style.height = H + 'px';
    frame.style.transform = `scale(${k})`; frame.style.width = D + 'px';
    stage.style.height = Math.round(H * k) + 'px';
    $('[data-w]').textContent = D + ' px' + (k < 1 ? ' · al ' + Math.round(k * 100) + ' %' : '');
  }
  new ResizeObserver(fit).observe(stage);

  /* ── Comprobaciones: las del escenario más lo que sale de las normas ── */
  function renderChecks() {
    const off = compute().off, ul = $('[data-checks]');
    if (!S.html) { ul.innerHTML = ''; return; }
    ul.innerHTML = S.checks.map((c) => `<li class="${c.ok ? 'is-ok' : c.warn ? 'is-warn' : 'is-bad'}"><b>${esc(c.k)}</b><span>${esc(c.d)}</span></li>`).join('')
      + (off.length ? `<li class="is-warn is-off"><b>Fuera de norma</b><span>${off.map(esc).join(' · ')}</span></li>` : '<li class="is-ok"><b>Dentro de norma</b><span>La exploración coincide con la base de Keyons.</span></li>');
    $('[data-reset]').disabled = !Object.keys(S.ex).length;
  }

  /* ── Historial ── */
  const snap = () => ({ titulo: S.titulo, html: S.html, css: S.css, js: S.js, ex: { ...S.ex }, origen: S.origen });
  function record() { hist.push(snap()); if (hist.length > 40) hist.shift(); $('[data-undo]').disabled = hist.length < 2; }
  let exT = 0;
  const recordSoon = () => { clearTimeout(exT); exT = setTimeout(record, 700); };
  function undo() {
    if (hist.length < 2) return;
    hist.pop(); const p = hist[hist.length - 1];
    const changed = p.html !== S.html || p.css !== S.css || p.js !== S.js;
    Object.assign(S, { titulo: p.titulo, html: p.html, css: p.css, js: p.js, ex: { ...p.ex }, origen: p.origen });
    $('[data-title]').value = S.titulo; syncEx();
    if (changed) build(); else push();
    $('[data-undo]').disabled = hist.length < 2;
  }

  /* ── Cargar contenido ── */
  function load(o, rec = true) {
    Object.assign(S, { html: o.html || '', css: o.css || '', js: o.js || '', origen: o.origen || S.origen, titulo: o.titulo || S.titulo });
    if (o.ex) S.ex = { ...o.ex };
    $('[data-title]').value = S.titulo;
    $('[data-start]').hidden = !!S.html;
    $('[data-chg]').hidden = !S.html || !S.server || !S.server.generar;
    $('[data-save]').disabled = !S.html || !S.server;
    syncEx(); build(); fit();
    if (rec) record();
  }
  function fresh() {
    Object.assign(S, { titulo: 'Sin título', origen: '', html: '', css: '', js: '', id: '', ex: {}, checks: [] });
    hist.length = 0; $('[data-undo]').disabled = true;
    $('[data-estado]').value = 'En exploración';
    load({}, false); msg('');
  }
  const tplBtns = () => (window.LAB_PLANTILLAS || []).map((p) => `<button type="button" class="lbx__tplb" data-tpl="${p.id}"><b>${esc(p.t)}</b><span>${esc(p.d)}</span></button>`).join('');
  $$('[data-tpls]').forEach((b) => { b.innerHTML = tplBtns(); });
  app.addEventListener('click', (e) => {
    const t = e.target.closest('[data-tpl]');
    if (!t) return;
    const p = window.LAB_PLANTILLAS.find((x) => x.id === t.dataset.tpl);
    S.id = ''; S.ex = {};
    load({ html: p.html, css: '', js: '', titulo: p.t, origen: 'plantilla:' + p.id });
    msg('Plantilla «' + p.t + '» cargada. Puede rellenarla con sus datos o pedir un cambio.');
  });

  /* ── Pestañas del panel ── */
  $$('.lbx__tabs [role="tab"]').forEach((b) => b.addEventListener('click', () => {
    $$('.lbx__tabs [role="tab"]').forEach((x) => { const on = x === b; x.setAttribute('aria-selected', on); $('#' + x.getAttribute('aria-controls')).hidden = !on; });
    if (b.id === 'lbx-t-guardados') listSaved();
  }));
  const tab = (id) => $('#lbx-t-' + id).click();

  /* ── Explorar: controles ── */
  function drawEx() {
    $('[data-ex]').innerHTML = G.map((g) => `<fieldset class="lbx__g"><legend>${esc(g.t)}<button type="button" class="lbx__gr" data-greset="${esc(g.t)}">Restablecer</button></legend>` + g.c.map((c) => {
      const id = 'lbx-x-' + c.k;
      if (c.type === 'select') return `<div class="lbx__c"><label for="${id}">${esc(c.t)}</label><select id="${id}" data-x="${c.k}">${c.o.map(([v, t]) => `<option value="${esc(v)}">${esc(t)}</option>`).join('')}</select></div>`;
      if (c.type === 'range') return `<div class="lbx__c"><label for="${id}">${esc(c.t)} <output data-xo="${c.k}"></output></label><input id="${id}" type="range" min="${c.min}" max="${c.max}" step="${c.step}" data-x="${c.k}"></div>`;
      return `<div class="lbx__c"><span class="lbx__cl">${esc(c.t)}</span><div class="lbx__sw">${c.o.map(([v, t]) => `<button type="button" data-xc="${c.k}" data-v="${v}" style="--c:${v}" aria-label="${esc(t)}" title="${esc(t)}"></button>`).join('')}<label class="lbx__free" title="Color libre"><input type="color" data-x="${c.k}" aria-label="${esc(c.t)}: color libre"></label></div></div>`;
    }).join('') + '</fieldset>').join('');
  }
  function syncEx() {
    Object.values(CTRL).forEach((c) => {
      const v = val(c.k), el = $(`[data-x="${c.k}"]`);
      if (el) el.value = c.type === 'range' ? v : String(v);
      const o = $(`[data-xo="${c.k}"]`); if (o) o.textContent = c.f(+v);
      $$(`[data-xc="${c.k}"]`).forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.v.toUpperCase() === String(v).toUpperCase())));
    });
  }
  function setEx(k, v) {
    const c = CTRL[k]; if (c.type === 'range') v = +v;
    if (String(v).toUpperCase() === String(c.base).toUpperCase()) delete S.ex[k]; else S.ex[k] = v;
    syncEx(); push(); recordSoon();
  }
  drawEx();
  app.addEventListener('input', (e) => { const k = e.target.dataset && e.target.dataset.x; if (k) setEx(k, e.target.value); });
  app.addEventListener('click', (e) => {
    const b = e.target.closest('[data-xc]'); if (b) setEx(b.dataset.xc, b.dataset.v);
    const gr = e.target.closest('[data-greset]');
    if (gr) { G.find((g) => g.t === gr.dataset.greset).c.forEach((c) => delete S.ex[c.k]); syncEx(); push(); recordSoon(); }
  });

  /* ── Barra del escenario ── */
  $$('[data-view]').forEach((b) => b.addEventListener('click', () => { S.view = b.dataset.view; $$('[data-view]').forEach((x) => x.setAttribute('aria-pressed', x === b)); send({ type: 'tecnica', on: S.view === 'tecnica' }); }));
  $$('[data-dev]').forEach((b) => b.addEventListener('click', () => { S.dev = +b.dataset.dev; $$('[data-dev]').forEach((x) => x.setAttribute('aria-pressed', x === b)); fit(); }));
  $('[data-title]').addEventListener('change', (e) => { S.titulo = e.target.value.trim() || 'Sin título'; });
  $('[data-undo]').addEventListener('click', undo);
  $('[data-reset]').addEventListener('click', () => { S.ex = {}; syncEx(); push(); record(); });
  $('[data-new]').addEventListener('click', fresh);
  $('[data-scratch]').addEventListener('click', () => { tab('pedido'); $('#lbx-q').focus(); });

  /* ── Servidor local: construir, cambiar y guardar ── */
  const msg = (t, bad) => { const m = $('[data-msg]'); m.textContent = t; m.classList.toggle('is-bad', !!bad); };
  async function api(path, body) {
    const r = await fetch('/api/lab/' + path, body ? { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) } : {});
    const j = await r.json().catch(() => ({}));
    if (!r.ok || j.error) throw new Error(j.error || 'El servidor respondió ' + r.status);
    return j;
  }
  async function detect() {
    try { S.server = await api('estado'); } catch (e) { S.server = null; }
    const gen = $('[data-gen]');
    if (!S.server) {
      gen.disabled = true;
      msg('Para construir desde un pedido y guardar, abra el laboratorio con el servidor local: python tools/laboratorio.py. Las plantillas y Explorar funcionan igual.');
    } else if (!S.server.generar) {
      gen.disabled = true; msg(S.server.aviso || 'Falta configurar la clave de la API de Claude.', true);
    } else if (S.server.modo === 'demo') msg('Modo de demostración: el servidor devuelve un ejemplo fijo, sin llamar a la API.');
  }
  async function generate(cambio) {
    const pedido = $('#lbx-q').value.trim(), datos = $('#lbx-d').value.trim();
    if (!cambio && !pedido) { msg('Escriba qué quiere construir.', true); $('#lbx-q').focus(); return; }
    if (cambio && !cambio.trim()) { msg('Escriba el cambio que necesita.', true); return; }
    const busy = $('[data-busy]'); busy.hidden = false; $('[data-start]').hidden = true;
    $$('[data-gen],[data-chg-go]').forEach((b) => { b.disabled = true; });
    msg(cambio ? 'Aplicando el cambio…' : 'Construyendo… suele tardar entre 30 segundos y 2 minutos.');
    try {
      const r = await api('generar', { pedido: cambio ? S.pedido || pedido : pedido, datos, cambio: cambio || '', actual: cambio ? { html: S.html, css: S.css, js: S.js } : null });
      if (!cambio) { S.pedido = pedido; S.datos = datos; S.id = ''; S.ex = {}; }
      load({ html: r.html, css: r.css, js: r.js, titulo: cambio ? S.titulo : r.titulo, origen: cambio ? S.origen : 'pedido' });
      msg((r.resumen || 'Listo.') + (r.normas && r.normas.length ? ' Normas aplicadas: ' + r.normas.join(', ') + '.' : ''));
      if (cambio) $('#lbx-c').value = '';
    } catch (e) { msg('No se pudo construir: ' + e.message, true); $('[data-start]').hidden = !!S.html; }
    busy.hidden = true;
    $$('[data-gen],[data-chg-go]').forEach((b) => { b.disabled = false; });
  }
  $('[data-gen]').addEventListener('click', () => generate(''));
  $('[data-chg-go]').addEventListener('click', () => generate($('#lbx-c').value));
  $('[data-save]').addEventListener('click', async () => {
    try {
      const r = await api('guardar', { id: S.id, titulo: S.titulo, estado: $('[data-estado]').value, pedido: S.pedido, datos: S.datos, origen: S.origen, html: S.html, css: S.css, js: S.js, ex: S.ex });
      S.id = r.id; msg('Guardado en _lab/experimentos/' + r.id + '.json.');
    } catch (e) { msg('No se pudo guardar: ' + e.message, true); }
  });

  /* ── Guardados ── */
  async function listSaved() {
    const box = $('[data-saved]');
    let exps = [], props = [];
    if (S.server) { try { const r = await api('lista'); exps = r.experimentos || []; props = r.propuestas || []; } catch (e) { /* sigue con lo que haya */ } }
    else { try { props = (await fetch(ROOT + 'sistema-diseno/laboratorio/propuestas/index.json').then((r) => r.json())).propuestas || []; } catch (e) { /* sin propuestas todavía */ } }
    const item = (x, kind) => `<li><button type="button" class="lbx__sv" data-open="${esc(x.id)}" data-kind="${kind}"><b>${esc(x.titulo)}</b><span>${esc(x.estado || 'Propuesta')} · ${esc((x.actualizado || '').slice(0, 10))}</span></button>${kind === 'exp' && S.server ? `<button type="button" class="lbx__pp" data-prop="${esc(x.id)}">Proponer para la marca</button>` : ''}</li>`;
    box.innerHTML = (S.server ? `<p class="lbx__k">Experimentos</p>${exps.length ? `<ul class="lbx__svl">${exps.map((x) => item(x, 'exp')).join('')}</ul>` : '<p class="lbx__note">Todavía no hay experimentos guardados.</p>'}` : '<p class="lbx__note">Los experimentos se guardan con el servidor local. Aquí se ven las propuestas para la marca.</p>')
      + `<p class="lbx__k">Propuestas para la marca</p>${props.length ? `<ul class="lbx__svl">${props.map((x) => item(x, 'prop')).join('')}</ul>` : '<p class="lbx__note">Ninguna propuesta todavía.</p>'}`;
  }
  app.addEventListener('click', async (e) => {
    const o = e.target.closest('[data-open]');
    if (o) {
      try {
        const x = o.dataset.kind === 'exp' ? await api('experimento?id=' + encodeURIComponent(o.dataset.open))
          : await fetch(ROOT + 'sistema-diseno/laboratorio/propuestas/' + encodeURIComponent(o.dataset.open) + '.json').then((r) => r.json());
        hist.length = 0; S.id = o.dataset.kind === 'exp' ? x.id : ''; S.pedido = x.pedido || ''; S.datos = x.datos || '';
        $('[data-estado]').value = x.estado || 'En exploración';
        load({ html: x.html, css: x.css, js: x.js, titulo: x.titulo, origen: x.origen, ex: x.ex || {} });
        msg('Abierto: ' + x.titulo + '.');
      } catch (err) { msg('No se pudo abrir: ' + err.message, true); }
    }
    const p = e.target.closest('[data-prop]');
    if (p) { try { await api('proponer', { id: p.dataset.prop }); msg('Copiado a sistema-diseno/laboratorio/propuestas/. Se publica con el próximo envío a main.'); listSaved(); } catch (err) { msg('No se pudo proponer: ' + err.message, true); } }
  });

  /* ── Inicio ── */
  loadRes().then(() => { fit(); detect(); });
})();
