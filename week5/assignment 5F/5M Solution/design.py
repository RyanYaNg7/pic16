# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainwidget(object):
    def setupUi(self, mainwidget):
        mainwidget.setObjectName("mainwidget")
        mainwidget.resize(457, 350)
        self.verticalLayout = QtWidgets.QVBoxLayout(mainwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.animation = Animation(mainwidget)
        self.animation.setObjectName("animation")
        self.verticalLayout.addWidget(self.animation)
        self.widget = QtWidgets.QWidget(mainwidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playpause = QtWidgets.QPushButton(self.widget)
        self.playpause.setEnabled(True)
        self.playpause.setMaximumSize(QtCore.QSize(40, 16777215))
        self.playpause.setObjectName("playpause")
        self.horizontalLayout.addWidget(self.playpause)
        self.stop = QtWidgets.QPushButton(self.widget)
        self.stop.setEnabled(True)
        self.stop.setMaximumSize(QtCore.QSize(40, 16777215))
        self.stop.setObjectName("stop")
        self.horizontalLayout.addWidget(self.stop)
        self.slider = QtWidgets.QSlider(self.widget)
        self.slider.setEnabled(True)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.horizontalLayout.addWidget(self.slider)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(mainwidget)
        QtCore.QMetaObject.connectSlotsByName(mainwidget)

    def retranslateUi(self, mainwidget):
        _translate = QtCore.QCoreApplication.translate
        mainwidget.setWindowTitle(_translate("mainwidget", "Point Animation"))
        self.playpause.setText(_translate("mainwidget", "Play"))
        self.stop.setText(_translate("mainwidget", "Stop"))

from animation import Animation
