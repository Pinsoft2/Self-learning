CREATE TABLE "passengers"(
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "age" INTEGER CHECK("age" > 0),
    PRIMARY KEY ("id")
);

CREATE TABLE "check_ins"(
    "id" INTEGER,
    "check_in_date" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "flight_id" INTEGER,
    "passenger_id" INTEGER,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("flight_id") REFERENCES "flights"("id"),
    FOREIGN KEY ("passenger_id") REFERENCES "passengers"("id")
);

CREATE TABLE "airlines"(
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "concourse" TEXT CHECK ("concourse" IN ('A','B','C','D','E','F','T')),
    PRIMARY KEY ("id")
    -- FOREIGN KEY ("flight_id") REFERENCES "Flights"("id"),
);


CREATE TABLE "flights"(
    "id" INTEGER,
    "airline_id" INTEGER,
    "airline_name" TEXT NOT NULL,
    "dept_airport_code" TEXT,
    "arrival_airport_code" TEXT,
    "expected_departure" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "expected_arrival" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("airline_id") REFERENCES "airlines"("id"),
    FOREIGN KEY ("airline_name") REFERENCES "airlines"("name")
    -- FOREIGN KEY ("passenger_id") REFERENCES "Passengers"("id")
);
