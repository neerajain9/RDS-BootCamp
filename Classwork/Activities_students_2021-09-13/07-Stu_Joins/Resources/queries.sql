SELECT p.id,
	p.player,
	p.height,
	p.weight,
	p.college,
	p.born,
	ss.position,
	ss.tm
-- INTO test
FROM players as p
INNER JOIN seasons_stats as ss
ON p.id = ss.player_id
LIMIT 6;



-- Second Output
SELECT p.id,
	p.college,
	ss.year,
	ss.position,
	ss.two_point_percentage,
	ss.fg_percentage,
	ss.ft_percentage,
	ss.ts_percentage
-- INTO test
FROM seasons_stats as ss
INNER JOIN players as p
ON p.id = ss.player_id
LIMIT 6;