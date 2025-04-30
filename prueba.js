(function () {
    const input = document.createElement('input');
    input.type = 'file';
    input.webkitdirectory = true;
    input.style.display = 'none';
  
    input.addEventListener('change', () => {
      const archivos = Array.from(input.files);
      const tree = {};
  
      for (const archivo of archivos) {
        const partes = archivo.webkitRelativePath.split('/');
        const carpeta = partes[0];
        const subcarpeta = partes[1];
  
        if (!tree[carpeta]) tree[carpeta] = new Set();
        if (subcarpeta) tree[carpeta].add(subcarpeta);
      }
  
      const output = [];
      for (const carpeta in tree) {
        output.push('📁 ' + carpeta);
        for (const sub of tree[carpeta]) {
          output.push('  📁 ' + sub);
        }
      }
  
      console.log(output.join('\n'));
    });
  
    document.body.appendChild(input);
    input.click();
  })();
  