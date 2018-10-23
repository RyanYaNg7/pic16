# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:45:07 2016

@author: haberland
"""

import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt

m = 1.
l = 1.
g = 1.
p = (m,l,g)

def dydt(y,t,p):
    m = p[0] # not needed, it turns out
    g = p[1]
    l = p[2]
    th = y[0]
    dth = y[1]
    ddth = -g/l*np.sin(th)
    dy = [dth, ddth]
    return dy
# Alternatively
# dydt = lambda y,t,p: [y[1], -p[1]/p[2]*np.sin(y[0])]
    

t = np.linspace(0,10,100)
y0 = [1,0]
y = spint.odeint(dydt,y0,t,args=(p,))
plt.rc('text',usetex=True)
plt.plot(t,y[:,0])
plt.xlabel(r"time $t$ (s)")
plt.ylabel(r"angle $\theta$ (rad)")
