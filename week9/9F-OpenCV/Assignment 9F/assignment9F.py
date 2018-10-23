#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 23:01:10 2018

@author: Ryan
"""
#%% basic set up
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('frame.png', 0) #grayscale reading
img2 = img.copy()
template = cv.imread('hip.png', 0) #grayscale reading
w, h = template.shape[::-1]

# All the 6 methods for comparion in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

#%% try all six methods on a single picture
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    
    # Apply template matching
    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    cv.rectangle(img, top_left, bottom_right, 255, 3)
    
    plt.subplot(121), plt.imshow(res, cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
    
#%% match hip in the vedio
cap = cv.VideoCapture('RyanRun.MP4')
loop = 0
hip_position = []
prev = (80,0)
while(cap.isOpened()):
    #break out to avoid showing unnecessary video
    loop = loop + 1
    if loop > 1082:
        break
    
    if loop < 870:
        cap.grab()
    else:
        ret, frame = cap.read()
        
        #setting up
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #convert to grayscale
        method = eval('cv.TM_CCORR_NORMED')
        
        # Apply template matching
        res = cv.matchTemplate(gray[max(prev[0]-50, 0):min(prev[0]+50, 480), max(prev[1]-30, 0):min(prev[1]+30, 640)], template, method)
        #res = cv.matchTemplate(gray, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        
        top_left = (max_loc[0] + max(prev[1]-30, 0), max_loc[1]+ max(prev[0]-50, 0))
        prev = (max_loc[1]+ max(prev[0]-50, 0), max_loc[0] + max(prev[1]-30, 0))
        hip_position.append(top_left)
        bottom_right = (top_left[0] + w, top_left[1] + h)
        
        cv.rectangle(gray, top_left, bottom_right, 255, 2)
        cv.imshow('RyanRun', gray)
        k = cv.waitKey(10)
        if k == ord('q'):
            break
        
cap.release()
cv.destroyAllWindows()

#%% plot position of hip
hip_position = np.array(hip_position)
hip_position[:,1] = -hip_position[:,1]
plt.plot(hip_position[:,0], hip_position[:,1])