# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 22:33:49 2016

@author: matthaberland
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

g = mpimg.imread("g.jpg")
# plt.imshow(a)

h = mpimg.imread("h.jpg")
# plt.imshow(b)

# This is not what we want
# i = g - h
# plt.imshow(i)

# uint8 sounds like an 8 bit integer
# let's find out whether it's signed
print g[0,0,0]
print h[0,0,0]
print h[0,0,0] - g[0,0,0]
# nope it wraps around
# when the difference goes below zero, it wraps around to the maximum (255)
# hence the funny colors

# What we want is for pixels that are similar in color to cancel out
# The difference should be nearly black - [0,0,0]
# But negative numbers are not allowed
# What we really want is the absolute value of the difference
# 1. Convert to data type that allows negative numbers
# 2. Take the absolute value
# 3. Convert back to uint8

g = np.array(g,dtype = int)
h = np.array(h,dtype = int)
i = h-g
print i[0,0,0] # sweet. we've got negatives.
i = abs(i)
i = np.array(i,dtype = "uint8")
plt.imshow(i)
plt.imsave("i.jpg",i)
