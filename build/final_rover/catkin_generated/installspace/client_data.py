import socket
import time
import json
import rospy
from final_rover.msg import RoverMsg, armClient, GPS
from std_msgs.msg import Int16
print('client_data.py')
data_to_send = {
    'rover':{
        'x':0,
        'y':0,
        'isPID':False
    },
    'arm':{
        'y':0,
        'command':'c',
        'position':0,
        'pitch': 0,
        'yaw': 0,
        'gripper':0
    },
    'science':{
        'step': 0 
    }
}

recieved_dict={
    "time":time.time(),
    'science':{
        'pressure':0,
        'soil_moisture':0
    }
    # 'GPS':{
    #     'latitude':0,
    #     'longitude':0,
    #     'altitude':0
    # }
}

def callback_rover(data):
    global data_to_send

    data_to_send['rover']['x'] = data.x
    data_to_send['rover']['y'] = data.y
    data_to_send['rover']['isPID'] = data.isPID

def callback_arm(data):
    global data_to_send

    data_to_send['arm'] = {
        'y':data.y,
        'command':chr(data.command),
        'position':data.position,
        'pitch': data.pitch,
        'yaw': data.yaw,
        'gripper':data.gripper
    }

def callback_science(data):
    global data_to_send

    data_to_send['science']['step'] = data.data

HOST = '127.0.0.1'
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

rospy.init_node('client_master')
# pub_gps = rospy.Publisher('/GPS_client', GPS, queue_size=10)
rospy.Subscriber('/rover_client', RoverMsg, callback_rover)
rospy.Subscriber('/arm_client', armClient, callback_arm)
rospy.Subscriber('/science_client', Int16, callback_science)

while True:
    json_object = json.dumps(data_to_send, indent=4)

    client.send(json_object.encode('utf-8'))

    recieved_message = client.recv(1024).decode('utf-8')
    recieved_dict = json.loads(recieved_message)
    print(recieved_dict)    

    # msgToSend_gps = GPS(float(recieved_dict['GPS']['latitude']), float(recieved_dict['GPS']['longitude']), float(recieved_dict['GPS']['altitude']))
    # pub_gps.publish(msgToSend_gps)
    
    time.sleep(0.1)

socket.close()
