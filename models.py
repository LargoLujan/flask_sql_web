from sqlalchemy import Column, Integer, String, Boolean, Date
import db

# Esta clase define el modelo de datos de nuestra tabla 'tasks' que utilizaremos en nuestro servidor Flask.
# La clase hereda de la clase Base de SQLAlchemy que a su vez hereda de la clase declarative_base.
# Cada instancia de esta clase representa una fila de nuestra tabla 'tasks'.
class Tasks(db.Base):
    __tablename__ = "tasks" # Este atributo indica el nombre de la tabla en nuestra base de datos.
    __table_args__ = {'sqlite_autoincrement': True} # Este atributo indica que la clave primaria se autoincrementa.
    id_task = Column(Integer, primary_key=True) # Este atributo indica el número de tarea. Es nuestra clave primaria.
    content = Column(String(200), nullable=False) # Este atributo indica el contenido de la tarea.
    done = Column(Boolean) # Este atributo indica si la tarea ha sido completada o no.
    category = Column(String(50), nullable=False) # Este atributo indica la categoría de la tarea.
    due_date = Column(Date, nullable=False) # Este atributo indica la fecha límite de la tarea.

    # Este método constructor define cómo se crea una tarea.
    def __init__(self, content, done, category, due_date):
        self.content = content
        self.done = done
        self.category = category
        self.due_date = due_date

    # Este método define cómo se representa una tarea como una cadena de caracteres.
    def __str__(self):
        return "Tarea: Nº {} = {} -> {})".format(self.id_task, self.content, self.done)

