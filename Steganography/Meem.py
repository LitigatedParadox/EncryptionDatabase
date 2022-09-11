#Import modules and initialize variables
import subprocess
from pynput.keyboard import *
import time
keyboard = Controller()

def Type(key):
    keyboard.press(key)
    keyboard.release(key)
    time.sleep(5)

#Filling the class with objects
Key1 = Key.enter

#Putting objects to use by iterating through a list they were previously appended to and then typing the key specified in the object
subprocess.call([r'C:\Users\Shahed\CMDSTart.bat'])
time.sleep(5)

