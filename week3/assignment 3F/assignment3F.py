# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:36:09 2018

@author: yangzm
"""

class Node():
    def __init__(self, arg1):
        self.data = arg1
        self.next = None
        
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return repr(self.data)
    
    
# =============================================================================
# n = Node(10)
# print str(n)
# print repr(n)
# print n
# =============================================================================

class LinkedList():
    def __init__(self, first_data):
        data1 = Node(first_data)
        self.first = data1
        self.last = data1
        self.n = 1
        self.current_node = data1
        
    def append(self, new_data):
        dataNew = Node(new_data)
        self.last.next = dataNew
        self.last = dataNew
        self.n += 1
    
# =============================================================================
#     def next(self):
#         if self.current_node is None:
#             self.current_node = self.first
#             raise StopIteration
#         else:
#             ret = self.current_node
#             self.current_node = self.current_node.next
#             return ret
# ===========================================================================
    
    def generator(self):
        self.current_node = self.first
        while self.current_node != None:
            yield self.current_node
            self.current_node = self.current_node.next
            
    def __iter__(self):
        return self.generator()
    
    def __len__(self):
        return self.n
    
    def __str__(self):
        s = "["
        for i in self:
            s += str(i.data)+"->"
        s +="]"
        return s
    
    def __repr__(self):
        s = "["
        for i in self:
            s += repr(i.data)+"->"
        s +="]"
        return s
        
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        elif key < 0 or key >= self.n:
            raise KeyError
        else:
            j = 0
            for i in self:
                if j == key:
                    return i
                j += 1
            
            
            
a = LinkedList(0)
a.append(1)
a.append(2)

print a
print a[0]
print a[1]


# =============================================================================
# a = LinkedList(0)
# a.append(1)
# a.append(2)
# for n in a:
#     print n
# 
# for n in a:
#     print n
#     
# for n in a:
#     if n.data == 2:
#         break
#     else:
#         print n
#         
# for n in a:
#     if n.data == 2:
#         break
#     else:
#         print n
# =============================================================================
    