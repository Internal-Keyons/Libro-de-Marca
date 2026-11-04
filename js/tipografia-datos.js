/* Tipografía · fuente única de datos.
   La escala de 8.2, el probador de 8.3 y las referencias V1 leen estos mismos valores.
   tr: tracking en %; desde trDesde px se usa trMax. */
window.KEYONS_TIPO = {
  familias: { tasa: 'TASA Orbiter', jak: 'Plus Jakarta Sans' },
  niveles: [
    { k: 'display', n: 'Display', f: 'tasa', min: 52, max: 128, peso: 500, lh: 0.93, tr: -3, trMax: -5, trDesde: 80 },
    { k: 'titulo', n: 'Título de sección', f: 'jak', min: 30, max: 44, peso: 500, lh: 1.1, tr: 0 },
    { k: 'subtitulo', n: 'Subtítulo', f: 'jak', min: 22, max: 27, peso: 500, lh: 1.2, tr: 0 },
    { k: 'menor', n: 'Título menor', f: 'jak', min: 17, max: 18, peso: 600, lh: 1.3, tr: 0 },
    { k: 'entrada', n: 'Entrada', f: 'jak', min: 18, max: 20, peso: 400, lh: 1.55, tr: 0 },
    { k: 'cuerpo', n: 'Cuerpo', f: 'jak', min: 16, max: 17, peso: 400, lh: 1.65, tr: 0 },
    { k: 'pequeno', n: 'Pequeño', f: 'jak', min: 14, max: 15, peso: 400, lh: 1.6, tr: 0 },
    { k: 'rotulo', n: 'Rótulo', f: 'jak', min: 13, max: 13, peso: 500, lh: 1.4, tr: 0 },
    { k: 'kicker', n: 'Kicker', f: 'tasa', min: 14, max: 14, peso: 500, lh: 1, tr: 8, mayus: true },
  ],
  /* Funciones de la jerarquía invertida: toman familia, peso e interlineado del nivel indicado */
  roles: {
    contexto: { n: 'Título contextual', base: 'menor', peso: 500 },
    declaracion: { n: 'Declaración protagonista', base: 'titulo', peso: 400 },
  },
  /* Configuraciones de referencia: jerarquía · intensidad */
  v1: {
    'trad-contenida': [['display', 52], ['titulo', 36], ['subtitulo', 24], ['entrada', 20], ['cuerpo', 16]],
    'trad-expresiva': [['display', 80], ['titulo', 44], ['subtitulo', 27], ['entrada', 20], ['cuerpo', 16]],
    'inv-contenida': [['contexto', 20], ['declaracion', 44], ['entrada', 20], ['cuerpo', 16]],
    'inv-expresiva': [['contexto', 23], ['declaracion', 68], ['entrada', 20], ['cuerpo', 16]],
  },
  /* Lectura prolongada · referencia digital V1 */
  lectura: { cuerpo: [16, 18], lh: [1.5, 1.65], cpl: [55, 75] },
};
