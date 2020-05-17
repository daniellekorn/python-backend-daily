from flask import Flask
from sunday.classes.jsonablePost import JsonablePost
from sunday.classes.comment import Comment
from datetime import datetime, timedelta
import requests
import random


app = Flask(__name__)

global_posts_dict = {}
post_comments = {}


# @app.before_first_request
def get_all_posts():
    get_posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    response_data = get_posts.json()
    for post in response_data:
        current_post = JsonablePost(post, created_at())
        global_posts_dict[post['id']] = current_post.to_json()
    return global_posts_dict


def get_comments(post_id):
    comments = requests.get('https://jsonplaceholder.typicode.com/posts/' + str(post_id) + '/comments')
    response_data = comments.json()
    for i in response_data:
        current_comment = Comment(i['postId'], i['id'], i['name'], i['email'], i['body'])
        post_comments[i['id']] = current_comment


@app.before_first_request
def comments_up_to_post_ten():
    return [get_comments(n) for n in range(1, 11)]


# function to generate random recent date for realistic post creation time
def created_at():
    end = datetime.now()
    start = end - timedelta(weeks=30)
    random_date = start + (end - start) * random.random()
    str_date = random_date.strftime('%m/%d/%Y %H:%M:%S')
    return str_date


if __name__ == "__main__":
    app.run()
