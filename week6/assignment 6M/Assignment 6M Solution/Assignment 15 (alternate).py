# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 13:23:57 2016

@author: Matt
"""
from sympy import *

Ie, T, w, t = symbols("Ie, T, w, t")

# Equation 11 as expression
e11 = diff(w(t),t) - T/Ie
# print e11

T0, P = symbols("T0, P")

# Equation 12 as an expression
e12 = T0*(1-w(t)*T0/(4*P))
# print e12

# Substitute 12 into 11
e13 = e11.subs(T,e12)
#print expand(e13)

# Solve 13, general solutions
e14 = dsolve(e13,w(t))
# print expand(e14)

# At t = 0, w = 0; solve for C1
# rhs - http://stackoverflow.com/questions/27930024/how-to-get-either-side-of-equation-in-sympy
w0 = e14.rhs.subs(t,0)
var("C1")
C1sub = solve(w0,C1)
C1sub = C1sub[0] # only one solution; take it out of the list

# Substitute C1 back in
e14 = e14.rhs.subs(C1,C1sub)
# print expand(e14)

# Substitute 14 into 12 and integrate to tf
T = e12.subs(w(t),e14)
var("tf")

# conds - http://stackoverflow.com/questions/15420816/dealing-with-piecewise-equations-returned-by-sympy-integrate
e15 = simplify(integrate(T,(t,0,tf),conds = 'none')) # if we don't pass conds = "none", we get a piecewise
# print e15

# Differentiate 15 and solve for T0
de15 = diff(e15,T0)
e18 = solve(de15,T0)
# print simplify(e18[0]) # this is the negative root
print simplify(e18[1])