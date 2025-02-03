#crosshair base 

#python crosshair overlay

#a crosshair overlay I made for myself

import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QPainterPath, QRegion

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
        QtCore.QSize(20, 20)
         # Calculate screen geometry to center the window
        screen_geometry = QtWidgets.QApplication.primaryScreen().availableGeometry()
        x = (screen_geometry.width() - 20) // 2 
        y = (screen_geometry.height() - 20) // 2         
        # Set geometry to center the window
        self.setGeometry(x, y, 20, 20)

        self.setStyleSheet("background-color: rgb(243, 248, 108);")
        
        path = QPainterPath()
        path.addEllipse(0, 0, 15,15)  
        region = QRegion(path.toFillPolygon().toPolygon())  
        self.setMask(region)  
        


    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == 80:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    app.exec_()
