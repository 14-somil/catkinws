#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
import numpy as np
import sys
from math import pi
import pygame
import time
import rospy
from beginner_tutorials.srv import angles


if __name__ == "__main__":

    x=0
    y=58
    z=59

    np.set_printoptions(precision=3, suppress=True)

    dh_params = np.array([[4.5,4.0,-0.5*pi,0.5*pi],
                      [0.0,54.55 ,0.0, -0.5*pi],                      
                      [0.0, 54.55, 0.0*pi, 0.5*pi]])

    robot = RobotSerial(dh_params) 

    xyz=np.array([[x],[y],[z]])
    abc=np.array([0,0,0])

    end=Frame.from_euler_3(abc,xyz)
    ang=robot.inverse(end)
    ang=ang*180/pi

    print(ang)
