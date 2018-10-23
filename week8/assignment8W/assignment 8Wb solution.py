# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:54:23 2017

@author: Matt
"""
import numpy as np
import scipy as sp
from scipy.optimize import linprog
from pyemd import emd_with_flow
from time import time

n = 100
x = np.random.rand(n)
y = np.random.rand(n)
y = np.sum(x)/np.sum(y)*y
w = sp.linalg.toeplitz(np.arange(n),np.arange(n)).astype(float)

c = w.flatten()

bounds = [(0,None)]*n**2

A1 = np.eye(n).repeat(n,axis = 1)
b1 = x
A2 = np.tile(np.eye(n),(1,n))
b2 = y
A_ub = np.vstack((A1,A2))
b_ub = np.vstack((x.reshape(-1,1), y.reshape(-1,1)))
A_eq = np.ones((1,n**2))
b_eq = min(np.sum(x), np.sum(y))

t0 = time()
sol1 = linprog(c, A_ub, b_ub, A_eq, b_eq, method = "interior-point")
t1 = time()
print "Interior Point: ", t1-t0, "s"

t0 = time()
sol2 = linprog(c, A_ub, b_ub, A_eq, b_eq, method = "interior-point", options ={"sparse":True})
t1 = time()
print "Interior Point, Sparse: ", t1-t0, "s"

t0 = time()
sol3 = linprog(c, A_ub, b_ub, A_eq, b_eq, method = "simplex")
t1 = time()
print "Simplex: ", t1-t0, "s"

e = emd_with_flow(x, y, w)

print "Relative Error: ", np.abs((sol2.fun - e[0])/e[0])