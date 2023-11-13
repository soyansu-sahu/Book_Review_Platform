from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.reviews import Review
from app.models.books import Book
from app.models.users import User
from app import db

bp = Blueprint('books', __name__)

@bp.route('/books', methods=['POST'])
@jwt_required()
def add_book():
    current_user = get_jwt_identity()
    print(request.data)
    if not User.query.get(current_user).role == 'admin':
        return jsonify({"message": "Access forbidden"}), 403
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    genre = data.get('genre')
    publication_year = data.get('publication_year')

    if not title or not author:
        return jsonify({"message": "Title and Author are required"}), 400

    book = Book(title=title, author=author, genre=genre, publication_year=publication_year)
    db.session.add(book)
    db.session.commit()

    return jsonify({"message": "Book added successfully"}), 201

@bp.route('/books', methods=['GET'])
def get_books():
    title = request.args.get('title')
    author = request.args.get('author')
    genre = request.args.get('genre')
    rating = request.args.get('rating')
    publication_year = request.args.get('publication_year')

    # Start with all books
    books_query = Book.query

    # Apply filters
    if title:
        books_query = books_query.filter(Book.title.ilike(f'%{title}%'))
    if author:
        books_query = books_query.filter(Book.author.ilike(f'%{author}%'))
    if genre:
        books_query = books_query.filter(Book.genre.ilike(f'%{genre}%'))
    if rating:
        books_query = books_query.filter(Book.average_rating() >= float(rating))
    if publication_year:
        books_query = books_query.filter(Book.publication_year == int(publication_year))

    # Retrieve filtered books
    books = books_query.all()

    # Convert books to a list of dictionaries
    book_list = [{"id": book.id, "title": book.title, "author": book.author,
                  "genre": book.genre, "publication_year": book.publication_year} for book in books]

    return jsonify({"books": book_list}), 200


@bp.route('/books/<int:book_id>/rate', methods=['POST'])
@jwt_required()
def rate_book(book_id):
    current_user = get_jwt_identity()
    data = request.get_json()

    rating = data.get('rating')

    if not rating or not 1 <= rating <= 5:
        return jsonify({"message": "Invalid rating"}), 400

    book = Book.query.get(book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    # Check if the user has already rated the book
    existing_review = Review.query.filter_by(user_id=current_user, book_id=book_id).first()
    if existing_review:
        return jsonify({"message": "User has already rated this book"}), 400

    review = Review(user_id=current_user, book_id=book_id, rating=rating, text="User rating")
    db.session.add(review)
    db.session.commit()

    return jsonify({"message": "Book rated successfully"}), 201
