#Import Statements
import cryptography
from cryptography import fernet as f
import json

#Text files
storage = open("1.txt", "a+")

#Variables/Arrays
Accounts = {}

def Assign_Account(User, Key):
    global Accounts
    Accounts[User]=Key

#Inputs
def AddPair():
    Repeat = True
    while Repeat == True:
        Add = input("Please enter the name by which the recipient will be called: ")
        Key = f.Fernet.generate_key()
        Assign_Account(Add, Key)
        print(Accounts)
        Continue = input("Continue (Y/N): ")
        if Continue == "Y":
            pass
        else:
            storage.write(json.dumps(str(Accounts)))
            Repeat = False

def RemovePair():
    Repeat = True
    while Repeat == True:
        for Account in storage:
            print(Account)
        Recipient = input("Please choose the recipient you would like to remove from the database: ")
        Accounts.pop(Recipient)
        Continue = input("Would you like to remove another recipient from the database (Y/N): ")
        if Continue == "Y":
            pass
        else:
            Repeat = False

def ViewPairs():
    print(str(storage))

Init = input("1. Add Recipient" + "\n" + "2. Remove Recipient" + "\n" + "3. View Database" + "\n")
if Init == "1":
    AddPair()
if Init == "2":
    RemovePair()
else:
    ViewPairs()