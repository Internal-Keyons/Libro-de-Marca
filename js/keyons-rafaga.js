/* ════════════════════════════════════════════════════════════════════
   KeyonsRafaga · la materia de las ráfagas (KYN-MRK-ILU-006) con el viento del encabezado

   Misma física que js/keyons-cielo.js: una rejilla de vectores en CPU recibe el
   impulso del cursor con caída gaussiana, se frena con fricción y vuelve sola a su
   lugar. Lo que se desplaza es la ráfaga dibujada (su forma y sus colores, leídos
   del SVG de la página), no un objeto rígido: cada zona se dispersa como la nube.
   Un viento lento y continuo mantiene la materia viva, como las nubes del encabezado.

   Uso: KeyonsRafaga.mount(figura)  → { destroy }
   Si no hay WebGL, el SVG original queda a la vista sin cambios.
   ════════════════════════════════════════════════════════════════════ */
(function (global) {
  'use strict';

  /* Parámetros del campo de ráfaga: los mismos del encabezado */
  var R = { sigma2: .012, gain: .55, max: .24, friction: 4.2, minSpeed: .02, maxSpeed: 3, smoothing: .4, idleDecay: 10 };
  var GRID_ROWS = 32, MAX_DPR = 1.5;

  var VS = 'attribute vec2 a;void main(){gl_Position=vec4(a,0.,1.);}';
  var FS = [
    '#ifdef GL_FRAGMENT_PRECISION_HIGH', 'precision highp float;', '#else', 'precision mediump float;', '#endif',
    'uniform vec2 R;uniform float TD,ASP,WIND;uniform sampler2D IMG,OFF;',
    'float h(vec2 p){p=fract(p*vec2(123.34,456.21));p+=dot(p,p+45.32);return fract(p.x*p.y);}',
    'float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}',
    'float fbm(vec2 p){float v=0.,a=.5;mat2 r=mat2(.8,.6,-.6,.8);for(int i=0;i<4;i++){v+=a*n(p);p=r*p*2.03+11.7;a*=.5;}return v;}',
    'void main(){',
    ' vec2 uv=gl_FragCoord.xy/R;',
    ' vec2 o=(texture2D(OFF,uv).xy-.5)*.5;',                         // desplazamiento de ráfaga (igual que el cielo)
    ' vec2 q=vec2(uv.x*ASP,uv.y)*2.2;',
    ' q-=vec2(TD*.05,TD*.006);',                                    // deriva lenta, como las nubes del encabezado
    ' vec2 w=vec2(fbm(q+vec2(TD*.03,TD*.05)),fbm(q+vec2(5.2-TD*.025,1.3+TD*.04)))-.5;', // viento: la materia fluye
    ' vec2 p=uv-o-w*WIND;',
    ' gl_FragColor=texture2D(IMG,p);',
    '}'
  ].join('\n');

  function mount(fig) {
    var svg = fig.querySelector('svg');
    if (!svg || fig.__rafaga) return null;
    var reduce = global.matchMedia ? global.matchMedia('(prefers-reduced-motion: reduce)') : { matches: false };
    var cv = document.createElement('canvas');
    cv.className = 'rfp__gl';
    cv.setAttribute('aria-hidden', 'true');
    cv.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;display:block;pointer-events:none';
    svg.insertAdjacentElement('afterend', cv);
    var gl = cv.getContext('webgl', { antialias: false, premultipliedAlpha: true, alpha: true });
    if (!gl) { cv.remove(); return null; }

    function sh(t, s) { var o = gl.createShader(t); gl.shaderSource(o, s); gl.compileShader(o); return o; }
    var pr = gl.createProgram(); gl.attachShader(pr, sh(gl.VERTEX_SHADER, VS)); gl.attachShader(pr, sh(gl.FRAGMENT_SHADER, FS)); gl.linkProgram(pr);
    if (!gl.getProgramParameter(pr, gl.LINK_STATUS)) { cv.remove(); return null; }
    gl.useProgram(pr);
    var buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf); gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    var aLoc = gl.getAttribLocation(pr, 'a'); gl.enableVertexAttribArray(aLoc); gl.vertexAttribPointer(aLoc, 2, gl.FLOAT, false, 0, 0);
    var U = {}; 'R TD ASP WIND IMG OFF'.split(' ').forEach(function (k) { U[k] = gl.getUniformLocation(pr, k); });

    function texture(unit) {
      var t = gl.createTexture(); gl.activeTexture(gl.TEXTURE0 + unit); gl.bindTexture(gl.TEXTURE_2D, t);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      return t;
    }
    var img = texture(0), tex = texture(1);
    gl.uniform1i(U.IMG, 0); gl.uniform1i(U.OFF, 1);
    var ready = false, alive = true;

    /* La ráfaga se lee del propio SVG: misma forma, mismos colores, mismos desenfoques */
    function raster() {
      var w = cv.width, hh = cv.height, c = svg.cloneNode(true);
      c.querySelectorAll('.rfp__dust,animate,animateMotion').forEach(function (x) { x.remove(); });
      c.setAttribute('xmlns', 'http://www.w3.org/2000/svg'); c.setAttribute('width', w); c.setAttribute('height', hh);
      var url = URL.createObjectURL(new Blob([new XMLSerializer().serializeToString(c)], { type: 'image/svg+xml' }));
      var im = new Image();
      im.onload = function () {
        URL.revokeObjectURL(url);
        if (!alive) return;
        gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, img);
        gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true); gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, true);
        gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, im);
        gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false); gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, false);
        if (!ready) { ready = true; svg.style.visibility = 'hidden'; fig.classList.add('has-rafaga'); }
      };
      im.src = url;
    }

    /* ===== Campo de ráfaga: rejilla de vectores en CPU, subida como textura ===== */
    var GW = 1, GH = GRID_ROWS, off, px, asp = 1, rt = 0;
    function allocGrid() {
      GW = Math.max(8, Math.min(128, Math.round(GH * asp)));
      off = new Float32Array(GW * GH * 2); px = new Uint8Array(GW * GH * 4);
      for (var i = 0; i < px.length; i += 4) { px[i] = 128; px[i + 1] = 128; px[i + 3] = 255; }
      gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, tex); gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, GW, GH, 0, gl.RGBA, gl.UNSIGNED_BYTE, px);
    }
    function resize() {
      var d = Math.min(global.devicePixelRatio || 1, MAX_DPR);
      var W = Math.max(1, cv.clientWidth * d | 0), H = Math.max(1, cv.clientHeight * d | 0);
      if (W === cv.width && H === cv.height && off) return;
      cv.width = W; cv.height = H; gl.viewport(0, 0, W, H);
      asp = cv.clientWidth / Math.max(cv.clientHeight, 1);
      if (!off || Math.round(GH * asp) !== GW) allocGrid();
      clearTimeout(rt); rt = setTimeout(raster, ready ? 160 : 0);
    }
    var ro = new ResizeObserver(resize); ro.observe(fig); resize();
    var visible = true, io = new IntersectionObserver(function (es) { visible = es[0].isIntersecting; }); io.observe(fig);

    /* ===== Cursor ===== */
    var mx = .5, my = .5, vx = 0, vy = 0, lt = 0, inside = false, moved = false, energy = 0;
    function onMove(e) {
      var r = fig.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = 1 - (e.clientY - r.top) / r.height;
      var now = performance.now() / 1000, dt = Math.max(now - lt, 1 / 120), k = R.smoothing;
      if (inside) { vx += ((x - mx) / dt - vx) * k; vy += ((y - my) / dt - vy) * k; }
      mx = x; my = y; lt = now; inside = true; moved = true;
    }
    function onLeave() { inside = false; vx = vy = 0; }
    fig.addEventListener('pointermove', onMove); fig.addEventListener('pointerleave', onLeave);

    /* ===== Bucle ===== */
    var prev = performance.now() / 1000, td = Math.random() * 40, raf = 0;
    function frame() {
      raf = requestAnimationFrame(frame);
      var now = performance.now() / 1000, dt = Math.min(now - prev, .05); prev = now;
      if (!visible || document.hidden || !ready) return;
      if (!reduce.matches) td += dt;
      if (!moved) { vx *= Math.exp(-dt * R.idleDecay); vy *= Math.exp(-dt * R.idleDecay); } moved = false;
      var spd = Math.hypot(vx, vy), push = inside && spd > R.minSpeed;
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
        energy = en; gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, tex); gl.texSubImage2D(gl.TEXTURE_2D, 0, 0, 0, GW, GH, gl.RGBA, gl.UNSIGNED_BYTE, px);
      }
      gl.uniform2f(U.R, cv.width, cv.height); gl.uniform1f(U.TD, td); gl.uniform1f(U.ASP, asp); gl.uniform1f(U.WIND, reduce.matches ? 0 : .07);   // en reposo la forma fluye; el cursor la dispersa encima
      gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    }
    raf = requestAnimationFrame(frame);
    fig.__rafaga = true;

    return {
      destroy: function () {
        alive = false; cancelAnimationFrame(raf); ro.disconnect(); io.disconnect();
        fig.removeEventListener('pointermove', onMove); fig.removeEventListener('pointerleave', onLeave);
        cv.remove(); svg.style.visibility = ''; fig.classList.remove('has-rafaga'); fig.__rafaga = false;
      }
    };
  }

  global.KeyonsRafaga = { mount: mount };
})(window);
