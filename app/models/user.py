from .core import db
from flask_security import SQLAlchemyUserDatastore
from sqlalchemy import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_on = db.Column(db.DateTime(), default=func.now())
    name = db.Column(db.Unicode(100))
    email = db.Column(db.Unicode(100), unique=True)
    phone = db.Column(db.Unicode(30), unique=True)
    password = db.Column(db.String(50))
    active = db.Column(db.Boolean, default=False)


user_datastore = SQLAlchemyUserDatastore(db, User, None)
