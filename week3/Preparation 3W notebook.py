# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:17:57 2016

@author: Matt
"""

# Try running this code one cell at a time in Spyder, predicting the output 
# beforehand and checking yourself. If you have questions about any portion,
# play around with the code to try to figure out what's going on.

class MyClass:
    a = 1;
    
    def __init__(self, x = 2, y = 3):
        MyClass.a = x
        self.b = y
        self.__c = 10
  
    def get__c(self):
        return self.__c
    
    def set__c(self, x):
        self.__c = x

print MyClass.a

#%%

o1 = MyClass();
print MyClass.a
print o1.a

#%%

o2 = MyClass(4);
print MyClass.a
print o1.a
print o2.a

#%%

o3 = MyClass(5,6);
print MyClass.a
print o1.a
print o2.a
print o3.a

#%%

MyClass.a = 7
print o1.a
print o2.a
print o3.a

#%%

o1.a = 8
print MyClass.a
print o1.a
print o2.a
print o3.a

#%%

del o1.a
print o1.a
print o2.a
print o3.a

#%%

print o1.b
print o2.b
print o3.b

#%%

print MyClass.b
#%%

o1.b = 9
print o1.b
print o2.b
print o3.b

#%%  (Optional) Private Variables
# Private variables (those that begin with double underscore) aren't covered
# on the tutorialpoint.com reading. See Chapter 9 of the Python Tutorial
# if you're interested 

print o1.__c

#%%

print o1.get__c()

#%%

o1.__c = 11
print o1.__c
print o1.get__c()
del o1.__c
o1.set__c(12)
print o1.get__c()

#%% Variables only REFER to objects; they do not hold the objects themselves

print ""
print o2.b
o2 = o1
print o2.b
o1.b = 13
print o2.b