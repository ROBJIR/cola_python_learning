import psycopg2
from psycopg2.extras import RealDictCursor


# pripojenie k databaze
conn = psycopg2.connect(
    host="localhost",
    database="exercises_db",
    user="zdenkocepan",
    password="",
    port=5432
)


with conn.cursor(cursor_factory=RealDictCursor) as curr:
    curr.execute("SELECT * FROM products;")
    data = curr.fetchall()


for row in data:
    for k,v in row.items():
        print(f"{k}:  {v}")
    
    print()

# zatvorenie spojenia
#cursor.close()
conn.close()