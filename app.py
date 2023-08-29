from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Configuracion de la base de datos

USER_DB = 'root'
PASS_DB = 'junior26'
URL_DB = 'localhost'
NAME_DB = 'flask_sqlalchemy'

FULL_URL_DB = F'mysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Configuracion de la migración

migrate = Migrate()
migrate.init_app(app, db)

#Escribimos la clase que se va a mapear

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    correo = db.Column(db.String(250))

    def __init__(self, id, nombre, apellido, correo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def json(self):
        return {'id': self.id, 'nombre': self.nombre, 'apellido': self.apellido, 'correo': self.correo}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

