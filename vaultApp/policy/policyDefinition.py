
class PolicyDefinition:
    def __init__(self):
        self.__length = 8
        self.__hasLowerCase = None
        self.__hasUpperCase = None
        self.__hasNumbers = None
        self.__hasSpecialChars = None

    def setLength(self, length):
        self.__length = length

    def getLength(self):
        return self.__length

    def setHasLowerCase(self, lowerCase):
        self.__hasLowerCase = lowerCase

    def isLowerCase(self):
        return self.__hasLowerCase

    def setHasUpperCase(self, upperCase):
        self.__hasUpperCase = upperCase

    def isUpperCase(self):
        return self.__hasUpperCase

    def setHasNumbers(self, numbers):
        self.__hasNumbers = numbers

    def hasNumbers(self):
        return self.__hasNumbers

    def setHasSpecialChars(self, specialChars):
        self.__hasLowerCase = specialChars

    def hasSpecialChars(self):
        return self.__hasSpecialChars