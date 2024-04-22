/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - suspecious
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`suspecious` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `suspecious`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add criminal_table',7,'add_criminal_table'),
(26,'Can change criminal_table',7,'change_criminal_table'),
(27,'Can delete criminal_table',7,'delete_criminal_table'),
(28,'Can view criminal_table',7,'view_criminal_table'),
(29,'Can add login_table',8,'add_login_table'),
(30,'Can change login_table',8,'change_login_table'),
(31,'Can delete login_table',8,'delete_login_table'),
(32,'Can view login_table',8,'view_login_table'),
(33,'Can add police_table',9,'add_police_table'),
(34,'Can change police_table',9,'change_police_table'),
(35,'Can delete police_table',9,'delete_police_table'),
(36,'Can view police_table',9,'view_police_table'),
(37,'Can add user_table',10,'add_user_table'),
(38,'Can change user_table',10,'change_user_table'),
(39,'Can delete user_table',10,'delete_user_table'),
(40,'Can view user_table',10,'view_user_table'),
(41,'Can add report_table',11,'add_report_table'),
(42,'Can change report_table',11,'change_report_table'),
(43,'Can delete report_table',11,'delete_report_table'),
(44,'Can view report_table',11,'view_report_table'),
(45,'Can add policestation_table',12,'add_policestation_table'),
(46,'Can change policestation_table',12,'change_policestation_table'),
(47,'Can delete policestation_table',12,'delete_policestation_table'),
(48,'Can view policestation_table',12,'view_policestation_table'),
(49,'Can add feedback_table',13,'add_feedback_table'),
(50,'Can change feedback_table',13,'change_feedback_table'),
(51,'Can delete feedback_table',13,'delete_feedback_table'),
(52,'Can view feedback_table',13,'view_feedback_table'),
(53,'Can add complaint_table',14,'add_complaint_table'),
(54,'Can change complaint_table',14,'change_complaint_table'),
(55,'Can delete complaint_table',14,'delete_complaint_table'),
(56,'Can view complaint_table',14,'view_complaint_table'),
(57,'Can add assigntask_table',15,'add_assigntask_table'),
(58,'Can change assigntask_table',15,'change_assigntask_table'),
(59,'Can delete assigntask_table',15,'delete_assigntask_table'),
(60,'Can view assigntask_table',15,'view_assigntask_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(15,'suspecious_activity','assigntask_table'),
(14,'suspecious_activity','complaint_table'),
(7,'suspecious_activity','criminal_table'),
(13,'suspecious_activity','feedback_table'),
(8,'suspecious_activity','login_table'),
(9,'suspecious_activity','police_table'),
(12,'suspecious_activity','policestation_table'),
(11,'suspecious_activity','report_table'),
(10,'suspecious_activity','user_table');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-02-09 23:23:44.705022'),
(2,'auth','0001_initial','2024-02-09 23:23:45.616414'),
(3,'admin','0001_initial','2024-02-09 23:23:45.768312'),
(4,'admin','0002_logentry_remove_auto_add','2024-02-09 23:23:45.784307'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-02-09 23:23:45.800293'),
(6,'contenttypes','0002_remove_content_type_name','2024-02-09 23:23:45.896228'),
(7,'auth','0002_alter_permission_name_max_length','2024-02-09 23:23:45.984169'),
(8,'auth','0003_alter_user_email_max_length','2024-02-09 23:23:46.024142'),
(9,'auth','0004_alter_user_username_opts','2024-02-09 23:23:46.032140'),
(10,'auth','0005_alter_user_last_login_null','2024-02-09 23:23:46.096096'),
(11,'auth','0006_require_contenttypes_0002','2024-02-09 23:23:46.104089'),
(12,'auth','0007_alter_validators_add_error_messages','2024-02-09 23:23:46.112083'),
(13,'auth','0008_alter_user_username_max_length','2024-02-09 23:23:46.184560'),
(14,'auth','0009_alter_user_last_name_max_length','2024-02-09 23:23:46.256511'),
(15,'auth','0010_alter_group_name_max_length','2024-02-09 23:23:46.288490'),
(16,'auth','0011_update_proxy_permissions','2024-02-09 23:23:46.304479'),
(17,'auth','0012_alter_user_first_name_max_length','2024-02-09 23:23:46.392420'),
(18,'sessions','0001_initial','2024-02-09 23:23:46.440388'),
(19,'suspecious_activity','0001_initial','2024-02-09 23:23:47.191888');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

/*Table structure for table `suspecious_activity_assigntask_table` */

DROP TABLE IF EXISTS `suspecious_activity_assigntask_table`;

CREATE TABLE `suspecious_activity_assigntask_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `task` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `status` varchar(100) NOT NULL,
  `policeid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `suspecious_activity__policeid_id_193b5359_fk_suspeciou` (`policeid_id`),
  CONSTRAINT `suspecious_activity__policeid_id_193b5359_fk_suspeciou` FOREIGN KEY (`policeid_id`) REFERENCES `suspecious_activity_police_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `suspecious_activity_assigntask_table` */

insert  into `suspecious_activity_assigntask_table`(`id`,`task`,`date`,`time`,`status`,`policeid_id`) values 
(1,'robbery','2024-02-12','10:00:00.000000','not completed',1);

/*Table structure for table `suspecious_activity_complaint_table` */

DROP TABLE IF EXISTS `suspecious_activity_complaint_table`;

CREATE TABLE `suspecious_activity_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint_details` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL,
  `policestation_id` bigint NOT NULL,
  `userid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `suspecious_activity__policestation_id_fa88ae71_fk_suspeciou` (`policestation_id`),
  KEY `suspecious_activity__userid_id_0c2f1d8e_fk_suspeciou` (`userid_id`),
  CONSTRAINT `suspecious_activity__policestation_id_fa88ae71_fk_suspeciou` FOREIGN KEY (`policestation_id`) REFERENCES `suspecious_activity_policestation_table` (`id`),
  CONSTRAINT `suspecious_activity__userid_id_0c2f1d8e_fk_suspeciou` FOREIGN KEY (`userid_id`) REFERENCES `suspecious_activity_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `suspecious_activity_complaint_table` */

insert  into `suspecious_activity_complaint_table`(`id`,`complaint_details`,`date`,`reply`,`report`,`policestation_id`,`userid_id`) values 
(1,'murder','2024-02-20','updation','comp',2,2);

/*Table structure for table `suspecious_activity_criminal_table` */

DROP TABLE IF EXISTS `suspecious_activity_criminal_table`;

CREATE TABLE `suspecious_activity_criminal_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `age` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `suspecious_activity_criminal_table` */

insert  into `suspecious_activity_criminal_table`(`id`,`Fname`,`lname`,`photo`,`place`,`age`) values 
(1,'amina','shibilin','nil','edpal',23);

/*Table structure for table `suspecious_activity_feedback_table` */

DROP TABLE IF EXISTS `suspecious_activity_feedback_table`;

CREATE TABLE `suspecious_activity_feedback_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `rating` double NOT NULL,
  `userid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `suspecious_activity__userid_id_d28ff0e9_fk_suspeciou` (`userid_id`),
  CONSTRAINT `suspecious_activity__userid_id_d28ff0e9_fk_suspeciou` FOREIGN KEY (`userid_id`) REFERENCES `suspecious_activity_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `suspecious_activity_feedback_table` */

insert  into `suspecious_activity_feedback_table`(`id`,`feedback`,`date`,`rating`,`userid_id`) values 
(1,'good','2024-02-20',5,1);

/*Table structure for table `suspecious_activity_login_table` */

DROP TABLE IF EXISTS `suspecious_activity_login_table`;

CREATE TABLE `suspecious_activity_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `suspecious_activity_login_table` */

insert  into `suspecious_activity_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','123','admin'),
(2,'nesrin','1234','station'),
(3,'user','098','user');

/*Table structure for table `suspecious_activity_police_table` */

DROP TABLE IF EXISTS `suspecious_activity_police_table`;

CREATE TABLE `suspecious_activity_police_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `gender` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL,
  `login_id` bigint NOT NULL,
  `policestation_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `suspecious_activity__policestation_id_4002aee7_fk_suspeciou` (`policestation_id`),
  KEY `suspecious_activity__login_id_5c1b48da_fk_suspeciou` (`login_id`),
  CONSTRAINT `suspecious_activity__login_id_5c1b48da_fk_suspeciou` FOREIGN KEY (`login_id`) REFERENCES `suspecious_activity_login_table` (`id`),
  CONSTRAINT `suspecious_activity__policestation_id_4002aee7_fk_suspeciou` FOREIGN KEY (`policestation_id`) REFERENCES `suspecious_activity_policestation_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `suspecious_activity_police_table` */

insert  into `suspecious_activity_police_table`(`id`,`Name`,`place`,`phone`,`gender`,`email`,`login_id`,`policestation_id`) values 
(1,'amal','idukki',8756789867,'male','amal2gmail.com',2,1);

/*Table structure for table `suspecious_activity_policestation_table` */

DROP TABLE IF EXISTS `suspecious_activity_policestation_table`;

CREATE TABLE `suspecious_activity_policestation_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(25) NOT NULL,
  `login_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `suspecious_activity__login_id_0283a801_fk_suspeciou` (`login_id`),
  CONSTRAINT `suspecious_activity__login_id_0283a801_fk_suspeciou` FOREIGN KEY (`login_id`) REFERENCES `suspecious_activity_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `suspecious_activity_policestation_table` */

insert  into `suspecious_activity_policestation_table`(`id`,`Name`,`place`,`phone`,`email`,`login_id`) values 
(1,'aravindh','palakkad',9867456790,'ar@gmail.com',2),
(2,'raman','edappally',9876543456,'ram@gmail.com',2);

/*Table structure for table `suspecious_activity_report_table` */

DROP TABLE IF EXISTS `suspecious_activity_report_table`;

CREATE TABLE `suspecious_activity_report_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `task` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `report` varchar(100) NOT NULL,
  `policeid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `suspecious_activity__policeid_id_1a4d4fb1_fk_suspeciou` (`policeid_id`),
  CONSTRAINT `suspecious_activity__policeid_id_1a4d4fb1_fk_suspeciou` FOREIGN KEY (`policeid_id`) REFERENCES `suspecious_activity_police_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `suspecious_activity_report_table` */

insert  into `suspecious_activity_report_table`(`id`,`task`,`date`,`report`,`policeid_id`) values 
(1,'murder','2023-12-30','completed',1);

/*Table structure for table `suspecious_activity_user_table` */

DROP TABLE IF EXISTS `suspecious_activity_user_table`;

CREATE TABLE `suspecious_activity_user_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(25) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(25) NOT NULL,
  `login_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `suspecious_activity__login_id_05a036d6_fk_suspeciou` (`login_id`),
  CONSTRAINT `suspecious_activity__login_id_05a036d6_fk_suspeciou` FOREIGN KEY (`login_id`) REFERENCES `suspecious_activity_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `suspecious_activity_user_table` */

insert  into `suspecious_activity_user_table`(`id`,`fname`,`lname`,`dob`,`gender`,`place`,`post`,`pin`,`phone`,`email`,`login_id`) values 
(1,'nesrin','fathima','2002-12-20','female','edappal','kolamba',679576,23456789,'fenen@gmail.com',1),
(2,'amal','shirin','2023-08-17','female','kunamkulam','edapal',896745,1234678,'amu@gemail.com',2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
