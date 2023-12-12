import socket
from pynput import keyboard
import time
import sys

HOST = '10.79.39.56'
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

isButton = False
button = None

def on_key_press(key):

    global isButton, button, client

    try:
        if(not isButton):
            if(key.char == 'x' and button != 'x'):
                print('x')
                isButton = True
                button = 'x'
                client.send(button.encode('utf-8'))
                print(client.recv(1024).decode('utf-8'))
                print("Shutting down....")
                time.sleep(1)
                sys.exit()

            if(key.char == 'w' and button != 'w'):
                print('w')
                isButton = True
                button = 'w'
                client.send(button.encode('utf-8'))
                print(client.recv(1024).decode('utf-8'))

            elif(key.char == 'a' and button != 'a'):
                print('a')
                isButton = True
                button = 'a'
                client.send(button.encode('utf-8'))
                print(client.recv(1024).decode('utf-8'))

            elif(key.char == 'd' and button != 'd'):
                print('d')
                isButton = True
                button = 'd'
                client.send(button.encode('utf-8'))
                print(client.recv(1024).decode('utf-8'))

            elif(key.char == 's' and button != 's'):
                print('s')
                isButton = True
                button = 's'
                client.send(button.encode('utf-8'))
                print(client.recv(1024).decode('utf-8'))

    except AttributeError:
    # Some special keys don't have a `char` attribute
        pass

def on_key_release(key):
    # Handle key release event
    global isButton, button, client

    try:
            
            isButton = False
            button = None
            client.send('k'.encode('utf-8'))
            print(client.recv(1024).decode('utf-8'))


    except AttributeError:
        pass


with keyboard.Listener(
        on_press=on_key_press,
        on_release=on_key_release) as listener:
    listener.join()
