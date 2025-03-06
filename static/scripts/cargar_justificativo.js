// Función genérica para cargar opciones en un select
function cargarOpciones(url, selectId, placeholder) {
    fetch(url)
        .then(response => response.json())
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
            console.error(`Error cargando opciones para ${selectId}:`, error);
        });
}

// Obtener el valor del usuario desde el campo oculto en el HTML
function getUsuarioId() {
    return document.getElementById("usuario-id")?.value || "default_user_id"; // Valor por defecto si no está disponible
}

// Cargar los años disponibles basados en la carrera seleccionada
function cargarAnos() {
    const carreraId = document.getElementById('carrera').value;
    const usuarioId = getUsuarioId();

    if (!carreraId || !usuarioId) return;

    cargarOpciones(`/get_anios/${carreraId}/${usuarioId}`, 'anio', 'Seleccionar Año');
}

// Cargar las comisiones disponibles basadas en carrera y año seleccionados
function cargarComisiones() {
    const carreraId = document.getElementById('carrera').value;
    const anioId = document.getElementById('anio').value;
    const usuarioId = getUsuarioId();

    if (!carreraId || !anioId || !usuarioId) return;

    cargarOpciones(`/get_comisiones/${carreraId}/${anioId}/${usuarioId}`, 'comision', 'Seleccionar Comisión');
}

// Cargar las materias disponibles basadas en carrera, año y comisión seleccionados
function cargarMaterias() {
    const carreraId = document.getElementById('carrera').value;
    const anioId = document.getElementById('anio').value;
    const comisionId = document.getElementById('comision').value;
    const usuarioId = getUsuarioId();

    if (!carreraId || !anioId || !comisionId || !usuarioId) return;

    cargarOpciones(`/get_materias/${carreraId}/${anioId}/${comisionId}/${usuarioId}`, 'materia', 'Seleccionar Materia');
}

// Asignar los eventos de cambio a los selectores
document.getElementById('carrera').addEventListener('change', cargarAnos);
document.getElementById('anio').addEventListener('change', cargarComisiones);
document.getElementById('comision').addEventListener('change', cargarMaterias);