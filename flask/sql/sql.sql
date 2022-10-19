/*
SQLyog Enterprise v12.13 (64 bit)
MySQL - 5.7.31-0ubuntu0.18.04.1-log : Database - treinamento_daila
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`treinamento_daila` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `treinamento_daila`;

/*Table structure for table `aluno` */

DROP TABLE IF EXISTS `aluno`;

CREATE TABLE `aluno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL,
  `cpf` varchar(20) NOT NULL,
  `matricula` varchar(50) NOT NULL,
  `telefone` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `matricula` (`matricula`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `aluno` */

insert  into `aluno`(`id`,`nome`,`cpf`,`matricula`,`telefone`) values (1,'Daila','02362909670','0000405115','31982829363'),(2,'Fernando','01010101010','0000405116','3199999999'),(3,'Gabriela','25874195836','0000405118','21985741548'),(4,'Geysi','025987415489','00004058749','215874968574'),(5,'Euler','58748596425','051548','245164.85947'),(6,'Luiz','58749685742','000041548','319857496852'),(9,'sabrina','5874968521','0000487592','319857496');

/*Table structure for table `emprestimo` */

DROP TABLE IF EXISTS `emprestimo`;

CREATE TABLE `emprestimo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fk_id_aluno` int(11) DEFAULT NULL,
  `fk_id_livro` int(11) DEFAULT NULL,
  `data_emprestimo` date NOT NULL,
  `data_devolucao` date NOT NULL,
  `situação` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_id_aluno` (`fk_id_aluno`),
  KEY `fk_id_livro` (`fk_id_livro`),
  CONSTRAINT `emprestimo_ibfk_1` FOREIGN KEY (`fk_id_aluno`) REFERENCES `aluno` (`id`),
  CONSTRAINT `emprestimo_ibfk_2` FOREIGN KEY (`fk_id_livro`) REFERENCES `livro` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `emprestimo` */

insert  into `emprestimo`(`id`,`fk_id_aluno`,`fk_id_livro`,`data_emprestimo`,`data_devolucao`,`situação`) values (1,2,2,'2022-09-28','2022-09-29',NULL),(2,6,5,'2022-09-30','2022-10-31',NULL),(3,6,8,'2022-09-29','2022-09-30',NULL),(4,5,5,'2022-10-04','2022-10-05',NULL),(5,4,7,'2022-10-03','2022-10-04',NULL);

/*Table structure for table `livro` */

DROP TABLE IF EXISTS `livro`;

CREATE TABLE `livro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `isbn` varchar(50) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `editora` varchar(50) NOT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `isbn` (`isbn`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `livro` */

insert  into `livro`(`id`,`isbn`,`nome`,`editora`,`tipo`) values (1,'0005','as aventuras de poliana','poliana','infantil'),(2,'0002','Pai rico pai pobre','Kiyosaki','mental'),(3,'0003','um menino maluquinho','alguem','infantil'),(4,'850205564X','A PROVA NO PROCESSO CIVIL','SARAIVA','ESTUDO'),(5,'850205709X','JIU-JITSU GRACIE','SARAIVA','ESPORTE'),(6,'850105030X','TERRAS DO SEM FIM','Não definido','Romance'),(7,'850105061X','O PAPAGAIO E O DOUTOR','Não definido','Romance'),(8,'850201773X','BIOLOGIA - A NATUREZA VIVA','SARAIVA','Educação'),(9,'850201806X','CODIGO DE PROCESSO PENAL MILITAR','SARAIVA','Direito');

/*Table structure for table `usuario` */

DROP TABLE IF EXISTS `usuario`;

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL,
  `cpf` varchar(50) NOT NULL,
  `telefone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `senha` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `usuario` (`usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `usuario` */

insert  into `usuario`(`id`,`nome`,`cpf`,`telefone`,`email`,`usuario`,`senha`) values (2,'daila danielle de oliveira santos','0000000000','3182829363','daila@gmail.com','daila14','123'),(3,'luiz','000001548745','215487458','luiz@gmail.com','luiz','123'),(4,'paulo mariano','97830045874','319858574','paulo123@gmail.com','paulo','12345'),(5,'fabiano jose','58749685741','3198256241','fabiano@gmail.com','fabiano','123');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
