from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from app.main import db
db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

    def __init__(self, id, username):
        self.id = id
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id'         : self.id,
            'username': self.username,
            # This is an example how to deal with Many2Many relations
            # 'many2many'  : self.serialize_many2many
        }
    # @property
    # def serialize_many2many(self):
    #     """
    #     Return object's relations in easily serializable format.
    #     NB! Calls many2many's serialize property.
    #     """
    #     return [ item.serialize for item in self.many2many]

