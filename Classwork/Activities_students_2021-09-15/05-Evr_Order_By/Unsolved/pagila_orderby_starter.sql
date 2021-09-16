-- Select count of actors first names in descending order
SELECT first_name, count(first_name) from actor
group by first_name

-- Select the average duration of movies by rating
SELECT rating, 
    AVG(length) "Average Duration"
FROM FILM
GROUP BY rating

-- Select top ten replace costs for the length of the movie
SELECT length, 
    round(AVG(replacement_cost),2) "Replacement Cost"
FROM FILM
GROUP BY length
ORDER BY "Replacement Cost" DESC
LIMIT 10

-- Select the count of countries
SELECT count(country)
FROM country
