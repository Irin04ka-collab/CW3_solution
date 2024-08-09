import pytest

from app.bookmarks.bookmarks import Bookmarks
from app.comments.comments import Comments
from app.posts.posts import Posts
from config import PATH_POSTS, PATH_COMMENTS, PATH_BOOKMARKS


@pytest.fixture
def posts_dao():
    return Posts(PATH_POSTS)

@pytest.fixture
def keys_should_be():
    return {"poster_name", "poster_avatar", "pic", "content",
            "views_count", "likes_count", "pk"}

@pytest.fixture
def comments_dao():
    return Comments(PATH_COMMENTS)

@pytest.fixture
def bookmarks_dao():
    return Bookmarks(PATH_BOOKMARKS)


