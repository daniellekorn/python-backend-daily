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
    def get_user_id_by_name(user_name):
        for user in Users.data:
            if Users.data[user]['username'] == user_name:
                return Users.data[user]['id_num']
        return False

    @staticmethod
    def instrument_exists(instrument_id):
        if Instruments.data.get(instrument_id):
            print("true")
            return True
        return False


validator = Validators()
