# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows an icon
in the titlebar of the window.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))        
    
        self.show()
        
        
def main():
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
    
if __name__ == '__main__':
    main()