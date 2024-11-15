-- Hits are great, but so are RBIs! In 12.sql, write a SQL query to find the players among the 10 least expensive players per hit and among the 10 least expensive players per RBI in 2001.

-- Your query should return a table with two columns, one for the players’ first names and one of their last names.
-- You can calculate a player’s salary per RBI by dividing their 2001 salary by their number of RBIs in 2001.
-- You may assume, for simplicity, that a player will only have one salary and one performance in 2001.
-- Order your results by player ID, least to greatest (or alphabetically by last name, as both are the same in this case!).


-- SELECT first_name, last_name
-- FROM salaries JOIN players ON players.id = salaries.player_id
-- JOIN performances ON performances.player_id = players.id

-- WHERE players.id = (
-- SELECT players.id
-- FROM salaries JOIN players ON players.id = salaries.player_id
-- JOIN performances ON performances.player_id = players.id
-- WHERE salaries.year = 2001 AND RBI > 0 AND performances.year = salaries.year
-- ORDER BY (salary/RBI))
-- AND salaries.year = 2001 AND H > 0

-- ORDER BY (salary/H), players.id
-- LIMIT 10;



WITH cheap_per_hit AS (
    SELECT players.id
    FROM salaries
    JOIN players ON players.id = salaries.player_id
    JOIN performances ON performances.player_id = players.id
    WHERE salaries.year = 2001 AND performances.year = 2001 AND H > 0
    ORDER BY (salary/H)
    LIMIT 10
),
cheap_per_rbi AS (
    SELECT players.id
    FROM salaries
    JOIN players ON players.id = salaries.player_id
    JOIN performances ON performances.player_id = players.id
    WHERE salaries.year = 2001 AND performances.year = 2001 AND RBI > 0
    ORDER BY (salary/RBI)
    LIMIT 10
)
SELECT DISTINCT players.first_name, players.last_name
FROM players
JOIN cheap_per_hit ON players.id = cheap_per_hit.id
JOIN cheap_per_rbi ON players.id = cheap_per_rbi.id
ORDER BY players.id;