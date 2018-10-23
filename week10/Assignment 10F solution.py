# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:19:21 2016

@author: matthaberland
"""

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QTextEdit
from PyQt5.QtCore import QTimer # Certain things are only supposed to be done in a PyQt Thread
import threading
import socket
import time


class SocketReader(threading.Thread):
    """A separate Thread to continuously read a connected socket.

        Invokes specified callback function with message when one is received.
        Executing the run() method does not cause it to execute in a separate thread.
        Use inherited start() instead.

        Arguments:
            param1: socket to read
            param2: callback function

    """

    def __init__(self,sock,callback):
        threading.Thread.__init__(self)
        self.sock = sock
        self.callback = callback

    def run(self):
        self.stopped = False
        while(not(self.stopped)):
            message = self.sock.recv(1024)
            self.callback(message)
            time.sleep(0.25)
        self.sock.close()

    def close(self):
        self.stopped = True

class ChatApp(QWidget):
    def __init__(self):
        super(ChatApp,self).__init__()
        self.initUi()
        # initialize network in separate Thread so GUI remains responsive
        threading.Thread(target = self.initNetwork).start()

    def closeEvent(self,e):
        # if server socket is blocking (in a separate thread) due to accept(),
        # connect to it so that it will stop. Otherwise it will continue to
        # hold the specified port indefinitely!
        if self.serverAccepting:
            self.quitNow = True # signal to close thread after accept() finishes
            s = socket.socket()
            s.connect(("localhost",5100))
            s.close()
        # Close any open sockets
        try: self.ss.close() # probably not necessary. closed after accepting.
        except: pass
        try: self.ss2.close() # also probably not necessary; same reason
        except: pass
        try: self.s.close() # important; signals disconnect to other machine
        except: pass
        try: self.s2thread.close() # important; otherwise thread would continue
        except: pass

    def initNetwork(self):
        self.serverAccepting = False
        self.quitNow = False
        # Try being the server. If that fails, be the client.
        try:
            # self.status is used to set label in a QTimer
            self.status = "<attempting to connect>"
            self.beClient()
        except:
            self.status = "<waiting for connection>"
            self.beServer()
        if self.quitNow: return # happens if closeEvent happens prematurely
        # self.s2 is the receiver socket from beClient or beServer
        # self.messageReceiveed is the callback when message comes in
        self.s2thread = SocketReader(self.s2,self.messageReceived)
        self.s2thread.start()
        self.t1.setEnabled(True)
        self.status = "<connected>"

    def messageReceived(self,message):
        if message == "":
            self.status = "<connection closed>"
            self.t1.setEnabled(False)
            self.s.close()
            self.s2thread.close()
        else:
            self.text = "Received: " + str(message)

    def beServer(self):
        self.ss = socket.socket()
        self.ss.bind(("localhost",5100))
        self.ss.listen(1)
        self.serverAccepting = True
        self.s,add = self.ss.accept()
        self.serverAccepting = False

        self.ss.close() # super important!!!
        if self.quitNow: return

        self.ss2 = socket.socket()
        self.ss2.bind(("localhost",5200))
        self.ss2.listen(1)
        self.s2,add = self.ss2.accept()
        self.ss2.close() # super important!!!


    def beClient(self):
        self.s2 = socket.socket()
        self.s2.connect(("localhost",5100))

        time.sleep(0.1)

        self.s = socket.socket()
        self.s.connect(("localhost",5200))


    def initUi(self):
        self.setGeometry(100,100,300,200)
        title = "Chat App"

        self.setWindowTitle(title)
        self.layout = QVBoxLayout()

        self.t1 = QLineEdit(self)
        self.t1.returnPressed.connect(self.sendMessage)
        self.t1.setEnabled(False)

        self.t2 = QTextEdit(self)
        self.t2.setReadOnly(True)

        self.l1 = QLabel("",self)

        self.layout.addWidget(self.t2)
        self.layout.addWidget(self.t1)
        self.layout.addWidget(self.l1)

        self.status = "Welcome to Chat App"
        self.text = ""
        self.qt = QTimer()
        self.qt.timeout.connect(self.updateTextBox)
        self.qt.start(100)

        self.setLayout(self.layout)
        self.show()

    def updateTextBox(self):
        self.l1.setText(self.status)
        if self.text != "":
            self.t2.append(self.text)
            self.text = ""

    def sendMessage(self):
        message = self.t1.text()
        if message != "":
            self.t1.setText("")
            self.s.send(message)
            self.text = "Sent: " + str(message)

def main():

    app = QApplication([])
    w = ChatApp()
    app.exec_()

if __name__=="__main__":
    main()