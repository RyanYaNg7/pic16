# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program centers a window 
on the screen. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.resize(250, 150)
        self.center()
        
        self.setWindowTitle('Center')    
        self.show()
        
        
    def center(self):
        
        qr = self.frameGeometry()
        window_width, window_height = qr.width(), qr.height()
        
        cp = QDesktopWidget().availableGeometry() 
        screen_width, screen_height = cp.width(), cp.height()
        
        self.move(screen_width/2-window_width/2, screen_height/2 - window_height/2)
        
def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
    
if __name__ == '__main__':
    main()