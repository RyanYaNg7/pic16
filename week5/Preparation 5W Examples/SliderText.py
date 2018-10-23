#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we connect a signal
of a QtGui.QSlider to a slot 
of a QtGui.QLCDNumber. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLineEdit
from PyQt5.QtCore import Qt

class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.valueChanged.connect(self.syncText)
        self.sld.move(25,25)
        self.sld.setMinimumWidth(200)
        
        self.text = QLineEdit(self)
        self.text.textChanged.connect(self.syncSlider)
        self.text.move(25, 50)
        self.text.setMinimumWidth(200)
        
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()
        
    def syncText(self,val):
        self.text.setText(str(val))
        
    def syncSlider(self,valstr):
        try:
            val = int(valstr)
        except:
            val = 0
        val = max(self.sld.minimum(), val)
        val = min(self.sld.maximum(), val)
        self.sld.setValue(val)

        
def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()

if __name__ == '__main__':
    main()
