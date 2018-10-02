from vaultApp.policy.policyDefinition import PolicyDefinition
from string import ascii_lowercase, ascii_uppercase, punctuation, digits
class PasswordGenerator(PolicyDefinition):

    def __init__(self, policy):
        self.__policy = policy


    def generateRandomPassword(self):
        length = self.__policy.getLength()
        value = ascii_lowercase+ascii_uppercase+digits+punctuation
