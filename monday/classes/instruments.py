from monday.modules.randomString import random_string


class Instrument(dict):

    def __init__(self, name, model, type):
        dict.__init__(self, name=name, model=model, type=type, id_num=random_string())

