import uuid


class Instrument(dict):

    def __init__(self, name, model, type):
        dict.__init__(self, name=name, id_num=str(uuid.uuid4()))

