import socket
import time
import rospy
from std_msgs.msg import Char

rospy.init_node('robotic_arm_keyboard')
rospy.loginfo('Press x to exit.')
pub = rospy.Publisher('/cmd_vel', Char, queue_size=10)

HOST = '10.70.39.56'#127.0.0.1 mat use karna kabhi woh wifi use karta hai
# HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090

print(HOST)                                   

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

server.listen(5) #5 se jyada unaccepted connection ko reject kar dega
communication_socket, address = server.accept()
print(f"connected to {address}")

while True:
    recv_mesg = communication_socket.recv(1024).decode('utf-8')
    pub.publish(ord(recv_mesg))
    communication_socket.send('Received...'.encode('utf-8'))