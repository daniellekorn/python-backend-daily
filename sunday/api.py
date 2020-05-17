from flask import Flask, json
from sunday.classes.jsonablePost import JsonablePost
from datetime import datetime
import requests

app = Flask(__name__)


global_post_dict = {}


@app.before_first_request
def get_all_posts():
    get_posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    response_data = get_posts.json()
    for i in response_data:
        current_post = JsonablePost(i['userId'], i['id'], i['title'], i['body'], datetime.now())
        post_instance = ({i['id']: current_post.return_as_obj()})
        global_post_dict.update(post_instance)

    print(global_post_dict)


if __name__ == "__main__":
    app.run()
