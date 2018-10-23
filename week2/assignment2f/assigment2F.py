#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 20:32:52 2018

@author: Ryan
"""

import time

def f(x):
    return x**2

g = lambda x : x**2

x = range(10000)
s = range(10000)
y = []
z = []

"""
for i in x:
    y.append(f(i))
"""

"""
for i in x:
    y.append(g(i))
"""

"""
for i in x:
    y.append(i**2)
"""

"""
for i in s:
    y[i] = f(y[i])
"""

"""
l = [i**2 for i in x]
"""

"""
l = map(g, x)
"""


for j in range(1000):
    begin = time.clock()
    #put the correspoding code in here
    end = time.clock()
    z += [end - begin]

print sum(z)/float(len(z))

""" 
each answer is the result of average from 1000 times of execution

1. measure the execution time of creating a large list with for loop, with f function
    N = 10000  execution time = 0.004752446 

2. using the lambda functino g
    N = 10000  execution time = 0.004741955
    
3. i**2 inside the loop
    N = 10000  execution time = 0.003444612
    
4. first initialize y to range(N) then square the elements in-place, with f function
    N = 10000  execution time = 0.004780582
    
5. Use list comprehension to generate the list of squares, using i**2
    N = 10000  execution time = 0.002406461
    
6. Use map to generate the list of squares, using lambda function g
    N = 10000  execution time = 0.002439596
    
    
    
    
Questions:
1. When it is possible to re-use an existing list in a for loop, is this faster than appending to an empty one?
    From case 1 and 4, we see that when we use for loop and f function to create the list, there is no difference on the execution time between two ways.

2. Is it faster to use list comprehension than a for loop when the operation you need to perform requires a single function call?
    From case 3 and 5, we can say that using list comprehension is faster than a for loop when operation can be performed in a single functoin call.

3. Under what circumstances might it be faster to use a for loop than list comprehension?
    --------------------

4. Is it faster to use map than list comprehension when the operation you need to perform requires a single function call?
    According to case 6 and 6, the answer is no.

5. Under what circumstances might it be faster to use list comprehension than map?
    --------------------

6. Is a lambda function faster than a regular function?
    From case 1 and 2, a lambda function is not faster than a regular function.
    
"""