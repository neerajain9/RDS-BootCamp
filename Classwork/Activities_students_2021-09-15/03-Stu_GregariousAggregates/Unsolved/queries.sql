SELECT AVG(rental_rate) "Average Rental Rate" 
FROM FILM;

SELECT rating, 
	AVG(rental_rate) "Average Rental Rate" 
FROM FILM
GROUP BY rating;

SELECT SUM(replacement_cost) "Replacement Cost"
FROM film;

SELECT rating, 
	SUM(replacement_cost) "Replacement Cost"
FROM film
GROUP BY rating;

SELECT MAX(length) "Longest Movie", 
	MIN(length) "Shortest Movie"
FROM film;