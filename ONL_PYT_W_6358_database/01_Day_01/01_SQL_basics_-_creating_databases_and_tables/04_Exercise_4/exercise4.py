sql = """
    CREATE TABLE IF NOT EXISTS cinemas (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        address VARCHAR(255)
        );
"""

sql2 = """
    CREATE TABLE IF NOT EXISTS movies (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        description TEXT,
        rating SMALLINT
        );
"""

sql3 = """
    CREATE TABLE IF NOT EXISTS tickets (
        id SERIAL PRIMARY KEY,
        quantity SMALLINT,
        price DECIMAL(6,2)
        );
"""


sql4 = """
    CREATE TABLE IF NOT EXISTS payments (
        id SERIAL PRIMARY KEY,
        type VARCHAR(255),
        date TIMESTAMP
        );
"""