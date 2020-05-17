from flask import Flask, json
import requests

app = Flask(__name__)


# generic reusable function for translating get request to json
def get_json(url):
    request = requests.get(url)
    response_data = request.json()
    response = app.response_class(response=json.dumps(response_data), status=200, mimetype='application/json')
    return response


@app.route("/posts")
def get_posts():
    return get_json('https://jsonplaceholder.typicode.com/posts')


@app.route("/posts/<post_id>")
def get_post_by_id(post_id):
    return get_json('https://jsonplaceholder.typicode.com/posts/' + post_id)


@app.route("/posts/<post_id>/comments")
def get_post_comments(post_id):
    return get_json('https://jsonplaceholder.typicode.com/posts/' + post_id + '/comments')


@app.route("/users/<user_id>")
def get_single_users_posts(user_id):
    return get_json('https://jsonplaceholder.typicode.com/users/' + user_id)


if __name__ == "__main__":
    app.run()
