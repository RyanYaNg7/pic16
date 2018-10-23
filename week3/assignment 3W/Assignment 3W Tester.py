# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 20:25:46 2016

@author: Matt
"""

# insert this test code into your file or run this file after naming your file MathVector.py and uncommenting the next line
# from MathVector import MathVector
        
u = MathVector(5)
print "u =",
u.print_me()

v = MathVector([2,3,6])
print "v =",
v.print_me()

w = MathVector(1,2,3)
print "w =",
w.print_me()

print v.get_el(2)
v.neg().print_me()
print v.mag()
print v.dot(w)
v.plus(w).print_me()
v.sp(3).print_me()

print v
print v[2]
print -v
print abs(v)
print v*w
print v+w
print v*3
print 3*v