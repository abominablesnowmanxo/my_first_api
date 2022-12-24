import os

from flask import Flask

from src.persons import persons
from src.database import db
from src.swagger import swagger_blueprint


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

db.app = app
db.init_app(app)
app.register_blueprint(persons)
app.register_blueprint(swagger_blueprint)


if __name__ == '__main__':
    app.run()
