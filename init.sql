-- Crear base de datos
CREATE DATABASE IF NOT EXISTS laboratorio_clinico CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE laboratorio_clinico;

-- Tabla: paciente
CREATE TABLE IF NOT EXISTS paciente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    documento VARCHAR(20) NOT NULL UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    genero ENUM('Masculino', 'Femenino', 'Otro') NOT NULL
);

-- Tabla: examen
CREATE TABLE IF NOT EXISTS examen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    area VARCHAR(50) NOT NULL
);

-- Tabla: orden
CREATE TABLE IF NOT EXISTS orden (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_orden VARCHAR(20) NOT NULL UNIQUE,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_paciente INT NOT NULL,
    estado ENUM('Pendiente', 'En proceso', 'Completado') DEFAULT 'Pendiente',
    FOREIGN KEY (id_paciente) REFERENCES paciente(id)
);

-- Tabla: orden_examen
CREATE TABLE IF NOT EXISTS orden_examen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_orden INT NOT NULL,
    id_examen INT NOT NULL,
    resultado TEXT,
    fecha_resultado DATETIME,
    FOREIGN KEY (id_orden) REFERENCES orden(id) ON DELETE CASCADE,
    FOREIGN KEY (id_examen) REFERENCES examen(id)
);

-- Datos de prueba: pacientes
INSERT INTO paciente (nombre_completo, documento, fecha_nacimiento, genero) VALUES
('Laura Sánchez', '12345678', '1995-05-10', 'Femenino'),
('Carlos Méndez', '87654321', '1988-11-23', 'Masculino');

-- Datos de prueba: exámenes
INSERT INTO examen (nombre, area) VALUES
('Hemograma', 'Hematología'),
('Glucosa', 'Química'),
('Perfil Lipídico', 'Química'),
('Orina Completa', 'Uroanálisis');

-- Datos de prueba: órdenes
INSERT INTO orden (numero_orden, id_paciente, estado) VALUES
('20250708-001', 1, 'Pendiente'),
('20250708-002', 2, 'En proceso');

-- Datos de prueba: orden_examen
INSERT INTO orden_examen (id_orden, id_examen, resultado, fecha_resultado) VALUES
(1, 1, NULL, NULL),
(1, 2, NULL, NULL),
(2, 3, 'Colesterol Total: 200 mg/dL', '2025-07-08 09:00:00'),
(2, 4, NULL, NULL); 