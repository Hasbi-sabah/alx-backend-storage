-- script that creates a table users following requirements
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	email VARCHAR(225) UNIQUE NOT NULL,
	name VARCHAR(225),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
)
