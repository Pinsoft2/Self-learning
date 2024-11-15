
-- need a table to store the 3 numbers
CREATE TABLE "code" (
    first_num INT,
    second_num INT,
    third_num INT
);

INSERT INTO code (first_num, second_num, third_num) values (14, 98, 4), (114, 3, 5), (618, 72, 9), (630, 7, 3), (932, 12, 5), (2230, 50, 7), (2346, 44, 10), (3041, 14, 5);


-- substrs are the actual ways of getting the message
CREATE VIEW "message" AS
    SELECT substr(
        "sentence",
        "second_num",
        "third_num") AS "phrase" FROM
        (SELECT sentence, second_num, third_num FROM sentences JOIN code on sentences.id = code.first_num) AS "new_code";

