import rospy
from pynput import keyboard
import sys
import time
from std_msgs.msg import String

rospy.init_node('rover_keyboard')
rospy.loginfo('Press x to exit.')
pub = rospy.Publisher('/rover', String, queue_size=10)

isButton = False
button = None

def on_key_press(key):

    global isButton, button

    try:
        if(not isButton):
            if(key.char == 'x' and button != 'x'):
                print('k')
                pub.publish('k')
                isButton = True
                button = 'k'
                print("Shutting down....")
                time.sleep(1)
                sys.exit()

            if(key.char == 'w' and button != 'w'):
                print('w')
                pub.publish('w')
                isButton = True
                button = 'w'

            elif(key.char == 'a' and button != 'a'):
                print('a')
                pub.publish('a')
                isButton = True
                button = 'a'

            elif(key.char == 'd' and button != 'd'):
                print('d')
                pub.publish('d')
                isButton = True
                button = 'd'

            elif(key.char == 's' and button != 's'):
                print('s')
                pub.publish('s')
                isButton = True
                button = 's'

    except AttributeError:
    # Some special keys don't have a `char` attribute
        pass

def on_key_release(key):
    # Handle key release event
    global isButton, button

    try:
            pub.publish('k')
            isButton = False
            button = None


    except AttributeError:
        pass


if __name__=='__main__':
    pub.publish('k')
    
    with keyboard.Listener(
            on_press=on_key_press,
            on_release=on_key_release) as listener:
        listener.join()

