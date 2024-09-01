#print('This is the main file')

'''from Encription_File import *
from pynput import keyboard
#from pynput.keyboard import Listener
#from pynput.mouse import Listener

from pynput.keyboard import Listener

#Storage = open("Keyboard_Save.txt", "a")

#Fucntion with application of recording keystokes
def on_press(key):
    global InputKey
    InputKey = key
    #letterA(InputKey)
    #Storage.write(f'{InputKey}')
    print(f'{InputKey} pressed')
    printing()
    if key == keyboard.Key.esc:
        return False  
        # Stop listener



with Listener(on_press=on_press) as listener:
    listener.join()

#Storage.close() #Closing file'''

#Start from scratch

from pynput import keyboard
from pynput.keyboard import Listener

def record_click(key):
    try:
        print(key.char, end='')
    except AttributeError:
        print(f'[{key}]', end='')

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

with keyboard.Listener(on_press=record_click, on_release=on_release) as listener:
    listener.join()