INSERT INTO usuario (nombre, apellido, dni, email, contraseña, tipo_usuario) VALUES 
('Juan', 'Pérez', '1234', '1234@example.com', '1234', 'superadmin');


INSERT INTO carrera (id, nombre) VALUES 
(1, 'Analista Funcional'),
(2, 'Técnico en Infraestructura'),
(3, 'Desarrollador de Software');


INSERT INTO anios (id, nombre) VALUES 
(1, '1° Año'),
(2, '2° Año'),
(3, '3° Año');


INSERT INTO comisiones (id, nombre) VALUES 
(1, 'Primera'),
(2, 'Segunda'),
(3, 'Tercera');


INSERT INTO carrera_anios_comisiones (id_carrera, id_anios, id_comisiones) VALUES 
-- Analista Funcional
(1, 1, 1), (1, 1, 2), (1, 1, 3),
(1, 2, 1), (1, 2, 2), (1, 2, 3),
(1, 3, 1), (1, 3, 2), (1, 3, 3),

-- Técnico en Infraestructura
(2, 1, 1), (2, 1, 2), (2, 1, 3),
(2, 2, 1), (2, 2, 2), (2, 2, 3),
(2, 3, 1), (2, 3, 2), (2, 3, 3),

-- Desarrollador de Software
(3, 1, 1), (3, 1, 2), (3, 1, 3),
(3, 2, 1), (3, 2, 2), (3, 2, 3),
(3, 3, 1), (3, 3, 2), (3, 3, 3);


-- Materias para Analista Funcional (carrera_id = 1)
INSERT INTO materias (id, nombre, id_profesor) VALUES 
-- Año 1
(1, 'Comunicacion', NULL),
(2, 'UDI I', NULL),
(3, 'Matematicas', NULL),
(4, 'Ingles Tecnico I', NULL),
(5, 'Psicologia de las Organizaciones', NULL),
(6, 'Modelos de Negocios', NULL),
(7, 'Arquitectura de las Computadoras', NULL),
(8, 'Gestion de Software I', NULL),
(9, 'Analistas de Sistemas Organizacionales', NULL),

-- Año 2

(10, 'Problematicas Socio Contemporaneas', NULL),
(11, 'UDI II', NULL),
(12, 'Ingles Tecnico II', NULL),
(13, 'Estadisticas', NULL),
(14, 'Innovacion y Desarrollo Emprendedor', NULL),
(15, 'Gestion de Software II', NULL),
(16, 'Estrategia de Negocios', NULL),
(17, 'Desarrollo de Sistemas', NULL),
(18, 'Practica Profesionalizante I', NULL),

-- Año 3

(19, 'Etica y Responsabilidad Social', NULL),
(20, 'Derecho y Legislacion Laboral', NULL),
(21, 'Redes y Comunicaciones', NULL),
(22, 'Seguridad de los Sistemas', NULL),
(23, 'SBase de Datos', NULL),
(24, 'Sistema de Informaxion Organizacional', NULL),
(25, 'Desarrollo de Sistemas Web', NULL),
(26, 'Practica Profesionalizante II', NULL),

-- Materias para Técnico en Infraestructura (carrera_id = 2)
-- Año 1

(27, 'Comunicacion', NULL),
(28, 'UDI I', NULL),
(29, 'Matematicas', NULL),
(30, 'Fisica Aplicada a las Tecnologias de la Informacion', NULL),
(31, 'Administracion', NULL),
(32, 'Ingles Tecnico', NULL),
(33, 'Arquitectura de las Computadoras', NULL),
(34, 'Logica y Programacion', NULL),
(35, 'Infraestructura de Redes I', NULL),

-- Año 2


(36, 'Problematicas Socio Contemporaneas', NULL),
(37, 'UDI II', NULL),
(38, 'Estadisticas', NULL),
(39, 'Innovacion y Desarrollo Emprendedor', NULL),
(40, 'Sistenas Operativos', NULL),
(41, 'Algoritmos y Estructur De Datos', NULL),
(42, 'Base de Datos', NULL),
(43, 'Infraestructura de Redes II', NULL),
(44, 'Practica Profesionalizante I', NULL),

-- Año 3

(45, 'Etica y Responsabilidad Social', NULL),
(46, 'Derecho y Legislacion Laboral', NULL),
(47, 'Administracion de Base de Datos', NULL),
(48, 'Seguridad de los Sistemas', NULL),
(49, 'Integridad y Migracion de Daots', NULL),
(50, 'Administracion de Sistemas y Redes', NULL),
(51, 'Practica Profesionalizante II', NULL),

-- Materias para Desarrollador de Software (carrera_id = 3)
-- Año 1

(52, 'Comunicacion', NULL),
(53, 'UDI I', NULL),
(54, 'Matematicas', NULL),
(55, 'Ingles Tecnico I', NULL),
(56, 'Administracion', NULL),
(57, 'Tecnologia de la Informacion', NULL),
(58, 'Logica y Estructura de Datos', NULL),
(59, 'Ingenieria de Software I', NULL),
(60, 'Sistemas Operativos', NULL),

-- Año 2

(61, 'Problematicas Socio Contemporaneas', NULL),
(62, 'UDI II', NULL),
(63, 'Ingles Tecnico II', NULL),
(64, 'Innovacion y Desarrollo Emprendedor', NULL),
(65, 'Estadisticas', NULL),
(66, 'Programacion I', NULL),
(67, 'Ingenieria de Software II', NULL),
(68, 'Base de Datos I', NULL),
(69, 'Practica Profesionalizante I', NULL),

-- Año 3

(70, 'Etica y Responsabilidad Social', NULL),
(71, 'Derecho y Legislacion Laboral', NULL),
(72, 'Redes y Comunicacion', NULL),
(73, 'Programacion II', NULL),
(74, 'Gestion y Proyecto de Software', NULL),
(75, 'Base de Datos II', NULL),
(76, 'Practica Profesionalizante II', NULL);


-- Materias para Analista Funcional (carrera_id = 1)
-- Año 1
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(1, 1, 1, 1),  -- Comunicacion
(1, 1, 1, 2),  -- UDI I
(1, 1, 1, 3),  -- Matematicas
(1, 1, 1, 4),  -- Ingles Tecnico I
(1, 1, 1, 5),  -- Psicologia de las Organizaciones
(1, 1, 1, 6),  -- Modelos de Negocios
(1, 1, 1, 7),  -- Arquitectura de las Computadoras
(1, 1, 1, 8),  -- Gestion de Software I
(1, 1, 1, 9);  -- Analistas de Sistemas Organizacionales

-- Año 1, Comisión B
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(1, 1, 2, 1),
(1, 1, 2, 2),
(1, 1, 2, 3),
(1, 1, 2, 4),
(1, 1, 2, 5),
(1, 1, 2, 6),
(1, 1, 2, 7),
(1, 1, 2, 8),
(1, 1, 2, 9);

-- Año 1, Comisión C
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(1, 1, 3, 1),
(1, 1, 3, 2),
(1, 1, 3, 3),
(1, 1, 3, 4),
(1, 1, 3, 5),
(1, 1, 3, 6),
(1, 1, 3, 7),
(1, 1, 3, 8),
(1, 1, 3, 9);

-- Año 2
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(1, 2, 1, 10), -- Problematicas Socio Contemporaneas
(1, 2, 1, 11), -- UDI II
(1, 2, 1, 12), -- Ingles Tecnico II
(1, 2, 1, 13), -- Estadisticas
(1, 2, 1, 14), -- Innovacion y Desarrollo Emprendedor
(1, 2, 1, 15), -- Gestion de Software II
(1, 2, 1, 16), -- Estrategia de Negocios
(1, 2, 1, 17), -- Desarrollo de Sistemas
(1, 2, 1, 18); -- Practica Profesionalizante I

-- Repetir para las comisiones B y C del Año 2
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(1, 2, 2, 10),
(1, 2, 2, 11),
(1, 2, 2, 12),
(1, 2, 2, 13),
(1, 2, 2, 14),
(1, 2, 2, 15),
(1, 2, 2, 16),
(1, 2, 2, 17),
(1, 2, 2, 18);

INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(1, 2, 3, 10),
(1, 2, 3, 11),
(1, 2, 3, 12),
(1, 2, 3, 13),
(1, 2, 3, 14),
(1, 2, 3, 15),
(1, 2, 3, 16),
(1, 2, 3, 17),
(1, 2, 3, 18);

-- Año 3
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(1, 3, 1, 19), -- Etica y Responsabilidad Social
(1, 3, 1, 20), -- Derecho y Legislacion Laboral
(1, 3, 1, 21), -- Redes y Comunicaciones
(1, 3, 1, 22), -- Seguridad de los Sistemas
(1, 3, 1, 23), -- Base de Datos
(1, 3, 1, 24), -- Sistema de Información Organizacional
(1, 3, 1, 25), -- Desarrollo de Sistemas Web
(1, 3, 1, 26); -- Practica Profesionalizante II

-- Repetir para las comisiones B y C del Año 3
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(1, 3, 2, 19),
(1, 3, 2, 20),
(1, 3, 2, 21),
(1, 3, 2, 22),
(1, 3, 2, 23),
(1, 3, 2, 24),
(1, 3, 2, 25),
(1, 3, 2, 26);

INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(1, 3, 3, 19),
(1, 3, 3, 20),
(1, 3, 3, 21),
(1, 3, 3, 22),
(1, 3, 3, 23),
(1, 3, 3, 24),
(1, 3, 3, 25),
(1, 3, 3, 26);

-- A continuación, insertamos las materias para Técnico en Infraestructura (carrera_id = 2)
-- Año 1
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(2, 1, 1, 27), -- Comunicacion
(2, 1, 1, 28), -- UDI I
(2, 1, 1, 29), -- Matematicas
(2, 1, 1, 30), -- Fisica Aplicada a las Tecnologias de la Informacion
(2, 1, 1, 31), -- Administracion
(2, 1, 1, 32), -- Ingles Tecnico
(2, 1, 1, 33), -- Arquitectura de las Computadoras
(2, 1, 1, 34), -- Logica y Programacion
(2, 1, 1, 35); -- Infraestructura de Redes I

-- Repetir para las comisiones B y C del Año 1
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(2, 1, 2, 27),
(2, 1, 2, 28),
(2, 1, 2, 29),
(2, 1, 2, 30),
(2, 1, 2, 31),
(2, 1, 2, 32),
(2, 1, 2, 33),
(2, 1, 2, 34),
(2, 1, 2, 35);

INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(2, 1, 3, 27),
(2, 1, 3, 28),
(2, 1, 3, 29),
(2, 1, 3, 30),
(2, 1, 3, 31),
(2, 1, 3, 32),
(2, 1, 3, 33),
(2, 1, 3, 34),
(2, 1, 3, 35);

-- Año 2
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(2, 2, 1, 36), -- Problematicas Socio Contemporaneas
(2, 2, 1, 37), -- UDI II
(2, 2, 1, 38), -- Estadisticas
(2, 2, 1, 39), -- Innovacion y Desarrollo Emprendedor
(2, 2, 1, 40), -- Sistemas Operativos
(2, 2, 1, 41), -- Algoritmos y Estructura De Datos
(2, 2, 1, 42), -- Base de Datos
(2, 2, 1, 43), -- Infraestructura de Redes II
(2, 2, 1, 44); -- Practica Profesionalizante I

-- Repetir para las comisiones B y C del Año 2
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(2, 2, 2, 36),
(2, 2, 2, 37),
(2, 2, 2, 38),
(2, 2, 2, 39),
(2, 2, 2, 40),
(2, 2, 2, 41),
(2, 2, 2, 42),
(2, 2, 2, 43),
(2, 2, 2, 44);

INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(2, 2, 3, 36),
(2, 2, 3, 37),
(2, 2, 3, 38),
(2, 2, 3, 39),
(2, 2, 3, 40),
(2, 2, 3, 41),
(2, 2, 3, 42),
(2, 2, 3, 43),
(2, 2, 3, 44);

-- Año 3
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(2, 3, 1, 45), -- Etica y Responsabilidad Social
(2, 3, 1, 46), -- Derecho y Legislacion Laboral
(2, 3, 1, 47), -- Administracion de Base de Datos
(2, 3, 1, 48), -- Seguridad de los Sistemas
(2, 3, 1, 49), -- Integridad y Migracion de Datos
(2, 3, 1, 50), -- Administracion de Sistemas y Redes
(2, 3, 1, 51); -- Practica Profesionalizante II

-- Repetir para las comisiones B y C del Año 3
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(2, 3, 2, 45),
(2, 3, 2, 46),
(2, 3, 2, 47),
(2, 3, 2, 48),
(2, 3, 2, 49),
(2, 3, 2, 50),
(2, 3, 2, 51);

INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(2, 3, 3, 45),
(2, 3, 3, 46),
(2, 3, 3, 47),
(2, 3, 3, 48),
(2, 3, 3, 49),
(2, 3, 3, 50),
(2, 3, 3, 51);

-- Materias para Desarrollador de Software (carrera_id = 3)
-- Año 1
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(3, 1, 1, 52), -- Comunicacion
(3, 1, 1, 53), -- UDI I
(3, 1, 1, 54), -- Matematicas
(3, 1, 1, 55), -- Ingles Tecnico I
(3, 1, 1, 56), -- Administracion
(3, 1, 1, 57), -- Tecnologia de la Informacion
(3, 1, 1, 58), -- Logica y Estructura de Datos
(3, 1, 1, 59), -- Ingenieria de Software I
(3, 1, 1, 60); -- Sistemas Operativos

-- Repetir para las comisiones B y C del Año 1
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(3, 1, 2, 52),
(3, 1, 2, 53),
(3, 1, 2, 54),
(3, 1, 2, 55),
(3, 1, 2, 56),
(3, 1, 2, 57),
(3, 1, 2, 58),
(3, 1, 2, 59),
(3, 1, 2, 60);

INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(3, 1, 3, 52),
(3, 1, 3, 53),
(3, 1, 3, 54),
(3, 1, 3, 55),
(3, 1, 3, 56),
(3, 1, 3, 57),
(3, 1, 3, 58),
(3, 1, 3, 59),
(3, 1, 3, 60);

-- Año 2
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(3, 2, 1, 61), -- Problematicas Socio Contemporaneas
(3, 2, 1, 62), -- UDI II
(3, 2, 1, 63), -- Ingles Tecnico II
(3, 2, 1, 64), -- Innovacion y Desarrollo Emprendedor
(3, 2, 1, 65), -- Estadisticas
(3, 2, 1, 66), -- Programacion I
(3, 2, 1, 67), -- Ingenieria de Software II
(3, 2, 1, 68), -- Base de Datos I
(3, 2, 1, 69); -- Practica Profesionalizante I

-- Repetir para las comisiones B y C del Año 2
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(3, 2, 2, 61),
(3, 2, 2, 62),
(3, 2, 2, 63),
(3, 2, 2, 64),
(3, 2, 2, 65),
(3, 2, 2, 66),
(3, 2, 2, 67),
(3, 2, 2, 68),
(3, 2, 2, 69);

INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(3, 2, 3, 61),
(3, 2, 3, 62),
(3, 2, 3, 63),
(3, 2, 3, 64),
(3, 2, 3, 65),
(3, 2, 3, 66),
(3, 2, 3, 67),
(3, 2, 3, 68),
(3, 2, 3, 69);

-- Año 3
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(3, 3, 1, 70), -- Etica y Responsabilidad Social
(3, 3, 1, 71), -- Derecho y Legislacion Laboral
(3, 3, 1, 72), -- Redes y Comunicacion
(3, 3, 1, 73), -- Programacion II
(3, 3, 1, 74), -- Gestion y Proyecto de Software
(3, 3, 1, 75), -- Base de Datos II
(3, 3, 1, 76); -- Practica Profesionalizante II

-- Repetir para las comisiones B y C del Año 3
INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(3, 3, 2, 70),
(3, 3, 2, 71),
(3, 3, 2, 72),
(3, 3, 2, 73),
(3, 3, 2, 74),
(3, 3, 2, 75),
(3, 3, 2, 76);

INSERT INTO carrera_materias (id_carrera, id_anio, id_comision, id_materia) VALUES 
(3, 3, 3, 70),
(3, 3, 3, 71),
(3, 3, 3, 72),
(3, 3, 3, 73),
(3, 3, 3, 74),
(3, 3, 3, 75),
(3, 3, 3, 76);




