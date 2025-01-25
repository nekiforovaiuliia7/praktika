from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/books.db'
db = SQLAlchemy(app)
CORS(app)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'category': book.category,
        'year': book.year,
        'price': book.price,
        'status': book.status
    } for book in books])

if __name__ == '__main__':
    app.run(debug=True)