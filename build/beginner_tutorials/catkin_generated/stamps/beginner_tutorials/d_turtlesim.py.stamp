#!/usr/bin/env python3

import math
from math import sin, cos, pi
import rospy
import tf
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Point, Quaternion, Twist, Vector3
from turtlesim.msg import Pose
import sys

class turtle:
    def __init__(self):
        rospy.init_node('d_turtlesim')
        self.initial_position = Pose()
        self.initial_position = None
        self.current_position = Pose()
        self.sample_rate = 100
        self.vx = 0
        self.vy = 0
        self.wz = 0
        self.er = 0.1

        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        rospy.Subscriber('/turtle1/pose', Pose, self.d_callback)

    def d_callback(self, data):
        if(self.initial_position is None):
            self.initial_position = data
        
        self.current_position = data

    def publish(self):
        if self.current_position.theta == 0.0:
            while (True):
                self.wz=2
                self.vx = 2* int(sys.argv[1])
                data = Twist(Vector3(self.vx, self.vy, 0), Vector3(0, 0, self.wz))
                self.pub.publish(data)
                if(self.current_position.theta >=3.12):
                    self.vx = 0
                    self.vy = 0
                    self.wz = 0
                    data = Twist(Vector3(self.vx, self.vy, 0), Vector3(0, 0, self.wz))
                    self.pub.publish(data)
                    break

            
            # self.vx = 0
            # self.wz = 0
        if(self.current_position.theta>=3.12 and self.current_position.y >= self.initial_position.y + self.er):
            while(True):
                self.vx=0
                self.vy=0
                self.wz=2
                data = Twist(Vector3(self.vx, self.vy, 0), Vector3(0, 0, self.wz))
                self.pub.publish(data)
                
                if(self.current_position.theta <= -1.55 and self.current_position.theta >= -1.59):
                    self.vx=0
                    self.vy=0
                    self.wz=0
                    data = Twist(Vector3(self.vx, self.vy, 0), Vector3(0, 0, self.wz))
                    self.pub.publish(data)
                    break

        if (self.current_position.theta <= -1.55 and self.current_position.theta >= -1.59 and self.current_position.y >= self.initial_position.y + self.er):
            while(True):
                
                self.vx=2
                self.vy=0
                self.wz=0
                data = Twist(Vector3(self.vx, self.vy, 0), Vector3(0, 0, self.wz))
                self.pub.publish(data)
                if(self.current_position.y <= float(self.initial_position.y)+float(self.er)):
                    self.vx = 0
                    self.vy = 0
                    self.wz = 0
                    data = Twist(Vector3(self.vx, self.vy, 0), Vector3(0, 0, self.wz))
                    self.pub.publish(data)
                    break
                    
        


if __name__ == '__main__':
    Turtle = turtle()
    r = rospy.Rate(Turtle.sample_rate)
    while not rospy.is_shutdown():
        Turtle.publish()
        r.sleep()
        
