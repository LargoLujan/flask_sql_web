from sqlalchemy import Column, Integer, String, Boolean, Date
from werkzeug.security import generate_password_hash, check_password_hash
import db


class Tasks(db.Base):
    __tablename__ = "tasks"
    __table_args__ = {'sqlite_autoincrement': True}
    id_task = Column(Integer, primary_key=True)
    content = Column(String(200), nullable=False)
    done = Column(Boolean)
    category = Column(String(50), nullable=False)
    due_date = Column(Date, nullable=False)

class Access(db.Base):
    __tablename__="access"
    __table_args___ = {"sqlite_autoincrement": True}
    id_access = Column(Integer, primary_key = True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)

    def __init__(self, content, done, category, due_date, username, password):
        self.content = content
        self.done = done
        self.category = category
        self.due_date = due_date
        self.username = username
        self.password = password

    def check_password(self):
        return f'<User {self.username}>'

    def __repr__(self):
        return check_password_hash(self.password, password)

    def __str__(self):
        return "Tarea: Nº {} = {} -> {})".format(self.id_task, self.content, self.done)


