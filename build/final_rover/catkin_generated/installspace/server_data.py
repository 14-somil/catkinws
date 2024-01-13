import socket
import time
import sys
import json
import rospy
from beginner_tutorials.msg import RoverMsg


HOST = '192.168.1.20' #127.0.0.1 mat use karna kabhi woh wifi use karta hai
# HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090

print(HOST)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

rospy.init_node('server_master')
pub_rover = rospy.Publisher('/rover', RoverMsg, queue_size=10)

data_to_send={
    "time":time.time()
}

server.listen(5) #5 se jyada unaccepted connection ko reject kar dega
communication_socket, address = server.accept()
print(f"connected to {address}")

while True:
    message = communication_socket.recv(1024).decode('utf-8')
    recieved_data = json.loads(message)
    rover_msg = RoverMsg(float(recieved_data['rover']['x']), float(recieved_data['rover']['y']))
    pub_rover.publish(rover_msg)
    print(recieved_data)

    data_to_send["time"] = time.time()
    communication_socket.send(json.dumps(data_to_send).encode('utf-8'))

