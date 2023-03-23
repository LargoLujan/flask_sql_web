import datetime

from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tasks

app = Flask(__name__)  # En app se encuentra nuestro servidor web de Flask


@app.route("/")
def home_web():
    every_tasks = db.session.query(Tasks).all()
    for i in every_tasks:
        print(i)
    return render_template("index.html", task_list=every_tasks)


@app.route("/create_task", methods=["POST"])
def create():
    due_date = datetime.strptime(request.form["due_date"], "%d-%m-%Y").date()
    task = Tasks(content=request.form["content_task"], done=False, category=request.form["category"])
    db.session.add(task)
    db.session.commit()
    return redirect(url_for("home_web"))


@app.route("/delete-task/<id>")
def delete(id):
    task = db.session.query(Tasks).filter_by(id_task=id).delete()
    db.session.commit()
    return redirect(url_for("home_web"))


@app.route("/done-task/<id>")
def done(id):
    task = db.session.query(Tasks).filter_by(id_task=int(id)).first()
    task.done = not(task.done)
    db.session.commit()
    return redirect(url_for("home_web"))

@app.route("/tasks_by_category/<category>")
def tasks_by_category(category):
    category_tasks = db.session.query(Tasks).filter_by(category=category).all()
    return render_template("index.html", task_list=category_tasks)

@app.route("/edit-task/<id>", methods=["GET", "POST"])
def edit(id):
    task = db.session.query(Tasks).filter_by(id_task=id).first()
    if request.method == "POST":
        task.content = request.form["content_task"]
        task.category = request.form["category"]
        task.due_date = datetime.strptime(request.form["due_date"], "%Y-%m-%d").date()
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home_web"))
    else:
        return render_template("edit.html", task=task)

@app.route("/update_task/<int:id>", methods=["POST"])
def update(id):
    task = db.session.query(Tasks).filter_by(id_task=id).first()
    task.content = request.form["content_task"]
    task.category = request.form["category"]
    task.due_date = datetime.datetime.strptime(request.form["due_date"], "%Y-%m-%d").date()
    db.session.commit()
    return redirect(url_for("home_web"))

if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)
    # app.run(debug=True, port=1111) Podemos elegir el puerto desde el que trabajar. Cuidado porque
    # hay puertos en uso por el pc y hay que comprobar que este libre.
