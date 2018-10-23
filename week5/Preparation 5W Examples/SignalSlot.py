import sys

from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QCheckBox, QPushButton, QCalendarWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

class Example(QWidget):
    
    
    def __init__(self):
        super(Example, self).__init__()        
        self.initUI()
        
    def initUI(self):      

        self.slider = QSlider(Qt.Horizontal,self)
        self.slider.valueChanged.connect(self.printSlider)                 
                 
        self.cb = QCheckBox('Show title', self)
        self.cb.move(0,50)  
        self.cb.stateChanged.connect(self.printCB)
        
        self.toggle = QPushButton("Hello", self)
        self.toggle.move(0, 100)
        self.toggle.setCheckable(True)
        self.toggle.toggled.connect(self.printToggle)

        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.move(0,150)
        self.cal.clicked.connect(self.printDate)
        
        
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Animation')
        self.show()

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()
        
    def draw(self, qp):

        qp.setPen(QColor(0, 0, 0))
          
        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(0, 0, self.width(), self.height())
        
    def printSlider(self):
        print self.slider.value()
        
    def printCB(self):
        print self.cb.checkState()
    
    def printToggle(self,onoff):
        print onoff
        
    def printDate(self,date):
        #print date
        print self.cal.selectedDate()
        
             
def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()


if __name__ == '__main__':
    main()