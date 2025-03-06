function cargarOpciones(url, selectId) {
    fetch(url)
        .then(res => res.json())
        .then(data => {
            const select = document.getElementById(selectId);
            select.innerHTML = '<option value="">Seleccionar</option>';
            data.forEach(item => {
                const option = document.createElement('option');
                option.value = item.id;
                option.textContent = item.nombre;
                select.appendChild(option);
            });
        });
}

document.getElementById('carrera').addEventListener('change', () => {
    const carreraId = document.getElementById('carrera').value;
    cargarOpciones(`/get_anios/${carreraId}`, 'anio');
});

document.getElementById('anio').addEventListener('change', () => {
    const carreraId = document.getElementById('carrera').value;
    const anioId = document.getElementById('anio').value;
    cargarOpciones(`/get_comisiones/${carreraId}/${anioId}`, 'comision');
});

document.getElementById('comision').addEventListener('change', () => {
    const carreraId = document.getElementById('carrera').value;
    const anioId = document.getElementById('anio').value;
    const comisionId = document.getElementById('comision').value;
    cargarOpciones(`/get_materias/${carreraId}/${anioId}/${comisionId}`, 'materia');
});




// // Función genérica para cargar opciones en un select
// function cargarOpciones(url, selectId, placeholder) {
//     fetch(url)
//         .then(response => response.json())
//         .then(data => {
//             const select = document.getElementById(selectId);
//             select.innerHTML = `<option value="">${placeholder}</option>`;
//             data.forEach(item => {
//                 const option = document.createElement('option');
//                 option.value = item.id;
//                 option.textContent = item.nombre;
//                 select.appendChild(option);
//             });
//         })
//         .catch(error => {
//             console.error(`Error cargando opciones para ${selectId}:`, error);
//         });
// }

// // Cargar años cuando se selecciona una carrera
// document.getElementById('carrera').addEventListener('change', function() {
//     const carreraId = this.value;
//     cargarOpciones(`/get_anios/${carreraId}`, 'anio', 'Seleccionar Año');
// });

// // Cargar comisiones cuando se selecciona un año
// document.getElementById('anio').addEventListener('change', function() {
//     const carreraId = document.getElementById('carrera').value;
//     const anioId = this.value;
//     cargarOpciones(`/get_comisiones/${carreraId}/${anioId}`, 'comision', 'Seleccionar Comisión');
// });

// // Cargar materias cuando se selecciona una comisión
// document.getElementById('comision').addEventListener('change', function() {
//     const carreraId = document.getElementById('carrera').value;
//     const anioId = document.getElementById('anio').value;
//     const comisionId = this.value;
//     cargarOpciones(`/get_materias/${carreraId}/${anioId}/${comisionId}`, 'materia', 'Seleccionar Materia');
// });

// // Establecer la fecha actual
// const fechaActual = new Date();
// const año = fechaActual.getFullYear();
// const mes = (fechaActual.getMonth() + 1).toString().padStart(2, '0');
// const dia = fechaActual.getDate().toString().padStart(2, '0');
// const fechaFormateada = `${año}-${mes}-${dia}`;
// document.getElementById('fecha').value = fechaFormateada;