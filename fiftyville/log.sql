-- database: fiftyville.db
-- Keep a log of any SQL queries you execute as you solve the mystery.

-- find out more detail about the crime
SELECT id, description FROM crime_scene_reports
where year = 2023 AND month = 7 AND day = 28;

-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. crime id = 295

-- check out the witnesses and bakery log

SELECT id, name, transcript FROM interviews
where year = 2023 AND month = 7 AND day = 28
AND transcript LIKE "%bakery%";

-- Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.


-- I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

-- As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- 1. find anyone left parking lot between 10:15- 10:25am

SELECT people.name FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25
AND activity = "exit";


-- 2. find someone withdraw money on that day before 10:15am

SELECT people.name FROM atm_transactions
JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number
JOIN people ON people.id = bank_accounts.person_id
WHERE atm_location = "Leggett Street"
AND transaction_type = "withdraw"
AND year = 2023 AND month = 7 AND day = 28;



-- 3. find someone that made a phone call after 10:15am that call lasted less than 1min;

SELECT people.name FROM phone_calls
JOIN people ON people.phone_number = phone_calls.caller
WHERE year = 2023 AND month = 7 AND day = 28
AND duration < 60;

 -- 4. find someone who receive the call
SELECT people.name FROM phone_calls
JOIN people ON people.phone_number = phone_calls.receiver
WHERE year = 2023 AND month = 7 AND day = 28
AND duration < 60;



--intersect 2 and 3 to find the thief
SELECT people.name AS thief FROM atm_transactions
JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number
JOIN people ON people.id = bank_accounts.person_id
WHERE atm_location = "Leggett Street"
AND transaction_type = "withdraw"
AND year = 2023 AND month = 7 AND day = 28
INTERSECT
SELECT people.name FROM phone_calls
JOIN people ON people.phone_number = phone_calls.caller
WHERE year = 2023 AND month = 7 AND day = 28
AND duration < 60;


--intersect 1 and 4 to find accomplice
SELECT people.name FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25
AND activity = "exit"
INTERSECT
SELECT people.name FROM phone_calls
JOIN people ON people.phone_number = phone_calls.receiver
WHERE year = 2023 AND month = 7 AND day = 28
AND duration < 60;

-- it seems the car belongs to the thief

SELECT people.name AS thief FROM atm_transactions
JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number
JOIN people ON people.id = bank_accounts.person_id
WHERE atm_location = "Leggett Street"
AND transaction_type = "withdraw"
AND year = 2023 AND month = 7 AND day = 28
INTERSECT
SELECT people.name FROM phone_calls
JOIN people ON people.phone_number = phone_calls.caller
WHERE year = 2023 AND month = 7 AND day = 28
AND duration < 60
INTERSECT
SELECT people.name FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25;

-- thief is one of Bruce and Diana!


-- match caller and receiver
SELECT
    p1.name AS caller,
    p2.name AS receiver
FROM phone_calls
JOIN people p1 ON p1.phone_number = phone_calls.caller
JOIN people p2 ON p2.phone_number = phone_calls.receiver
WHERE year = 2023
    AND month = 7
    AND day = 28
    AND duration < 60
    AND p1.name IN ('Bruce', 'Diana');

-- so it's either Bruce Robin or Diana Philip


-- find out any of the 4 booked a flight and order by earliest

SELECT flights.hour, flights.destination_airport_id, people.name FROM flights
JOIN passengers ON passengers.flight_id = flights.id
JOIN people ON people.passport_number = passengers.passport_number
WHERE flights.year = 2023 AND flights.month = 7 AND flights.day = 29
AND people.name in ('Bruce', 'Diana', 'Philip','Robin')
ORDER BY flights.hour, flights.minute LIMIT 1;

-- Bruce ran! (I stg Diana looked so sus)
SELECT airports.full_name, city FROM airports WHERE airports.id = (
    SELECT flights.destination_airport_id FROM flights
JOIN passengers ON passengers.flight_id = flights.id
JOIN people ON people.passport_number = passengers.passport_number
WHERE flights.year = 2023 AND flights.month = 7 AND flights.day = 29
AND people.name in ('Bruce', 'Diana', 'Philip','Robin')
ORDER BY flights.hour, flights.minute LIMIT 1
);

- Bruce ran to NYC!

