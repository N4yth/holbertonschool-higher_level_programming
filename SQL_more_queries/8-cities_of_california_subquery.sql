-- create and give permissions to the created user
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
