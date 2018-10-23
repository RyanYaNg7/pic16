#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 19:19:42 2018

@author: Ryan
"""

import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt

p1 = 1
p2 = 1
p3 = 1

def f(y, t, p1, p2, p3):
    dy = np.zeros(len(y))
    dy[0] = y[1]
    dy[1] = -p2 * np.sin(y[0]) / p3
    return dy

f1 = lambda y, t: f(y, t, p1, p2, p3)
t = np.linspace(0, 10, 100)
y = spint.odeint(f1, np.array([1, 0]), t)

print y.shape

plt.plot(t, y[:,0])