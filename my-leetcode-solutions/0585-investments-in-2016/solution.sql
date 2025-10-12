SELECT ROUND(SUM(T1.tiv_2016), 2) AS tiv_2016
FROM Insurance AS T1
WHERE
    T1.tiv_2015 IN (
        SELECT tiv_2015
        FROM Insurance
        GROUP BY tiv_2015
        HAVING COUNT(pid) > 1
    )
    AND
    (T1.lat, T1.lon) IN (
        SELECT lat, lon
        FROM Insurance
        GROUP BY lat, lon
        HAVING COUNT(pid) = 1
    );
