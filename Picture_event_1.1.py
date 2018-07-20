import sys
import random
from provide_data_for_gui import *
from win32api import GetSystemMetrics

from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import *#QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter,QIcon,QPixmap

import matplotlib.font_manager as fm
import matplotlib
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
global day,flag,index,MyWindow


myfont = fm.FontProperties(fname="C:\\Windows\\Fonts\\simsun.ttc", size=14)#设置字体，实现显示中文
matplotlib.rcParams["axes.unicode_minus"] = False



class MyWindow(QMainWindow):
    global flag
    flag=0
    def __init__(self,parent=None):
        super(MyWindow,self).__init__(parent)

        self.initPic()
        self.initMenu()
        self.initBtn()

    def on_click(self):
        self.setTime()
    def double_click(self):
        global day,flag
        flag=1

        self.calendar.hide()
        date=self.calendar.selectedDate().toString('yyyy-MM-dd')#日期显示格式 例:2017-01-02
        date_input = '12345678'
        date_input = date[:4]+date[5:7]+date[8:10]
        self.timeBtn.setText(date)

        day=int(date_input)
        #print(day)
        '''col1,col2=get_by_hour(day)

        self.table.setRowCount(len(col1))
        self.table.setHorizontalHeaderLabels(['名称','数值'])
        for i in range(len(col1)):
            newItem = QTableWidgetItem(col1[i])
            self.table.setItem(i, 0, newItem)
            newItem = QTableWidgetItem(str(col2[i]))
            self.table.setItem(i, 1, newItem)'''



    def initBtn(self):
        self.timeBtn=QPushButton('双击确定',self.widget)
        self.timeBtn.move(self.width*0.5,40)
        self.timeBtn.clicked.connect(self.on_click)
        self.timeBtn.show()

        self.timeLabel = QLabel(self.widget)
        self.timeLabel.move(self.width*0.5-30, 45)
        self.timeLabel.resize(30,20)
        self.timeLabel.setText('日期')
        self.timeLabel.show()
    def setTime(self):
        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate(2002,6,19))
        self.calendar.setSelectedDate(QDate(2017,1,23))
        self.calendar.resize(400, 300)
        self.calendar.move(0,23)
        self.calendar.show()
        self.calendar.activated.connect(self.double_click)



    def dataVisual(self):
        print("窑系统数据可视化")

    def initMenu(self):

        #数据模块
        dataInputAct=QAction('数据输入',self)

        openFileAct = QAction('打开数据文件', self)

        saveFileAct = QAction('数据保存', self)

        saveasFileAct = QAction('数据另存为', self)

        changeDataAct = QAction('数据修改', self)

        simulateDataAct = QAction('数据模拟', self)

        leadInAct = QAction('数据导入', self)

        leadOutAct = QAction('数据导出', self)
        #可视化模块
        dataVisualAct = QAction('窑系统数据可视化', self)
        dataVisualAct.setStatusTip('数据可视化')
        dataVisualAct.triggered.connect(self.dataVisual)

        singleVisualAct = QAction('独立因素热耗分析可视化', self)

        mulVisualAct = QAction('联合因素热耗分析可视化', self)

        heatVisualAct = QAction('窑系统热耗可视化', self)

        deviceVisualAct = QAction('窑系统设备热耗可视化', self)
        #生产指导模块
        warningAct = QAction('生产预警', self)

        warningGuideAct = QAction('生产预警指导', self)

        errorAct = QAction('生产异常报警', self)

        errorGuideAct = QAction('生产异常指导', self)
        #设置模块
        deviceSetAct = QAction('窑系统设备', self)

        dataSetAct = QAction('窑系统数据', self)

        userSetAct = QAction('用户设置', self)

        standardSetAct = QAction('生产数据标准设置', self)

        objectSetAct = QAction('可视化对象设置', self)
        #输出模块
        dataOutAct = QAction('窑系统数据可视化输出', self)

        singleOutAct = QAction('独立因素热耗分析结果输出', self)

        mulOutAct = QAction('联合因素热耗分析结果输出', self)

        heatOutAct = QAction('窑系统热耗结果输出', self)

        warningOutAct = QAction('生产预警结果输出', self)

        errorOutAct = QAction('生产异常结果输出', self)
        #维护模块
        userManageAct = QAction('用户管理', self)

        dataBackupAct = QAction('数据备份', self)

        dataRecAct = QAction('数据恢复', self)

        knowBackupAct = QAction('知识库备份', self)

        sysLogAct = QAction('系统日志', self)

        sysHelpAct = QAction('系统帮助', self)
        #退出模块
        userChangeAct = QAction('用户切换', self)

        userLoginAct = QAction('用户登陆', self)

        exitAct = QAction('系统退出', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出系统')
        exitAct.triggered.connect(qApp.exit)

        self.menubar=self.menuBar()
        self.status = self.statusBar()

        dataMenu=self.menubar.addMenu('数据')
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

    def initPic(self):

        metric_width = GetSystemMetrics(0)
        metric_height = GetSystemMetrics(1)#获取电脑分辨率
        self.width = metric_width # 图片宽度
        self.height = metric_height # 图片高度

        self.pic_x = 40
        self.pic_y = 200  # 图片起始点
        #设置信息显示区域
        self.setWindowTitle("Cement Kiln")
        self.widget = QWidget(self)
        self.table = QTableWidget(0, 2) #以表格形式显示数据
        self.table.setMinimumHeight(100)
        self.messageView = QWidget()
        self.messageView.setMinimumHeight(100)

        #self.resize(self.width,self.height)

        self.table.horizontalHeader().setDefaultSectionSize(150)
        self.messageSplitter = QSplitter(Qt.Vertical)
        self.messageSplitter.addWidget(self.table)
        self.messageSplitter.addWidget(self.messageView)
        #self.messageSplitter.addWidget(self.functionList)
        self.mainSplitter = QSplitter(Qt.Horizontal)
        self.mainSplitter.addWidget(self.widget)
        self.mainSplitter.addWidget(self.messageSplitter)
        self.setCentralWidget(self.mainSplitter)

        self.table.setMaximumHeight(300)

        self.l = QVBoxLayout(self.messageView)
        self.click_flag = 0

        xft = QPixmap('picture\\xft_dl.png')#旋风筒
        fjl = QPixmap('picture\\fjl.png')#分解炉
        blj = QPixmap('picture\\blj.png')#篦冷机
        mfc = QPixmap('picture\\mfc.png')#煤粉仓
        gwfj = QPixmap('picture\\gwfj.png')#高温风机
        ljg_sp = QPixmap('picture\\ljg_sp.png')#水平连接管
        ljg_sz = QPixmap('picture\\ljg_sz.png')#竖直连接管
        yao = QPixmap('picture\\yao.png')

        self.l1=MyLabel()
        self.l1.setPixmap(xft)
        self.l1.setObjectName('一级筒A')
        self.l1.changeindex.connect(self.change_pic)

        self.l2 = MyLabel()
        self.l2.setPixmap(xft)
        self.l2.setObjectName('一级筒A')
        self.l2.changeindex.connect(self.change_pic)

        self.l3 = MyLabel()
        self.l3.setPixmap(xft)
        self.l3.setObjectName('二级筒A')
        self.l3.changeindex.connect(self.change_pic)

        self.l4 = MyLabel()
        self.l4.setPixmap(xft)
        self.l4.setObjectName('三级筒A')
        self.l4.changeindex.connect(self.change_pic)

        self.l5 = MyLabel()
        self.l5.setPixmap(xft)
        self.l5.setObjectName('四级筒A')
        self.l5.changeindex.connect(self.change_pic)

        self.l6 = MyLabel()
        self.l6.setPixmap(xft)
        self.l6.setObjectName('五级筒A')
        self.l6.changeindex.connect(self.change_pic)

        self.l7 = MyLabel()
        self.l7.setPixmap(fjl)
        self.l7.setObjectName('分解炉')
        self.l7.changeindex.connect(self.change_pic)

        self.l8=MyLabel()
        self.l8.setPixmap(ljg_sp)
        self.l8.setObjectName('水平连接管')
        self.l8.changeindex.connect(self.change_pic)

        self.l9 = MyLabel()
        self.l9.setPixmap(yao)
        self.l9.setObjectName('窑')
        self.l9.changeindex.connect(self.change_pic)


        self.l10 = MyLabel()
        self.l10.setPixmap(blj)
        self.l10.setObjectName('篦冷机')
        self.l10.changeindex.connect(self.change_pic)

        self.l11 = MyLabel()
        self.l11.setPixmap(xft)
        self.l11.setObjectName('一级筒B')
        self.l11.changeindex.connect(self.change_pic)

        self.l12 = MyLabel()
        self.l12.setPixmap(xft)
        self.l12.setObjectName('一级筒B')
        self.l12.changeindex.connect(self.change_pic)

        self.l13 = MyLabel()
        self.l13.setPixmap(xft)
        self.l13.setObjectName('二级筒B')
        self.l13.changeindex.connect(self.change_pic)

        self.l14 = MyLabel()
        self.l14.setPixmap(xft)
        self.l14.setObjectName('三级筒B')
        self.l14.changeindex.connect(self.change_pic)

        self.l15 = MyLabel()
        self.l15.setPixmap(xft)
        self.l15.setObjectName('四级筒B')
        self.l15.changeindex.connect(self.change_pic)

        self.l16 = MyLabel()
        self.l16.setPixmap(xft)
        self.l16.setObjectName('五级筒B')
        self.l16.changeindex.connect(self.change_pic)

        lay=QGridLayout()


        lay.addWidget(self.l1, 0, 0)
        lay.addWidget(self.l2, 0, 1)
        lay.addWidget(self.l3, 1, 2)
        lay.addWidget(self.l4, 2, 1)
        lay.addWidget(self.l5, 3, 2)
        lay.addWidget(self.l6, 4, 1)
        lay.addWidget(self.l7, 3, 4)
        lay.addWidget(self.l8, 3, 3)

        lay.addWidget(self.l9, 5, 5, 6, 8)
        lay.addWidget(self.l10, 6, 9)

        lay.addWidget(self.l11, 0, 6)
        lay.addWidget(self.l12, 0, 7)
        lay.addWidget(self.l13, 1, 5)
        lay.addWidget(self.l14, 2, 6)
        lay.addWidget(self.l15, 3, 5)
        lay.addWidget(self.l16, 4, 6)

        lay.setSpacing(0)
        lay.setAlignment(Qt.AlignLeft)

        self.widget.setLayout(lay)
        self.widget.move(100,100)

        self.resize(800,600)
        self.showMaximized()

    def change_pic(self,click_flag):
        print(click_flag)
        if self.click_flag == 0:
            self.fp = MyStaticMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.l.addWidget(self.fp)
            self.click_flag = 1
        elif self.click_flag == 1:
            self.sp = MyStaticMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.l.replaceWidget(self.fp, self.sp)
            self.click_flag = 2
        elif self.click_flag == 2:
            self.fp = MyStaticMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.l.replaceWidget(self.sp, self.fp)
            self.click_flag = 1


            #                self.messageView.setText("煤粉仓")
    '''def mousePressEvent(self, QMouseEvent):
        globalPos = self.mapToGlobal(QMouseEvent.pos())
        global index
        #print("The mouse is at (%d,%d)" % (QMouseEvent.pos().x(), QMouseEvent.pos().y()))
        x=QMouseEvent.pos().x()-self.pic_x
        y=QMouseEvent.pos().y()-self.pic_y
        menuwidth=23
        y=y-menuwidth

        ratio_x=self.change_x
        if self.flag == 1:#判断是否选择了时间
            #l.setObjectName('picture')
            if x>34*ratio_x and x<88*ratio_x and y>28*ratio_x and y<73*ratio_x:
                index = 8
                self.change_pic()
                #1级旋风筒
            if x > 101*ratio_x and x < 155*ratio_x and y > 65*ratio_x and y < 109*ratio_x:
                index = 12
                self.change_pic()
                #2级旋风筒
            if x > 34*ratio_x and x < 88*ratio_x and y > 105*ratio_x and y < 149*ratio_x:
                index = 17
                self.change_pic()
                # 3级旋风筒
            if x > 102*ratio_x and x < 155*ratio_x and y > 143*ratio_x and y < 189*ratio_x:
                index = 21
                self.change_pic()
                # 4级旋风筒
            if x > 34*ratio_x and x < 88*ratio_x and y > 196*ratio_x and y < 242*ratio_x:
                index = 24
                self.change_pic()
                # 5级旋风筒
            if x > 146*ratio_x and x < 204*ratio_x and y > 197*ratio_x and y < 241*ratio_x:
                index = 29
                self.change_pic()
                #self.messageView.setText("分解炉")
            if x > 218*ratio_x and x < 251*ratio_x and y > 272*ratio_x and y < 322*ratio_x:
                index = 28
                self.change_pic()
                #self.messageView.setText("窑尾")
            if x > 252*ratio_x and x < 290*ratio_x and y > 272*ratio_x and y < 321*ratio_x:
                index = 8
                self.change_pic()
                #                self.messageView.setText("预热带")
            if x > 297*ratio_x and x < 345*ratio_x and y > 272*ratio_x and y < 322*ratio_x:
                index = 8
                self.change_pic()
                #self.messageView.setText("分解带")
            if x > 352*ratio_x and x < 393*ratio_x and y > 272*ratio_x and y < 322*ratio_x:
                index = 8
                self.change_pic()
                #                self.messageView.setText("烧成带")
            if x > 399*ratio_x and x < 440*ratio_x and y > 272*ratio_x and y < 322*ratio_x:
                index = 8
                self.change_pic()
                #                self.messageView.setText("冷却带")
            if x > 426*ratio_x and x < 479*ratio_x and y > 272*ratio_x and y < 322*ratio_x:
                index = 5
                self.change_pic()
                #                self.messageView.setText("窑头")
            if x > 498*ratio_x and x < 540*ratio_x and y > 298*ratio_x and y < 323*ratio_x:
                index = 33
                self.change_pic()
                #                self.messageView.setText("篦冷机1段")
            if x > 544*ratio_x and x < 584*ratio_x and y > 298*ratio_x and y < 323*ratio_x:
                index = 36
                self.change_pic()
                #                self.messageView.setText("篦冷机2段")
            if x > 587*ratio_x and x < 633*ratio_x and y > 298*ratio_x and y < 323*ratio_x:
                index = 38
                self.change_pic()
                #                self.messageView.setText("篦冷机3段")
            if x > 370*ratio_x and x < 427*ratio_x and y > 121*ratio_x and y < 164*ratio_x:
                index = 40
                self.change_pic()
                #                self.messageView.setText("高温风机")
            if x > 426*ratio_x and x < 479*ratio_x and y > 345*ratio_x and y < 369*ratio_x:
                index = 0
                self.change_pic()
                #                self.messageView.setText("煤粉仓")
        else:
            self.msg()'''

    def msg(self):
        reply=QMessageBox.information(self,'提示','请先选择时间',QMessageBox.Yes|QMessageBox.No)

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

class MyLabel(QLabel):
    changeindex = pyqtSignal(int)
    def __init__(self,parent=None):
        super(MyLabel,self).__init__(parent)

    def call_win(self,int):
        self.changeindex.emit(int)

    def mousePressEvent(self,e):
        global flag,index
        if flag == 1:  # 判断是否选择了时间
            if self.objectName() == '一级筒A':
                index = 8
                self.call_win(index)
            elif self.objectName() == '一级筒B':
                index = 10
                self.call_win(index)
            elif self.objectName() == '二级筒A':
                index = 12
                self.call_win(index)
            elif self.objectName() == '二级筒B':
                index = 14
                self.call_win(index)
            elif self.objectName() == '三级筒A':
                index = 16
                self.call_win(index)
            elif self.objectName() == '三级筒B':
                index = 18
                self.call_win(index)
            elif self.objectName() == '四级筒A':
                index = 20
                self.call_win(index)
            elif self.objectName() == '四级筒B':
                index = 23
                self.call_win(index)
            elif self.objectName() == '五级筒A':
                index = 24
                self.call_win(index)
            elif self.objectName() == '五级筒B':
                index = 26
                self.call_win(index)
            elif self.objectName() == '分解炉':
                index = 29
                self.call_win(index)
            elif self.objectName() == '窑':
                index = 32
                self.call_win(index)
            elif self.objectName() == '篦冷机':
                index = 33
                self.call_win(index)
        else :
            self.msg()

    def msg(self):
        reply = QMessageBox.information(self, '提示', '请先选择时间', QMessageBox.Yes | QMessageBox.No)

class MyMplCanvas(FigureCanvas):
    """这是一个窗口部件，即QWidget（当然也是FigureCanvasAgg）"""
    def __init__(self, parent=None, width=3, height=4, dpi=100):
        global index,day
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # 每次plot()调用的时候，我们希望原来的坐标轴被清除(所以False)
        self.axes.hold(False)

        self.compute_initial_figure()

        tablename = get_by_day(day)
        self.axes.set_title(tablename[0][index], fontproperties=myfont)
        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

class MyStaticMplCanvas(MyMplCanvas):
    """静态画布：一条正弦线"""
    def compute_initial_figure(self):
        global day,index
        t = arange(0, 24, 1)
        tablevalue = get_by_day(day)
        '''for i in range(len(tablevalue)):
            print(i)
            print(tablevalue[0][i])'''
        self.axes.plot(t, tablevalue[1][index])

class MyDynamicMplCanvas(MyMplCanvas):
    """动态画布：每秒自动更新，更换一条折线。"""
    def __init__(self, *args, **kwargs):
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
        self.draw()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    form = MyWindow()
    form.show()
    app.exec_()
