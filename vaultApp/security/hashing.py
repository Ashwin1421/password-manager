from hashlib import sha1, sha256, sha384, sha512
from bcrypt import hashpw, gensalt
from base64 import b64encode
from os import urandom


class PasswordHashing:

    def __init__(self, algorithm="sha256"):
        self.__algorithm = algorithm
        if algorithm == "sha1":
            self.__sha = sha1
        elif algorithm == "sha384":
            self.__sha = sha384
        elif algorithm == "sha512":
            self.__sha = sha512
        else:
            self.__sha = sha256

    def get_hash_value(self, password):
        hashed = hashpw(
            b64encode(self.__sha(password.encode() + urandom(len(password))).digest()),
            gensalt(16)
        )
        return hashed.decode()
