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
    task = Tasks(content=request.form["content_task"], done=False)
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


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)
    # app.run(debug=True, port=1111) Podemos elegir el puerto desde el que trabajar. Cuidado porque
    # hay puertos en uso por el pc y hay que comprobar que este libre.
