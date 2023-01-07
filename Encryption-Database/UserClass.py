import cryptography
from cryptography import fernet as f
storage = open("Pairs.csv", "r")

class Recipients:

    def __init__(self, name, key):
        self.name = name
        self.key = key

def AddUser():
    Repeat = True
    while Repeat == True:
        name = input("Enter the name by which this user will be called: ")
        key = f.Fernet.generate_key()
        User = Recipients(name, key)
        dict = {User.name: User.key}
        storage.write(str(dict) + "\n")
        Continue = input("Would you like to add another recipient to the database? (Y/N)")
        if Continue == "Y":
            pass
        else:
            Repeat = False

def RemoveUser():
    global storage
    i = 1
    Database = storage.readlines()
    for line in Database:
        print(i, ".) ", line)
        i+=1

RemoveUser()