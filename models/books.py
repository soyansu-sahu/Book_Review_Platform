from app import db
from sqlalchemy import func
from app.models.reviews import Review

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    publication_year = db.Column(db.Integer)

    @staticmethod
    def average_rating():
        return func.coalesce(func.avg(Review.rating), 0)
