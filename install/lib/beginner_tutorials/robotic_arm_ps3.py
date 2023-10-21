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

rospy.init_node('robotic_arm_ps3')
rospy.loginfo('Press x to exit.')
pub = rospy.Publisher('/input', Char, queue_size=10)
r = rospy.Rate(1)

isButtonPressed = False
Button = None

if __name__=='__main__':
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
            axis_2 = joystick.get_axis(4)
            button_left = joystick.get_button(15)
            button_right = joystick.get_button(16)
            servo_1_left = joystick.get_button(4)
            servo_1_right = joystick.get_button(5)
            servo_2_left = joystick.get_button(6)
            servo_2_right = joystick.get_button(7)
            pump = joystick.get_button(1)

            exit_button = joystick.get_button(0)

            if(axis_1 > 0.1 or axis_1 < -0.1 or axis_2 > 0.1 or axis_2 < -0.1 or button_left == 1 or button_right == 1 or servo_1_left==1 or servo_1_right==1 or servo_2_left==1 or servo_2_right==1 or exit_button==1 or pump == 1):

                data = None

                if(not isButtonPressed):
                    if (exit_button == 1):
                        data = 'x'
                        print("Shutting down")
                        print('x')
                        msg = Char(ord(data))
                        pub.publish(msg)
                        joystick.quit()
                        pygame.quit()
                        break

                    if(axis_1 < -0.5 and Button != 'a'):
                        data = 'a'
                        Button = 'a'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))
                        pub.publish(msg)

                    elif(axis_1 > 0.5 and Button != 'q'):
                        data = 'q'
                        Button = 'q'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))
                        pub.publish(msg)

                    elif(axis_2 < -0.5 and Button != 'd'):
                        data = 'd'
                        Button = 'd'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))
                        pub.publish(msg)

                    elif(axis_2 > 0.5 and Button != 'e'):
                        data = 'e'
                        Button = 'e'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))
                        pub.publish(msg)

                    elif(button_left==1 and Button != 'n'):
                        data = 'n'
                        Button = 'n'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))
                        pub.publish(msg)

                    elif(button_right==1 and Button != 'm'):
                        data = 'm'
                        Button = 'm'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))
                        pub.publish(msg)

                    elif(servo_1_left==1 and Button != 'j'):
                        data = 'j'
                        Button = 'j'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))
                        pub.publish(msg)

                    elif(servo_1_right==1 and Button != 'k'):
                        data = 'k'
                        Button = 'k'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))
                        pub.publish(msg)

                    elif(servo_2_left==1 and Button != 'i'):
                        data = 'i'
                        Button = 'i'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))
                        pub.publish(msg)

                    elif(servo_2_right==1 and Button != 'o'):
                        data = 'o'
                        Button = 'o'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))
                        pub.publish(msg)
                    
                    elif(pump == 1 and Button != 'z'):
                        data = 'z'
                        Button = 'z'
                        isButtonPressed = True
                        print(data)
                        msg = Char(ord(data))
                        pub.publish(msg)

            else:
                if(isButtonPressed == True):
                    data = 'c'
                    isButtonPressed = False
                    Button = None
                    print('c')
                    msg = Char(ord(data))
                    pub.publish(msg)