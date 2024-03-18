from selenium import webdriver
import csv
import os
import pandas as pd
from selenium.webdriver.common.by import By
import time
import random
import rospy
from final_rover.msg import GPS
import threading

rospy.init_node('GPS')
pub = rospy.Publisher('/GPS_client', GPS, queue_size=10)

latitude = 11.004556
longitude = 76.961632
altitude = 425

def publisher():
    global pub, longitude, latitude, altitude

    r=rospy.Rate(100)
    while True:
        msgToSend = GPS(float(latitude), float(longitude), float(altitude))
        pub.publish(msgToSend)
        r.sleep()

publisher_thread = threading.Thread(target=publisher)
publisher_thread.start

def read_csv_values(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)

        return next(reader)

def update_csv_values(file_path, new_values):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_values)

def main():
    print('gps.py')
    file_name= str(random.randint(0, 10000))
    print(file_name)
    # file_name="1"
    csv_file_path = '/home/somil/Documents/'+file_name+'.csv'

    if not os.path.exists(csv_file_path):
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['longitude', 'latitude','altitude(m)'])

    df = pd.read_csv(csv_file_path)

    username = "TeamRoboconSector"
    password = "Gocorona2022"
    url = "https://192.168.1.20/"
    os.environ['PATH'] += r"/home/somil/Downloads"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(3)
    driver.find_element(By.ID,"details-button").click()
    driver.find_element(By.ID,"proceed-link").click()
    driver.find_element(By.NAME,"username").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.NAME,"login").click()

    xpath_expression = "//*[div[1]/div/div[4]/div/div/div[2]/div[4]/div/div/div[3]/div[2]/div[4]/div/div[3]/div/div[1]/div[2]]"

    while(True):
        dynamic_element = driver.find_element(By.XPATH, xpath_expression)
        string = dynamic_element.text
        length = len(string)
        half=int(3*length/4)
        str0=string[half:length]
        index_1=str0.find("LOCATION")
        index_2=str0.find("ALTITUDE")
        str1=str0[index_1+9:index_2-1]

        i=0
        while True:
            if str1[i]==' ':
                break
            else:
                i+=1

        string2=str1[0:i]
        string3=str1[i+3:len(str1)]
        longitude = float(string2)
        latitude = float(string3)
        print(longitude)
        print(latitude)

        index_3=str0.find("Ubiquiti")
        str2=str0[index_2+9:index_3-1]
        j=0
        while True:
            if str2[j]==' ':
                break
            else:
                j+=1
        string3=str2[0:j]
        altitude=float(string3)
        print(altitude)
        new_row = {'longitude': longitude, 'latitude': latitude, 'altitude(m)':altitude}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        df.to_csv(csv_file_path, index=False)

        time.sleep(2)

if __name__ == '__main__':
    main()