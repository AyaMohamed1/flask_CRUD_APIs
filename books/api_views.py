from flask_restful import Resource, marshal_with, fields, abort
from flask import make_response
from app.models import Book ,db
from app.books.parser import book_parser

author_serializer = {
    "id": fields.Integer,
    "name": fields.String
}


book_serilizer = {
    "id": fields.Integer,
    "title": fields.String,
    "price": fields.Integer,
    "author_id": fields.Integer,
    "author": fields.Nested(author_serializer)
}

class BookList(Resource):
    @marshal_with(book_serilizer)
    def get(self):
        books = Book.query.all()
        return books, 200

    @marshal_with(book_serilizer)
    def post(self):
        book_args = book_parser.parse_args()
        book = Book(**book_args)
        db.session.add(book)
        db.session.commit()

        return book, 201

    
class Book_Details(Resource):
    @marshal_with(book_serilizer)
    def get(self, book_id):
        book = Book.query.get(book_id)
        if book :
            return book, 200
        else:
            abort(404, message="Book not found ")

    @marshal_with(book_serilizer)
    def put(self, book_id):
        book = Book.query.get(book_id)
        if book:
            book_args = book_parser.parse_args()
            book.title = book_args["title"]
            book.price = book_args['price']
            book.author_id = book_args["author_id"]
            db.session.add(book)
            db.session.commit()
            return book, 200

        else:
            abort(404, message="Book not found ")

    def delete(self, book_id):
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            response = make_response("done", 204)
            return response
        else:
            abort(404, message="Book not found ")

