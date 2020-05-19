from mini_project.modules.randomString import random_string


class Instrument(dict):

    def __init__(self, type, model, images):
        dict.__init__(self, type=type, model=model, images=images, _id_num=random_string())

