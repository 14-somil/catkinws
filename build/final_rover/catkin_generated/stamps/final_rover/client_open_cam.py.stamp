import socket
import time
import pickle
import cv2
import sys
import struct

def main():
    HOST = str(sys.argv[1])
    PORT = int(sys.argv[2])

    print(HOST,':',PORT)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    data = b""
    payload_size = struct.calcsize("Q")

    image_path = './images/'

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
            frame = cv2.resize(frame,None, fx=2, fy=2)
            cv2.imshow("Receiving..."+str(sys.argv[3]),frame)
            key = cv2.waitKey(10) 
            if key  == 13:
                break
            elif key == ord('k'):
                height, width, channel = frame.shape
                if(width/height >=3):
                    cropped_frame = frame[0:int(height), 0:int(width/2)]
                    cropped_frame = cv2.putText(cropped_frame, str(time.time()), (50,50), 1, 2, (255,0,0),2)
                    cv2.imwrite(image_path + 'img_' + str(int(time.time())) + '.png', cropped_frame)
                    print('Image saved as '+image_path + 'img_' + str(int(time.time())) + '.png')

        except:
            break
    client.close()   

    while True:
        continue

if __name__=='__main__':
    main()