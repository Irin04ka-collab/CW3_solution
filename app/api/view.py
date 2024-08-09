import logging

from flask import Blueprint, jsonify

from app.posts.posts import Posts
from config import PATH_POSTS

api_blueprint = Blueprint(
    'api_blueprint',
    __name__,
    template_folder='templates')

posts_for_api = Posts(PATH_POSTS)

logger_api = logging.getLogger("api")

@api_blueprint.route('/api/posts/')
def get_json_all_posts():
    data = posts_for_api.get_posts_all()
    logger_api.info(f'Запрошены все посты через API')
    return jsonify(data)


@api_blueprint.route('/api/posts/<int:post_id>')
def get_json_for_post_id(post_id):
    logger_api.info(f'Запрощен пост {post_id} через API')
    data = posts_for_api.get_post_by_pk(post_id)
    return jsonify(data)
