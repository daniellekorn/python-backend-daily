from flask import Flask, json
from sunday.classes.jsonablePost import JsonablePost
from sunday.classes.basePost import BasePost
import requests

app = Flask(__name__)


@app.before_first_request
def get_all_posts():
    get_posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    response_data = get_posts.json()
    for i in response_data:
        new_item = BasePost(i['userId'], i['id'], i['title'], i['body'])
        print(new_item)


if __name__ == "__main__":
    app.run()
