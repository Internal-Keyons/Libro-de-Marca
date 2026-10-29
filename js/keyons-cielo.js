/*! Keyons · Cielo con Ráfaga · v1.1 · 2026-10-10
 *
 * Uso:
 *   <header class="hero"> …contenido… </header>
 *   1. Cargar este archivo (o pegar este código dentro de una etiqueta script).
 *   2. Llamar: KeyonsCielo.mount(document.querySelector('.hero'), { sky: 'mediodia' });
 *
 * - El header queda con position:relative y el lienzo va detrás del contenido (z-index 0).
 *   El contenido del header necesita position:relative y z-index:1 para quedar encima.
 * - Cielos: 'amanecer' | 'mediodia' | 'atardecer' | 'noche' | 'galaxia'.
 * - REGLA: no reescribir el shader ni el campo de ráfaga. Solo se cambia la configuración
 *   que se pasa a mount(). Cada número tiene sentido únicamente dentro de este algoritmo.
 */
(function (global) {
  'use strict';

  // ===== Tokens de cielo (idénticos a la especificación) =====
  var SKIES = {
    amanecer:  { ws: .8,  stops: [['#729BDD', 0], ['#B2BFE5', .34], ['#FED8B5', .64], ['#FFCE86', .84], ['#FFEBB1', 1]],
                 glow: ['#FFEBB1', .68, .02, .5, .65], band: ['#E99D9E', .52, .09, .22],
                 clouds: { lit: '#FFEBB1', low: '#E99D9E', high: '#B2BFE5', cover: .52, alpha: .72, stretch: .42, add: 0 },
                 stars: [0, '#FFF8E7', '#FFF8E7'], grain: .045 },
    mediodia:  { ws: 1,   stops: [['#3D6BAF', 0], ['#729BDD', .32], ['#8FB4DC', .58], ['#9EBADD', .76], ['#C4DBF0', 1]],
                 glow: ['#CCD6E5', .85, 1.05, .55, .35], band: ['#CCD6E5', .5, .1, 0],
                 clouds: { lit: '#FFFFFF', low: '#9EBADD', high: '#CCD6E5', cover: .56, alpha: .85, stretch: .42, add: 0 },
                 stars: [0, '#FFF8E7', '#FFF8E7'], grain: .04 },
    atardecer: { ws: .8,  stops: [['#3D6BAF', 0], ['#7D81B9', .26], ['#D182AB', .5], ['#E99D9E', .66], ['#E87838', .84], ['#F5A742', 1]],
                 glow: ['#F5A742', .3, 0, .45, .6], band: ['#C4658B', .44, .08, .2],
                 clouds: { lit: '#F5A742', low: '#CE635D', high: '#7D81B9', cover: .5, alpha: .75, stretch: .38, add: 0 },
                 stars: [0, '#FFF8E7', '#FFF8E7'], grain: .045 },
    noche:     { ws: .6,  stops: [['#10122A', 0], ['#17234F', .45], ['#2C3C78', .8], ['#2D4775', 1]],
                 glow: ['#3E547F', .8, .82, .32, .55], band: ['#3E4A7C', .5, .1, 0],
                 clouds: { lit: '#3E547F', low: '#17234F', high: '#3E4A7C', cover: .5, alpha: .6, stretch: .36, add: 0 },
                 stars: [0, '#FFF8E7', '#FFF8E7'], grain: .05 },
    galaxia:   { ws: .25, stops: [['#10122A', 0], ['#1E2A5C', .55], ['#2D4775', 1]],
                 glow: ['#8B3A47', .28, .62, .42, .55], band: ['#5C4B7E', .7, .18, .3],
                 clouds: { lit: '#E99D9E', low: '#6B2E5C', high: '#5C4B7E', cover: .58, alpha: .6, stretch: 1, add: 1 },
                 stars: [.6, '#FFF8E7', '#E8D4B0'], grain: .05 }
  };

  // ===== Configuración (lo único que se ajusta) =====
  var DEFAULTS = {
    sky: 'mediodia',
    seed: 'keyons',        // cada texto genera una disposición distinta de nubes
    hover: 'rafaga',       // 'rafaga' | 'none'
    cloudScale: 2.4,       // tamaño de las nubes respecto al alto: más alto = nubes más pequeñas
    rise: .12,             // el viento sube 12 % de lo que avanza
    maxDPR: 1.5,           // tope de resolución para rendimiento
    rafaga: {
      sigma2: .012,        // alcance: gaussiana de ~11 % del alto alrededor del cursor
      gain: .55,           // fuerza: fracción de la velocidad del gesto que se transfiere
      max: .24,            // desplazamiento máximo (fracción del alto)
      friction: 4.2,       // segundos de la constante de fricción (se calma en 3–5 s)
      minSpeed: .02,       // por debajo de esta velocidad no empuja
      maxSpeed: 3,         // tope de velocidad del gesto
      smoothing: .4,       // suavizado de la velocidad del cursor (0–1)
      idleDecay: 10        // qué tan rápido muere la velocidad cuando el cursor se detiene
    },
    gridRows: 32           // resolución del campo de ráfaga (columnas = filas × proporción)
  };

  var VS = 'attribute vec2 a;void main(){gl_Position=vec4(a,0.,1.);}';
  var FS = [
    '#ifdef GL_FRAGMENT_PRECISION_HIGH', 'precision highp float;', '#else', 'precision mediump float;', '#endif',
    'uniform vec2 R,SEED,GLP;uniform float ASP,TD,NS,GLR,GLI,BDP,BDW,BDI,COV,CLA,STR,CLADD,STARS,GR,DRIFT,RISE,SCALE;',
    'uniform vec3 ST[6];uniform float SP[6];uniform vec3 GLC,BDC,CLL,CLS,CLS2,STC,STC2;uniform sampler2D OFF;',
    // ruido de valor + fbm de 5 octavas con rotación
    'float h(vec2 p){p=fract(p*vec2(123.34,456.21));p+=dot(p,p+45.32);return fract(p.x*p.y);}',
    'float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}',
    'float fbm(vec2 p){float v=0.,a=.5;mat2 r=mat2(.8,.6,-.6,.8);for(int i=0;i<5;i++){v+=a*n(p);p=r*p*2.03+11.7;a*=.5;}return v;}',
    'vec3 grad(float t){vec3 c=ST[0];for(int i=1;i<6;i++){if(float(i)<NS){c=mix(c,ST[i],smoothstep(SP[i-1],SP[i],t));}}return c;}',
    'void main(){',
    ' vec2 uv=gl_FragCoord.xy/R;',                                   // 0–1, y hacia arriba
    ' vec2 sp=vec2(uv.x*ASP,uv.y);',                                // espacio con proporción real
    ' vec2 o=(texture2D(OFF,uv).xy-.5)*.5;o.x*=ASP;',               // desplazamiento de ráfaga
    ' vec2 cp=sp-o;',                                               // SOLO las nubes se desplazan
    ' vec2 cc=vec2((cp.x-DRIFT)*STR,cp.y-DRIFT*RISE)*SCALE+SEED;',  // coordenada de nube + viento
    ' float base=fbm(cc),det=fbm(cc*2.7+3.1);',
    ' float v=base*.78+det*.32;',                                   // densidad bruta
    ' float t=clamp(1.-uv.y+(base-.5)*.05,0.,1.);',                 // 0 arriba, 1 abajo
    ' vec3 col=grad(t);',
    ' float d=length((uv-GLP)*vec2(ASP,1.));col=mix(col,GLC,GLI*exp(-d*d/(GLR*GLR)));',
    ' col=mix(col,BDC,BDI*exp(-pow((t-BDP)/max(BDW,.001),2.)));',
    ' if(STARS>0.){vec2 g=sp*R.y/2.5;vec2 id=floor(g);float r=h(id+SEED);float s=step(1.-STARS*.03,r);',
    '   float tw=.65+.35*sin(TD*1.3+r*40.);col+=mix(STC,STC2,fract(r*13.))*s*smoothstep(.45,0.,length(fract(g)-.5))*tw*(.4+r*.6);}',
    ' float th=mix(.78,.42,COV);float dens=smoothstep(th,th+.28,v);',
    ' vec2 ld=normalize((GLP-uv)*vec2(ASP,1.)+1e-4);',
    ' float v2=fbm(cc+vec2(ld.x*STR,ld.y)*.25)*.78+det*.32;',        // un paso hacia la luz
    ' float lit=clamp((v-v2)*4.+.55,0.,1.);',
    ' vec3 shc=mix(CLS,CLS2,smoothstep(.15,.95,uv.y));vec3 ccol=mix(shc,CLL,lit);',
    ' float al=dens*CLA;',
    ' if(CLADD>.5)col+=ccol*al*.7;else col=mix(col,ccol,al);',
    ' col+=(h(gl_FragCoord.xy*.73+SEED)-.5)*GR;',                    // grano fijo, no animado
    ' gl_FragColor=vec4(col,1.);',
    '}'
  ].join('\n');

  function hex(h) { return [1, 3, 5].map(function (i) { return parseInt(h.slice(i, i + 2), 16) / 255; }); }
  function seedOf(s) { var x = 2166136261; for (var i = 0; i < s.length; i++) { x ^= s.charCodeAt(i); x = Math.imul(x, 16777619); } x >>>= 0; return [(x % 9973) / 97.3, ((x / 9973 | 0) % 9967) / 97.1]; }
  function merge(a, b) { var o = {}, k; for (k in a) o[k] = a[k]; for (k in b || {}) o[k] = (a[k] && typeof a[k] === 'object' && !Array.isArray(a[k])) ? merge(a[k], b[k]) : b[k]; return o; }

  function mount(el, options) {
    var cfg = merge(DEFAULTS, options);
    var reduce = global.matchMedia ? global.matchMedia('(prefers-reduced-motion: reduce)') : { matches: false };
    if (getComputedStyle(el).position === 'static') el.style.position = 'relative';
    var cv = document.createElement('canvas');
    cv.setAttribute('aria-hidden', 'true');
    cv.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;display:block;z-index:0;pointer-events:none;border-radius:inherit';
    el.insertBefore(cv, el.firstChild);
    var gl = cv.getContext('webgl', { antialias: false });
    var sky = SKIES[cfg.sky] || SKIES.mediodia;

    function cssFallback() {
      el.style.background = 'linear-gradient(to bottom,' + sky.stops.map(function (s) { return s[0] + ' ' + (s[1] * 100) + '%'; }).join(',') + ')';
    }
    if (!gl) { cv.remove(); cssFallback(); return { setSky: function (k) { sky = SKIES[k] || sky; cssFallback(); }, destroy: function () {} }; }

    function sh(t, s) { var o = gl.createShader(t); gl.shaderSource(o, s); gl.compileShader(o); if (!gl.getShaderParameter(o, gl.COMPILE_STATUS)) console.error(gl.getShaderInfoLog(o)); return o; }
    var pr = gl.createProgram(); gl.attachShader(pr, sh(gl.VERTEX_SHADER, VS)); gl.attachShader(pr, sh(gl.FRAGMENT_SHADER, FS)); gl.linkProgram(pr); gl.useProgram(pr);
    var buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf); gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    var aLoc = gl.getAttribLocation(pr, 'a'); gl.enableVertexAttribArray(aLoc); gl.vertexAttribPointer(aLoc, 2, gl.FLOAT, false, 0, 0);
    var U = {};
    'R SEED GLP ASP TD NS GLR GLI BDP BDW BDI COV CLA STR CLADD STARS GR DRIFT RISE SCALE ST SP GLC BDC CLL CLS CLS2 STC STC2 OFF'.split(' ')
      .forEach(function (k) { U[k] = gl.getUniformLocation(pr, k); });

    function applySky() {
      var st = new Float32Array(18), sp = new Float32Array(6);
      sky.stops.forEach(function (s, i) { st.set(hex(s[0]), i * 3); sp[i] = s[1]; });
      gl.uniform3fv(U.ST, st); gl.uniform1fv(U.SP, sp); gl.uniform1f(U.NS, sky.stops.length);
      var g = sky.glow, b = sky.band, c = sky.clouds;
      gl.uniform3fv(U.GLC, hex(g[0])); gl.uniform2f(U.GLP, g[1], g[2]); gl.uniform1f(U.GLR, g[3]); gl.uniform1f(U.GLI, g[4]);
      gl.uniform3fv(U.BDC, hex(b[0])); gl.uniform1f(U.BDP, b[1]); gl.uniform1f(U.BDW, b[2]); gl.uniform1f(U.BDI, b[3]);
      gl.uniform3fv(U.CLL, hex(c.lit)); gl.uniform3fv(U.CLS, hex(c.low)); gl.uniform3fv(U.CLS2, hex(c.high));
      gl.uniform1f(U.COV, c.cover); gl.uniform1f(U.CLA, c.alpha); gl.uniform1f(U.STR, c.stretch); gl.uniform1f(U.CLADD, c.add);
      gl.uniform1f(U.STARS, sky.stars[0]); gl.uniform3fv(U.STC, hex(sky.stars[1])); gl.uniform3fv(U.STC2, hex(sky.stars[2]));
      gl.uniform1f(U.GR, sky.grain);
    }
    applySky();
    var sd = seedOf(String(cfg.seed)); gl.uniform2f(U.SEED, sd[0], sd[1]);
    gl.uniform1f(U.RISE, cfg.rise); gl.uniform1f(U.SCALE, cfg.cloudScale);

    // ===== Campo de ráfaga: rejilla de vectores en CPU, subida como textura =====
    var GW = 1, GH = cfg.gridRows, off, px, asp = 1;
    var tex = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, tex);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    gl.uniform1i(U.OFF, 0);
    function allocGrid() {
      GW = Math.max(8, Math.min(128, Math.round(GH * asp)));
      off = new Float32Array(GW * GH * 2); px = new Uint8Array(GW * GH * 4);
      for (var i = 0; i < px.length; i += 4) { px[i] = 128; px[i + 1] = 128; px[i + 3] = 255; }
      gl.bindTexture(gl.TEXTURE_2D, tex); gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, GW, GH, 0, gl.RGBA, gl.UNSIGNED_BYTE, px);
    }
    function resize() {
      var d = Math.min(global.devicePixelRatio || 1, cfg.maxDPR);
      cv.width = Math.max(1, cv.clientWidth * d | 0); cv.height = Math.max(1, cv.clientHeight * d | 0);
      var na = cv.clientWidth / Math.max(cv.clientHeight, 1);
      gl.viewport(0, 0, cv.width, cv.height);
      if (!off || Math.round(GH * na) !== GW) { asp = na; allocGrid(); } else asp = na;
    }
    var ro = new ResizeObserver(resize); ro.observe(el); resize();
    var visible = true, io = new IntersectionObserver(function (es) { visible = es[0].isIntersecting; }); io.observe(el);

    // ===== Cursor =====
    var mx = .5, my = .5, vx = 0, vy = 0, lt = 0, inside = false, moved = false, energy = 0;
    function onMove(e) {
      var r = el.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = 1 - (e.clientY - r.top) / r.height;
      var now = performance.now() / 1000, dt = Math.max(now - lt, 1 / 120), k = cfg.rafaga.smoothing;
      if (inside) { vx += ((x - mx) / dt - vx) * k; vy += ((y - my) / dt - vy) * k; }
      mx = x; my = y; lt = now; inside = true; moved = true;
    }
    function onLeave() { inside = false; vx = vy = 0; }
    el.addEventListener('pointermove', onMove); el.addEventListener('pointerleave', onLeave);

    // ===== Bucle =====
    var prev = performance.now() / 1000, td = 0, drift = 0, raf = 0;
    function frame() {
      raf = requestAnimationFrame(frame);
      var now = performance.now() / 1000, dt = Math.min(now - prev, .05); prev = now;
      if (!visible || document.hidden) return;
      if (!reduce.matches) { td += dt; drift += dt * asp * sky.ws / 60; }   // viento: anchos de header por minuto
      var R = cfg.rafaga;
      if (!moved) { vx *= Math.exp(-dt * R.idleDecay); vy *= Math.exp(-dt * R.idleDecay); } moved = false;
      var spd = Math.hypot(vx, vy), push = cfg.hover === 'rafaga' && inside && spd > R.minSpeed;
      if (push || energy > 1e-4) {
        var dec = Math.exp(-dt / R.friction), en = 0, gg = push ? Math.min(spd, R.maxSpeed) / spd : 0;
        for (var j = 0; j < GH; j++) for (var i = 0; i < GW; i++) {
          var q = (j * GW + i) * 2, ox = off[q] * dec, oy = off[q + 1] * dec;          // 1) fricción
          if (push) {                                                               // 2) impulso del gesto
            var dx = ((i + .5) / GW - mx) * asp, dy = (j + .5) / GH - my;
            var w = Math.exp(-(dx * dx + dy * dy) / R.sigma2);
            ox += vx * gg * dt * w * R.gain; oy += vy * gg * dt * w * R.gain;
          }
          var m = Math.hypot(ox, oy); if (m > R.max) { ox *= R.max / m; oy *= R.max / m; } // 3) tope
          off[q] = ox; off[q + 1] = oy; en = Math.max(en, Math.abs(ox) + Math.abs(oy));
          var p4 = (j * GW + i) * 4;                                                // 4) codificar 128 ± o/0.25·127
          px[p4] = Math.max(0, Math.min(255, 128 + ox / .25 * 127)); px[p4 + 1] = Math.max(0, Math.min(255, 128 + oy / .25 * 127));
        }
        energy = en; gl.bindTexture(gl.TEXTURE_2D, tex); gl.texSubImage2D(gl.TEXTURE_2D, 0, 0, 0, GW, GH, gl.RGBA, gl.UNSIGNED_BYTE, px);
      }
      gl.uniform2f(U.R, cv.width, cv.height); gl.uniform1f(U.ASP, asp); gl.uniform1f(U.TD, td); gl.uniform1f(U.DRIFT, drift);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    }
    raf = requestAnimationFrame(frame);

    return {
      setSky: function (k) { if (SKIES[k]) { sky = SKIES[k]; applySky(); } },
      destroy: function () { cancelAnimationFrame(raf); ro.disconnect(); io.disconnect(); el.removeEventListener('pointermove', onMove); el.removeEventListener('pointerleave', onLeave); cv.remove(); }
    };
  }

  global.KeyonsCielo = { mount: mount, SKIES: SKIES, DEFAULTS: DEFAULTS };
})(window);
