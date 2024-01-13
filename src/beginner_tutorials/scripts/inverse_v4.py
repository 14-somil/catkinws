#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi 
import time
import rospy
import sys
from pynput import keyboard
from beginner_tutorials.msg import anglesMsg, encodersFeedback

x=None
y=None
z=None
angle = {
    'first':None,
    'second':None,
    'base':None
    }
target = {
    'first':0,
    'second':0,
    'base':0
    }

Button = None

speed = 5

np.set_printoptions(precision=3, suppress=True)
dh_params = np.array([[4.5,4.0,-0.5*pi,0.5*pi],
                    [0.0,54.55 ,0.0, -0.5*pi],                      
                    [0.0, 54.55, 0.0*pi, 0.5*pi]])
robot = RobotSerial(dh_params)

def subCallback(msg):
    global robot, target, x, y, z, angle, speed, Button

    if(angle['first'] == None):
        rospy.loginfo('Go!!!')

    angle['first'] = msg.first
    angle['second']= msg.second
    angle['base'] = msg.base

rospy.init_node('robotic_arm_control')
rospy.loginfo('Started....')
pub = rospy.Publisher('/input', anglesMsg, queue_size=10)
rospy.Subscriber('/angleFeedback', encodersFeedback, subCallback)
r = rospy.Rate(10)

def on_key_press(key):
    global robot, target, x, y, z, angle, speed, Button

    try:
        if(key.char == 'x'):
            Button = 'x'
            
        if(key.char == 'w'):
            Button = 'w'
        elif(key.char == 's'):
            Button = 's'
        elif(key.char == '8'):
            Button = '8'
        elif(key.char == '2'):
            Button = '2'


    except AttributeError:
        pass

def on_key_release(key):
    global robot, target, x, y, z, angle, speed, Button

    try:
        Button = None

    except AttributeError:
        pass

def handleButton():
    global robot, target, x, y, z, angle, speed, Button

    angle_rad={
        'first':angle['first'] *pi/180,
        'second':angle['second'] *pi/180,
        'base':angle['base'] *pi/180
    }

    theta = np.array([angle_rad['base'], angle_rad['first'], angle_rad['second']])
    f= robot.forward(theta)

    x,y,z = f.t_3_1.reshape([3, ])

    if(Button == 'w'):
        xyz=np.array([[x],[y+speed],[z]])
        abc=np.array([0,0,0])

        end=Frame.from_euler_3(abc,xyz)
        ang=robot.inverse(end)
        ang=ang*180/pi

        new_base, new_first, new_second = ang
        
        target = {
            'first':new_first,
            'second':new_second,
            'base':new_base
        }
    elif(Button == 's'):
        xyz=np.array([[x],[y-speed],[z]])
        abc=np.array([0,0,0])

        end=Frame.from_euler_3(abc,xyz)
        ang=robot.inverse(end)
        ang=ang*180/pi

        new_base, new_first, new_second = ang
        
        target = {
            'first':new_first,
            'second':new_second,
            'base':new_base
        }
    elif(Button == '8'):
        xyz=np.array([[x],[y],[z+speed]])
        abc=np.array([0,0,0])

        end=Frame.from_euler_3(abc,xyz)
        ang=robot.inverse(end)
        ang=ang*180/pi

        new_base, new_first, new_second = ang
        
        target = {
            'first':new_first,
            'second':new_second,
            'base':new_base
        }
    elif(Button == '2'):
        xyz=np.array([[x],[y],[z-speed]])
        abc=np.array([0,0,0])

        end=Frame.from_euler_3(abc,xyz)
        ang=robot.inverse(end)
        ang=ang*180/pi

        new_base, new_first, new_second = ang
        
        target = {
            'first':new_first,
            'second':new_second,
            'base':new_base
        }
    else:
        target = angle

if __name__ == '__main__':

    with keyboard.Listener(
            on_press=on_key_press,
            on_release=on_key_release) as listener:
        
        while(angle['first'] == None):
            continue

        while Button != 'x':

            handleButton()

            msgToSend = anglesMsg(float(target['first']), float(target['second']), ord('s'), 0,0,False)
            pub.publish(msgToSend)
            r.sleep()
        
        rospy.loginfo('Stopping...')
        time.sleep(1)
        sys.exit()

        listener.join()

