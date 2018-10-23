# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 20:25:46 2016

@author: Matt
"""

class MathVector:
    def __init__(self,*arg):
        if len(arg) == 1: 
            arg = arg[0];
            try:
                self.v = [0 for i in range(arg)]
            except:
                self.v = list(arg)
        else:
            self.v = list(arg)
            
    def __str__(self):
        return str(self.v)
    
    def __repr__(self):
        return repr(self.v)
    
    def __add__(self,other):
        return self.plus(other)
        
    def __neg__(self):
        return self.neg()
    
    def __len__(self):
        return len(self.v)
        
    def __mul__(self,w):
        try:
            return self.dot(w)
        except:
            return self.sp(w)  
            
    def __abs__(self):
        return self.mag()
            
    def __rmul__(self,w):
        return self*w
    
    def __getitem__(self, key):
        return self.get_el(key)
        
    def get_el(self,i):
        try:
            return self.v[i-1]
        except:
            return []
    
    def neg(self):
        return MathVector([-i for i in self.v])
    
    def print_me(self):
        print self.v

    def mag(self):
        return sum((i**2 for i in self.v))**.5
    
    def dot(self,w):
        return sum((i*j for i,j in zip(self.v, w.v)))
        
    def plus(self,w):
        return MathVector([i+ j for i, j in zip(self.v, w.v)])
        
    def sp(self,n):
        return MathVector([n*i for i in self.v])
        
        
        
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