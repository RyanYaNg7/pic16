# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 14:36:04 2016

@author: Matt
"""

from imageio import imread # using scipy's imread
import cv2
import numpy as np

def boundaries(binarized,axis):
    # variables named assuming axis = 0; algorithm valid for axis=1
    # [1,0][axis] effectively swaps axes for summing
    rows = np.sum(binarized,axis = [1,0][axis]) > 0
    rows[1:] = np.logical_xor(rows[1:], rows[:-1])
    change = np.nonzero(rows)[0]
    ymin = change[::2]
    ymax = change[1::2]
    height = ymax-ymin
    too_small = 10 # real letters will be bigger than 10px by 10px
    ymin = ymin[height>too_small]
    ymax = ymax[height>too_small]
    return zip(ymin,ymax)

def separate(img):
    orig_img = img.copy()
    pure_white = 255.
    white = np.max(img)
    black = np.min(img)
    thresh = (white+black)/2.0
    binarized = img<thresh
    row_bounds = boundaries(binarized, axis = 0) 
    cropped = []
    for r1,r2 in row_bounds:
        img = binarized[r1:r2,:]
        col_bounds = boundaries(img,axis=1)
        rects = [r1,r2,col_bounds[0][0],col_bounds[0][1]]
        cropped.append(np.array(orig_img[rects[0]:rects[1],rects[2]:rects[3]]/pure_white))
    return cropped

# Example usage
big_img = imread("b.png", as_gray) # flatten = True converts to grayscale
cv2.imshow("b",big_img/255)
cv2.waitKey(1000)
cv2.destroyAllWindows()

imgs = separate(big_img) # separates big_img (pure white = 255) into array of little images (pure white = 1.0)
for img in imgs:
    cv2.imshow("a",img) 
    cv2.waitKey(250)
cv2.destroyAllWindows()