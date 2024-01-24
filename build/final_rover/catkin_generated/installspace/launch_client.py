import subprocess
import time


commands  = ['roscore',
                'rosrun final_rover client_data.py',
                'rosrun final_rover client_video.py',
                'rosrun final_rover arm_client.py',
                'rosrun final_rover chassis_client.py'
]
for command in commands:
    subprocess.call(['gnome-terminal', '--', 'bash', '-c', command])
    print('Executing: ', command)
    time.sleep(1)

