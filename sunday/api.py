from flask import Flask, json
from sunday.classes.jsonablePost import JsonablePost
from sunday.classes.comment import Comment
from sunday.modules.randomDate import created_at
import requests


app = Flask(__name__)

global_posts_dict = {}
post_comments = {}


@app.before_first_request
def get_all_posts():
    req_posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    response_data = req_posts.json()
    for post in response_data:
        current_post = JsonablePost(post, created_at())
        global_posts_dict[post['id']] = current_post.return_as_obj()
    return global_posts_dict


# adds comments as an array to post num key for 1-10 in global post_comments dict
@app.before_first_request
def get_comments():
    for n in range(1, 11):
        post_comments.update({n: []})
        comments = requests.get('https://jsonplaceholder.typicode.com/posts/' + str(n) + '/comments')
        response_data = comments.json()
        for i in response_data:
            current_comment = Comment(i['postId'], i['id'], i['name'], i['email'], i['body'])
            post_comments[i['postId']].append(current_comment)
    return post_comments


# appends the comments as an array to each post item in global_posts_dict
@app.before_first_request
def add_comments_to_post_info():
    for n in range(1, 11):
        global_posts_dict.get(n).update({'comments': post_comments[n]})
    return global_posts_dict


@app.route("/posts")
def get_posts():
    return app.response_class(response=json.dumps(global_posts_dict), status=200, mimetype='application/json')


@app.route("/posts/<post_id>")
def get_post_by_id(post_id):
    posts = global_posts_dict[int(post_id)]
    return app.response_class(response=json.dumps(posts), status=200,
                              mimetype='application/json')


@app.route("/posts/<post_id>/comments")
def get_post_comments(post_id):
    comments = global_posts_dict[int(post_id)]['comments']
    return app.response_class(response=json.dumps(comments), status=200, mimetype='application/json')


@app.route("/posts/userId/<user_id>")
def get_single_users_posts(user_id):
    user_posts = [global_posts_dict[n] for n in global_posts_dict if global_posts_dict[n]['user_id'] == int(user_id)]
    return app.response_class(response=json.dumps(user_posts), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run()
