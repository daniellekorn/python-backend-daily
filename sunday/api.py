from flask import Flask, json
from sunday.classes.jsonablePost import JsonablePost
from sunday.classes.comment import Comment
from sunday.modules.randomDate import created_at
import requests


app = Flask(__name__)

global_posts_dict = {}
post_comments = []


@app.before_first_request
def get_all_posts():
    get_posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    response_data = get_posts.json()
    for post in response_data:
        current_post = JsonablePost(post, created_at())
        global_posts_dict[post['id']] = current_post.return_as_obj()
    return global_posts_dict


# this function adds the comments as an array to each post item from 1-10
@app.before_first_request
def add_comments_to_post_info():
    for n in range(1, 11):
        comments = requests.get('https://jsonplaceholder.typicode.com/posts/' + str(n) + '/comments')
        response_data = comments.json()
        post = []
        for i in response_data:
            current_comment = Comment(i['postId'], i['id'], i['name'], i['email'], i['body'])
            post.append(current_comment)
        post_comments.append(post)
        global_posts_dict.get(n).update({'comments': post})
    return global_posts_dict


if __name__ == "__main__":
    app.run()
