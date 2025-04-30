async function seleccionarYMostrarTree() {
    const output = [];
  
    async function mostrarArbol(dirHandle, nivel = 0) {
      for await (const [nombre, handle] of dirHandle.entries()) {
        if (handle.kind === 'directory') {
          output.push('  '.repeat(nivel) + '📁 ' + nombre);
          if (nivel === 0) {
            await mostrarArbol(handle, nivel + 1);
          }
        }
      }
    }
  
    try {
      const dirHandle = await window.showDirectoryPicker();
      await mostrarArbol(dirHandle);
      console.log(output.join('\n'));
    } catch (err) {
      console.error('Error o cancelado:', err.message);
    }
  }
  
  // Llama a la función (puedes enlazarla a un botón también)
  seleccionarYMostrarTree();
  