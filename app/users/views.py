from app.posts.posts import Posts
from config import PATH_POSTS

from flask import Blueprint, render_template

users_blueprint = Blueprint(
    'users_blueprint',
    __name__,
    template_folder='templates')

posts_for_users = Posts(PATH_POSTS)


@users_blueprint.route('/user-feed/<user_name>')
def page_post_by_user(user_name):
    posts_by_user = posts_for_users.get_posts_by_user(user_name)
    return render_template('user-feed.html', posts_by_user=posts_by_user,
                           user_name=user_name)

