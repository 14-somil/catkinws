import rospy
from pynput import keyboard
import sys
import time
from std_msgs.msg import Char

rospy.init_node('robotic_arm_keyboard')
rospy.loginfo('Press x to exit.')
pub = rospy.Publisher('/cmd_vel', Char, queue_size=10)

isButton = False
button = None

def on_key_press(key):

    global isButton, button

    try:
        if(not isButton):
            if(key.char == 'x' and button != 'x'):
                print('x')
                pub.publish(ord('x'))
                isButton = True
                button = 'x'
                print("Shutting down....")
                time.sleep(1)
                sys.exit()

            if(key.char == 'w' and button != 'w'):
                print('w')
                pub.publish(ord('w'))
                isButton = True
                button = 'w'

            elif(key.char == 'a' and button != 'a'):
                print('a')
                pub.publish(ord('a'))
                isButton = True
                button = 'a'

            elif(key.char == 'd' and button != 'd'):
                print('d')
                pub.publish(ord('d'))
                isButton = True
                button = 'd'

            elif(key.char == 's' and button != 's'):
                print('s')
                pub.publish(ord('s'))
                isButton = True
                button = 's'

    except AttributeError:
    # Some special keys don't have a `char` attribute
        pass

def on_key_release(key):
    # Handle key release event
    global isButton, button

    try:
            pub.publish(ord('k'))
            isButton = False
            button = None


    except AttributeError:
        pass


if __name__=='__main__':
    
    with keyboard.Listener(
            on_press=on_key_press,
            on_release=on_key_release) as listener:
        listener.join()

