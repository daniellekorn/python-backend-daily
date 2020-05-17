from .basePost import BasePost


class ExtendedPost(BasePost):

    def __init__(self, post, created_at):
        super().__init__(post)
        self.created_at = created_at

