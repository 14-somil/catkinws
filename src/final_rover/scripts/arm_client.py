import pygame
import time
import rospy
import sys
import threading
from final_rover.msg import armClient
from std_msgs.msg import Int16

y=0
command = 'c'
pos = 0
pitch = 0 
yaw = 0
gripper = 0

step = 0

iskill =False

rospy.init_node('arm_client')
rospy.loginfo('Press x to exit.')
pub_arm = rospy.Publisher('/arm_client', armClient, queue_size=10)
pub_science = rospy.Publisher('/science_client', Int16, queue_size=10)

pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joysticks found.")
    pygame.quit()
    sys.exit()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Joystick detected:", joystick.get_name())

def publisher():
    global y, command, pos, pitch, yaw, gripper, iskill, pub_arm, pub_science, step

    r=rospy.Rate(100)
    while not iskill:
        msgToSend = armClient(float(y), ord(command), int(pos), float(pitch), float(yaw), int(gripper))
        pub_arm.publish(msgToSend)
        pub_science.publish(Int16(step))
        r.sleep()

publisher_thread = threading.Thread(target=publisher)
publisher_thread.start()

def main():
    global y, command, pos, pitch, yaw, gripper, iskill, joystick, step

    while(True):
        pygame.event.pump()

        y = 255 * joystick.get_axis(0)
        x = -joystick.get_axis(1)
        pitch = -255 * joystick.get_axis(4)
        yaw = 255 * joystick.get_axis(3)
        z = joystick.get_hat(0)[1]
        gripper = joystick.get_hat(0)[0]
        kill = joystick.get_button(0)
        pos1 = joystick.get_button(1)
        pos2 = joystick.get_button(2)
        step1 = joystick.get_button(4)
        step2 = joystick.get_button(5)
        step3 = joystick.get_button(6)
        step4 = joystick.get_button(7)

        if kill == 1:
            rospy.loginfo('Bye!!!')
            command = 'c'
            pos = 0
            y=0
            pitch=0
            yaw=0
            gripper=0
            step = 0
            time.sleep(1)
            iskill = True
            sys.exit()
        
        if(step1 == 1):
            step = -40
        elif(step2 == 1):
            step = 40
        elif(step3 == 1):
            step = -10
        elif(step4 == 1):
            step = 10
        else:
            step = 0

        if pos1 == 1:
            pos = 1
        elif pos2 == 1:
            pos = 2
        else:
            pos = 0

        if(x >0.5):
            command = 'w'
        elif(x <-0.5):
            command = 's'
        elif(z == 1):
            command = '8'
        elif(z == -1):
            command = '2'
        else:
            command = 'c'



if __name__ == '__main__':
    main()