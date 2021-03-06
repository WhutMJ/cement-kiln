import sys
import random
import sip
from provide_data_for_gui import *
from win32api import GetSystemMetrics

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *  # QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter, QIcon, QPixmap

import matplotlib.font_manager as fm
from matplotlib.ticker import MultipleLocator
import matplotlib
from numpy import arange
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import mpl_toolkits.axisartist as axisartist

global day, flag, index_T, index_P

myfont = fm.FontProperties(fname="C:\\Windows\\Fonts\\simsun.ttc", size=14)  # 设置字体，实现显示中文
labelfont = fm.FontProperties(fname="C:\\Windows\\Fonts\\simsun.ttc", size=9)  # 设置字体，实现显示中文
matplotlib.rcParams["axes.unicode_minus"] = False


class MyWindow(QMainWindow):
    global flag
    flag = 0

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        metric_width = GetSystemMetrics(0)
        metric_height = GetSystemMetrics(1)  # 获取电脑分辨率
        self.resize(metric_width, metric_height)
        self.showMaximized()

        # self.initPic()
        self.initMenu()
        # self.initBtn()
        self.set_window = MyWindow2()  # 初始化对话框
        self.set_window.show()

        self.set_window.yao_par_signal.connect(self.initDevice)

    def initDevice(self, flag, num):
        metric_width = GetSystemMetrics(0)
        metric_height = GetSystemMetrics(1)  # 获取电脑分辨率
        self.width = metric_width  # 图片宽度
        self.height = metric_height  # 图片高度

        self.pic_x = 40
        self.pic_y = 200  # 图片起始点
        # 设置信息显示区域
        self.setWindowTitle("Cement Kiln")
        self.widget = QWidget()
        self.table = QTableWidget(0, 2)  # 以表格形式显示数据
        self.table.setMinimumHeight(100)
        self.messageView = QTabWidget()
        self.messageView.setMinimumHeight(100)

        # self.resize(self.width,self.height)

        self.table.horizontalHeader().setDefaultSectionSize(150)
        self.messageSplitter = QSplitter(Qt.Vertical)
        self.messageSplitter.addWidget(self.table)
        self.messageSplitter.addWidget(self.messageView)
        # self.messageSplitter.addWidget(self.functionList)
        self.mainSplitter = QSplitter(Qt.Horizontal)
        self.mainSplitter.addWidget(self.widget)
        self.mainSplitter.addWidget(self.messageSplitter)
        self.setCentralWidget(self.mainSplitter)

        self.table.setMaximumHeight(300)

        self.tab1 = QLabel()
        self.tab2 = QLabel()
        self.messageView.addTab(self.tab1, '温度')
        self.messageView.addTab(self.tab2, '压强')
        self.pic1 = QVBoxLayout(self.tab1)
        self.pic2 = QVBoxLayout(self.tab2)

        self.click_flag = 0  # 切换图片标志

        xft_dl = QPixmap('picture\\xft_dl.png')  # 旋风筒
        xft_zuo = QPixmap('picture\\xft_zuo.png')  # 旋风筒左管
        xft_you = QPixmap('picture\\xft_you.png')  # 旋风筒右管
        fjl = QPixmap('picture\\fjl.png')  # 分解炉
        blj = QPixmap('picture\\blj.png')  # 篦冷机
        fjl_yao = QPixmap('picture\\fjl_yao')  # 分解炉与窑之间的连接部件
        mfc = QPixmap('picture\\mfc.png')  # 煤粉仓
        gwfj = QPixmap('picture\\gwfj.png')  # 高温风机
        yao = QPixmap('picture\\yao.png')

        ratio = 0.3  # 图片放大倍数

        self.widget.autoFillBackground()

        number = int(num)

        self.xft = {}

        self.xft[0] = MyLabel()
        self.xft[0].setPixmap(xft_dl.scaled(xft_dl.width() * ratio, xft_dl.height() * ratio))
        self.xft[0].setObjectName('%d级筒A' % 1)
        self.xft[0].changeindex.connect(self.change_pic)
        # print(self.xft[0].objectName())
        self.xft[number] = MyLabel()
        self.xft[number].setPixmap(xft_dl.scaled(xft_dl.width() * ratio, xft_dl.height() * ratio))
        self.xft[number].setObjectName('%d级筒A' % number)
        self.xft[number].changeindex.connect(self.change_pic)

        for i in arange(1, number, 2):  # 不会取到number,奇数旋风筒为右管
            self.xft[i] = MyLabel()
            self.xft[i].setPixmap(xft_you.scaled(xft_you.width() * ratio, xft_you.height() * ratio))
            self.xft[i].setObjectName('%d级筒A' % i)
            self.xft[i].changeindex.connect(self.change_pic)
        for i in arange(2, number, 2):  # 偶数旋风筒为左管
            self.xft[i] = MyLabel()
            self.xft[i].setPixmap(xft_zuo.scaled(xft_zuo.width() * ratio, xft_zuo.height() * ratio))
            self.xft[i].setObjectName('%d级筒A' % i)
            self.xft[i].changeindex.connect(self.change_pic)

        if flag == 2:  # 双系列
            self.xft[number + 1] = MyLabel()
            self.xft[number + 1].setPixmap(xft_dl.scaled(xft_dl.width() * ratio, xft_dl.height() * ratio))
            self.xft[number + 1].setObjectName('%d级筒B' % 1)
            self.xft[number + 1].changeindex.connect(self.change_pic)
            # print(self.xft[0].objectName())
            self.xft[2 * number + 1] = MyLabel()
            self.xft[2 * number + 1].setPixmap(xft_dl.scaled(xft_dl.width() * ratio, xft_dl.height() * ratio))
            self.xft[2 * number + 1].setObjectName('%d级筒B' % number)
            self.xft[2 * number + 1].changeindex.connect(self.change_pic)

            for i in arange(number + 2, 2 * number + 1, 2):  # 不会取到2*number,奇数旋风筒为左管
                print(i)
                self.xft[i] = MyLabel()
                self.xft[i].setPixmap(xft_zuo.scaled(xft_zuo.width() * ratio, xft_zuo.height() * ratio))
                self.xft[i].setObjectName('%d级筒B' % (i % (number + 1)))
                self.xft[i].changeindex.connect(self.change_pic)

            for i in arange(number + 3, 2 * number + 1, 2):  # 偶数旋风筒为右管
                print(i)
                self.xft[i] = MyLabel()
                self.xft[i].setPixmap(xft_you.scaled(xft_you.width() * ratio, xft_you.height() * ratio))
                self.xft[i].setObjectName('%d级筒B' % (i % (number + 1)))
                self.xft[i].changeindex.connect(self.change_pic)

        self.lab_fjl = MyLabel()
        if number % 2 == 0:
            self.lab_fjl.setPixmap(fjl.scaled(xft_dl.width() * 5 * ratio, xft_dl.height() * 3 * ratio))
        else:
            self.lab_fjl.setPixmap(fjl.scaled(xft_dl.width() * 7 * ratio, xft_dl.height() * 3 * ratio))
        self.lab_fjl.setObjectName('分解炉')
        self.lab_fjl.changeindex.connect(self.change_pic)

        self.lab_yao = MyLabel()
        self.lab_yao.setPixmap(yao.scaled(xft_dl.width() * 9 * ratio, yao.height() * ratio))
        self.lab_yao.setObjectName('窑')
        self.lab_yao.changeindex.connect(self.change_pic)

        self.lab_blj = MyLabel()
        self.lab_blj.setPixmap(blj.scaled(blj.width() * ratio, blj.height() * ratio))
        self.lab_blj.setObjectName('篦冷机')
        self.lab_blj.changeindex.connect(self.change_pic)

        self.fjl_yao = MyLabel()
        self.fjl_yao.setPixmap(fjl_yao.scaled(xft_dl.width() * ratio, fjl_yao.height() * ratio))
        self.fjl_yao.setObjectName('分解炉--窑')

        lay = QGridLayout()
        xft_row = 1  # 旋风筒所占行数
        xft_col = 2  # 旋风筒所占列数
        fjl_row = 3  # 分解炉所占行数
        fjl_col = 5  # 分解炉所占列数

        lay.addWidget(self.xft[0], 0, 0)
        for i in arange(1, number):
            lay.addWidget(self.xft[i], i - 1, 1, xft_row, xft_col)
        if number % 2 == 0:
            lay.addWidget(self.lab_fjl, number - 2, 2, fjl_row, fjl_col)  # 分解炉
            lay.addWidget(self.xft[number], number - 1, 2)
            lay.addWidget(self.fjl_yao, number - 2 + fjl_row, (fjl_col - 1) / 2 + 2)  # 连接件
            lay.addWidget(self.lab_yao, number - 2 + fjl_row, (fjl_col - 1) / 2 + 3, 2, 9)  # 窑
            lay.addWidget(self.lab_blj, number - 2 + fjl_row, 16, 2, 3)  # 篦冷机
        else:
            lay.addWidget(self.lab_fjl, number - 2, 1, fjl_row, fjl_col + 2)  # 分解炉
            lay.addWidget(self.xft[number], number - 1, 1)
            lay.addWidget(self.fjl_yao, number - 2 + fjl_row, (fjl_col - 1) / 2 + 2)  # 连接件
            lay.addWidget(self.lab_yao, number - 2 + fjl_row, (fjl_col - 1) / 2 + 3, 2, 9)  # 窑
            lay.addWidget(self.lab_blj, number - 2 + fjl_row, 16, 2, 3)  # 篦冷机
        if flag == 2:
            lay.addWidget(self.xft[number + 1], 0, 10 - flag)
            for i in arange(number + 2, 2 * number + 1):
                # print(i)
                lay.addWidget(self.xft[i], (i - 2) % number, 8 - flag, xft_row, xft_col)
            if number % 2 == 0:
                lay.addWidget(self.xft[number * 2 + 1], number - 1, 8 - flag)
            else:
                lay.addWidget(self.xft[number * 2 + 1], number - 1, 9 - flag)
        lay.setSpacing(0)
        lay.setAlignment(Qt.AlignLeft | Qt.AlignCenter)

        self.widget.setLayout(lay)

        self.initBtn()  # 初始化时间选择控件

    def on_click(self):
        self.setTime()

    def double_click(self):
        global day, flag
        flag = 1

        self.calendar.hide()
        date = self.calendar.selectedDate().toString('yyyy-MM-dd')  # 日期显示格式 例:2017-01-02
        date_input = '12345678'
        date_input = date[:4] + date[5:7] + date[8:10]
        self.timeBtn.setText(date)

        day = int(date_input)
        # print(day)

        '''col1,col2=get_by_hour(day)

        self.table.setRowCount(len(col1))
        self.table.setHorizontalHeaderLabels(['名称','数值'])
        for i in range(len(col1)):
            newItem = QTableWidgetItem(col1[i])
            self.table.setItem(i, 0, newItem)
            newItem = QTableWidgetItem(str(col2[i]))
            self.table.setItem(i, 1, newItem)'''

    def initBtn(self):
        global flag
        flag = 0
        self.click_flag = 0
        self.timeBtn = QPushButton('双击确定', self.widget)
        self.timeBtn.move(self.width * 0.5, self.height * 0.05)
        self.timeBtn.clicked.connect(self.on_click)
        self.timeBtn.show()

        self.timeLabel = QLabel(self.widget)
        self.timeLabel.move(self.width * 0.5 - 30, self.height * 0.05 + 5)
        self.timeLabel.resize(30, 20)
        self.timeLabel.setText('日期')

        self.timeLabel.show()

    def setTime(self):
        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate(2002, 6, 19))
        self.calendar.setSelectedDate(QDate(2017, 1, 23))
        self.calendar.resize(400, 300)
        self.calendar.move(0, 23)
        self.calendar.show()
        self.calendar.activated.connect(self.double_click)

    def dataVisual(self):
        print("窑系统数据可视化")

    def deviceSet(self):
        self.set_window.show()

    def initMenu(self):

        # 数据模块
        dataInputAct = QAction('数据输入', self)

        openFileAct = QAction('打开数据文件', self)

        saveFileAct = QAction('数据保存', self)

        saveasFileAct = QAction('数据另存为', self)

        changeDataAct = QAction('数据修改', self)

        simulateDataAct = QAction('数据模拟', self)

        leadInAct = QAction('数据导入', self)

        leadOutAct = QAction('数据导出', self)

        # 可视化模块
        dataVisualAct = QAction('窑系统数据可视化', self)
        dataVisualAct.setStatusTip('数据可视化')
        dataVisualAct.triggered.connect(self.dataVisual)

        singleVisualAct = QAction('独立因素热耗分析可视化', self)

        mulVisualAct = QAction('联合因素热耗分析可视化', self)

        heatVisualAct = QAction('窑系统热耗可视化', self)

        deviceVisualAct = QAction('窑系统设备热耗可视化', self)

        # 生产指导模块
        warningAct = QAction('生产预警', self)

        warningGuideAct = QAction('生产预警指导', self)

        errorAct = QAction('生产异常报警', self)

        errorGuideAct = QAction('生产异常指导', self)

        # 设置模块
        deviceSetAct = QAction('窑系统设备', self)
        deviceSetAct.setStatusTip('窑系统设备设置')
        deviceSetAct.triggered.connect(self.deviceSet)

        dataSetAct = QAction('窑系统数据', self)

        userSetAct = QAction('用户设置', self)

        standardSetAct = QAction('生产数据标准设置', self)

        objectSetAct = QAction('可视化对象设置', self)

        # 输出模块
        dataOutAct = QAction('窑系统数据可视化输出', self)

        singleOutAct = QAction('独立因素热耗分析结果输出', self)

        mulOutAct = QAction('联合因素热耗分析结果输出', self)

        heatOutAct = QAction('窑系统热耗结果输出', self)

        warningOutAct = QAction('生产预警结果输出', self)

        errorOutAct = QAction('生产异常结果输出', self)

        # 维护模块
        userManageAct = QAction('用户管理', self)

        dataBackupAct = QAction('数据备份', self)

        dataRecAct = QAction('数据恢复', self)

        knowBackupAct = QAction('知识库备份', self)

        sysLogAct = QAction('系统日志', self)

        sysHelpAct = QAction('系统帮助', self)

        # 退出模块
        userChangeAct = QAction('用户切换', self)

        userLoginAct = QAction('用户登陆', self)

        exitAct = QAction('系统退出', self)  # exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出系统')
        exitAct.triggered.connect(qApp.exit)

        self.menubar = self.menuBar()
        self.status = self.statusBar()

        dataMenu = self.menubar.addMenu('数据')
        dataMenu.addAction(dataInputAct)
        dataMenu.addAction(openFileAct)
        dataMenu.addAction(saveFileAct)
        dataMenu.addAction(saveasFileAct)
        dataMenu.addSeparator()
        dataMenu.addAction(changeDataAct)
        dataMenu.addAction(simulateDataAct)
        dataMenu.addSeparator()
        dataMenu.addAction(leadInAct)
        dataMenu.addAction(leadOutAct)

        visualMenu = self.menubar.addMenu('窑系统热耗分析可视化')
        visualMenu.addAction(dataVisualAct)
        visualMenu.addSeparator()
        visualMenu.addAction(singleVisualAct)
        visualMenu.addAction(mulVisualAct)
        visualMenu.addSeparator()
        visualMenu.addAction(heatVisualAct)
        visualMenu.addSeparator()
        visualMenu.addAction(deviceVisualAct)

        guideMenu = self.menubar.addMenu('窑系统生产指导')
        guideMenu.addAction(warningAct)
        guideMenu.addAction(warningGuideAct)
        guideMenu.addSeparator()
        guideMenu.addAction(errorAct)
        guideMenu.addAction(errorGuideAct)

        setMenu = self.menubar.addMenu('窑系统设置')
        setMenu.addAction(deviceSetAct)
        setMenu.addAction(dataSetAct)
        setMenu.addSeparator()
        setMenu.addAction(userSetAct)
        setMenu.addSeparator()
        setMenu.addAction(standardSetAct)
        setMenu.addSeparator()
        setMenu.addAction(objectSetAct)

        outputMenu = self.menubar.addMenu('结果输出')
        outputMenu.addAction(dataOutAct)
        outputMenu.addSeparator()
        outputMenu.addAction(singleOutAct)
        outputMenu.addAction(mulOutAct)
        outputMenu.addAction(heatOutAct)
        outputMenu.addSeparator()
        outputMenu.addAction(warningOutAct)
        outputMenu.addAction(errorOutAct)

        defendMenu = self.menubar.addMenu('系统维护')
        defendMenu.addAction(userManageAct)
        defendMenu.addSeparator()
        defendMenu.addAction(dataBackupAct)
        defendMenu.addAction(dataRecAct)
        defendMenu.addSeparator()
        defendMenu.addAction(knowBackupAct)
        defendMenu.addSeparator()
        defendMenu.addAction(sysLogAct)
        defendMenu.addSeparator()
        defendMenu.addAction(sysHelpAct)

        exitMenu = self.menubar.addMenu('退出')
        exitMenu.addAction(userChangeAct)
        exitMenu.addSeparator()
        exitMenu.addAction(userLoginAct)
        exitMenu.addAction(exitAct)

    '''def initPic(self):

        metric_width = GetSystemMetrics(0)
        metric_height = GetSystemMetrics(1)  # 获取电脑分辨率
        self.width = metric_width  # 图片宽度
        self.height = metric_height  # 图片高度

        self.pic_x = 40
        self.pic_y = 200  # 图片起始点
        # 设置信息显示区域
        self.setWindowTitle("Cement Kiln")
        self.widget = QWidget()
        self.table = QTableWidget(0, 2)  # 以表格形式显示数据
        self.table.setMinimumHeight(100)
        self.messageView = QTabWidget()
        self.messageView.setMinimumHeight(100)

        # self.resize(self.width,self.height)

        self.table.horizontalHeader().setDefaultSectionSize(150)
        self.messageSplitter = QSplitter(Qt.Vertical)
        self.messageSplitter.addWidget(self.table)
        self.messageSplitter.addWidget(self.messageView)
        # self.messageSplitter.addWidget(self.functionList)
        self.mainSplitter = QSplitter(Qt.Horizontal)
        self.mainSplitter.addWidget(self.widget)
        self.mainSplitter.addWidget(self.messageSplitter)
        self.setCentralWidget(self.mainSplitter)

        self.table.setMaximumHeight(300)

        self.tab1 = QLabel()
        self.tab2 = QLabel()
        self.messageView.addTab(self.tab1, '温度')
        self.messageView.addTab(self.tab2, '压强')
        self.pic1 = QVBoxLayout(self.tab1)
        self.pic2 = QVBoxLayout(self.tab2)

        self.click_flag = 0

        xft_dl = QPixmap('picture\\xft_dl.png')  # 旋风筒
        xft_zuo = QPixmap('picture\\xft_zuo.png')  # 旋风筒左管
        xft_you = QPixmap('picture\\xft_you.png')  # 旋风筒右管
        fjl = QPixmap('picture\\fjl.png')  # 分解炉
        blj = QPixmap('picture\\blj.png')  # 篦冷机
        fjl_yao = QPixmap('picture\\fjl_yao')  # 分解炉与窑之间的连接部件
        mfc = QPixmap('picture\\mfc.png')  # 煤粉仓
        gwfj = QPixmap('picture\\gwfj.png')  # 高温风机
        ljg_sp = QPixmap('picture\\ljg_sp.png')  # 水平连接管
        ljg_sz = QPixmap('picture\\ljg_sz.png')  # 竖直连接管
        ljg_zj_1 = QPixmap('picture\\ljg_1.png')  # 左上
        ljg_zj_2 = QPixmap('picture\\ljg_2.png')  # 右上
        ljg_zj_3 = QPixmap('picture\\ljg_zj_3.png')  # 左下
        ljg_zj_4 = QPixmap('picture\\ljg_zj_4.png')  # 右下

        yao = QPixmap('picture\\yao.png')
        ratio = 0.3  # 图片放大倍数

        self.l1 = MyLabel()
        self.l1.setPixmap(xft_dl.scaled(xft_dl.width() * ratio, xft_dl.height() * ratio))
        self.l1.setObjectName('一级筒A')
        self.l1.changeindex.connect(self.change_pic)
        self.widget.autoFillBackground()

        self.l2 = MyLabel()
        self.l2.setPixmap(xft_you.scaled(xft_you.width() * ratio, xft_you.height() * ratio))
        self.l2.setObjectName('一级筒A')
        self.l2.changeindex.connect(self.change_pic)

        self.l3 = MyLabel()
        self.l3.setPixmap(xft_zuo.scaled(xft_zuo.width() * ratio, xft_zuo.height() * ratio))
        self.l3.setObjectName('二级筒A')
        self.l3.changeindex.connect(self.change_pic)

        self.l4 = MyLabel()
        self.l4.setPixmap(xft_you.scaled(xft_you.width() * ratio, xft_you.height() * ratio))
        self.l4.setObjectName('三级筒A')
        self.l4.changeindex.connect(self.change_pic)

        self.l5 = MyLabel()
        self.l5.setPixmap(xft_zuo.scaled(xft_zuo.width() * ratio, xft_zuo.height() * ratio))
        self.l5.setObjectName('四级筒A')
        self.l5.changeindex.connect(self.change_pic)

        self.l6 = MyLabel()
        self.l6.setPixmap(xft_dl.scaled(xft_dl.width() * ratio, xft_dl.height() * ratio))
        self.l6.setObjectName('五级筒A')
        self.l6.changeindex.connect(self.change_pic)

        self.lab_fjl = MyLabel()
        self.lab_fjl.setPixmap(fjl.scaled(xft_dl.width() * 6.9 * ratio, xft_dl.width() * 3 * ratio))
        self.lab_fjl.setObjectName('分解炉')
        self.lab_fjl.changeindex.connect(self.change_pic)

        self.ljg_sp = QLabel()
        self.ljg_sp.setPixmap(ljg_sp.scaled(ljg_sp.width() * ratio, ljg_sp.height() * ratio))

        

        self.lab_yao = MyLabel()
        self.lab_yao.setPixmap(yao.scaled(xft_dl.width() * 9 * ratio, yao.height() * ratio))
        self.lab_yao.setObjectName('窑')
        self.lab_yao.changeindex.connect(self.change_pic)

        self.lab_blj = MyLabel()
        self.lab_blj.setPixmap(blj.scaled(blj.width() * ratio, blj.height() * ratio))
        self.lab_blj.setObjectName('篦冷机')
        self.lab_blj.changeindex.connect(self.change_pic)

        

        self.fjl_yao = MyLabel()
        self.fjl_yao.setPixmap(fjl_yao.scaled(fjl_yao.width() * ratio, fjl_yao.height() * ratio))
        self.fjl_yao.setObjectName('分解炉--窑')

        lay = QGridLayout()
        x0 = 0
        y0 = 0  # 初始位置
        dx = 3
        dy = 3  # 跨越列行
        lay.addWidget(self.l1, x0, y0)  # 1级筒A
        lay.addWidget(self.l2, x0, y0 + 1, 1, 2)  # 1级筒A
        lay.addWidget(self.l3, x0 + 1, y0 + 1, 1, 2)  # 2级筒A
        lay.addWidget(self.l4, x0 + 2, y0 + 1, 1, 2)  # 3级筒A
        lay.addWidget(self.l5, x0 + 3, y0 + 1, 1, 2)  # 4级筒A
        lay.addWidget(self.lab_fjl, x0 + 3, y0 + 1, dx, dy + 4)  # 分解炉
        lay.addWidget(self.l6, x0 + 4, y0 + 1)  # 5级筒A
        lay.addWidget(self.fjl_yao, x0 + 6, y0 + 4)

        

        lay.addWidget(self.lab_yao, x0 + 6, y0 + 5, 2, dy * 3)  # 窑
        lay.addWidget(self.lab_blj, x0 + 6, y0 + 16, 2, dy)  # 篦冷机

        lay.addWidget(self.l11, x0 + 0, y0 + 6, 1, 2)  # 1级筒B
        lay.addWidget(self.l12, x0 + 0, y0 + 8, 1, 2)  # 1级筒B
        lay.addWidget(self.l13, x0 + 1, y0 + 6, 1, 2)  # 2级筒B
        lay.addWidget(self.l14, x0 + 2, y0 + 6, 1, 2)  # 3级筒B
        lay.addWidget(self.l15, x0 + 3, y0 + 6, 1, 2)  # 4级筒B
        lay.addWidget(self.l16, x0 + 4, y0 + 7)  # 5级筒B
        # lay.addWidget(QLabel(''), 8, 5, 10, 3)

        lay.setSpacing(0)
        lay.setAlignment(Qt.AlignLeft | Qt.AlignCenter)

        self.widget.setLayout(lay)
        # self.widget.move(100,100)'''

    def change_pic(self, click_flag):
        # print(self.click_flag)
        if self.click_flag == 0:
            self.fp1 = MyTempMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.fp2 = MyPressMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.pic1.addWidget(self.fp1)
            self.pic2.addWidget(self.fp2)
            self.click_flag = 1
        elif self.click_flag == 1:
            self.sp1 = MyTempMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.sp2 = MyPressMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.pic1.replaceWidget(self.fp1, self.sp1)
            self.pic2.replaceWidget(self.fp2, self.sp2)
            self.click_flag = 2
        elif self.click_flag == 2:
            self.fp1 = MyTempMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.fp2 = MyPressMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.pic1.replaceWidget(self.sp1, self.fp1)
            self.pic2.replaceWidget(self.sp2, self.fp2)
            self.click_flag = 1

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
        # self.QPainter.drawRect(x1, y1, x2, y2)
        # self.QPainter.drawRect(50, 50, 50, 50)


class MyWindow2(QWidget):
    yao_par_signal = pyqtSignal(int, str)

    def __init__(self):
        super(MyWindow2, self).__init__()

        self.setWindowTitle('配置设备')
        self.resize(400, 300)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)  # 禁止窗口最大化
        self.setFixedSize(self.width(), self.height())  # 禁止拉伸窗口

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 291, 78))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle('窑系统类型')

        self.serial_sin = QRadioButton('单系列', self.groupBox)
        self.serial_sin.setGeometry(QtCore.QRect(50, 30, 106, 16))
        self.serial_dou = QRadioButton('双系列', self.groupBox)
        self.serial_dou.setGeometry(QtCore.QRect(170, 30, 161, 16))
        self.serial_sin.setChecked(True)

        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 110, 291, 101))
        self.groupBox_2.setTitle('旋风筒参数')
        self.xft_num = QtWidgets.QComboBox(self.groupBox_2)
        self.xft_num.setGeometry(QtCore.QRect(150, 40, 69, 22))
        self.xft_num.setObjectName("comboBox")
        self.label_xft = QLabel('旋风筒个数', self.groupBox_2)
        self.label_xft.setGeometry(QtCore.QRect(63, 42, 61, 20))
        self.num = ['4', '5', '6']
        for i in self.num:
            self.xft_num.addItem(i)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def accept(self):
        if self.serial_sin.isChecked():
            flag = 1
        else:
            flag = 2
        self.yao_par_signal.emit(flag, self.xft_num.currentText())
        self.close()

    def reject(self):
        self.close()


class MyLabel(QLabel):
    changeindex = pyqtSignal(int)  # 单击窑系统部件时会发出信号

    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

    def call_win(self, int):
        self.changeindex.emit(int)

    def mousePressEvent(self, e):
        global flag, index_T, index_P
        if flag == 1:  # 判断是否选择了时间
            if self.objectName() == '1级筒A':
                index_T = 8
                index_P = 9
                self.call_win(index_T)
            elif self.objectName() == '1级筒B':
                index_T = 10
                index_P = 11
                self.call_win(index_T)
            elif self.objectName() == '2级筒A':
                index_T = 12
                index_P = 13
                self.call_win(index_T)
            elif self.objectName() == '2级筒B':
                index_T = 14
                index_P = 15
                self.call_win(index_T)
            elif self.objectName() == '3级筒A':
                index_T = 16
                index_P = 17
                self.call_win(index_T)
            elif self.objectName() == '3级筒B':
                index_T = 18
                index_P = 19
                self.call_win(index_T)
            elif self.objectName() == '4级筒A':
                index_T = 20
                index_P = 21
                self.call_win(index_T)
            elif self.objectName() == '4级筒B':
                index_T = 22
                index_P = 23
                self.call_win(index_T)
            elif self.objectName() == '5级筒A':
                index_T = 24
                index_P = 25
                self.call_win(index_T)
            elif self.objectName() == '5级筒B':
                index_T = 26
                index_P = 27
                self.call_win(index_T)
            elif self.objectName() == '分解炉':
                index_T = 29
                index_P = 30
                self.call_win(index_T)
            elif self.objectName() == '窑':
                index_T = 28
                index_P = 0
                self.call_win(index_T)
            elif self.objectName() == '篦冷机':
                index_T = 33
                index_P = 0
                self.call_win(index_T)
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

    def cal_null(self, str):
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
        global day, index_T
        if index_T == 0:
            pass
        else:
            tablevalue = get_by_day(day)
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


class MyPressMplCanvas(MyMplCanvas):
    """压强画布"""

    def compute_initial_figure(self):
        global day, index_P
        if index_P == 0:
            pass
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWindow()
    form.show()
    app.exec_()
