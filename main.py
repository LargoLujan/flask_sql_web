from _curses import flash
from datetime import datetime
from flask_login import login_user, logout_user, login_required
from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tasks, Access

app = Flask(__name__)  # En app se encuentra nuestro servidor web de Flask


@app.route("/")
def home_web():
    every_tasks = db.session.query(Tasks).all()
    for i in every_tasks:
        print(i)
    return render_template("index.html", task_list=every_tasks)


@app.route("/create_task", methods=["POST"])
def create():
    due_date = datetime.strptime(request.form["due_date"], "%Y-%m-%d").date()
    task = Tasks(content=request.form["content_task"], done=False, category=request.form["category"], due_date=due_date)
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user is None or not check_password_hash(user.password, request.form['password']):
            flash('Usuario o contraseña inválido')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)
    # app.run(debug=True, port=1111) Podemos elegir el puerto desde el que trabajar. Cuidado porque
    # hay puertos en uso por el pc y hay que comprobar que este libre.
