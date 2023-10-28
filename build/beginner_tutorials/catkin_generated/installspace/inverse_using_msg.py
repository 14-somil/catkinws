#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi
import pygame
import time
import rospy
from beginner_tutorials.msg import anglesMsg

x=0
y=60
z=10

def forward():
    
    global x,y,z
    y = y+1

    base, first, second=ik(x,y,z)
    msg = anglesMsg(int(first), int(second), int(base))
    pub.publish(msg)

def backward():

    global x,y,z
    y = y-1

    base, first, second=ik(x,y,z)
    msg = anglesMsg(int(first), int(second), int(base))
    pub.publish(msg)


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
                      [0.0, 34.5, 0.0*pi, 0.5*pi]])

    robot = RobotSerial(dh_params)    


    pygame.init()
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()

    # isButtonPressed = False
    # Button = None

    rospy.init_node('control')
    pub = rospy.Publisher('/angles', anglesMsg, queue_size=10)
    rospy.loginfo('Press x to exit.')

    r = rospy.Rate(1)

    if joystick_count == 0:
        print("No joysticks found.")
        pygame.quit()
    
    else:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        print("Joystick detected:", joystick.get_name())

        while not rospy.is_shutdown():

            pygame.event.pump()
            axis_1 = joystick.get_axis(1)

            exit_button = joystick.get_button(0)

            if (exit_button == 1):
                print("Shutting down")
                print('x')
                joystick.quit()
                pygame.quit()
                break
            
            elif axis_1 < -0.5 :
                print('a')
                forward()

            elif axis_1 > 0.5 :
                print('z')
                backward()

            r.sleep()

