import json
from .extendedPost import ExtendedPost


class JsonablePost(ExtendedPost):

    def __init__(self, post, created_at):
        super().__init__(post, created_at)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


