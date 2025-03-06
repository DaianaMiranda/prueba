// Función para cargar opciones en un select (Años y Comisiones)
function cargarSelect(url, selectId) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error en la solicitud: ${response.statusText}`);
            }
            return response.json();
        })
        .then(data => {
            const select = document.getElementById(selectId);
            select.innerHTML = '<option value="">Seleccionar</option>'; // Limpiar y agregar opción por defecto
            if (Array.isArray(data)) {
                data.forEach(item => {
                    let option = document.createElement('option');
                    option.value = item.id;
                    option.textContent = item.nombre;
                    select.appendChild(option);
                });
            } else {
                console.error("La respuesta no es un array:", data);
            }
        })
        .catch(error => console.error(`Error cargando ${selectId}:`, error));
}

// Función para cargar las materias cuando se selecciona una comisión
function cargarMaterias(url, containerId) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error en la solicitud: ${response.statusText}`);
            }
            return response.json();
        })
        .then(data => {
            const container = document.getElementById(containerId);
            container.innerHTML = ''; 
            if (Array.isArray(data)) {
                data.forEach(item => {
                    const div = document.createElement('div');
                    div.classList.add('form-check');

                    const checkbox = document.createElement('input');
                    checkbox.type = 'checkbox';
                    checkbox.name = 'materias[]';  
                    checkbox.value = item.id;
                    checkbox.id = `materia-${item.id}`;
                    checkbox.classList.add('form-check-input');

                    const label = document.createElement('label');
                    label.htmlFor = `materia-${item.id}`;
                    label.textContent = item.nombre;
                    label.classList.add('form-check-label');

                    div.appendChild(checkbox);
                    div.appendChild(label);
                    container.appendChild(div);
                });
            } else {
                console.error("La respuesta no es un array:", data);
            }
        })
        .catch(error => console.error(`Error cargando materias:`, error));
}

//  selección de carrera
document.getElementById('carrera').addEventListener('change', function() {
    const carreraId = this.value;
    if (carreraId) {
        cargarSelect(`/get_anios/${carreraId}`, 'anio'); // Cargar años según la carrera
    } else {
        document.getElementById('anio').innerHTML = '<option value="">Seleccionar</option>';
        document.getElementById('comision').innerHTML = '<option value="">Seleccionar</option>';
        document.getElementById('materias-container').innerHTML = '';
    }
});

//  selección de año
document.getElementById('anio').addEventListener('change', function() {
    const carreraId = document.getElementById('carrera').value;
    const anioId = this.value;
    if (carreraId && anioId) {
        cargarSelect(`/get_comisiones/${carreraId}/${anioId}`, 'comision'); // Cargar comisiones según la carrera y año
    } else {
        document.getElementById('comision').innerHTML = '<option value="">Seleccionar</option>';
        document.getElementById('materias-container').innerHTML = '';
    }
});

// selección de comisión
document.getElementById('comision').addEventListener('change', function() {
    const carreraId = document.getElementById('carrera').value;
    const anioId = document.getElementById('anio').value;
    const comisionId = this.value;
    if (carreraId && anioId && comisionId) {
        cargarMaterias(`/get_materias/${carreraId}/${anioId}/${comisionId}`, 'materias-container');
    } else {
        document.getElementById('materias-container').innerHTML = '';
    }
});
