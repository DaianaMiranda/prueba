import mysql.connector

class DatabaseConnection:
    @staticmethod
    def connect():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="asistencia"
        )

class Usuario:
    def __init__(self, id, nombre, apellido, dni, email, contraseña, tipo_usuario):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        self.contraseña = contraseña
        self.tipo_usuario = tipo_usuario

    @classmethod
    def verificar_usuario(cls, email, contraseña):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)
        
        query = "SELECT id, tipo_usuario FROM usuario WHERE email = %s AND contraseña = %s"
        cursor.execute(query, (email, contraseña))
        
        usuario = cursor.fetchone()
        cursor.close()
        db.close()

        if usuario:
            return cls(usuario['id'], None, None, None, email, None, usuario['tipo_usuario'])
        return None

class Alumno(Usuario):
    def __init__(self, id, nombre, apellido, dni, email, contraseña, id_carrera):
        super().__init__(id, nombre, apellido, dni, email, contraseña, 'alumno')
        self.id_carrera = id_carrera

    @classmethod
    def save_student(cls, nombre, apellido, dni, email, contraseña, carrera_id, anio_id, comision_id, materias):
        db = DatabaseConnection.connect()
        cursor = db.cursor()

        try:
            # Insertar en la tabla usuario
            cursor.execute("""
                INSERT INTO usuario (nombre, apellido, dni, email, contraseña, tipo_usuario)
                VALUES (%s, %s, %s, %s, %s, 'alumno')
            """, (nombre, apellido, dni, email, contraseña))
            db.commit()

            # Obtener el ID del usuario recién insertado
            usuario_id = cursor.lastrowid

            # Insertar en la tabla alumnos
            cursor.execute("""
                INSERT INTO alumnos (id_usuario, id_carrera, id_anio, id_comision)
                VALUES (%s, %s, %s, %s)
            """, (usuario_id, carrera_id, anio_id, comision_id))
            db.commit()

            # Obtener el ID del alumno recién insertado
            alumno_id = cursor.lastrowid

            # Insertar las materias del alumno en la tabla alumno_materias
            for materia_id in materias:
                cursor.execute("""
                    INSERT INTO alumno_materias (id_alumno, id_materia)
                    VALUES (%s, %s)
                """, (alumno_id, materia_id))
            db.commit()

        except Exception as e:
            print(f"Error al guardar el alumno: {e}")
            db.rollback()
        finally:
            cursor.close()
            db.close()


    @classmethod
    def get_id_alumno(cls, id_usuario):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)
        
        query = "SELECT id FROM alumnos WHERE id_usuario = %s"
        cursor.execute(query, (id_usuario,))
        alumno = cursor.fetchone()
        
        cursor.close()
        db.close()
        
        return alumno['id'] if alumno else None

    @classmethod
    def get_carreras(cls, id_usuario):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        query = """
        SELECT c.id, c.nombre 
        FROM carrera c
        JOIN alumnos al ON al.id_carrera = c.id
        WHERE al.id_usuario = %s
        """
        cursor.execute(query, (id_usuario,))
        carreras = cursor.fetchall()
        cursor.close()
        db.close()
        return carreras

    @classmethod
    def get_alumnos_por_materia(cls, carrera_id, materia_id):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        query = """
        SELECT al.id, u.nombre, u.apellido
        FROM alumnos al
        JOIN usuario u ON al.id_usuario = u.id
        JOIN alumno_materias am ON al.id = am.id_alumno
        WHERE al.id_carrera = %s AND am.id_materia = %s
        """
        cursor.execute(query, (carrera_id, materia_id))
        alumnos = cursor.fetchall()

        cursor.close()
        db.close()

        return alumnos



    @classmethod
    def get_asistencias_alumno(cls, alumno_id):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        try:
            query = """
            SELECT a.fecha, m.nombre AS materia, a.asistio
            FROM asistencia a
            JOIN materias m ON a.id_materia = m.id
            JOIN alumnos al ON a.id_alumno = al.id
            WHERE al.id = %s
            """
            cursor.execute(query, (alumno_id,))
            asistencias = cursor.fetchall()
            return asistencias
        except Exception as e:
            print(f"Error al obtener las asistencias del alumno: {e}")
            return []
        finally:
            cursor.close()
            db.close()

class Profesor(Usuario):

    def __init__(self, id, nombre, apellido, dni, email, contraseña, id_carrera):
        super().__init__(id, nombre, apellido, dni, email, contraseña, 'profesor')
        self.id_carrera = id_carrera

    @classmethod
    def get_carreras_del_profesor(cls, id_usuario):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        query = """
        SELECT c.id, c.nombre
        FROM profesores p
        JOIN profesor_carrera pc ON p.id = pc.id_profesor
        JOIN carrera c ON pc.id_carrera = c.id
        WHERE p.id_usuario = %s
        """
        cursor.execute(query, (id_usuario,))
        carreras = cursor.fetchall()

        cursor.close()
        db.close()
        return carreras
    
    @classmethod
    def get_anios_profesor(cls, id_usuario, id_carrera):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        query = """
        SELECT DISTINCT a.id, a.nombre
        FROM profesor_materias pm
        JOIN carrera_materias cm ON pm.id_materia = cm.id_materia
        JOIN anios a ON cm.id_anio = a.id
        JOIN profesores p ON pm.id_profesor = p.id
        WHERE p.id_usuario = %s AND cm.id_carrera = %s
        """

        cursor.execute(query, (id_usuario, id_carrera))
        anios = cursor.fetchall()
        cursor.close()
        db.close()
        return anios

    @classmethod
    def get_comisiones_profesor(cls, id_usuario, id_carrera, id_anio):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        query = """
        SELECT DISTINCT c.id, c.nombre
        FROM profesor_materias pm
        JOIN carrera_materias cm ON pm.id_materia = cm.id_materia
        JOIN comisiones c ON cm.id_comision = c.id
        JOIN profesores p ON pm.id_profesor = p.id
        WHERE p.id_usuario = %s AND cm.id_carrera = %s AND cm.id_anio = %s
        """

        cursor.execute(query, (id_usuario, id_carrera, id_anio))
        comisiones = cursor.fetchall()
        cursor.close()
        db.close()
        return comisiones

    @classmethod
    def get_materias_profesor(cls, id_usuario, id_carrera, id_anio, id_comision):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        query = """
        SELECT m.id, m.nombre
        FROM profesor_materias pm
        JOIN materias m ON pm.id_materia = m.id
        JOIN carrera_materias cm ON pm.id_materia = cm.id_materia
        JOIN profesores p ON pm.id_profesor = p.id
        WHERE p.id_usuario = %s
        AND cm.id_carrera = %s
        AND cm.id_anio = %s
        AND cm.id_comision = %s
        """

        cursor.execute(query, (id_usuario, id_carrera, id_anio, id_comision))
        materias = cursor.fetchall()
        cursor.close()
        db.close()
        return materias

    @classmethod
    def get_asistencias_por_materia_y_fecha(cls, materia_id, fecha):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        query = """
        SELECT u.nombre, u.apellido, a.asistio
        FROM asistencia a
        JOIN alumnos al ON a.id_alumno = al.id
        JOIN usuario u ON al.id_usuario = u.id
        WHERE a.id_materia = %s AND a.fecha = %s
        """
        cursor.execute(query, (materia_id, fecha))
        asistencias = cursor.fetchall()

        cursor.close()
        db.close()

        return asistencias

    

    @classmethod
    def get_justificaciones_por_materia_y_fecha(cls, materia_id, fecha):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        query = """
        SELECT u.nombre, u.apellido, j.fecha, j.causa, j.certificado
        FROM justificacion_inasistencia j
        JOIN alumnos al ON j.id_alumno = al.id
        JOIN usuario u ON al.id_usuario = u.id
        WHERE j.id_materia = %s AND j.fecha = %s
        """
        cursor.execute(query, (materia_id, fecha))
        justificaciones = cursor.fetchall()

        cursor.close()
        db.close()

        return justificaciones

    @classmethod
    def save_professor(cls, nombre, apellido, dni, email, contraseña, carrera_id, materias):
        db = DatabaseConnection.connect()
        cursor = db.cursor()

        try:
            cursor.execute("""
                INSERT INTO usuario (nombre, apellido, dni, email, contraseña, tipo_usuario)
                VALUES (%s, %s, %s, %s, %s, 'profesor')
            """, (nombre, apellido, dni, email, contraseña))
            db.commit()

            id_usuario = cursor.lastrowid

            cursor.execute("""
                INSERT INTO profesores (id_usuario, id_carrera)
                VALUES (%s, %s)
            """, (id_usuario, carrera_id))
            db.commit()

            profesor_id = cursor.lastrowid

            for materia_id in materias:
                cursor.execute("""
                    INSERT INTO profesor_materias (id_profesor, id_materia)
                    VALUES (%s, %s)
                """, (profesor_id, materia_id))
            db.commit()

        except Exception as e:
            print(f"Error al guardar el profesor: {e}")
            db.rollback()
            raise
        finally:
            cursor.close()
            db.close()

    
class Superadmin(Usuario):
    def __init__(self, id, nombre, apellido, dni, email, contraseña):
        super().__init__(id, nombre, apellido, dni, email, contraseña, 'superadmin')

        

    @classmethod
    def cambiar_porcentaje_asistencia(cls, nuevo_porcentaje):
        db = DatabaseConnection.connect()
        cursor = db.cursor()

        try:
            cursor.execute("UPDATE configuracion SET porcentaje_asistencia_critica = %s", (nuevo_porcentaje,))
            db.commit()
        except Exception as e:
            print(f"Error al cambiar el porcentaje de asistencia crítica: {e}")
            db.rollback()
        finally:
            cursor.close()
            db.close()

class Carrera:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


    @classmethod
    def get_anios(cls, id_carrera):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        query = """
        SELECT DISTINCT a.id, a.nombre
        FROM carrera_anios_comisiones cac
        JOIN anios a ON cac.id_anios = a.id
        WHERE cac.id_carrera = %s
        """
        cursor.execute(query, (id_carrera,))
        anios = cursor.fetchall()

        cursor.close()
        db.close()
        return {'años': anios}


    @classmethod
    def get_comisiones(cls, id_carrera, id_anio):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        query = """
        SELECT c.id, c.nombre
        FROM carrera_anios_comisiones cac
        JOIN comisiones c ON cac.id_comisiones = c.id
        WHERE cac.id_carrera = %s AND cac.id_anios = %s
        """
        cursor.execute(query, (id_carrera, id_anio))
        comisiones = cursor.fetchall()

        cursor.close()
        db.close()
        return {'comisiones': comisiones}

    @classmethod
    def get_materias(cls, id_carrera, id_anio, id_comision):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        query = """
        SELECT m.id, m.nombre
        FROM carrera_materias cm
        JOIN materias m ON cm.id_materia = m.id
        WHERE cm.id_carrera = %s AND cm.id_anio = %s AND cm.id_comision = %s
        """
        cursor.execute(query, (id_carrera, id_anio, id_comision))
        materias = cursor.fetchall()

        cursor.close()
        db.close()
        return {'materias': materias}

    @classmethod
    def get_all(cls):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        query = "SELECT id, nombre FROM carrera"
        cursor.execute(query)
        carreras = cursor.fetchall()

        cursor.close()
        db.close()
        return carreras

  


class Materia:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    @classmethod
    def get_materias_por_carrera_anio_y_comision(cls, carrera_id, anio_id, comision_id):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        try:
            query = """
            SELECT m.id, m.nombre
            FROM materias m
            JOIN carrera_materias cm ON m.id = cm.id_materia
            WHERE cm.id_carrera = %s AND cm.id_anio = %s AND cm.id_comision = %s
            """
            cursor.execute(query, (carrera_id, anio_id, comision_id))
            materias = cursor.fetchall()
            return [{"id": materia["id"], "nombre": materia["nombre"]} for materia in materias]
        except Exception as e:
            print(f"Error al obtener las materias: {e}")
            return []
        finally:
            cursor.close()
            db.close()

    @classmethod
    def get_nombre_materia(cls, materia_id):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        query = "SELECT nombre FROM materias WHERE id = %s"
        cursor.execute(query, (materia_id,))
        materia = cursor.fetchone()

        cursor.close()
        db.close()

        return materia['nombre'] if materia else "Desconocida"

class Comision:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    @classmethod
    def get_comisiones_por_carrera_y_anio(cls, carrera_id, anio_id):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        try:
            query = """
            SELECT DISTINCT c.id, c.nombre
            FROM carrera_anios_comisiones cac
            JOIN comisiones c ON cac.id_comisiones = c.id
            WHERE cac.id_carrera = %s AND cac.id_anios = %s
            """
            cursor.execute(query, (carrera_id, anio_id))
            comisiones = cursor.fetchall()
            return [{"id": comision["id"], "nombre": comision["nombre"]} for comision in comisiones]  # Devuelve un array de objetos
        except Exception as e:
            print(f"Error al obtener las comisiones: {e}")
            return []  # Devuelve un array vacío en caso de error
        finally:
            cursor.close()
            db.close()
class Anio:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    @classmethod
    def get_anios_por_carrera(cls, carrera_id):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        try:
            query = """
            SELECT DISTINCT a.id, a.nombre
            FROM carrera_anios_comisiones cac
            JOIN anios a ON cac.id_anios = a.id
            WHERE cac.id_carrera = %s
            """
            cursor.execute(query, (carrera_id,))
            anios = cursor.fetchall()
            return [{"id": anio["id"], "nombre": anio["nombre"]} for anio in anios]  # Devuelve un array de objetos
        except Exception as e:
            print(f"Error al obtener los años: {e}")
            return []  # Devuelve un array vacío en caso de error
        finally:
            cursor.close()
            db.close()

class Asistencia:
    def __init__(self, id, id_alumno, id_materia, fecha, id_comision, id_anio, asistio):
        self.id = id
        self.id_alumno = id_alumno
        self.id_materia = id_materia
        self.fecha = fecha
        self.id_comision = id_comision
        self.id_anio = id_anio
        self.asistio = asistio

    @classmethod
    def guardar_asistencia(cls, id_alumno, id_materia, id_comision, id_anio, fecha, asistio):
        db = DatabaseConnection.connect()
        cursor = db.cursor()

        query = """
        INSERT INTO asistencia (id_alumno, id_materia, id_comision, id_anio, fecha, asistio)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (id_alumno, id_materia, id_comision, id_anio, fecha, asistio))
        db.commit()

        cursor.close()
        db.close()

    @classmethod
    def existe_asistencia_para_hoy(cls, id_materia, id_comision, id_anio, fecha):
        db = DatabaseConnection.connect()
        cursor = db.cursor()

        query = """
        SELECT COUNT(*)
        FROM asistencia
        WHERE id_materia = %s AND id_comision = %s AND id_anio = %s AND fecha = %s
        """
        cursor.execute(query, (id_materia, id_comision, id_anio, fecha))
        (existe,) = cursor.fetchone()

        cursor.close()
        db.close()

        return existe > 0


    @classmethod
    def get_asistencia_por_materia(cls, materia_id, fecha, periodo):
        db = DatabaseConnection.connect()
        cursor = db.cursor(dictionary=True)

        try:
            query = """
            SELECT 
                u.nombre, 
                u.apellido, 
                a.fecha, 
                a.asistio,
                COUNT(CASE WHEN a.asistio = 1 THEN 1 END) AS asistencias_presente
            FROM asistencia a
            JOIN alumnos al ON a.id_alumno = al.id
            JOIN usuario u ON al.id_usuario = u.id
            WHERE a.id_materia = %s
            """

            if periodo == 'dia':
                query += " AND a.fecha = %s"
                cursor.execute(query + " GROUP BY a.id_alumno", (materia_id, fecha))
            elif periodo == 'semana':
                query += " AND YEARWEEK(a.fecha, 1) = YEARWEEK(%s, 1)"
                cursor.execute(query + " GROUP BY a.id_alumno", (materia_id, fecha))
            elif periodo == 'mes':
                query += " AND MONTH(a.fecha) = MONTH(%s) AND YEAR(a.fecha) = YEAR(%s)"
                cursor.execute(query + " GROUP BY a.id_alumno", (materia_id, fecha, fecha))
            else:
                cursor.execute(query + " GROUP BY a.id_alumno", (materia_id,))

            asistencias = cursor.fetchall()
            return asistencias
        except Exception as e:
            print(f"Error al obtener la asistencia por materia: {e}")
            return []
        finally:
            cursor.close()
            db.close()

class JustificacionInasistencia:
    def __init__(self, id, id_alumno, id_materia, causa, fecha, certificado):
        self.id = id
        self.id_alumno = id_alumno
        self.id_materia = id_materia
        self.causa = causa
        self.fecha = fecha
        self.certificado = certificado

    @classmethod
    def guardar_justificacion(cls, id_alumno, id_materia, causa, fecha, certificado):
        db = DatabaseConnection.connect()
        cursor = db.cursor()

        try:
            cursor.execute("""
                INSERT INTO asistencia.justificacion_inasistencia (id_alumno, id_materia, causa, fecha, certificado)
                VALUES (%s, %s, %s, %s, %s)
            """, (id_alumno, id_materia, causa, fecha, certificado))
            db.commit()
        except Exception as e:
            print(f"Error al guardar la justificación: {e}")
            db.rollback()
        finally:
            cursor.close()
            db.close()