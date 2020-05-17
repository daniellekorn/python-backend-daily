class Comment(dict):

    def __init__(self, post_id, comment_id, name, email, body):
        dict.__init__(self, postId=post_id, id=comment_id, name=name, email=email, body=body)
