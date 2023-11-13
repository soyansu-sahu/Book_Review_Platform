from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.reviews import Review
from app.models.books import Book
from app.models.users import User


from app import db

bp = Blueprint('reviews', __name__)

@bp.route('/reviews', methods=['POST'])
@jwt_required()
def add_review():
    current_user = get_jwt_identity()

    data = request.get_json()

    book_id = data.get('book_id')
    rating = data.get('rating')
    text = data.get('text')

    if not book_id or not rating or not text:
        return jsonify({"message": "Book ID, Rating, and Text are required"}), 400

    book = Book.query.get(book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    review = Review(user_id=current_user, book_id=book_id, rating=rating, text=text)
    db.session.add(review)
    db.session.commit()

    return jsonify({"message": "Review added successfully"}), 201

@bp.route('/reviews/<int:review_id>', methods=['PUT', 'DELETE'])
@jwt_required()
def manage_review(review_id):
    current_user = get_jwt_identity()
    review = Review.query.get(review_id)

    if not review:
        return jsonify({"message": "Review not found"}), 404

    if not current_user == review.user_id and not User.query.get(current_user).role == 'admin':
        return jsonify({"message": "Access forbidden"}), 403

    if request.method == 'PUT':
        data = request.get_json()
        review.rating = data.get('rating', review.rating)
        review.text = data.get('text', review.text)
        db.session.commit()
        return jsonify({"message": "Review updated successfully"}), 200

    elif request.method == 'DELETE':
        db.session.delete(review)
        db.session.commit()
        return jsonify({"message": "Review deleted successfully"}), 200
