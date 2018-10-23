# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 17:44:13 2016

@author: matthaberland
"""

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import QTimer

class BouncingBall(QWidget):
    def __init__(self):
        super(BouncingBall,self).__init__()
        self.x = 0
        self.y = 0
        self.d = 30
        self.vx = 2
        self.vy = 2
        self.w = 600
        self.h = 400
        self.T = 10
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100,100,self.w,self.h)
        self.show()
        
        self.t = QTimer()
        self.t.timeout.connect(self.animate)
        self.t.start(self.T)
        self.animate()
        
    def paintEvent(self,e):
        qp = QPainter()
        qp.begin(self)       
        self.drawFrame(qp)
        qp.end()
    
    def drawFrame(self,qp):
        white = QColor(255,255,255)
        red = QColor(255,0,0)
        qp.setBrush(white)
        qp.setPen(white)
        
#        qp.drawRect(0,0,self.w,self.h)
        # The following gets the present geometry. 
        # Good if the user resizes the window.
        g = self.geometry()
        qp.drawRect(0,0,g.width(),g.height())
        
        qp.setBrush(red)
        qp.setPen(red)
        qp.drawEllipse(self.x,self.y,self.d,self.d)
        
    def animate(self):
        self.x+=self.vx
        self.y+=self.vy
        self.checkCollision()
        self.update()
        
    def checkCollision(self):
        g = self.geometry()
#        # More compact but ball can get stuck if user resizes
#        if self.x  <= 0 or self.x + self.d >= g.width():
#            self.vx *= -1
#        if self.y <= 0 or self.y + self.d >= g.height():
#            self.vy *= -1
        if self.x  <= 0: self.vx = abs(self.vx)
        if self.x + self.d >= g.width(): self.vx = -abs(self.vx)
        if self.y <= 0: self.vy = abs(self.vy)
        if self.y + self.d >= g.height(): self.vy = -abs(self.vy)
            

def main():
    app = QApplication([])
    b = BouncingBall()
    app.exec_()
    
if __name__ == "__main__":
    main()

    
            