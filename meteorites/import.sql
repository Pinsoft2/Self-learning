.mode csv
.import meteorites.csv meteorites

UPDATE "meteorites" SET "mass" = NULL WHERE "mass" = "";
UPDATE "meteorites" SET "year" = NULL WHERE "year" = "";
UPDATE "meteorites" SET "lat" = NULL WHERE "lat" = "";
UPDATE "meteorites" SET "long" = NULL WHERE "long" = "";

UPDATE "meteorites" SET "mass" = ROUND(CAST("mass" AS REAL), 2) WHERE "mass" IS NOT NULL;
UPDATE "meteorites" SET "lat" = ROUND(CAST("lat" AS REAL), 2) WHERE "lat" IS NOT NULL;
UPDATE "meteorites" SET "long" = ROUND(CAST("long" AS REAL), 2) WHERE "long" IS NOT NULL;

DELETE FROM "meteorites" WHERE nametype ="Relict";

SELECT * FROM meteorites ORDER BY year, name;

CREATE TABLE "new_meteorites" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT,
    "class" TEXT,
    "mass" TEXT,
    "discovery" TEXT,
    "year" TEXT,
    "lat" TEXT,
    "long" TEXT
);

INSERT INTO "new_meteorites" (name, class, mass, discovery, year, lat, long)
SELECT name, class, mass, discovery, year, lat, long
FROM "meteorites"
-- WHERE "year" IS NOT NULL AND "name" IS NOT NULL
ORDER BY year, name;

DROP TABLE "meteorites";
ALTER TABLE "new_meteorites" RENAME TO "meteorites";