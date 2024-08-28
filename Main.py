print('This is the main file')

from pynput import keyboard
#from pynput.keyboard import Listener
#from pynput.mouse import Listener

'''def keyboard_clicks(key):
    print(f"{key} pressed")

keyboard_clicks'''
from pynput.keyboard import Listener

def on_press(key):
    print(f'{key} pressed')

def on_release(key):
    print(f'{key} released')
    if key == keyboard.Key.esc:
        return False  # Stop listener

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
