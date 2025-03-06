document.getElementById('carrera').addEventListener('change', function() {
    const carreraId = this.value;

    // Obtener los años correspondientes a la carrera seleccionada
    fetch(`/get_anios/${carreraId}`)
        .then(response => response.json())
        .then(data => {
            const anioSelect = document.getElementById('anio');
            anioSelect.innerHTML = '<option value="">Seleccionar Año</option>';
            data.años.forEach(anio => {
                const option = document.createElement('option');
                option.value = anio.id;
                option.textContent = anio.nombre;
                anioSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching años:', error);
        });
});

document.getElementById('anio').addEventListener('change', function() {
    const anioId = this.value;  
    const carreraId = document.getElementById('carrera').value;

    // Obtener las comisiones correspondientes al año seleccionado
    fetch(`/get_comisiones/${carreraId}/${anioId}`)  
        .then(response => response.json())
        .then(data => {
            const comisionSelect = document.getElementById('comision');
            comisionSelect.innerHTML = '<option value="">Seleccionar Comisión</option>';
            data.comisiones.forEach(comision => {
                const option = document.createElement('option');
                option.value = comision.id;
                option.textContent = comision.nombre; 
                comisionSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching comisiones:', error);
        });
});

document.getElementById('comision').addEventListener('change', function() {
    const anioId = document.getElementById('anio').value;  
    const carreraId = document.getElementById('carrera').value;  
    const comisionId = this.value;

    // Obtener las materias correspondientes a la carrera, año y comisión seleccionados
    fetch(`/get_materias/${carreraId}/${anioId}/${comisionId}`)  
        .then(response => response.json())
        .then(data => {
            const materiaSelect = document.getElementById('materia');
            materiaSelect.innerHTML = '<option value="">Seleccionar Materia</option>';
            data.materias.forEach(materia => {
                const option = document.createElement('option');
                option.value = materia.id;
                option.textContent = materia.nombre; 
                materiaSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching materias:', error);
        });
});
