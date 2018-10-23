# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 07:05:52 2018

@author: Matt
"""
from __future__ import division

import math
import random


def row_length(w):
    bits_per_byte = 8
    bytes_per_instruction = 4
    w_bytes = w/bits_per_byte
    w_instructions = math.ceil(w_bytes/bytes_per_instruction)
    return int(w_instructions*bytes_per_instruction) # row length in bytes

def read_hex(bmp, offset, size):
    return sum(ord(bmp[offset+i])*16**i for i in xrange(0,size))

def load_img(fname):
    with open(fname,'rb') as f:
        bmp = f.read()
    
#    with open('pic_bmp.txt', 'w') as f:
#        f.write(repr(bmp))
    data_begins = read_hex(bmp, 10,4)
    w_pix = read_hex(bmp, 18,4)
    h = read_hex(bmp, 22,4)
    bits_per_pixel =  read_hex(bmp, 28, 2)
    if bits_per_pixel != 1:
        raise ValueError("The file " + fname + " does not contain a monochrome image.")
    
    bmp = bmp[data_begins:] # discard header
    
#    w = row_length(w_pix) # row length in bytes
    w = int(len(bmp)/h)

    assert h*w == len(bmp) # check dimensions
    
    img = [] # could probably be a generator
    for i in range(h-1,0,-1):
        row = bmp[i*w:(i+1)*w]
        row_binary = ""
        for j in row[:]:
            row_binary += format(ord(j), '08b')
        row_binary = row_binary[:w_pix]
        img += [row_binary]
    return img

def randstr(p):
    s = set()
    while len(s)<p:
        s.add(chr(random.randint(ord('!'),ord('~'))))
    return "".join(s)

def img_to_strgm(img, period):
    w_pix = len(img[0])
    n_x = int(w_pix/period + 2)
    x_str = ("X"+" "*(period-1))
    def strgm_generator():
        yield (x_str * n_x + "X")[:w_pix + period]
        for line in img:
            l = randstr(period)
            last = line[0]
            for i in xrange(len(line)):
                if line[i] == '1':
                    if last == '0':
                        l += randstr(1)
                    else:    
                        l += l[i]
                    last = '1'
                else:
                    l += l[i+1]
                    last = '0'
            yield l
    
    return "\n".join(strgm_generator())
        
w = 69
h = 39
period = 10
bmp = 'PIC.bmp'

img = load_img(bmp)
strgm = img_to_strgm(img, period)
print strgm

#with open('PIC_img.txt','w') as f:
#    for line in img:
#        f.write(line)
#        f.write("\n")
#        
#with open('PIC_stereogram.txt','w') as f:
#    f.writelines(strgm)
        