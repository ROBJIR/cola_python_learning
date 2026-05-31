add_movies = """
INSERT INTO movies(name, description, rating) VALUES
('Harry Potter', 'fantasy carodejnicky film', 9),
('Titanic', 'romanticka dramma o potopeni lode', 8),
('The Dark Knight', 'akčný film o Batmanovi', 10),
('Forrest Gump', 'pribeh o zivote jednoducheho muza', 9),
('Inception', 'sci-fi thriller o snoch a realite', 8),
('The Godfather', 'klasicky gangstersky film', 10),
('Interstellar', 'vedecko-fantasticke cestovanie vesmírom', 9),
('Joker', 'psychologicky thriller o vzniku zlocinca', 7),
('Avengers Endgame', 'superhrdinský film o zachrane vesmiru', 8),
('Parasite', 'koreajsky thriller o socialnych rozdieloch', 7);
"""
add_tickets = """
INSERT INTO tickets(quantity, price) VALUES
(3, 845.9),
(1, 299.0),
(5, 1250.5),
(2, 580.0),
(4, 960.0),
(1, 189.9),
(6, 1540.0),
(2, 420.5),
(3, 750.0),
(8, 2100.0);
"""

get_movies = """
SELECT * FROM movies WHERE name LIKE 'W%';
"""
get_tickets_1 = """
SELECT * FROM tickets WHERE price BETWEEN 500 AND 1000;
"""
get_tickets_2 = """
SELECT * FROM tickets WHERE quantity > 3;
"""
