from flask import json
import logging
from app.users.users import get_list_of_users

logger1 = logging.getLogger("basic")


class Posts:

    def __init__(self, path_posts):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path_posts = path_posts


    def _load_posts(self):
        """загружает данные из файла"""
        with open(self.path_posts, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data


    def get_posts_all(self):
        """возвращает посты"""
        posts = self._load_posts()
        return posts


    def get_post_by_pk(self, pk):
        """возвращает один пост по его идентификатору. """
        posts = self.get_posts_all()

        for post in posts:
            #logger1.debug(f"печатаем pk {pk} и post['pk'] = {post['pk']}")
            if post["pk"] == pk:
                return post



    def get_posts_by_user(self, user_name):
        """возвращает посты определенного пользователя. Функция должна вызывать ошибку
         `ValueError` если такого пользователя нет и пустой список, если у пользователя нет постов."""
        posts = self._load_posts()
        user_list = get_list_of_users()
        if user_name.lower() in user_list:
            users_posts = []
            for post in posts:
                if post['poster_name'].lower() == user_name.lower():
                    users_posts.append(post)
            return users_posts
        else:
            raise ValueError



    def get_posts_by_search(self, query):
        """возвращает кортеж: список постов по ключевому слову и количество найденных постов"""
        posts = self.get_posts_all()
        # logger1.debug(f"список {posts}")
        posts_list = []
        query_lower = query.lower()
        for post in posts:
            if query_lower in post['content'].lower():
                posts_list.append(post)
        return posts_list


    def get_tag(self, post_id):
        """возвращает список тэгов"""

        post = self.get_post_by_pk(post_id)
        content = post['content']
        tag_list = []
        for i, letter in enumerate(content):
            if letter == '#':
                string_ = content[i+1:]
                if ' ' in  string_:
                    pos_space = string_.find(' ')
                    tag = string_[:pos_space]
                else:
                    tag = string_
                tag_list.append(tag)
        return tag_list



# posts = Posts(PATH_POSTS, PATH_COMMENTS)
# # print(f"длина {posts.get_comments_by_post_id(1)[1]}, список  {posts.get_comments_by_post_id(1)[0]}")
# print(posts.get_tag(5))