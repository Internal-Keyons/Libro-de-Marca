/* Keyons · Laboratorio de Interfaces
   Espacio de exploración para diseñadores y desarrolladores: lo que se crea aquí es una dirección visual
   para revisar, no un producto final.
   Lienzo primero: una sola navegación de etapas (Elegir, Diseñar, Comprobar, Guardar) y paneles que
   aparecen cuando se necesitan. El escenario es un iframe aislado (sandbox sin mismo origen) con tokens.css,
   el kit css/laboratorio-kit.css y el runtime js/laboratorio-runtime.js, todos en línea.
   Construir, pedir un cambio, corregir y sugerir normas usan el servicio de <meta name="keyons:lab-api">
   (hoy, el servidor local; mañana puede ser Polaris). Todo lo demás funciona sin costo.
   El trabajo no se pierde: deshacer y rehacer (también tras cambios con IA) y copia local automática. */
(function () {
  'use strict';
  const app = document.querySelector('[data-labx]');
  if (!app) return;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const ROOT = (document.body.dataset.root || '..') + '/';
  const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const ifr = $('[data-ifr]'), ifrBase = $('[data-ifr-base]'), frame = $('[data-frame]'), stage = $('[data-lstage]');
  const picker = $('[data-picker]'), pifr = $('[data-pifr]'), pframe = $('[data-pframe]');

  /* ── Estado ── */
  const S = { titulo: 'Sin título', origen: '', pedido: '', datos: '', html: '', css: '', js: '', id: '', ex: {}, view: 'final', dev: 1280, server: null, checks: [] };

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
    v['--lab-track'] = val('track') + 'em'; if (val('track') !== 0) off.push('Tracking en texto de lectura (TYP-002)');
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

  const COMBOS = [
    { t: 'Corporativo sobrio', d: 'Blanco Keyons · Plus Jakarta', sw: ['#F4F4F4', '#10122A', '#729BDD', '#CE635D'], ex: {} },
    { t: 'Producto amplio', d: 'Blanco puro · densidad amplia', sw: ['#FFFFFF', '#10122A', '#729BDD', '#E99D9E'], ex: { fondo: 'puro', sp: '1.3', maxw: '1440px' } },
    { t: 'Noche', d: 'Azul Noche · acento Salmón Atardecer', sw: ['#10122A', '#F4F4F4', '#E99D9E', '#729BDD'], ex: { fondo: 'noche', acento: '#E99D9E', cta: '#E99D9E' } },
    { t: 'Expresivo de cielo', d: 'Cielo de mediodía · vidrio', sw: ['#729BDD', '#C6D5EC', '#F4F4F4', '#10122A'], ex: { fondo: 'mediodia', cta: '#10122A' } },
  ];
  const KIT = 'r21';
  const DRAFT_KEY = 'keyons.lab.borrador';

  /* ── Escenario aislado ── */
  const RES = {};
  async function loadRes() {
    const get = async (p, n = 3) => {
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
  const doc = (html, css, js) => `<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>${safe(RES.tok)}</style><style>${safe(RES.kit)}</style><style>${safe(css)}</style></head>
<body>${html}<script>${safe(RES.cielo)}<\/script><script>${safe(RES.rt)}<\/script>${js ? `<script>${safe(js)}<\/script>` : ''}</body></html>`;
  /* El escenario solo se reconstruye cuando cambia el contenido; vistas, anchos, paneles y etapas no lo tocan */
  let built = '';
  function build(force) {
    const key = S.html + '\u0000' + S.css + '\u0000' + S.js;
    if (!S.html) { ifr.removeAttribute('srcdoc'); built = ''; stage.classList.remove('has-doc'); return; }
    stage.classList.add('has-doc');
    if (force || key !== built) { built = key; ifr.srcdoc = doc(S.html, S.css, S.js); }
    if (S.split) ifrBase.srcdoc = doc(S.html, S.css, S.js);
  }
  const send = (m, w = ifr) => { try { w.contentWindow.postMessage(m, '*'); } catch (e) {} };
  const capas = () => Object.fromEntries($$('[data-capa]').map((c) => [c.dataset.capa, c.checked]));
  function push() {
    const c = compute();
    send({ type: 'vars', vars: c.v, attrs: c.a });
    send({ type: 'tecnica', on: S.view === 'tecnica', capas: capas() });
    send({ type: 'guia', v: S.guia }); send({ type: 'editar', on: S.edit && S.stage === 'disenar' }); send({ type: 'snap', on: S.snap });
    if (S.split) { send({ type: 'vars', vars: {}, attrs: {} }, ifrBase); send({ type: 'guia', v: S.guia }, ifrBase); }
  }
  window.addEventListener('message', (e) => {
    const m = e.data || {};
    if (e.source === ifrBase.contentWindow) { if (m.type === 'ready') send({ type: 'vars', vars: {}, attrs: {} }, ifrBase); return; }
    if (e.source !== ifr.contentWindow) return;
    if (m.type === 'ready') push();
    if (m.type === 'checks') { S.checks = m.items || []; S.checkW = m.w; renderChecks(); }
    if (m.type === 'sel') showProps(m.info);
    if (m.type === 'html') { S.html = m.html; built = S.html + '\u0000' + S.css + '\u0000' + S.js; S.edited = true; recordSoon(); }
  });

  /* ── Ancho real y zoom: el ancho cambia el viewport del escenario; el zoom solo lo escala ── */
  const DEV_H = { 375: 760, 768: 1024, 1280: 800, 1440: 900 };
  function place(fr, iframe, W) {
    const D = S.dev, H = DEV_H[D] || 800;
    const k = S.zoom === 'fit' ? Math.min(1, W / D) : +S.zoom;
    iframe.style.width = D + 'px'; iframe.style.height = H + 'px';
    fr.style.transform = k !== 1 ? `scale(${k})` : ''; fr.style.width = D + 'px';
    const clip = fr.parentElement; clip.style.height = Math.round(H * k) + 'px'; clip.style.width = Math.round(D * k) + 'px';
    return k;
  }
  function fit() {
    const W = (S.split ? (stage.clientWidth - 24) / 2 : stage.clientWidth) - 32;
    const k = place(frame, ifr, W);
    if (S.split) place($('[data-base] .lbx__frame'), ifrBase, W);
    const pv = $('.lbx__pick-v');
    if (pv && !picker.hidden) { const kp = Math.min(1, pv.clientWidth / 1280); pframe.style.transform = `scale(${kp})`; pifr.style.width = '1280px'; pifr.style.height = '800px'; pv.style.height = Math.round(800 * kp) + 'px'; }
    $('[data-zoom]').title = 'Ancho ' + S.dev + ' px · Zoom ' + Math.round(k * 100) + ' %';
    const fz = $('[data-zoom] option[value="fit"]'); if (fz) fz.textContent = S.html && S.stage !== 'elegir' ? 'Ajustar · ' + Math.round(k * 100) + ' %' : 'Ajustar';
  }
  new ResizeObserver(fit).observe(stage);

  /* ── Etapas: Elegir · Diseñar · Comprobar · Guardar ── */
  const HELP = {
    elegir: ['Selecciona cómo quieres comenzar.', '../fundamentos/composicion/editorial.html#decidir'],
    disenar: ['Selecciona un elemento para modificarlo.', '../fundamentos/composicion/editorial.html#reticula'],
    comprobar: ['Revisa los resultados antes de guardar.', 'accesibilidad-adaptacion.html'],
    guardar: ['Guarda el diseño o envíalo a revisión.', '../guia/index.html#gobierno'],
  };
  function setStage(st) {
    if (st !== 'elegir' && !S.html) { msg('Elija una plantilla o construya desde cero para continuar.', true); return; }
    S.stage = st;
    $$('[data-stage]').forEach((b) => (b.dataset.stage === st ? b.setAttribute('aria-current', 'step') : b.removeAttribute('aria-current')));
    $('[data-help]').textContent = HELP[st][0]; $('[data-norm]').href = HELP[st][1];
    picker.hidden = st !== 'elegir'; $('[data-ctools]').hidden = st !== 'disenar'; $('[data-mark]').hidden = !S.html || st === 'elegir';
    $('[data-frames]').hidden = st === 'elegir';
    if (st !== 'disenar') showProps(null);
    if (st === 'comprobar') { openPanel('comprobar', 'Comprobar'); send({ type: 'check' }); }
    else if (st === 'guardar') openPanel('guardar', 'Guardar');
    else closePanel();
    push(); fit();
  }
  $$('[data-stage]').forEach((b) => b.addEventListener('click', () => setStage(b.dataset.stage)));

  /* ── Paneles: solo uno a la vez y solo cuando se pide ── */
  const side = $('[data-side]');
  function openPanel(name, title) {
    side.hidden = false; $('[data-side-t]').textContent = title;
    $$('[data-panel]').forEach((p) => { p.hidden = p.dataset.panel !== name; });
    if (name === 'abrir') listSaved();
    fit();
  }
  function closePanel() { side.hidden = true; fit(); }
  $('[data-side-x]').addEventListener('click', closePanel);
  $('[data-open-estilo]').addEventListener('click', () => (side.hidden || $('[data-panel="estilo"]').hidden ? openPanel('estilo', 'Estilo') : closePanel()));
  $('[data-scratch]').addEventListener('click', () => { openPanel('cero', 'Desde cero'); $('#lbx-q').focus(); });
  $('[data-opensaved]').addEventListener('click', () => openPanel('abrir', 'Abrir un diseño guardado'));
  const props = $('[data-props]');
  $('[data-props-x]').addEventListener('click', () => { props.hidden = true; fit(); });

  /* ── Comprobar: cuatro resultados, con evidencia por elemento ── */
  const EST = { no: ['No cumple', 1], rec: ['Recomendación Keyons', 2], manual: ['Revisión manual', 3], sin: ['Sin verificar', 4], cumple: ['Cumple', 5] };
  const WCAG = { objetivo: 'target-size-minimum', contraste: 'contrast-minimum', nombre: 'name-role-value', etiquetas: 'labels-or-instructions', alt: 'non-text-content', foco: 'focus-order', reflow: 'reflow' };
  const normHref = (id) => { const n = (window.KEYONS_NORMAS || []).find((x) => x.id === id); return n ? ROOT + n.h : ''; };
  function renderChecks() {
    const box = $('[data-results]'); if (!box) return;
    const off = compute().off;
    const all = S.checks.slice();
    if (off.length) all.push({ id: 'exploracion', k: 'Exploración fuera de norma', nivel: 'keyons', ref: 'Keyons', req: 'La exploración se aparta de la base en:', met: 'Controles de Estilo distintos de la base.', estado: 'rec', items: off.map((x) => ({ i: null, e: x, u: 'Estilo', v: 'fuera de norma', x: 'base Keyons', ok: 'rec' })), fix: 'Use «Restablecer» en el grupo de Estilo correspondiente.' });
    const cnt = {}; all.forEach((c) => { cnt[c.estado] = (cnt[c.estado] || 0) + 1; });
    $('[data-sum]').innerHTML = Object.keys(EST).map((k) => `<span class="lbx__st lbx__st--${k}"><b>${cnt[k] || 0}</b>${EST[k][0]}</span>`).join('') + `<span class="lbx__k">Ancho de prueba: ${S.checkW || S.dev} px</span>`;
    const ord = all.slice().sort((a, b) => EST[a.estado][1] - EST[b.estado][1] || (a.nivel === 'wcag' ? -1 : 1));
    box.innerHTML = ord.map((c) => {
      const ref = c.nivel === 'wcag' && WCAG[c.id] ? `<a href="https://www.w3.org/WAI/WCAG22/Understanding/${WCAG[c.id]}" target="_blank" rel="noopener">${esc(c.ref)}</a>` : esc(c.ref);
      const nm = c.norma ? ` · <a href="${normHref(c.norma)}">${esc(c.norma)}</a>` : '';
      const items = (c.items || []).filter((x) => x.ok !== true).slice(0, 12);
      const rows = items.map((x) => `<li class="${x.ok === false ? 'is-no' : x.ok === 'rec' ? 'is-rec' : 'is-manual'}">${x.i !== null && x.i !== undefined ? `<button type="button" class="lbx__el" data-hl="${x.i}">${esc(x.e)}</button>` : `<span class="lbx__el">${esc(x.e)}</span>`}<span>${esc(x.u)}</span><span>Detectado: ${esc(x.v)} · Esperado: ${esc(x.x)}</span></li>`).join('');
      const okN = (c.items || []).filter((x) => x.ok === true).length;
      return `<details class="lbx__res lbx__res--${c.estado}"${c.estado === 'no' ? ' open' : ''}><summary><span class="lbx__badge">${EST[c.estado][0]}</span><b>${esc(c.k)}</b><span class="lbx__lvl">${c.nivel === 'wcag' ? 'WCAG 2.2 AA' : 'Keyons'}</span></summary>
        <dl><div><dt>Norma</dt><dd>${ref}${nm}</dd></div><div><dt>Requisito</dt><dd>${esc(c.req)}</dd></div><div><dt>Método</dt><dd>${esc(c.met)}</dd></div>
        <div><dt>Evidencia</dt><dd>${c.estado === 'sin' ? esc(c.sinMsg || '') : `${okN} elementos cumplen${items.length ? ', ' + items.length + ' requieren atención' : ''}.`}</dd></div>
        ${c.estado !== 'cumple' && c.estado !== 'sin' ? `<div><dt>Cómo corregir</dt><dd>${esc(c.fix)}</dd></div>` : ''}</dl>
        ${rows ? `<ul class="lbx__items">${rows}</ul>` : ''}</details>`;
    }).join('');
    $('[data-fix]').hidden = $('[data-cost-fix]').hidden = !S.server || !S.server.generar || !all.some((c) => c.estado === 'no');
  }
  $('[data-results]').addEventListener('click', (e) => { const b = e.target.closest('[data-hl]'); if (b) send({ type: 'hl', i: +b.dataset.hl }); });

  /* Revisión manual: lo que solo una persona puede evaluar; se registra aparte */
  const MANUAL = [
    ['fondos', 'Lectura sobre fotografías, degradados y fondos variables'],
    ['agrupacion', 'La agrupación comunica bien las relaciones entre elementos'],
    ['orientacion', 'Una persona encuentra lo que necesita y entiende dónde está'],
    ['formularios', 'Instrucciones y mensajes ayudan a completar y recuperar la tarea'],
    ['jerarquia', 'Se reconoce rápido la información más importante'],
    ['teclado', 'Recorrido real con teclado y tecnologías de asistencia'],
    ['responsive', 'La distribución sigue siendo cómoda en cada ancho'],
    ['movimiento', 'La animación orienta, aclara y resulta cómoda'],
    ['marca', 'La composición conserva el carácter de Keyons'],
  ];
  function renderManual() {
    $('[data-manual]').innerHTML = MANUAL.map(([k, t]) => {
      const r = (S.revision || {})[k];
      return `<li><span>${esc(t)}</span><span class="lbx__mbtns"><button type="button" data-m="${k}" data-r="cumple" aria-pressed="${r && r.estado === 'cumple'}">Cumple</button><button type="button" data-m="${k}" data-r="no" aria-pressed="${r && r.estado === 'no'}">No cumple</button></span>${r ? `<small>${r.estado === 'cumple' ? 'Cumple' : 'No cumple'} · ${esc(r.quien)} · ${esc(r.fecha)}</small>` : '<small>Sin evaluar</small>'}</li>`;
    }).join('');
  }
  $('[data-manual]').addEventListener('click', (e) => {
    const b = e.target.closest('[data-m]'); if (!b) return;
    const quien = $('[data-rev-quien]').value.trim();
    if (!quien) { msg('Escriba quién revisa antes de registrar el resultado.', true); $('[data-rev-quien]').focus(); return; }
    S.revision = S.revision || {}; S.revision[b.dataset.m] = { estado: b.dataset.r, quien, fecha: new Date().toISOString().slice(0, 10) };
    renderManual(); autosave();
  });

  /* ── Historial: deshacer y rehacer, también después de cambios hechos con IA ── */
  const hist = [], redo = [];
  const snap = () => ({ titulo: S.titulo, html: S.html, css: S.css, js: S.js, ex: { ...S.ex }, origen: S.origen });
  const same = (a, b) => a && b && a.html === b.html && a.css === b.css && a.js === b.js && JSON.stringify(a.ex) === JSON.stringify(b.ex) && a.titulo === b.titulo;
  function record() { const s = snap(); if (same(hist[hist.length - 1], s)) return; hist.push(s); if (hist.length > 60) hist.shift(); redo.length = 0; histUI(); autosave(); }
  let exT = 0;
  const recordSoon = () => { clearTimeout(exT); exT = setTimeout(record, 600); };
  function restore(p) { Object.assign(S, { titulo: p.titulo, html: p.html, css: p.css, js: p.js, ex: { ...p.ex }, origen: p.origen }); $('[data-title]').value = S.titulo; syncEx(); build(); push(); autosave(); }
  function undo() { if (hist.length < 2) return; redo.push(hist.pop()); restore(hist[hist.length - 1]); histUI(); }
  function redoIt() { if (!redo.length) return; const p = redo.pop(); hist.push(p); restore(p); histUI(); }
  function histUI() { $('[data-undo]').disabled = hist.length < 2; $('[data-redo]').disabled = !redo.length; $('[data-draft]').disabled = !S.html; }
  $('[data-undo]').addEventListener('click', undo); $('[data-redo]').addEventListener('click', redoIt);
  document.addEventListener('keydown', (e) => {
    if (!(e.ctrlKey || e.metaKey) || e.target.closest('input,textarea')) return;
    if (e.key.toLowerCase() === 'z' && !e.shiftKey) { e.preventDefault(); undo(); }
    if (e.key.toLowerCase() === 'y' || (e.key.toLowerCase() === 'z' && e.shiftKey)) { e.preventDefault(); redoIt(); }
  });

  /* ── Copia local automática: el trabajo no se pierde al recargar ── */
  function autosave() {
    if (!S.html) return;
    try { localStorage.setItem(DRAFT_KEY, JSON.stringify({ t: Date.now(), s: { ...snap(), pedido: S.pedido, datos: S.datos, id: S.id, estado: S.estado, revision: S.revision || {} } })); } catch (e) { /* sin almacenamiento local */ }
  }
  function offerRecover() {
    let d = null; try { d = JSON.parse(localStorage.getItem(DRAFT_KEY) || 'null'); } catch (e) { d = null; }
    if (!d || !d.s || !d.s.html) return;
    const box = $('[data-recover]'); box.hidden = false;
    $('[data-recover-when]').textContent = new Date(d.t).toLocaleString('es');
    $('[data-recover-yes]').onclick = () => { box.hidden = true; Object.assign(S, { pedido: d.s.pedido || '', datos: d.s.datos || '', id: d.s.id || '', estado: d.s.estado || 'En exploración', revision: d.s.revision || {} }); load(d.s); setStage('disenar'); msg('Borrador recuperado.'); };
    $('[data-recover-no]').onclick = () => { box.hidden = true; try { localStorage.removeItem(DRAFT_KEY); } catch (e) { /* nada */ } };
  }

  /* ── Cargar contenido ── */
  function load(o, rec = true) {
    Object.assign(S, { html: o.html || '', css: o.css || '', js: o.js || '', origen: o.origen || S.origen, titulo: o.titulo || S.titulo });
    if (o.ex) S.ex = { ...o.ex };
    $('[data-title]').value = S.titulo; $('[data-estado]').value = S.estado || 'En exploración';
    syncEx(); build(); renderManual(); histUI();
    if (rec) record();
  }
  function fresh() {
    Object.assign(S, { titulo: 'Sin título', origen: '', html: '', css: '', js: '', id: '', ex: {}, checks: [], estado: 'En exploración', revision: {}, edited: false });
    hist.length = 0; redo.length = 0; histUI();
    try { localStorage.removeItem(DRAFT_KEY); } catch (e) { /* nada */ }
    load({}, false); msg(''); setStage('elegir'); pick(S.tpl || 'dashboard');
  }

  /* ── Elegir plantilla ── */
  const TPL = window.LAB_PLANTILLAS || [], ICON = window.LAB_ICONOS || {};
  const TICON = { dashboard: 'chart', listado: 'users', formulario: 'file', ajustes: 'gear', estados: 'alert' };
  $('[data-tpls]').innerHTML = TPL.map((p) => `<li role="option" aria-selected="false" tabindex="0" data-tpl="${p.id}"><svg viewBox="0 0 24 24" aria-hidden="true">${ICON[TICON[p.id]] || ''}</svg><b>${esc(p.t)}</b><span>(${esc(p.d)})</span></li>`).join('');
  function pick(id) {
    S.tpl = id; const p = TPL.find((x) => x.id === id) || TPL[0];
    $$('[data-tpl]').forEach((li) => li.setAttribute('aria-selected', String(li.dataset.tpl === p.id)));
    if (RES.kit) pifr.srcdoc = doc(p.html, '', '');
    fit();
  }
  $('[data-tpls]').addEventListener('click', (e) => { const li = e.target.closest('[data-tpl]'); if (li) pick(li.dataset.tpl); });
  $('[data-tpls]').addEventListener('keydown', (e) => { const li = e.target.closest('[data-tpl]'); if (li && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); pick(li.dataset.tpl); } });
  $('[data-use]').addEventListener('click', () => {
    if (S.html && !confirm('Se reemplazará el diseño del lienzo. Podrá volver con Deshacer. ¿Continuar?')) return;
    const p = TPL.find((x) => x.id === S.tpl) || TPL[0];
    S.id = ''; S.ex = {};
    load({ html: p.html, css: '', js: '', titulo: p.t, origen: 'plantilla:' + p.id });
    setStage('disenar');
    msg('Plantilla «' + p.t + '» cargada.');
  });

  /* ── Estilo: controles en grupos abiertos ── */
  function drawEx() {
    $('[data-ex]').innerHTML = G.map((g) => `<fieldset class="lbx__g"><legend><span>${esc(g.t)}</span><button type="button" class="lbx__gr" data-greset="${esc(g.t)}">Restablecer</button></legend>` + g.c.map((c) => {
      const id = 'lbx-x-' + c.k;
      if (c.type === 'select') return `<div class="lbx__ctl"><label for="${id}">${esc(c.t)}</label><select id="${id}" data-x="${c.k}">${c.o.map(([v, t]) => `<option value="${esc(v)}">${esc(t)}</option>`).join('')}</select></div>`;
      if (c.type === 'range') return `<div class="lbx__ctl"><label for="${id}">${esc(c.t)} <output data-xo="${c.k}"></output></label><input id="${id}" type="range" min="${c.min}" max="${c.max}" step="${c.step}" data-x="${c.k}"></div>`;
      return `<div class="lbx__ctl"><span>${esc(c.t)}</span><div class="lbx__sw">${c.o.map(([v, t]) => `<button type="button" data-xc="${c.k}" data-v="${v}" style="--c:${v}" aria-label="${esc(t)}" title="${esc(t)}"></button>`).join('')}<label class="lbx__free" title="Color libre"><input type="color" data-x="${c.k}" aria-label="${esc(c.t)}: color libre"></label></div></div>`;
    }).join('') + '</fieldset>').join('');
    $('[data-combos]').innerHTML = COMBOS.map((c, i) => `<button type="button" class="lbx__combo" data-combo="${i}"><span class="lbx__combo-sw">${c.sw.map((x) => `<i style="background:${x}"></i>`).join('')}</span><b>${esc(c.t)}</b><span>${esc(c.d)}</span></button>`).join('');
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
    const cb = e.target.closest('[data-combo]');
    if (cb && S.html) { S.ex = { ...COMBOS[+cb.dataset.combo].ex }; syncEx(); push(); record(); }
  });

  /* ── Diseñar: editar, retícula, guía y propiedades contextuales ── */
  $('[data-edit]').addEventListener('change', (e) => { S.edit = e.target.checked; push(); if (!S.edit) showProps(null); });
  $('[data-snap]').addEventListener('change', (e) => { S.snap = e.target.checked; push(); });
  $('[data-guia]').addEventListener('change', (e) => { S.guia = e.target.value; push(); });
  $$('[data-capa]').forEach((c) => c.addEventListener('change', push));
  const VARS = { btn: [['primary', 'Principal'], ['outline', 'Contorno'], ['ghost', 'Texto']], badge: [['neutral', 'Neutra'], ['ok', 'Éxito'], ['warn', 'Advertencia'], ['err', 'Error'], ['info', 'Información']] };
  function showProps(info) {
    props.hidden = !info;
    if (info) {
      $('[data-pinfo]').textContent = `${info.cls || info.tag} · ${info.w} × ${info.h} px${info.span ? ' · ' + info.span + ' columnas' : ''}`;
      $$('[data-gridonly]').forEach((b) => { b.hidden = !info.grid || !S.snap; });
      $$('[data-freeonly]').forEach((b) => { b.hidden = !info.free; });
      const vs = VARS[info.kind], sel = $('[data-var]');
      $('[data-varwrap]').hidden = sel.hidden = !vs;
      if (vs) { sel.innerHTML = vs.map(([v, t]) => `<option value="${v}">${t}</option>`).join(''); sel.value = info.variant; }
    }
    fit();
  }
  $$('[data-cmd]').forEach((b) => b.addEventListener('click', () => send({ type: 'cmd', c: b.dataset.cmd, v: b.dataset.v ? +b.dataset.v : undefined })));
  $('[data-var]').addEventListener('change', (e) => send({ type: 'cmd', c: 'variant', v: e.target.value }));

  /* ── Barra superior ── */
  $$('[data-view]').forEach((b) => b.addEventListener('click', () => { S.view = b.dataset.view; $$('[data-view]').forEach((x) => x.setAttribute('aria-pressed', x === b)); $('[data-ttools]').hidden = S.view !== 'tecnica'; push(); }));
  $('[data-dev]').addEventListener('change', (e) => { S.dev = +e.target.value; fit(); setTimeout(() => send({ type: 'check' }), 300); });
  $('[data-zoom]').addEventListener('change', (e) => { S.zoom = e.target.value; stage.classList.toggle('is-real', S.zoom !== 'fit'); fit(); });
  $('[data-title]').addEventListener('change', (e) => { S.titulo = e.target.value.trim() || 'Sin título'; record(); });
  const menu = $('[data-menu]'), more = $('[data-more]');
  more.addEventListener('click', () => { const o = menu.hidden; menu.hidden = !o; more.setAttribute('aria-expanded', String(o)); });
  document.addEventListener('click', (e) => { if (!e.target.closest('.lbx__more')) { menu.hidden = true; more.setAttribute('aria-expanded', 'false'); } });
  $('[data-new]').addEventListener('click', () => { if (!S.html || confirm('Se cerrará este diseño. Lo que no haya guardado queda en Deshacer solo mientras la página esté abierta. ¿Empezar de nuevo?')) fresh(); });
  $('[data-split]').addEventListener('click', (e) => {
    if (!S.html) return;
    S.split = !S.split; e.currentTarget.setAttribute('aria-pressed', String(S.split));
    $('[data-base]').hidden = !S.split; $('[data-cap-main]').hidden = !S.split; stage.classList.toggle('is-split', S.split);
    if (S.split) ifrBase.srcdoc = doc(S.html, S.css, S.js);
    fit();
  });
  $('[data-full]').addEventListener('click', (e) => {
    const on = !app.classList.contains('is-full'); app.classList.toggle('is-full', on); document.body.classList.toggle('lbx-full', on);
    e.currentTarget.textContent = on ? 'Salir de pantalla completa' : 'Pantalla completa'; fit();
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && app.classList.contains('is-full')) $('[data-full]').click(); });

  /* ── Exportar ── */
  const slugify = (t) => t.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  function exportDoc() {
    const c = compute(), vars = Object.entries(c.v).filter(([, v]) => v !== null && v !== '').map(([k, v]) => `${k}:${v}`).join(';');
    const attrs = Object.entries(c.a).filter(([, v]) => v).map(([k, v]) => `body.setAttribute('data-${k}','${v}');`).join('');
    const note = `<!-- Keyons · Laboratorio de Interfaces · «${S.titulo}». Exploración: no es un producto final. Requiere revisión antes de aplicarse. Kit ${KIT}. -->`;
    return doc(S.html, S.css + `:root{${vars}}`, (S.js || '') + `;(function(){var body=document.body;${attrs}})();`).replace('<!DOCTYPE html>', '<!DOCTYPE html>\n' + note);
  }
  $('[data-export]').addEventListener('click', () => {
    const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([exportDoc()], { type: 'text/html' }));
    a.download = (slugify(S.titulo) || 'experimento') + '.html'; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 2000);
    msg('Exportado como HTML independiente, con la nota «Exploración · no es un producto final».');
  });

  /* ── Servicio que construye (hoy el servidor local; mañana Polaris) ── */
  const API = (document.querySelector('meta[name="keyons:lab-api"]') || {}).content || window.LAB_API || '/api/lab/';
  const msg = (t, bad) => { const m = $('[data-msg]'); m.textContent = t; m.classList.toggle('is-bad', !!bad); };
  async function api(path, body) {
    const r = await fetch(API + path, body ? { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) } : {});
    const j = await r.json().catch(() => ({}));
    if (!r.ok || j.error) throw new Error(j.error || 'El servicio respondió ' + r.status);
    return j;
  }
  async function detect() {
    try { S.server = await api('estado'); } catch (e) { S.server = null; }
    const gen = $('[data-gen]');
    if (!S.server) { gen.disabled = true; $('[data-cost-gen]').textContent = 'Para construir y guardar, abra el laboratorio con el servidor local (python tools/laboratorio.py).'; }
    else if (!S.server.generar) { gen.disabled = true; $('[data-cost-gen]').textContent = S.server.aviso || 'Falta configurar la clave de la API de Claude.'; }
    else if (S.server.modo === 'demo') { $$('.lbx__cost').forEach((c) => { c.textContent = 'Modo de demostración: no llama a la API ni tiene costo.'; }); }
    $('[data-save]').disabled = $('[data-send]').disabled = !S.server;
  }
  const costTxt = (c) => (c ? `Esta operación: ≈ USD ${String(c.usd).replace('.', ',')} · ${c.enviados.toLocaleString('es')} tokens enviados (${c.en_memoria.toLocaleString('es')} en memoria) · ${c.recibidos.toLocaleString('es')} recibidos.` : '');
  async function generate(cambio, costEl) {
    const pedido = $('#lbx-q').value.trim(), datos = $('#lbx-d').value.trim();
    if (!cambio && !pedido) { msg('Escriba qué quiere construir.', true); $('#lbx-q').focus(); return; }
    const busy = $('[data-busy]'); busy.hidden = false;
    msg(cambio ? 'Aplicando el cambio…' : 'Construyendo… suele tardar entre 30 segundos y 2 minutos.');
    try {
      const r = await api('generar', { pedido: cambio ? S.pedido || pedido : pedido, datos, cambio: cambio || '', actual: cambio ? { html: S.html, css: S.css, js: S.js } : null });
      if (!cambio) { S.pedido = pedido; S.datos = datos; S.id = ''; S.ex = {}; }
      load({ html: r.html, css: r.css, js: r.js, titulo: cambio ? S.titulo : r.titulo, origen: cambio ? S.origen : 'pedido' });
      if (S.stage === 'elegir') setStage('disenar'); else { push(); if (S.stage === 'comprobar') send({ type: 'check' }); }
      msg((r.resumen || 'Listo.') + ' Puede volver atrás con Deshacer.');
      if (costEl && r.costo) costEl.textContent = costTxt(r.costo);
    } catch (e) { msg('No se pudo completar: ' + e.message, true); }
    busy.hidden = true;
  }
  $('[data-gen]').addEventListener('click', () => { closePanel(); generate('', $('[data-cost-gen]')); });
  const dlg = $('[data-dlg]');
  $('[data-ask]').addEventListener('click', () => { if (!S.server || !S.server.generar) { msg('Pedir un cambio necesita el servidor local con la API configurada.', true); return; } dlg.showModal(); $('#lbx-c').focus(); });
  dlg.addEventListener('close', () => { if (dlg.returnValue === 'ok' && $('#lbx-c').value.trim()) { const t = $('#lbx-c').value.trim(); $('#lbx-c').value = ''; generate(t, null); } });
  $('[data-fix]').addEventListener('click', () => {
    const f = S.checks.filter((c) => c.estado === 'no').map((c) => c.k + ': ' + (c.items || []).filter((x) => x.ok === false).map((x) => x.e + ' (' + x.v + ', se espera ' + x.x + ')').join('; '));
    generate('Corrija solo estos incumplimientos y no cambie nada más: ' + f.join(' · '), $('[data-cost-fix]'));
  });
  $('[data-cc]').addEventListener('click', async () => {
    const pedido = $('#lbx-q').value.trim() || '(describa aquí lo que necesita)', datos = $('#lbx-d').value.trim();
    const t = `Construye un experimento para el Laboratorio de Interfaces de Keyons (sistema-diseno/laboratorio.html).
Pedido: ${pedido}${datos ? '\nDatos de ejemplo: ' + datos : ''}
Usa solo el kit css/laboratorio-kit.css (clases lx-* y variables --lab-*), con las plantillas de js/laboratorio-plantillas.js como referencia, y las reglas de ia/libro-de-marca.md e ia/tokens.json.
Guárdalo como _lab/experimentos/<nombre>.json con los campos id, titulo, estado («En exploración»), kit («${KIT}»), pedido, origen («claude-code»), html (solo el contenido del body), css, js y ex ({}).
Es una exploración, no un producto final.`;
    try { await navigator.clipboard.writeText(t); msg('Pedido copiado. Péguelo en Claude Code; el diseño aparecerá en «Abrir un diseño guardado».'); } catch (e) { msg('No se pudo copiar el pedido.', true); }
  });

  /* ── Guardar ── */
  $('[data-estado]').addEventListener('change', (e) => { S.estado = e.target.value; autosave(); });
  async function save(estado) {
    if (!S.server) { msg('Guardar en el proyecto necesita el servidor local. El borrador queda en este navegador.', true); autosave(); return null; }
    if (estado) { S.estado = estado; $('[data-estado]').value = estado; }
    try {
      const r = await api('guardar', { id: S.id, titulo: S.titulo, estado: S.estado, kit: KIT, pedido: S.pedido, datos: S.datos, origen: S.origen, html: S.html, css: S.css, js: S.js, ex: S.ex, revision: S.revision || {} });
      S.id = r.id; msg('Guardado en _lab/experimentos/' + r.id + '.json.'); return r.id;
    } catch (e) { msg('No se pudo guardar: ' + e.message, true); return null; }
  }
  $('[data-draft]').addEventListener('click', () => save(''));
  $('[data-save]').addEventListener('click', () => save(''));
  $('[data-send]').addEventListener('click', async () => {
    const id = await save('Enviado a revisión'); if (!id) return;
    try { await api('proponer', { id }); msg('Enviado a revisión: copiado a sistema-diseno/laboratorio/propuestas/. Se publica con el próximo envío a main.'); } catch (e) { msg('No se pudo enviar: ' + e.message, true); }
  });

  /* ── Sugerir normas ── */
  const notes = $('[data-notes]');
  const offList = () => compute().off.concat(S.checks.filter((c) => c.estado === 'rec' || c.estado === 'no').map((c) => c.k + ': ' + EST[c.estado][0]));
  $('[data-normas]').addEventListener('click', async () => {
    const fuera = offList(); let md, file = '';
    if (S.server) {
      if (S.server.modo !== 'demo' && !confirm('Sugerir normas usa la API (cuesta como una construcción pequeña). ¿Continuar?')) return;
      try { const r = await api('normas', { titulo: S.titulo, fuera, html: S.html, css: S.css }); md = r.markdown; file = r.archivo; } catch (e) { msg('No se pudo sugerir: ' + e.message, true); return; }
    } else md = `# Notas para el libro · ${S.titulo}\n\n## Lo que se aparta de las normas\n\n${fuera.map((x) => '- ' + x).join('\n') || '- Nada: el diseño está dentro de norma.'}\n`;
    notes.hidden = false; notes.querySelector('[data-notes-md]').textContent = md;
    notes.querySelector('[data-notes-file]').textContent = file ? 'Guardado en ' + file : 'Sin la API: solo la lista de lo que sale de las normas.';
  });
  notes.querySelector('[data-notes-copy]').addEventListener('click', () => navigator.clipboard.writeText(notes.querySelector('[data-notes-md]').textContent).then(() => msg('Notas copiadas.')));
  notes.querySelector('[data-notes-dl]').addEventListener('click', () => { const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([notes.querySelector('[data-notes-md]').textContent], { type: 'text/markdown' })); a.download = 'notas-' + (slugify(S.titulo) || 'experimento') + '.md'; a.click(); });

  /* ── Abrir guardados, con miniaturas ── */
  const thumb = (x) => `<span class="lbx__th"><iframe sandbox="" tabindex="-1" aria-hidden="true" srcdoc="${esc(doc(x.html || '', x.css || '', ''))}"></iframe></span>`;
  async function listSaved() {
    const box = $('[data-saved]');
    let exps = [], propsL = [];
    if (S.server) { try { const r = await api('lista'); exps = r.experimentos || []; propsL = r.propuestas || []; } catch (e) { /* sigue */ } }
    else { try { propsL = (await fetch(ROOT + 'sistema-diseno/laboratorio/propuestas/index.json').then((r) => r.json())).propuestas || []; } catch (e) { /* sin propuestas */ } }
    const item = (x, kind) => `<li><button type="button" class="lbx__sv" data-open="${esc(x.id)}" data-kind="${kind}"><span class="lbx__th" data-th></span><b>${esc(x.titulo)}</b><span>${esc(x.estado || 'Enviado a revisión')} · ${esc((x.actualizado || '').slice(0, 10))}</span></button></li>`;
    box.innerHTML = (S.server ? `<p class="lbx__k">Borradores</p>${exps.length ? `<ul class="lbx__svl">${exps.map((x) => item(x, 'exp')).join('')}</ul>` : '<p class="lbx__p">Todavía no hay borradores guardados.</p>'}` : '<p class="lbx__p">Los borradores se guardan con el servidor local. Aquí se ven los enviados a revisión.</p>')
      + `<p class="lbx__k">Enviados a revisión</p>${propsL.length ? `<ul class="lbx__svl">${propsL.map((x) => item(x, 'prop')).join('')}</ul>` : '<p class="lbx__p">Ninguno todavía.</p>'}`;
    const full = (x, kind) => (kind === 'exp' ? api('experimento?id=' + encodeURIComponent(x.id)) : fetch(ROOT + 'sistema-diseno/laboratorio/propuestas/' + encodeURIComponent(x.id) + '.json').then((r) => r.json()));
    for (const [list, kind] of [[exps, 'exp'], [propsL, 'prop']]) for (const x of list.slice(0, 12)) {
      try { const f = await full(x, kind); const th = box.querySelector(`[data-kind="${kind}"][data-open="${CSS.escape(x.id)}"] [data-th]`); if (th) th.outerHTML = thumb(f); } catch (e) { /* sin miniatura */ }
    }
  }
  app.addEventListener('click', async (e) => {
    const o = e.target.closest('[data-open]'); if (!o) return;
    try {
      const x = o.dataset.kind === 'exp' ? await api('experimento?id=' + encodeURIComponent(o.dataset.open)) : await fetch(ROOT + 'sistema-diseno/laboratorio/propuestas/' + encodeURIComponent(o.dataset.open) + '.json').then((r) => r.json());
      if (S.html && !same(snap(), hist[hist.length - 1]) && !confirm('Hay cambios sin registrar en el lienzo. ¿Abrir de todas formas?')) return;
      S.id = o.dataset.kind === 'exp' ? x.id : ''; S.pedido = x.pedido || ''; S.datos = x.datos || ''; S.estado = x.estado || 'En exploración'; S.revision = x.revision || {};
      load({ html: x.html, css: x.css, js: x.js, titulo: x.titulo, origen: x.origen, ex: x.ex || {} });
      closePanel(); setStage('disenar');
      msg('Abierto: ' + x.titulo + '.' + (x.kit && x.kit !== KIT ? ' Se hizo con una versión anterior de las piezas del laboratorio: puede verse distinto a como se guardó.' : ''));
    } catch (err) { msg('No se pudo abrir: ' + err.message, true); }
  });

  /* ── Móvil: solo consulta ── */
  const mq = matchMedia('(max-width: 767px)');
  const consulta = () => { document.body.classList.toggle('lbx-consulta', mq.matches); if (mq.matches) { S.edit = false; openPanel('abrir', 'Diseños guardados'); } };
  mq.addEventListener('change', consulta);

  /* ── Inicio: el lienzo primero, con los paneles cerrados ── */
  Object.assign(S, { estado: 'En exploración', edit: true, snap: true, split: false, stage: 'elegir', zoom: 'fit', guia: '', revision: {} });
  histUI(); renderManual();
  loadRes().then(() => { pick('dashboard'); setStage('elegir'); fit(); detect(); consulta(); offerRecover(); });
})();
