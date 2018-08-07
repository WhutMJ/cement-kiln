# 本文件为折线图显示的相关函数

import os
import config as con

from provide_data_for_gui import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import matplotlib.font_manager as fm
import matplotlib
from matplotlib.ticker import MultipleLocator
from numpy import arange
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

#     日期， 时间选择标志，温度，压强，  小时，日期，单双系列标志，旋风筒数
myfont = fm.FontProperties(fname="C:\\Windows\\Fonts\\simsun.ttc", size=14)  # 设置字体，实现显示中文
labelfont = fm.FontProperties(fname="C:\\Windows\\Fonts\\simsun.ttc", size=9)  # 设置字体，实现显示中文
matplotlib.rcParams["axes.unicode_minus"] = False


class MyLabel(QLabel):
    changeindex = pyqtSignal(int, int, str)  # 单击窑系统部件时会发出信号

    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

    def call_win(self, index1, index2, name):
        self.changeindex.emit(index1, index2, name)

    def mousePressEvent(self, e):
        flag_Time = con.getValue_flagTime()

        if flag_Time == 1:  # 判断是否选择了时间
            if self.objectName() == '1级筒A0':
                con.setValue_index_T(8)
                con.setValue_index_P(9)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '1级筒A':
                con.setValue_index_T(8)
                con.setValue_index_P(9)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '1级筒B0':
                con.setValue_index_T(10)
                con.setValue_index_P(11)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '1级筒B':
                con.setValue_index_T(10)
                con.setValue_index_P(11)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '2级筒A':
                con.setValue_index_T(12)
                con.setValue_index_P(13)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '2级筒B':
                con.setValue_index_T(14)
                con.setValue_index_P(15)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '3级筒A':
                con.setValue_index_T(16)
                con.setValue_index_P(17)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '3级筒B':
                con.setValue_index_T(18)
                con.setValue_index_P(19)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '4级筒A':
                con.setValue_index_T(20)
                con.setValue_index_P(21)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '4级筒B':
                con.setValue_index_T(22)
                con.setValue_index_P(23)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '5级筒A':
                con.setValue_index_T(24)
                con.setValue_index_P(25)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '5级筒B':
                con.setValue_index_T(26)
                con.setValue_index_P(27)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '分解炉':
                con.setValue_index_T(29)
                con.setValue_index_P(30)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '窑1':
                con.setValue_index_T(28)
                con.setValue_index_P(0)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '窑2':
                con.setValue_index_T(0)
                con.setValue_index_P(0)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '窑3':
                con.setValue_index_T(0)
                con.setValue_index_P(32)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '篦冷机1段':
                con.setValue_index_T(33)
                con.setValue_index_P(34)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '篦冷机2段':
                con.setValue_index_T(36)
                con.setValue_index_P(37)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
            elif self.objectName() == '篦冷机3段':
                con.setValue_index_T(38)
                con.setValue_index_P(39)
                self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        else:
            self.msg()

    def msg(self):
        reply = QMessageBox.information(self, '提示', '请先选择时间', QMessageBox.Yes | QMessageBox.No)


class MyMplCanvas(FigureCanvas):
    """这是一个窗口部件，即QWidget（当然也是FigureCanvasAgg）"""

    def __init__(self, parent=None, width=3, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # 每次plot()调用的时候，我们希望原来的坐标轴被清除(所以False)
        # self.axes.hold(False)
        '''self.ax = axisartist.Subplot(fig, 111)
        fig.add_axes(self.ax)
        self.ax.axis['bottom'].set_axisline_style('->', size=1.5)
        self.ax.axis["left"].set_axisline_style("->", size=1.5)
        self.ax.axis["top"].set_visible(False)
        self.ax.axis["right"].set_visible(False)'''

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def cal_null(self, str):  # 计算一天的空数据个数及不为空下标
        # null = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        null = []
        count = 0
        for i in range(len(str)):
            if str[i] == None:
                count += 1
            else:
                null.append(i)  # 记录数据不为空的下标
        return count, null

    def compute_initial_figure(self):
        pass


class MyTempMplCanvas(MyMplCanvas):
    """温度画布"""

    def compute_initial_figure(self):
        day = str(con.getValue_day())

        index_T = con.getValue_index_T()
        if index_T == 0:
            pass
        else:
            if con.getValue_flag_Visual() == 0:  # 显示一天的图片
                tablevalue = get_by_day(day)  # tablevalue[0]是标题，tablevalue[1]是各部件当天数据
                count, null = self.cal_null(tablevalue[1][index_T])
                self.axes.set_ylabel('温度/℃', verticalalignment='center', fontproperties=labelfont)
                self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
                for tick_x in self.axes.get_xmajorticklabels():
                    tick_x.set_fontsize(8)
                for tick_y in self.axes.get_ymajorticklabels():
                    tick_y.set_fontsize(7)
                if count >= 1:
                    value = []
                    t = [i for i in range(24 - count)]
                    x_label = []
                    x_label.append('0')
                    j = 0
                    # x_label[j] = '0'
                    for i in range(24 - count):
                        value.append(tablevalue[1][index_T][null[i]])
                        x_label.append(str(null[i]))

                    #在此标注出异常点
                    self.axes.plot(t[2],value[2],'ro')

                    self.axes.plot(t, value)
                    self.axes.set_xticklabels(x_label)
                    xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为5的倍数
                    self.axes.xaxis.set_major_locator(xmajorLocator)
                    self.axes.set_title(tablevalue[0][index_T], fontproperties=myfont)
                else:
                    t = arange(0, 24, 1)
                    self.axes.plot(t, tablevalue[1][index_T])
                    xmajorLocator = MultipleLocator(5)  # 将x主刻度标签设置为5的倍数
                    xminorLocator = MultipleLocator(1)  # 将x轴次刻度标签设置为1的倍数
                    self.axes.xaxis.set_major_locator(xmajorLocator)
                    self.axes.xaxis.set_minor_locator(xminorLocator)
                    self.axes.set_title(tablevalue[0][index_T], fontproperties=myfont)
            elif con.getValue_flag_Visual() == 1:  # 显示 10 小时的数据
                tablevalue = get_by_day(day)  # tablevalue[0]是标题，tablevalue[1]是各部件当天数据
                hour = con.getValue_hour()  # 显示hour之前的10小时数据(包括此hour)
                count, null = self.cal_null(tablevalue[1][index_T])  # null[i] 记录了数据不为空的下标
                self.axes.set_ylabel('温度/℃', verticalalignment='center', fontproperties=labelfont)
                self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
                for tick_x in self.axes.get_xmajorticklabels():
                    tick_x.set_fontsize(8)
                for tick_y in self.axes.get_ymajorticklabels():
                    tick_y.set_fontsize(7)

                value = []
                t = []
                x_label = []

                # x_label[j] = '0'
                cycle = 10  # 循环十次
                for i in range(len(null)):  # 找到第hour小时的下标
                    if null[i] == hour:
                        j = i

                if null != []:
                    while (cycle > 0):

                        value.insert(0, tablevalue[1][index_T][null[j]])
                        # t[j] = i

                        x_label.insert(0, str(null[j]))
                        j -= 1
                        cycle -= 1
                        t.append(10 - cycle)
                        if j < 0:
                            break
                x_label.insert(0, '0')
                self.axes.plot(t, value)
                self.axes.set_xticklabels(x_label)

                xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为1的倍数
                self.axes.xaxis.set_major_locator(xmajorLocator)
                self.axes.set_title(tablevalue[0][index_T], fontproperties=myfont)


class MyPressMplCanvas(MyMplCanvas):
    """压强画布"""

    def compute_initial_figure(self):
        day = str(con.getValue_day())
        index_P = con.getValue_index_P()

        if index_P == 0:
            pass
        else:
            if con.getValue_flag_Visual() == 0:  # 显示一天的图片
                tablevalue = get_by_day(day)  # tablevalue[0]是标题，tablevalue[1]是各部件当天数据
                count, null = self.cal_null(tablevalue[1][index_P])
                self.axes.set_ylabel('温度/℃', verticalalignment='center', fontproperties=labelfont)
                self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
                for tick_x in self.axes.get_xmajorticklabels():
                    tick_x.set_fontsize(8)
                for tick_y in self.axes.get_ymajorticklabels():
                    tick_y.set_fontsize(7)
                if count >= 1:
                    value = []
                    t = [i for i in range(24 - count)]
                    x_label = []
                    x_label.append('0')
                    j = 0
                    # x_label[j] = '0'
                    for i in range(24 - count):
                        value.append(tablevalue[1][index_P][null[i]])
                        x_label.append(str(null[i]))
                    self.axes.plot(t, value)
                    self.axes.set_xticklabels(x_label)
                    xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为5的倍数
                    self.axes.xaxis.set_major_locator(xmajorLocator)
                    self.axes.set_title(tablevalue[0][index_P], fontproperties=myfont)
                else:
                    t = arange(0, 24, 1)
                    self.axes.plot(t, tablevalue[1][index_P])
                    xmajorLocator = MultipleLocator(5)  # 将x主刻度标签设置为5的倍数
                    xminorLocator = MultipleLocator(1)  # 将x轴次刻度标签设置为1的倍数
                    self.axes.xaxis.set_major_locator(xmajorLocator)
                    self.axes.xaxis.set_minor_locator(xminorLocator)
                    self.axes.set_title(tablevalue[0][index_P], fontproperties=myfont)
            elif con.getValue_flag_Visual() == 1:  # 显示 10 小时的数据
                tablevalue = get_by_day(day)  # tablevalue[0]是标题，tablevalue[1]是各部件当天数据
                hour = con.getValue_hour()  # 显示hour之前的10小时数据(包括此hour)

                count, null = self.cal_null(tablevalue[1][index_P])  # null[i] 记录了数据不为空的下标

                self.axes.set_ylabel('温度/℃', verticalalignment='center', fontproperties=labelfont)
                self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
                for tick_x in self.axes.get_xmajorticklabels():
                    tick_x.set_fontsize(8)
                for tick_y in self.axes.get_ymajorticklabels():
                    tick_y.set_fontsize(7)

                value = []
                t = []
                x_label = []

                # x_label[j] = '0'
                cycle = 10  # 循环十次
                for i in range(len(null)):  # 找到第hour小时的下标
                    if null[i] == hour:
                        j = i
                if null != []:
                    while (cycle > 0):
                        value.insert(0, tablevalue[1][index_P][null[j]])
                        # t[j] = i
                        x_label.insert(0, str(null[j]))
                        j -= 1
                        cycle -= 1
                        t.append(10 - cycle)
                        if j < 0:
                            break
                x_label.insert(0, '0')  # 不知道为什么标签的第一个是不显示的，所以要在首位随便插入一个字符
                self.axes.plot(t, value)
                self.axes.set_xticklabels(x_label)

                xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为1的倍数
                self.axes.xaxis.set_major_locator(xmajorLocator)
                self.axes.set_title(tablevalue[0][index_P], fontproperties=myfont)

    '''def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        # 构建4个随机整数，位于闭区间[0, 10]
        l = [random.randint(0, 10) for i in range(4)]

        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()'''
