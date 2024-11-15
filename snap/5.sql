-- 5.sql
-- For any two users, the app needs to quickly show a list of the friends they have in common. Given two usernames, lovelytrust487 and exceptionalinspiration482, find the user IDs of their mutual friends. A mutual friend is a user that both lovelytrust487 and exceptionalinspiration482 count among their friends.

-- Ensure your query uses the index automatically created on primary key columns of the friends table. This index is called sqlite_autoindex_friends_1.

SELECT id FROM users
JOIN friends ON friends.user_id = users.id
WHERE friends.friend_id = (SELECT users.id FROM users WHERE username = 'lovelytrust487')

INTERSECT

SELECT id FROM users
JOIN friends ON friends.user_id = users.id
WHERE friends.friend_id = (SELECT users.id FROM users WHERE username = 'exceptionalinspiration482');