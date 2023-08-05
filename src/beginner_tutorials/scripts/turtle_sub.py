#!/usr/bin/env python3
# Set linear and angular values of Turtlesim's speed and turning. 

import rospy    # Needed to create a ROS node 
    # Message that moves base   
import math
from math import sin, cos, pi
import tf
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist, Vector3

class ReadTurtlesim: 
        def __init__(self): 
                
            #initialization
            # self.current_time=rospy.Time.now()
            self.sample_rate=100.0
            self.x = 0.0
            self.y = 0.0
            self.th = 0.0 #theta
            self.wz=1.0
            self.v=0.0
            self.vx=1.0
            self.vy=0.0
            self.dt=0.01
            
            rospy.init_node('TurtleSubcribe', anonymous=False) 
            rospy.loginfo(" Press CTRL+c to stop TurtleBot") 

            self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=50)

            self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callbackPose)

            rospy.spin()

        def callbackPose(self,msg):
            self.th = float(msg.theta)
            rospy.loginfo("%f", self.th)
        


        def publish(self):
             hello = Twist(Vector3(self.vx, self.vy, 0), Vector3(0, 0, self.wz))

             self.pub.publish(hello)


if __name__ == "__main__":
    turtlesim = ReadTurtlesim()
    r = rospy.Rate(turtlesim.sample_rate)
    while not rospy.is_shutdown():
        try:
            turtlesim.publish()
            r.sleep()
        except rospy.ROSInterruptException:
            rospy.loginfo("End of the trip for Turtlesim")