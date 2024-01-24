import socket
import time
import sys
import json
import rospy
from final_rover.msg import RoverMsg, armClient, GPS
from std_msgs.msg import Int16, Float32
from sensor_msgs.msg import FluidPressure

print('server_data.py')
HOST = '127.0.0.1' #127.0.0.1 mat use karna kabhi woh wifi use karta hai
# HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090

print(HOST)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

data_to_send={
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

recieved_data = {
    'rover':{
        'x':0,
        'y':0,
        'isPID': False
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

# def callback_gps(data):
#     global data_to_send

#     data_to_send['GPS'] = {
#         'latitude':data.latitude,
#         'longitude':data.longitude,
#         'altitude':data.altitude
#     }

def callback_moisture(data):
    global data_to_send

    data_to_send['science']['soil_moisture'] = data.data

def callback_pressure(data):
    global data_to_send

    data_to_send['science']['pressure'] = data.fluid_pressure * 100

rospy.init_node('server_master')
pub_rover = rospy.Publisher('/rover_controller_server', RoverMsg, queue_size=10)
pub_arm = rospy.Publisher('/arm_controller_server', armClient, queue_size=10)
pub_science = rospy.Publisher('/science_server', Int16, queue_size=10)
# rospy.Subscriber('/gps_location', GPS, callback_gps)
rospy.Subscriber('/moisture_feedback', Float32, callback_moisture)
rospy.Subscriber('/zed2i/zed_node/atm_press', FluidPressure, callback_pressure)

server.listen(5) #5 se jyada unaccepted connection ko reject kar dega
communication_socket, address = server.accept()
print(f"connected to {address}")

while True:
    message = communication_socket.recv(1024).decode('utf-8')
    recieved_data = json.loads(message)

    rover_msg = RoverMsg(float(recieved_data['rover']['x']), float(recieved_data['rover']['y']), bool(recieved_data['rover']['isPID']))
    pub_rover.publish(rover_msg)

    arm_msg = armClient(float(recieved_data['arm']['y']), ord(recieved_data['arm']['command']), int(recieved_data['arm']['position']), float(recieved_data['arm']['pitch']), float(recieved_data['arm']['yaw']), int(recieved_data['arm']['gripper'])) 
    pub_arm.publish(arm_msg)

    science_msg = Int16(recieved_data['science']['step'])
    pub_science.publish(science_msg)

    print(recieved_data)

    data_to_send["time"] = time.time()
    communication_socket.send(json.dumps(data_to_send).encode('utf-8'))

