import socket
import time
import pickle
import cv2
import sys
import struct
import rospy
from final_rover.msg import GPS

latitude = 0
longitude = 0
altitude = 0

today_time = int(time.time())

count = 1

def callback_gps(msg):
    global latitude, longitude, altitude

    latitude = msg.latitude
    longitude = msg.longitude
    altitude = msg.altitude

rospy.init_node('camera_'+str(sys.argv[3]))
rospy.Subscriber('/GPS_client', GPS, callback_gps)

def main():
    print('client_open_cam.py')
    global latitude, longitude, altitude, count

    HOST = str(sys.argv[1])
    PORT = int(sys.argv[2])

    print(HOST,':',PORT)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    data = b""
    payload_size = struct.calcsize("Q")

    image_path = '/home/somil/rover_images/'

    while True:
        try:
            while len(data) < payload_size:
                packet = client.recv(4*1024)
                if not packet: break
                data+=packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q",packed_msg_size)[0]
            while len(data) < msg_size:
                data += client.recv(4*1024)
            frame_data = data[:msg_size]
            data  = data[msg_size:]
            frame = pickle.loads(frame_data)
            frame = cv2.resize(frame,None, fx=4, fy=4)
            cv2.imshow("Receiving..."+str(sys.argv[3]),frame)
            key = cv2.waitKey(10) 
            if key  == 13:
                break
            elif key == ord('k'):
                height, width, channel = frame.shape
                if(width/height >=3):
                    cropped_frame = frame[0:int(height), 0:int(width/2)]

                    text_to_print = 'latitude: ' + str(latitude) + ', longitude: ' + str(longitude) + ', altitude: ' + str(altitude)
                    cropped_frame = cv2.putText(cropped_frame, text_to_print, (50,50), 1, 1.5, (0,0,255),2)

                    cv2.imwrite(image_path + 'img_' +str(today_time)+'_'+ str(int(count)) + '.png', cropped_frame)
                    print('Image saved as '+image_path + 'img_' +str(today_time)+'_'+ str(int(count)) + '.png')

                elif(width/height >=1):
                    cropped_frame = frame[0:int(height), 0:int(width)]

                    text_to_print = 'latitude: ' + str(latitude) + ', longitude: ' + str(longitude) + ', altitude: ' + str(altitude)
                    cropped_frame = cv2.putText(cropped_frame, text_to_print, (50,50), 1, 1.5, (0,0,255),2)

                    cv2.imwrite(image_path + 'img_' +str(today_time)+'_'+ str(sys.argv[3]) + '_' + str(int(count)) + '.png', cropped_frame)
                    print('Image saved as '+image_path + 'img_' +str(today_time)+'_'+ str(sys.argv[3]) + '_' + str(int(count)) + '.png')
                count+=1
        except:
            break
    client.close()   

    while True:
        continue

if __name__=='__main__':
    main()