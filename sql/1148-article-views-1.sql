# Write your MySQL query statement below
SELECT DISTINCT author_id AS id
FROM Views
Where viewer_id = author_id
ORDER BY id ASC;