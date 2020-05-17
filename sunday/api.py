from flask import Flask, json
from sunday.classes.jsonablePost import JsonablePost
from datetime import datetime, timedelta
import requests
import random

app = Flask(__name__)


global_posts_dict = {}


@app.before_first_request
def get_all_posts():
    get_posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    response_data = get_posts.json()
    for i in response_data:
        current_post = JsonablePost(i['userId'], i['id'], i['title'], i['body'], random_date())
        post_instance = ({i['id']: current_post.return_as_obj()})
        global_posts_dict.update(post_instance)
    print(global_posts_dict)


def random_date():
    end = datetime.now()
    start = end - timedelta(weeks=30)
    date = start + (end - start) * random.random()
    str_date = date.strftime('%m/%d/%Y')
    return str_date


if __name__ == "__main__":
    app.run()
