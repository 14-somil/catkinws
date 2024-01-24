import cv2
import socket 
import struct
import subprocess
import time


def main():
    print('server_video.py')
    HOST = '127.0.0.1'
    PORT = 7070

    print(HOST,':',PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST,PORT))

    server.listen(1)
    communication_socket, address = server.accept()
    print(f"connected to {address}")

    index = 0
    camera_list = []

    try:
        while True:
            cap = cv2.VideoCapture(index)
            
            if not cap.isOpened():
                break
            
            camera_list.append(index)
            cap.release()
            index += 2

        print("Available camera indices:", camera_list)

        for i in camera_list:
            command = 'rosrun final_rover server_open_cam.py ' + HOST + ' ' + str(PORT+i+1)+ ' '+ str(i)
            subprocess.call(['gnome-terminal', '--', 'bash', '-c', command])
        
        command = 'rosrun final_rover server_video_zed.py ' + HOST + ' ' + str(PORT+camera_list[-1]+3)+ ' '+ str(camera_list[-1] + 2)
        subprocess.call(['gnome-terminal', '--', 'bash', '-c', command])
        time.sleep(2)

        camera_list.append(camera_list[-1]+2)

        for i in camera_list:
            message = struct.pack("Q", i)
            communication_socket.sendall(message)

    except:
        pass

    communication_socket.close()


if __name__ == '__main__':
    main()