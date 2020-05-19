from mini_project.modules.randomString import random_string


class User(dict):

    def __init__(self, username, email, password, instruments):
        dict.__init__(self, username=username, email=email, password=password, instruments=instruments,
                      _id_num=random_string())
