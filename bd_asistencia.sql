-- Crear esquema si no existe
CREATE SCHEMA IF NOT EXISTS `asistencia` DEFAULT CHARACTER SET utf8mb4;
USE `asistencia`;

-- Tabla Usuario (Base para Alumnos, Profesores y Superadmin)
CREATE TABLE IF NOT EXISTS usuario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(20) UNIQUE NOT NULL,  -- DNI se incluye en la tabla usuario
    email VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(100) NOT NULL,
    tipo_usuario ENUM('alumno', 'profesor', 'superadmin') NOT NULL
);

-- Tabla Carrera
CREATE TABLE IF NOT EXISTS carrera (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla Años
CREATE TABLE IF NOT EXISTS anios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla Comisiones
CREATE TABLE IF NOT EXISTS comisiones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla Alumnos (Relacionada con Usuario)
CREATE TABLE IF NOT EXISTS alumnos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_carrera INT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE,
    FOREIGN KEY (id_carrera) REFERENCES carrera(id) ON DELETE SET NULL
);

-- Tabla Profesores (Relacionada con Usuario)
CREATE TABLE IF NOT EXISTS profesores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_carrera INT,  -- Relación con la carrera, en caso de que sea necesario
    FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE,
    FOREIGN KEY (id_carrera) REFERENCES carrera(id) ON DELETE SET NULL
);

-- Tabla Superadmin (Relacionada con Usuario, ahora con campo id)
CREATE TABLE IF NOT EXISTS superadmin (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- Se agrega el campo id como PK
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE
);

-- Tabla Carrera_Anios_Comisiones
CREATE TABLE IF NOT EXISTS carrera_anios_comisiones (
    id_carrera INT,
    id_anios INT,
    id_comisiones INT,
    PRIMARY KEY (id_carrera, id_anios, id_comisiones),
    FOREIGN KEY (id_carrera) REFERENCES carrera(id) ON DELETE CASCADE,
    FOREIGN KEY (id_anios) REFERENCES anios(id) ON DELETE CASCADE,
    FOREIGN KEY (id_comisiones) REFERENCES comisiones(id) ON DELETE CASCADE
);

-- Tabla Materias
CREATE TABLE IF NOT EXISTS materias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
    
);

-- Tabla Carrera_Materias (Relación carrera, año, comisión y materia)
CREATE TABLE IF NOT EXISTS carrera_materias (
    id_carrera INT,
    id_anio INT,
    id_comision INT,
    id_materia INT,
    PRIMARY KEY (id_carrera, id_anio, id_comision, id_materia),
    FOREIGN KEY (id_carrera) REFERENCES carrera(id) ON DELETE CASCADE,
    FOREIGN KEY (id_anio) REFERENCES anios(id) ON DELETE CASCADE,
    FOREIGN KEY (id_comision) REFERENCES comisiones(id) ON DELETE CASCADE,
    FOREIGN KEY (id_materia) REFERENCES materias(id) ON DELETE CASCADE
);

-- Tabla Profesor_Carrera (Relación de profesores con carreras)
CREATE TABLE IF NOT EXISTS profesor_carrera (
    id_profesor INT,
    id_carrera INT,
    PRIMARY KEY (id_profesor, id_carrera),
    FOREIGN KEY (id_profesor) REFERENCES profesores(id) ON DELETE CASCADE,
    FOREIGN KEY (id_carrera) REFERENCES carrera(id) ON DELETE CASCADE
);

-- Tabla `asistencia`
CREATE TABLE IF NOT EXISTS `asistencia` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `id_alumno` INT(11) NOT NULL,
  `id_materia` INT(11) NOT NULL,
  `fecha` DATE NOT NULL,
  `id_comision` INT(11) NOT NULL,
  `id_anio` INT(11) NOT NULL,
  `asistio` TINYINT(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `unique_asistencia` (`id_alumno`, `id_materia`, `fecha`, `id_comision`, `id_anio`),
  INDEX `fk_asistencia_alumno` (`id_alumno`),
  INDEX `fk_asistencia_materia` (`id_materia`),
  INDEX `fk_asistencia_comision` (`id_comision`),
  INDEX `fk_asistencia_anio` (`id_anio`),
  CONSTRAINT `fk_asistencia_alumno`
    FOREIGN KEY (`id_alumno`) REFERENCES `alumnos` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `fk_asistencia_materia`
    FOREIGN KEY (`id_materia`) REFERENCES `materias` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `fk_asistencia_comision`
    FOREIGN KEY (`id_comision`) REFERENCES `comisiones` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `fk_asistencia_anio`
    FOREIGN KEY (`id_anio`) REFERENCES `anios` (`id`)
    ON DELETE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;



CREATE TABLE profesor_materias (
    id_profesor INT,
    id_materia INT,
    PRIMARY KEY (id_profesor, id_materia),
    FOREIGN KEY (id_profesor) REFERENCES profesores(id) ON DELETE CASCADE,
    FOREIGN KEY (id_materia) REFERENCES materias(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS alumno_materias (
    id_alumno INT,
    id_materia INT,
    PRIMARY KEY (id_alumno, id_materia),
    FOREIGN KEY (id_alumno) REFERENCES alumnos(id) ON DELETE CASCADE,
    FOREIGN KEY (id_materia) REFERENCES materias(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS asistencia.justificacion_inasistencia (
  id INT AUTO_INCREMENT NOT NULL,
  id_alumno INT NOT NULL,
  id_materia INT NOT NULL,
  causa VARCHAR(255) NOT NULL,
  fecha DATE NOT NULL,
  certificado LONGBLOB,  -- Para almacenar el archivo de certificado en formato binario (PDF o imagen)
  PRIMARY KEY (id),
  UNIQUE (id_alumno, id_materia, fecha),
  CONSTRAINT fk_justificacion_alumno
    FOREIGN KEY (id_alumno) REFERENCES asistencia.alumnos (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_justificacion_materia
    FOREIGN KEY (id_materia) REFERENCES asistencia.materias (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;
