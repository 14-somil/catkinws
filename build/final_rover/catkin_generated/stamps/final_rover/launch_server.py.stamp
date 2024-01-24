import subprocess
import time
import sys

commands  = ['roscore',
                'rosrun final_rover server_data.py',
                'rosrun final_rover server_video.py',
                'rosrun final_rover gps.py',
                'rosrun final_rover arm_server.py',
                'rosrun final_rover chassis_server.py',
                'rosrun rosserial_python serial_node.py ' + str(sys.argv[1]) + ' _baud:=57600',
                'rosrun rosserial_python serial_node.py ' + str(sys.argv[2]) + ' _baud:=115200',
                ]

for command in commands:
    subprocess.call(['gnome-terminal', '--', 'bash', '-c', command])
    print('Executing: ', command)
    time.sleep(1)

