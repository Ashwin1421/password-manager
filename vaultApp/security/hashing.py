from hashlib import sha1, sha256, sha384, sha512
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

    def get_hash_value(self, input):
        self.__sha.update(input.encode())
        return self.__sha.hexdigest()