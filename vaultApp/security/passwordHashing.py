from hashlib import sha1, sha256, sha384, sha512
from vaultApp.policy.policyDefinition import PolicyDefinition
from vaultApp.manager.manager import PasswordGenerator
class PasswordHashing():

    def __init__(self, algorithm="sha256"):
        self.__algorithm = algorithm
        if algorithm.__eq__("sha1"):
            self.__sha  = sha1()
        elif algorithm.__eq__("sha384"):
            self.__sha = sha384()
        elif algorithm.__eq__("sha512"):
            self.__sha = sha512()
        else:
            self.__sha = sha256()

    def getHashValue(self, input):
        self.__sha.update(input.encode())
        return self.__sha.hexdigest()


if __name__ == "__main__":
    rule = PolicyDefinition()
    rule.setLength(16)
    rule.setHasLowerCase(True)
    rule.setHasUpperCase(True)
    rule.setHasNumbers(True)
    rule.setHasSpecialChars(True)
    pg = PasswordGenerator(rule)
    pg.generateRandomPassword()