-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(225), IN score float)
BEGIN
	IF NOT EXISTS (select * from projects where name = project_name) 
		THEN INSERT INTO projects (name) VALUES (project_name);
	END IF;
	set @id = (select id from projects where name = project_name);
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @id, score);
END $$
DELIMITER ;
