# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 10:18:39 2016

@author: Matt
"""

from PyQt5.QtWidgets import QWidget,QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor

class BareBonesGUI(QWidget):
    def __init__(self):
        super(BareBonesGUI, self).__init__()
        button = QPushButton(self)
        button.setText("Push Me!")
        button.move(0,110)
        button.clicked.connect(self.doSomething)
        
    def doSomething(self,e):
        print "hi!"
#
    def paintEvent(self,e):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255,0,0))
        qp.drawRect(0,0,100,100)
        qp.end()
    
def main():
    app = QApplication([])
    form = BareBonesGUI()
    form.show()
    app.exec_()
    
if __name__ == "__main__":
    main()