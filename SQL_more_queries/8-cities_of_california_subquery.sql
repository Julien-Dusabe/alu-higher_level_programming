-- Insert California into states (only if it doesn't already exist)
INSERT IGNORE INTO states (id, name) VALUES (1, 'California');

-- Insert 3 California cities (if needed)
INSERT INTO cities (state_id, name)
VALUES (1, 'Los Angeles'), 
	(1, 'San Francisco'), 
	(1, 'San Jose');
