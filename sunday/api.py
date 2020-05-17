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
        new_item = JsonablePost(i['userId'], i['id'], i['title'], i['body'], datetime.now())
        post_dict_with_id_key = ({i['id']: new_item})
        global_post_dict.update(post_dict_with_id_key)

    print(global_post_dict)


if __name__ == "__main__":
    app.run()
