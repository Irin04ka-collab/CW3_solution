from flask import json

from app.posts.posts import Posts
from config import PATH_POSTS

posts_dao = Posts(PATH_POSTS)

class Comments:

    def __init__(self, path_comments):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path_comments = path_comments


    def _load_comments(self):
        """загружает данные из файла"""
        with open(self.path_comments, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data


    def get_comments_by_post_id(self, post_id):
        """возвращает комментарии определенного поста. Функция должна вызывать
        ошибку `ValueError` если такого поста нет и пустой список, если у поста нет комментов. """
        comments_list = []
        comments = self._load_comments()

        for comment in comments:
            if comment['post_id'] == post_id:
                comments_list.append(comment)
        return comments_list

# comments_dao = Comments("../../data/comments.json")
# # print(f"длина {posts.get_comments_by_post_id(1)[1]}, список  {posts.get_comments_by_post_id(1)[0]}")
# print(comments_dao.get_comments_by_post_id(1))
# print(type(comments_dao.get_comments_by_post_id(1)))
