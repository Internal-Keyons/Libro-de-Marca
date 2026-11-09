/* Keyons · Laboratorio de Interfaces · plantillas base
   Cinco puntos de partida frecuentes en software SaaS y a medida. Están hechas con el kit
   del escenario (css/laboratorio-kit.css) y solo usan variables --lab-*, así responden
   a todos los controles de Explorar. Los datos son de muestra. */
(function () {
  'use strict';
  const P = {
    home: '<path d="M4 11l8-6 8 6v8H4z"/><path d="M10 19v-5h4v5"/>',
    chart: '<path d="M5 19V9M12 19V5M19 19v-7"/>',
    users: '<circle cx="9" cy="8" r="3"/><path d="M3.5 19c.8-3.2 3-5 5.5-5s4.7 1.8 5.5 5"/><path d="M16 5.5a3 3 0 0 1 0 5.6M18 14c1.4.7 2.3 2.4 2.6 5"/>',
    file: '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M10 12h5M10 16h5"/>',
    gear: '<circle cx="12" cy="12" r="3"/><path d="M12 3v2.5M12 18.5V21M3 12h2.5M18.5 12H21M5.6 5.6l1.8 1.8M16.6 16.6l1.8 1.8M5.6 18.4l1.8-1.8M16.6 7.4l1.8-1.8"/>',
    bell: '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20.5h4"/>',
    search: '<circle cx="11" cy="11" r="6"/><path d="m16 16 4 4"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    filter: '<path d="M4 6h16M7 12h10M10 18h4"/>',
    more: '<circle cx="6" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="18" cy="12" r="1"/>',
    check: '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    alert: '<path d="M12 4 2.8 19.5h18.4z"/><path d="M12 10v4.5M12 17v.5"/>',
    info: '<circle cx="12" cy="12" r="9"/><path d="M12 11v5.5M12 7.5v.5"/>',
    lock: '<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>',
    left: '<path d="M15 5l-7 7 7 7"/>',
    right: '<path d="M9 5l7 7-7 7"/>',
  };
  const i = (k) => `<svg class="lx-i" viewBox="0 0 24 24" aria-hidden="true">${P[k]}</svg>`;
  const nav = (cur) => `<nav class="lx-nav" aria-label="Principal"><div class="lx-brand">${i('chart')}Keyons Ops</div>`
    + [['home', 'Inicio'], ['chart', 'Indicadores'], ['users', 'Clientes'], ['file', 'Documentos'], ['gear', 'Configuración']]
      .map(([k, t]) => `<a href="#"${t === cur ? ' aria-current="page"' : ''}>${i(k)}<span>${t}</span></a>`).join('') + '</nav>';

  const dashboard = `<div class="lx-app">${nav('Indicadores')}<main class="lx-main">
  <header class="lx-top"><div><p class="lx-kicker">Operaciones · Noviembre</p><h1 class="lx-h1">El cierre bajó a tres días</h1></div>
    <div class="lx-row"><button class="lx-btn lx-btn--outline" type="button">${i('file')}Exportar</button><button class="lx-btn lx-btn--primary" type="button">${i('plus')}Nueva solicitud</button></div></header>
  <div class="lx-group lx-cols">
    <section class="lx-card lx-kpi"><p class="lx-meta">Duración del cierre</p><p class="lx-num">3 días</p><p class="lx-delta">−6 días frente a octubre</p></section>
    <section class="lx-card lx-kpi"><p class="lx-meta">Solicitudes abiertas</p><p class="lx-num">42</p><p class="lx-delta">12 vencen esta semana</p></section>
    <section class="lx-card lx-kpi"><p class="lx-meta">Horas recuperadas</p><p class="lx-num">126</p><p class="lx-delta">+18 % en el trimestre</p></section>
  </div>
  <div class="lx-grid lx-section">
    <section class="lx-card lx-s8"><div class="lx-card__h"><h2 class="lx-h3">Solicitudes por semana</h2><span class="lx-badge lx-badge--info">Últimas 8 semanas</span></div>
      <div class="lx-bars"><span style="--h:45%"></span><span style="--h:58%"></span><span style="--h:52%"></span><span style="--h:66%"></span><span style="--h:61%"></span><span style="--h:74%"></span><span style="--h:70%"></span><span class="is-on" style="--h:88%"></span></div>
      <div class="lx-axis"><span>S1</span><span>S2</span><span>S3</span><span>S4</span><span>S5</span><span>S6</span><span>S7</span><span>S8</span></div></section>
    <section class="lx-card lx-s4"><div class="lx-card__h"><h2 class="lx-h3">Actividad reciente</h2></div>
      <div class="lx-stack">
        <div class="lx-row"><span class="lx-badge lx-badge--ok">${i('check')}Aprobada</span><span class="lx-small">Conciliación de proveedores</span></div>
        <div class="lx-row"><span class="lx-badge lx-badge--warn">En revisión</span><span class="lx-small">Ajuste de inventario</span></div>
        <div class="lx-row"><span class="lx-badge lx-badge--err">Rechazada</span><span class="lx-small">Pago fuera de plazo</span></div>
      </div></section>
  </div></main></div>`;

  const rows = [['Distribuidora Central', 'Ana Rojas', 'Activo', 'ok', '12 nov.'], ['Clínica del Valle', 'Luis Mora', 'Pendiente', 'warn', '10 nov.'], ['Agroexport Norte', 'María Solís', 'Activo', 'ok', '08 nov.'], ['Laboratorio Andino', 'Jorge Vega', 'Bloqueado', 'err', '02 nov.'], ['Ferretería El Sol', 'Carla Núñez', 'Activo', 'ok', '28 oct.']];
  const listado = `<div class="lx-app">${nav('Clientes')}<main class="lx-main">
  <header class="lx-top"><div><p class="lx-kicker">Clientes</p><h1 class="lx-h2">Cartera activa</h1></div><button class="lx-btn lx-btn--primary" type="button">${i('plus')}Agregar cliente</button></header>
  <div class="lx-row" style="margin-bottom:var(--lab-6)"><div class="lx-field" style="flex:1;min-width:220px"><label for="q">Buscar</label><input class="lx-input" id="q" type="search" placeholder="Nombre, responsable o código"></div>
    <div class="lx-field"><label for="est">Estado</label><select class="lx-select" id="est"><option>Todos</option><option>Activo</option><option>Pendiente</option><option>Bloqueado</option></select></div></div>
  <section class="lx-card" style="padding:0"><div class="lx-scroll"><table class="lx-table"><thead><tr><th scope="col">Cliente</th><th scope="col">Responsable</th><th scope="col">Estado</th><th scope="col">Última actividad</th><th scope="col"><span class="lx-meta">Acciones</span></th></tr></thead><tbody>`
    + rows.map(([c, r, e, k, d]) => `<tr><td><b>${c}</b></td><td>${r}</td><td><span class="lx-badge lx-badge--${k}">${e}</span></td><td>${d}</td><td><button class="lx-btn lx-btn--ghost" type="button" aria-label="Más acciones para ${c}">${i('more')}</button></td></tr>`).join('')
    + `</tbody></table></div></section>
  <div class="lx-row" style="justify-content:space-between;margin-top:var(--lab-6)"><p class="lx-small">5 de 48 clientes</p><div class="lx-row"><button class="lx-btn lx-btn--outline" type="button" aria-label="Página anterior">${i('left')}</button><button class="lx-btn lx-btn--outline" type="button" aria-label="Página siguiente">${i('right')}</button></div></div>
  </main></div>`;

  const formulario = `<main class="lx-main" style="max-width:720px">
  <p class="lx-kicker">Nueva solicitud</p><h1 class="lx-h2" style="margin-top:var(--lab-2)">Datos del responsable</h1>
  <ol class="lx-steps" style="margin:var(--lab-8) 0"><li class="is-done">Tipo de solicitud</li><li aria-current="step">Responsable</li><li>Documentos</li><li>Resumen</li></ol>
  <section class="lx-card lx-stack">
    <div class="lx-field"><label for="n">Nombre completo</label><input class="lx-input" id="n" value="Ana Rojas"></div>
    <div class="lx-field is-error"><label for="c">Correo de trabajo</label><input class="lx-input" id="c" value="ana.rojas@" aria-invalid="true" aria-describedby="c-h"><p class="lx-help" id="c-h">Escriba un correo completo, por ejemplo ana@empresa.com.</p></div>
    <div class="lx-field"><label for="a">Área</label><select class="lx-select" id="a"><option>Finanzas</option><option>Operaciones</option><option>Comercial</option></select></div>
    <label class="lx-check"><input type="checkbox" checked>Recibir avisos cuando cambie el estado</label>
  </section>
  <div class="lx-row" style="justify-content:space-between;margin-top:var(--lab-6)"><button class="lx-btn lx-btn--ghost" type="button">${i('left')}Volver</button><button class="lx-btn lx-btn--primary" type="button">Continuar</button></div>
  </main>`;

  const ajustes = `<div class="lx-app">${nav('Configuración')}<main class="lx-main" style="max-width:880px">
  <header class="lx-top"><div><p class="lx-kicker">Configuración</p><h1 class="lx-h2">Cuenta y notificaciones</h1></div></header>
  <div class="lx-tabs" role="tablist" aria-label="Secciones"><button type="button" role="tab" aria-selected="true">Cuenta</button><button type="button" role="tab" aria-selected="false">Notificaciones</button><button type="button" role="tab" aria-selected="false">Seguridad</button></div>
  <div class="lx-group lx-section">
    <section class="lx-card lx-stack"><h2 class="lx-h3">Perfil</h2>
      <div class="lx-grid"><div class="lx-field lx-s6"><label for="pn">Nombre</label><input class="lx-input" id="pn" value="Ana Rojas"></div><div class="lx-field lx-s6"><label for="pe">Correo</label><input class="lx-input" id="pe" value="ana@empresa.com"></div></div></section>
    <section class="lx-card lx-stack"><h2 class="lx-h3">Avisos</h2>
      <label class="lx-check" style="justify-content:space-between">Resumen diario por correo<input class="lx-switch" type="checkbox" checked></label>
      <label class="lx-check" style="justify-content:space-between">Avisos de vencimiento<input class="lx-switch" type="checkbox" checked></label>
      <label class="lx-check" style="justify-content:space-between">Novedades del producto<input class="lx-switch" type="checkbox"></label></section>
  </div>
  <div class="lx-row" style="justify-content:flex-end;margin-top:var(--lab-6)"><button class="lx-btn lx-btn--outline" type="button">Cancelar</button><button class="lx-btn lx-btn--primary" type="button">Guardar cambios</button></div>
  </main></div>`;

  const estados = `<main class="lx-main">
  <p class="lx-kicker">Mensajes y estados</p><h1 class="lx-h2" style="margin:var(--lab-2) 0 var(--lab-8)">Qué pasó y cómo continuar</h1>
  <div class="lx-group">
    <div class="lx-card lx-alert lx-alert--err" role="alert">${i('alert')}<div><b>No pudimos guardar la solicitud</b><p class="lx-small">La conexión se interrumpió. Sus datos siguen aquí: vuelva a intentarlo.</p></div></div>
    <div class="lx-card lx-alert lx-alert--ok" role="status">${i('check')}<div><b>Solicitud enviada</b><p class="lx-small">Le avisaremos por correo cuando cambie de estado.</p></div></div>
    <div class="lx-card lx-alert lx-alert--warn">${i('info')}<div><b>Faltan dos documentos</b><p class="lx-small">Puede continuar y adjuntarlos antes del 20 de noviembre.</p></div></div>
  </div>
  <div class="lx-grid lx-section">
    <section class="lx-card lx-empty lx-s6">${i('search')}<h2 class="lx-h3">Sin resultados</h2><p class="lx-p">No hay clientes con «Andina». Revise la búsqueda o quite un filtro.</p><button class="lx-btn lx-btn--outline" type="button">Quitar filtros</button></section>
    <section class="lx-card lx-empty lx-s6">${i('lock')}<h2 class="lx-h3">Sin permiso</h2><p class="lx-p">Esta sección es para administradores. Pida acceso a su responsable.</p><button class="lx-btn lx-btn--primary" type="button">Pedir acceso</button></section>
    <section class="lx-card lx-s12 lx-stack" aria-busy="true"><p class="lx-meta">Cargando actividad</p><div class="lx-skel" style="width:70%"></div><div class="lx-skel" style="width:90%"></div><div class="lx-skel" style="width:55%"></div></section>
  </div>
  <section class="lx-section" style="text-align:center"><p class="lx-num">404</p><h2 class="lx-h2" style="margin-top:var(--lab-4)">Esta página ya no está aquí</h2><p class="lx-p" style="margin:var(--lab-3) auto var(--lab-6)">Puede que el enlace haya cambiado. Vuelva al inicio o busque lo que necesita.</p><div class="lx-row" style="justify-content:center"><button class="lx-btn lx-btn--outline" type="button">${i('home')}Ir al inicio</button><button class="lx-btn lx-btn--outline" type="button">${i('search')}Buscar</button></div></section>
  </main>`;

  window.LAB_PLANTILLAS = [
    { id: 'dashboard', t: 'Dashboard', d: 'Indicadores, gráfico y actividad reciente.', html: dashboard },
    { id: 'listado', t: 'Listado con filtros', d: 'Búsqueda, filtros, tabla, paginación y acciones por fila.', html: listado },
    { id: 'formulario', t: 'Formulario por pasos', d: 'Progreso, validación y navegación entre pasos.', html: formulario },
    { id: 'ajustes', t: 'Configuración de cuenta', d: 'Secciones, interruptores y guardado.', html: ajustes },
    { id: 'estados', t: 'Mensajes y estados', d: 'Error, éxito, aviso, vacío, sin permiso, carga y 404.', html: estados },
  ];
  window.LAB_ICONOS = P;
})();
