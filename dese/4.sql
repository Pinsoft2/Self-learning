-- Some cities have more public schools than others. In 4.sql, write a SQL query to find the 10 cities with the most public schools. Your query should return the names of the cities and the number of public schools within them, ordered from greatest number of public schools to least. If two cities have the same number of public schools, order them alphabetically.

SELECT schools.city, COUNT(schools.name) AS "# of Public Schools" FROM districts JOIN schools ON schools.district_id = districts.id WHERE schools.type = "Public School"
GROUP BY schools.city
ORDER BY "# of Public Schools" DESC, districts.city LIMIT 10;
