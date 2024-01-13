import pygame
import time
import rospy
import sys
from beginner_tutorials.msg import roboticArmController,encodersFeedback
import threading
from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi 

x_z = 'c'
y = 0
iskill = False
speed = 5
pitch =0 
yaw = 0
gripper = 0
isPreset = False

angles = {
    'first':0,
    'second':0
}

target = {
    'first':0,
    'second':0
}

def subCallback(msg):
    global angles
    if(angles['first'] is None):
        rospy.loginfo('Go!!!')
    angles['first'] = msg.first
    angles['second'] = msg.second

rospy.init_node('rover_joystick')
rospy.loginfo('Press x to exit.')
pub = rospy.Publisher('/arm', roboticArmController, queue_size=10)
rospy.Subscriber('/angleFeedback', encodersFeedback, subCallback)

pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joysticks found.")
    pygame.quit()
    sys.exit()
# Initialize the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Joystick detected:", joystick.get_name())

np.set_printoptions(precision=3, suppress=True)
dh_params = np.array([[4.5,4.0,-0.5*pi,0.5*pi],
                    [0.0,54.55 ,0.0, -0.5*pi],                      
                    [0.0, 54.55, 0.0*pi, 0.5*pi]])
robot = RobotSerial(dh_params)

def publisher():
    global pub,x_z,y, target, pitch, yaw, gripper

    r = rospy.Rate(100)
    while not iskill:
        msgToSend = roboticArmController(float(y), float(target['first']), float(target['second']), float(pitch), float(yaw), int(gripper))
        pub.publish(msgToSend)
        r.sleep()

def gotoPos1():
    global target, isPreset
    target = {
        'first':0,
        'second':0
    }

    isPreset = True

    while(int(angles['first'])!=int(target['first']) and int(angles['second'])!=int(target['second'])):
        continue

    isPreset = False

def gotoPos2():
    global target, isPreset
    target = {
        'first':10,
        'second':20
    }

    isPreset = True

    while(int(angles['first'])!=int(target['first']) and int(angles['second'])!=int(target['second'])):
        continue

    isPreset = False

def controller():
    global x_z, y, joystick, iskill, pitch, yaw, gripper

    while True:
        pygame.event.pump()
        y = 30 * joystick.get_axis(0)
        x = -joystick.get_axis(1)
        pitch = -255* joystick.get_axis(4)
        yaw = 255 * joystick.get_axis(3)
        z = joystick.get_hat(0)[1]
        gripper = joystick.get_hat(0)[0]
        kill = joystick.get_button(0)
        pos1 = joystick.get_button(1)
        pos2 = joystick.get_button(2)

        if kill == 1:
            rospy.loginfo('Bye!!!')
            x_z = 'c'
            y=0
            pitch=0
            yaw=0
            gripper=0
            time.sleep(1)
            iskill = True
            sys.exit()

        if pos1 == 1:
            gotoPos1()
        elif pos2 == 1:
            gotoPos2()

        if(x >0.5):
            x_z = 'w'
        elif(x <-0.5):
            x_z = 's'
        elif(z == 1):
            x_z = '8'
        elif(z == -1):
            x_z = '2'
        else:
            x_z = 'c'
        
        rospy.loginfo("x_z: %s, y: %f", x_z, y)    

publisher_thread = threading.Thread(target=publisher)
publisher_thread.start()
controller_thread = threading.Thread(target=controller)
controller_thread.start()

def main():
    global iskill, robot, target, angles, speed

    while not iskill:
        angle_rad={
            'first':angles['first'] *pi/180,
            'second':angles['second'] *pi/180,
        }

        theta = np.array([0, angle_rad['first'], angle_rad['second']])
        f= robot.forward(theta)

        x,y,z = f.t_3_1.reshape([3, ])



        if(x_z == 'w'):
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
        elif(x_z == 's'):
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
        elif(x_z == '8'):
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
        elif(x_z == '2'):
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