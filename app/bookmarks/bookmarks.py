from flask import json


class Bookmarks:

    def __init__(self, path_bookmarks):
        """ При создании экземпляра нужно указать путь к файлу с данными"""
        self.path_bookmarks = path_bookmarks

    def _load_bookmarks(self):
        """загружает данные из файла"""
        with open(self.path_bookmarks, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data


    def _write_bookmarks(self, data):
        with open(self.path_bookmarks, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)


    def get_bookmarks_all(self):
        """возвращает посты  в закладках"""
        bookmarks = self._load_bookmarks()
        return bookmarks

    def get_count_bookmarks(self):
        bookmarks = self._load_bookmarks()
        return len(bookmarks)

    def check_bookmarks(self, post_id):
        bookmarks = self._load_bookmarks()
        for bookmark in bookmarks:
            if bookmark['pk'] == int(post_id):
                return True
        return False

    def add_bookmark(self, new_bookmark):
        bookmarks = self._load_bookmarks()
        bookmarks.append(new_bookmark)
        self._write_bookmarks(bookmarks)


    def del_bookmark(self, post_id):
        bookmarks = self._load_bookmarks()
        i = 0
        for bookmark in bookmarks:
            if bookmark['pk'] == int(post_id):
                break
            i += 1
        bookmarks.pop(i)
        self._write_bookmarks(bookmarks)


# b = Bookmarks('../data/bookmarks.json')
# print(b.get_count_bookmarks())
# new = {
#     "poster_name": "hank",
#     "poster_avatar": "https://randus.org/avatars/m/383c7e7e3c3c1818.png",
#     "pic": "https://images.unsplash.com/photo-1612450632008-22c2a5437dc1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
#     "content": "Смотрите-ка – ржавые елки! Раньше на этом месте была свалка старых машин, а потом все засыпали песком. Теперь тут ничего не растет – только ржавые елки , кусты и грязь. Да и не может тут ничего расти: слишком много пыли и песка. Зато теперь стало очень красиво – все-таки это не свалка.",
#     "views_count": 187,
#     "likes_count": 67,
#     "pk": 3
# }
# b.add_bookmark(new)
# print(b.get_count_bookmarks())
# b.del_bookmark(3)
# print(b.get_count_bookmarks())

