#!/usr/bin/env python3

from cmath import sin
from symbol import factor
import cv2
# import pyrealsense2
# from realsense_depth import *
# from ultralytics import YOLO
import numpy as np
import math
import time
import rospy
from pynput import keyboard
from beginner_tutorials.msg import anglesMsg, encodersFeedback
from inverse_kinematics_grid import ik
# from servo_qr_final_accurate import QR_identify
# from Box_orientation_realsesne1 import give_coordinates_of_box
import threading

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
    global  target, x, y, z, angle

    if(angle['first'] == None):
        rospy.loginfo('Go!!!')

    angle['first'] = msg.first
    angle['second']= msg.second
    angle['base'] = msg.base

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
    
    new_base, new_first, new_second, servo[0], servo[1]= ang
    servo[2]=90
    target = {
        'first':new_first,
        'second':new_second,
        'base':new_base
        }
    
def qr_check():
    global servo
    stTime = time.time()
    servo[2] = 85 
    ret = QR_identify(stTime)
    # while True:
    #     if isQR():
    #         break
    #     if time.time()-stTime >=4:
    #         break
    
    servo[2] = 90
    return (time.time() - stTime)

def reOrient(qr_time):
    timeReq = (90*qr_time)/(90/0.9)
    servo[2]=97
    time.sleep(timeReq)
    servo[2]=90


def start():
    ik_publish(0.6,0.55,0.25, 0, 0,1)

def orient_plane(pos):
    ik_publish(float(pos['x']), float(pos['y']), 0.6, float(pos['alpha']), float(pos['beta']), float(pos['gamma']))

def orient_z(pos):
    ik_publish(float(pos['x']), float(pos['y']), float(pos['z']), float(pos['alpha']), float(pos['beta']), float(pos['gamma']))

def to_drop_zone():
    ik_publish(0.6, 0.55, 0.25, 0, 0 ,1)

def main():
    while True:
        start()
        time.sleep(5)

        # position['x'],position['y'],position['z'],position['alpha'],position['beta'],position['gamma']=give_coordinates_of_box()
        # orient_plane(position)
        # time.sleep(5)

        # isPump = True
        # orient_z(position)
        # time.sleep(6)

        # orient_plane(position)
        # time.sleep(5)
        
        # qr_time = qr_check()

        # to_drop_zone()
        # time.sleep(5)

        # isPump = False

        # reOrient(qr_time)

        # servo[2] = 97 # 85-1 97-0.9
        # time.sleep(0.9)
        # servo[2] = 90
        # time.sleep(5)

if __name__ == '__main__':
    main()