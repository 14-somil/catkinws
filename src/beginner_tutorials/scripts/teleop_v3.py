import pygame
import time
import rospy
import sys
from beginner_tutorials.msg import RoverMsg
import threading

rospy.init_node('rover_joystick')
rospy.loginfo('Press x to exit.')
pub = rospy.Publisher('/rover', RoverMsg, queue_size=10)

pygame.init()
pygame.joystick.init()

iskill = False
k=100
rospy.loginfo("k= %f", k)

joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("No joysticks found.")
    pygame.quit()
    sys.exit()

# Initialize the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

print("Joystick detected:", joystick.get_name())

axes=[0,0]

def publisher():
    global pub, axes, iskill

    r = rospy.Rate(100)
    while not iskill:
        msgToSend = RoverMsg(float(axes[0]), float(axes[1]))
        pub.publish(msgToSend)
        r.sleep()

publisher_thread = threading.Thread(target=publisher)
publisher_thread.start()

def main():
    global axes, joystick, iskill,k
    while True:
        pygame.event.pump()
        x = - joystick.get_axis(1)
        y = joystick.get_axis(0)
        kill = joystick.get_button(0)
        speed_reduce = joystick.get_button(4)
        speed_increase = joystick.get_button(5)

        if(speed_increase == 1):
            k += 1
            rospy.loginfo("k= %f", k) 
            time.sleep(0.01)
        
        if(speed_reduce == 1):
            k -= 1
            rospy.loginfo("k= %f", k) 
            time.sleep(0.01)

        if kill == 1:
            rospy.loginfo('Bye!!!')
            axes=[0, 0]
            time.sleep(1)
            iskill = True
            sys.exit()
        
        axes=[k*x, 1.75*k*y]

if __name__=='__main__':
    main()