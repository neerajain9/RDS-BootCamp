CREATE TABLE firepower (
	country VARCHAR,
	ISO3 VARCHAR,
	rank INT,
	TotalPopulation INT,
	ManpowerAvailable INT,
	TotalMilitaryPersonnel INT,
	ActivePersonnel INT,
	ReservePersonnel INT,
	TotalAircraftStrength INT,
	FighterAircraft INT,
	AttackAircraft INT,
	TotalHelicopterStrength INT,
	AttackHelicopters INT
);

ALTER TABLE firepower ADD COLUMN id SERIAL PRIMARY KEY; 

-- ALTER TABLE firepower 
-- ADD COLUMN "id" INT;
-- SELECT * FROM firepower

-- ALTER TABLE firepower 
-- ALTER COLUMN "id" SET NOT NULL;


-- select * from firepower