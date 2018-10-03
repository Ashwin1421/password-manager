from security.manager import PasswordGenerator
from security.policy import Policy
from security.hashing import PasswordHashing

if __name__ == '__main__':
    policy = Policy(
        length=16,
        has_lowercase=True,
        has_uppercase=True,
        has_numbers=True,
        has_special_chars=True
    )
    manager = PasswordGenerator(policy)
    password = manager.get_random_password()
    print(password)
    password_hashing = PasswordHashing(algorithm="sha512")
    hash = password_hashing.get_hash_value(password)
    print(hash)