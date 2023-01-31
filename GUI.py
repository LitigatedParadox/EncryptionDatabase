import tkinter as tk
from tkinter import *
from UserClass import AddUser, RemoveUser, ListUsers, WriteMessage, MassWrite, DecryptMessage
#Initialize first screen in which user confirms their intentions
SelectionScreen = tk.Tk()
SelectionScreen.geometry("1500x1000")
SelectionScreen.configure(background="gray")

#Functions
def AddScreen():
    global SelectionScreen
    SelectionScreen.destroy()
    AddScreen = tk.Tk()
    AddScreen.geometry("1500x1000")
    AddScreen.configure(background="gray")
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
    with open("Pairs.json", 'r') as Users:
        UserLabel = tk.Label(text=Users.read(), bg='gray', fg='white')
        UserLabel.place(x=100, y=100)

def WriteScreen():
    global SelectionScreen
    SelectionScreen.destroy()
    WriteScreen = tk.Tk()
    WriteScreen.geometry("1500x1000")
    WriteScreen.configure(background="gray")
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
        EncryptionLabel = tk.Label(WriteScreen, text = "Your encrypted message here: ", bg = 'gray', fg="white")
        EncryptionLabel.place(x=650, y=500)
        
    EncryptionButton = tk.Button(WriteScreen, height=5, width=15, bg="gray", text="Enter", fg="white", command=GetInfo)
    EncryptionButton.place(x=750, y=600)

#Fill initial screen with buttons tied to functions
AddButton = tk.Button(SelectionScreen, height=5, width=15, bg="gray", text="Add User", fg="white", command=AddScreen)
AddButton.place(x=0, y=400)

RemoveButton = tk.Button(SelectionScreen, height=5, width=15, bg="gray", text="Remove Users", fg="white", command=RemoveUsers)
RemoveButton.place(x=200, y=400)

ListButton = tk.Button(SelectionScreen, height=5, width=15, bg="gray", text="List Users", fg="white", command=ListScreen)
ListButton.place(x=400, y=400)

WriteButton = tk.Button(SelectionScreen, height=5, width=15, bg="gray", text="Write Message", fg="white", command=WriteScreen)
WriteButton.place(x=600, y=400)


SelectionScreen.mainloop()