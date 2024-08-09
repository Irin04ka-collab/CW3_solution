from flask import Flask

from app.api.view import api_blueprint
from app.posts.views import posts_blueprint
from app.bookmarks.view import bookmarks_blueprint
from app.users.views import users_blueprint
from app import logger

app = Flask(__name__)

logger.create_logger()

app.register_blueprint(posts_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(users_blueprint)



if __name__ == "__main__":
    app.run(port=8000)
