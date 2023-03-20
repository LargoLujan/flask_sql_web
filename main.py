from flask import Flask, render_template, request
import db
from models import Tasks

app = Flask(__name__)  # En app se encuentra nuestro servidor web de Flask


@app.route("/")
def home_web():
    return render_template("index.html")


@app.route("/create-task", methods=["POST"])
def create():
    task = Tasks(content=request.form["contenido_tarea"],
                 done=False)  # request.form trae la info del html del apartado input como una variable
    db.session.add(task)
    db.session.commit()
    return "Tarea guardada"


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, port=1111) Podemos elegir el puerto desde el que trabajar. Cuidado porque
    # hay puertos en uso por el pc y hay que comprobar que este libre.
