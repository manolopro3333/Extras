fetch('https://generalsantander.gnosoft.com.co/inicioV2/servicioGeneral?idServicio=99&idPersona=243787')
  .then(response => response.text())  // Obtiene el contenido como texto
  .then(xmlText => {
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(xmlText, 'application/xml');

    // Muestra el contenido en consola
    console.log('Contenido del XML:', xmlDoc);

    // Accede a los elementos del XML
    const scripts = xmlDoc.getElementsByTagName('script');
    for (let i = 0; i < scripts.length; i++) {
      console.log('Elemento <script> encontrado:', scripts[i].outerHTML);
    }

    // También puedes acceder al número final (el 0) como un texto dentro del XML
    const numberElement = xmlDoc.getElementsByTagName('root')[0].textContent.trim();
    console.log('Número encontrado:', numberElement);
  })
  .catch(error => console.error('Error al cargar el XML:', error));
