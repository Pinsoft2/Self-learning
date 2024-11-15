-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it

-- To recreate the database for testing and demo purposes
-- DROP DATABASE IF EXISTS cs50;
-- CREATE DATABASE cs50;

-- Use the database
-- \c cs50;

-- Define ENUM types for statuses
CREATE TYPE internet_status AS ENUM ('disconnected', 'connected');
CREATE TYPE stove_status AS ENUM ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
CREATE TYPE switch_status AS ENUM ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');

-- Create Users table
CREATE TABLE "Users" (
    "id" SERIAL PRIMARY KEY,
    "FirstName" VARCHAR(50) NOT NULL,
    "LastName" VARCHAR(50) NOT NULL,
    "Email" VARCHAR(255) NOT NULL UNIQUE,
    "HomeAddress" TEXT,
    "IPAddress" INET NOT NULL,
    "WifiPassword" VARCHAR(64) NOT NULL,
    "PurchaseDate" TIMESTAMP NOT NULL DEFAULT NOW(),
    "InstallationDate" TIMESTAMP NOT NULL DEFAULT NOW(),
    "CameraId" INT,
    "SwitchId" INT,
    "is_deleted" BOOLEAN DEFAULT FALSE
);

-- Create Cameras table
CREATE TABLE "Cameras" (
    "id" SERIAL PRIMARY KEY,
    "ManufacturedDate" TIMESTAMP NOT NULL,
    "InternetStatus" internet_status,
    "UserId" INT,
    "is_deleted" BOOLEAN DEFAULT FALSE,
    FOREIGN KEY ("UserId") REFERENCES "Users" ("id")
);

-- Create Switches table
CREATE TABLE "Switches" (
    "id" SERIAL PRIMARY KEY,
    "SwitchStatus" switch_status,
    "UserId" INT,
    "is_deleted" BOOLEAN DEFAULT FALSE,
    FOREIGN KEY ("UserId") REFERENCES "Users" ("id")
);

-- Create Scannings table
CREATE TABLE "Scannings" (
    "id" SERIAL PRIMARY KEY,
    "ScanningTime" TIMESTAMP NOT NULL DEFAULT NOW(),
    "StoveStatus" stove_status,
    "Image" BYTEA,
    "CameraId" INT,
    FOREIGN KEY ("CameraId") REFERENCES "Cameras" ("id")
);

-- Create important indexes on IDs
CREATE INDEX User_idx ON "Users"("id");
CREATE INDEX Camera_idx ON "Cameras"("id");
CREATE INDEX Switch_idx ON "Switches"("id");
CREATE INDEX Scanning_idx ON "Scannings"("id");
CREATE INDEX Scanning_image ON "Scannings"("Image", "ScanningTime");

-- Create functions and triggers for any updates between users, switches, and cameras
CREATE OR REPLACE FUNCTION update_user_camera()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' OR TG_OP = 'UPDATE' THEN
        UPDATE "Users"
        SET "CameraId" = NEW."id"
        WHERE "id" = NEW."UserId";
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_user_switch()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' OR TG_OP = 'UPDATE' THEN
        UPDATE "Users"
        SET "SwitchId" = NEW."id"
        WHERE "id" = NEW."UserId";
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER camera_update
AFTER INSERT OR UPDATE ON "Cameras"
FOR EACH ROW
EXECUTE FUNCTION update_user_camera();

CREATE TRIGGER switch_update
AFTER INSERT OR UPDATE ON "Switches"n
FOR EACH ROW
EXECUTE FUNCTION update_user_switch();


-- Create important views on statuses
CREATE VIEW stove_status_2024 AS
    SELECT "StoveStatus", "Image"
    FROM "Scannings"
    JOIN "Cameras" ON "Scannings"."CameraId" = "Cameras"."id"
    WHERE "Cameras"."is_deleted" = FALSE
    AND EXTRACT(YEAR FROM "ScanningTime") = 2024
    ORDER BY "ScanningTime" DESC
    LIMIT 5;

-- Add sample users
INSERT INTO "Users" ("FirstName", "LastName", "Email", "IPAddress", "WifiPassword", "PurchaseDate", "InstallationDate") VALUES
('Alice', 'Johnson', 'alice@example.com', '192.168.1.2', 'securepass1', NOW(), NOW()),
('Bob', 'Smith', 'bob@example.com', '192.168.1.3', 'strongpwd2', NOW() - INTERVAL '2 days', NOW() - INTERVAL '1 day'),
('Carol', 'Davis', 'carol@example.com', '192.168.1.4', 'safeword3', NOW() - INTERVAL '5 days', NOW() - INTERVAL '4 days'),
('Dave', 'Wilson', 'dave@example.com', '192.168.1.5', 'password4', NOW() - INTERVAL '10 days', NOW() - INTERVAL '5 days'),
('Eve', 'Taylor', 'eve@example.com', '192.168.1.6', 'password5', NOW() - INTERVAL '3 days', NOW() - INTERVAL '1 day'),
('Frank', 'Miller', 'frank@example.com', '192.168.1.7', 'password6', NOW() - INTERVAL '1 week', NOW() - INTERVAL '2 days');


-- Add sample cameras
INSERT INTO "Cameras" ("ManufacturedDate", "InternetStatus", "UserId") VALUES
(NOW() - INTERVAL '30 days', 'connected', 1),
(NOW() - INTERVAL '45 days', 'disconnected', 2),
(NOW() - INTERVAL '60 days', 'connected', 3),
(NOW() - INTERVAL '5 days', 'connected', 4);

-- Add sample switches
INSERT INTO "Switches" ("SwitchStatus", "UserId") VALUES
('1', 1),
('4', 2),
('9', 3);

-- Add sample scannings
INSERT INTO "Scannings" ("ScanningTime", "StoveStatus", "Image", "CameraId") VALUES
(NOW() - INTERVAL '1 hour', '1', E'\\x0123456789ABCDEF', 1),
(NOW() - INTERVAL '2 hours', '0', E'\\xFEDCBA9876543210', 2),
(NOW() - INTERVAL '30 minutes', '7', E'\\x1A2B3C4D5E6F7890', 3),
(NOW() - INTERVAL '10 minutes', '9', E'\\x9876543210ABCDEF', 4);
