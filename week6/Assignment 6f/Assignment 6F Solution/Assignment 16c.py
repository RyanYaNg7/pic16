# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 22:33:49 2016

@author: matthaberland
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as mpcol
import numpy as np

e = mpimg.imread("e.jpg")
# plt.imshow(e)

# The background of the minion is almost pure green
# That is, the green channel is about 255
# Let's find the pixels with very high green and black them out

green = e[:,:,1]
plt.imshow(green)
e[green > 250 ] = 0
# plt.imshow(e)

# hmmm we're getting some undesirable effects
# The green halo is not so bad, but the minion is disappearing
# Yellow has significant red. We can make sure red is also low.
e = mpimg.imread("e.jpg")
red = e[:,:,0]
green = e[:,:,1]
blue = e[:,:,2]
e[np.logical_and(green > 250, red < 10)] = 0
#plt.imshow(e)

# The more effective way to do it would be to change colorspaces
# Let's drop the pixels close to that green hue
e = mpimg.imread("e.jpg")
e2 = mpcol.rgb_to_hsv(e)
hue = e2[:,:,0]
pg = hue[0,0]   # the top left pixel has the hue we're after
print pg        # Note that range is 0-1, not 0-255
r = 0.02        # let's take anything within 2%
mask = np.logical_and(hue > (pg-r), hue < (pg + r))
e[mask] = 0
# plt.imshow(e)

# Finally we need to add this into the image
# Really, we need to REPLACE pixels of the original image with the pixels from this image
# Let's first get the positioning right
d = mpimg.imread("d.jpg")
e = mpimg.imread("e.jpg")
tly = 575
tlx = 275
h = e.shape[0]
w = e.shape[1]
d[tly:tly+h, tlx:tlx+w] = e
# plt.imshow(d)

# OK now let's replace pixels
mask = np.logical_not(mask)
d = mpimg.imread("d.jpg")
e_in_d = d[tly:tly+h, tlx:tlx+w]
e_in_d[mask] = e[mask]
plt.imshow(d)
plt.imsave("f.jpg",d)
