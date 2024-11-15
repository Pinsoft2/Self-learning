-- try to find info around Natick

SELECT dropped, graduated, per_pupil_expenditure, schools.name FROM
graduation_rates JOIN schools ON graduation_rates.school_id = schools.id
JOIN districts on districts.id = schools.district_id
JOIN expenditures ON districts.id = expenditures.district_id
WHERE schools.name LIKE "%Natick%" OR "%Waltham%";