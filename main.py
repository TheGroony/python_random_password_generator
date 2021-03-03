import random
import string


def menu():
    password = generatePassword(10)
    print("Náhodné heslo: " + password)


def generatePassword(length):

    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(password_characters) for i in range(length))

    return password


menu()
