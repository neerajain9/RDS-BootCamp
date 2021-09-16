-- 1. Retreive the latest rental for each customer's first and last name and emial address. 
SELECT DISTINCT ON (r.customer_id)
    c.first_name, 
    c.last_name, 
    c.email,
    r.rental_date
FROM rental as r
INNER JOIN customer as c
ON r.customer_id = c.customer_id
ORDER BY r.customer_id, r.rental_date DESC

-- 2. Retrieve the latest rental date for each title. 


-- Bonus:
-- Query 2 only returned 958 movies, which means 42 movies are not being rented. 
-- We know that there are 1,000 movies in the `film` table. 
-- Retrieve the film titles of the 42 movies that are not in the `inventory` table. 