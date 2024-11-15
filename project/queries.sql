-- 1. Get the latest stove status for each user
-- This query joins Users, Cameras, and Scannings tables to retrieve the most recent stove status for each user
SELECT "Users"."FirstName", "Users"."LastName", "Scannings"."StoveStatus", "Scannings"."ScanningTime"
FROM "Users"
JOIN "Cameras" ON "Users"."CameraId" = "Cameras"."id"
JOIN "Scannings" ON "Scannings"."CameraId" = "Cameras"."id"
WHERE "Scannings"."ScanningTime" = (
    SELECT MAX("ScanningTime")
    FROM "Scannings"
    WHERE "Scannings"."CameraId" = "Cameras"."id"
)
ORDER BY "Scannings"."ScanningTime" DESC;

-- 2. Count the number of disconnected cameras
-- This query checks the Cameras table to count how many cameras are currently disconnected
SELECT COUNT(*) as disconnected_cameras
FROM "Cameras"
WHERE "Cameras"."InternetStatus" = 'disconnected';

-- 3. Get users who haven't had a scanning in the last 24 hours
-- This query identifies users who might need attention due to lack of recent scans
SELECT "Users"."FirstName", "Users"."LastName", "Users"."Email", MAX("Scannings"."ScanningTime") as last_scan
FROM "Users"
JOIN "Cameras" ON "Users"."CameraId" = "Cameras"."id"
JOIN "Scannings" ON "Cameras"."id" = "Scannings"."CameraId"
GROUP BY "Users"."id", "Users"."FirstName", "Users"."LastName", "Users"."Email"
HAVING MAX("Scannings"."ScanningTime") < NOW() - INTERVAL '24 hours' OR MAX("Scannings"."ScanningTime") IS NULL
ORDER BY last_scan ASC NULLS FIRST;

-- 4. Get the average time between purchase and installation for each user
-- This query calculates how long it takes on average for users to install their device after purchasing
SELECT AVG("Users"."InstallationDate" - "Users"."PurchaseDate") as avg_installation_time
FROM "Users";

-- 5. Find users with stove status greater than 5 in their last scanning
-- This query helps identify potentially dangerous situations where the stove might be left on high
SELECT "Users"."FirstName", "Users"."LastName", "Users"."Email", "Scannings"."StoveStatus", "Scannings"."ScanningTime"
FROM "Users"
JOIN "Cameras" ON "Users"."CameraId" = "Cameras"."id"
JOIN "Scannings" ON "Cameras"."id" = "Scannings"."CameraId"
WHERE "Scannings"."ScanningTime" = (
    SELECT MAX("ScanningTime")
    FROM "Scannings"
    WHERE "Scannings"."CameraId" = "Cameras"."id"
)
AND "Scannings"."StoveStatus" > '5'
ORDER BY "Scannings"."ScanningTime" DESC;

-- 6. Get the total number of scannings per user in the last 7 days
-- This query provides insights into system usage patterns
SELECT "Users"."FirstName", "Users"."LastName", COUNT("Scannings"."id") as scan_count
FROM "Users"
JOIN "Cameras" ON "Users"."CameraId" = "Cameras"."id"
JOIN "Scannings" ON "Cameras"."id" = "Scannings"."CameraId"
WHERE "Scannings"."ScanningTime" >= NOW() - INTERVAL '7 days'
GROUP BY "Users"."id", "Users"."FirstName", "Users"."LastName"
ORDER BY scan_count DESC;


