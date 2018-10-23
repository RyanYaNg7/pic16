# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
import sys
import csv


#make a list of rows that only contain the correct numbers
regex = r"(\d{3})\D*(\d{3})\D*(\d{4})"
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    data = []
    for row in reader:
        match = re.search(regex, row[1])
        if match is None:
            continue
        number = "(%s) %s-%s" % (match.group(1), match.group(2), match.group(3))
        data.append([row[0], number])



regex = r"((\w+) ([A-Z]\.) (\w+))|((\w+)\, (\w+) ([A-Z]\.))|((\w+) (\w+))|((\w+)\, (\w+))"
finalList = []
finalList.append(["First", "M.I.", "Last", "Number"])
for i in data:
    match = re.search(regex, i[0])
    if match.group(1) is None:
        pass
    else:
        finalList.append([match.group(2), match.group(3), match.group(4), i[1]])
        continue
    if match.group(5) is None:
        pass
    else:
        finalList.append([match.group(7), match.group(8), match.group(6), i[1]])
        continue
    if match.group(9) is None:
        pass
    else:
        finalList.append([match.group(10), None, match.group(11), i[1]])
        continue
    if match.group(12) is None:
        pass
    else:
        finalList.append([match.group(14), None, match.group(13), i[1]])
        

with open('mydata.csv', 'w') as f:
    w = csv.writer(f, delimiter = ',')
    for row in finalList:
        w.writerow(row)    



        #0 all
        #1 234  first mid last
        #5 678  last first mid
        #9 10 11  first last
        #12 13 14  last first