import random
import string
import pymongo


def menu():
    password = generatePassword(10)
    print("Náhodné heslo: " + password)
    storeToDb(password)


def generatePassword(length):

    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(password_characters) for i in range(length))

    return password


def storeToDb(password):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["Šifry"]
    collection = database["random_password"]
    data = {"nahodne_heslo": password}
    x = collection.insert_one(data)
    print("Heslo " + password + " zapsáno do databáze.")


menu()
