'''图标'''
import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import *#QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter


class MyWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MyWindow,self).__init__(parent)
        self.width = 900  # 图片宽度
        self.height = 600  # 图片高度
        self.pic_x = 30
        self.pic_y = 100  # 图片起始点
        self.setWindowTitle("Cement Kiln")
        self.widget=QWidget()
        self.messageView=QTextBrowser()
        self.functionList=QListWidget()
        self.boxList=QListWidget()
        self.messageSplitter=QSplitter(Qt.Vertical)
        self.messageSplitter.addWidget(self.messageView)
        self.messageSplitter.addWidget(self.functionList)
        self.messageSplitter.addWidget(self.boxList)
        self.mainSplitter=QSplitter(Qt.Horizontal)
        self.mainSplitter.addWidget(self.widget)
        self.mainSplitter.addWidget(self.messageSplitter)
        self.setCentralWidget(self.mainSplitter)

        l1=QtWidgets.QLabel(self.widget)
        l1.setPixmap(QtGui.QPixmap('picture\yaoxt.png').scaled(self.width, self.height, aspectRatioMode=Qt.KeepAspectRatio))  # 改变图片大小.scaled(self.width, self.height, aspectRatioMode=Qt.KeepAspectRatio)
        pic_size=QtGui.QPixmap('picture\yaoxt.png')
        self.change_x=self.width/pic_size.width()#由于图片显示保持比例，故放缩比例只需要计算x方向即可
        l1.move(self.pic_x,self.pic_y)  # 改变图片位置
        l1.setStyleSheet("QLabel{border:2px solid rgb(0, 255, 0);}")  # Label周围显示边框
        self.resize(1200,800)
        self.showMaximized()


    def mousePressEvent(self, QMouseEvent):
        globalPos = self.mapToGlobal(QMouseEvent.pos())
        print("The mouse is at (%d,%d)" % (QMouseEvent.pos().x(), QMouseEvent.pos().y()))
        x=QMouseEvent.pos().x()-self.pic_x
        y=QMouseEvent.pos().y()-self.pic_y
        ratio_x=self.change_x
        if x>34*ratio_x and x<88*ratio_x and y>28*ratio_x and y<73*ratio_x:
            self.messageView.setText("1级旋风筒")
            '''painter = QPainter(self)
            painter.setBrush(Qt.blue)
            painter.setPen(Qt.blue)
            painter.drawRect(72,136,140,189)'''
            #self.update()
        if x > 101*ratio_x and x < 155*ratio_x and y > 65*ratio_x and y < 109*ratio_x:
            self.messageView.setText("2级旋风筒")
        if x > 34*ratio_x and x < 88*ratio_x and y > 105*ratio_x and y < 149*ratio_x:
            self.messageView.setText("3级旋风筒")
        if x > 102*ratio_x and x < 155*ratio_x and y > 143*ratio_x and y < 189*ratio_x:
            self.messageView.setText("4级旋风筒")
        if x > 34*ratio_x and x < 88*ratio_x and y > 196*ratio_x and y < 242*ratio_x:
            self.messageView.setText("5级旋风筒")
        if x > 146*ratio_x and x < 204*ratio_x and y > 197*ratio_x and y < 241*ratio_x:
            self.messageView.setText("分解炉")
        if x > 218*ratio_x and x < 251*ratio_x and y > 272*ratio_x and y < 322*ratio_x:
            self.messageView.setText("窑尾")
        if x > 252*ratio_x and x < 290*ratio_x and y > 272*ratio_x and y < 321*ratio_x:
            self.messageView.setText("预热带")
        if x > 297*ratio_x and x < 345*ratio_x and y > 272*ratio_x and y < 322*ratio_x:
            self.messageView.setText("分解带")
        if x > 352*ratio_x and x < 393*ratio_x and y > 272*ratio_x and y < 322*ratio_x:
            self.messageView.setText("烧成带")
        if x > 399*ratio_x and x < 440*ratio_x and y > 272*ratio_x and y < 322*ratio_x:
            self.messageView.setText("冷却带")
        if x > 426*ratio_x and x < 479*ratio_x and y > 272*ratio_x and y < 322*ratio_x:
            self.messageView.setText("窑头")
        if x > 499*ratio_x and x < 540*ratio_x and y > 298*ratio_x and y < 323*ratio_x:
            self.messageView.setText("篦冷机1段")
        if x > 545*ratio_x and x < 583*ratio_x and y > 298*ratio_x and y < 323*ratio_x:
            self.messageView.setText("篦冷机2段")
        if x > 588*ratio_x and x < 633*ratio_x and y > 298*ratio_x and y < 323*ratio_x:
            self.messageView.setText("篦冷机3段")
        if x > 370*ratio_x and x < 427*ratio_x and y > 121*ratio_x and y < 164*ratio_x:
            self.messageView.setText("高温风机")
        if x > 426*ratio_x and x < 479*ratio_x and y > 345*ratio_x and y < 369*ratio_x:
            self.messageView.setText("煤粉仓")

        '''def event(self, event):
        if event.type() == QEvent.KeyPress and \
                event.key() == Qt.Key_Tab:
            self.key = QString("Tab captured in event()")
            self.update()
            return True
        return QWidget.event(self, event)'''
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            settings = QSettings()
            settings.setValue("MainWindow/Size", QVariant(self.size()))
            settings.setValue("MainWindow/Position", QVariant(self.pos()))
            settings.setValue("mainSplitter", QVariant(self.mainSplitter.saveState()))
            settings.setValue("messageSplitter", QVariant(self.messageSplitter.saveState()))
            event.accept()
        else:
            event.ignore()

    def paintEvent(self, QPaintEvent):

        if False:
            painter = QPainter(self)
            painter.setBrush(Qt.white)
            painter.setPen(Qt.blue)
            painter.drawRect(self.rec)
        #self.QPainter.drawRect(x1, y1, x2, y2)
        #self.QPainter.drawRect(50, 50, 50, 50)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form = MyWindow()
    form.show()
    app.exec_()
