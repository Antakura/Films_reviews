from datetime import date

from . import db


class Films(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(63), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    path = db.Column(db.String(63))
    reviews = db.relationship('Reviews', back_populates='film')


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.Date, default=date.today)
    score = db.Column(db.Integer, nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'), nullable=False)
    film = db.relationship('Films', back_populates='reviews')
