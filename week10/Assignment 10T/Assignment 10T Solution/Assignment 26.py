# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 14:36:04 2016

@author: Matt
"""

from scipy.misc import imread
import cv2
import numpy as np
from sklearn import svm

def boundaries(binarized,axis):
    # variables named assuming axis = 0; algorithm valid for axis=1
    # [1,0][axis] effectively swaps axes for summing
    rows = np.sum(binarized,axis = [1,0][axis]) > 0
    rows[1:] = np.logical_xor(rows[1:], rows[:-1])
    change = np.nonzero(rows)[0]
    ymin = change[::2]
    ymax = change[1::2]
    height = ymax-ymin
    too_small = 10 # 
    ymin = ymin[height>too_small]
    ymax = ymax[height>too_small]
    return zip(ymin,ymax)

def separate(img):
    orig_img = img.copy()
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
        cropped.append(np.array(orig_img[rects[0]:rects[1],rects[2]:rects[3]]/255))
    return cropped
    
def resize_all(imgs,dim):
    imgs2= []
    for img in imgs:
        img = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
        imgs2.append(img)
#        cv2.imshow("a",img)
#        cv2.waitKey(1000)
#    cv2.destroyAllWindows()
    return imgs2

def load_data(datasets):
    data = None
    for filename,target_val in datasets:
        az = imread(filename,True)
        imgs = separate(az)
        resized = resize_all(imgs,(5,5))
        resized = np.asarray(resized)
        new_data = resized.reshape((len(imgs), -1))
        new_target = np.ones(new_data.shape[0])*target_val
        if data is None:
            data = new_data
            target = new_target
        else:
            data = np.concatenate((data,new_data))
            target = np.concatenate((target,new_target))
    return data,target
  
def permute(data,target):
    i = np.random.permutation(data.shape[0])
    return data[i,:], target[i]
          
def partition(data, target, p):
    # p is percentage of data to train on
    i = np.random.rand(data.shape[0]) 
    train = i < p
    test = np.logical_not(train)
    train_data, train_target = permute(data[train,:], target[train])
    test_data, test_target = permute(data[test,:], target[test])
#    train_data, train_target = data[train,:], target[train]
#    test_data, test_target = data[test,:], target[test]
    return train_data, train_target, test_data, test_target


datasets = [("a.png", 0),("b.png", 1),("c.png",2)]

data,target = load_data(datasets)

p = 0.9

train_data, train_target, test_data, test_target = partition(data,target,p) 

classifier = svm.SVC(gamma= .5) # Doesn't work with gamma = 0.1!
#classifier = svm.LinearSVC()
classifier.fit(train_data, train_target)

predicted = classifier.predict(test_data)

print "Predicted: ", predicted
print "Truth: ", test_target
print "Accuracy: ", (1. - (1.*np.nonzero(predicted-test_target)[0].size)/test_target.size)*100, "%"