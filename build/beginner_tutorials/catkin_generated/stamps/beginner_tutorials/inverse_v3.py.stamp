#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi 
import time
import rospy
import sys
from pynput import keyboard
from beginner_tutorials.msg import speedMsg, encodersFeedback

x=None
y=None
z=None
angle_first=0
angle_second=0
angle_base=0
speed_first=0
speed_second=0
speed_base=0

Button = None

speed = 2

np.set_printoptions(precision=3, suppress=True)
dh_params = np.array([[4.5,4.0,-0.5*pi,0.5*pi],
                    [0.0,54.55 ,0.0, -0.5*pi],                      
                    [0.0, 54.55, 0.0*pi, 0.5*pi]])
robot = RobotSerial(dh_params)


def subCallback(data):
    global angle_first, angle_second, angle_base, x, y, z, robot
    
    angle_first = data.first
    angle_second = data.second
    angle_base = data.base

    angle_first_rad = angle_first*pi/180
    angle_second_rad = angle_second*pi/180
    angle_base_rad = angle_base*pi/180

    theta = np.array([angle_base_rad, angle_first_rad, angle_second_rad])
    f=robot.forward(theta)

    if(x is None):
        rospy.loginfo('Go!!!')

    x,y,z = f.t_3_1.reshape([3, ])


rospy.init_node('robotic_arm_control')
rospy.loginfo('Started....')
pub = rospy.Publisher('/speedFeed', speedMsg, queue_size=10)
rospy.Subscriber('/angleFeed', encodersFeedback, subCallback)
r = rospy.Rate(10)

def on_key_press(key):
    global x, y, z, angle_first, angle_second, angle_base, speed_first, speed_second, speed_base, robot, speed, Button

    try:
        if(key.char == 'x'):
            speed_first = 0
            speed_second = 0
            speed_base = 0

            Button = 'x'
            
            pub.publish(speedMsg(0,0,0))

        if(key.char == 'w'):
            Button = 'w'


    except AttributeError:
        pass

def on_key_release(key):
    global x, y, z, angle_first, angle_second, angle_base, speed_first, speed_second, speed_base, Button

    try:
        speed_base = 0
        speed_first = 0
        speed_second = 0

        Button = None

    except AttributeError:
        pass

def handleButton():
    global x, y, z, angle_first, angle_second, angle_base, speed_first, speed_second, speed_base, robot, speed, Button

    if(Button == 'w'):
        xyz=np.array([[x],[y+speed],[z]])
        abc=np.array([0,0,0])

        end=Frame.from_euler_3(abc,xyz)
        ang=robot.inverse(end)
        ang=ang*180/pi

        new_base, new_first, new_second = ang

        speed_first = new_first - angle_first
        speed_second = new_second - angle_second
        speed_base = new_base - angle_base
     
    elif(Button == None):
        speed_first = 0
        speed_second = 0
        speed_base = 0


if __name__ == '__main__':

    with keyboard.Listener(
            on_press=on_key_press,
            on_release=on_key_release) as listener:

        while Button != 'x':

            handleButton()

            msgToSend = speedMsg(float(speed_first), float(speed_second), float(speed_base))
            pub.publish(msgToSend)
            r.sleep()
        
        rospy.loginfo('Stopping...')
        time.sleep(1)
        sys.exit()

        listener.join()

