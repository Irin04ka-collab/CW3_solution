import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request, abort

from app.bookmarks.bookmarks import Bookmarks
from app.comments.comments import Comments
from app.posts.posts import Posts
from config import PATH_COMMENTS, PATH_POSTS, PATH_BOOKMARKS

logger = logging.getLogger("basic")
# logging.basicConfig(filename='./logs/api.log', level=logging.INFO,
#                     format='%(asctime)s [%(levelname)s] %(message)s')


posts_blueprint = Blueprint(
    'posts_blueprint',
    __name__,
    template_folder='templates')

posts_dao = Posts(PATH_POSTS)
comments_dao = Comments(PATH_COMMENTS)
bookmarks_for_app = Bookmarks(PATH_BOOKMARKS)


@posts_blueprint.route('/')
def page_index():

    logger.debug("Открытие главной")
    try:
        posts_list = posts_dao.get_posts_all()
        count_bookmarks = bookmarks_for_app.get_count_bookmarks()
        return render_template('index.html', posts_list=posts_list,
                               count_bookmarks=count_bookmarks)
    except:
        return "Что-то пошло не так"

@posts_blueprint.route('/posts/<int:post_id>/')
def page_post(post_id):

    try:
        post_by_id = posts_dao.get_post_by_pk(post_id)
        comments = comments_dao.get_comments_by_post_id(post_id)
    except (JSONDecodeError, FileNotFoundError) as error:
        return render_template('error.html', error=error)
    else:
        if post_by_id is None:
            abort(404)
        count_comments = len(comments)
        tags = posts_dao.get_tag(post_id)
        return render_template('post.html', post_by_id=post_by_id,
                               comments=comments, count_comments=count_comments, tags=tags)


@posts_blueprint.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "Такой пост не найден", 404
        # render_template('404.html'), 404)


@posts_blueprint.route('/search/')
def page_search():
    query = request.args.get('s', "")
    logger.debug(f'сlово для поиска - {query}')

    if query != "":
        posts_by_key_word = posts_dao.get_posts_by_search(query)
        count_posts = len(posts_by_key_word)
    else:
        posts_by_key_word = []
        count_posts = 0

    return render_template('search.html',
                           posts_by_key_word=posts_by_key_word,
                           count_posts=count_posts,
                           query=query)


@posts_blueprint.route('/tag/<tag_word>')
def page_tag(tag_word):
    key_word = "#"+tag_word
    posts_by_tag = posts_dao.get_posts_by_search(key_word)
    return render_template('tag.html', posts_by_tag=posts_by_tag, tag_word=tag_word)



