from flask import Flask
from .models.core import db
from .models.user import user_datastore
from . import views
from flask_security import Security


def register_blueprints_on_app(app):
    app.register_blueprint(views.main_pages_bp)
    app.register_blueprint(views.main_api_bp, url_prefix='/api')


def create_app(register_blueprints=True):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('app.default_config')
    app.config.from_pyfile('application.cfg.py')

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        "{db_prefix}://{user}:{passwd}@{server}/{db}".format(
        db_prefix=app.config['SQLALCHEMY_DB_PREFIX'],
        user=app.config['DB_USERNAME'],
        passwd=app.config['DB_PASSWORD'],
        server=app.config['DB_SERVER'],
        db=app.config['DB_NAME'])
    db.init_app(app)

    if register_blueprints:
        register_blueprints_on_app(app)

    Security(
        app, user_datastore)

    return app
