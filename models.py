"""Models for Adoption."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Model to create a new pet record"""
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text, nullable=True)

    age = db.Column(db.Integer, nullable=False)

    notes = db.Column(db.Text, nullable=True)

    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"< pet id ='{self.id}' name='{self.name}' >"
