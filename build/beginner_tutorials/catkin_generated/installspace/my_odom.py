#!/usr/bin/env python3

import math
from math import sin, cos, pi
import rospy
import tf
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

class odom_task:

    #self
    def __init__(self):
        self.x=0
        self.y=0
        self.th=0
        self.sample_rate=100
        self.dt = 0.01

        #subcriber
        rospy.Subscriber("/cmd_vel", Twist, self.odomCallback)
    
    def odomCallback(self, msg):

        # phi = (math.pi - msg.angular.z * self.dt)/2
        # delta_x = (msg.linear.x * self.dt) * math.sin(se)
        rospy.loginfo("%f", msg.angular.z)

    


if __name__ == '__main__':
    odom=odom_task()
    r = rospy.Rate(odom.sample_rate)
    while not rospy.is_shutdown():
        try:
            odom.broadcast()
            odom.publish()
            r.sleep()
        except rospy.exceptions.ROSTimeMovedBackwardsException:
            pass
