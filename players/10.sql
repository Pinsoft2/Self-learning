-- In 10.sql, write SQL query to answer a question of your choice. This query should:
-- Make use of AS to rename a column
-- Involve at least condition, using WHERE
-- Sort by at least one column using ORDER BY


SELECT (final_game - debut) AS "Active Years for MA players", debut, final_game, first_name, last_name FROM players WHERE birth_state = "MA" ORDER BY "Active Years for MA players" DESC limit 5;