import json


def get_list_of_users():
    user_list = []

    with open('./data/posts.json', "r", encoding="utf-8") as file:
        posts = json.load(file)

    for post in posts:
        user_list.append(post["poster_name"])

    with open('./data/comments.json', "r", encoding="utf-8") as file:
        comments = json.load(file)

    for comment in comments:
        user_list.append(comment["commenter_name"])

    user_set = set(user_list)
    return list(user_set)

