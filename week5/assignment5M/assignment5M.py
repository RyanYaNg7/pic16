# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 15:37:35 2018

@author: yangzm
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPalette
from PyQt5.QtCore import Qt, QTimer

class Example(QWidget):
    
    def __init__(self):
        
        super(Example, self).__init__()
        
        self.initUI()
        
        
        
    def initUI(self):
        
        self.d = 30
        self.x = 0
        self.y = 0
        self.v_x = 1
        self.v_y = 1
        self.setGeometry(300, 300, 600, 400)
        
        self.setWindowTitle('Bouncing Ball')
        
        self.show()
        
        
    def animate(self):
        self.checkCollision()
        self.x = self.x + self.v_x
        self.y = self.y + self.v_y
        self.update()
        
        
    def resizeEvent(self, e):
        print "resizing happening!@!!!!!!"
        self.animate()
        
    def checkCollision(self):
        rect = self.geometry()
        left = rect.left()
        right = rect.right()
        bottom = rect.bottom()
        top = rect.top()

        
        if self.x+330 >= right:
            self.x = right-330
            self.v_x = -1
        
        if self.y+330 >= bottom:
            self.y = bottom-330
            self.v_y = -1
        
        if self.x+300 <= left:
            self.x = left-300
            self.v_x = 1
        
        if self.y+300 <= top:
            self.y = top-300
            self.v_y = 1
        
    def paintEvent(self,e):
        
        qp = QPainter()
        qp.begin(self)
        self.changeBackground(qp)
        self.drawCircle(qp)
        qp.end()
        
        
    def changeBackground(self, qp):
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)
        
        
    def drawCircle(self, qp):
        
        qp.setBrush(Qt.red)
        qp.setPen(Qt.red)
        qp.drawEllipse(self.x, self.y, self.d, self.d)
        
        

def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    t = QTimer()
    t.timeout.connect(ex.animate)
    t.setInterval(10)
    t.start()
    app.exec_()

if __name__ == '__main__':
    main()