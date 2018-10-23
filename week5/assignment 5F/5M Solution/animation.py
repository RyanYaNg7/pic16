from design import Ui_mainwidget
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMenuBar, QMenu, QAction, QErrorMessage
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer
from itertools import chain, tee
from csv import reader
class MainWindow(Ui_mainwidget, QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.qt = QTimer(self)
        self.qt.timeout.connect(self.animation_step)
        self.playpause.clicked.connect(self.playpause_callback)
        self.stop.clicked.connect(self.stop_callback)
        self.slider.valueChanged.connect(self.slider_callback)
        self.play = False
        self.timerPeriod = 10
        
        self.data = []
        self.xmin = 0; self.xmax = 1; self.ymin = 0; self.ymax = 1
        self.frame = 0
        self.animation.frame_data = []
        self.animation.connections =  [] # [[0,1],[1,2],[2,0]]
        # self.load_csv()
        
        # Added this manually because I set up the design as a QWidget in
        # Qt Designer. I think you have to start with a QMainWindow to 
        # have a menu bar.
        self.menu = QMenuBar(self)
        self.file = QMenu("File")
        self.open = QAction("Open", self)
        self.open.triggered.connect(self.load_csv)
        self.menu.addMenu(self.file)
        self.file.addAction(self.open)

        self.verticalLayout.setMenuBar(self.menu)
        self.disable()
        
        
    def load_csv(self):        
        try:
            fileName = QFileDialog.getOpenFileName(self, filter = "Comma Separated Value (*.csv)")
            
            f = open(fileName[0])
            r = reader(f)
            ps = []
            for row in r:
                for i in range(0,len(row)/2):
                    p = (float(row[2*i+1]), float(row[2*i+2]))
                    try:
                        ps[i].append(p)
                    except:
                        ps.append([p])
            self.data = ps
            
            self.slider.setMinimum(0)
            self.slider.setMaximum(len(self.data[0])-1)
            
            self.xmin, self.ymin, self.xmax, self.ymax = self.find_min_max(self.data)        
            self.recalc_scale()
            self.set_frame(0)
            self.enable()
        except:
            err = QErrorMessage(self)
            err.showMessage("Error opening " + fileName + ". File must contain two equal-length columns in CSV format.")
    
    def disable(self):
        self.slider.setEnabled(False)
        self.playpause.setEnabled(False)
        self.stop.setEnabled(False)
        
    def enable(self):
        self.slider.setEnabled(True)
        self.playpause.setEnabled(True)
        self.stop.setEnabled(True)
        
    def recalc_scale(self):
#        self.xmax = max(self.xs)
#        self.xmin = min(self.xs)
#        self.ymax = max(self.ys)
#        self.ymin = min(self.ys)
        
        self.xmin_px = self.animation.dot_diameter/2.0
        self.xmax_px = self.animation.width()-self.animation.dot_diameter/2.0-1
        self.ymin_px = self.animation.dot_diameter/2.0+1     
        self.ymax_px = self.animation.height()-self.animation.dot_diameter/2.0-2
        
        xscale = (self.xmax_px - self.xmin_px)/float(self.xmax-self.xmin)
        yscale = (self.ymax_px - self.ymin_px)/float(self.ymax-self.ymin)
        self.scale = min([xscale, yscale])
        
    def find_min_max(self,data):
#        allx = []; ally = []
#        for series in data:
#            allx = allx + [point[0] for point in series]
#            ally = ally + [point[1] for point in series]
#        return min(allx), min(ally), max(allx), max(ally)
        
        allx = (_ for _ in ()); ally = (_ for _ in ());
        for series in data:
            allx = chain(allx, (point[0] for point in series))
            ally = chain(ally, (point[1] for point in series))
        allx1,allx2 = tee(allx); ally1,ally2 = tee(ally)
        return min(allx1), min(ally1), max(allx2), max(ally2)            
            
    def resizeEvent(self,e = None):
        self.recalc_scale()
        self.set_frame(self.frame)
        
    def playpause_callback(self):
        if self.play == False:
            self.play_callback()
        else:
            self.pause_callback()
        
    def set_frame(self,frame):
        if frame >= self.slider.maximum():
            self.pause_callback();
        else:
            self.frame = frame
            self.calc_frame(frame)
            self.slider.setValue(frame)
            self.update()
    
    
    def calc_frame(self, frame):
        self.animation.frame_data = []
        for series in self.data:
            x_px = self.x2px(series[frame][0])
            y_px = self.y2px(series[frame][1])
            self.animation.frame_data.append((x_px,y_px))
        
    def x2px(self, x):
        return self.xmin_px+(x - self.xmin)*self.scale
    def y2px(self, y):
        return self.ymax_px-(y - self.ymin)*self.scale
        
#    def x2px(self, x):
#        return self.xmin_px+(x - self.xmin)/float(self.xmax - self.xmin)*(self.xmax_px - self.xmin_px)
#    def y2px(self, y):
#        return self.ymax_px-(y - self.ymin)/float(self.ymax - self.ymin)*(self.ymax_px - self.ymin_px)
        
    def animation_step(self):
        self.set_frame(self.frame+1)
        
    def stop_callback(self):
        self.pause_callback()
        self.set_frame(0)
    
    def pause_callback(self):
        self.playpause.setText("Play")
        self.qt.stop()
        self.play = False
        
    def play_callback(self):
        self.playpause.setText("Pause")
        self.qt.start(self.timerPeriod)
        self.play = True     
        
    def slider_callback(self):
        self.set_frame(self.slider.value())
        
        
class Animation(QWidget):
    def __init__(self,parent):
        super(Animation,self).__init__(parent)
        self.dot_diameter = 10

    def paintEvent(self,e):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255,255,255))
        qp.drawRect(0,0,self.width()-1,self.height()-1)
        qp.setBrush(QColor(0,0,0))
        for point in self.frame_data:
            x_px = point[0]
            y_px = point[1]
            qp.drawEllipse(x_px - self.dot_diameter/2, y_px-self.dot_diameter/2,self.dot_diameter,self.dot_diameter)
        
        if (len(self.frame_data) > 0) and (len(self.connections) > 0 ) :
            for pair in self.connections:
                p1 = self.frame_data[pair[0]]
                p2 = self.frame_data[pair[1]]
                qp.drawLine(p1[0],p1[1], p2[0], p2[1])
        qp.end()
    
def main():
    app = QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()
 	
if __name__ == "__main__":
    main()