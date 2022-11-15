from app.books import books_blueprint

@books_blueprint.route("/")
def index():
    return "<h1>hiiii</h1>"