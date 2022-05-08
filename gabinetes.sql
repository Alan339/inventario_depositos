-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 08-05-2022 a las 02:02:53
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
-- Estructura de tabla para la tabla `gabinetes`
--

DROP TABLE IF EXISTS `gabinetes`;
CREATE TABLE IF NOT EXISTS `gabinetes` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEPOSITO` int(1) DEFAULT NULL,
  `GABINETE` int(11) DEFAULT NULL,
  `MARCA` varchar(20) DEFAULT NULL,
  `SO` varchar(30) DEFAULT NULL,
  `FUNCIONA` tinyint(1) DEFAULT NULL,
  `OBSERVACIONES` varchar(200) DEFAULT NULL,
  `COMPONENTES_FALTANTES` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `gabinetes`
--

INSERT INTO `gabinetes` (`ID`, `DEPOSITO`, `GABINETE`, `MARCA`, `SO`, `FUNCIONA`, `OBSERVACIONES`, `COMPONENTES_FALTANTES`) VALUES
(1, 1, 1, 'BANGHO', NULL, 0, 'No se pudo encender por falta de componentes', 'RAM'),
(2, 1, 2, 'BANGHO', NULL, 0, 'No se pudo encender por falta de componentes', 'Cooler salido - Disco desconectado'),
(3, 1, 3, 'OMNIDATA', 'Windows 10', 1, 'Sin problemas', NULL),
(4, 1, 4, 'OMNIDATA', NULL, 0, 'No se pudo encender por falta de componentes', 'RAM - Fuente de Alimentación'),
(5, 1, 5, 'BANGHO', NULL, 0, 'No se pudo verificar bien el interior, pero no enciende por falta de fuente', 'Fuente de Alimentación - etc'),
(6, 1, 6, 'DELL', NULL, 0, 'No se pudo encender por falta de componentes', 'RAM - Fuente de Alimentación - etc'),
(7, 1, 7, 'DELL', 'Windows 10', 1, 'Sin problemas', 'None'),
(8, 1, 8, 'DELL', NULL, 0, 'Al iniciar, no detecta un disco de booteo', 'Disco'),
(9, 1, 9, 'BANGHO', NULL, 0, 'Aparentemente, no tiene disco', 'Disco?'),
(10, 1, 10, 'DELL', 'Windows 10', 1, 'Sin problemas', NULL),
(11, 1, 11, 'BANGHO', NULL, 0, 'No se pudo encender por falta de componentes', 'RAM'),
(12, 1, 12, 'EXO', NULL, 0, 'No se pudo encender por falta de componentes', 'RAM - Fuente de Alimentación - Disco'),
(13, 1, 13, 'BANGHO', NULL, 0, 'No se pudo encender por falta de componentes', 'RAM - Fuente de Alimentación'),
(14, 1, 14, 'BANGHO', NULL, 0, 'No se pudo encender por falta de componentes', 'RAM - Disco'),
(15, 1, 15, 'BANGHO', NULL, 0, 'No hay forma de que funcione', 'Todo menos CPU y Motherboard'),
(16, 1, 16, 'MUSTIFF', 'None', 0, 'No se pudo encender por falta de componentes', 'RAM - Disco'),
(17, 2, 1, NULL, 'Windows 98', 1, 'No se puede probar por la antigüedad', NULL),
(18, 2, 2, 'MUSTIFF', 'Windows 10', 1, 'Sin problemas', NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
