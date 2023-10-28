from coords2 import get_detected_coordinates
import cv2
import time
from aruco import find_least_pitch_aruco_marker
from aruco_distance import calculate_distance_from_aruco_markers
from beginner_tutorials.srv import angles

first = 0
second = 0
base=0
servo1=90
servo2=90

while(True):
    x_box,y_box=get_detected_coordinates()
    if(x_box!=320 and y_box!=240):
        while(x_box <= 310 or x_box >= 330):
            x_box,y_box=get_detected_coordinates()
            if(x_box < 320):
                #rotate ACW by 1degree
                print("1 deg ACW")
            if(x_box>320):
                #rotate CW by 1degree
                print("1 deg CW")    
            time.sleep(0.069)    
        #coming out from above loop we will have x_box,y_box as 320xY
        #Now we will move it straight back and front for Y
        while(y_box<=230 or y_box>=250):
            x_box,y_box=get_detected_coordinates()
            if(y_box<240):
                #move forward by 1cm
                print("Move fwd by 1cm")
            if(y_box>240):
                #move backward by 1cm
                print("Move back by 1cm")            
            time.sleep(0.069)

        #After this we have the camera at centre of bounding box found and centered as 320x240
        #Now we use aruco marker technique to get the least pitch among all aruco markers detected

        calibration_data_path = "./calib_data/MultiMatrix.npz"  # Update with the path to your calibration data
        least_pitch_id, least_pitch = find_least_pitch_aruco_marker(2, calibration_data_path)

        #Now rotate the suction servo motor by least_pitch

        #Now open the suction pump

        #Now bring the end effector straight downwards by distance units
        calibration_data_path = "./calib_data2/MultiMatrix.npz"  # Update with the path to your calibration data
        distance = calculate_distance_from_aruco_markers(2, calibration_data_path)

        #Now bring back the end effector Up by distance units

        #Rotate the suction servo motor in other direction by least pitch

        #Take the box to the destination by feeding the coordinates of final position(x_box,y_box,z-13)

        #Shut the suction

        #Bring back the end effector to (0,0,0) or (320x240)