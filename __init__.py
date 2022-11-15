from flask import Flask
from flask_restful import Api
from app.models import db
from app.config import config as AppConfig
from flask_migrate import Migrate
from app.books.api_views import BookList, Book_Details

def create_app(config_name):
    app = Flask(__name__)
    current_config = AppConfig[config_name]

    app.config["SQLALCHEMY_DATABASE_URI"] = current_config
    app.config.from_object(current_config)
    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app)
    api.add_resource(BookList, '/books')
    api.add_resource(Book_Details, '/books/<int:book_id>')


    from app.books import books_blueprint
    app.register_blueprint(books_blueprint)
    return app