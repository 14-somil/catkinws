#!/usr/bin/env python3

import rospy
from std_msgs.msg import Char
import tf
import termios
import sys
import tty

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

if __name__ == '__main__':
    rospy.init_node('teleop')
    rospy.loginfo('Press x to exit.')
    pub = rospy.Publisher('/cmd_vel', Char, queue_size=10)
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        input = getch()
        if(input == 'x'):
            break

        rospy.loginfo(input)
        data = Char(ord(input))
        pub.publish(data)
