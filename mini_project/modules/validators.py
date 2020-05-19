from mini_project.classes.mockDatabase import Instruments, Users


class Validators:
    def __init__(self):
        pass

    @staticmethod
    def user_exists(user_id):
        if Users.data.get(user_id):
            return True
        return False

    @staticmethod
    def instrument_exists(instrument_id):
        if Instruments.data.get(instrument_id):
            print("true")
            return True
        return False


validator = Validators()
