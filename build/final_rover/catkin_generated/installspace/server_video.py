import cv2
import socket 
import struct
import subprocess
import time


def main():
    HOST = '127.0.0.1'
    PORT = 7070

    print(HOST,':',PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST,PORT))

    # server.listen(1)
    # communication_socket, address = server.accept()
    # print(f"connected to {address}")

    index = 0
    camera_list = []

    try:
        while True:
            cap = cv2.VideoCapture(index)
            
            if not cap.isOpened():
                break
            _, frame = cap.read()

            cv2.imshow('frame', frame)
            key = cv2.waitKey()

            if key == ord('y'):
                camera_list.append(index)
                cap.release()
                cv2.destroyAllWindows()
                index += 2
            else :
                cap.release()
                cv2.destroyAllWindows()
                index+=2

        print("Available camera indices:", camera_list)

        while True:
            try:
                
                server.listen(1)
                communication_socket, address = server.accept()
                print(f"connected to {address}")

                for i in camera_list:
                    command = 'python3 /home/riya/catkin_ws/src/final_rover/scripts/server_open_cam.py ' + HOST + ' ' + str(PORT+i+1)+ ' '+ str(i)
                    subprocess.call(['gnome-terminal', '--', 'bash', '-c', command])
                
                # command = 'python3 /home/riya/catkin_ws/src/final_rover/scripts/server_video_zed.py ' + HOST + ' ' + str(PORT+camera_list[-1]+3)+ ' '+ str(camera_list[-1] + 2)
                # subprocess.call(['gnome-terminal', '--', 'bash', '-c', command])
                time.sleep(2)

                # camera_list.append(camera_list[-1]+2)

                for i in camera_list:
                    message = struct.pack("Q", i)
                    communication_socket.sendall(message)

                communication_socket.close()
            
            except:
                communication_socket.close()
                pass

    except:
        pass

    communication_socket.close()


if __name__ == '__main__':
    main()
