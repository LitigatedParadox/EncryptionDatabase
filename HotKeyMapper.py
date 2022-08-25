import subprocess
from pynput.keyboard import *
import os
HotKey = {Key.ctrl_l, Key.alt, Key.shift}

def press_on(key):
    print('Press ON: {0}'.format(key))
    if key == Key.shift:
        subprocess.call([r'C:\Users\Shahed\CMDSTart.bat']) 

def press_off(key):
    print('Press OFF: {0}'.format(key))
    if key == Key.esc:
        return False

with Listener(on_press=press_on, on_release=press_off) as listener:
    listener.join()
