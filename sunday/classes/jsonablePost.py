import json
from .extendedPost import ExtendedPost


class JsonablePost(ExtendedPost):

    def __init__(self, user_id, post_id, title, body, created_at):
        super().__init__(user_id, post_id, title, body, created_at)

    def __repr__(self):
        return self.body

    def to_json(self):
        return json.dumps(self.__dict__)
