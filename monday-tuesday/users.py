class User:

    def __init__(self, user_id, name, role, instruments):
        self.user_id = user_id # uuid str
        self.name = name # str
        self. role = role # str: musician, manager, etc.
        self.instruments = instruments # array
