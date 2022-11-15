import os

class Config:
    pass

@staticmethod
def init_app():
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"


class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:portnumber/dbname"
    # SQLALCHEMY_DATABASE_URI = os.environ(DATABASE_CONGFIG)
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost:5432/flask_books"



config = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig
}