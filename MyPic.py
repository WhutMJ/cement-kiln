# 本文件为折线图显示的相关函数
from provide_data_for_gui import *
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
legendFont = fm.FontProperties(fname="C:\\Windows\\Fonts\\simsun.ttc", size=9)  # 设置字体，实现显示中文
labelfont = fm.FontProperties(fname="C:\\Windows\\Fonts\\simsun.ttc", size=9)  # 设置字体，实现显示中文
matplotlib.rcParams["axes.unicode_minus"] = False


class MyLabel(QLabel):
    changeindex = pyqtSignal(list, list, str)  # 单击窑系统部件时会发出信号

    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

    def call_win(self, index1, index2, name):
        self.changeindex.emit(index1, index2, name)

    def mousePressEvent(self, e):

        name = get_table_name()
        if self.objectName() == '1级筒A0':
            con.setValue_index_T(name.index('yijitwdA'))
            con.setValue_index_P(name.index('yijityqA'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '1级筒A':
            con.setValue_index_T(name.index('yijitwdA'))
            con.setValue_index_P(name.index('yijityqA'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '1级筒B0':
            con.setValue_index_T(name.index('yijitwdB'))
            con.setValue_index_P(name.index('yijityqB'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '1级筒B':
            con.setValue_index_T(name.index('yijitwdB'))
            con.setValue_index_P(name.index('yijityqB'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '2级筒A':
            con.setValue_index_T(name.index('erjitwdA'))
            con.setValue_index_P(name.index('erjityqA'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '2级筒B':
            con.setValue_index_T(name.index('erjitwdB'))
            con.setValue_index_P(name.index('erjityqB'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '3级筒A':
            con.setValue_index_T(name.index('sanjitwdA'))
            con.setValue_index_P(name.index('sanjityqA'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '3级筒B':
            con.setValue_index_T(name.index('sanjitwdB'))
            con.setValue_index_P(name.index('sanjityqB'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '4级筒A':
            con.setValue_index_T(name.index('sijitwdA'))
            con.setValue_index_P(name.index('sijityqA'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '4级筒B':
            con.setValue_index_T(name.index('sijitwdB'))
            con.setValue_index_P(name.index('sijityqB'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '5级筒A':
            con.setValue_index_T(name.index('wujitwdA'))
            con.setValue_index_P(name.index('wujityqA'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '5级筒B':
            con.setValue_index_T(name.index('wujitwdB'))
            con.setValue_index_P(name.index('wujityqB'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '分解炉':
            con.setValue_index_T(name.index('fenjielwd'))
            con.setValue_index_P(name.index('fenjielyq'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '窑1':
            con.setValue_index_T(0)
            con.setValue_index_P(name.index('yaoweic'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '窑2':
            con.setValue_index_T(name.index('tongtiwd'))
            con.setValue_index_P(name.index('yaos'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '窑3':
            con.setValue_index_T(name.index('yaotouyl'))
            con.setValue_index_P(name.index('yaotouc'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '篦冷机1段':
            con.setValue_index_T(name.index('bilengjydyl'))
            con.setValue_index_P(name.index('bilengjydS1'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '篦冷机2段':
            con.setValue_index_T(name.index('bilengjedS1'))
            con.setValue_index_P(name.index('bilengjedI1'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '篦冷机3段':
            con.setValue_index_T(name.index('bilengjsdS1'))
            con.setValue_index_P(name.index('bilengjsdI1'))
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())
        elif self.objectName() == '分解炉--窑':
            con.setValue_index_T(0)
            con.setValue_index_P(0)
            self.call_win(con.getValue_index_T(), con.getValue_index_P(), self.objectName())

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
            if str[i] == None or str[i] == "":
                count += 1
            else:
                null.append(i)  # 记录数据不为空的下标
        return count, null

    def normalization(self, data):
        Z = data
        newdata = []
        if Z == []:
            return newdata
        Zmax, Zmin = max(Z), min(Z)
        if Zmax == Zmin:
            for i in Z:
                newdata.append(0.5)
            return newdata

        for i in Z:
            newdata.append((i - Zmin) / (Zmax - Zmin))

        return newdata

    def compute_initial_figure(self):
        pass


class MyTempMplCanvas(MyMplCanvas):
    """温度画布"""

    def compute_initial_figure(self):
        day = str(con.getValue_day())
        index_T = con.getValue_index_T()
        if index_T == [] or index_T[0] == 0:
            pass
        else:
            if con.getValue_flag_Ctrl() == 0:  # 没有按住CTRL键
                if con.getValue_flag_Visual() == 0:  # 显示一天的图片
                    tablevalue = get_by_day(day)  # tablevalue[0]是标题，tablevalue[1]是各部件当天数据
                    count, null = self.cal_null(tablevalue[1][index_T[0] - 2])  # null为数据不为空的下标列表，空数据应当为None而不是
                    # 若：null = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
                    # 则意为0~23全由数据，若缺失，则为缺失的数字的小时没有数据
                    self.axes.set_ylabel('温度/℃', verticalalignment='center', fontproperties=labelfont)
                    self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
                    for tick_x in self.axes.get_xmajorticklabels():
                        tick_x.set_fontsize(8)
                    for tick_y in self.axes.get_ymajorticklabels():
                        tick_y.set_fontsize(7)
                    if count >= 1:
                        x = [i for i in range(24)]
                        y = tablevalue[1][index_T[0] - 2]
                        self.axes.plot(x, y, 'bo-')
                        if y[5]!=None:
                            self.axes.plot(5, y[5], 'ro-')  # 突出显示此危险点
                        # self.axes.set_xticklabels(x_label)
                        xmajorLocator = MultipleLocator(2)  # 将x主刻度标签设置为2的倍数
                        self.axes.xaxis.set_major_locator(xmajorLocator)
                        self.axes.set_title(get_chinese(tablevalue[0][index_T[0]]), fontproperties=myfont)
                    else:
                        t = arange(0, 24, 1)
                        try:
                            self.axes.plot(t, tablevalue[1][index_T[0] - 2], 'bo-')#如果t和tablevalue长度不一致会报错
                            #                                                   但是全为None不会报错

                            y = tablevalue[1][index_T[0] - 2]
                            if y[5]!=None:
                                self.axes.plot(5, y[5], 'ro-')  # 突出显示此危险点

                            xmajorLocator = MultipleLocator(5)  # 将x主刻度标签设置为5的倍数
                            xminorLocator = MultipleLocator(1)  # 将x轴次刻度标签设置为1的倍数
                            self.axes.xaxis.set_major_locator(xmajorLocator)
                            self.axes.xaxis.set_minor_locator(xminorLocator)
                            self.axes.set_title(get_chinese(tablevalue[0][index_T[0]]), fontproperties=myfont)
                        except Exception:
                            pass
                elif con.getValue_flag_Visual() == 1:  # 显示 10 小时的数据
                    tablevalue = get_by_day(day)  # tablevalue[0]是标题，tablevalue[1]是各部件当天数据
                    hour = con.getValue_hour()  # 显示hour之前的10小时数据(包括此hour)
                    self.axes.set_ylabel('温度/℃', verticalalignment='center', fontproperties=labelfont)
                    self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
                    for tick_x in self.axes.get_xmajorticklabels():
                        tick_x.set_fontsize(8)
                    for tick_y in self.axes.get_ymajorticklabels():
                        tick_y.set_fontsize(7)
                    y = tablevalue[1][index_T[0] - 2]

                    if hour >= 10:
                        x = [i for i in range(hour - 10, hour)]
                        y2 = y[hour - 10:hour]

                    else:
                        x = [i for i in range(hour + 1)]
                        y2 = y[:hour + 1]
                    self.axes.plot(x, y2, 'bo-')

                    xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为1的倍数
                    self.axes.xaxis.set_major_locator(xmajorLocator)
                    self.axes.set_title(tablevalue[0][index_T[0]], fontproperties=myfont)

            elif con.getValue_flag_Ctrl() == 1:#按住了Ctrl键
                tablevalue = get_by_day(day)  # tablevalue[0]是标题，tablevalue[1]是各部件当天数据
                self.axes.set_ylabel('温度/℃', verticalalignment='center', fontproperties=labelfont)
                self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
                for tick_x in self.axes.get_xmajorticklabels():
                    tick_x.set_fontsize(8)
                for tick_y in self.axes.get_ymajorticklabels():
                    tick_y.set_fontsize(7)

                x = [i for i in range(24)]
                p = [None for i in range(len(index_T))]
                line = []
                index = 0
                for i in index_T:
                    count, null = self.cal_null(tablevalue[1][i - 2])
                    line.append(tablevalue[0][i - 2])
                    y = tablevalue[1][i - 2]
                    z = []
                    for i in null:
                        z.append(y[i])
                    z = self.normalization(z)
                    j = 0
                    for i in null:
                        y[i] = z[j]
                        j += 1
                    p[index], = self.axes.plot(x, y)
                    index += 1
                self.axes.legend(p, line, loc='upper right', prop=legendFont)

                xmajorLocator = MultipleLocator(2)  # 将x主刻度标签设置为2的倍数
                self.axes.xaxis.set_major_locator(xmajorLocator)
                self.axes.set_title('趋势走向', fontproperties=myfont)


class MyPressMplCanvas(MyMplCanvas):
    """压强画布"""

    def compute_initial_figure(self):
        day = str(con.getValue_day())
        index_P = con.getValue_index_P()
        if index_P == [] or index_P[0] == 0:
            pass
        else:
            if con.getValue_flag_Ctrl() == 0:
                if con.getValue_flag_Visual() == 0:  # 显示一天的图片
                    tablevalue = get_by_day(day)  # tablevalue[0]是标题，tablevalue[1]是各部件当天数据
                    count, null = self.cal_null(tablevalue[1][index_P[0] - 2])
                    self.axes.set_ylabel('压强/MPa', verticalalignment='center', fontproperties=labelfont)
                    self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
                    for tick_x in self.axes.get_xmajorticklabels():
                        tick_x.set_fontsize(8)
                    for tick_y in self.axes.get_ymajorticklabels():
                        tick_y.set_fontsize(7)
                    if count >= 1:
                        x = [i for i in range(24)]
                        y = tablevalue[1][index_P[0] - 2]
                        self.axes.plot(x, y, 'bo-')
                        if y[5] != None:
                            self.axes.plot(5, y[5], 'ro-')  # 突出显示此危险点

                        xmajorLocator = MultipleLocator(2)  # 将x主刻度标签设置为2的倍数
                        self.axes.xaxis.set_major_locator(xmajorLocator)
                        self.axes.set_title(tablevalue[0][index_P[0]], fontproperties=myfont)
                    else:
                        t = arange(0, 24, 1)
                        try:
                            self.axes.plot(t, tablevalue[1][index_P[0] - 2], 'bo-')
                            y = tablevalue[1][index_P[0] - 2]
                            if y[5] != None:
                                self.axes.plot(5, y[5], 'ro-')  # 突出显示此危险点

                            xmajorLocator = MultipleLocator(5)  # 将x主刻度标签设置为5的倍数
                            xminorLocator = MultipleLocator(1)  # 将x轴次刻度标签设置为1的倍数
                            self.axes.xaxis.set_major_locator(xmajorLocator)
                            self.axes.xaxis.set_minor_locator(xminorLocator)
                            self.axes.set_title(tablevalue[0][index_P[0]], fontproperties=myfont)
                        except Exception:
                            pass
                elif con.getValue_flag_Visual() == 1:  # 显示 10 小时的数据
                    tablevalue = get_by_day(day)  # tablevalue[0]是标题，tablevalue[1]是各部件当天数据
                    hour = con.getValue_hour()  # 显示hour之前的10小时数据(包括此hour)

                    self.axes.set_ylabel('压强/MPa', verticalalignment='center', fontproperties=labelfont)
                    self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
                    for tick_x in self.axes.get_xmajorticklabels():
                        tick_x.set_fontsize(8)
                    for tick_y in self.axes.get_ymajorticklabels():
                        tick_y.set_fontsize(7)

                    y = tablevalue[1][index_P[0] - 2]

                    if hour >= 10:
                        x = [i for i in range(hour - 10, hour)]
                        y2 = y[hour - 10:hour]
                    else:
                        x = [i for i in range(hour + 1)]
                        y2 = y[:hour + 1]

                    self.axes.plot(x, y2, 'bo-')

                    xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为1的倍数
                    self.axes.xaxis.set_major_locator(xmajorLocator)
                    self.axes.set_title(tablevalue[0][index_P[0]], fontproperties=myfont)

            elif con.getValue_flag_Ctrl() == 1:  # 按住了CTRL键
                tablevalue = get_by_day(day)  # tablevalue[0]是标题，tablevalue[1]是各部件当天数据
                self.axes.set_ylabel('压强/MPa', verticalalignment='center', fontproperties=labelfont)
                self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
                for tick_x in self.axes.get_xmajorticklabels():
                    tick_x.set_fontsize(8)
                for tick_y in self.axes.get_ymajorticklabels():
                    tick_y.set_fontsize(7)

                x = [i for i in range(24)]
                p = [None for i in range(len(index_P))]
                line = []
                index = 0
                for i in index_P:
                    count, null = self.cal_null(tablevalue[1][i - 2])
                    line.append(tablevalue[0][i - 2])
                    y = tablevalue[1][i - 2]
                    z = []
                    for i in null:
                        z.append(y[i])
                    z = self.normalization(z)
                    j = 0
                    for i in null:
                        y[i] = z[j]
                        j += 1
                    p[index], = self.axes.plot(x, y)
                    index += 1
                self.axes.legend(p, line, loc='upper right', prop=legendFont)

                xmajorLocator = MultipleLocator(2)  # 将x主刻度标签设置为2的倍数
                self.axes.xaxis.set_major_locator(xmajorLocator)
                self.axes.set_title('趋势走向', fontproperties=myfont)

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
