/* Archivo de campañas (21.3, KYN-MRK-RED-001) · fuente única de las campañas aprobadas.
   Funciona sin servidor: es JS, igual que js/tipografia-datos.js.
   Una campaña entra aquí solo cuando está aprobada. Sus materiales se enlazan a su fuente original: nunca se copian.

   Formato de cada campaña:
   {
     id: 'CMP-2026-01',                    identificador de la campaña
     nombre: 'Nombre de la campaña',
     tipo: 'Lanzamiento',                  tipo de campaña (filtro)
     anio: 2026,                           año (filtro)
     estado: 'Activa',                     Activa · Finalizada · Archivada (filtro)
     concepto: '…', objetivo: '…',
     inicio: '2026-03-01', fin: '2026-04-30',
     canales: ['Redes', 'Sitio web'],
     responsable: '…',
     condiciones: '…',                     condiciones de uso de los materiales
     portada: 'assets/img/cielo-amanecer.webp',   opcional: imagen de la Galería que se muestra en la tarjeta (ruta desde la raíz)
     materiales: [
       { t: 'Fotografía de portada', fuente: 'galeria', ref: 'KY-001' },
       { t: 'Plantilla de publicación', fuente: 'plantillas', ref: 'plantillas' },
       { t: 'Presentación de lanzamiento', fuente: 'presentaciones', ref: 'plantillas' },
       { t: 'Textura de fondo', fuente: 'texturas', ref: 'texturas' },
       { t: 'Ícono de la campaña', fuente: 'iconos', ref: 'catalogo' },
       { t: 'Publicación final', fuente: 'campana', archivo: 'assets/campanas/cmp-2026-01/publicacion.png' }
     ]
   }
   fuente: galeria (ref = ID de imagen) · texturas · iconos · plantillas · presentaciones (ref = ancla de la sección)
           · campana: pieza final creada para la campaña, que se conserva en el archivo de esa campaña (archivo = ruta desde la raíz). */
window.KEYONS_CAMPANAS = [];
