# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:04:21 2016

@author: matthaberland
"""

from PyQt4.QtGui import QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout
from PyQt4 import QtCore
from sympy import *
import re

def process_command(command):
    command = re.sub(r"(\d+)\/(\d+)", r"Rational(\1,\2)", command)
    command = re.sub(r"differentiate|derivative", r"diff", command)
    command = re.sub(r"int\(|integral\(", r"integrate(", command)
    command = re.sub(r"sol\(|solution\(", r"solve(", command)
    command = re.sub(r"\^", r"**", command)
    command = re.sub(r"solve\(([^=]*)=([^=]*)\s*,", r"solve(\1-\2,",command)
    return command
    
def process_result(result):
    result = re.sub(r"\*\*", r"^", result)
    return result
    
class MathApp(QWidget):
    def __init__(self):
        super(MathApp,self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.layout()
        self.connections()
        self.show()
        
    def layout(self):
        self.l1 = QLabel("Enter math command:")
        self.t1 = QLineEdit()
        self.l2 = QLabel("Result:")
        self.l3 = QLabel(" ")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.l1)
        self.layout.addWidget(self.t1)
        self.layout.addWidget(self.l2)
        self.layout.addWidget(self.l3)
        self.setLayout(self.layout)
    
    def connections(self):
        self.t1.returnPressed.connect(self.text_callback)
    
    def text_callback(self):
        command = self.t1.text()
        try:
            result= str(sympify(process_command(command)))
            result = process_result(result)
        except:
            result = "Invalid command" 
        self.l3.setText(result)

def main():
    app = QApplication([])
    w = MathApp()
    app.exec_()
    
if __name__ == "__main__":
    main()
    
