-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 08-05-2022 a las 02:03:16
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
-- Estructura de tabla para la tabla `monitores`
--

DROP TABLE IF EXISTS `monitores`;
CREATE TABLE IF NOT EXISTS `monitores` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEPOSITO` int(1) DEFAULT NULL,
  `MONITOR` int(11) DEFAULT NULL,
  `MARCA` varchar(20) DEFAULT NULL,
  `MODELO` varchar(30) DEFAULT NULL,
  `FUNCIONA` tinyint(1) DEFAULT NULL,
  `OBSERVACIONES` varchar(200) DEFAULT NULL,
  `RECOMENDACIONES` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `monitores`
--

INSERT INTO `monitores` (`ID`, `DEPOSITO`, `MONITOR`, `MARCA`, `MODELO`, `FUNCIONA`, `OBSERVACIONES`, `RECOMENDACIONES`) VALUES
(1, 1, 1, 'Samsung', 'GH17WS', 0, 'Pantalla rota', 'Desaserse de él'),
(2, 1, 2, 'LG', 'W1943TE-PFV', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(3, 1, 3, 'Benq', 'ET-0025-TA', 1, 'No tiene soporte', 'Comprar soporte'),
(4, 1, 4, 'LG', 'W1943TE-PFV', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(5, 1, 5, 'LG', 'W1943TE-PFV', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(6, 1, 6, 'LG', 'W1943TE-PFV', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(7, 1, 7, 'LG', '19M38A-BB', 1, 'Base suelta', 'Fijar la base'),
(8, 1, 8, 'LG', 'W1943TE-PFV', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(9, 1, 9, 'LG', 'W1943TE-PFV', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(10, 1, 10, 'Samsung', 'LS19D300NYCZB', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(11, 1, 11, 'Samsung', 'GH17WS', 0, 'No prende', 'Esta complicado de recuperar'),
(12, 2, 1, 'LG', 'W1943TE-PFV', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(13, 2, 2, 'LG', '19M38A-BB', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(14, 2, 3, 'Samsung', 'GH17WS', 1, 'Debe conectarse a un gabinete', 'Perfecto para usarlo'),
(15, 2, 4, 'LG', '19M38A-BB', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(16, 2, 5, 'LG', '19M38A-BB', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(17, 2, 6, 'Samsung', 'LS19D300NYCZB', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(18, 2, 7, 'Samsung', 'GH17WS', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(19, 2, 8, 'Olivetti', 'LD 19052', 0, 'No tenemos el cable de alimentación correcto', 'Obtener el cable de alimentación correspondiente'),
(20, 2, 9, 'LG', 'StudioWorks', 1, 'Perfecto estado', 'Perfecto para usarlo'),
(21, 2, 10, 'Globalcomp', 'G-717A', 1, 'Quizá este muy azulada la pantalla', 'Perfecto para usarlo'),
(22, 2, 11, 'HP', 'D8901A', 0, 'No prende', 'Verificar funcionamiento interno'),
(23, 2, 12, 'Globalcomp', 'G-717A', 1, 'Perfecto estado', 'Perfecto para usarlo');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
