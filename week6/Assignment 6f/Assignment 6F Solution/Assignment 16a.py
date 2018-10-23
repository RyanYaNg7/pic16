# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 22:33:49 2016

@author: matthaberland
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

a = mpimg.imread("a.jpg")
# plt.imshow(a)

b = mpimg.imread("b.jpg")
# plt.imshow(b)

# get the center of a
axc = a.shape[0]/2 
ayc = a.shape[1]/2

# get the dimensions of b
bw = b.shape[0]
bh = b.shape[1]

# get the top left corner of the empty spot
tlx = axc - bw/2
tly = ayc - bh/2

# replace the empty spot with b
a[tlx:tlx+bw,tly:tly+bh,:] = b

plt.imshow(a)
mpimg.imsave("c.jpg",a)