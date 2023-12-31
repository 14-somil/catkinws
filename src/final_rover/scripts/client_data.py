import socket
import time
import json
import rospy
from std_msgs.msg import String

data_to_send = {
    "rover":{
        "data":'k'
    }
}

def callback_rover(data):
    global data_to_send

    data_to_send['rover']['data'] = data.data

HOST = '127.0.0.1'
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

rospy.init_node('client_master')
rospy.Subscriber('/rover', String, callback_rover)

while True:
    json_object = json.dumps(data_to_send, indent=4)

    client.send(json_object.encode('utf-8'))

    recieved_message = client.recv(1024).decode('utf-8')
    recieved_dict = json.loads(recieved_message)
    print(recieved_dict)    
    
    time.sleep(0.1)

socket.close()
