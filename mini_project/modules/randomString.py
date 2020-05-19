import random
import string


def random_string():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letters_and_digits) for n in range(8)))
