
-- *** The Lost Letter ***
-- The current address (or location!) of their missing package

-- Clerk, my name’s Anneke. I live over at 900 Somerville Avenue. Not long ago, I sent out a special letter. It’s meant for my friend Varsha. She’s starting a new chapter of her life at 2 Finnegan Street, uptown.



SELECT address, type FROM addresses WHERE id = (
SELECT  to_address_id FROM packages
WHERE from_address_id =
(SELECT id FROM addresses WHERE address LIKE "900 Somerville Avenue"));



-- *** The Devious Delivery ***
-- The type of address or location (e.g. residential, business, etc.)
-- What were the contents of the Devious Delivery?
--  there’s no “From” address.

SELECT type, contents FROM scans JOIN packages ON packages.id = scans.package_id
JOIN addresses ON scans.address_id = addresses.id
WHERE from_address_id IS NULL
ORDER BY timestamp DESC LIMIT 1;


-- *** The Forgotten Gift ***
-- The contents of the package
-- Oh, excuse me, Clerk. I had sent a mystery gift, you see, to my wonderful granddaughter, off at 728 Maple Place. That was about two weeks ago. Now the delivery date has passed by seven whole days and I hear she still waits, her hands empty and heart filled with anticipation. I’m a bit worried wondering where my package has gone. I cannot for the life of me remember what’s inside, but I do know it’s filled to the brim with my love for her. Can we possibly track it down so it can fill her day with joy? I did send it from my home at 109 Tileston Street.

SELECT name AS "Driver Name", contents FROM drivers JOIN scans ON scans.driver_id = drivers.id
JOIN packages ON packages.id = scans.package_id
JOIN addresses ON addresses.id = scans.address_id
WHERE from_address_id = (SELECT id FROM addresses WHERE address = "109 Tileston Street") AND
to_address_id = (SELECT id FROM addresses WHERE address = "728 Maple Place")
ORDER BY timestamp DESC LIMIT 1;



