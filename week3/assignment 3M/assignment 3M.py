# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
from __future__ import division
from fractions import Fraction
import time 
import numbers

#%%
def my_divide1(a, b):
    return [i / j for i,j in zip(a, b)]
    
#%%
def my_divide2(a, b):
    if all(ai != 0 and bi != 0 and (isinstance(bi, numbers.Number)) and (isinstance(ai, numbers.Number)) for ai, bi in zip(a, b)):
        return [i / j for i,j in zip(a, b)]
    else:
        print "Somethings’s wrong with the inputs to my_divide2"
        return []
    
#%%
def my_divide3(a, b):
    try:
        c = [i / j for i,j in zip(a, b)]
        return c
    except:
        print "Somethings’s wrong with the inputs to my_divide3"
        return []
    
#%%
testa = range(1, 1000000)
testb = range(5, 1000004)

begin2 = time.clock()
my_divide2(testa, testb)
end2 = time.clock()
print "time for my_divide2 is {}".format(end2-begin2)

begin3 = time.clock()
my_divide3(testa, testb)
end3 = time.clock()
print "time for my_divide3 is {}".format(end3-begin3)

#my_divide3 is faster

#%%
def my_divide4(a, b):
    try:
        c = [i / j for i,j in zip(a, b)]
        return c
    except ZeroDivisionError as zero:
        print "There is a zero in b"
        return []
    except TypeError:
        print "Non-numeric data detected"
        return []
    except:
        print "Somethings’s wrong with the inputs to my_divide4"
        return []

