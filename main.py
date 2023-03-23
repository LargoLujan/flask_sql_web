import datetime

from flask import Flask, render_template, request, redirect, url_for
import db  # Nuestra base de datos para que no se pierdan las tareas
from models import Tasks  # Nuestro modelo de tarea para que todo esté ordenado

app = Flask(__name__)  # ¡Empezamos el show! Creamos la instancia de nuestra aplicación web de Flask


@app.route("/")  # Ruta para la página principal de nuestra app
def home_web():
    every_tasks = db.session.query(Tasks).all()  # Pedimos todas las tareas de la base de datos
    for i in every_tasks:
        print(i)  # Siempre es bueno tener un log en algún lado para ver que todo anda bien
    return render_template("index.html", task_list=every_tasks)  # Renderizamos la plantilla HTML de la página principal


@app.route("/create_task", methods=["POST"])  # Ruta para crear una tarea nueva
def create():
    due_date = datetime.strptime(request.form["due_date"], "%d-%m-%Y").date()  # Convertimos la fecha a formato datetime
    task = Tasks(content=request.form["content_task"], done=False, category=request.form["category"])  # Creamos una tarea nueva
    db.session.add(task)  # La agregamos a la base de datos
    db.session.commit()  # ¡Guardamos los cambios!
    return redirect(url_for("home_web"))  # Redirigimos a la página principal


@app.route("/delete-task/<id>")  # Ruta para borrar una tarea
def delete(id):
    task = db.session.query(Tasks).filter_by(id_task=id).delete()  # Buscamos la tarea a borrar
    db.session.commit()  # ¡Guardamos los cambios!
    return redirect(url_for("home_web"))  # Redirigimos a la página principal


@app.route("/done-task/<id>")  # Ruta para marcar una tarea como hecha
def done(id):
    task = db.session.query(Tasks).filter_by(id_task=int(id)).first()  # Buscamos la tarea a marcar como hecha
    task.done = not(task.done)  # ¡Cambiamos su estado!
    db.session.commit()  # ¡Guardamos los cambios!
    return redirect(url_for("home_web"))  # Redirigimos a la página principal


@app.route("/tasks_by_category/<category>")  # Ruta para buscar tareas por categoría
def tasks_by_category(category):
    category_tasks = db.session.query(Tasks).filter_by(category=category).all()  # Buscamos las tareas de esa categoría
    return render_template("index.html", task_list=category_tasks)  # Renderizamos la plantilla HTML con la lista de tareas


@app.route("/edit-task/<id>", methods=["GET", "POST"])  # Ruta para editar una tarea
def edit(id):
    task = db.session.query(Tasks).filter_by(id_task=id).first()  # Buscamos la tarea a editar
    if request.method == "POST":  # Si nos enviaron un formulario con los datos nuevos
        task.content = request.form["content_task"]  # Actualizamos la descripción de la tarea
        task.category = request.form["category"]  # Actualizamos la categoría de la tarea
        task.due_date = datetime.strptime(request.form["due_date"], "%Y-%m-%d").date()
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home_web"))
    else:
        return render_template("edit.html", task=task) # Si no, mostramos el formulario de edición


@app.route("/update_task/<int:id>", methods=["POST"])
def update(id):
    task = db.session.query(Tasks).filter_by(id_task=id).first() # Busca la tarea en la base de datos a partir del ID proporcionando
    task.content = request.form["content_task"] # Actualiza el contenido, la categoría y la fecha límite de la tarea con la información del formulario enviado
    task.category = request.form["category"]
    task.due_date = datetime.datetime.strptime(request.form["due_date"], "%Y-%m-%d").date()
    db.session.commit() # Guarda los cambios en la base de datos
    return redirect(url_for("home_web")) # Redirige al usuario a la página principal


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine) # Crea las tablas de la base de datos (si no existen)
    app.run(debug=True) # Inicia la aplicación Flask en modo debug

    # También podemos elegir el puerto desde el que trabajar, pero hay que asegurarse de que esté libre
    # app.run(debug=True, port=1111)
