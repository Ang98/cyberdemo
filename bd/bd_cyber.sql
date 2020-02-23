CREATE DATABASE  IF NOT EXISTS `cyberdemocracia` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `cyberdemocracia`;
-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: cyberdemocracia
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `api_administrador`
--

DROP TABLE IF EXISTS `api_administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_administrador` (
  `persona_ptr_id` int(11) NOT NULL,
  `cargo` varchar(20) NOT NULL,
  PRIMARY KEY (`persona_ptr_id`),
  CONSTRAINT `api_administrador_persona_ptr_id_8f665e75_fk_api_persona_id` FOREIGN KEY (`persona_ptr_id`) REFERENCES `api_persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_administrador`
--

LOCK TABLES `api_administrador` WRITE;
/*!40000 ALTER TABLE `api_administrador` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_alternativa`
--

DROP TABLE IF EXISTS `api_alternativa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_alternativa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contenido` varchar(45) NOT NULL,
  `respuesta` tinyint(1) NOT NULL,
  `fecha_registro` date NOT NULL,
  `usuario_registro` varchar(45) NOT NULL,
  `fecha_modificacion` date NOT NULL,
  `usuario_modificacion` varchar(45) NOT NULL,
  `id_examen_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_alternativa_id_examen_id_9023b5d8_fk_api_examen_id` (`id_examen_id`),
  CONSTRAINT `api_alternativa_id_examen_id_9023b5d8_fk_api_examen_id` FOREIGN KEY (`id_examen_id`) REFERENCES `api_examen` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_alternativa`
--

LOCK TABLES `api_alternativa` WRITE;
/*!40000 ALTER TABLE `api_alternativa` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_alternativa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_conferencia`
--

DROP TABLE IF EXISTS `api_conferencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_conferencia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tema` varchar(45) NOT NULL,
  `apellidos_conferencista` varchar(100) NOT NULL,
  `nombres_conferecista` varchar(100) NOT NULL,
  `tipo` varchar(45) NOT NULL,
  `fecha_registro` date NOT NULL,
  `usuario_registro` varchar(45) NOT NULL,
  `fecha_modificacion` date NOT NULL,
  `usuario_modificacion` varchar(45) NOT NULL,
  `id_plan_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_conferencia_id_plan_id_fb1f64a2_fk_api_planestudio_id` (`id_plan_id`),
  CONSTRAINT `api_conferencia_id_plan_id_fb1f64a2_fk_api_planestudio_id` FOREIGN KEY (`id_plan_id`) REFERENCES `api_planestudio` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_conferencia`
--

LOCK TABLES `api_conferencia` WRITE;
/*!40000 ALTER TABLE `api_conferencia` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_conferencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_curso`
--

DROP TABLE IF EXISTS `api_curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_curso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_curso` varchar(45) NOT NULL,
  `sumilla` varchar(300) NOT NULL,
  `docente` varchar(100) NOT NULL,
  `fecha_registro` date NOT NULL,
  `usuario_registro` varchar(45) NOT NULL,
  `fecha_modificacion` date NOT NULL,
  `usuario_modificacion` varchar(45) NOT NULL,
  `id_plan_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_curso_id_plan_id_62ee02ad_fk_api_planestudio_id` (`id_plan_id`),
  CONSTRAINT `api_curso_id_plan_id_62ee02ad_fk_api_planestudio_id` FOREIGN KEY (`id_plan_id`) REFERENCES `api_planestudio` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_curso`
--

LOCK TABLES `api_curso` WRITE;
/*!40000 ALTER TABLE `api_curso` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_debate`
--

DROP TABLE IF EXISTS `api_debate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_debate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tema` varchar(45) NOT NULL,
  `estado` varchar(45) NOT NULL,
  `moderador` varchar(45) NOT NULL,
  `fecha_registro` date NOT NULL,
  `usuario_registro` varchar(45) NOT NULL,
  `fecha_modificacion` date NOT NULL,
  `usuario_modificacion` varchar(45) NOT NULL,
  `id_militante_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_debate_id_militante_id_0fce5ad4_fk_api_milit` (`id_militante_id`),
  CONSTRAINT `api_debate_id_militante_id_0fce5ad4_fk_api_milit` FOREIGN KEY (`id_militante_id`) REFERENCES `api_militante` (`persona_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_debate`
--

LOCK TABLES `api_debate` WRITE;
/*!40000 ALTER TABLE `api_debate` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_debate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_esegjne`
--

DROP TABLE IF EXISTS `api_esegjne`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_esegjne` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado` int(11) NOT NULL,
  `dni_responsable` varchar(45) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `nombres` varchar(100) NOT NULL,
  `sugerencia` varchar(400) NOT NULL,
  `observacion` varchar(400) NOT NULL,
  `fecha_registro` date NOT NULL,
  `usuario_registro` varchar(45) NOT NULL,
  `fecha_modificacion` date NOT NULL,
  `usuario_modificacion` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_esegjne`
--

LOCK TABLES `api_esegjne` WRITE;
/*!40000 ALTER TABLE `api_esegjne` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_esegjne` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_examen`
--

DROP TABLE IF EXISTS `api_examen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_examen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(45) NOT NULL,
  `responsable` varchar(45) NOT NULL,
  `fecha_registro` date NOT NULL,
  `usuario_registro` varchar(45) NOT NULL,
  `fecha_modificacion` date NOT NULL,
  `usuario_modificacion` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_examen`
--

LOCK TABLES `api_examen` WRITE;
/*!40000 ALTER TABLE `api_examen` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_examen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_examenpregunta`
--

DROP TABLE IF EXISTS `api_examenpregunta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_examenpregunta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_registro` date NOT NULL,
  `usuario_registro` varchar(45) NOT NULL,
  `fecha_modificacion` date NOT NULL,
  `usuario_modificacion` varchar(45) NOT NULL,
  `id_examen_id` int(11) NOT NULL,
  `id_pregunta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_examenpregunta_id_examen_id_9f9cdcdd_fk_api_examen_id` (`id_examen_id`),
  KEY `api_examenpregunta_id_pregunta_id_b4059a18_fk_api_pregunta_id` (`id_pregunta_id`),
  CONSTRAINT `api_examenpregunta_id_examen_id_9f9cdcdd_fk_api_examen_id` FOREIGN KEY (`id_examen_id`) REFERENCES `api_examen` (`id`),
  CONSTRAINT `api_examenpregunta_id_pregunta_id_b4059a18_fk_api_pregunta_id` FOREIGN KEY (`id_pregunta_id`) REFERENCES `api_pregunta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_examenpregunta`
--

LOCK TABLES `api_examenpregunta` WRITE;
/*!40000 ALTER TABLE `api_examenpregunta` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_examenpregunta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_externo`
--

DROP TABLE IF EXISTS `api_externo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_externo` (
  `persona_ptr_id` int(11) NOT NULL,
  `descripcion` varchar(400) NOT NULL,
  PRIMARY KEY (`persona_ptr_id`),
  CONSTRAINT `api_externo_persona_ptr_id_7e1c3d5d_fk_api_persona_id` FOREIGN KEY (`persona_ptr_id`) REFERENCES `api_persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_externo`
--

LOCK TABLES `api_externo` WRITE;
/*!40000 ALTER TABLE `api_externo` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_externo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_militante`
--

DROP TABLE IF EXISTS `api_militante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_militante` (
  `persona_ptr_id` int(11) NOT NULL,
  `perfil` varchar(45) NOT NULL,
  `cargo` varchar(45) NOT NULL,
  `encargado` varchar(45) NOT NULL,
  `id_partido_id` int(11) NOT NULL,
  `id_plan_id` int(11) NOT NULL,
  PRIMARY KEY (`persona_ptr_id`),
  KEY `api_militante_id_plan_id_50d18b3e_fk_api_planestudio_id` (`id_plan_id`),
  KEY `api_militante_id_partido_id_336b9e72_fk_api_partidopolitico_id` (`id_partido_id`),
  CONSTRAINT `api_militante_id_partido_id_336b9e72_fk_api_partidopolitico_id` FOREIGN KEY (`id_partido_id`) REFERENCES `api_partidopolitico` (`id`),
  CONSTRAINT `api_militante_id_plan_id_50d18b3e_fk_api_planestudio_id` FOREIGN KEY (`id_plan_id`) REFERENCES `api_planestudio` (`id`),
  CONSTRAINT `api_militante_persona_ptr_id_854adb54_fk_api_persona_id` FOREIGN KEY (`persona_ptr_id`) REFERENCES `api_persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_militante`
--

LOCK TABLES `api_militante` WRITE;
/*!40000 ALTER TABLE `api_militante` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_militante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_militanteexamen`
--

DROP TABLE IF EXISTS `api_militanteexamen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_militanteexamen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nota` int(11) NOT NULL,
  `fecha_registro` date NOT NULL,
  `usuario_registro` varchar(45) NOT NULL,
  `fecha_modificacion` date NOT NULL,
  `usuario_modificacion` varchar(45) NOT NULL,
  `id_examen_id` int(11) NOT NULL,
  `id_militante_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_militanteexamen_id_examen_id_b95b929f_fk_api_examen_id` (`id_examen_id`),
  KEY `api_militanteexamen_id_militante_id_c44ab43f_fk_api_milit` (`id_militante_id`),
  CONSTRAINT `api_militanteexamen_id_examen_id_b95b929f_fk_api_examen_id` FOREIGN KEY (`id_examen_id`) REFERENCES `api_examen` (`id`),
  CONSTRAINT `api_militanteexamen_id_militante_id_c44ab43f_fk_api_milit` FOREIGN KEY (`id_militante_id`) REFERENCES `api_militante` (`persona_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_militanteexamen`
--

LOCK TABLES `api_militanteexamen` WRITE;
/*!40000 ALTER TABLE `api_militanteexamen` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_militanteexamen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_partidopolitico`
--

DROP TABLE IF EXISTS `api_partidopolitico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_partidopolitico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `estado` varchar(45) NOT NULL,
  `fecha_registro` date NOT NULL,
  `usuario_registro` varchar(45) NOT NULL,
  `fecha_modificacion` date NOT NULL,
  `usuario_modificacion` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_partidopolitico`
--

LOCK TABLES `api_partidopolitico` WRITE;
/*!40000 ALTER TABLE `api_partidopolitico` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_partidopolitico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_persona`
--

DROP TABLE IF EXISTS `api_persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_persona` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(40) NOT NULL,
  `apellido_paterno` varchar(20) NOT NULL,
  `apellido_materno` varchar(20) NOT NULL,
  `dni` varchar(15) NOT NULL,
  `correo` varchar(254) NOT NULL,
  `telefono` int(11) NOT NULL,
  `usuario` varchar(40) NOT NULL,
  `contraseña` varchar(40) NOT NULL,
  `fecha_registro` date NOT NULL,
  `usuario_registro` varchar(45) NOT NULL,
  `fecha_modificacion` date NOT NULL,
  `usuario_modificacion` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_persona`
--

LOCK TABLES `api_persona` WRITE;
/*!40000 ALTER TABLE `api_persona` DISABLE KEYS */;
INSERT INTO `api_persona` VALUES (1,'angel german','cayatopa','yauri','70099798','angel@gmail.com',998896940,'angel','angel','2020-02-23','','2020-02-23','');
/*!40000 ALTER TABLE `api_persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_planestudio`
--

DROP TABLE IF EXISTS `api_planestudio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_planestudio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `estado` varchar(45) NOT NULL,
  `fecha_registro` date NOT NULL,
  `usuario_registro` varchar(45) NOT NULL,
  `fecha_modificacion` date NOT NULL,
  `usuario_modificacion` varchar(45) NOT NULL,
  `id_seg_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_planestudio_id_seg_id_bb72d2af_fk_api_esegjne_id` (`id_seg_id`),
  CONSTRAINT `api_planestudio_id_seg_id_bb72d2af_fk_api_esegjne_id` FOREIGN KEY (`id_seg_id`) REFERENCES `api_esegjne` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_planestudio`
--

LOCK TABLES `api_planestudio` WRITE;
/*!40000 ALTER TABLE `api_planestudio` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_planestudio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_pregunta`
--

DROP TABLE IF EXISTS `api_pregunta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_pregunta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contenido` varchar(600) NOT NULL,
  `puntaje` int(11) NOT NULL,
  `fecha_registro` date NOT NULL,
  `usuario_registro` varchar(45) NOT NULL,
  `fecha_modificacion` date NOT NULL,
  `usuario_modificacion` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_pregunta`
--

LOCK TABLES `api_pregunta` WRITE;
/*!40000 ALTER TABLE `api_pregunta` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_pregunta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_secretariapp`
--

DROP TABLE IF EXISTS `api_secretariapp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `api_secretariapp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `responsable` varchar(45) NOT NULL,
  `fecha_registro` date NOT NULL,
  `usuario_registro` varchar(45) NOT NULL,
  `fecha_modificacion` date NOT NULL,
  `usuario_modificacion` varchar(45) NOT NULL,
  `id_partido_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_secretariapp_id_partido_id_3e0fe23a_fk_api_parti` (`id_partido_id`),
  CONSTRAINT `api_secretariapp_id_partido_id_3e0fe23a_fk_api_parti` FOREIGN KEY (`id_partido_id`) REFERENCES `api_partidopolitico` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_secretariapp`
--

LOCK TABLES `api_secretariapp` WRITE;
/*!40000 ALTER TABLE `api_secretariapp` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_secretariapp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Token',7,'add_token'),(26,'Can change Token',7,'change_token'),(27,'Can delete Token',7,'delete_token'),(28,'Can view Token',7,'view_token'),(29,'Can add eseg jne',8,'add_esegjne'),(30,'Can change eseg jne',8,'change_esegjne'),(31,'Can delete eseg jne',8,'delete_esegjne'),(32,'Can view eseg jne',8,'view_esegjne'),(33,'Can add examen',9,'add_examen'),(34,'Can change examen',9,'change_examen'),(35,'Can delete examen',9,'delete_examen'),(36,'Can view examen',9,'view_examen'),(37,'Can add partido politico',10,'add_partidopolitico'),(38,'Can change partido politico',10,'change_partidopolitico'),(39,'Can delete partido politico',10,'delete_partidopolitico'),(40,'Can view partido politico',10,'view_partidopolitico'),(41,'Can add persona',11,'add_persona'),(42,'Can change persona',11,'change_persona'),(43,'Can delete persona',11,'delete_persona'),(44,'Can view persona',11,'view_persona'),(45,'Can add pregunta',12,'add_pregunta'),(46,'Can change pregunta',12,'change_pregunta'),(47,'Can delete pregunta',12,'delete_pregunta'),(48,'Can view pregunta',12,'view_pregunta'),(49,'Can add administrador',13,'add_administrador'),(50,'Can change administrador',13,'change_administrador'),(51,'Can delete administrador',13,'delete_administrador'),(52,'Can view administrador',13,'view_administrador'),(53,'Can add externo',14,'add_externo'),(54,'Can change externo',14,'change_externo'),(55,'Can delete externo',14,'delete_externo'),(56,'Can view externo',14,'view_externo'),(57,'Can add militante',15,'add_militante'),(58,'Can change militante',15,'change_militante'),(59,'Can delete militante',15,'delete_militante'),(60,'Can view militante',15,'view_militante'),(61,'Can add secretaria pp',16,'add_secretariapp'),(62,'Can change secretaria pp',16,'change_secretariapp'),(63,'Can delete secretaria pp',16,'delete_secretariapp'),(64,'Can view secretaria pp',16,'view_secretariapp'),(65,'Can add plan estudio',17,'add_planestudio'),(66,'Can change plan estudio',17,'change_planestudio'),(67,'Can delete plan estudio',17,'delete_planestudio'),(68,'Can view plan estudio',17,'view_planestudio'),(69,'Can add examen pregunta',18,'add_examenpregunta'),(70,'Can change examen pregunta',18,'change_examenpregunta'),(71,'Can delete examen pregunta',18,'delete_examenpregunta'),(72,'Can view examen pregunta',18,'view_examenpregunta'),(73,'Can add curso',19,'add_curso'),(74,'Can change curso',19,'change_curso'),(75,'Can delete curso',19,'delete_curso'),(76,'Can view curso',19,'view_curso'),(77,'Can add conferencia',20,'add_conferencia'),(78,'Can change conferencia',20,'change_conferencia'),(79,'Can delete conferencia',20,'delete_conferencia'),(80,'Can view conferencia',20,'view_conferencia'),(81,'Can add alternativa',21,'add_alternativa'),(82,'Can change alternativa',21,'change_alternativa'),(83,'Can delete alternativa',21,'delete_alternativa'),(84,'Can view alternativa',21,'view_alternativa'),(85,'Can add militante examen',22,'add_militanteexamen'),(86,'Can change militante examen',22,'change_militanteexamen'),(87,'Can delete militante examen',22,'delete_militanteexamen'),(88,'Can view militante examen',22,'view_militanteexamen'),(89,'Can add debate',23,'add_debate'),(90,'Can change debate',23,'change_debate'),(91,'Can delete debate',23,'delete_debate'),(92,'Can view debate',23,'view_debate');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(13,'api','administrador'),(21,'api','alternativa'),(20,'api','conferencia'),(19,'api','curso'),(23,'api','debate'),(8,'api','esegjne'),(9,'api','examen'),(18,'api','examenpregunta'),(14,'api','externo'),(15,'api','militante'),(22,'api','militanteexamen'),(10,'api','partidopolitico'),(11,'api','persona'),(17,'api','planestudio'),(12,'api','pregunta'),(16,'api','secretariapp'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'authtoken','token'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-02-23 23:34:24.457398'),(2,'auth','0001_initial','2020-02-23 23:34:29.074687'),(3,'admin','0001_initial','2020-02-23 23:34:55.222340'),(4,'admin','0002_logentry_remove_auto_add','2020-02-23 23:35:04.438611'),(5,'admin','0003_logentry_add_action_flag_choices','2020-02-23 23:35:04.562301'),(6,'api','0001_initial','2020-02-23 23:35:26.456700'),(7,'contenttypes','0002_remove_content_type_name','2020-02-23 23:36:35.787968'),(8,'auth','0002_alter_permission_name_max_length','2020-02-23 23:36:41.554996'),(9,'auth','0003_alter_user_email_max_length','2020-02-23 23:36:43.139001'),(10,'auth','0004_alter_user_username_opts','2020-02-23 23:36:43.330999'),(11,'auth','0005_alter_user_last_login_null','2020-02-23 23:36:48.068064'),(12,'auth','0006_require_contenttypes_0002','2020-02-23 23:36:48.485054'),(13,'auth','0007_alter_validators_add_error_messages','2020-02-23 23:36:48.750062'),(14,'auth','0008_alter_user_username_max_length','2020-02-23 23:36:53.552408'),(15,'auth','0009_alter_user_last_name_max_length','2020-02-23 23:36:58.905030'),(16,'auth','0010_alter_group_name_max_length','2020-02-23 23:36:59.768628'),(17,'auth','0011_update_proxy_permissions','2020-02-23 23:36:59.969628'),(18,'authtoken','0001_initial','2020-02-23 23:37:01.884152'),(19,'authtoken','0002_auto_20160226_1747','2020-02-23 23:37:12.532999'),(20,'sessions','0001_initial','2020-02-23 23:37:13.921054');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'cyberdemocracia'
--

--
-- Dumping routines for database 'cyberdemocracia'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-23 18:41:44
