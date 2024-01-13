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

servo = []
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
    'QRcheck':False,
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

def ik(x,y,z,a,b,c):
    global robot, target, pub, servo, isPump

    xyz=np.array([[x],[y],[z]]) 
    abc=np.array([a,b,c])

    end=Frame.from_euler_3(abc,xyz)
    ang=robot.inverse(end)
    ang=ang*180/pi

    new_base, new_first, new_second = ang
    
    target = {
        'first':new_first,
        'second':new_second,
        'base':new_base
        }
    
    msgToSend = anglesMsg(float(target['first']), float(target['second']), float(target['base']),servo[0], servo[1],servo[2],isPump)
    pub.publish(msgToSend)

def start():
    ik(X,Y,Z,A,B,C)

def orient_plane(pos):
    
    ik(pos['x'], pos['y'], 59, pos['alpha'], pos['beta'], pos['gamma']) # 59 ya jis bhi height par rakhna hai

def orient_z(pos):
    
    ik(pos['x'], pos['y'], pos['z'], pos['alpha'], pos['beta'], pos['gamma']) 

def to_qr_check(pos):
    ik(pos['x'], pos['y'], 59, pos['alpha'], pos['beta'], pos['gamma']) # pehle upar aayega

def to_drop_zone():
    global position

    if position['QRcheck'] == True:
        ik(X,Y,Z,A,B,C) #dropzone ki postion aur angle dedo
    
    else :
        ik(X,Y,Z,A,B,C) #dropzone ki postion aur angle dedo



if __name__ == '__main__':

    while 1:

        start()
        while(int(angle['first']) != int(target['first']) and int(angle['second']) != int(target['second']) and int(angle['base']) != int(target['base'])):
            continue

        update(position)
        # position mein saari values aa jaati hai suppose
        orient_plane(position)

        while(int(angle['first']) != int(target['first']) and int(angle['second']) != int(target['second']) and int(angle['base']) != int(target['base'])):
            continue

        isPump = True
        orient_z(position)

        while(int(angle['first']) != int(target['first']) and int(angle['second']) != int(target['second']) and int(angle['base']) != int(target['base'])):
            continue

        check_stick()

        to_qr_check(position)

        while(int(angle['first']) != int(target['first']) and int(angle['second']) != int(target['second']) and int(angle['base']) != int(target['base'])):
            continue

        check_qr()

        to_drop_zone()

        while(int(angle['first']) != int(target['first']) and int(angle['second']) != int(target['second']) and int(angle['base']) != int(target['base'])):
            continue
        
       
        time .sleep(1)
        msgToSend = anglesMsg(float(target['first']), float(target['second']), float(target['base']),servo[0], servo[1],servo[2],isPump)




