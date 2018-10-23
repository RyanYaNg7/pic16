# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 14:14:31 2016

@author: Matt
"""

import math

def solve(fun, guess, eps = 0.0001):    
    x = guess
    f,df = fun(x)
    
    while(abs(f) > eps):
        delta = -f*1.0/df
        x = x + delta
        f,df = fun(x)

    return x

print solve(lambda x: [x**2-1, 2*x],3,0.0001)
print solve(lambda x: [x**2-1, 2*x],-0.5)
print solve(lambda x: [math.sin(x), math.cos(x)],2)
print solve(lambda x: [math.log(x)-1, 1/x],1.5)
