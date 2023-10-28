#!/usr/bin/env python3

import rospy
from beginner_tutorials.msg import anglesMsg
from visual_kinematics.RobotSerial import *
import numpy as np
import sys
from math import pi

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

    rospy.init_node('Visual_kinematics')
    pub = rospy.Publisher('/angles', anglesMsg, queue_size=10)

    x=int(input('Enter x '))
    y=int(input('Enter y '))
    z=int(input('Enter z '))

    base, first, second=ik(x,y,z)

    msg = anglesMsg(int(first), int(second), int(base))
