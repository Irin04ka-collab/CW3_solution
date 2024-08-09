import pytest


class TestComments:

    parameters_to_get_comments_by_post = [(1, {1, 2, 3, 4}), (2, {5, 6, 7, 8})]
    @pytest.mark.parametrize("post_pk, correct_comments_pk", parameters_to_get_comments_by_post)
    def test_get_comments_by_post_pk(self, post_pk, correct_comments_pk, comments_dao):
        """Проверка что по посту выдается корректный набоор комментов"""
        comments_dict = comments_dao.get_comments_by_post_id(post_pk)
        comments_pk = set()
        for comment_dict in comments_dict:
            comments_pk.add(comment_dict['pk'])

        assert comments_pk == correct_comments_pk, f"Не корректный набор комментов по посту {post_pk}"

