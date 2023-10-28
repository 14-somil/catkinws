#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi
import pygame
import time
import rospy
from beginner_tutorials.srv import angles
from std_msgs.msg import Bool
from aruco import find_least_pitch_aruco_marker
from aruco_distance import calculate_distance_from_aruco_markers
from coords2 import get_detected_coordinates

x=0
y=54
z=58
first=0
second=0
base=0
servo1=0
servo2=0

def rotate_acw():
    global x,y,z,first,second,base,servo1,servo2

    base += 1

    resp=request(int(first),int(second),int(base),int(servo1),int(servo2),False)

    return resp.check

def rotate_cw():
    global x,y,z,first,second,base,servo1,servo2

    base -= 1

    resp=request(int(first),int(second),int(base),int(servo1),int(servo2),False)

    return resp.check

def forward():
    
    global x,y,z,first,second,base,servo1,servo2
    y = y+5

    base, first, second=ik(x,y,z)

    resp=request(int(first),int(second),int(base),int(servo1),int(servo2), True)
    print(resp.check)
    return resp.check

def backward():

    global x,y,z,first,second,base,servo1,servo2
    y = y-5

    base, first, second=ik(x,y,z)

    resp=request(int(first),int(second),int(base),int(servo1),int(servo2), True)
    print(resp.check)
    return resp.check

def up():
    
    global x,y,z
    z = z+5

    base, first, second=ik(x,y,z)

    resp=request(int(first),int(second),int(base),int(servo1),int(servo2), True)
    print(resp.check)
    return resp.check

def down():

    global x,y,z
    z = z-5

    base, first, second=ik(x,y,z)

    resp=request(int(first),int(second),int(base),int(servo1),int(servo2), True)
    print(resp.check)
    return resp.check


def orient(least_pitch,least_roll, least_yaw):

    global x,y,z,first,second,base,servo1,servo2

    base, first, second=ik(x,y,z, least_pitch, least_roll, least_yaw)

    resp=request(int(first),int(second),int(base),int(servo1),int(servo2), False)
    print(resp.check)
    return resp.check

def reach_bottom(distance):
    global x,y,z,first,second,base,servo1,servo2

    temp = distance

    while(temp>0):
        down()
        temp -= 5

def reach_top(distance):
    global x,y,z,first,second,base,servo1,servo2

    temp = -distance

    while(temp<0):
        up()
        temp += 5

def drop_zone():

    base, first, second=ik(x,y,z,0,0,0)

    resp=request(int(first),int(second),int(base),int(servo1),int(servo2),False)
    print(resp.check)
    return resp.check

def back_home():

    base, first, second=ik(0,54,58,0,0,0)

    resp=request(int(first),int(second),int(base),int(servo1),int(servo2),False)
    print(resp.check)
    return resp.check

def suction_on():
    pub.publish(True)

def suction_off():
    pub.publish(False)

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

    rospy.init_node('control_alg')
    pub = rospy.Publisher('/suction_control', Bool, queue_size=10)
    rospy.wait_for_service('angles')
    request = rospy.ServiceProxy('angles', angles)

    calibration_data_path = "./calib_data/MultiMatrix.npz"  # Update with the path to your calibration data

    while(True):
        x_box,y_box=get_detected_coordinates()
        if(x_box!=320 and y_box!=240):

            while(x_box <= 310 or x_box >= 330):
                x_box,y_box=get_detected_coordinates()
                if(x_box < 320):
                    #rotate ACW by 1degree
                    rotate_acw()
                    print("1 deg ACW")
                elif(x_box>320):
                    #rotate CW by 1degree
                    rotate_cw()
                    print("1 deg CW")    
                time.sleep(0.069) 

            while(y_box<=230 or y_box>=250):
                x_box,y_box=get_detected_coordinates()
                if(y_box<240):
                    #move forward by 1cm
                    forward()
                    print("Move fwd by 5cm")
                if(y_box>240):
                    #move backward by 1cm
                    backward()
                    print("Move back by 5cm")            
                time.sleep(0.069)


            least_pitch_id, least_pitch, least_roll , least_yaw = find_least_pitch_aruco_marker(2, calibration_data_path)
            orient(least_pitch,least_roll, least_yaw)

            suction_on()

            distance = calculate_distance_from_aruco_markers(2, calibration_data_path)

            reach_bottom(distance)
            reach_top(distance)

            drop_zone()
            suction_off()

            back_home()

