from app.bookmarks.bookmarks import Bookmarks
from app.posts.posts import Posts
from config import PATH_BOOKMARKS, PATH_POSTS

from flask import Blueprint, render_template, redirect

bookmarks_blueprint = Blueprint(
    'bookmarks_blueprint',
    __name__,
    template_folder='templates')

posts_for_bookmarks = Posts(PATH_POSTS)
bookmarks = Bookmarks(PATH_BOOKMARKS)


@bookmarks_blueprint.route('/bookmarks.html')
def page_bookmarks():
    bookmarks_all = bookmarks.get_bookmarks_all()
    return render_template('bookmarks.html', bookmarks=bookmarks_all)


@bookmarks_blueprint.route('/bookmarks/add/<int:post_id>')
def page_add_bookmark(post_id):
    #logger.debug(f"Добавление закладки {post_id}")
    post_for_add = posts_for_bookmarks.get_post_by_pk(post_id)
    if not bookmarks.check_bookmarks(post_id):
        bookmarks.add_bookmark(post_for_add)
        return redirect("/", code=302)
    return redirect("/", code = 302)


@bookmarks_blueprint.route('/bookmarks/remove/<int:post_id>')
def page_remove_bookmark(post_id):
    #logger.debug(f"Удаление закладки {post_id}")
    bookmarks.del_bookmark(post_id)
    return redirect("/", code=302)