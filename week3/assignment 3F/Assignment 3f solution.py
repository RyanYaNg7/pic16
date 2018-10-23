# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:10:09 2016

@author: matthaberland
"""

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return repr(self.data)
        
class LinkedList():
    def __init__(self,data = None):
        if not data is None:
            self.first = Node(data)
            self.last = self.first
            self.current = self.first
            self.n = 1
        else:
            self.first = None
            self.n = 0
        
    def append(self,data):
        if self.first == None:
            self.__init__(data)
        else:
            self.n += 1
            new_node = Node(data)
            self.last.next = new_node
            self.last = new_node
        
    def __iter__(self):
        return self.LLIter()
    
    def __len__(self):
        return self.n
        
#    def __iter__(self):
#        return self
#        
#    def next(self):
#        if self.current is None:
#            self.current = self.first
#            raise StopIteration()
#        else:
#            temp = self.current
#            self.current = self.current.next
#            return temp.data
    
    def LLIter(self):
        current =  self.first
        while not (current is None):
            yield current.data
            current = current.next
    
    def __add__(self,data):
        b = a[:]
        b.append(data)
        return b

    def __getitem__(self, key):
        if isinstance(key,slice):
            b = LinkedList()
            start = key.start
            stop = key.stop
            step = key.step
            if start == None:
                start = 0
            if step == None:
                step = 1
            if step <= 0:
                raise TypeError("cannot iterate backwards through forward-linked list")
            i = 0
            current = self.first
            while not (current is None or current == stop):
                if ((start <= i < stop) or (start <= i and stop==None)) and ((i-start) % step == 0):
                    b.append(current.data)
                i+=1
                current = current.next
            return b
        else:
            if key > self.n:
                raise IndexError("list index out of range")
            i = 0
            current = self.first
            while not (current is None):
                if i == key:
                    return current.data
                i+=1
                current = current.next
            
    def __setitem__(self,key,val):
        i = 0
        current = self.first
        while not (current is None):
            if i == key:
                current.data = val
                return
            i+=1
            current = current.next
        raise IndexError("list index out of range")
        
    def __str__(self):
        s = "["
        for i in self:
            s = s + str(i) + "->"
        s=s+"]"
        return s

    def __repr__(self):
        return repr(str(self))
        
a = LinkedList(0);
a.append(1)
a.append(2)

print "40 points if this works"
for n in a:
    print n

print ""

print "10 points if this works"
for n in a:
    print n
    
print ""
    
print "15 points if both of these work"
for n in a:
    if n == 2:
        break
    else:
        print n
 
print ""
       
for n in a:
    if n == 2:
        break
    else:
        print n

print ""

a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)
a.append(8)

print ""

print "5 points each"
print len(a)
print str(a)
print repr(a)

print ""

print "5 points each. That is, 10 points if the output of the next line is correct"
a[5] = 20
print a[5]

print ""

print "10 points for correct operation of +"
a+9 # doesn't modify a
print a

print ""

a = a+9 # appends 9 to a
print a
    
print ""

print "10 bonus points if all the following work"
print a[1:5]
print a[1:]
print a[:5]
print a[1::2]
print a[::]

print ""

try:
    print a[999]
except IndexError as e:
    print e
    
print ""

try:
    print a[::-1]
except TypeError as e:
    print e
    
    