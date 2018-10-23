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
    
    # the bottom pixel is is part of the letter
    if ymax.size == 0:
         ymax = np.array([rows.shape[0]-1])
    elif ymax.size < ymin.size: 
        ymax = np.concatenate((ymax,np.array([rows.shape[0]])))
    
    height = ymax-ymin
    too_small = 5 # 
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
        for c1,c2 in col_bounds:
            img = binarized[r1:r2,c1:c2]
            row_bounds = boundaries(img, axis = 0)
            r1_revised, r2_revised = row_bounds[0]
            cropped.append(np.array(orig_img[r1+r1_revised:r1+r2_revised,c1:c2]/255.))
    cv2.destroyAllWindows()
    return cropped
    
def resize_all(imgs,dim):
    imgs2= []
    for img in imgs:
        img = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
        imgs2.append(img)
    return imgs2

def load_data(datasets):
    data = None
    for filename,target_val in datasets:
        az = imread(filename,True)
        imgs = separate(az)
        resized = resize_all(imgs,(5,5))
        resized = np.asarray(resized)
        new_data = resized.reshape((len(imgs), -1))
        n_samples = new_data.shape[0]
        new_target = np.tile(target_val,n_samples/target_val.shape[0])
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

alphabet = np.array(['a','b','c','d','e','f','g','h','o'])

def array2string(array):
    s = ""
    for c in array:
        s = s+c
    return s
    
# Train on all the data in train.jpg
datasets = [("train.jpg", alphabet)]
train_data,train_target = load_data(datasets)

# test with the data in test.jpg
dataset2 = [("test.jpg", np.array(['b','a','d','d','o','g','c','a','f','e']))]
test_data, test_target = load_data(dataset2)

classifier = svm.SVC(gamma= .5) 
#classifier = svm.LinearSVC() # Now a LinearSVC is not as good!
classifier.fit(train_data, train_target)
predicted = classifier.predict(test_data)

predicted = array2string(predicted)
test_target = array2string(test_target)
print "Predicted: ", predicted
print "Truth: ", test_target
