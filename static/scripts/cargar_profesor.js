document.addEventListener('DOMContentLoaded', () => {
    const carreraSelect = document.getElementById('carrera');
    const anioSelect = document.getElementById('anio');
    const comisionSelect = document.getElementById('comision');
    const materiasContainer = document.getElementById('materias-container');

    carreraSelect.addEventListener('change', function() {
        const carreraId = this.value;
        limpiarSelect(anioSelect);
        limpiarSelect(comisionSelect);
        materiasContainer.innerHTML = '';

        if (carreraId) {
            fetch(`/get_anios/${carreraId}`)
                .then(response => response.json())
                .then(data => {
                    data.años.forEach(anio => {
                        const option = document.createElement('option');
                        option.value = anio.id;
                        option.textContent = anio.nombre;
                        anioSelect.appendChild(option);
                    });
                })
                .catch(error => console.error('Error al obtener los años:', error));
        }
    });

    anioSelect.addEventListener('change', function() {
        const carreraId = carreraSelect.value;
        const anioId = this.value;
        limpiarSelect(comisionSelect);
        materiasContainer.innerHTML = '';

        if (carreraId && anioId) {
            fetch(`/get_comisiones/${carreraId}/${anioId}`)
                .then(response => response.json())
                .then(data => {
                    data.comisiones.forEach(comision => {
                        const option = document.createElement('option');
                        option.value = comision.id;
                        option.textContent = comision.nombre;
                        comisionSelect.appendChild(option);
                    });
                })
                .catch(error => console.error('Error al obtener las comisiones:', error));
        }
    });

    comisionSelect.addEventListener('change', function() {
        const carreraId = carreraSelect.value;
        const anioId = anioSelect.value;
        const comisionId = this.value;
        materiasContainer.innerHTML = '';

        if (carreraId && anioId && comisionId) {
            fetch(`/get_materias/${carreraId}/${anioId}/${comisionId}`)
                .then(response => response.json())
                .then(data => {
                    data.materias.forEach(materia => {
                        const div = document.createElement('div');
                        div.classList.add('form-check');

                        const checkbox = document.createElement('input');
                        checkbox.type = 'checkbox';
                        checkbox.name = 'materias[]';
                        checkbox.value = materia.id;
                        checkbox.classList.add('form-check-input');

                        const label = document.createElement('label');
                        label.textContent = materia.nombre;
                        label.classList.add('form-check-label');

                        div.appendChild(checkbox);
                        div.appendChild(label);
                        materiasContainer.appendChild(div);
                    });
                })
                .catch(error => console.error('Error al obtener las materias:', error));
        }
    });

    function limpiarSelect(select) {
        select.innerHTML = '<option value="">Seleccionar</option>';
    }
});
