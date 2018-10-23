#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 05:19:42 2018

@author: Ryan
"""

import math

def solve(twoFunc, init, tole = 0.0001):
    def is_good(x):  
        return -tole <= twoFunc(init)[0] <= tole
    
    while (not is_good(init)):
        init = float(init) - twoFunc(init)[0]/twoFunc(init)[1]

    return init


#print solve(lambda x: [x**2-1, 2*x], 3, 0.0001)
#print solve(lambda x: [x**2-1, 2*x], -0.5, 0.0001)
#print solve(lambda x: [math.sin(x), math.cos(x)], 2, 0.0001)
#print solve(lambda x: [math.log(x)-1, 1/x], 1.5, 0.0001)

"""
#the initial setting of the function
init_func = lambda x: math.log(x)-1
deriv_func = lambda x: 1/x
tolerance = 0.0001
x = 1.5

#take in a value x and return true if the result of f(x) is with in boundary
def is_good(x):  
    return -tolerance <= init_func(x) <= tolerance

while (not is_good(x)):
    #apply correction
    x = x - init_func(x)/deriv_func(x)
    print x
    
print x
"""