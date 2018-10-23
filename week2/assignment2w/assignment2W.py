#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:09:16 2018

@author: Ryan
"""
#%%
import string
import time

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
#lis = string.split(text, ' ')
lis = text.split()

dic = {s: lis.count(s) for s in lis}

print len(dic.keys())

#%%
newdic = {}
for word in lis:
    if not word in newdic:
        newdic[word] = 1
    else:
        newdic[word] += 1


f = open('863-0.txt')

s = f.read()

lls = s.split()

begin1 = time.clock()
#dicc = {i: lls.count(i) for i in lls}
end1 = time.clock()

print end1-begin1


newdicc = {}
begin2 = time.clock()
for wordd in lls:
    if not wordd in newdicc:
        newdicc[wordd] = 1
    else:
        newdicc[wordd] += 1
end2 = time.clock()
print end2-begin2
print newdicc['found']