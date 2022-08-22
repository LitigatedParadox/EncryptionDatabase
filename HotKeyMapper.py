from re import L
from pynput.keyboard import Key, Listener

LocationList = []
ApplicationList = []
HotkeyList = []

AddRemoveHotkey = input("Add or remove a hotkey? (a/r): ")

if AddRemoveHotkey == "Add" or "a" or "add":
    Location = input("Enter an application location (note that you must add the directory the application lies within, not the application itself): ")
    LocationList.append(Location)