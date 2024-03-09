import socket 
import subprocess
import struct
import sys

def main():
    print('client_video.py')
    HOST = '192.168.1.22'
    PORT = 7070

    print(HOST,':',PORT)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    camera = []

    data = b""
    payload_size = struct.calcsize("Q")

    while True:
        while len(data) < payload_size:
            packet = client.recv(4*1024)
            if not packet: break
            data+=packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        temp = struct.unpack("Q",packed_msg_size)[0]
        try:
            print(temp)
            command = 'rosrun final_rover client_open_cam.py '+ HOST + ' ' + str(PORT+1+int(temp))+ ' ' +str(temp)
            subprocess.call(['gnome-terminal', '--', 'bash', '-c', command])
        except:
            break

    client.close()

if __name__ == '__main__':
    main()
