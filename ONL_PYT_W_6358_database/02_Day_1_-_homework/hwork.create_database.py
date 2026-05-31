sql = """
      CREATE DATABASE library_db;
"""

sql1 = """
    CREATE TABLE IF NOT EXISTS author (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255)
        );
"""

sql2 = """
    CREATE TABLE IF NOT EXISTS book (
        id SERIAL PRIMARY KEY,
        isbn VARCHAR(13),
        name VARCHAR(255),
        description TEXT,
        is_loaned BOOLEAN
        );
"""
alter2 = """
    ALTER TABLE book 
        ADD COLUMN author_id INTEGER
    ;
"""

sql3 = """
    CREATE TABLE IF NOT EXISTS client (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255)
        );
"""

sql3 = """
    CREATE TABLE IF NOT EXISTS category (
        id SERIAL PRIMARY KEY,
        name VARCHAR(80)
        );
"""

ins1 = """
INSERT INTO author (name) VALUES 
    ('George Orwel'),
    ('Patrik Hartl'),
    ('David Mitchell'),
    ('Luis Bunuel'),
    ('Henry Miller');    
    
"""

ins2 = """
INSERT INTO "library".book (isbn, "name", description, is_loaned, author_id) VALUES
    ('1123115766', 'Valecny denik', NULL, false, 1),
    ('223345677', 'Do posledniho dechu', NULL, false, 5),
    ('4455566787888', 'Tiche dny v Clichy', NULL, false, 4),
    ('987654321', 'Atlas mraku', NULL, false, 3),
    ('9780451524935', '1984', NULL, false, 1),
    ('9780451526342', 'Farma zvirat', NULL, false, 1),
    ('9780156421171', 'Na dne v Parizi a Londyne', NULL, false, 1),
    ('9780156551502', 'Hold Aspidistre', NULL, false, 1),
    ('9780156901505', 'Cesta k pristavisti Wigan', NULL, false, 1),
    ('9788026504665', 'Manzelstvi', NULL, false, 2),
    ('9788026504665', 'Maly prazsky erotikon', NULL, false, 2),
    ('9788026504665', 'Prvok, Sampon, Tecka a Karel', NULL, false, 2),
    ('9788026718079', 'Gazely', NULL, false, 2);
"""

ins3 = """
INSERT INTO client (first_name,last_name) VALUES
    ('Robert','Jiranek'),
    ('Zdenko','Cepman'),
    ('Andy','Hodna'),
    ('Martin','Coranda');
"""