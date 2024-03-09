import subprocess
import time
import sys

commands  = ['roscore',
                'rosrun final_rover server_data.py',
                'rosrun final_rover server_video.py',
                'rosrun final_rover arm_server.py',
                'rosrun final_rover chassis_server.py',
                'rosrun rosserial_python serial_node.py ' + str(sys.argv[1]) + ' _baud:=57600 __name:=rover_arduino',
                'rosrun rosserial_python serial_node.py ' + str(sys.argv[2]) + ' _baud:=115200 __name:=arm_arduino',
                ]

for command in commands:
    subprocess.call(['gnome-terminal', '--', 'bash', '-c', command])
    print('Executing: ', command)
    time.sleep(1)

