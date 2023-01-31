import tkinter as tk
from tkinter import *
from UserClass import AddUser, RemoveUser, WriteMessage, MassWrite, DecryptMessage
#Initialize first screen in which user confirms their intentions
SelectionScreen = tk.Tk()
SelectionScreen.geometry("1500x1000")
SelectionScreen.configure(background="gray")

#Functions
def BackButton(root):
    global SelectionScreen
    root.destroy()
    SelectionScreen = tk.Tk()
    SelectionScreen.geometry("1500x1000")
    SelectionScreen.configure(background="gray")
    AddButton = tk.Button(SelectionScreen, height=5, width=25, bg="gray", text="Add User", fg="white", command=AddScreen)
    AddButton.place(x=0, y=400)

    RemoveButton = tk.Button(SelectionScreen, height=5, width=25, bg="gray", text="Remove Users", fg="white", command=RemoveUsers)
    RemoveButton.place(x=200, y=400)

    ListButton = tk.Button(SelectionScreen, height=5, width=25, bg="gray", text="List Users", fg="white", command=ListScreen)
    ListButton.place(x=400, y=400)

    EncryptButton = tk.Button(SelectionScreen, height=5, width=25, bg="gray", text="Encrypt Message (One User)", fg="white", command=WriteScreen)
    EncryptButton.place(x=600, y=400)

    DecryptButton = tk.Button(SelectionScreen, height=5, width=25, bg="gray", text = "Decrypt Message", fg="white", command=OriginalMessage)
    DecryptButton.place(x=800, y=400)

    MassEncryptButton = tk.Button(SelectionScreen, height=5, width=25, bg="gray", text = "Encrypt Message (All Users)", fg="white", command=MassEncrypt)
    MassEncryptButton.place(x=1000, y=400)
    SelectionScreen.mainloop()

def AddBack(root):
    BackRoot = root
    Button = tk.Button(root, height=5, width=15, bg="gray", text="Back", fg="white", command = lambda:BackButton(BackRoot))
    Button.place(x=200, y=800)

    
def AddScreen():
    global SelectionScreen
    SelectionScreen.destroy()
    AddScreen = tk.Tk()
    AddScreen.geometry("1500x1000")
    AddScreen.configure(background="gray")
    AddBack(AddScreen)
    #Buttons
    RecipientField = tk.Entry(AddScreen, bg="white", fg='black', width=20)
    RecipientField.place(x=750, y=300)
    def GetName():
        Name = RecipientField.get()
        AddUser(Name)
        RecipientField.delete(0, END)
        CompletionMessage = tk.Label(text = 'Recipient added to database!', bg='gray', fg="white")
        CompletionMessage.place(x=750, y=350)
    AddData = tk.Button(AddScreen, height=5, width=15, bg="gray", text="Enter", fg="white", command=GetName)
    AddData.place(x=750, y=400)

def RemoveUsers():
    global SelectionScreen
    SelectionScreen.destroy()
    RemoveScreen = tk.Tk()
    RemoveScreen.geometry("1500x1500")
    RemoveScreen.configure(background="gray")
    AddBack(RemoveScreen)
    #Buttons
    RemovalField = tk.Entry(RemoveScreen, bg="white", fg='black', width=20)
    RemovalField.place(x=750, y=300)
    def GetRemoval():
        Name = RemovalField.get()
        RemoveUser(Name)
        RemovalField.delete(0, END)
        RemovalMessage = tk.Label(text = "Recipient removed from databse!", bg='gray', fg='white')
        RemovalMessage.place(x=750, y=350)
    RemoveData = tk.Button(RemoveScreen, height=5, width=15, bg='gray', text="Enter", fg="white", command=GetRemoval)
    RemoveData.place(x=750, y=400)
        

def ListScreen():
    global SelectionScreen
    SelectionScreen.destroy()
    ListScreen = tk.Tk()
    ListScreen.geometry("1500x1000")
    ListScreen.configure(background="gray")
    AddBack(ListScreen)
    with open("Pairs.json", 'r') as Users:
        UserLabel = tk.Label(text=Users.read(), bg='gray', fg='white')
        UserLabel.place(x=100, y=100)

def WriteScreen():
    global SelectionScreen
    SelectionScreen.destroy()
    WriteScreen = tk.Tk()
    WriteScreen.geometry("1500x1000")
    WriteScreen.configure(background="gray")
    AddBack(WriteScreen)
    #Buttons
    RecipientField = tk.Entry(WriteScreen, bg="white", fg="black", width=20)
    RecipientField.place(x=950, y=300)
    RecipientLabel = tk.Label(WriteScreen, text="To whom would you like to send your message?", bg='gray', fg='white')
    RecipientLabel.place(x=650, y=300)
    MessageField = tk.Entry(WriteScreen, bg="white", fg="black", width=20)
    MessageField.place(x=950, y=400)
    MessageLabel = tk.Label(WriteScreen, text = "Enter your message here: ", bg="gray", fg="white")
    MessageLabel.place(x=650, y=400)
    def GetInfo():
        Recipient = RecipientField.get()
        Message = MessageField.get()
        WriteMessage(Recipient, Message)
        RecipientField.delete(0, END)
        MessageField.delete(0, END)
        with open("Encryption.txt", "r") as Encryption:
            EncryptedField = Text(WriteScreen, height=5, width=25)
            text = Encryption.read()
            EncryptedField.insert(tk.END, text)
            EncryptedField.place(x=950, y=500)
            with open("Encryption.txt", "r+") as Encryption:
                Encryption.truncate(0)
        EncryptionLabel = tk.Label(WriteScreen, text = "Your encrypted message here: ", bg = 'gray', fg="white")
        EncryptionLabel.place(x=650, y=500)
    EncryptionButton = tk.Button(WriteScreen, height=5, width=15, bg="gray", text="Enter", fg="white", command=GetInfo)
    EncryptionButton.place(x=750, y=600)

def OriginalMessage():
    #Create Window
    global SelectionScreen
    SelectionScreen.destroy()
    DecryptScreen = tk.Tk()
    DecryptScreen.geometry("1500x1000")
    DecryptScreen.configure(background="gray")
    AddBack(DecryptScreen)
    #Entry fields
    MessageField = tk.Entry(DecryptScreen, bg="white", fg='black', width=20)
    MessageField.place(x=950, y=300)
    MessageLabel = tk.Label(DecryptScreen, text="Enter the message you received here: ", bg='gray', fg='white')
    MessageLabel.place(x=650, y=300)
    SenderField = tk.Entry(DecryptScreen, bg='white', fg='black', width=20)
    SenderField.place(x=950, y=400)
    SenderLabel = tk.Label(DecryptScreen, text="From whom did you receive this message?", bg='gray', fg='white')
    SenderLabel.place(x=650, y=400)
    def GetInfo():
        Sender = SenderField.get()
        Message = MessageField.get()
        DecryptMessage(Message, Sender)
        MessageField.delete(0, END)
        MessageField.delete(0, END)
        with open('Encryption.txt', 'r') as Decryption:
            DecryptedField = Text(DecryptScreen, height=5, width=25)
            text = Decryption.read()
            DecryptedField.insert(tk.END, text)
            DecryptedField.place(x=950, y=500)
            with open("Encryption.txt", "r+") as DecryptionTextFile:
                DecryptionTextFile.truncate(0)
        DecryptionLabel = tk.Label(DecryptScreen, text = "Decrypted message here: ", bg='gray', fg='white')
        DecryptionLabel.place(x=650, y=500)

    #Enter Button
    DecryptionButton = tk.Button(DecryptScreen, height=5, width=15, bg="gray", text="Enter", fg="white", command=GetInfo)
    DecryptionButton.place(x=650, y=500)
            
def MassEncrypt():
    global SelectionScreen
    SelectionScreen.destroy()
    AllScreen = tk.Tk()
    AllScreen.geometry("1500x1000")
    AllScreen.configure(background="gray")
    AddBack(AllScreen)
    #Entry fields
    EncryptionField = tk.Entry(AllScreen, bg="white", fg="black", width=20)
    EncryptionField.place(x=950, y=300)
    EncryptionLabel = tk.Label(AllScreen, text="Enter the message you would like to encrypt here: ", bg="gray", fg="white")
    EncryptionLabel.place(x=650, y=300)
    def MassEncrypt():
        Message = EncryptionField.get()
        MassWrite(Message)
        EncryptionField.delete(0, END)
        with open("Encryption.txt", "r") as Encryption:
            EncryptedList = Text(AllScreen, height=25, width=50)
            text = Encryption.read()
            EncryptedList.insert(tk.END, text)
            EncryptedList.place(x=950, y=500)
            with open('Encryption.txt', "r+") as TextFile:
                TextFile.truncate(0)
        ListLabel = tk.Label(AllScreen, text = "Encrypted messages here: ", bg='gray', fg='white')
        ListLabel.place(x=650, y=500)
    
    #Enter Button
    MassEncryptButton = tk.Button(AllScreen, height=5, width = 25, bg="gray", text = "Enter", fg="white", command=MassEncrypt)
    MassEncryptButton.place(x=650, y=500)
#Fill initial screen with buttons tied to functions
AddButton = tk.Button(SelectionScreen, height=5, width=25, bg="gray", text="Add User", fg="white", command=AddScreen)
AddButton.place(x=0, y=400)

RemoveButton = tk.Button(SelectionScreen, height=5, width=25, bg="gray", text="Remove Users", fg="white", command=RemoveUsers)
RemoveButton.place(x=200, y=400)

ListButton = tk.Button(SelectionScreen, height=5, width=25, bg="gray", text="List Users", fg="white", command=ListScreen)
ListButton.place(x=400, y=400)

EncryptButton = tk.Button(SelectionScreen, height=5, width=25, bg="gray", text="Encrypt Message (One User)", fg="white", command=WriteScreen)
EncryptButton.place(x=600, y=400)

DecryptButton = tk.Button(SelectionScreen, height=5, width=25, bg="gray", text = "Decrypt Message", fg="white", command=OriginalMessage)
DecryptButton.place(x=800, y=400)

MassEncryptButton = tk.Button(SelectionScreen, height=5, width=25, bg="gray", text = "Encrypt Message (All Users)", fg="white", command=MassEncrypt)
MassEncryptButton.place(x=1000, y=400)
SelectionScreen.mainloop()