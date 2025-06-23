-- change the score of Bob to 10

SELECT score , count(*) AS number
FROM second_table
GROUP BY score
HAVING COUNT(*)
ORDER BY score DESC