from monday.modules.randomString import random_string


class User(dict):

    def __init__(self, name, title, instruments):
        dict.__init__(self, name=name, title=title, instruments=instruments, user_id=random_string())

