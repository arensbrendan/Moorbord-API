CREATE DATABASE  IF NOT EXISTS `new` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `new`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 69.247.163.204    Database: new
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  PRIMARY KEY (`admin_id`),
  KEY `admin_user_id_idx` (`user_id`),
  CONSTRAINT `admin_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` VALUES (1,40);

--
-- Table structure for table `chair`
--

DROP TABLE IF EXISTS `chair`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chair` (
  `chair_id` int NOT NULL AUTO_INCREMENT,
  `chair_x` int NOT NULL DEFAULT '0',
  `chair_y` int NOT NULL DEFAULT '0',
  `student_id` int DEFAULT NULL,
  `class_id` int NOT NULL,
  PRIMARY KEY (`chair_id`),
  KEY `chair_student_id_idx` (`student_id`),
  KEY `chair_class_id_idx` (`class_id`),
  CONSTRAINT `chair_class_id` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`),
  CONSTRAINT `chair_student_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='X/Y in pixels';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chair`
--


--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class` (
  `class_id` int NOT NULL AUTO_INCREMENT,
  `teacher_id` int DEFAULT NULL,
  `class_name` varchar(255) NOT NULL,
  `hour` tinyint(1) NOT NULL,
  PRIMARY KEY (`class_id`),
  UNIQUE KEY `class_id_UNIQUE` (`class_id`),
  KEY `teacher_id_idx` (`teacher_id`),
  CONSTRAINT `teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

INSERT INTO `class` VALUES (5,1,'crookery for dummies',1);
INSERT INTO `class` VALUES (6,1,'mathematics 1',2);
INSERT INTO `class` VALUES (7,NULL,'calculus 9000',5);

--
-- Table structure for table `guardian`
--

DROP TABLE IF EXISTS `guardian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guardian` (
  `guardian_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  PRIMARY KEY (`guardian_id`),
  KEY `guardian_user_id_idx` (`user_id`),
  CONSTRAINT `guardian_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guardian`
--

INSERT INTO `guardian` VALUES (1,50);

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `log_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` int NOT NULL,
  `log` varchar(255) NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `user_id_idx` (`user_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

INSERT INTO `log` VALUES (29,'2023-01-21 03:29:17',1,'Login {\"username\": \"TU100001\", \"password\": \"passwd\"}');

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `user_id` int NOT NULL,
  `password` varchar(255) NOT NULL,
  UNIQUE KEY `username_UNIQUE` (`user_id`),
  CONSTRAINT `login_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

INSERT INTO `login` VALUES (1,'passwd');
INSERT INTO `login` VALUES (51,'password2');

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `role_id` int NOT NULL,
  `role_name` char(10) NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

INSERT INTO `role` VALUES (0,'Student');
INSERT INTO `role` VALUES (1,'Parent');
INSERT INTO `role` VALUES (2,'Teacher');
INSERT INTO `role` VALUES (3,'Admin');

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room` (
  `room_id` int NOT NULL AUTO_INCREMENT,
  `room_name` varchar(45) NOT NULL,
  `room_length` int NOT NULL,
  `room_width` int NOT NULL,
  PRIMARY KEY (`room_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Length/Width in pixels';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--


--
-- Temporary view structure for view `select_all_admin`
--

DROP TABLE IF EXISTS `select_all_admin`;
/*!50001 DROP VIEW IF EXISTS `select_all_admin`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `select_all_admin` AS SELECT 
 1 AS `user_id`,
 1 AS `username`,
 1 AS `first_name`,
 1 AS `last_name`,
 1 AS `email`,
 1 AS `phone_num`,
 1 AS `role_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `select_all_guardians`
--

DROP TABLE IF EXISTS `select_all_guardians`;
/*!50001 DROP VIEW IF EXISTS `select_all_guardians`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `select_all_guardians` AS SELECT 
 1 AS `user_id`,
 1 AS `username`,
 1 AS `first_name`,
 1 AS `last_name`,
 1 AS `email`,
 1 AS `phone_num`,
 1 AS `role_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `select_all_students`
--

DROP TABLE IF EXISTS `select_all_students`;
/*!50001 DROP VIEW IF EXISTS `select_all_students`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `select_all_students` AS SELECT 
 1 AS `user_id`,
 1 AS `username`,
 1 AS `first_name`,
 1 AS `last_name`,
 1 AS `email`,
 1 AS `phone_num`,
 1 AS `role_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `select_all_teachers`
--

DROP TABLE IF EXISTS `select_all_teachers`;
/*!50001 DROP VIEW IF EXISTS `select_all_teachers`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `select_all_teachers` AS SELECT 
 1 AS `user_id`,
 1 AS `username`,
 1 AS `first_name`,
 1 AS `last_name`,
 1 AS `email`,
 1 AS `phone_num`,
 1 AS `role_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `grade` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`student_id`),
  KEY `user_id_idx` (`user_id`),
  CONSTRAINT `student_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

INSERT INTO `student` VALUES (1,1,7);
INSERT INTO `student` VALUES (2,12,9);
INSERT INTO `student` VALUES (3,2,4);

--
-- Table structure for table `student_classes`
--

DROP TABLE IF EXISTS `student_classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_classes` (
  `student_id` int NOT NULL,
  `class_id` int NOT NULL,
  PRIMARY KEY (`student_id`,`class_id`),
  KEY `class_id_idx` (`class_id`),
  KEY `student_id_idx` (`student_id`),
  CONSTRAINT `class_id` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`),
  CONSTRAINT `student_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_classes`
--

INSERT INTO `student_classes` VALUES (1,5);
INSERT INTO `student_classes` VALUES (2,5);
INSERT INTO `student_classes` VALUES (3,7);

--
-- Table structure for table `student_guardians`
--

DROP TABLE IF EXISTS `student_guardians`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_guardians` (
  `student_id` int NOT NULL,
  `guardian_id` int NOT NULL,
  PRIMARY KEY (`student_id`,`guardian_id`),
  KEY `student_id_sg_idx` (`student_id`),
  KEY `guardian_id_sg_idx` (`guardian_id`),
  CONSTRAINT `guardian_id_sg` FOREIGN KEY (`guardian_id`) REFERENCES `guardian` (`guardian_id`),
  CONSTRAINT `student_id_sg` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_guardians`
--

INSERT INTO `student_guardians` VALUES (1,1);

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `teacher_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  PRIMARY KEY (`teacher_id`),
  KEY `teacher_user_id_idx` (`user_id`),
  CONSTRAINT `teacher_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` VALUES (1,30);

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` char(8) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone_num` char(10) DEFAULT NULL,
  `role_id` int NOT NULL DEFAULT '0' COMMENT '0: Student\\n1: Parent\\n2: Teacher\\n3: Admin',
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  KEY `role_id_idx` (`role_id`),
  CONSTRAINT `role_id` FOREIGN KEY (`role_id`) REFERENCES `role` (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

INSERT INTO `user` VALUES (1,'TU100001','test','mctest','mlm13510@ucmo.edu',NULL,3);
INSERT INTO `user` VALUES (2,'SE100002','yeet','mckskeet','blah@gmail.com',NULL,3);
INSERT INTO `user` VALUES (12,'MT100003','mctest','test','bigfatcalculator@yahoo.com',NULL,3);
INSERT INTO `user` VALUES (30,'TC100004','teach1','teach1','teach@teach.com',NULL,2);
INSERT INTO `user` VALUES (40,'AD100005','adm1','adm1','adm@admin.com',NULL,0);
INSERT INTO `user` VALUES (50,'GD100006','par1','par1','par@parent.com',NULL,1);
INSERT INTO `user` VALUES (51,'TD100007','Trey','Davis','treydogdavis@gmail.com',NULL,0);

--
-- Dumping events for database 'new'
--

--
-- Dumping routines for database 'new'
--
/*!50003 DROP PROCEDURE IF EXISTS `get_passwd_from_username` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`api`@`%` PROCEDURE `get_passwd_from_username`(IN uName VARCHAR(8))
BEGIN
	SELECT password FROM new.login WHERE user_id = (SELECT user_id from new.user WHERE username = uName);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_user_id_from_username` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`api`@`%` PROCEDURE `get_user_id_from_username`(IN uName VARCHAR(8))
BEGIN
	SELECT password FROM new.login WHERE user_id = (SELECT user_id from new.user WHERE username = uName);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `select_all_admin`
--

/*!50001 DROP VIEW IF EXISTS `select_all_admin`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`153.91.106.138` SQL SECURITY DEFINER */
/*!50001 VIEW `select_all_admin` AS select `user`.`user_id` AS `user_id`,`user`.`username` AS `username`,`user`.`first_name` AS `first_name`,`user`.`last_name` AS `last_name`,`user`.`email` AS `email`,`user`.`phone_num` AS `phone_num`,`user`.`role_id` AS `role_id` from (`user` join `admin` on((`admin`.`user_id` = `user`.`user_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `select_all_guardians`
--

/*!50001 DROP VIEW IF EXISTS `select_all_guardians`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`153.91.106.138` SQL SECURITY DEFINER */
/*!50001 VIEW `select_all_guardians` AS select `user`.`user_id` AS `user_id`,`user`.`username` AS `username`,`user`.`first_name` AS `first_name`,`user`.`last_name` AS `last_name`,`user`.`email` AS `email`,`user`.`phone_num` AS `phone_num`,`user`.`role_id` AS `role_id` from (`user` join `guardian` on((`guardian`.`user_id` = `user`.`user_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `select_all_students`
--

/*!50001 DROP VIEW IF EXISTS `select_all_students`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`153.91.106.138` SQL SECURITY DEFINER */
/*!50001 VIEW `select_all_students` AS select `user`.`user_id` AS `user_id`,`user`.`username` AS `username`,`user`.`first_name` AS `first_name`,`user`.`last_name` AS `last_name`,`user`.`email` AS `email`,`user`.`phone_num` AS `phone_num`,`user`.`role_id` AS `role_id` from (`user` join `student` on((`student`.`user_id` = `user`.`user_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `select_all_teachers`
--

/*!50001 DROP VIEW IF EXISTS `select_all_teachers`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`153.91.106.138` SQL SECURITY DEFINER */
/*!50001 VIEW `select_all_teachers` AS select `user`.`user_id` AS `user_id`,`user`.`username` AS `username`,`user`.`first_name` AS `first_name`,`user`.`last_name` AS `last_name`,`user`.`email` AS `email`,`user`.`phone_num` AS `phone_num`,`user`.`role_id` AS `role_id` from (`user` join `teacher` on((`teacher`.`user_id` = `user`.`user_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-27 13:20:50
