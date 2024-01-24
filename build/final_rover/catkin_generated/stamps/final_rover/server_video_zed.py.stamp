import socket
import cv2
import pickle
import struct
import sys
import rospy
from sensor_msgs.msg import CompressedImage
import numpy as np
from cv_bridge import CvBridge

frame = np.zeros((1920, 1080, 3), np.uint8)

bridge = CvBridge()

def callback(data):
    global frame,bridge

    frame = bridge.compressed_imgmsg_to_cv2(data, "bgr8")

def main():
    print('server_video_zed.py')
    global frame

    HOST = str(sys.argv[1])
    PORT = int(sys.argv[2])

    print(HOST,':',PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))

    server.listen(5) 
    communication_socket, address = server.accept()
    print(f"connected to {address}")

    rospy.init_node('zed_camera_node')
    rospy.Subscriber('/zed2i/zed_node/stereo/image_rect_color/compressed', CompressedImage, callback)

    while True:

        frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
        
        a = pickle.dumps(frame)
        message = struct.pack("Q",len(a))+a
        communication_socket.sendall(message)

        frame = cv2.resize(frame, None, fx=2, fy=2)
        cv2.imshow('Sending...', frame)
        key = cv2.waitKey(33)
        if key == 13:
            communication_socket.close()
            break

        continue


if __name__ == '__main__':
    main()