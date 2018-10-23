# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 08:19:09 2016

@author: matthaberland
"""

from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer

from design import Ui_Form

class ClickDrag(Ui_Form,QWidget):
    def __init__(self, parent = None):
        super(ClickDrag, self).__init__()
        self.setupUi(self)
        self.horizontalSlider.valueChanged.connect(self.slider_callback)
        self.show()
        
    def slider_callback(self):
        try:
            self.widget.l = self.horizontalSlider.value()
            self.widget.update() # not required, but seems to make it smoother
        except:
            pass
        
class Canvas(QWidget):
    
    def __init__(self, parent = None):
        super(Canvas,self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        
        self.x = 0
        self.y = 0
        self.l = 50
        
        self.setGeometry(100,100,600,400)
        self.setWindowTitle("Click Drag")
        self.show()
        
        self.t = QTimer(self)
        self.t.timeout.connect(self.update)
        self.t.start(5)
        
        self.clicked = False
        
        self.mouseX = 0
        self.mouseY = 0
        self.offsetX = 0
        self.offsetY = 0
        
        self.col = QColor(255,0,0)
        
    def paintEvent(self,e):
        qp = QPainter()
        qp.begin(self)
        self.drawSquare(qp)
        qp.end()
        
    def drawSquare(self,qp):
        white = QColor(255,255,255)
        qp.setBrush(white)
        qp.setPen(white)
        qp.drawRect(0,0,self.geometry().width(), self.geometry().height())
        
        qp.setBrush(self.col)
        qp.setPen(self.col)
        self.x = self.mouseX - self.offsetX
        self.y = self.mouseY - self.offsetY
        qp.drawRect(self.x,self.y,self.l,self.l)
        
    def mouseDoubleClickEvent(self,e):
        if self.inSquare(e):
            self.col = QColorDialog.getColor()
            
    def mousePressEvent(self,e):
        self.clicked = self.inSquare(e)
        if self.clicked:
            self.mouseX = e.x()
            self.mouseY = e.y()
            self.offsetX = e.x()-self.x
            self.offsetY = e.y()-self.y
        
    def mouseMoveEvent(self,e):
        if self.clicked:
            self.mouseX = e.x()
            self.mouseY = e.y()
    
    def mouseReleaseEvent(self,e):
        self.clicked = False
        
    def inSquare(self,e):
        return self.x <= e.x() <= self.x+self.l and self.y <= e.y() <= self.y+self.l
        
def main():
    app = QApplication([])
    cd = ClickDrag()
    app.exec_()    
    
if __name__ == "__main__":
    main()