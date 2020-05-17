from flask import Flask, json
import requests

app = Flask(__name__)


@app.route("/posts")
def get_posts():
    posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = posts_response.json()
    response = app.response_class(response=json.dumps(posts), status=200, mimetype='application/json')
    return response


@app.route("/posts/<post_id>")
def get_post_by_id(post_id):
    post_response = requests.get('https://jsonplaceholder.typicode.com/posts/' + post_id)
    post = post_response.json()
    response = app.response_class(response=json.dumps(post), status=200, mimetype='application/json')
    return response


@app.route("/users/<user_id>")
def get_users_posts(user_id):
    user_response = requests.get('https://jsonplaceholder.typicode.com/users/' + user_id)
    user_posts = user_response.json()
    response = app.response_class(response=json.dumps(user_posts), status=200, mimetype='application/json')
    return response


@app.route("/posts/<post_id>/comments")
def get_post_comments(post_id):
    posts_response = requests.get('https://jsonplaceholder.typicode.com/posts/' + post_id + '/comments')
    posts = posts_response.json()
    response = app.response_class(response=json.dumps(posts), status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run()
