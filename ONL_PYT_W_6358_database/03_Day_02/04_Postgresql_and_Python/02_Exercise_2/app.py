from flask import Flask, request, render_template
from sql_utils import execute_sql

DB_NAME = "cinemas_db"


app = Flask(__name__)

@app.route("/movies")
def all_movies():
    query = "SELECT id, name FROM movies;"
    data = execute_sql(query, DB_NAME)

    output = "<ul>"
    for row in data:
        output += f"<li><a href='/movie/{row['id']}'><h3>{row['name']}</h3></a></li>"
    
    output += "</ul>"

    return output

@app.route("/movie/<int:id>", methods=["GET", "POST"])
def movie_page(id:int):
    if request.method == "POST":
        query = f"DELETE FROM movies WHERE id={id};"
        execute_sql(query, DB_NAME)
        return "<h1> success delete</h1>"

    query = f"SELECT * FROM movies WHERE id={id};"
    data = execute_sql(query, DB_NAME)

    output = "<ul>"
    for row in data:
        for k,v in row.items():
            output += f"<li><h3>{k} : {v}</h3></li>"
    
    output += "</ul>"

    output += f"""
<form method='post'>
    <input type='submit'>
</form>
    """

    return output


@app.route("/add_movie", methods=["GET", "POST"])
def new_movie():
    if request.method == "GET":
        return render_template("form.html")

    name = request.form["name"]
    description = request.form["desc"]
    rating = request.form["rating"]

    query = f"""
INSERT INTO movies (name, description, rating)
VALUES ('{name}','{description}',{rating});
"""
    execute_sql(query, DB_NAME)
    return "<h1> success</h1>"


@app.route("/update_movie/<int:id>", methods=["GET", "POST"])
def update_movie(id:int):
    if request.method == "GET":
        query = f"SELECT * FROM movies WHERE id={id};"
        data = execute_sql(query, DB_NAME)
        return render_template(
            "form.html", 
            name=data[0]["name"],
            description=data[0]["description"],
            rating=data[0]["rating"]
            )

    name = request.form["name"]
    description = request.form["desc"]
    rating = request.form["rating"]

    query = f"""
UPDATE movies
SET name='{name}', description='{description}', rating={rating}
WHERE id={id};
"""
    execute_sql(query, DB_NAME)
    return "<h1> success</h1>"

app.run()