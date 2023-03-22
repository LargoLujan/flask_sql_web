from sqlalchemy import Column, Integer, String, Boolean, Date
import db


class Tasks(db.Base):
    __tablename__ = "tasks"
    __table_args__ = {'sqlite_autoincrement': True}
    id_task = Column(Integer, primary_key=True)
    content = Column(String(200), nullable=False)
    done = Column(Boolean)
    category = Column(String(50), nullable=False)
    due_date = Column(Date, nullable=False)

    def __init__(self, content, done, category, due_date):
        self.content = content
        self.done = done
        self.category = category
        self.due_date = due_date

    def __str__(self):
        return "Tarea: Nº {} = {} -> {})".format(self.id_task, self.content, self.done)


