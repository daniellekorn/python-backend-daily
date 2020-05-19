from monday.modules.randomString import random_string


class Instrument(dict):

    def __init__(self, type, model):
        dict.__init__(self, type=type, model=model, id_num=random_string())

