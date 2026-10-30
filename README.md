# Casa Camargo

Web de https://casacamargo.cl. El historial de cambios se mantiene en este repositorio.

## Archivos
- index.html: versión inicial proporcionada por Eduardo; incluye imágenes, estilos y código.
- scripts/deploy.py: transfiere únicamente la página mediante FTPS explícito, puerto 21.
- .github/workflows/publicar.yml: publicación exclusivamente manual.

## Trabajo compartido
Crear una rama para cada cambio y abrir una solicitud de revisión (pull request).
Revisar el resultado antes de incorporarlo a main. Guardar cambios o aprobar una
solicitud no publica la web. Para colaborar, el propietario debe invitar los
usuarios exactos de Diego y Benja en Settings > Collaborators.
El repositorio actualmente es público.

## Publicar
Pendiente: primera prueba real de conexión con el hosting, a partir del domingo
1 de noviembre de 2026, cuando Eduardo confirme la disponibilidad de Actions.
No hay publicación automática ni programación.

1. Abrir Actions > Publicar Casa Camargo > Run workflow.
2. Seleccionar main y escribir PUBLICAR.
3. Ejecutar una sola vez y revisar el resultado.
4. Revisar https://casacamargo.cl y www.

Secretos requeridos: FTP_SERVER, FTP_USERNAME y FTP_PASSWORD.
Se confirmó la existencia de sus nombres; los valores no se han leído ni probado.

La cuenta FTP debe tener /home/casacama/public_html como raíz.
El script usa / dentro de esa cuenta; no añade public_html de nuevo.
La conexión exige cifrado y certificado válido. Si falla el certificado,
consultar al hosting por el nombre FTPS correcto; no desactivar la verificación.

La publicación guarda index-respaldo-<sha256>.html, verifica la transferencia y
reemplaza únicamente index.html. No sincroniza ni borra carpetas.
contab, factura, .htaccess y los registros DNS quedan fuera de este proceso.

## Volver a una versión anterior
Revertir el cambio en GitHub y publicar manualmente, o copiar el contenido de un
respaldo a index.html desde cPanel. Antes de hacerlo, conservar la versión actual.

## Estado del sitio
El formulario incluido en el HTML es una demostración: no envía consultas.
Este repositorio contiene el HTML exportado, no los componentes originales del
constructor. Es posible editarlo, aunque recuperar las fuentes originales haría
más sencillo mantenerlo.
