from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtGui import QPainter, QColor

class Example(QWidget):
    
    
    def __init__(self):
        super(Example, self).__init__()        
        self.initUI()
        
    def initUI(self):      
         
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Animation')
        self.show()


    def draw(self, qp):
        qp.setPen(QColor(0, 0, 0))
        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(0, 0, self.width(), self.height())
        
    def mouseDoubleClickEvent(self,e):
        print "Mouse Double Click"
        
    def mousePressEvent(self,e):
        print "Mouse Press"
        print e.x()
        print e.y()
        print e.button()
        
    def mouseReleaseEvent(self,e):
        print "Mouse Release"
    
    def keyPressEvent(self,e):
        print "Key Press"
        print e.key()
        print e.text()
        
    def keyReleaseEvent(self,e):
        print "Key Release" 
        
    def leaveEvent(self,e):
        print "Mouse Left"

    def enterEvent(self,e):
        print "Mouse Entered"

             
def main():
    
    app = QApplication([])
    ex = Example()
    app.exec_()


if __name__ == '__main__':
    main()