-- create and give permissions to the created user
CREATE USER IF NOT EXISTS'user_0d_1'@'localhost' identified by 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';