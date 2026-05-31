import psycopg2

# pripojenie k databaze
conn = psycopg2.connect(
    host="localhost",
    database="databaza",
    user="postgres",
    password="heslo",
    port=5432
)
cursor = conn.cursor()

# vytvorenie tabulky
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        age INTEGER
    )
""")
conn.commit()

# vlozenie zaznamu
cursor.execute("INSERT INTO users(name, age) VALUES (%s, %s)", ('Adam', 25))
conn.commit()

# vlozenie viacerych zaznamov
users = [('Peter', 30), ('Jana', 22), ('Martin', 28)]
cursor.executemany("INSERT INTO users(name, age) VALUES (%s, %s)", users)
conn.commit()

# nacitanie dat
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# zatvorenie spojenia
cursor.close()
conn.close()