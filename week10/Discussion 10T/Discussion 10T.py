# Reference https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html

import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('ballbounce2.MP4')
ball = cv2.imread('ball1.png',0)

h,w = ball.shape[::-1]
i = 1
while(cap.isOpened()):
    ret,frame = cap.read()
       
    # TODO
    # Convert frame to gray colored image


    # TODO
    # Use matchTemplate to find the position of the ball
    # http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html

   
    # TODO
    # Draw rectangle on multiple balls
    # Use http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html


    ##########################################

    cv2.imshow('frame',frame)
    key = cv2.waitKey(10)
    if key == ord('q') or i > 22:
        break
    i+=1
   
cap.release()
cv2.destroyAllWindows()