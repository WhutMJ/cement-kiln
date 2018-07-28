# 本文件为折线图显示的相关函数

import os
import config as con

from provide_data_for_gui import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import matplotlib.font_manager as fm
from matplotlib.ticker import MultipleLocator
import matplotlib
from numpy import arange
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

#     日期， 时间选择标志，温度，压强，  小时，日期，单双系列标志，旋风筒数
myfont = fm.FontProperties(fname="C:\\Windows\\Fonts\\simsun.ttc", size=14)  # 设置字体，实现显示中文
labelfont = fm.FontProperties(fname="C:\\Windows\\Fonts\\simsun.ttc", size=9)  # 设置字体，实现显示中文
matplotlib.rcParams["axes.unicode_minus"] = False


class MyLabel(QLabel):
    changeindex = pyqtSignal(int, int)  # 单击窑系统部件时会发出信号

    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

    def call_win(self, index1, index2):
        self.changeindex.emit(index1, index2)

    def mousePressEvent(self, e):
        flag_Time = con.getValue_flagTime()
        if flag_Time == 1:  # 判断是否选择了时间
            if self.objectName() == '1级筒A':
                con.setValue_index_T(8)
                con.setValue_index_P(9)
                self.call_win(con.getValue_index_T(), con.getValue_index_P())
            elif self.objectName() == '1级筒B':
                con.setValue_index_T(10)
                con.setValue_index_P(11)
                self.call_win(con.getValue_index_T(), con.getValue_index_P())
            elif self.objectName() == '2级筒A':
                con.setValue_index_T(12)
                con.setValue_index_P(13)
                self.call_win(con.getValue_index_T(), con.getValue_index_P())
            elif self.objectName() == '2级筒B':
                con.setValue_index_T(14)
                con.setValue_index_P(15)
                self.call_win(con.getValue_index_T(), con.getValue_index_P())
            elif self.objectName() == '3级筒A':
                con.setValue_index_T(16)
                con.setValue_index_P(17)
                self.call_win(con.getValue_index_T(), con.getValue_index_P())
            elif self.objectName() == '3级筒B':
                con.setValue_index_T(18)
                con.setValue_index_P(19)
                self.call_win(con.getValue_index_T(), con.getValue_index_P())
            elif self.objectName() == '4级筒A':
                con.setValue_index_T(20)
                con.setValue_index_P(21)
                self.call_win(con.getValue_index_T(), con.getValue_index_P())
            elif self.objectName() == '4级筒B':
                con.setValue_index_T(22)
                con.setValue_index_P(23)
                self.call_win(con.getValue_index_T(), con.getValue_index_P())
            elif self.objectName() == '5级筒A':
                con.setValue_index_T(24)
                con.setValue_index_P(25)
                self.call_win(con.getValue_index_T(), con.getValue_index_P())
            elif self.objectName() == '5级筒B':
                con.setValue_index_T(26)
                con.setValue_index_P(27)
                self.call_win(con.getValue_index_T(), con.getValue_index_P())
            elif self.objectName() == '分解炉':
                con.setValue_index_T(29)
                con.setValue_index_P(30)
                self.call_win(con.getValue_index_T(), con.getValue_index_P())
            elif self.objectName() == '窑':
                con.setValue_index_T(28)
                con.setValue_index_P(0)
                self.call_win(con.getValue_index_T(), con.getValue_index_P())
            elif self.objectName() == '篦冷机':
                con.setValue_index_T(33)
                con.setValue_index_P(0)
                self.call_win(con.getValue_index_T(), con.getValue_index_P())
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

    def cal_null(self, str):  # 计算一天的空数据个数及其下标
        null = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        count = 0
        for i in range(len(str)):
            if str[i] == 'null':
                null[i] = 1
                count += 1
        return count, null

    def compute_initial_figure(self):
        pass


class MyTempMplCanvas(MyMplCanvas):
    """温度画布"""

    def compute_initial_figure(self):
        day = con.getValue_day()
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
                    value = [0 for i in range(24 - count)]
                    t = [i for i in range(24 - count)]
                    x_label = [str(i) for i in range(24 - count + 1)]
                    j = 0
                    x_label[j] = '0'
                    for i in range(24):
                        if null[i] == 1:
                            pass
                        else:
                            value[j] = tablevalue[1][index_T][i]
                            # t[j] = i
                            x_label[j + 1] = str(i)
                            j += 1
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
            else:#显示 10 小时的数据
                tablevalue = get_by_day(day)  # tablevalue[0]是标题，tablevalue[1]是各部件当天数据

                #以后会将day换成hour

                count, null = self.cal_null(tablevalue[1][index_T])
                self.axes.set_ylabel('温度/℃', verticalalignment='center', fontproperties=labelfont)
                self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
                for tick_x in self.axes.get_xmajorticklabels():
                    tick_x.set_fontsize(8)
                for tick_y in self.axes.get_ymajorticklabels():
                    tick_y.set_fontsize(7)
                if count >= 1:
                    value = [0 for i in range(10 - count)]
                    t = [i for i in range(10 - count)]
                    x_label = [str(i) for i in range(10 - count + 1)]
                    j = 0
                    x_label[j] = '0'
                    for i in range(10):
                        if null[i] == 1:
                            pass
                        else:
                            value[j] = tablevalue[1][index_T][i]
                            # t[j] = i
                            x_label[j + 1] = str(i)
                            j += 1
                    self.axes.plot(t, value)
                    self.axes.set_xticklabels(x_label)

                    xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为1的倍数
                    self.axes.xaxis.set_major_locator(xmajorLocator)
                    self.axes.set_title(tablevalue[0][index_T], fontproperties=myfont)
                else:
                    t = arange(0, 10, 1)
                    self.axes.plot(t, tablevalue[1][index_T][0:10])
                    # 以后需要修改参数不一定是[0:10]
                    xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为5的倍数
                    #xminorLocator = MultipleLocator(1)  # 将x轴次刻度标签设置为1的倍数
                    self.axes.xaxis.set_major_locator(xmajorLocator)
                    #self.axes.xaxis.set_minor_locator(xminorLocator)
                    self.axes.set_title(tablevalue[0][index_T], fontproperties=myfont)


class MyPressMplCanvas(MyMplCanvas):
    """压强画布"""

    def compute_initial_figure(self):
        day = con.getValue_day()
        index_P = con.getValue_index_P()
        if index_P == 0:
            pass
        else:
            if con.getValue_flag_Visual() == 0:  # 显示一天的图片
                tablevalue = get_by_day(day)
                count, null = self.cal_null(tablevalue[1][index_P])
                self.axes.set_ylabel('压强/kPa', verticalalignment='center', fontproperties=labelfont)
                self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
                for tick_x in self.axes.get_xmajorticklabels():
                    tick_x.set_fontsize(8)
                for tick_y in self.axes.get_ymajorticklabels():
                    tick_y.set_fontsize(7)
                if count >= 1:
                    value = [0 for i in range(24 - count)]
                    t = [i for i in range(24 - count)]
                    x_label = [str(i) for i in range(24 - count + 1)]
                    j = 0
                    x_label[j] = '0'
                    for i in range(24):
                        if null[i] == 1:
                            pass
                        else:
                            value[j] = tablevalue[1][index_P][i]
                            # t[j] = i
                            x_label[j + 1] = str(i)
                            j += 1
                    self.axes.plot(t, value)
                    self.axes.set_xticklabels(x_label)
                    for tick in self.axes.get_xmajorticklabels():
                        tick.set_fontsize(8)
                    xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为5的倍数
                    self.axes.xaxis.set_major_locator(xmajorLocator)

                else:
                    t = arange(0, 24, 1)
                    self.axes.plot(t, tablevalue[1][index_P])
                    xmajorLocator = MultipleLocator(5)  # 将x主刻度标签设置为5的倍数
                    xminorLocator = MultipleLocator(1)  # 将x轴次刻度标签设置为1的倍数
                    self.axes.xaxis.set_major_locator(xmajorLocator)
                    self.axes.xaxis.set_minor_locator(xminorLocator)
                    self.axes.set_title(tablevalue[0][index_P], fontproperties=myfont)
            else:
                tablevalue = get_by_day(day)
                count, null = self.cal_null(tablevalue[1][index_P])
                self.axes.set_ylabel('压强/kPa', verticalalignment='center', fontproperties=labelfont)
                self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
                for tick_x in self.axes.get_xmajorticklabels():
                    tick_x.set_fontsize(8)
                for tick_y in self.axes.get_ymajorticklabels():
                    tick_y.set_fontsize(7)
                if count >= 1:
                    value = [0 for i in range(10 - count)]
                    t = [i for i in range(10 - count)]
                    x_label = [str(i) for i in range(10 - count + 1)]
                    j = 0
                    x_label[j] = '0'
                    for i in range(10):
                        if null[i] == 1:
                            pass
                        else:
                            value[j] = tablevalue[1][index_P][i]
                            # t[j] = i
                            x_label[j + 1] = str(i)
                            j += 1
                    self.axes.plot(t, value)
                    self.axes.set_xticklabels(x_label)
                    for tick in self.axes.get_xmajorticklabels():
                        tick.set_fontsize(8)
                    xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为5的倍数
                    self.axes.xaxis.set_major_locator(xmajorLocator)

                else:
                    t = arange(0, 10, 1)
                    self.axes.plot(t, tablevalue[1][index_P][0:10])
                    #以后需要修改参数不一定是[0:10]
                    xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为5的倍数
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
