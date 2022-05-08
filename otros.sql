-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 08-05-2022 a las 02:03:42
-- Versión del servidor: 5.7.36
-- Versión de PHP: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inventario`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `otros`
--

DROP TABLE IF EXISTS `otros`;
CREATE TABLE IF NOT EXISTS `otros` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DISPOSITIVO` varchar(80) DEFAULT NULL,
  `CANTIDAD` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `otros`
--

INSERT INTO `otros` (`ID`, `DISPOSITIVO`, `CANTIDAD`) VALUES
(1, 'RAM', 71),
(2, 'Discos', 23),
(3, 'Cables IDLE', 32),
(4, 'Cables SATA', 6),
(5, 'Repuestos Notebook Gobierno', 8),
(6, 'Baterias Notebook Gobierno', 2),
(7, 'Placas de red', 8),
(8, 'Unidades ópticas', 5),
(9, 'Cargadores routers', 25),
(10, 'Placas de video', 5),
(11, 'Webcam', 1),
(12, 'Mouse', 14),
(13, 'Placa de router', 1),
(14, 'Cables VGA', 23),
(15, 'Cables de alimentación varios', 63),
(16, 'Baterias', 11),
(17, 'Routers', 21),
(18, 'Coolers (enteros)', 11),
(19, 'Rejillas de ventilación', 10),
(20, 'Ventiladores', 10),
(21, 'Cargadores de netbook', 14),
(22, 'Adaptadores', 3),
(23, 'Micrófonos?', 3),
(24, 'UPS', 7),
(25, 'Laptop', 28),
(26, 'Unidad de ventilación', 3),
(27, 'Carcasas de laptop', 12),
(28, 'Fuentes de poder', 4),
(29, 'Plástico para impresora 3D', 18),
(30, 'Soporte de monitor', 2),
(31, 'Impresoras', 4);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
