from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    books = db.relationship('Book', backref='author', lazy=True)



class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    price = db.Column(db.Integer)
    author_id= db.Column(db.Integer, db.ForeignKey('author.id'),
        nullable=False)