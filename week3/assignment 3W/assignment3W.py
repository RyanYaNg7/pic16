#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 11:08:14 2018

@author: Ryan
"""
import numbers

class MathVector():
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            self.vec = [0 for i in xrange(args[0])]
        elif len(args) == 1 and isinstance(args[0], list):
            self.vec = args[0]
        elif isinstance(args, tuple):
            self.vec = list(args)
        else:
            print "there is an error with your argument"
            raise 

    def get_el(self, index):
        return self.vec[index-1]

    def neg(self):
        return MathVector([-i for i in self.vec])

    def mag(self):
        return sum(i**2 for i in self.vec)**0.5

    def dot(self, other):
        return sum(x*q for x,q in zip(self.vec, other.vec))

    def plus(self, other):
        return MathVector([x+y for x,y in zip(self.vec, other.vec)])

    def sp(self, scalar):
        return MathVector([scalar*i for i in self.vec])

    def print_me(self):
        print self.vec
        

    def __neg__(self):
        return self.neg()

    def __abs__(self):
        return self.mag()
    
    def __add__(self, other):
        return self.plus(other)
    
    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return self.sp(other)
        else:
            return self.dot(other)
        
    def __getitem__(self, key):
        return self.get_el(key)
    
    def __rmul__(self, other):
        if isinstance(other, numbers.Number):
            return self.sp(other)
        else:
            return self.dot(other)
        
    def __str__(self):
        self.print_me()
        return ""

    
    
#%%
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
                
