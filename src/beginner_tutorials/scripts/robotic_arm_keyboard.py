#!/usr/bin/env python3

import termios
import sys
import tty
import pygame
import socket
import time
import rospy
from std_msgs.msg import Char
from pynput import keyboard

rospy.init_node('robotic_arm_keyboard')
rospy.loginfo('Press x to exit.')
pub = rospy.Publisher('/input', Char, queue_size=10)
r = rospy.Rate(1)

isButtonPressed = False
Button = None

def on_key_press(key):
    global isButtonPressed, Button

    try:
        # Handle key press event
        print(f'Key pressed: {key.char}')
        data = None

        if(not isButtonPressed and (key.char == 'x' or key.char == 'a' or key.char == 'q' or key.char == 'd' or key.char == 'e' or key.char == 'n' or key.char == 'm' or key.char == 'z')):

            if(key.char == 'x'):
                data = 'x'
                print("Shutting down...")
                time.sleep(1)
                msg = Char(ord(data))
                pub.publish(msg)
                sys.exit()
            
            if(key.char == 'a' and Button != 'a'):
                data = 'a'
                Button = 'a'
                isButtonPressed = True
                msg = Char(ord(data))
                pub.publish(msg)
            
            elif(key.char == 'q' and Button != 'q'):
                data = 'q'
                Button = 'q'
                isButtonPressed = True
                msg = Char(ord(data))
                pub.publish(msg)

            elif(key.char == 'd'and Button != 'd'):
                data = 'd'
                Button = 'd'
                isButtonPressed = True
                msg = Char(ord(data))
                pub.publish(msg)
            
            elif(key.char == 'e'and Button != 'e'):
                data = 'e'
                Button = 'e'
                isButtonPressed = True
                msg = Char(ord(data))
                pub.publish(msg)

            elif(key.char == 'n'and Button != 'n'):
                data = 'n'
                Button = 'n'
                isButtonPressed = True
                msg = Char(ord(data))
                pub.publish(msg)

            elif(key.char == 'm'and Button != 'm'):
                data = 'm'
                Button = 'm'
                isButtonPressed = True
                msg = Char(ord(data))
                pub.publish(msg)

            elif(key.char == 'z'and Button != 'z'):
                data = 'z'
                Button = 'z'
                isButtonPressed = True
                msg = Char(ord(data))
                pub.publish(msg)
            
        elif(key.char == 'j' or key.char == 'k' or key.char == 'i' or key.char == 'o'):
            
            if(key.char == 'j'):
                data='j'
                Button = 'j'
                isButtonPressed = True
                msg = Char(ord(data))
                pub.publish(msg)
            
            elif(key.char == 'k'):
                data='k'
                Button = 'k'
                isButtonPressed = True
                msg = Char(ord(data))
                pub.publish(msg)

            elif(key.char == 'i'):
                data='i'
                Button = 'i'
                isButtonPressed = True
                msg = Char(ord(data))
                pub.publish(msg)
            
            elif(key.char == 'o'):
                data='o'
                Button = 'o'
                isButtonPressed = True
                msg = Char(ord(data))
                pub.publish(msg)

    except AttributeError:
        # Some special keys don't have a `char` attribute
        print(f'Special key pressed: {key}')


def on_key_release(key):
    global isButtonPressed, Button

    # Handle key release event
    print(f'Key released: {key}')
    if isButtonPressed:
        data = 'c'
        isButtonPressed = False
        Button = None
        print('c')
        msg = Char(ord(data))
        pub.publish(msg)

if __name__=='__main__':
    with keyboard.Listener(
            on_press=on_key_press,
            on_release=on_key_release) as listener:
        listener.join()
