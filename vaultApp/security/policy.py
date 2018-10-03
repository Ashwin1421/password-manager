
class Policy:
    def __init__(self, **kwargs):
        self.__length = kwargs.get('length')
        self.__has_lowercase = kwargs.get('has_lowercase')
        self.__has_uppercase = kwargs.get('has_uppercase')
        self.__has_numbers = kwargs.get('has_numbers')
        self.__has_special_chars = kwargs.get('has_special_chars')

    def __len__(self):
        return self.__length

    def has_lowercase(self):
        return self.__has_lowercase

    def has_uppercase(self):
        return self.__has_uppercase

    def has_special_chars(self):
        return self.__has_special_chars

    def has_numbers(self):
        return self.__has_numbers
