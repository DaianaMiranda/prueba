function cargarOpciones(url, selectId, placeholder) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error ${response.status} al cargar ${selectId}`);
            }
            return response.json();
        })
        .then(data => {
            const select = document.getElementById(selectId);
            select.innerHTML = `<option value="">${placeholder}</option>`;
            data.forEach(item => {
                const option = document.createElement('option');
                option.value = item.id;
                option.textContent = item.nombre;
                select.appendChild(option);
            });
        })
        .catch(error => {
            console.error(`❌ Error cargando opciones para ${selectId}:`, error);
        });
}

// Al seleccionar carrera, cargar años disponibles
document.getElementById('carrera').addEventListener('change', function() {
    const carreraId = this.value;
    cargarOpciones(`/get_anios_profesor/${carreraId}`, 'anio', 'Seleccionar Año');
    limpiarSelect('comision');
    limpiarSelect('materia');
});

// Al seleccionar año, cargar comisiones disponibles
document.getElementById('anio').addEventListener('change', function() {
    const carreraId = document.getElementById('carrera').value;
    const anioId = this.value;
    cargarOpciones(`/get_comisiones_profesor/${carreraId}/${anioId}`, 'comision', 'Seleccionar Comisión');
    limpiarSelect('materia');
});

// Al seleccionar comisión, cargar materias disponibles
document.getElementById('comision').addEventListener('change', function() {
    const carreraId = document.getElementById('carrera').value;
    const anioId = document.getElementById('anio').value;
    const comisionId = this.value;
    cargarOpciones(`/get_materias_profesor/${carreraId}/${anioId}/${comisionId}`, 'materia', 'Seleccionar Materia');
});

// limpiar selects
function limpiarSelect(selectId) {
    const select = document.getElementById(selectId);
    select.innerHTML = '<option value="">Seleccionar</option>';
}
