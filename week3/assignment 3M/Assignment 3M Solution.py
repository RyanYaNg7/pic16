# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 16:00:55 2016

@author: matthaberland
"""
from time import clock 
def my_divide1(a,b):
    return [float(x)/y for x,y in zip(a,b)]
    
#a = range(1,10) 
#b = range(2,12) # contains one extra element
#print my_divide1(a,b[:-1])
#print my_divide1(a,b)
#print my_divide1(b,a)

#print ""

import numbers
def my_divide2(a,b):
    z= []
    for x,y in zip(a,b):
        if isinstance(x,numbers.Number) and isinstance(y,numbers.Number) and y != 0:
            z.append(float(x)/y)
        else:
            print "Something is wrong with the inputs to my_divide2"
            z = []
    return z
#print my_divide2(a,b)
#c = [1, 2, 3, "c"]
#print my_divide2(a,c)
#print my_divide2(c,a)
#d = [ 1, 2, 3, 0]
#print my_divide2(a,d)

#print ""

def my_divide3(a,b):
    z= []
    try:
        for x,y in zip(a,b):
            z.append(float(x)/y)
    except:
        print "Something is wrong with the inputs to my_divide2"
        z = [] 
    return z
#print my_divide2(a,b)
#c = [1, 2, 3, "c"]
#print my_divide2(a,c)
#print my_divide2(c,a)
#d = [ 1, 2, 3, 0]
#print my_divide2(a,d)

def time_this(fun, a,b):
    t1 = clock()
    fun(a,b)
    t2 = clock()
    return t2-t1

#a = range(0,1000000); b = range(1,1000001)
##c2 = my_divide2(a,b)
##c3 = my_divide3(a,b)
##print c2 == c3
#d2 = time_this(my_divide2,a,b)
#d3 = time_this(my_divide3,a,b)
#print "my_divide2 takes:", d2, "s"
#print "my_divide3 takes:", d3, "s"
#
#a = range(0,1000000); b = range(1,1000000)+ [0] 
##c2 = my_divide2(a,b)
##c3 = my_divide3(a,b)
##print c2 == c3
#d2 = time_this(my_divide2,a,b)
#d3 = time_this(my_divide3,a,b)
#print "my_divide2 takes:", d2, "s"
#print "my_divide3 takes:", d3, "s"
#
#a = range(0,1000000); b = range(1,1000000)+ ['a']
##c2 = my_divide2(a,b)
##c3 = my_divide3(a,b)
##print c2 == c3
#d2 = time_this(my_divide2,a,b)
#d3 = time_this(my_divide3,a,b)
#print "my_divide2 takes:", d2, "s"
#print "my_divide3 takes:", d3, "s"

def my_divide4(a,b):
    z= []
    try:
        for x,y in zip(a,b):
            z.append(float(x)/y)
    except ZeroDivisionError as e: 
        print "There is at least one zero in the second input:",e
        z = [] 
    except (TypeError,ValueError) as e: 
        print "There is non-numeric input:",e
        z = [] 
    return z
a = [1,2]
b = [2,3]
c = [2,0]
d = [2,'c']
my_divide4(a,b)
my_divide4(a,c)
my_divide4(a,d)
my_divide4(d,a)