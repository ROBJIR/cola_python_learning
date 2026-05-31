import sqlite3

# pripojenie / vytvorenie databazy
conn = sqlite3.connect('databaza.db')
cursor = conn.cursor()

# vytvorenie tabulky
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
""")

# vlozenie zaznamu
cursor.execute("INSERT INTO users(name, age) VALUES (?, ?)", ('Adam', 25))
conn.commit()

# vlozenie viacerych zaznamov
users = [('Peter', 30), ('Jana', 22), ('Martin', 28)]
cursor.executemany("INSERT INTO users(name, age) VALUES (?, ?)", users)
conn.commit()

# nacitanie dat
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# zatvorenie spojenia
conn.close()