from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from secrets import SystemRandom

class PasswordGenerator:

    def __init__(self, policy):
        self.__policy = policy


    def get_random_password(self):
        length = len(self.__policy)
        value = ""
        if self.__policy.has_lowercase():
            value += ascii_lowercase
        if self.__policy.has_uppercase():
            value += ascii_uppercase
        if self.__policy.has_numbers():
            value += digits
        if self.__policy.has_special_chars():
            value += punctuation

        return "".join(SystemRandom().choice(value) for _ in range(length))