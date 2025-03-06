from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from models import Usuario, Alumno, Profesor, Superadmin, Carrera, Materia, Comision, Anio, Asistencia, JustificacionInasistencia
from datetime import datetime
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html') 
    
    email = request.form['email']
    password = request.form['password']

    usuario = Usuario.verificar_usuario(email, password)

    if usuario:
        session['user_id'] = usuario.id
        session['role'] = usuario.tipo_usuario

        if session['role'] == 'alumno':
            return redirect(url_for('alumno'))
        elif session['role'] == 'profesor':
            return redirect(url_for('profesor'))
        elif session['role'] == 'superadmin':
            return redirect(url_for('superadmin_dashboard'))

    flash('Correo, contraseña o rol incorrectos.')
    return redirect(url_for('home'))


@app.route('/alumno', methods=['GET'])
def alumno():
    if 'user_id' in session:
        alumno_id = session['user_id']
        asistencias = Alumno.get_asistencias_alumno(alumno_id)
        return render_template('alumno.html', asistencias=asistencias)
    return redirect(url_for('home'))

@app.route('/profesor', methods=['GET'])
def profesor():
    if 'user_id' in session and session['role'] == 'profesor':
        return render_template('profesor.html')
    return redirect(url_for('home'))

@app.route('/tomar_asistencia', methods=['GET', 'POST'])
def tomar_asistencia():
    if request.method == 'GET':
        profesor_id = session.get('id_usuario')
        if not profesor_id:
            flash('Debes iniciar sesión como profesor.')
            return redirect(url_for('login'))

        carreras = Profesor.get_carreras_del_profesor(profesor_id)

        return render_template('tomar_asistencia.html', carreras=carreras)

    # POST para avanzar a seleccionar alumnos
    carrera_id = request.form['carrera']
    anio_id = request.form['anio']
    comision_id = request.form['comision']
    materia_id = request.form['materia']
    fecha = datetime.date.today()

    return redirect(url_for('listado_alumnos', carrera_id=carrera_id, anio_id=anio_id, comision_id=comision_id, materia_id=materia_id, fecha=fecha))


@app.route('/get_anios_profesor/<int:carrera_id>')
def get_anios_profesor(carrera_id):
    profesor_id = session['user_id']
    anios = Profesor.get_anios_profesor(profesor_id, carrera_id)
    return jsonify(anios)


@app.route('/get_comisiones_profesor/<int:carrera_id>/<int:anio_id>')
def get_comisiones_profesor(carrera_id, anio_id):
    profesor_id = session['user_id']
    comisiones = Profesor.get_comisiones_profesor(profesor_id, carrera_id, anio_id)
    return jsonify(comisiones)


@app.route('/get_materias_profesor/<int:carrera_id>/<int:anio_id>/<int:comision_id>')
def get_materias_profesor(carrera_id, anio_id, comision_id):
    profesor_id = session['user_id']
    materias = Profesor.get_materias_profesor(profesor_id, carrera_id, anio_id, comision_id)
    return jsonify(materias)


@app.route('/profesor/listado_alumnos', methods=['GET', 'POST'])
def listado_alumnos():
    if 'user_id' not in session or session['role'] != 'profesor':
        return redirect(url_for('home'))

    if request.method == 'POST':
        materia_id = session['asistencia_materia']
        carrera_id = session['asistencia_carrera']
        comision_id = session['asistencia_comision']
        anio_id = session['asistencia_anio']
        fecha = datetime.now().date()

        # Valida que no se haya tomado ya la asistencia para esta materia,comision,anio en esta fecha
        if Asistencia.existe_asistencia_para_hoy(materia_id, comision_id, anio_id, fecha):
            flash('La asistencia para esta materia, comisión y año ya fue tomada hoy.')
            return redirect(url_for('profesor'))

        for alumno_id in request.form:
            if alumno_id.startswith('asistencia_'):
                real_id = alumno_id.split('_')[1]
                asistio = (request.form[alumno_id] == 'presente')
                Asistencia.guardar_asistencia(real_id, materia_id, comision_id, anio_id, fecha, asistio)

        flash('Asistencia guardada correctamente.')
        return redirect(url_for('profesor'))

    carrera_id = session['asistencia_carrera']
    materia_id = session['asistencia_materia']

    alumnos = Alumno.get_alumnos_por_materia(carrera_id, materia_id)

    for alumno in alumnos:
        alumno['apellido_nombre'] = f"{alumno['apellido']}, {alumno['nombre']}"

    materia = Materia.get_nombre_materia(materia_id)
    fecha_actual = datetime.now().strftime('%Y-%m-%d')

    return render_template('listado_alumnos.html', alumnos=alumnos, materia=materia, fecha_actual=fecha_actual)

@app.route('/profesor/ver_asistencia', methods=['GET', 'POST'])
def ver_asistencia():
    profesor_id = session['user_id']
    carreras = Profesor.get_carreras(profesor_id)

    if request.method == 'POST':
        session['asistencia_carrera'] = request.form['carrera']
        session['asistencia_anio'] = request.form['anio']
        session['asistencia_comision'] = request.form['comision']
        session['asistencia_materia'] = request.form['materia']
        return redirect(url_for('listado_asistencia'))

    return render_template('ver_asistencia.html', carreras=carreras)


@app.route('/profesor/listado_asistencia')
def listado_asistencia():
    filtro = request.args.get('filtro', 'semana')

    materia_id = session['asistencia_materia']
    comision_id = session['asistencia_comision']
    anio_id = session['asistencia_anio']

    alumnos = Asistencia.get_asistencia_por_materia(materia_id, comision_id, anio_id, filtro)
    materia = Materia.get_nombre_materia(materia_id)

    return render_template('listado_asistencia.html', alumnos=alumnos, materia=materia, filtro=filtro)


@app.route('/profesor/ver_justificaciones', methods=['GET'])
def ver_justificaciones():
    if 'user_id' in session and session['role'] == 'profesor':
        profesor_id = session['user_id']
        materias = Profesor.get_materias_del_profesor(profesor_id)

        materia_id = request.args.get('materia')
        fecha = request.args.get('fecha')

        justificaciones = []
        if materia_id and fecha:
            justificaciones = Profesor.get_justificaciones_por_materia_y_fecha(materia_id, fecha)

        return render_template('ver_justificaciones.html', materias=materias, justificaciones=justificaciones)

    return redirect(url_for('home'))



@app.route('/superadmin_dashboard')
def superadmin_dashboard():
    if 'user_id' in session and session['role'] == 'superadmin':
        return render_template('superadmin.html')
    return redirect(url_for('home'))

@app.route('/cargar_alumno', methods=['GET', 'POST'])
def cargar_alumno():
    if 'user_id' in session and session['role'] == 'superadmin':
        if request.method == 'POST':
            # Procesar el formulario para guardar un alumno
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            dni = request.form['dni']
            email = request.form['email']
            contrasena = request.form['contrasena']
            carrera_id = request.form['carrera']
            anio_id = request.form['anio']
            comision_id = request.form['comision']
            materias = request.form.getlist('materias[]')

            # Guardar el alumno en la base de datos
            Alumno.save_student(nombre, apellido, dni, email, contrasena, carrera_id, anio_id, comision_id, materias)
            flash('Alumno guardado exitosamente.')
            return redirect(url_for('superadmin_dashboard'))

        # Si es un GET, mostrar el formulario para cargar un alumno
        carreras = Carrera.get_carreras()
        return render_template('cargar_alumno.html', carreras=carreras)
    return redirect(url_for('home'))

@app.route('/get_anios/<int:carrera_id>')
def get_anios(carrera_id):
    return jsonify(Carrera.get_anios(carrera_id))

@app.route('/get_comisiones/<int:carrera_id>/<int:anio_id>')
def get_comisiones(carrera_id, anio_id):
    return jsonify(Carrera.get_comisiones(carrera_id, anio_id))

@app.route('/get_materias/<int:carrera_id>/<int:anio_id>/<int:comision_id>')
def get_materias(carrera_id, anio_id, comision_id):
    return jsonify(Carrera.get_materias(carrera_id, anio_id, comision_id))


@app.route('/cargar_profesor', methods=['GET', 'POST'])
def cargar_profesor():
    if request.method == 'GET':
        carreras = Carrera.get_all()
        return render_template('cargar_profesor.html', carreras=carreras)

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['dni']
    email = request.form['email']
    contrasena = request.form['contrasena']
    carrera_id = request.form['carrera']
    materias = request.form.getlist('materias[]')

    Profesor.save_professor(nombre, apellido, dni, email, contrasena, carrera_id, materias)

    flash('Profesor cargado correctamente.')
    return redirect(url_for('superadmin_dashboard'))


@app.route('/cambiar_porcentaje_asistencia', methods=['POST'])
def cambiar_porcentaje_asistencia():
    if 'user_id' in session and session['role'] == 'superadmin':
        nuevo_porcentaje = request.form['porcentaje']
        Superadmin.cambiar_porcentaje_asistencia(nuevo_porcentaje)
        flash('Porcentaje de asistencia crítica actualizado.')
        return redirect(url_for('superadmin_dashboard'))
    return redirect(url_for('home'))

# @app.route('/cargar_justificativo', methods=['GET', 'POST'])
# def cargar_justificativo():
#     if 'user_id' in session:
#         if request.method == 'POST':
#             user_id = session['user_id']
#             alumno_id = Alumno.get_id_alumno(user_id)

#             carrera_id = request.form['carrera']
#             anio_id = request.form['anio']
#             comision_id = request.form['comision']
#             materia_id = request.form['materia']
#             causa = request.form['causa']
#             fecha = request.form['fecha']
#             certificado = request.files['certificado']

#             if certificado and allowed_file(certificado.filename):
#                 filename = secure_filename(certificado.filename)
#                 archivo_path = os.path.join(UPLOAD_FOLDER, f"{alumno_id}_{filename}")
#                 certificado.save(archivo_path)

#                 JustificacionInasistencia.guardar_justificacion(alumno_id, materia_id, causa, fecha, archivo_path)
#                 flash('Justificativo cargado correctamente y notificado al profesor.')
#             else:
#                 flash('El archivo no es válido. Solo se permiten archivos PDF, JPG, JPEG o PNG.')

#             return redirect(url_for('alumno'))

#         carreras = Carrera.get_carreras()
#         return render_template('cargar_justificativo.html', carreras=carreras)
#     return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada correctamente.')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)