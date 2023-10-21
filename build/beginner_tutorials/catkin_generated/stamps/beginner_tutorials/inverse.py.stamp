#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi
import pygame
import time
import rospy
from beginner_tutorials.srv import *

x=0
y=60
z=10
# def main():
#     np.set_printoptions(precision=3, suppress=True)

#     dh_params = np.array([[4.5,4.0,-0.5*pi,0.5*pi],
#                       [0.0,54.55 ,0.0, -0.5*pi],                      
#                       [0.0, 34.5, 0.0*pi, 0.5*pi]])

#     robot = RobotSerial(dh_params)

#     # =====================================
#     # inverse
#     # =====================================

#     xyz = np.array([[0], [66.9],[18.67]])
#     abc = np.array([0.5*pi,0.5*pi,0.5*pi])
#     end = Frame.from_euler_3(abc, xyz)
#     robot.inverse(end)

#     print("inverse is successful: {0}".format(robot.is_reachable_inverse))
#     print("axis values: \n{0}".format(robot.axis_values))

def forward():
    
    global x,y,z
    y = y+1

    base, first, second=ik(x,y,z)

    resp1 = request(int(first), int(second), int(base))
    return resp1.check

def backward():

    global x,y,z
    y = y-1

    base, first, second=ik(x,y,z)

    resp1 = request(int(first), int(second), int(base))
    return resp1.check


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


    pygame.init()
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()

    isButtonPressed = False
    Button = None

    rospy.wait_for_service('angles')
    request = rospy.ServiceProxy('angles', angles)
    rospy.loginfo('Press x to exit.')

    if joystick_count == 0:
        print("No joysticks found.")
        pygame.quit()

    else:
        # Initialize the first joystick
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        print("Joystick detected:", joystick.get_name())

        while not rospy.is_shutdown():
            pygame.event.pump()
            axis_1 = joystick.get_axis(1)

            exit_button = joystick.get_button(0)

            if(axis_1 > 0.1 or axis_1 < -0.1 or exit_button==1):
               
                if(not isButtonPressed):
                    if (exit_button == 1):
                        print("Shutting down")
                        print('x')
                        joystick.quit()
                        pygame.quit()
                        break

                    if(axis_1 < -0.5 and Button != 'a'):
                        print('a')
                        forward()
                        while 1:
                            pygame.event.pump()
                            axis_1 = joystick.get_axis(1)
                            if(axis_1 < -0.5):
                                print('a')
                                forward()
                                time.sleep(0.1)
                            else:
                                break
                    elif(axis_1 > 0.5 and Button != 'a'):
                        print('a')
                        backward()
                        while 1:
                            pygame.event.pump()
                            axis_1 = joystick.get_axis(1)
                            if(axis_1 > +0.5):
                                print('z')
                                backward()
                                time.sleep(0.1)
                            else:
                                break
            
            else:
                if(isButtonPressed == True):
                    isButtonPressed = False
                    Button = None
                    
