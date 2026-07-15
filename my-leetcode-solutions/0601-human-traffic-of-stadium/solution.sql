# Write your MySQL query statement below
WITH CTE AS (
    SELECT *, id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
)

SELECT ID, VISIT_DATE, PEOPLE
FROM CTE
WHERE grp IN (
    SELECT grp
    FROM cte
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
ORDER BY VISIT_DATE;
