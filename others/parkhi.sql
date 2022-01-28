-- MySQL dump 10.13  Distrib 5.5.30, for Win64 (x86)
--
-- Host: localhost    Database: sample
-- ------------------------------------------------------
-- Server version	5.5.30

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
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bill` (
  `P_ID` int(11) NOT NULL,
  `P_Name` varchar(20) NOT NULL,
  `P_Age` int(11) NOT NULL,
  `Medicines` varchar(20) NOT NULL,
  `Room` int(11) NOT NULL,
  `Total_Bill` int(11) NOT NULL,
  PRIMARY KEY (`P_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (101,'Arundhati',45,'Azithral500',33,120),(102,'Rahul',34,'Azithral250',32,130),(103,'Chandramukhi',40,'Ascoril',31,108),(104,'Annabelle',30,'ABC',30,1111),(105,'Monalisa',30,'FCC',29,4564),(106,'Atharv',34,'Dolo',28,434),(107,'Varun',33,'Dolo',29,434),(108,'Vandhna',23,'Ascoril',23,108),(109,'Gopal',46,'Ascoril',13,108),(110,'Raju',34,'Anovate Cream',12,122);
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `doctor` (
  `ID` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Age` int(11) NOT NULL,
  `Department` varchar(20) NOT NULL,
  `Phone` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Phone` (`Phone`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (91,'Parkhi Jain',25,'Cardiologist',34565),(92,'Prerna',25,'Psychiatrist',17643),(93,'Gopal',32,'Therepist',65243),(94,'Vimarsh',25,'Dermatologist',987657),(95,'Raman',34,'Psychiatrist',8767564),(96,'Khyati',25,'Physician',9758465),(97,'Trapti',25,'Dermatologist',75846567),(98,'Rohit',34,'Dietitian',987678656),(99,'Shourya',25,'Psychiatrist',9867576),(100,'Riya',34,'Dietition',676546);
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login` (
  `NAME` varchar(20) DEFAULT NULL,
  `PHONE_NO` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_1`
--

DROP TABLE IF EXISTS `login_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login_1` (
  `NAME` varchar(20) DEFAULT NULL,
  `PHONE_NO` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_1`
--

LOCK TABLES `login_1` WRITE;
/*!40000 ALTER TABLE `login_1` DISABLE KEYS */;
/*!40000 ALTER TABLE `login_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_1067`
--

DROP TABLE IF EXISTS `login_1067`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login_1067` (
  `NAME` varchar(20) DEFAULT NULL,
  `PHONE_NO` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_1067`
--

LOCK TABLES `login_1067` WRITE;
/*!40000 ALTER TABLE `login_1067` DISABLE KEYS */;
INSERT INTO `login_1067` VALUES ('PARKHI',1067),('parkhi',1067),('Palku',123),('Prerna',827345),('pARKHI',2344),('Parkhi',333);
/*!40000 ALTER TABLE `login_1067` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine`
--

DROP TABLE IF EXISTS `medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medicine` (
  `Name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine`
--

LOCK TABLES `medicine` WRITE;
/*!40000 ALTER TABLE `medicine` DISABLE KEYS */;
INSERT INTO `medicine` VALUES ('Paracitamol'),('Disprin'),('Azitral 500 Tablet'),('Dolo 500'),('Dolo 250'),('Anovate Cream');
/*!40000 ALTER TABLE `medicine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicines`
--

DROP TABLE IF EXISTS `medicines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medicines` (
  `M_ID` int(11) NOT NULL,
  `M_Name` varchar(20) NOT NULL,
  `M_Price` int(11) NOT NULL,
  PRIMARY KEY (`M_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicines`
--

LOCK TABLES `medicines` WRITE;
/*!40000 ALTER TABLE `medicines` DISABLE KEYS */;
INSERT INTO `medicines` VALUES (100,'Ampicillin',987),(101,'Paracetamol',50),(102,'Doxophyline',500),(103,'Diazepum',1000),(104,'Ondansetron',550),(105,'Mebendazole',123);
/*!40000 ALTER TABLE `medicines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patients` (
  `Name` varchar(20) NOT NULL,
  `ID` int(11) NOT NULL,
  `City` varchar(20) NOT NULL,
  `RoomNO` varchar(6) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES ('Raman',10,'Nagpur','43'),('Raunak',30,'Etawah','45'),('Raju',40,'Noida','46'),('Anamika',50,'Bhopal','47'),('Rohit',60,'Bhopal','48'),('Varun',80,'Delhi','50'),('Priyanshu',90,'Jaipur','51'),('Priyanshi',100,'Mumbai','52');
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `staff` (
  `Name` varchar(20) DEFAULT NULL,
  `Staff_ID` int(11) DEFAULT NULL,
  `Department` varchar(20) DEFAULT NULL,
  `Dept_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff1`
--

DROP TABLE IF EXISTS `staff1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `staff1` (
  `Name` varchar(20) NOT NULL,
  `ID` int(11) NOT NULL,
  `Department` varchar(20) NOT NULL,
  `Dept_ID` int(11) DEFAULT NULL,
  `City` varchar(20) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Dept_ID` (`Dept_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff1`
--

LOCK TABLES `staff1` WRITE;
/*!40000 ALTER TABLE `staff1` DISABLE KEYS */;
INSERT INTO `staff1` VALUES ('Ayush',101,'Receptionist',81,'Jaipur'),('Arushi',102,'Receptionist',82,'Delhi'),('Ritika',103,'Psychiatrist',65,'Mumbai'),('Ajit',104,'Pharmacy',89,'Delhi'),('Sherya',105,'Dietician',67,'Mumbai'),('Prerna',106,'Cardiologist',43,'Hyderabad'),('Maya',107,'Nurse',56,'Jaipur'),('Vaibhav',108,'Orthopaedics',34,'Banglore'),('Vandhana',109,'Dentist',23,'Jaipur'),('Atharv',110,'Counsellor',24,'Banglore');
/*!40000 ALTER TABLE `staff1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-16 22:39:42
