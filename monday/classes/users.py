import uuid


class User(dict):

    def __init__(self, name, title, instruments):
        dict.__init__(self, name=name, title=title, instruments=instruments, user_id=str(uuid.uuid4()))

