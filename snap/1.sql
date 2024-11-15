-- CREATE INDEX "search_users_by_last_login"
-- ON "users"("last_login_date");

SELECT username FROM users WHERE "last_login_date" >= "2024-01-01";