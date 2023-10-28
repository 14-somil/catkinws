
from __future__ import print_function

from beginner_tutorials.srv import angles,anglesResponse
import rospy

def handle_angles(req):
    print("Returning true")
    print(req.first)
    print(req.second)
    print(req.base)
    return True

def angles_server():
    rospy.init_node('angles')
    s = rospy.Service('angles', angles, handle_angles)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    angles_server()