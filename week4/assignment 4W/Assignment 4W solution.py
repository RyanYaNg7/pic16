# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 09:26:24 2016

@author: matthaberland
"""

import csv
import re

re_phone = r"\(?(\d{3})\)?[-\. ]?(\d{3})[-\. ]?(\d{4})"
re_name = r"(\w+), (\w+) ?(\w\.)?|(\w+) (\w\.)? ?(\w+)"

new_list = []

with open("data.csv","r") as f:
    r = csv.reader(f)
    for row in r:        
        phonelist = re.findall(re_phone,row[1])
        if phonelist == []: continue
        phonelist = phonelist[0]
        phone = "(" + phonelist[0] + ") " + phonelist[1] + "-" + phonelist[2]
        
        namelist = re.findall(re_name,row[0])
        namelist= namelist[0]
        first = namelist[1] or namelist[3]
        middle = namelist[2] or namelist[4]
        last = namelist[0] or namelist[5]
        
#        if middle: middle = middle +  " "
#        name = first + " " + middle + last
        
        new_list.append((first,middle,last,phone))
        
with open("data2.csv","wb") as f:
    w = csv.writer(f,delimiter = ",")
    w.writerow(("First","M.I.","Last","Phone"))
    for row in new_list:
        w.writerow(row)
