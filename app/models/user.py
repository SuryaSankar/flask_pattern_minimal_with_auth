from .core import db
from flask_security import (
    SQLAlchemyUserDatastore, UserMixin, RoleMixin)
from sqlalchemy import func


class UserRole(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_on = db.Column(db.DateTime(), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_on = db.Column(db.DateTime(), default=func.now())
    name = db.Column(db.Unicode(100))
    email = db.Column(db.Unicode(100), unique=True)
    phone = db.Column(db.Unicode(30), unique=True)
    password = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=False)

    roles = db.relationship(
        "Role", secondary=UserRole.__table__)

    def __repr__(self):
        if self.name:
            return "{} <{}>".format(
                self.name, self.email)
        return self.email


class Role(db.Model, RoleMixin):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_on = db.Column(db.DateTime(), default=func.now())
    name = db.Column(db.String(30), unique=True)
    description = db.Column(db.String(200))

    users = db.relationship(
        "User", secondary=UserRole.__table__)

    def __repr__(self):
        return self.name


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
