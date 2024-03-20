-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: my_imdb
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `actors`
--

DROP TABLE IF EXISTS `actors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actors` (
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `creators`
--

DROP TABLE IF EXISTS `creators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `creators` (
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `directors`
--

DROP TABLE IF EXISTS `directors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `directors` (
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genres` (
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `movie_actor`
--

DROP TABLE IF EXISTS `movie_actor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_actor` (
  `movie_url` varchar(250) NOT NULL,
  `actor_name` varchar(100) NOT NULL,
  PRIMARY KEY (`movie_url`,`actor_name`),
  KEY `movie_actor_actors_FK` (`actor_name`),
  CONSTRAINT `movie_actor_actors_FK` FOREIGN KEY (`actor_name`) REFERENCES `actors` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `movie_actor_movies250_FK` FOREIGN KEY (`movie_url`) REFERENCES `movies250` (`url`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `movie_director`
--

DROP TABLE IF EXISTS `movie_director`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_director` (
  `movie_url` varchar(255) NOT NULL,
  `director_name` varchar(100) NOT NULL,
  PRIMARY KEY (`movie_url`,`director_name`),
  KEY `movie_director_directors_FK` (`director_name`),
  CONSTRAINT `movie_director_directors_FK` FOREIGN KEY (`director_name`) REFERENCES `directors` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `movie_director_movies250_FK` FOREIGN KEY (`movie_url`) REFERENCES `movies250` (`url`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `movie_genre`
--

DROP TABLE IF EXISTS `movie_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_genre` (
  `movie_url` varchar(255) NOT NULL,
  `genre_name` varchar(100) NOT NULL,
  PRIMARY KEY (`genre_name`,`movie_url`),
  KEY `movie_genre_movies250_FK` (`movie_url`),
  CONSTRAINT `movie_genre_genres_FK` FOREIGN KEY (`genre_name`) REFERENCES `genres` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `movie_genre_movies250_FK` FOREIGN KEY (`movie_url`) REFERENCES `movies250` (`url`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `movie_writer`
--

DROP TABLE IF EXISTS `movie_writer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_writer` (
  `movie_url` varchar(255) NOT NULL,
  `writer_name` varchar(100) NOT NULL,
  PRIMARY KEY (`movie_url`,`writer_name`),
  KEY `movie_writer_writers_FK` (`writer_name`),
  CONSTRAINT `movie_writer_movies250_FK` FOREIGN KEY (`movie_url`) REFERENCES `movies250` (`url`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `movie_writer_writers_FK` FOREIGN KEY (`writer_name`) REFERENCES `writers` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `movies250`
--

DROP TABLE IF EXISTS `movies250`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies250` (
  `url` varchar(255) NOT NULL,
  `movie_rank` smallint NOT NULL,
  `title` varchar(150) DEFAULT NULL,
  `orignal_title` varchar(150) DEFAULT NULL,
  `score` decimal(10,1) DEFAULT NULL,
  `scrapy_genres` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `year` smallint DEFAULT NULL,
  `duration` smallint DEFAULT NULL,
  `plot` text,
  `scrapy_directors` text,
  `scrapy_writers` text,
  `scrapy_stars` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `audience` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `original_language` varchar(50) DEFAULT NULL,
  `budget` bigint DEFAULT NULL,
  `gross_worldwide` bigint DEFAULT NULL,
  PRIMARY KEY (`url`),
  UNIQUE KEY `movies250_unique` (`movie_rank`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `movies250_ai` AFTER INSERT ON `movies250` FOR EACH ROW BEGIN
    DECLARE v_movie_url VARCHAR(255);
    DECLARE v_name VARCHAR(100);
    DECLARE v_separator VARCHAR(1);
    DECLARE v_start_pos INT;
    DECLARE v_end_pos INT;
    
    SET v_separator = '|';
    SET v_movie_url = NEW.url;
    
    
    -- --------- --
    -- DIRECTORS --
    -- --------- --
    SET v_start_pos = 1;
    WHILE v_start_pos > 0 AND v_start_pos <= LENGTH(NEW.scrapy_directors) DO
        SET v_end_pos = LOCATE(v_separator, NEW.scrapy_directors, v_start_pos);
        
        IF v_end_pos = 0 THEN
            SET v_end_pos = LENGTH(NEW.scrapy_directors) + 1;
        END IF;
        
        SET v_name = SUBSTRING(NEW.scrapy_directors, v_start_pos, v_end_pos - v_start_pos);
        
       	INSERT INTO directors (name)
        SELECT v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM directors WHERE name = v_name
        );
       
        INSERT INTO movie_director (movie_url, director_name)
        SELECT v_movie_url, v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM movie_director WHERE movie_url = v_movie_url AND director_name = v_name
        );
        
        SET v_start_pos = v_end_pos + 1;
    END WHILE;
    
    
    -- ------- --
    -- WRITERS --
    -- ------- --
    SET v_start_pos = 1;
    WHILE v_start_pos > 0 AND v_start_pos <= LENGTH(NEW.scrapy_writers) DO
        SET v_end_pos = LOCATE(v_separator, NEW.scrapy_writers, v_start_pos);
        
        IF v_end_pos = 0 THEN
            SET v_end_pos = LENGTH(NEW.scrapy_writers) + 1;
        END IF;
        
        SET v_name = SUBSTRING(NEW.scrapy_writers, v_start_pos, v_end_pos - v_start_pos);
        
       	INSERT INTO writers (name)
        SELECT v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM writers WHERE name = v_name
        );
       
        INSERT INTO movie_writer (movie_url, writer_name)
        SELECT v_movie_url, v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM movie_writer WHERE movie_url = v_movie_url AND writer_name = v_name
        );
        
        SET v_start_pos = v_end_pos + 1;
    END WHILE;
    
    
    -- ------ --
    -- ACTORS --
    -- ------ --
    SET v_start_pos = 1;
    WHILE v_start_pos > 0 AND v_start_pos <= LENGTH(NEW.scrapy_stars) DO
        SET v_end_pos = LOCATE(v_separator, NEW.scrapy_stars, v_start_pos);
        
        IF v_end_pos = 0 THEN
            SET v_end_pos = LENGTH(NEW.scrapy_stars) + 1;
        END IF;
        
        SET v_name = SUBSTRING(NEW.scrapy_stars, v_start_pos, v_end_pos - v_start_pos);
        
       	INSERT INTO actors (name)
        SELECT v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM actors WHERE name = v_name
        );
       
        INSERT INTO movie_actor (movie_url, actor_name)
        SELECT v_movie_url, v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM movie_actor WHERE movie_url = v_movie_url AND actor_name = v_name
        );
        
        SET v_start_pos = v_end_pos + 1;
    END WHILE;
    
    
    -- ------ --
    -- GENRES --
    -- ------ --
    SET v_start_pos = 1;
    WHILE v_start_pos > 0 AND v_start_pos <= LENGTH(NEW.scrapy_genres) DO
        SET v_end_pos = LOCATE(v_separator, NEW.scrapy_genres, v_start_pos);
        
        IF v_end_pos = 0 THEN
            SET v_end_pos = LENGTH(NEW.scrapy_genres) + 1;
        END IF;
        
        SET v_name = SUBSTRING(NEW.scrapy_genres, v_start_pos, v_end_pos - v_start_pos);
        
       	INSERT INTO genres (name)
        SELECT v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM genres WHERE name = v_name
        );
       
        INSERT INTO movie_genre (movie_url, genre_name)
        SELECT v_movie_url, v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM movie_genre WHERE movie_url = v_movie_url AND genre_name = v_name
        );
        
        SET v_start_pos = v_end_pos + 1;
    END WHILE;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `tv_shows250`
--

DROP TABLE IF EXISTS `tv_shows250`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tv_shows250` (
  `url` varchar(255) NOT NULL,
  `tvshow_rank` smallint NOT NULL,
  `title` varchar(150) DEFAULT NULL,
  `orignal_title` varchar(150) DEFAULT NULL,
  `score` decimal(10,1) DEFAULT NULL,
  `scrapy_genres` text,
  `year_start` smallint DEFAULT NULL,
  `year_stop` smallint DEFAULT NULL,
  `duration` smallint DEFAULT NULL,
  `plot` text,
  `scrapy_creators` text,
  `scrapy_stars` text,
  `audience` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `original_language` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`url`),
  UNIQUE KEY `tv_shows_unique` (`tvshow_rank`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tv_shows250_ai` AFTER INSERT ON `tv_shows250` FOR EACH ROW BEGIN
    DECLARE v_tvshow_url VARCHAR(255);
    DECLARE v_name VARCHAR(100);
    DECLARE v_separator VARCHAR(1);
    DECLARE v_start_pos INT;
    DECLARE v_end_pos INT;
    
    SET v_separator = '|';
    SET v_tvshow_url = NEW.url;
    
    
    -- --------- --
    -- CREATORS --
    -- --------- --
    SET v_start_pos = 1;
    WHILE v_start_pos > 0 AND v_start_pos <= LENGTH(NEW.scrapy_creators) DO
        SET v_end_pos = LOCATE(v_separator, NEW.scrapy_creators, v_start_pos);
        
        IF v_end_pos = 0 THEN
            SET v_end_pos = LENGTH(NEW.scrapy_creators) + 1;
        END IF;
        
        SET v_name = SUBSTRING(NEW.scrapy_creators, v_start_pos, v_end_pos - v_start_pos);
        
       	INSERT INTO creators (name)
        SELECT v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM creators WHERE name = v_name
        );
       
        INSERT INTO tvshow_creator (tvshow_url, creator_name)
        SELECT v_tvshow_url, v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM tvshow_creator WHERE tvshow_url = v_tvshow_url AND creator_name = v_name
        );
        
        SET v_start_pos = v_end_pos + 1;
    END WHILE;
    
    
    -- ------ --
    -- ACTORS --
    -- ------ --
    SET v_start_pos = 1;
    WHILE v_start_pos > 0 AND v_start_pos <= LENGTH(NEW.scrapy_stars) DO
        SET v_end_pos = LOCATE(v_separator, NEW.scrapy_stars, v_start_pos);
        
        IF v_end_pos = 0 THEN
            SET v_end_pos = LENGTH(NEW.scrapy_stars) + 1;
        END IF;
        
        SET v_name = SUBSTRING(NEW.scrapy_stars, v_start_pos, v_end_pos - v_start_pos);
        
       	INSERT INTO actors (name)
        SELECT v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM actors WHERE name = v_name
        );
       
        INSERT INTO tvshow_actor (tvshow_url, actor_name)
        SELECT v_tvshow_url, v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM tvshow_actor WHERE tvshow_url = v_tvshow_url AND actor_name = v_name
        );
        
        SET v_start_pos = v_end_pos + 1;
    END WHILE;
    
    
    -- ------ --
    -- GENRES --
    -- ------ --
    SET v_start_pos = 1;
    WHILE v_start_pos > 0 AND v_start_pos <= LENGTH(NEW.scrapy_genres) DO
        SET v_end_pos = LOCATE(v_separator, NEW.scrapy_genres, v_start_pos);
        
        IF v_end_pos = 0 THEN
            SET v_end_pos = LENGTH(NEW.scrapy_genres) + 1;
        END IF;
        
        SET v_name = SUBSTRING(NEW.scrapy_genres, v_start_pos, v_end_pos - v_start_pos);
        
       	INSERT INTO genres (name)
        SELECT v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM genres WHERE name = v_name
        );
       
        INSERT INTO tvshow_genre (tvshow_url, genre_name)
        SELECT v_tvshow_url, v_name
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM tvshow_genre WHERE tvshow_url = v_tvshow_url AND genre_name = v_name
        );
        
        SET v_start_pos = v_end_pos + 1;
    END WHILE;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `tvshow_actor`
--

DROP TABLE IF EXISTS `tvshow_actor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tvshow_actor` (
  `tvshow_url` varchar(255) NOT NULL,
  `actor_name` varchar(100) NOT NULL,
  PRIMARY KEY (`tvshow_url`,`actor_name`),
  KEY `tvshow_actor_actors_FK` (`actor_name`),
  CONSTRAINT `tvshow_actor_actors_FK` FOREIGN KEY (`actor_name`) REFERENCES `actors` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tvshow_actor_tv_shows250_FK` FOREIGN KEY (`tvshow_url`) REFERENCES `tv_shows250` (`url`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tvshow_creator`
--

DROP TABLE IF EXISTS `tvshow_creator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tvshow_creator` (
  `tvshow_url` varchar(255) NOT NULL,
  `creator_name` varchar(100) NOT NULL,
  PRIMARY KEY (`tvshow_url`,`creator_name`),
  KEY `tvshow_creator_creators_FK` (`creator_name`),
  CONSTRAINT `tvshow_creator_creators_FK` FOREIGN KEY (`creator_name`) REFERENCES `creators` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tvshow_creator_tv_shows250_FK` FOREIGN KEY (`tvshow_url`) REFERENCES `tv_shows250` (`url`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tvshow_genre`
--

DROP TABLE IF EXISTS `tvshow_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tvshow_genre` (
  `tvshow_url` varchar(255) NOT NULL,
  `genre_name` varchar(100) NOT NULL,
  PRIMARY KEY (`tvshow_url`,`genre_name`),
  KEY `tvshow_genre_genres_FK` (`genre_name`),
  CONSTRAINT `tvshow_genre_genres_FK` FOREIGN KEY (`genre_name`) REFERENCES `genres` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tvshow_genre_tv_shows250_FK` FOREIGN KEY (`tvshow_url`) REFERENCES `tv_shows250` (`url`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `writers`
--

DROP TABLE IF EXISTS `writers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `writers` (
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-20 13:57:33
