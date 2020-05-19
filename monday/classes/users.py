from monday.modules.randomString import random_string


class User(dict):

    def __init__(self, username, email, password, instruments):
        dict.__init__(self, username=username, email=email, password=password, instruments=instruments,
                      user_id=random_string())
