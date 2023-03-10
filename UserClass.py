import cryptography
from cryptography import fernet as f
from cryptography.fernet import Fernet
import json
#Initialize empty dictionary
dict = {}

'''#Instantiate class
class Recipients:

    def __init__(self, name, key):
        self.name = name
        self.key = key'''

#Function to add a recipient to the database 
def AddUser(name):
    Repeat = True
    while Repeat == True:
        with open('Pairs.json', 'r') as Pairs:
        #Checks file to see whether or not it is empty. If it is empty, writes a Dummy element to the dictionary that is later deleted
            LineOne = Pairs.readline()
        if LineOne != "{\n":
            with open("Pairs.json", "w") as Ti83Plus:
                Ti83Plus.write('{"Dummy": "Null"}')
        #Takes input from user for new recipient's name, generates cryptographic key to be paired to user given recipient
        with open('Pairs.json', 'r') as Pairs:
            dict = json.load(Pairs)
            key = str(Fernet.generate_key())
            dict[name] = key
        #Deletes Dummy value from dictionary if it is found, then writes recipient key pairs to dictionary. If Dummy value is not in dictionary, simply writes given values to dictionary
        with open('Pairs.json', 'w') as storage:
            try:
                del dict["Dummy"]
                json.dump(dict, storage, indent = 4)
            except:
                json.dump(dict, storage, indent= 4)
                Repeat = False
        #Asks if user would like to add another user to the database. If yes: passes to the top of the loop. If no: breaks out of loop

#Function to remove user from the database
def RemoveUser(name):
    #Takes input from user to determine which user will be removed from the database
    with open('Pairs.json', 'r') as Pears:
        dict = json.load(Pears)
        del dict[name]
        #print("The waffle house has found its new host:", name)
    #Writes new dictionary with deleted values to json file
    with open('Pairs.json', 'w') as Pairs:
        json.dump(dict, Pairs, indent = 4)

#Function to list users in databse
def ListUsers():
    with open("Pairs.json", "r") as storage:
        storage = json.load(storage)
        print(str(storage.keys()))

def WriteMessage(Recipient, Message):
    with open("Pairs.json", 'r') as Pairs:
        Pairs = json.load(Pairs)
        print(str(Pairs.keys()))
        #Takes input from user pertaining to recipient
        key = str(Pairs[Recipient])
        #Strips b string of b and '
        key = key.strip("b")
        key = key.strip("'")
        #Encodes string into bytes to be used for Fernet key
        Finalkey = bytes(key, 'utf-8')
        EncryptionKey = Fernet(Finalkey)
        #Receives message from user to be encrypted 
        EncryptedMessage = EncryptionKey.encrypt(bytes(Message, 'utf-8'))
        #Converts EncryptedMessage to string to and strips message of b and ' before printing
        EncryptedMessage = str(EncryptedMessage)
        EncryptedMessage = EncryptedMessage.strip('b')
        EncryptedMessage = EncryptedMessage.strip("'")
        print(EncryptedMessage)
        with open("Encryption.txt", "w") as Encryption:
            Encryption.write(EncryptedMessage)

def MassWrite(Message):
    with open("Pairs.json", 'r') as Pairs:
        Pairs = json.load(Pairs)
        i = 0
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
            with open("Encryption.txt", "a") as Encryption:
                if i == 0:
                    Encryption.write("Message for " + str(Users[i]) + ": " + EncryptedMessage)
                else:
                    Encryption.write("\nMessage for " + str(Users[i]) + ": " + EncryptedMessage)
                i += 1

def DecryptMessage(EncryptedMessage, Sender):
    with open("Pairs.json", "r") as storage:
        storage = json.load(storage)
        print(str(storage.keys()))
        SenderKey = str(storage[Sender])
        SenderKey = SenderKey.strip("b")
        SenderKey = SenderKey.strip("'")
        SenderKey = bytes(SenderKey, 'utf-8')
        DecryptionKey = Fernet(SenderKey)
        DecryptedMessage = DecryptionKey.decrypt(bytes(EncryptedMessage, 'utf-8'))
        DecryptedMessage = str(DecryptedMessage)
        DecryptedMessage = DecryptedMessage.strip("b")
        DecryptedMessage = DecryptedMessage.strip("'")
        with open('Encryption.txt', 'w') as Decryption:
            Decryption.write(DecryptedMessage)