import socket
import cv2
import pickle
import struct
import sys

def main():
    print('server_open_cam.py')
    HOST = str(sys.argv[1]) 
    PORT = int(sys.argv[2])

    print(HOST,':',PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))

    server.listen(5) 
    communication_socket, address = server.accept()
    print(f"connected to {address}")

    while True:
        if communication_socket:
            vid = cv2.VideoCapture(int(sys.argv[3]))
            while(vid.isOpened()):
                img,frame = vid.read()

                frame = cv2.resize(frame,None, fx=0.5, fy=0.5)

                a = pickle.dumps(frame)
                message = struct.pack("Q",len(a))+a
                communication_socket.sendall(message)
                frame = cv2.resize(frame,None, fx=2, fy=2)
                cv2.imshow('Sending...',frame)
                key = cv2.waitKey(10) 
                if key ==13:
                    communication_socket.close()
                    break
        break

    server.close()   

if __name__=='__main__':
    main()