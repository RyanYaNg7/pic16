#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 18:30:23 2018

@author: Ryan
"""
#%%
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
import cv2 as cv

import os
os.chdir("/Users/Ryan/Desktop/week10/Assignment 10T")
os.getcwd()

#%%
def separate(a, thresh_bright, loarea, uparea):
    
    #draw contours
    a_gray = cv.cvtColor(a, cv.COLOR_BGR2GRAY)
    ret, mask_a = cv.threshold(a_gray, thresh_bright, 255, 0)
    a2, contours, hierarchy = cv.findContours(mask_a, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(a, contours, -1, (0,0,255), 1)
    cv.namedWindow('a',cv.WINDOW_NORMAL)
    cv.imshow('a', a)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
        #cleaning and filtering the contours
    sub_image = []
    for contour in contours:
        #calculate the bounding rectangle
        #left = min(contour[:,0,0])#right = max(contour[:,0,0])#top = min(contour[:,0,1])#bottom = max(contour[:,0,1])
        x,y,w,h = cv.boundingRect(contour)
        #calculate the area of the bounding rectangle
        area = w*h
        
        #filter on the area, make a rectangle of the ok's, and put the corresponding sub-image in a list
        if area > loarea and area < uparea:
            cv.rectangle(a, (x, y), (x+w, y+h), (255,255,255), 2)
            sub_image.append(a[y:y+h, x:x+w])
            
    cv.namedWindow('img', cv.WINDOW_NORMAL)
    cv.imshow('img', a)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    sub_image = np.array(sub_image)
    
    for im in sub_image:
        cv.imshow('img', im)
        cv.waitKey(400)
        cv.destroyAllWindows()
    
    def processIm(im):
        im = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        return cv.resize(im, (10,10), fx=0, fy=0, interpolation = cv.INTER_CUBIC)
    
    data = [processIm(im) for im in sub_image]
    data = np.array(data)
    return data

#%%
a = cv.imread('a.png')
data_a = separate(a, 200, 500, 2000)
target_a = np.zeros(len(data_a))
#%% for z
z = cv.imread('z.png')
data_z = separate(z, 150, 0, 3000)
target_z = np.zeros(len(data_z))

#%% for m
m = cv.imread('m.png')
data_m = separate(m, 150, 0, 3000)
target_m = np.ones(len(data_m))

#%% for y
y = cv.imread('y.png')
data_y = separate(y, 150, 1300, 3000)
target_y = np.ones(len(data_y)) + 1

data = np.vstack((data_z, data_m, data_y))
target = np.hstack((target_z, target_m, target_y))

#%% partition training and testing data

def partition(data, target, p):
    l = len(data)
    print l
    n = int(l*p)
    print n
    train_i = np.random.choice(l, n, False)
    all_i = np.arange(l)
    all_i[train_i] = -1
    test_i = all_i[all_i > -1]

    train_data = np.reshape(data[train_i], (n, -1))
    train_target = target[train_i]
    test_data = np.reshape(data[test_i], (l-n, -1))
    test_target = target[test_i]
    
    return train_data, train_target, test_data, test_target

#%% train and test with p = 60%
accuracies = []
clf = svm.LinearSVC()
for p in np.linspace(0.1,1,9, endpoint=False):
    temp_acc = []
    for i in np.arange(10):
        train_data, train_target, test_data, test_target = partition(data, target, p)
        clf.fit(train_data, train_target)
        predict_result = clf.predict(test_data)
        print "Predicted:", predict_result
        print "Truth:", test_target
        accuracy = sum(predict_result==test_target)*1.0/(len(test_data))
        print "Accuracy:", accuracy
        temp_acc.append(accuracy)
    accuracyi = np.mean(temp_acc)
    accuracies.append(accuracyi)
    
plt.hist(accuracies, bins = 10)
plt.xlabel('accuracy level')
plt.ylabel('times in different settings')
plt.show()
plt.plot(np.linspace(0.1,1,9, endpoint=False), accuracies)
plt.xlabel('ratio of data')
plt.ylabel('accuracy level')
plt.show()
#%%
clf2 = svm.SVC(gamma=0.000001)#, kernel='poly')
train_data, train_target, test_data, test_target = partition(data, target, 0.6)
clf2.fit(train_data, train_target)
predict_result = clf2.predict(test_data)
print "Using normal SVC"
print "Predicted:", predict_result
print "Truth:", test_target
accuracy = sum(predict_result==test_target)*1.0/(len(test_data))
print "Accuracy:", accuracy


