import rospy
import time 
import threading
from final_rover.msg import RoverMsg, roverServer
from geometry_msgs.msg import PoseStamped
import math

left = 0
right = 0
x=0
y=0
isPID = False
yaw = 0
reference_angle = 0

def control_callback(data):
    global x,y, isPID

    x=data.x
    y=data.y
    isPID = data.isPID

def yaw_callback(data):
    global yaw

    qx = data.pose.orientation.x
    qy = data.pose.orientation.y
    qz = data.pose.orientation.z
    qw = data.pose.orientation.w
    yaw = math.atan2(2 * (qw * qz + qx * qy), 1 - 2 * (qy**2 + qz**2))

rospy.init_node('chassis_controller')
pub = rospy.Publisher('/rover_server', roverServer, queue_size=10)
rospy.Subscriber('/rover_controller_server', RoverMsg, control_callback)
rospy.Subscriber('/zed2i/zed_node/pose', PoseStamped, yaw_callback)

def publisher():
    global pub, left, right

    r=rospy.Rate(100)
    while True:
        msgToSend = roverServer(int(left), int(right))
        pub.publish(msgToSend)
        r.sleep()

publisher_thread = threading.Thread(target=publisher)
publisher_thread.start()

def main():
    print('chassis_server.py')
    global x,y,left,right,yaw,reference_angle, isPID

    if(isPID == False):
        left = x+y
        right = x-y
        reference_angle = yaw
    
    else:
        diff = reference_angle - yaw
        correction = 19*diff*x

        right = x+correction
        left = x-correction


if __name__ == '__main__':
    main()