-- Write your PostgreSQL query statement below
SELECT firstname, lastname, a.city, a.state
FROM Person p

LEFT JOIN Address a on p.personId = a.personId