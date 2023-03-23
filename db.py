# Motor. El motor permite a SQLAlchemy comunicarse con la base de datos.
# https://docs.sqlalchemy.org/en/14/core/engines.html
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Creamos el motor y especificamos que trabajaremos con una base de datos SQLite.
# También le indicamos a la conexión que permita trabajar en diferentes hilos (threads).
engine = create_engine('sqlite:///database/tasks.db', connect_args={"check_same_thread": False})
# connect_args indica que las funciones en segundo plano funcionen sin problemas con el HTML.
connect_args = {'check_same_thread': False}

# ¡Ojo! La creación del motor no nos conecta inmediatamente a la base de datos.
# Esto lo haremos más adelante.

# Ahora creamos la sesión, lo que nos permite realizar transacciones (operaciones) dentro de nuestra base de datos.
# De esta forma, podemos consultar, crear, actualizar o eliminar registros.
Session = sessionmaker(bind=engine)
session = Session()

# Indicamos al ORM que su trabajo principal será transformar clases en tablas.
# Vamos al archivo models.py y en las clases que queremos transformar en tablas,
# agregamos esta variable. Esto se encargará de mapear y vincular la clase a la tabla.
Base = declarative_base()


