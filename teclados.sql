-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 08-05-2022 a las 02:04:09
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
-- Estructura de tabla para la tabla `teclados`
--

DROP TABLE IF EXISTS `teclados`;
CREATE TABLE IF NOT EXISTS `teclados` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEPOSITO` int(1) DEFAULT NULL,
  `TECLADO` int(11) DEFAULT NULL,
  `MARCA` varchar(20) DEFAULT NULL,
  `MODELO` varchar(30) DEFAULT NULL,
  `FICHA` varchar(5) DEFAULT NULL,
  `FUNCIONA` tinyint(1) DEFAULT NULL,
  `OBSERVACIONES` varchar(200) DEFAULT NULL,
  `RECOMENDACIONES` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `teclados`
--

INSERT INTO `teclados` (`ID`, `DEPOSITO`, `TECLADO`, `MARCA`, `MODELO`, `FICHA`, `FUNCIONA`, `OBSERVACIONES`, `RECOMENDACIONES`) VALUES
(1, 1, 1, 'ONSET', '#it1180', 'USB', 1, 'Funciona pero le faltan teclas', 'Colocar teclas'),
(2, 1, 2, 'ONSET', '#it1180', 'USB', 1, 'Funciona pero le faltan teclas y tiene teclas cambiadas de lugar', 'Colocar teclas en su lugar'),
(3, 1, 3, 'ONSET', '#it1180', 'USB', 1, 'Funciona pero le faltan teclas', 'Colocar teclas'),
(4, 1, 4, 'ONSET', '#it1180', 'USB', 1, 'Funciona pero le faltan teclas y tiene teclas cambiadas de lugar', 'Colocar teclas en su lugar'),
(5, 1, 5, 'ONSET', '#it1180', 'USB', 1, 'Funciona pero le faltan f y -', 'Colocar teclas'),
(6, 1, 6, 'ONSET', '#it1180', 'USB', 1, 'Funciona pero la tecla espacio esta rota', 'Cambiar tecla espacio'),
(7, 1, 7, 'ONSET', '#it1180', 'USB', 1, 'Funciona pero la tecla tabulador esta rota', 'Cambiar tecla tabulador'),
(8, 1, 8, 'ONSET', '#it1180', 'USB', 1, 'Funciona pero le faltan teclas y tiene teclas cambiadas de lugar', 'Colocar teclas en su lugar'),
(9, 1, 9, 'GENIUS', 'KB-06XE', 'USB', 1, 'Perfecto estado', 'Listo para utilizar'),
(10, 1, 10, 'Verbatin', '98111', 'USB', 1, 'Funciona pero le faltan teclas, tiene teclas cambiadas de lugar y su estructura y cable están dañados', 'Colocar teclas en su lugar y reparar cable'),
(11, 1, 11, 'GENIUS', 'GK-070001/U', 'USB', 0, 'Le faltan teclas, tiene teclas cambiadas de lugar y esta rota la zona donde se encontraría la o, por lo que esta presionada constantemente', 'Desaserse de el'),
(12, 1, 12, 'HP', 'KB-0316', 'PS-2', 1, 'Funciona pero le faltan teclas y tiene teclas cambiadas de lugar', 'Colocar teclas en su lugar'),
(13, 1, 13, 'GENIUS', 'GK-100015', 'PS-2', 0, 'Le faltan teclas y esta rota la ficha ps-2', 'Desaserse de el'),
(14, 1, 14, 'GENIUS', 'GK-100015', 'PS-2', 1, 'Perfecto estado', 'Listo para utilizar'),
(15, 2, 1, 'ONSET', '#it1180', 'USB', 1, 'Perfecto estado', 'Listo para utilizar'),
(16, 2, 2, 'ONSET', '#it1180', 'USB', 1, 'Perfecto estado', 'Listo para utilizar'),
(17, 2, 3, 'ONSET', '#it1180', NULL, 0, 'No funciona, faltan teclas y ficha', 'Desaserse de el'),
(18, 2, 4, 'ONSET', '#it1180', 'USB', 1, 'Funciona pero tiene teclas cambiadas de lugar', 'Colocar teclas en su lugar'),
(19, 2, 5, 'ONSET', '#it1180', NULL, 0, 'No funciona, faltan teclas y ficha', 'Desaserse de el'),
(20, 2, 6, 'ONSET', '#it1180', 'USB', 1, 'Funciona pero tiene teclas cambiadas de lugar y falta la letra f', 'Colocar teclas en su lugar'),
(21, 2, 7, 'ONSET', '#it1180', 'USB', 1, 'Fuciona pero algunas teclas no', 'Intentar reparar'),
(22, 2, 8, 'GENIUS', 'GK-100015', 'PS-2', 1, 'Funciona pero le faltan teclas', 'Colocar teclas'),
(23, 2, 9, 'GENIUS', 'GK-100015', 'PS-2', 1, 'Perfecto estado', 'Listo para utilizar'),
(24, 2, 10, 'GENIUS', 'GK-100015', 'PS-2', 1, 'Funciona pero tiene teclas desconfiguradas', 'Configurar'),
(25, 2, 11, 'DELL', 'KB2012-B', 'USB', 1, 'Perfecto estado', 'Listo para utilizar'),
(26, 2, 12, 'DELL', 'KB2012-B', 'USB', 1, 'Perfecto estado', 'Listo para utilizar'),
(27, 2, 13, 'DELL', 'KB2012-B', 'USB', 1, 'Funciona pero tiene teclas cambiadas de lugar y el ctrl izquierdo no funciona', 'Colocar teclas en su lugar'),
(28, 2, 14, 'DELL', 'SK-8115', 'USB', 1, 'Perfecto estado', 'Listo para utilizar'),
(29, 2, 15, 'DELL', 'SK-8115', 'USB', 1, 'Funciona pero la tecla ctrl izquierda esta precionada y la derecha no esta', 'Arreglar teclas'),
(30, 2, 16, 'BANGH6', NULL, 'USB', 1, 'Funciona pero tiene teclas cambiada de lugar y faltan algunas', 'Colocar teclas en su lugar'),
(31, 2, 17, 'Soneview', 'FZK-8832', 'PS-2', 0, 'No funciona, faltan teclas y ficha ps-2', 'Desaserse de el'),
(32, 2, 18, 'POSITIVO BGH', NULL, 'USB', 1, 'Perfecto estado', 'Listo para utilizar'),
(33, 2, 19, 'Verbatin', '98111', 'USB', 1, 'Perfecto estado', 'Listo para utilizar'),
(34, 2, 20, 'DELL', 'SK-8115', 'USB', 1, 'Funciona pero la tecla ctrl izquierda esta precionada y la derecha no esta', 'Arreglar teclas');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
