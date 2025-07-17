-- Create user_0d_1 with only expected privileges (no excessive GRANT OPTION or extra roles)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';

GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN,
       PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER,
       CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE,
       REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, 
       ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, 
       CREATE ROLE, DROP ROLE 
ON *.* TO 'user_0d_1'@'localhost';

-- Create user_0d_2 with limited access to user_2_db
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';
