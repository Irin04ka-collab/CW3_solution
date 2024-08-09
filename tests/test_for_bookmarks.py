
class TestBookmarks:

    def test_get_all_check_type(self, bookmarks_dao):
        """ Проверяем, верный ли список постов возвращается """

        bookmarks = bookmarks_dao.get_bookmarks_all()
        assert type(bookmarks) == list, "список постов не возвращается как тип list"
        assert type(bookmarks[0]) == dict, "пост не возвращается как словарь"


    def test_get_count_bookmarks(self):
        """ Проверяем верное количество комментариев выводится """

        pass

    def test_check_bookmarks(self):
        pass
