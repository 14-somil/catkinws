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

        rospy.init_node('my_odom') #node name

        self.x=0
        self.y=0
        self.th=0
        self.sample_rate=10
        self.dt = 0.1

        #subcriber
        rospy.Subscriber("/cmd_vel", Twist, self.odomCallback)
    
    def odomCallback(self, msg):

        # phi = (math.pi + msg.angular.z * self.dt)/2
        # delta_x = (msg.linear.x * self.dt) * math.sin(phi + self.th - (math.pi /2))
        # delta_y = (msg.linear.x * self.dt) * math.cos(phi + self.th - (math.pi /2))
        # delta_th = msg.angular.z * self.dt
        delta_x = msg.linear.x * self.dt * math.cos(self.th) 
        delta_y = msg.linear.x * self.dt * math.sin(self.th) 
        delta_th = msg.angular.z * self.dt 

        self.x += delta_x
        self.y += delta_y
        self.th += delta_th
        rospy.loginfo("x=%f , y=%f, th=%f", self.x, self.y, self.th)

    


if __name__ == '__main__':
    odom=odom_task()
    r = rospy.Rate(odom.sample_rate)
    while not rospy.is_shutdown():
        try:
            # odom.broadcast()
            # odom.publish()
            r.sleep()
        except rospy.exceptions.ROSTimeMovedBackwardsException:
            pass
