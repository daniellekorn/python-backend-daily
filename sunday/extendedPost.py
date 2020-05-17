from .basePost import BasePost


class ExtendedPost(BasePost):

    def __init__(self, user_id, post_id, title, body, created_at):
        super().__init__(user_id, post_id, title, body)
        self.created_at = created_at

