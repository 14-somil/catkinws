#!/usr/bin/env python3

import termios
import sys
import tty
import pygame
import socket
import time
import rospy
from std_msgs.msg import Char


pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

rospy.init_node('teleop')
rospy.loginfo('Press x to exit.')
pub = rospy.Publisher('/cmd_vel', Char, queue_size=10)
r = rospy.Rate(1)

isButtonPressed = False
Button = None

if __name__ == '__main__':
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
            axis_x = joystick.get_axis(0)
            axis_y = joystick.get_axis(1)
            exit_button = joystick.get_button(16)

            if(axis_x > 0.1 or axis_x < -0.1 or axis_y>0.1 or axis_y<-0.1 or exit_button == 1):

                data = None 

                if(not isButtonPressed):

                    if (exit_button == 1):
                        data = 'x'
                        print("Shutting down")
                        print('x')
                        msg = Char(ord(data))
                        break

                    if(axis_x < -0.5 and Button != 'a'):
                        data = 'a'
                        Button = 'a'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))

                    elif(axis_x > 0.5 and Button != 'd'):
                        data = 'd'
                        Button = 'd'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))

                    elif(axis_y < -0.5 and Button != 'w'):
                        data = 'w'
                        Button = 'w'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))

                    elif(axis_y > 0.5 and Button != 's'):
                        data = 's'
                        Button = 's'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))
                    
                    pub.publish(msg)

            else:
                if(isButtonPressed == True):
                    data = 'k'
                    isButtonPressed = False
                    Button = None
                    print('k')
                    msg = Char(ord(data))
                
                pub.publish(msg)
