import pytest

class TestPosts:

    # получение списка постов
    def test_get_all_check_type(self, posts_dao):
        """ Проверяем, верный ли список постов возвращается """
        posts = posts_dao.get_posts_all()
        assert type(posts) == list, "список постов не возвращается как тип list"
        assert type(posts[0]) == dict, "пост не возвращается как словарь"
        # assert len(posts) > 0, "возвращается пустой список"

    def test_get_all_check_structure(self, posts_dao, keys_should_be):
        posts = posts_dao.get_posts_all()
        set_keys = set(posts[0].keys())
        assert set_keys == keys_should_be, "Неправильный набор ключей"

    # получение одного поста
    def test_get_one_check_type(self, posts_dao):
        """ Проверяем, верный ли список постов возвращается """
        post = posts_dao.get_post_by_pk(1)
        assert type(post) == dict, "пост не возвращается как словарь"

    def test_get_one_check_structure(self, posts_dao, keys_should_be):
        post = posts_dao.get_post_by_pk(1)
        set_keys = set(post.keys())
        assert set_keys == keys_should_be, "Неправильный набор ключей"

    parameters_to_get_by_pk = range(1,8)

    @pytest.mark.parametrize("post_pk", parameters_to_get_by_pk)
    def test_get_one_check_type_has_correct_pk(self, posts_dao, post_pk):
        post = posts_dao.get_post_by_pk(post_pk)
        assert post['pk'] == post_pk, f"Номер поста {post['pk']} не соответсвует ожидаемому"


    #посты по пользователю

    def test_get_by_user_check_type(self, posts_dao):
        """ Проверяем, верный ли список постов возвращается """
        posts = posts_dao.get_posts_by_user("leo")
        assert type(posts) == list, "список постов не возвращается как тип list"
        assert type(posts[0]) == dict, "пост не возвращается как словарь"
        # assert len(posts) > 0, "возвращается пустой список"

    def test_get_by_user_check_structure(self, posts_dao, keys_should_be):
        posts = posts_dao.get_posts_by_user("leo")
        set_keys = set(posts[0].keys())
        assert set_keys == keys_should_be, "Неправильный набор ключей"


    parameters_to_get_by_user = [
        ("leo", {1, 5}),
        ("johnny", {2, 6}),
        ("hank", {3, 7}) #,
        # ("hankhank", {})
    ]

    @pytest.mark.parametrize("poster_name, correct_pk", parameters_to_get_by_user)
    def test_get_posts_by_user(self, posts_dao, poster_name, correct_pk):
        "Проверка что по пользователю выдается корректный набоор постов"

        posts = posts_dao.get_posts_by_user(poster_name)
        posts_by_user = set()
        for post in posts:
            posts_by_user.add(post["pk"])

        assert posts_by_user == set(correct_pk), f"Не корректный набор постов по {poster_name}"

    # поиск

    post_parameters_search = [("тарелка", {1}),
                              ("елки", {3}),
                              ("проснулся", {4}),
                              ("Дом", {2, 7, 8}),
                              ("000000000", set())
                              ]

    @pytest.mark.parametrize("query, correct_pk", post_parameters_search)
    def test_get_posts_by_query(self, posts_dao, query, correct_pk):
        """Проверка что по строке поиска выдается корректный набоор постов"""

        posts = posts_dao.get_posts_by_search(query)
        posts_by_query = set()
        for post in posts:
            posts_by_query.add(post["pk"])

        assert posts_by_query == correct_pk, f"Не корректный набор постов по строке поиска {query}"


    tag_parametres_by_post = [(2, {"инста"}), (5, {"кот", "котики", "инста", "инстаграм",
                                               "любовькживотным", "любимыйкот"})]

    @pytest.mark.parametrize("post_pk, tags", tag_parametres_by_post)
    def test_get_tag_by_post(self, posts_dao, post_pk, tags):
        """Проверка что по посту выдается корректный набоор тэгов"""

        tags_by_post = set(posts_dao.get_tag(post_pk))

        assert tags_by_post == tags, f"Не корректный набор тэгов по посту {post_pk}"

