CREATE TABLE "users" (
    "id" INTEGER PRIMARY KEY,
    "follower_id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL UNIQUE,
    "password" TEXT NOT NULL,
    "school_start_date" NUMERIC NOT NULL,
    "school_end_date" NUMERIC NOT NULL,
    "title" TEXT,
    "work_start_date" NUMERIC NOT NULL,
    "work_end_date" NUMERIC NOT NULL,
    FOREIGN KEY ("follower_id") REFERENCES "users"("id")
);

CREATE TABLE "schools" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL UNIQUE,
    "user_id" INTEGER,
    "type" TEXT,
    "location" TEXT,
    "year_founded" INTEGER CHECK ("year_founded" > 0),
    "school_start_date" NUMERIC NOT NULL,
    "school_end_date" NUMERIC NOT NULL,
    FOREIGN KEY ("user_id") REFERENCES "users"("id")
);

CREATE TABLE "companies" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL UNIQUE,
    "industry" TEXT,
    "location" TEXT,
    "user_id" INTEGER,
    "title" TEXT,
    "work_start_date" NUMERIC,
    "work_end_date" NUMERIC,
    FOREIGN KEY ("user_id") REFERENCES "users"("id")
);