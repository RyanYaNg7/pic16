# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

os.chdir('/Users/Ryan/Desktop/Assignment 6f')
img1 = mpimg.imread('a.jpg')
img2 = mpimg.imread('b.jpg')

copy = img1.copy()
copy[250:650, 100:500, :] = img2
plt.imshow(copy)
plt.show()
c = Image.fromarray(copy)
c.save('c.jpg')

#%%
img_g = mpimg.imread('g.jpg')
img_h = mpimg.imread('h.jpg')

copy_g = img_g.astype('float64') / 255
copy_h = img_h.astype('float64') / 255

subtr1 = copy_g - copy_h
subtr2 = copy_h - copy_g

# =============================================================================
# subtr1[subtr1 < 0] = 0
# subtr2[subtr2 < 0] = 0
# subtr = subtr1 + subtr2
# =============================================================================

subtr1[subtr1 < 0] = -subtr1[subtr1 < 0]
subtr = (subtr1 * 255).astype('uint8')
plt.imshow(subtr)
plt.show()
i = Image.fromarray(subtr)
i.save('i.jpg')


#%%
img_d = mpimg.imread('d.jpg')
img_e = mpimg.imread('e.jpg')

copy_d = img_d.copy()
copy_e = img_e.copy()

copy_e[np.logical_and(copy_e[:,:,0]<140, copy_e[:,:,1]>150, copy_e[:,:,2]<250)] = 0
plt.imshow(copy_e)
plt.show()

copy_d[575:736, 250:415, :][copy_e!=0] = copy_e[copy_e != 0]
plt.imshow(copy_d)
plt.show()
f = Image.fromarray(copy_d)
f.save('f.jpg')