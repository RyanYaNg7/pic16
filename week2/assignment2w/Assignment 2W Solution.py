# -*- coding: utf-8 -*-
"""
Created on Wed Jan 06 14:19:07 2016

@author: Matt
"""

import time # not necessary

#%% Compact algorithm
s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
ss = s.split()
# ss = s.lower().split() # if we don't want capitalization to make "different" words
start_time = time.clock();
d = {x:ss.count(x) for x in ss}
end_time = time.clock();

print d
w = "dolor"
print "There are ", len(d), " unique words."
print "'",w,"' is found ",d[w], "times"
print "That took",end_time-start_time, "seconds"

#%% Improved algorithm on lorem ipsum

start_time = time.clock();
d = {x:0 for x in ss}
for word in ss:
    if word in d:
        d[word] = d[word]+1
        
end_time = time.clock();


#print d
print "'",w,"' is found ",d[w], "times"
print "That took",end_time-start_time, "seconds"

#%% Improved algorithm on whole book
f = open("863-0.txt")
s = f.read()

ss = s.split()
# ss = s.lower().split() # if we don't want capitalization to make "different" words

start_time = time.clock();
d = {x:0 for x in ss}
for word in ss:
    d[word] = d[word]+1
end_time = time.clock();


#print d
w = "found"
print "'",w,"' is found ",d[w], "times"
print "That took",end_time-start_time, "seconds"

#%% Even a little better algorithm

f = open("863-0.txt")
s = f.read()
ss = s.split()
# ss = s.lower().split() # if we don't want capitalization to make "different" words

start_time = time.clock();
d = {}
for word in ss:
    if word in d:
        d[word] = d[word]+1
    else:
        d[word] = 1
end_time = time.clock();
        
#print d
w = "found"
print "'",w,"' is found ",d[w], "times"
print "That took",end_time-start_time, "seconds"

#%% More "Pythonic" (as you'll see in 2W)

f = open("863-0.txt")
s = f.read()
ss = s.split()
# ss = s.lower().split() # if we don't want capitalization to make "different" words

start_time = time.clock();
d = {}
for word in ss:
    try:
        d[word] = d[word]+1
    except:
        d[word] = 1
end_time = time.clock();
        
#print d
w = "found"
print "'",w,"' is found ",d[w], "times"
print "That took",end_time-start_time, "seconds"