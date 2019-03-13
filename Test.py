import sys
from PyQt5 import QtWidgets, QtCore

from PyQt5.QtWidgets import *
import PyQt5.QtWidgets

class MainWindow(QMainWindow):
    def __init__(self, ):
        super(QMainWindow, self).__init__()
        self.number = 0

        w = QWidget()
        self.setCentralWidget(w)

        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(250, 2000)  #######设置滚动条的尺寸
        # for filename in range(20):
        #     self.MapButton = QPushButton(self.topFiller)
        #     self.MapButton.setText(str(filename))
        #     self.MapButton.move(10, filename * 40)
        self.pic = QVBoxLayout(self.topFiller)
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(0, self.height() * 0.73, self.width(), 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pic.addWidget(self.line)

        ##创建一个滚动条
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topFiller)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        w.setLayout(self.vbox)

        self.statusBar().showMessage("底部信息栏")
        self.resize(300, 500)

if __name__ == "__main__":
    str='20170223'
    str2='6'
    print(str[:4]+'/'+str[4:6]+'/'+str[6:]+' '+str2+':00')
    # app = QApplication(sys.argv)
    # mainwindow = MainWindow()
    # mainwindow.show()
    # sys.exit(app.exec_())
