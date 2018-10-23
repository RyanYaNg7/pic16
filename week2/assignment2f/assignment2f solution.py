# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:12:29 2016

@author: matthaberland
"""

from time import clock, time

def f(x):
    return x**2

g = lambda x: x**2

N = 10000000

x = range(N)

y = x

t1 = clock()
y = map(f,x)
t2 = clock()
print "map f", t2 - t1

t1 = clock()
y = map(g,x)
t2 = clock()
print "map g", t2 - t1

t1 = clock()
y = [f(i) for i in x]
t2 = clock()
print "listcomp f", t2 - t1

t1 = clock()
y = [g(i) for i in x]
t2 = clock()
print "listcomp g", t2 - t1

t1 = clock()
y = [i**2 for i in x]
t2 = clock()
print "listcomp **2", t2 - t1

y = range(N)
t1 = clock()
for i in x:
    y[i] = f(i)
t2 = clock()
print "for f", t2 - t1

y = range(N)
t1 = clock()   
for i in x:
    y[i] = g(i)
t2 = clock()
print "for g", t2 - t1

y = range(N)
t1 = clock()  
for i in x:
    y[i] = i**2
t2 = clock()
print "for **2", t2 - t1

y = []
t1 = clock()
for i in x:
    y.append(f(i))
t2 = clock()
print "for f append", t2 - t1

y = []
t1 = clock()
for i in x:
    y.append(g(i))
t2 = clock()
print "for g append", t2 - t1

y = []
t1 = clock()
for i in x:
    y.append(i**2)
t2 = clock()
print "for **2 append", t2 - t1

# 1.	When it is possible to re-use an existing list in a for loop, is this faster than appending to an empty one?
# Yes

# 2.	Is it faster to use list comprehension than a for loop when the operation you need to perform requires a single function call?
# Yes. 

# 3.	Under what circumstances might it be faster to use a for loop than list comprehension?
# If the operation to be performed requires multiple lines that can be written out in the for loop without a function call.
 
# 4.	Is it faster to use map than list comprehension when the operation you need to perform requires a single function call?
# Yes

# 5.	Under what circumstances might it be faster to use list comprehension than map?
# If the operation to be performed requires only a single operation that can be written out in the list comprehension without a function call, there is no significant advantage to map.

# 6. Is a lambda function fater than a regular function?
# No, they seem to be able the same.