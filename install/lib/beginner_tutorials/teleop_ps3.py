#!/usr/bin/env python3

import rospy
from std_msgs.msg import Char
import tf
import termios
import sys
import tty
import pygame
import time

pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

if __name__ == '__main__':

    if joystick_count == 0:
        print("No joysticks found.")
        pygame.quit()
    else:
        # Initialize the first joystick
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        print("Joystick detected:", joystick.get_name())

        rospy.init_node('teleop')
        pub = rospy.Publisher('/cmd_vel', Char, queue_size=10)
        r = rospy.Rate(1)

        while not rospy.is_shutdown():
            pygame.event.pump()
            axis_x = joystick.get_axis(0)
            axis_y = joystick.get_axis(1)
            exit_button = joystick.get_button(16)

            if(axis_x > 0.1 or axis_x < -0.1 or axis_y>0.1 or axis_y<-0.1 or exit_button == 1):

                data = '\0'

                if (exit_button == 1):
                    break

                if(axis_x < -0.5):
                    data = 'a'
                elif(axis_x > 0.5):
                    data = 'd'
                elif(axis_y < -0.5):
                    data = 'w'
                elif(axis_y > 0.5):
                    data = 's'
                rospy.loginfo(data)
                msg = Char(ord(data))
                pub.publish(msg)
                time.sleep(1.5)
                r.sleep()

