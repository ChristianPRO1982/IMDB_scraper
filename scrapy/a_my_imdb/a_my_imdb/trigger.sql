CREATE DEFINER=`root`@`localhost` TRIGGER `movies250_ai` AFTER INSERT ON `movies250` FOR EACH ROW BEGIN
    DECLARE movie_url VARCHAR(255);
    DECLARE director_name VARCHAR(100);
    DECLARE director_separator VARCHAR(1);
    DECLARE director_start_pos INT;
    DECLARE director_end_pos INT;
    
    SET director_separator = '|';
    SET director_start_pos = 1;
   
    SET movie_url = NEW.url;
    
    -- Loop through the scrapy_directors values
    WHILE director_start_pos > 0 DO
        SET director_end_pos = LOCATE(director_separator, NEW.scrapy_directors, director_start_pos);
        
        IF director_end_pos = 0 THEN
            SET director_end_pos = LENGTH(NEW.scrapy_directors) + 1;
        END IF;
        
        SET director_name = SUBSTRING(NEW.scrapy_directors, director_start_pos, director_end_pos - director_start_pos);
        
        -- Insert director_name into directors table
--        	INSERT INTO directors (name)
--         SELECT director_name
--         FROM dual
--         WHERE NOT EXISTS (
--             SELECT 1 FROM directors WHERE name = director_name
--         );
        
        SET director_start_pos = director_end_pos + 1;
    END WHILE;
END