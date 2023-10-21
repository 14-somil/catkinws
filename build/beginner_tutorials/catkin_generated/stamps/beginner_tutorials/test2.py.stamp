#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
import numpy as np
import sys
from math import pi
import pygame
import time
import rospy
from beginner_tutorials.srv import angles

def ik(x,y,z):
    xyz=np.array([[x],[y],[z]])
    abc=np.array([0,0,0])

    end=Frame.from_euler_3(abc,xyz)
    ang=robot.inverse(end)
    ang=ang*180/pi
    
    return(ang)

if __name__ == "__main__":

    np.set_printoptions(precision=3, suppress=True)

    dh_params = np.array([[4.5,4.0,-0.5*pi,0.5*pi],
                      [0.0,54.55 ,0.0, -0.5*pi],                      
                      [0.0, 54.55, 0.0*pi, 0.5*pi]])

    robot = RobotSerial(dh_params) 

    rospy.wait_for_service('angles')
    request = rospy.ServiceProxy('angles', angles)

    x=int(sys.argv[1])
    y=int(sys.argv[2])
    z=int(sys.argv[3])

    base, first, second=ik(x,y,z)
    print('check')
    resp1 = request(int(first), int(second), int(base))
    print(resp1.check)