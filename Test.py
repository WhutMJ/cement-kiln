# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer

import random
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

    def compute_initial_figure(self):
        pass


class AnimationWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.vbox = QtWidgets.QVBoxLayout()
        self.canvas = MyMplCanvas(self, width=5, height=4, dpi=100)

        self.x = [0.5]
        self.y = [1]
        self.canvas.axes.plot(self.x, self.y,'bo-')

        self.vbox.addWidget(self.canvas)
        hbox = QtWidgets.QHBoxLayout()
        self.start_button = QtWidgets.QPushButton("start", self)
        self.stop_button = QtWidgets.QPushButton("stop", self)
        self.start_button.clicked.connect(self.on_start)
        self.stop_button.clicked.connect(self.on_stop)
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        self.vbox.addLayout(hbox)
        self.setLayout(self.vbox)

        self.setTimer()

    def setTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.operate)  # 触发事件
        self.timer.start(2000)  # 触发间隔
        self.time_count=0

    def operate(self):
        self.time_count+=1
        delt_x = random.random()
        delt_y = random.random()
        self.x.append(self.x[-1] + delt_x)
        self.y.append(self.y[-1] + delt_y)
        if len(self.x)>8:
            self.x=self.x[1:]
            self.y=self.y[1:]
        if self.time_count%3==1:
            self.canvas2=MyMplCanvas(self, width=5, height=4, dpi=100)
            self.canvas2.axes.plot(self.x,self.y,'bo-')
            self.vbox.replaceWidget(self.canvas,self.canvas2)
        elif self.time_count%3==2:
            self.canvas3=MyMplCanvas(self, width=5, height=4, dpi=100)
            self.canvas3.axes.plot(self.x,self.y,'bo-')
            self.vbox.replaceWidget(self.canvas2,self.canvas3)
        else:
            self.canvas=MyMplCanvas(self, width=5, height=4, dpi=100)
            self.canvas.axes.plot(self.x,self.y,'bo-')
            self.vbox.replaceWidget(self.canvas3,self.canvas)

    def on_start(self):
        pass

    def on_stop(self):
        pass


if __name__ == "__main__":
    qApp = QtWidgets.QApplication(sys.argv)
    aw = AnimationWidget()
    aw.show()
    sys.exit(qApp.exec_())
