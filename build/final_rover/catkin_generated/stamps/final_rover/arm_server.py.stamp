import time
import rospy
from final_rover.msg import encodersFeedback, anglesMsg, armClient
import threading
from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi

y=0
command = 'c'
position = 0
pitch = 0
yaw = 0
gripper = 0

isPreset = False

speed = 5

angles = {
    'first':0,
    'second':0
}

target = {
    'first':0,
    'second':0
}

np.set_printoptions(precision=3, suppress=True)
dh_params = np.array([[4.5,4.0,-0.5*pi,0.5*pi],
                    [0.0,54.55 ,0.0, -0.5*pi],                      
                    [0.0, 54.55, 0.0*pi, 0.5*pi]])
robot = RobotSerial(dh_params)

def arm_callback(data):
    global y, command, position, pitch, yaw, gripper
    y = data.y
    command = chr(data.command)
    position = data.position
    pitch = data.pitch
    yaw = data.yaw
    gripper = data.gripper

def angles_callback(data):
    global angles

    angles = {
        'first':data.first,
        'second':data.second
    }

rospy.init_node('arm_server')
rospy.Subscriber('/arm_controller_server', armClient, arm_callback)
rospy.Subscriber('/angle_feedback_server', encodersFeedback, angles_callback)
pub = rospy.Publisher('/arm_angles_server', anglesMsg, queue_size=10)

def publisher():
    global y, target, pitch, yaw, gripper, pub

    r = rospy.Rate(100)

    while True:
        msgToSend = anglesMsg(float(y), float(target['first']), float(target['second']), float(pitch), float(yaw), int(gripper))
        pub.publish(msgToSend)
        r.sleep()

publisher_thread = threading.Thread(target=publisher)
publisher_thread.start()

def goToPos1():
    global target, isPreset

    target = {
        'first':0,
        'second':0
    }
    isPreset = True

def goToPos2():
    global target, isPreset

    target = {
        'first':10,
        'second':20
    }
    isPreset = True

def main():
    print('arm_server.py')
    global robot, angles, target, speed, isPreset, command, position
    
    while True:
        angle_rad = {
            'first':angles['first'] *pi/180,
            'second':angles['second'] *pi/180,
        }

        theta = np.array([0, angle_rad['first'], angle_rad['second']])
        f= robot.forward(theta)

        x,y,z = f.t_3_1.reshape([3, ])

        if position == 1:
            goToPos1()
        elif position == 2:
            goToPos2()

        if(command == 'w'):
            isPreset = False
            xyz=np.array([[x],[y+speed],[z]])
            abc=np.array([0,0,0])

            end=Frame.from_euler_3(abc,xyz)
            ang=robot.inverse(end)
            ang=ang*180/pi

            _, new_first, new_second = ang
            
            target = {
                'first':new_first,
                'second':new_second,
            }
        elif(command == 's'):
            isPreset = False
            xyz=np.array([[x],[y-speed],[z]])
            abc=np.array([0,0,0])

            end=Frame.from_euler_3(abc,xyz)
            ang=robot.inverse(end)
            ang=ang*180/pi

            _, new_first, new_second = ang
            
            target = {
                'first':new_first,
                'second':new_second
            }
        elif(command == '8'):
            isPreset = False
            xyz=np.array([[x],[y],[z+speed]])
            abc=np.array([0,0,0])

            end=Frame.from_euler_3(abc,xyz)
            ang=robot.inverse(end)
            ang=ang*180/pi

            _, new_first, new_second = ang
            
            target = {
                'first':new_first,
                'second':new_second
            }
        elif(command == '2'):
            isPreset = False
            xyz=np.array([[x],[y],[z-speed]])
            abc=np.array([0,0,0])

            end=Frame.from_euler_3(abc,xyz)
            ang=robot.inverse(end)
            ang=ang*180/pi

            _, new_first, new_second = ang
            
            target = {
                'first':new_first,
                'second':new_second
            }
        elif(not isPreset):
            target = angles


if __name__ == '__main__':
    main()