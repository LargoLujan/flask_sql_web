from sqlalchemy import Column, Integer, String, Boolean
import db


class Tasks(db.Base):
    __tablename__ = "tasks"
    __table_args__ = {'sqlite_autoincrement': True}
    id_task = Column(Integer, primary_key=True)
    content = Column(String(200), nullable=False)
    done = Column(Boolean)
    category = Column(String(50), nullable=False)

    def __init__(self, content, done, category):
        self.content = content
        self.done = done
        self.category = category

    def __str__(self):
        return "Tarea: Nº {} = {} -> {})".format(self.id_task, self.content, self.done)


