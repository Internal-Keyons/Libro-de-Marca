/* ════════════════════════════════════════════════════════════════════
   Recursos técnicos (KYN-MRK-TEC-001) · catálogo de la expresión visual Keyons

   Una sola fuente: la demostración, el código que se copia y los archivos que se
   descargan salen de los mismos archivos que usa el libro.
   - Módulos JS (js/keyons-cielo.js, js/keyons-rafaga.js): se leen y se entregan tal cual.
   - Funciones del libro (trama, nubes, aparecer, girar): window.KeyonsEfectos, de js/libro.js.
   - CSS: las reglas se extraen de css/libro.css por selector, en el orden de la cascada.
   - Tokens: las variables se extraen de css/tokens.css y css/libro.css, con sus dependencias.
   Los datos de cada recurso (textos, parámetros, selectores) viven en data/recursos-tecnicos.json.
   ════════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  const box = document.querySelector('[data-rtec]');
  if (!box) return;
  const ROOT = (document.body.dataset.root || '.') + '/';
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const cache = {};
  const get = (p) => cache[p] || (cache[p] = fetch(ROOT + p).then((r) => { if (!r.ok) throw new Error(p); return r.text(); }));

  /* ─── Lectura de CSS: reglas, animaciones y variables del :root ─── */
  const strip = (s) => s.replace(/\/\*[\s\S]*?\*\//g, '');
  function closeAt(s, i) {
    let d = 0, q = '';
    for (; i < s.length; i++) {
      const c = s[i];
      if (q) { if (c === '\\') i++; else if (c === q) q = ''; continue; }
      if (c === '"' || c === "'") q = c;
      else if (c === '{') d++;
      else if (c === '}' && --d === 0) return i;
    }
    return s.length;
  }
  function splitTop(s, ch) {
    const out = []; let d = 0, q = '', cur = '';
    for (let i = 0; i < s.length; i++) {
      const c = s[i];
      if (q) { cur += c; if (c === '\\') { cur += s[++i] || ''; } else if (c === q) q = ''; continue; }
      if (c === '"' || c === "'") q = c;
      else if (c === '(') d++;
      else if (c === ')') d--;
      else if (c === ch && d === 0) { out.push(cur); cur = ''; continue; }
      cur += c;
    }
    if (cur.trim()) out.push(cur);
    return out;
  }
  const decls = (body) => splitTop(body, ';').map((x) => { const k = x.indexOf(':'); return k < 0 ? null : [x.slice(0, k).trim(), x.slice(k + 1).trim().replace(/\s+/g, ' ')]; }).filter(Boolean);
  function parse(s, file, media = [], out = { rules: [], kf: {}, root: {} }) {
    let i = 0;
    while (i < s.length) {
      const b = s.indexOf('{', i), sc = s.indexOf(';', i);
      if (b < 0) break;
      if (sc >= 0 && sc < b && s.slice(i, sc).trim().startsWith('@')) { i = sc + 1; continue; }
      const pre = s.slice(i, b).trim().replace(/\s+/g, ' '), e = closeAt(s, b), body = s.slice(b + 1, e);
      if (/^@(media|supports)/.test(pre)) parse(body, file, media.concat(pre), out);
      else if (/^@(-webkit-)?keyframes /.test(pre)) { if (!media.length) out.kf[pre.split(' ')[1]] = body; }
      else if (pre && !pre.startsWith('@')) {
        out.rules.push({ sel: pre, body, media });
        if (pre === ':root' && !media.length) decls(body).forEach(([k, v]) => { if (k.startsWith('--')) out.root[k] = { v, file }; });
      }
      i = e + 1;
    }
    return out;
  }
  const norm = (s) => s.trim().replace(/\s+/g, ' ').replace(/\s*>\s*/g, ' > ');
  const pad = (n) => ' '.repeat(n);
  const rule = (sel, body, ind) => `${pad(ind)}${sel} {\n${decls(body).map(([k, v]) => `${pad(ind + 2)}${k}: ${v};`).join('\n')}\n${pad(ind)}}`;
  /* Reglas del recurso consolidadas: cada selector aparece una vez con el valor final que el libro aplica
     (las rondas posteriores ajustan reglas anteriores; aquí se resuelve esa cascada). Las de @media conservan su condición. */
  function extract(P, want) {
    const W = new Set(want.map(norm)), groups = new Map();
    P.rules.forEach((r) => {
      const keep = splitTop(r.sel, ',').map(norm).filter((x) => W.has(x));
      if (!keep.length) return;
      const mk = r.media.join('|');
      if (!groups.has(mk)) groups.set(mk, { media: r.media, sels: new Map() });
      const g = groups.get(mk);
      keep.forEach((sel) => {
        if (!g.sels.has(sel)) g.sels.set(sel, new Map());
        const m = g.sels.get(sel);
        decls(r.body).forEach(([k, v]) => {
          const prev = m.get(k);
          if (prev && /!important$/.test(prev) && !/!important$/.test(v)) return;
          m.delete(k); m.set(k, v);   // la última declaración queda al final, como en la cascada
        });
      });
    });
    return [...groups.values()].map((g) => {
      const ind = g.media.length * 2;
      let s = [...g.sels].map(([sel, m]) => `${pad(ind)}${sel} {\n${[...m].map(([k, v]) => `${pad(ind + 2)}${k}: ${v};`).join('\n')}\n${pad(ind)}}`).join('\n');
      for (let k = g.media.length - 1; k >= 0; k--) s = `${pad(k * 2)}${g.media[k]} {\n${s}\n${pad(k * 2)}}`;
      return s;
    }).join('\n');
  }
  function keyframes(P, name) {
    const body = P.kf[name];
    if (!body) return '';
    const inner = parse(body, '').rules.map((r) => rule(r.sel, r.body, 2)).join('\n');
    return `@keyframes ${name} {\n${inner}\n}`;
  }
  /* Variables que usa el código, con las variables de las que dependen */
  function tokens(ROOTV, text, extra) {
    const seen = [], want = (extra || []).slice();
    (text.match(/var\(--[\w-]+/g) || []).forEach((m) => want.push(m.slice(4)));
    while (want.length) {
      const k = want.shift();
      if (seen.includes(k) || !ROOTV[k]) continue;
      seen.push(k);
      (ROOTV[k].v.match(/var\(--[\w-]+/g) || []).forEach((m) => want.push(m.slice(4)));
    }
    return seen;
  }
  function rootBlock(ROOTV, names) {
    if (!names.length) return '';
    const val = (v) => (v.length > 90 ? '\n    ' + splitTop(v, ',').map((x) => x.trim()).join(',\n    ') : v);
    return `:root {\n${names.map((k) => `  ${k}: ${val(ROOTV[k].v)};`).join('\n')}\n}`;
  }

  /* ─── Configuración leída del propio módulo: DEFAULTS con sus comentarios ─── */
  function defaults(src, notas) {
    const a = src.indexOf('var DEFAULTS = {');
    if (a < 0) return [];
    const b = src.indexOf('};', a), rows = [];
    let grp = '';
    src.slice(a, b).split('\n').slice(1).forEach((ln) => {
      const g = ln.match(/^\s+(\w+):\s*\{/);
      if (g) { grp = g[1] + '.'; return; }
      if (/^\s+\},?/.test(ln)) { grp = ''; return; }
      const m = ln.match(/^\s+(\w+):\s*(.+?),?\s*(?:\/\/\s*(.+))?$/);
      if (m) rows.push([grp + m[1], m[2].replace(/,$/, ''), (notas || {})[grp + m[1]] || m[3] || '']);
    });
    return rows;
  }

  const ICON = {
    plus: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 3v10M3 8h10"/></svg>',
    down: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2.5v8M4.5 7 8 10.5 11.5 7M3 13.5h10"/></svg>',
    open: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M9 3h4v4M13 3 7.5 8.5M11 9.5V13H3V5h3.5"/></svg>',
    redo: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M12.5 4.5v3h-3M12.3 7.5A4.8 4.8 0 1 0 12 10"/></svg>'
  };

  Promise.all([get('data/recursos-tecnicos.json'), get('css/tokens.css'), get('css/libro.css')]).then(([j, tk, lb]) => {
    const D = JSON.parse(j);
    const T = parse(strip(tk), 'css/tokens.css'), L = parse(strip(lb), 'css/libro.css');
    const ROOTV = Object.assign({}, T.root, L.root);
    const R = D.recursos, CAT = {};
    D.categorias.forEach((c) => { CAT[c.k] = c.t; });
    const normas = () => new Promise((res) => {
      if (window.KEYONS_NORMAS) return res(window.KEYONS_NORMAS);
      let n = 0; const t = setInterval(() => { if (window.KEYONS_NORMAS || ++n > 80) { clearInterval(t); res(window.KEYONS_NORMAS || []); } }, 50);
    });

    /* Filtro por categoría y lista */
    const count = (k) => R.filter((r) => !k || r.cat === k).length;
    box.innerHTML = `
      <div class="rtec__bar" role="group" aria-label="Filtrar por categoría">
        <button type="button" data-rcat="" aria-pressed="true">Todas <span>${count('')}</span></button>
        ${D.categorias.map((c) => `<button type="button" data-rcat="${c.k}" aria-pressed="false">${esc(c.t)} <span>${count(c.k)}</span></button>`).join('')}
      </div>
      <ol class="rtec__list">${R.map((r, i) => `
        <li class="rtec__i" data-cat="${r.cat}" id="rtec-${r.id}">
          <button class="rtec__h" type="button" aria-expanded="false" aria-controls="rtec-b-${r.id}">
            <span class="rtec__n">${String(i + 1).padStart(2, '0')}</span>
            <span class="rtec__tt"><b>${esc(r.t)}</b><small>${esc(r.d)}</small></span>
            <span class="rtec__c">${esc(CAT[r.cat])}</span>
            <span class="rtec__pl">${ICON.plus}</span>
          </button>
          <div class="rtec__b" id="rtec-b-${r.id}" hidden></div>
        </li>`).join('')}
      </ol>`;
    box.querySelectorAll('[data-rcat]').forEach((b) => b.addEventListener('click', () => {
      box.querySelectorAll('[data-rcat]').forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
      box.querySelectorAll('.rtec__i').forEach((li) => { li.hidden = !!b.dataset.rcat && li.dataset.cat !== b.dataset.rcat; });
    }));

    /* Partes de un recurso para una variante: HTML, CSS, JS y el ejemplo completo */
    async function parts(r, v, from) {
      const sub = (s) => (s || '').split('{{v}}').join(v);
      const html = from ? from[v].html : sub(r.html);
      const glue = sub(r.demo);
      let rules = r.css ? extract(L, r.css.sel) : '';
      if (r.css && r.css.kf) rules += '\n\n' + r.css.kf.map((k) => keyframes(L, k)).filter(Boolean).join('\n\n');
      const base = extract(L, ['*', 'button']);
      const vars = tokens(ROOTV, base + rules + glue + html, r.vars);
      const css = [vars.length ? `/* Tokens Keyons · css/tokens.css y css/libro.css */\n${rootBlock(ROOTV, vars)}` : '', `/* Base del libro · css/libro.css */\n${base}`, rules ? `/* ${esc(r.t)} · css/libro.css, con el valor final de cada propiedad */\n${rules}` : ''].filter(Boolean).join('\n\n');
      let js = '', src = '';
      if (r.js && r.js.file) { src = await get(r.js.file); js = src; }
      else if (r.js && r.js.fn) {
        const f = (window.KeyonsEfectos || {})[r.js.fn];
        js = f ? `/* ${r.js.fn}() · js/libro.js */\nconst ${r.js.fn} = ${f.toString()};` : '';
      }
      if (r.init) js += `\n\n/* Llamada */\n${sub(r.init)}`;
      const doc = `<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Keyons · ${esc(r.t)}</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
${css}

/* Solo para este ejemplo */
${glue}
</style>
</head>
<body>
${html}
${js ? `<script>\n${js.replace(/<\/script/gi, '<\\/script')}\n</script>\n` : ''}</body>
</html>
`;
      return { html, css, js: js.trim(), doc, vars, src };
    }

    const save = (name, text, type) => {
      const a = document.createElement('a');
      a.href = URL.createObjectURL(new Blob([text], { type }));
      a.download = name; document.body.appendChild(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(a.href), 2000);
    };

    async function open(li, r) {
      const b = li.querySelector('.rtec__b');
      let from = null, ops = r.variantes ? r.variantes.op : null, v = r.variantes ? r.variantes.def : '';
      if (r.htmlFrom) {
        const page = new DOMParser().parseFromString(await get(r.htmlFrom.page), 'text/html');
        from = [...page.querySelectorAll(r.htmlFrom.sel)].map((f) => {
          const n = f.querySelector(r.htmlFrom.name);
          return { html: f.outerHTML, t: n ? n.firstChild.textContent.trim() : '' };
        });
        ops = from.map((f, i) => [String(i), f.t]); v = '0';
      }
      const N = await normas(), byId = {};
      N.forEach((o) => { byId[o.id] = o; });
      const P0 = await parts(r, v, from);
      const cfg = r.config === 'defaults' ? defaults(P0.src, r.configNotas) : r.config;
      const files = [r.js && r.js.file ? `<a href="${ROOT}${r.js.file}">${r.js.file}</a>` : '', r.js && r.js.fn ? `Función ${r.js.fn}() de js/libro.js` : '', r.css ? 'Reglas de css/libro.css' : '', P0.vars.length ? 'Variables de css/tokens.css y css/libro.css' : ''].filter(Boolean);
      b.innerHTML = `
        <div class="rtec__demo">
          <div class="rtec__stage"><iframe sandbox="allow-scripts" title="Demostración: ${esc(r.t)}"></iframe></div>
          <div class="rtec__ctl">
            ${ops ? `<div class="rtec__var" role="group" aria-label="${esc(r.variantes.t)}"><span class="paren">(${esc(r.variantes.t)})</span>${ops.map(([k, t]) => `<button type="button" data-rv="${k}" aria-pressed="${k === v}">${esc(t)}</button>`).join('')}</div>` : ''}
            <span class="rtec__sp"></span>
            <button class="rtec__a" type="button" data-rre>${ICON.redo}Reiniciar</button>
            <button class="rtec__a" type="button" data-rop>${ICON.open}Abrir aparte</button>
          </div>
        </div>
        <div class="code rtec__code">
          <div class="code__bar">
            <div class="rtec__tabs" role="tablist" aria-label="Código">
              ${[['html', 'HTML'], ['css', 'CSS'], ['js', 'JS'], ['doc', 'Ejemplo completo']].map(([k, t]) => `<button type="button" role="tab" data-rtab="${k}" aria-selected="${k === 'html'}">${t}</button>`).join('')}
            </div>
            <button class="code__copy" type="button" data-copy-msg="Código copiado">Copiar</button>
          </div>
          <pre tabindex="0"><code></code></pre>
        </div>
        <div class="rtec__dl"><span class="paren">(Descargar)</span>
          <button type="button" data-rdl="doc">${ICON.down}Ejemplo completo · HTML</button>
          ${r.css || P0.vars.length ? `<button type="button" data-rdl="css">${ICON.down}CSS</button>` : ''}
          ${r.js && r.js.file ? `<a href="${ROOT}${r.js.file}" download>${ICON.down}${r.js.file.split('/').pop()}</a>` : r.js ? `<button type="button" data-rdl="js">${ICON.down}JS</button>` : ''}
        </div>
        <dl class="rtec__spec">
          <div><dt>Configuración</dt><dd><div class="rtec__cfg">${cfg.map(([k, val, d]) => `<p><code>${esc(k)}</code><code>${esc(val)}</code><span>${esc(d)}</span></p>`).join('')}</div></dd></div>
          <div><dt>Dependencias</dt><dd class="rtec__kv">
            <p><b>Archivos</b><span>${files.join('<br>')}</span></p>
            ${P0.vars.length ? `<p><b>Tokens</b><span class="rtec__tok">${P0.vars.map((k) => `<code>${k}</code>`).join(' ')}</span></p>` : ''}
            ${P0.vars.includes('--font-sans') || /font-family:var\(--font-sans/.test(r.demo || '') ? '<p><b>Fuente</b><span>Plus Jakarta Sans, de Google Fonts</span></p>' : ''}
            ${r.js && r.js.file ? '<p><b>Navegador</b><span>WebGL 1; sin WebGL, el recurso muestra su versión fija</span></p>' : ''}
          </dd></div>
          <div><dt>Implementación</dt><dd><ol class="rtec__steps">${r.impl.map((s) => `<li>${esc(s)}</li>`).join('')}</ol></dd></div>
          <div><dt>Compatibilidad</dt><dd class="rtec__kv">${r.compat.map(([k, d]) => `<p><b>${esc(k)}</b><span>${esc(d)}</span></p>`).join('')}</dd></div>
          <div><dt>Referencia</dt><dd class="rtec__kv">
            <p><b>Normas</b><span>${r.normas.length ? r.normas.map((id) => byId[id] ? `<a href="${ROOT}${byId[id].h}">${id}</a> ${esc(byId[id].t)}` : id).join('<br>') : esc(r.nota || '')}</span></p>
            <p><b>Fuente</b><span>${files.join('<br>')}</span></p>
            <p><b>Versión</b><span>${esc(r.v)} · catálogo ${esc(D.version)}, ${esc(D.fecha)}</span></p>
          </dd></div>
        </dl>`;
      const frame = b.querySelector('iframe'), pre = b.querySelector('pre code'), cp = b.querySelector('.code__copy');
      let P = P0, tab = 'html';
      const show = () => {
        pre.textContent = P[tab] || '// Este recurso no necesita ' + tab.toUpperCase();
        cp.dataset.copy = P[tab] || '';
      };
      const paint = () => { frame.srcdoc = P.doc; show(); };
      paint();
      /* Recursos que dependen del ancho: el ejemplo se dibuja a su ancho real y se escala al escenario.
         En un teléfono se muestra a su tamaño, como lo vería ahí. */
      if (r.ancho && 'ResizeObserver' in window) {
        const st = b.querySelector('.rtec__stage');
        const fit = () => { const k = st.clientWidth / r.ancho; if (st.clientWidth < 600) { frame.style.cssText = ''; return; } frame.style.cssText = `position:absolute;left:0;top:0;width:${r.ancho}px;height:${st.clientHeight / k}px;transform:scale(${k});transform-origin:0 0`; };
        new ResizeObserver(fit).observe(st); fit();
      }
      b.querySelectorAll('[data-rtab]').forEach((t) => t.addEventListener('click', () => {
        tab = t.dataset.rtab;
        b.querySelectorAll('[data-rtab]').forEach((x) => x.setAttribute('aria-selected', String(x === t)));
        show();
      }));
      b.querySelectorAll('[data-rv]').forEach((x) => x.addEventListener('click', async () => {
        v = x.dataset.rv;
        b.querySelectorAll('[data-rv]').forEach((y) => y.setAttribute('aria-pressed', String(y === x)));
        P = await parts(r, v, from); paint();
      }));
      b.querySelector('[data-rre]').addEventListener('click', () => { frame.srcdoc = ''; requestAnimationFrame(() => { frame.srcdoc = P.doc; }); });
      b.querySelector('[data-rop]').addEventListener('click', () => {
        const u = URL.createObjectURL(new Blob([P.doc], { type: 'text/html' }));
        window.open(u, '_blank', 'noopener'); setTimeout(() => URL.revokeObjectURL(u), 60000);
      });
      b.querySelectorAll('[data-rdl]').forEach((x) => x.addEventListener('click', () => {
        const k = x.dataset.rdl;
        if (k === 'doc') save(`keyons-${r.id}.html`, P.doc, 'text/html');
        if (k === 'css') save(`keyons-${r.id}.css`, P.css + '\n', 'text/css');
        if (k === 'js') save(`keyons-${r.id}.js`, P.js + '\n', 'text/javascript');
      }));
    }

    /* Una fila abierta a la vez: al cerrarla, su demostración se retira y deja de consumir */
    const close = (li) => {
      li.classList.remove('is-open');
      li.querySelector('.rtec__h').setAttribute('aria-expanded', 'false');
      const b = li.querySelector('.rtec__b'); b.hidden = true; b.innerHTML = '';
    };
    box.querySelectorAll('.rtec__i').forEach((li, i) => {
      const h = li.querySelector('.rtec__h');
      h.addEventListener('click', () => {
        const on = h.getAttribute('aria-expanded') !== 'true';
        box.querySelectorAll('.rtec__i.is-open').forEach(close);
        if (!on) return;
        li.classList.add('is-open'); h.setAttribute('aria-expanded', 'true');
        li.querySelector('.rtec__b').hidden = false;
        open(li, R[i]).catch(() => { li.querySelector('.rtec__b').innerHTML = '<p class="rtec__err">No se pudo cargar el recurso. Abra la página desde el servidor del libro.</p>'; });
      });
    });
    const deep = location.hash.match(/^#rtec-([\w-]+)$/);
    if (deep) { const li = document.getElementById('rtec-' + deep[1]); if (li) li.querySelector('.rtec__h').click(); }
  }).catch(() => { box.innerHTML = '<p class="rtec__err">No se pudo cargar el catálogo. Abra la página desde el servidor del libro.</p>'; });
})();
