import pygame
import time
import rospy
import sys
from final_rover.msg import RoverMsg
import threading

rospy.init_node('rover_joystick')
rospy.loginfo('Press x to exit.')
pub = rospy.Publisher('/rover_client', RoverMsg, queue_size=10)

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

joystick = None
# for i in range(joystick_count):
#     if 'Xbox 360 Controller' in pygame.joystick.Joystick(i).get_name():
#         joystick = pygame.joystick.Joystick(i)
#         joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Joystick detected:", joystick.get_name())

axes=[0,0]
isPID = False

def publisher():
    global pub, axes, iskill, isPID

    r = rospy.Rate(100)
    while not iskill:
        msgToSend = RoverMsg(float(axes[0]), float(axes[1]), bool(isPID))
        pub.publish(msgToSend)
        r.sleep()

publisher_thread = threading.Thread(target=publisher)
publisher_thread.start()

def main():
    print('chassis_client.py')
    global axes, joystick, iskill,k, isPID
    while True:
        pygame.event.pump()
        x_no_pid = - joystick.get_axis(1)
        x_pid_neg = -(joystick.get_axis(2) + 1) / 2
        x_pid_pos = (joystick.get_axis(5) + 1) / 2

        pid_pos_button = joystick.get_button(7)
        pid_neg_button = joystick.get_button(6)

        x = x_no_pid + x_pid_neg + x_pid_pos

        if(pid_neg_button == 1 or pid_pos_button == 1 or x_pid_neg != 0 or x_pid_pos != 0):
            isPID = True
        else:
            isPID = False
        
        y = -joystick.get_axis(0)
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
            isPID = False
            time.sleep(1)
            iskill = True
            sys.exit()
        
        axes=[k*x, 1.75*k*y]

if __name__=='__main__':
    main()