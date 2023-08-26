#!/usr/bin/env python3

import socket
import rospy
from std_msgs.msg import Char
import tf
import termios
import sys
import tty
import pygame
import time

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090

print(HOST)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5) #5 se jyada unaccepted connection ko reject kar dega
communication_socket, address = server.accept()
print(f"connected to {address}")

rospy.init_node('teleop')
pub = rospy.Publisher('/cmd_vel', Char, queue_size=10)
r = rospy.Rate(1)

while not rospy.is_shutdown():
    
    message = communication_socket.recv(1024).decode('utf-8')
    rospy.loginfo(message)
    msg = Char(ord(message))
    pub.publish(msg)
    r.sleep()
    

