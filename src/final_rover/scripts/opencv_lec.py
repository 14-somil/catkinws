import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

# img = cv2.imread('/home/somil/Test_codes/data/messi5.jpg',0)
# cv2.imshow('frame', img)
# k=cv2.waitKey()
# cv2.destroyAllWindows()
# cv2.imwrite('../test1.png', img)
# print(img)

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame=cap.read()

#     if ret ==True:
#         frame = cv2.putText(frame, str(time.time()), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 1)
#         cv2.imshow('frame', frame)
#         key = cv2.waitKey(1)
#         if key == 13:
#             break

#     else:
#         break

# cap.release()
# cv2.destroyAllWindows()


img = cv2.imread('/home/somil/Test_codes/data/sudoku.png',0)

_ , th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)


cv2.waitKey(0)
cv2.destroyAllWindows()













































# cap = cv2.VideoCapture('/home/somil/Test_codes/data/Megamind.avi')

# while(True): # we can also write while(cap.isOpened()) this will give true if file exist 
#     ret, frame=cap.read()

#     if ret==True:

#         cv2.imshow('frame', frame)
#         key=cv2.waitKey(1)
#         if key == 13:
#             break
#     else:
#         break

# cap.release() 
# cv2.destroyAllWindows()

