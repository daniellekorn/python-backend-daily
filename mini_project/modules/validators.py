from mini_project.classes.mockDatabase import instruments, users


class Validators:
    def __init__(self):
        pass

    @staticmethod
    def user_exists(user_id):
        if users.get(user_id):
            return True
        return False

    @staticmethod
    def instrument_exists(instrument_id):
        if instruments.get(instrument_id):
            return True
        return False


validator = Validators()
