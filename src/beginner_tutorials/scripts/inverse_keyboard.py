#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi 
import termios
import sys
import tty
import pygame
import socket
import time
import rospy
from beginner_tutorials.msg import anglesMsg
from pynput import keyboard

x=0
y=58
z=59
first = 0
second = 0
servo1 = 0
servo2 = 0
isPump = False
base = 's'

rospy.init_node('robotic_arm_keyboard')
rospy.loginfo('Press x to exit.')
pub = rospy.Publisher('/input', anglesMsg, queue_size=10)

isButtonPressed = False
Button = None

def forward():
    
    global x,y,z,servo1,servo2,isPump,base,first,second
    y = y+2

    _, first, second=ik(x,y,z)
    msg = anglesMsg(int(first), int(second), ord(base), servo1, servo2, isPump)
    pub.publish(msg)

def backward():

    global x,y,z,servo1,servo2,isPump,base,first,second
    y = y-2

    _, first, second=ik(x,y,z)
    msg = anglesMsg(int(first), int(second), ord(base), servo1, servo2, isPump)
    pub.publish(msg)

def up():

    global x,y,z,servo1,servo2,isPump,base,first,second
    z = z+2

    _, first, second=ik(x,y,z)
    msg = anglesMsg(int(first), int(second), ord(base), servo1, servo2, isPump)
    pub.publish(msg)

def down():

    global x,y,z,servo1,servo2,isPump,base,first,second
    z = z-2

    _, first, second=ik(x,y,z)
    msg = anglesMsg(int(first), int(second), ord(base), servo1, servo2, isPump)
    pub.publish(msg)

def left():
    global x,y,z,servo1,servo2,isPump,base,first,second

    base = 'l'

    msg = anglesMsg(int(first), int(second), ord(base), servo1, servo2, isPump)
    pub.publish(msg)

def right():
    global x,y,z,servo1,servo2,isPump,base,first,second

    base = 'r'

    msg = anglesMsg(int(first), int(second), ord(base), servo1, servo2, isPump)
    pub.publish(msg)

def stop():
    global x,y,z,servo1,servo2,isPump,base,first,second

    base = 's'

    msg = anglesMsg(int(first), int(second), ord(base), servo1, servo2, isPump)
    pub.publish(msg)

def serv_right():
    global x,y,z,servo1,servo2,isPump,base,first,second

    servo1 += 2

    msg = anglesMsg(int(first), int(second), ord(base), servo1, servo2, isPump)
    pub.publish(msg)

def serv_left():
    global x,y,z,servo1,servo2,isPump,base,first,second

    servo1 -= 2

    msg = anglesMsg(int(first), int(second), ord(base), servo1, servo2, isPump)
    pub.publish(msg)

def serv_up():
    global x,y,z,servo1,servo2,isPump,base,first,second

    servo2 += 2

    msg = anglesMsg(int(first), int(second), ord(base), servo1, servo2, isPump)
    pub.publish(msg)

def serv_down():
    global x,y,z,servo1,servo2,isPump,base,first,second

    servo2 -= 2

    msg = anglesMsg(int(first), int(second), ord(base), servo1, servo2, isPump)
    pub.publish(msg)

def pumpToggle():
    global x,y,z,servo1,servo2,isPump,base,first,second

    isPump = True if isPump == False else False

    msg = anglesMsg(int(first), int(second), ord(base), servo1, servo2, isPump)
    pub.publish(msg)

def ik(x,y,z):
    xyz=np.array([[x],[y],[z]])
    abc=np.array([0,0,0])

    end=Frame.from_euler_3(abc,xyz)
    ang=robot.inverse(end)
    ang=ang*180/pi
    
    return(ang)

def on_key_press(key):
    global isButtonPressed, Button

    try:
        # Handle key press event
        print(f'Key pressed: {key.char}')

        if(key.char == 'x'):
            print('Shutting down...')
            time.sleep(1)
            sys.exit()

        if(key.char == 'w'):
            forward()

        elif(key.char == 's'):
            backward()

        elif(key.char == 'a'):
            left()

        elif(key.char == 'd'):
            right()

        elif(key.char == 'o'):
            up()
        
        elif(key.char == 'l'):
            down()

        elif(key.char == '4'):
            serv_right()
        
        elif(key.char == '6'):
            serv_left()
        
        elif(key.char == '2'):
            serv_up()
        
        elif(key.char == '8'):
            serv_down()
        
        elif(key.char == 'z'):
            pumpToggle()

    except AttributeError:
        # Some special keys don't have a `char` attribute
        print(f'Special key pressed: {key}')

def on_key_release(key):
    # Handle key release event
    print(f'Key released: {key}')

    try:
        if(key.char == 'a' or key.char =='d'):
            stop()

    except AttributeError:
        pass

if __name__=='__main__':

    np.set_printoptions(precision=3, suppress=True)

    dh_params = np.array([[4.5,4.0,-0.5*pi,0.5*pi],
                      [0.0,54.55 ,0.0, -0.5*pi],                      
                      [0.0, 54.55, 0.0*pi, 0.5*pi]])

    robot = RobotSerial(dh_params)  
    print(ik(x,y,z))
    with keyboard.Listener(
            on_press=on_key_press,
            on_release=on_key_release) as listener:
        listener.join()
