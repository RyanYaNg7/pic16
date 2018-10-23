#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 20:21:17 2018

@author: Ryan
"""

class reverse_iter():
    def __init__(self, alist):
        self.i = len(alist)
        self.list = alist
        
    def __iter__(self):
        return self    #because this is a iterator
    
    def next(self):
        if self.i > 0:
            self.i -= 1
            return self.list[self.i]
        else:
            raise StopIteration()
            
            
x = reverse_iter([1, 2, 3, 4])


print (sum(1.0/x**2 for x in xrange(1, 100000))*6)**0.5
