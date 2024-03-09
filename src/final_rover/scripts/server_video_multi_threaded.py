import cv2
import socket 
import struct
import subprocess
import time
import threading

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

                thread_object = []
                for i in camera_list:
                    path = '/home/somil/catkin_ws/src/final_rover/scripts/server_open_cam.py' ##+ HOST + ' ' + str(PORT+i+1)+ ' '+ str(i)
                    thread_object.append(threading.Thread(target=subprocess.run, args=(['python3', path, str(HOST), str(PORT+1+i), str(i)])))

                    thread_object[i].start()
                time.sleep(2)

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
