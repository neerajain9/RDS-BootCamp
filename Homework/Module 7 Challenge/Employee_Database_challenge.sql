-- Initial Query to Get all employees titles (duplicate exists)
SELECT e.emp_no, 
	e.first_name,
	e.last_name,
	t.title, 
	t.from_date,
	t.to_date
INTO retirement_titles
FROM titles as t
INNER JOIN employees as e
ON t.emp_no = e.emp_no
-- WHERE t.emp_no = 10004
WHERE (e.birth_date >= '1952-01-01') AND
	(e.birth_date <= '1955-12-31')
ORDER BY t.emp_no;




-- Use Dictinct with Orderby to remove duplicate rows
SELECT DISTINCT ON (emp_no) emp_no, 
	first_name,
	last_name,
	title
INTO unique_titles
FROM retirement_titles
ORDER BY emp_no,
	to_date DESC;




-- Retiring Titles
SELECT count(title), title
INTO retiring_titles
FROM unique_titles
GROUP BY title
ORDER BY COUNT(title) DESC;




-- Mentor Eligibility
SELECT DISTINCT ON (e.emp_no) e.emp_no,
    e.first_name,
    e.last_name,
    e.birth_date,
    de.from_date,
    de.to_date,
    t.title
INTO mentorship_eligibilty
FROM employees as e
    INNER JOIN dept_emp as de
    ON e.emp_no = de.emp_no
    
    INNER JOIN titles as t
    ON e.emp_no = t.emp_no

WHERE de.to_date = '9999-01-01' AND
    e.birth_date >= '1965-01-01' AND
    e.birth_date <= '1965-12-31'

ORDER BY e.emp_no



-- Mentorship Eligible Employees
SELECT COUNT(*) "Mentorship Eligible Employees"
FROM mentorship_eligibilty

-- Total Retiring Employees
SELECT SUM(count) "Total Retiring Employees"
FROM retiring_titles














-- FOR REFERENCE ONLY -- (NOT PART OF THE CHALLENGE)
-- 
-- 
-- ONCE SQL THAT DOES IT ALL
SELECT DISTINCT ON (t.emp_no) t.emp_no, 
	e.first_name,
	e.last_name,
	t.title, 
	t.from_date,
	t.to_date
INTO test
FROM titles as t
INNER JOIN employees as e
ON t.emp_no = e.emp_no
-- WHERE t.emp_no = 10004
WHERE (e.birth_date >= '1952-01-01') AND
	(e.birth_date <= '1955-12-31')
ORDER BY t.emp_no,
 	t.to_date DESC;

-- Retiring Titles
SELECT count(title), title
INTO retiring_titles
FROM test
GROUP BY title
ORDER BY COUNT(title) DESC;