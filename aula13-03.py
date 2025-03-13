from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="biblioteca"
)

compor = db.cursor()

@app.route("/")
def index():
    compor.execute("SELECT * FROM livros")
    livros = compor.fetchall()
    return render_template("index.html", livros=livros)

@app.route("/redirecionar")
def adicionar():
    return render_template("adicionar_livros.html")

@app.route("/salvar", methods=["POST"])
def salvar():
    titulo = request.form["titulo"]
    autor = request.form["autor"]
    ano_publicacao = request.form["ano_publicacao"]

    sql = "INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (%s, %s, %s)"
    compor.execute(sql, (titulo, autor, ano_publicacao))
    db.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
