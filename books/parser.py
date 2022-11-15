from flask_restful import reqparse

book_parser = reqparse.RequestParser()
book_parser.add_argument('title', type=str, help="book name is required", required=True)
book_parser.add_argument('price', type=int)
book_parser.add_argument("author_id", type=int)

