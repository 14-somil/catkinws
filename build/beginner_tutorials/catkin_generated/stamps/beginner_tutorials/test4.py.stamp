#!/usr/bin/env python3

import rospy
from beginner_tutorials.msg import anglesMsg
from visual_kinematics.RobotSerial import *
import numpy as np
import sys
from math import pi

def callback(msg):
    print(msg.first)
    print(msg.second)
    print(msg.base)

if __name__ == "__main__":
    rospy.init_node('Test', anonymous=True)
    rospy.Subscriber('chatter', anglesMsg, callback)

    rospy.spin()