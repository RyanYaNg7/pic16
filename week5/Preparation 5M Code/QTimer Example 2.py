# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 19:36:08 2016

@author: matthaberland
"""

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from sys import stdout

i = 0

def f():
    global i 
    try:
        print "Hello" + str(i) + "!"
        i += 1
        stdout.flush()
    finally:
        QTimer.singleShot(1000, f)
    
def main():
    app = QApplication([])
    f()
    app.exec_()
    
if __name__ == "__main__":
    main()