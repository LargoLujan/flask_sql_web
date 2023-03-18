# Engine. El engine permite a SQLAlchemy comunicarse con la Base de datos
# https://docs.sqlalchemy.org/en/14/core/engines.html
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///database/tasks.db')
# Advertencia, crear el engine no conecta inmediatamente a la base de datos eso lo hacemos más adelante

# Ahora creamos la sesión lo que nos permite realizar transacciones (operaciones) dentro de nuestra BD
Session = sessionmaker(bind=engine)
session = Session()

# Indicarle al ORM que su trabajo principal va a ser transformar clases en tablas
# Ahora vamos al fichero models.poy y en los modelos (clases) donde queremos que se transformen en tablas,
# le añadiremos esta variable, y esto se encargara de mapear y vincular la clase a la tabla
Base = declarative_base()
