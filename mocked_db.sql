-- MySQL dump 10.13  Distrib 5.7.44, for Linux (x86_64)
--
-- Host: localhost    Database: toro_test_db
-- ------------------------------------------------------
-- Server version	5.7.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account` (
  `acc_code` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `cpf` varchar(11) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `hashed_password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`acc_code`),
  KEY `ix_account_acc_code` (`acc_code`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (1,'Thaynara Bertossi','00484392077',5500,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(2,'Ana Souza','23456789012',3200,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(3,'André Nogueira','13981594762',875.5,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(4,'Maria Oliveira','45678901234',1299.99,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(5,'Pedro Costa','56789012345',563.75,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(6,'Laura Rocha','67890123456',10950.3,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(7,'Fernanda Almeida','78901234567',495,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(8,'Ricardo Santos','89012345678',7000.5,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(9,'Patrícia Silva','90123456789',150.75,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(10,'Rafael Correia','01234567890',3400.25,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(11,'Juliana Ribeiro','12345098765',825,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(12,'Paulo Martins','23456098765',5000,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(13,'Simone Pereira','34567098765',2750.75,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(14,'Thiago Silva','45678098765',660,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(15,'Mariana Fernandes','56789098765',12500,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(16,'Roberto Carvalho','67890109876',200.45,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(17,'Beatriz Castro','78901209876',3800.75,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(18,'Igor Andrade','89012309876',970,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(19,'Aline Mendes','90123409876',4500.5,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(20,'Gabriel Farias','01234509876',2150.3,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(21,'Jéssica Macedo','12345698765',1100,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(22,'Lucas Barros','23456798765',890,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(23,'Cláudia Lopes','34567898765',635.5,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(24,'Henrique Neves','45678998765',10350.8,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(25,'Letícia Amorim','56789098765',210.25,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(26,'André Ribeiro','67890198765',6000,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(27,'Vanessa Silva','78901298765',125.75,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(28,'Eduardo Oliveira','89012398765',470,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(29,'Bruna Fernandes','90123498765',7500.25,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2'),(30,'Felipe Costa','01234598765',999.5,'$2b$12$aIWW/rEU5z5lq5mqLipGjuBllparaX1uSDg13I8qCW7rwqwVUiPE2');
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `position`
--

DROP TABLE IF EXISTS `position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `position` (
  `id_position` int(11) NOT NULL AUTO_INCREMENT,
  `acc_code` int(11) DEFAULT NULL,
  `symbol` varchar(10) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `last_price` float DEFAULT NULL,
  PRIMARY KEY (`id_position`),
  KEY `acc_code` (`acc_code`),
  KEY `ix_position_id_position` (`id_position`),
  CONSTRAINT `position_ibfk_1` FOREIGN KEY (`acc_code`) REFERENCES `account` (`acc_code`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `position`
--

LOCK TABLES `position` WRITE;
/*!40000 ALTER TABLE `position` DISABLE KEYS */;
INSERT INTO `position` VALUES (1,1,'PETR4',20,28.5),(2,1,'VALE3',10,65),(3,1,'ITUB4',15,27.4),(4,1,'BBDC4',18,23.7),(5,2,'ABEV3',30,14.9),(6,2,'BBAS3',12,41.25),(7,2,'GGBR4',25,28.75),(8,2,'WEGE3',10,38.9),(9,2,'RENT3',8,56.5),(10,3,'MGLU3',40,3.2),(11,3,'PETR4',15,28.6),(12,3,'VALE3',20,64.8),(13,3,'ITUB4',5,27.3),(14,3,'BBDC4',12,23.5),(15,4,'ABEV3',50,15),(16,4,'BBAS3',8,41),(17,4,'GGBR4',14,28.4),(18,4,'WEGE3',6,39.1),(19,4,'RENT3',10,56.25),(20,5,'MGLU3',45,3.15),(21,5,'PETR4',25,28.4),(22,5,'VALE3',18,65.1),(23,5,'ITUB4',20,27.35),(24,5,'BBDC4',10,23.65),(25,6,'ABEV3',35,14.85),(26,6,'BBAS3',7,41.5),(27,6,'GGBR4',13,28.8),(28,6,'WEGE3',9,39),(29,6,'RENT3',11,56.4),(30,7,'MGLU3',33,3.1),(31,7,'PETR4',17,28.7),(32,7,'VALE3',9,64.9),(33,7,'ITUB4',22,27.45),(34,7,'BBDC4',13,23.85),(35,8,'ABEV3',42,14.95),(36,8,'BBAS3',16,41.15),(37,8,'GGBR4',18,28.9),(38,8,'WEGE3',5,39.05),(39,8,'RENT3',12,56.2),(40,9,'MGLU3',29,3.25),(41,9,'PETR4',23,28.55),(42,9,'VALE3',11,65.25),(43,9,'ITUB4',19,27.5),(44,9,'BBDC4',7,23.75),(45,10,'ABEV3',36,14.8),(46,10,'BBAS3',9,41.45),(47,10,'GGBR4',21,28.95),(48,10,'WEGE3',14,39.2),(49,10,'RENT3',6,56),(50,1,'MGLU3',32,3.05),(51,2,'PETR4',24,28.65),(52,3,'VALE3',17,64.95),(53,4,'ITUB4',11,27.55),(54,5,'BBDC4',5,23.95),(55,6,'ABEV3',26,14.75),(56,7,'BBAS3',20,41.1),(57,8,'GGBR4',15,28.65),(58,9,'WEGE3',18,39.3),(59,10,'RENT3',4,56.1),(60,1,'MGLU3',37,3.18);
/*!40000 ALTER TABLE `position` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-07 15:57:34
