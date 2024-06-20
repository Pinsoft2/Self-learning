-- In 7.sql, write a SQL query to count the number of players who bat (or batted) right-handed and throw (or threw) left-handed, or vice versa.

-- SELECT COUNT(*) FROM players WHERE bats != throws
-- AND bats IS NOT NULL
-- AND throws IS NOT NULL;

SELECT COUNT(*) FROM players WHERE (bats = "R" AND throws ="L" ) OR (bats = "L" AND throws ="R" );