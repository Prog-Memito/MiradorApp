from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SingletonDB:
    _instance = None

    def __new__(cls, app=None):
        if cls._instance is None:
            cls._instance = super(SingletonDB, cls).__new__(cls)
            cls._instance.init_app(app)
        return cls._instance

    def init_app(self, app):
        if app is not None:
            db.init_app(app)

def crear_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edificio.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar SQLAlchemy con la aplicación
    db.init_app(app)

    # Importar y registrar el blueprint
    from views.VistaGastoComun import gastos_comunes_blueprint
    app.register_blueprint(gastos_comunes_blueprint, url_prefix='/api')

    return app