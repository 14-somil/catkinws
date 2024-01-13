#!/usr/bin/env python3

from cmath import sin
from symbol import factor
import cv2
import numpy as np
import math
import time
import rospy
from pynput import keyboard
from beginner_tutorials.msg import anglesMsg, encodersFeedback
from inverse_kinematics_grid import ik
import threading
from random import randint

x=None
y=None
z=None

servo = [0,0,90]
isPump = False

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

position = {
    'x':None,
    'y':None,
    'z':None,
    'alpha':None,
    'beta':None,
    'gamma':None,
    # 'QRcheck':False,
}

def subCallback(msg):
    global  target, x, y, z, angle, servo

    if(angle['first'] == None):
        rospy.loginfo('Go!!!')

    angle['first'] = msg.first
    angle['second']= msg.second
    angle['base'] = msg.base

    # servo[1] = angle['first']+angle['second']

def publisher():
    global target, servo, isPump, pub

    r = rospy.Rate(100)
    while True:
        msgToSend = anglesMsg(float(target['first']), float(target['second']), float(target['base']),int(servo[0]+90), int(servo[1]+60),int(servo[2]),isPump)
        pub.publish(msgToSend)
        r.sleep()

rospy.init_node('robotic_arm_control')
rospy.loginfo('Started....')
pub = rospy.Publisher('/input', anglesMsg, queue_size=10)
rospy.Subscriber('/angleFeedback', encodersFeedback, subCallback)
publisher_thread = threading.Thread(target=publisher)
publisher_thread.start()

def ik_publish(p,q,r,a,b,c):
    global target, pub, servo, isPump
    ang=ik(p,q,r,a,b,c)

    # rospy.loginfo(ang)
    
    new_base, new_first, new_second, servo[0],servo[2]= ang
    # servo[2]=90
    target = {
            'first':new_first,
            'second':new_second,
            'base':new_base
        }

def ik_publish1(p,q,r,a,b,c):
    global target, pub, servo, isPump
    ang=ik(p,q,r,a,b,c)

    # rospy.loginfo(ang)
    
    new_base, new_first, new_second, _, _= ang
    # servo[2]=90
    target = {
            'first':new_first,
            'second':new_second,
            'base':new_base
        }

def start():
    global target, servo, isPump
    target = {
        'first':10,
        'second':20,
        'base':30
    }

def aboveBox(pos):
    ik_publish(pos[0], pos[1], 0.5, 0, 0, 1)

def aboveBox1(pos):
    ik_publish1(pos[0], pos[1], 0.5, 0, 0, 1)

def toBox(pos):
    ik_publish(pos[0], pos[1], 0.23, 0, 0, 1)


def main():
    global isPump

    while angle['first'] is None:
        continue

    start()
    time.sleep(10)

    isPump = False

    pos = [0.8, -0.3]
    aboveBox(pos)
    time.sleep(5)

    isPump = True

    toBox(pos)
    time.sleep(5)

    aboveBox1(pos)
    time.sleep(5)

    while True:
        
        start()
        time.sleep(10)

        isPump = False

        pos = [randint(50,90)/100, randint(-40, 20)/100]
        aboveBox(pos)
        time.sleep(5)

        isPump = True

        toBox(pos)
        time.sleep(5)

        aboveBox(pos)
        time.sleep(5)

if __name__ == '__main__':
    main()
