import json
from .extendedPost import ExtendedPost


class JsonablePost(ExtendedPost):

    def __init__(self, post, created_at):
        super().__init__(post, created_at)

    def return_as_obj(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__)


