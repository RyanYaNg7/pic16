# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:54:18 2016

@author: haberland
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

## 1
#frame = cv2.imread('frame.png',0)
#hip = cv2.imread('hip.png',0)
#
#method = cv2.TM_CCOEFF_NORMED
#h,w = hip.shape
#res = cv2.matchTemplate(frame,hip,method)
#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#top_left = max_loc
#bottom_right = (top_left[0] + w, top_left[1] + h)
#
#cv2.rectangle(frame,top_left, bottom_right, 255, 3)
#
#cv2.imshow("image",frame)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

## 2
#cap = cv2.VideoCapture('RyanRun.MP4')
#hip = cv2.imread('hip.png',0)
#method = cv2.TM_CCOEFF_NORMED
#h,w = hip.shape
#while (cap.isOpened()):
#    ret,frame = cap.read()
#    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     
#    res = cv2.matchTemplate(frame,hip,method)
#    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#    top_left = max_loc
#    bottom_right = (top_left[0] + w, top_left[1] + h)    
#    cv2.rectangle(frame,top_left, bottom_right, 255, 3)
#    
#    cv2.imshow('frame',frame)
#    key = cv2.waitKey(30)
#    if key == ord('q'):
#        break
#    
#cap.release()
#cv2.destroyAllWindows()

## 3
#cap = cv2.VideoCapture('RyanRun.MP4')
#hip = cv2.imread('hip.png',0)
#method = cv2.TM_CCOEFF_NORMED
#h,w = hip.shape
#i = 1
#while (cap.isOpened()):
#    
#    if i <870:
#        cap.grab()
#        i+=1
#        continue
#    
#    
#    ret,frame = cap.read()
#        
#    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)     
#    res = cv2.matchTemplate(frame,hip,method)
#    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#    top_left = max_loc
#    bottom_right = (top_left[0] + w, top_left[1] + h)    
#    cv2.rectangle(frame,top_left, bottom_right, 255, 3)
#    
#    cv2.imshow('frame',frame)
#    key = cv2.waitKey(30)
#    if key == ord('q') or i > 1082:
#        break
#    i+=1
#    
#cap.release()
#cv2.destroyAllWindows()

## 4
#cap = cv2.VideoCapture('RyanRun.MP4')
#hip = cv2.imread('hip.png',0)
#method = cv2.TM_CCOEFF_NORMED
#h,w = hip.shape
#i = 1
#xs = []
#ys = []
#while (cap.isOpened()):
#    
#    if i <870:
#        cap.grab()
#        i+=1
#        continue
#    
#    
#    ret,frame = cap.read()
#        
#    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)     
#    res = cv2.matchTemplate(frame,hip,method)
#    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#    top_left = max_loc
#    xs.append(top_left[0])
#    ys.append(top_left[1])
#    bottom_right = (top_left[0] + w, top_left[1] + h)    
#    cv2.rectangle(frame,top_left, bottom_right, 255, 3)
#    
#    cv2.imshow('frame',frame)
#    key = cv2.waitKey(30)
#    if key == ord('q') or i > 1082:
#        break
#    i+=1
#    
#cap.release()
#cv2.destroyAllWindows()
#xs = np.array(xs)
#ys = -np.array(ys)
#plt.plot(xs,ys)
#plt.xlabel("X Pixel")
#plt.ylabel("-Y Pixel")
#plt.title("Hip Trace")

## 5
cap = cv2.VideoCapture('RyanRun.MP4')
hip = cv2.imread('hip.png',0)
method = cv2.TM_CCOEFF_NORMED
h,w = hip.shape
i = 1
xs = []
ys = []
last_top_left = None

while (cap.isOpened()):
    
    if i <872:
        cap.grab()
        i+=1
        continue
    
    ret,frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    view = frame
    
    if last_top_left is None: # if this is the first frame
        res = cv2.matchTemplate(frame,hip,method) # search the whole frame
    else: # otherwise
        # create a view around the previous position of the template
        last_row = last_top_left[1]
        last_col = last_top_left[0]
        min_row = max(last_row-h,0)
        min_col = max(last_col-w,0)
        max_row = min(last_row+2*h,frame.shape[0])
        max_col = min(last_col+2*w,frame.shape[1])
        view = frame[min_row:max_row,min_col:max_col]
        res = cv2.matchTemplate(view,hip,method) #find the template in the view
        
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    if last_top_left is not None: # if the view was searched, coordinates need to be adjusted
        top_left = (top_left[0]+min_col, top_left[1]+min_row)
    last_top_left = top_left
    xs.append(top_left[0])
    ys.append(top_left[1])
    bottom_right = (top_left[0] + w, top_left[1] + h)    
    cv2.rectangle(frame,top_left, bottom_right, 255, 3)
    
#    cv2.imshow('frame',view)
#    key = cv2.waitKey(0)
#    if key == ord('q'):
#        break
    if i > 1082:
        break
    i+=1
    
cap.release()
#cv2.destroyAllWindows()
xs = np.array(xs)
ys = -np.array(ys)
plt.plot(xs,ys)
plt.xlabel("X Pixel")
plt.ylabel("-Y Pixel")
plt.title("Hip Trace")