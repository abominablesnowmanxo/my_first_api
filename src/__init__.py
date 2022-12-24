# import os

# from flask import Flask

# from src.persons import persons
# from src.database import db
# from src.swagger import swagger_blueprint


# BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# def create_app(test_config=None):
#     app = Flask(__name__, instance_relative_config=True)

#     if test_config is None:
#         app.config.from_mapping(
#             SECRET_KEY='dev',
#             SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(BASE_DIR, 'database.db'),
#             SQLACHEMY_TRACK_MODIFICATIONS=False,
#             JSON_SORT_KEYS=False
#         )
#     else:
#         app.config.from_mapping(test_config)

#     db.app = app
#     db.init_app(app)
#     app.register_blueprint(persons)
#     app.register_blueprint(swagger_blueprint)


#     return app
