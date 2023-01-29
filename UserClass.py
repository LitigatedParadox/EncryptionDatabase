import cryptography
from cryptography import fernet as f
from cryptography.fernet import Fernet
import json
import base64
textfile = open('new.txt', 'a')
dict = {}

class Recipients:

    def __init__(self, name, key):
        self.name = name
        self.key = key

def AddUser():
    Repeat = True
    while Repeat == True:
        with open('Pairs.json', 'r') as Pairs:
            LineOne = Pairs.readline()
        if LineOne != "{\n":
            with open("Pairs.json", "w") as Ti83Plus:
                Ti83Plus.write('{"Dummy": "Null"}')
        with open('Pairs.json', 'r') as Pairs:
            dict = json.load(Pairs)
            name = input("Enter the name by which this user will be called: ")
            key = str(Fernet.generate_key())
            dict[name] = key
        with open('Pairs.json', 'w') as storage:
            try:
                del dict["Dummy"]
                json.dump(dict, storage, indent = 4)
            except:
                json.dump(dict, storage, indent= 4)
        Terminate = input("Would you like to add another user to the database? (Y/N): ")
        if Terminate == 'N':
            with open('Pairs.json', 'w') as storage:
                json.dump(dict, storage, indent=4)
                storage.close()
                break
        elif Terminate == "Y":
            pass

def RemoveUser():
    with open('Pairs.json', 'r') as Pears:
        dict = json.load(Pears)
        print(dict.keys())
        name = input("Please enter the name of the user you would like to remove from the database? ")
        del dict[name]
        #print("The waffle house has found its new host:", name)
    with open('Pairs.json', 'w') as Pairs:
        json.dump(dict, Pairs, indent = 4)
        
def ListUsers():
    with open("Pairs.json", "r") as storage:
        storage = json.load(storage)
        print(storage.keys())

def WriteMessage():
    with open("Pairs.json", 'r') as Pairs:
        Pairs = json.load(Pairs)
        print(Pairs.keys())
        Recipient = input("To whom would you like to send your message? ")
        key = str(Pairs[Recipient])
        key = key.strip("b")
        key = key.strip("'")
        Finalkey = bytes(key, 'utf-8')
        EncryptionKey = Fernet(Finalkey)
        Message = input("Please enter the message you would like to encrypt here: ")
        EncryptedMessage = EncryptionKey.encrypt(bytes(Message, 'utf-8'))
        EncryptedMessage = str(EncryptedMessage)
        EncryptedMessage = EncryptedMessage.strip('b')
        EncryptedMessage = EncryptedMessage.strip("'")
        print(EncryptedMessage)

def MassWrite():
    with open("Pairs.json", 'r') as Pairs:
        Pairs = json.load(Pairs)
        i = 0
        Message = input("Please enter the message you would like to send to every recipient in your database: ")
        for Pair in Pairs:
            User_Key = Pairs[Pair]
            User_Key = User_Key.strip("b")
            User_Key = User_Key.strip("'")
            Finalkey = bytes(User_Key, 'utf-8')
            Encryptionkey = Fernet(Finalkey)
            EncryptedMessage = Encryptionkey.encrypt(bytes(Message, 'utf-8'))
            EncryptedMessage = str(EncryptedMessage)
            EncryptedMessage = EncryptedMessage.strip('b')
            EncryptedMessage = EncryptedMessage.strip("'")
            Users = list(Pairs.keys())
            print("Message for", Users[i], ": ", EncryptedMessage)
            i += 1

def DecryptMessage():
    with open("Pairs.json", "r") as storage:
        storage = json.load(storage)
        EncryptedMessage = input("Please enter the encrypted message you receieved here: ")
        print(storage.keys())
        Sender = input("From whom did you receive this message? ")
        SenderKey = str(storage[Sender])
        SenderKey = SenderKey.strip("b")
        SenderKey = SenderKey.strip("'")
        SenderKey = bytes(SenderKey, 'utf-8')
        DecryptionKey = Fernet(SenderKey)
        DecryptedMessage = DecryptionKey.decrypt(bytes(EncryptedMessage, 'utf-8'))
        DecryptedMessage = str(DecryptedMessage)
        DecryptedMessage = DecryptedMessage.strip("b")
        DecryptedMessage = DecryptedMessage.strip("'")
        print(DecryptedMessage)
        

while True:
    InitialAction = input("What would you like to do? \n 1. Add User \n 2. Remove User \n 3. List Users \n 4. Encrypt Message (One Recipient) \n 5. Encrypt Message (All Recipients) \n 6. Decrypt Message \n")
    def Continuation(InitialAction):
        if InitialAction == "1":
            AddUser()
        elif InitialAction == "2":
            RemoveUser()
        elif InitialAction == "3":
            ListUsers()
        elif InitialAction == "4":
            WriteMessage()
        elif InitialAction == "5":
            MassWrite()
        elif InitialAction == "6":
            DecryptMessage()
        Continue = input("Would you like to do anything else? (Y/N) ")
        if Continue == "Y":
            pass
        if Continue == "N":
            exit()
    Continuation(InitialAction)