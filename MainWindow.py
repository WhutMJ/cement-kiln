import sys
from MyPic import *
from win32api import GetSystemMetrics

from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    con.setValue_flag_Time(0)  # 是否选择时间的标志初始化为0
    con.setValue_hour(0)

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        metric_width = GetSystemMetrics(0)
        metric_height = GetSystemMetrics(1)  # 获取电脑分辨率
        self.resize(metric_width, metric_height - 30)
        self.showMaximized()
        self.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(46, 139, 130))  # 更改背景色
        self.setPalette(palette)

        self.initMenu()  # 初始化菜单栏
        self.updatePic()  # 加载图片资源
        self.setTimer()  # 设定计时器，稍后会摆在正确位置

        self.set_window = MyWindow2()  # 初始化对话框
        self.set_window.show()
        self.set_window.yao_par_signal.connect(self.initDevice)

    def initInfor(self):  # 信息栏
        self.lab_infor = QLabel(self.widget)
        self.lab_infor.setStyleSheet('background-color:white')
        self.lab_infor.resize(self.width, self.lab_infor.height())
        if con.getValue_flag_Visual() == 0:
            self.lab_infor.setText('\t窑系统设备热耗可视化\t选择时间：未选择\t热耗：无数据')
        else:
            self.lab_infor.setText('\t窑系统热耗可视化\t选择时间：未选择\t热耗：无数据')

    def updateInfor(self):

        flag_Time = con.getValue_flagTime()
        day = con.getValue_day()
        # print(con.getValue_flag_Visual())
        if con.getValue_number() != 0:  # 判断用户是否完成了窑系统配置信息
            if con.getValue_flag_Visual() == 1:

                if flag_Time == 0:
                    self.lab_infor.setText('\t窑系统热耗可视化\t选择时间：未选择\t热耗：无数据')
                elif self.click_flag == 0:
                    day_str = str(day)
                    self.lab_infor.setText(
                        '\t窑系统热耗可视化\t选择时间：%s-%s-%s\t热耗：无数据' % (day_str[0:4], day_str[4:6], day_str[6:8]))
                else:
                    day_str = str(day)
                    value = get_by_day(day)
                    self.lab_infor.setText(
                        '\t窑系统热耗可视化\t选择时间：%s-%s-%s\t热耗：' % (
                            day_str[0:4], day_str[4:6], day_str[6:8]))
            else:

                if flag_Time == 0:
                    self.lab_infor.setText('\t窑系统设备热耗可视化\t选择时间：未选择\t热耗：无数据')
                elif self.click_flag == 0:
                    day_str = str(day)
                    self.lab_infor.setText(
                        '\t窑系统设备热耗可视化\t选择时间：%s-%s-%s\t热耗：无数据' % (day_str[0:4], day_str[4:6], day_str[6:8]))
                else:
                    value = get_by_day(day)
                    day_str = str(day)
                    self.lab_infor.setText(
                        '\t窑系统设备热耗可视化\t选择时间：%s-%s-%s\t热耗：' % (
                            day_str[0:4], day_str[4:6], day_str[6:8]))

    def initDevice(self, flag_Seri, num):
        #self.lay.deleteAllItems()
        metric_width = GetSystemMetrics(0)
        metric_height = GetSystemMetrics(1)  # 获取电脑分辨率
        self.width = metric_width  # 图片宽度
        self.height = metric_height  # 图片高度
        self.click_flag = 0  # 折线图的切换图片标志

        # 设置信息显示区域
        self.setWindowTitle("Cement Kiln")
        self.widget = QWidget()
        self.table = QTableWidget(0, 2)  # 以表格形式显示数据
        self.table.setMinimumHeight(100)
        self.messageView = QTabWidget()
        self.messageView.setMinimumHeight(100)
        self.messageView.setMinimumWidth(400)  # 设置右边信息栏的最小宽度

        # self.resize(self.width,self.height)

        self.table.horizontalHeader().setDefaultSectionSize(200)
        self.messageSplitter = QSplitter(Qt.Vertical)
        self.messageSplitter.addWidget(self.table)
        self.messageSplitter.addWidget(self.messageView)

        self.mainSplitter = QSplitter(Qt.Horizontal)
        self.mainSplitter.addWidget(self.widget)
        self.mainSplitter.addWidget(self.messageSplitter)
        self.setCentralWidget(self.mainSplitter)

        self.table.setMaximumHeight(300)

        self.initInfor()  # 初始化信息栏

        self.tab1 = QLabel()
        self.tab2 = QLabel()
        self.messageView.addTab(self.tab1, '温度')
        self.messageView.addTab(self.tab2, '压强')
        self.pic1 = QVBoxLayout(self.tab1)
        self.pic2 = QVBoxLayout(self.tab2)

        con.setValue_flag_Ser(flag_Seri)
        con.setValue_number(int(num))
        self.update_normal_Pic()#重置为正常图片
        self.initPic()  # 初始化窑系统各部件

        self.initBtn()  # 初始化时间选择控件

    def on_click(self):  # 单击选择时间按钮
        print(self.flag_timeBtn)
        if self.flag_timeBtn == 0:
            self.flag_timeBtn = 1
            self.calendar = QCalendarWidget(self)
            self.calendar.setMinimumDate(QDate(2002, 6, 19))
            self.calendar.setSelectedDate(QDate(2017, 1, 23))
            self.calendar.resize(400, 300)
            self.calendar.move(0, 23)
            self.calendar.show()
            self.calendar.activated.connect(self.double_click)
        else:
            self.flag_timeBtn = 0
            self.calendar.hide()

    def double_click(self):  # 双击确认时间
        con.setValue_flag_Time(1)
        self.flag_timeBtn = 0  # 选择时间后单击标志归零

        self.update_normal_Pic()
        self.initPic()
        self.calendar.hide()
        date = self.calendar.selectedDate().toString('yyyy-MM-dd')  # 日期显示格式 例:2017-01-02
        date_input = '12345678'
        date_input = date[:4] + date[5:7] + date[8:10]
        self.timeBtn.setText(date)

        con.setValue_day(int(date_input))

        self.updateInfor()

    def initPic(self):#初始化布局

        # self.widget.autoFillBackground()
        if con.getValue_flagTime()==0:
            self.lay = QGridLayout()
        xft_row = 1  # 旋风筒所占行数
        xft_col = 2  # 旋风筒所占列数
        fjl_row = 3  # 分解炉所占行数
        fjl_col = 5  # 分解炉所占列数
        number = con.getValue_number()
        flag_Ser = con.getValue_flag_Ser()

        if number % 2 == 0:
            self.lay.addWidget(self.lab_fjl, number - 2, 2, fjl_row, fjl_col)  # 分解炉
            self.lay.addWidget(self.xft[number], number - 1, 2)
            self.lay.addWidget(self.fjl_yao, number - 2 + fjl_row, (fjl_col - 1) / 2 + 2)  # 连接件
            self.lay.addWidget(self.lab_yao, number - 2 + fjl_row, (fjl_col - 1) / 2 + 3, 2, 9)  # 窑
            self.lay.addWidget(self.lab_blj, number - 2 + fjl_row, 16, 2, 3)  # 篦冷机
        else:
            self.lay.addWidget(self.lab_fjl, number - 2, 1, fjl_row, fjl_col + 2)  # 分解炉
            self.lay.addWidget(self.xft[number], number - 1, 1)
            self.lay.addWidget(self.fjl_yao, number - 2 + fjl_row, (fjl_col - 1) / 2 + 2)  # 连接件
            self.lay.addWidget(self.lab_yao, number - 2 + fjl_row, (fjl_col - 1) / 2 + 3, 2, 9)  # 窑
            self.lay.addWidget(self.lab_blj, number - 2 + fjl_row, 16, 2, 3)  # 篦冷机

        self.lay.addWidget(self.xft[0], 0, 0)
        for i in arange(1, number):
            self.lay.addWidget(self.xft[i], i - 1, 1, xft_row, xft_col)

        if flag_Ser == 2:
            self.lay.addWidget(self.xft[number + 1], 0, 10 - flag_Ser)
            for i in arange(number + 2, 2 * number + 1):
                # print(i)
                self.lay.addWidget(self.xft[i], (i - 2) % number, 8 - flag_Ser, xft_row, xft_col)
            if number % 2 == 0:
                self.lay.addWidget(self.xft[number * 2 + 1], number - 1, 8 - flag_Ser)
            else:
                self.lay.addWidget(self.xft[number * 2 + 1], number - 1, 9 - flag_Ser)
        self.lay.setSpacing(0)
        self.lay.setAlignment(Qt.AlignLeft | Qt.AlignCenter)

        self.widget.setLayout(self.lay)

    def updatePic(self):
        # 加载正常状态下的图片
        self.xft_dl = QPixmap('picture\\xft_dl.png')  # 旋风筒
        self.xft_zuo = QPixmap('picture\\xft_zuo.png')  # 旋风筒左管
        self.xft_you = QPixmap('picture\\xft_you.png')  # 旋风筒右管
        self.fjl = QPixmap('picture\\fjl.png')  # 分解炉
        self.blj = QPixmap('picture\\blj.png')  # 篦冷机
        self.mfc = QPixmap('picture\\mfc.png')  # 煤粉仓
        self.fjl_yao1 = QPixmap('picture\\fjl_yao.png')
        self.gwfj = QPixmap('picture\\gwfj.png')  # 高温风机
        self.yao = QPixmap('picture\\yao.png')

        # 加载问题下的图片
        self.xft_dl_d = QPixmap('picture\\xft_dl_d.png')
        self.xft_zuo_d = QPixmap('picture\\xft_zuo_d.png')  # 旋风筒左管
        self.xft_you_d = QPixmap('picture\\xft_you_d.png')  # 旋风筒右管
        self.fjl_d = QPixmap('picture\\fjl_d.png')  # 分解炉
        self.blj_d = QPixmap('picture\\blj_d.png')  # 篦冷机
        self.mfc_d = QPixmap('picture\\mfc_d.png')  # 煤粉仓
        self.gwfj_d = QPixmap('picture\\gwfj_d.png')  # 高温风机
        self.yao_d = QPixmap('picture\\yao_d.png')


    def update_normal_Pic(self):

        number = con.getValue_number()
        flag_Ser = con.getValue_flag_Ser()

        self.ratio = 0.3 * self.width / 1366  # 图片放大倍数

        self.xft = {}
        self.xft[0] = MyLabel()
        self.xft[0].setPixmap(self.xft_dl.scaled(self.xft_dl.width() * self.ratio, self.xft_dl.height() * self.ratio))
        self.xft[0].setObjectName('%d级筒A' % 1)
        self.xft[0].changeindex.connect(self.change_pic)
        # print(self.xft[0].objectName())
        self.xft[number] = MyLabel()
        self.xft[number].setPixmap(
            self.xft_dl.scaled(self.xft_dl.width() * self.ratio, self.xft_dl.height() * self.ratio))
        self.xft[number].setObjectName('%d级筒A' % number)
        self.xft[number].changeindex.connect(self.change_pic)

        for i in arange(1, number, 2):  # 不会取到number,奇数旋风筒为右管
            self.xft[i] = MyLabel()
            self.xft[i].setPixmap(
                self.xft_you.scaled(self.xft_you.width() * self.ratio, self.xft_you.height() * self.ratio))
            self.xft[i].setObjectName('%d级筒A' % i)
            self.xft[i].changeindex.connect(self.change_pic)
        for i in arange(2, number, 2):  # 偶数旋风筒为左管
            self.xft[i] = MyLabel()
            self.xft[i].setPixmap(
                self.xft_zuo.scaled(self.xft_zuo.width() * self.ratio, self.xft_zuo.height() * self.ratio))
            self.xft[i].setObjectName('%d级筒A' % i)
            self.xft[i].changeindex.connect(self.change_pic)

        if flag_Ser == 2:  # 双系列
            self.xft[number + 1] = MyLabel()
            self.xft[number + 1].setPixmap(
                self.xft_dl.scaled(self.xft_dl.width() * self.ratio, self.xft_dl.height() * self.ratio))
            self.xft[number + 1].setObjectName('%d级筒B' % 1)
            self.xft[number + 1].changeindex.connect(self.change_pic)
            # print(self.xft[0].objectName())
            self.xft[2 * number + 1] = MyLabel()
            self.xft[2 * number + 1].setPixmap(
                self.xft_dl.scaled(self.xft_dl.width() * self.ratio, self.xft_dl.height() * self.ratio))
            self.xft[2 * number + 1].setObjectName('%d级筒B' % number)
            self.xft[2 * number + 1].changeindex.connect(self.change_pic)

            for i in arange(number + 2, 2 * number + 1, 2):  # 不会取到2*number,奇数旋风筒为左管
                # print(i)
                self.xft[i] = MyLabel()
                self.xft[i].setPixmap(
                    self.xft_zuo.scaled(self.xft_zuo.width() * self.ratio, self.xft_zuo.height() * self.ratio))
                self.xft[i].setObjectName('%d级筒B' % (i % (number + 1)))
                self.xft[i].changeindex.connect(self.change_pic)

            for i in arange(number + 3, 2 * number + 1, 2):  # 偶数旋风筒为右管
                # print(i)
                self.xft[i] = MyLabel()
                self.xft[i].setPixmap(
                    self.xft_you.scaled(self.xft_you.width() * self.ratio, self.xft_you.height() * self.ratio))
                self.xft[i].setObjectName('%d级筒B' % (i % (number + 1)))
                self.xft[i].changeindex.connect(self.change_pic)

        self.lab_fjl = MyLabel()
        if number % 2 == 0:
            self.lab_fjl.setPixmap(
                self.fjl.scaled(self.xft_dl.width() * 5 * self.ratio, self.xft_dl.height() * 3 * self.ratio))
        else:
            self.lab_fjl.setPixmap(
                self.fjl.scaled(self.xft_dl.width() * 7 * self.ratio, self.xft_dl.height() * 3 * self.ratio))
        self.lab_fjl.setObjectName('分解炉')
        self.lab_fjl.changeindex.connect(self.change_pic)

        self.lab_yao = MyLabel()
        self.lab_yao.setPixmap(self.yao.scaled(self.xft_dl.width() * 9 * self.ratio, self.yao.height() * self.ratio))
        self.lab_yao.setObjectName('窑')
        self.lab_yao.changeindex.connect(self.change_pic)

        self.lab_blj = MyLabel()
        self.lab_blj.setPixmap(self.blj.scaled(self.blj.width() * self.ratio, self.blj.height() * self.ratio))
        self.lab_blj.setObjectName('篦冷机')
        self.lab_blj.changeindex.connect(self.change_pic)

        self.fjl_yao = MyLabel()
        self.fjl_yao.setPixmap(
            self.fjl_yao1.scaled(self.xft_dl.width() * self.ratio, self.fjl_yao1.height() * self.ratio))
        self.fjl_yao.setObjectName('分解炉--窑')

    def judgePic(self):
        day = con.getValue_day()
        tvalue = get_by_day(day)
        hour=con.getValue_hour()
        number=con.getValue_number()
        flag_Ser=con.getValue_flag_Ser()
        if tvalue[1][8][hour] == 'null':
            pass
        elif tvalue[1][8][hour] > 300:
            self.xft[0].setPixmap(
                self.xft_dl_d.scaled(self.xft_dl_d.width() * self.ratio, self.xft_dl_d.height() * self.ratio))
            self.xft[0].setObjectName('%d级筒A' % 1)

        if tvalue[1][(number - 1) * 4 + 8][hour] == 'null':
            pass
        elif tvalue[1][(number - 1) * 4 + 8][hour] > 300:
            self.xft[number].setPixmap(
                self.xft_dl_d.scaled(self.xft_dl_d.width() * self.ratio, self.xft_dl_d.height() * self.ratio))
            self.xft[number].setObjectName('%d级筒A' % number)

        for i in arange(1, number, 2):  # 不会取到number,奇数旋风筒为右管
            if tvalue[1][(i - 1) * 4 + 8][hour] == 'null':
                pass
            elif tvalue[1][(i - 1) * 4 + 8][hour] > 300:
                self.xft[i].setPixmap(
                    self.xft_you_d.scaled(self.xft_you.width() * self.ratio, self.xft_you.height() * self.ratio))
                self.xft[i].setObjectName('%d级筒A' % i)
        for i in arange(2, number, 2):  # 偶数旋风筒为左管
            if tvalue[1][(i - 1) * 4 + 8][hour] == 'null':
                pass
            elif tvalue[1][(i - 1) * 4 + 8][hour] > 300:
                self.xft[i].setPixmap(
                    self.xft_zuo_d.scaled(self.xft_zuo.width() * self.ratio, self.xft_zuo.height() * self.ratio))
                self.xft[i].setObjectName('%d级筒A' % i)
        if flag_Ser==2:
            if tvalue[1][10][hour]=='null':
                pass
            elif tvalue[1][10][hour]>300:
                self.xft[number + 1].setPixmap(
                    self.xft_dl_d.scaled(self.xft_dl.width() * self.ratio, self.xft_dl.height() * self.ratio))
                self.xft[number + 1].setObjectName('%d级筒B' % 1)
            if tvalue[1][(number-1)*4+10][hour]=='null':
                pass
            elif tvalue[1][(number-1)*4+10][hour]>300:
                self.xft[2 * number + 1].setPixmap(
                    self.xft_dl_d.scaled(self.xft_dl.width() * self.ratio, self.xft_dl.height() * self.ratio))
                self.xft[2 * number + 1].setObjectName('%d级筒B' % number)
            for i in arange(number + 2, 2 * number + 1, 2):  # 不会取到2*number,奇数旋风筒为左管
                if tvalue[1][(i-number-1)*4+10][hour]=='null':
                    pass
                elif tvalue[1][(i-number-1)*4+10][hour]>300:
                    self.xft[i].setPixmap(
                        self.xft_zuo_d.scaled(self.xft_zuo.width() * self.ratio, self.xft_zuo.height() * self.ratio))
                    self.xft[i].setObjectName('%d级筒B' % (i % (number + 1)))


            for i in arange(number + 3, 2 * number + 1, 2):  # 偶数旋风筒为右管
                if tvalue[1][(i-number-1)*4+10][hour]=='null':
                    pass
                elif tvalue[1][(i-number-1)*4+10][hour]>300:
                    self.xft[i].setPixmap(
                    self.xft_you_d.scaled(self.xft_you.width() * self.ratio, self.xft_you.height() * self.ratio))
                    self.xft[i].setObjectName('%d级筒B' % (i % (number + 1)))

        if tvalue[1][29][hour]=='null':
            pass
        elif tvalue[1][29][hour]>300:
            if number % 2 == 0:
                self.lab_fjl.setPixmap(
                    self.fjl_d.scaled(self.xft_dl.width() * 5 * self.ratio, self.xft_dl.height() * 3 * self.ratio))
            else:
                self.lab_fjl.setPixmap(
                    self.fjl_d.scaled(self.xft_dl.width() * 7 * self.ratio, self.xft_dl.height() * 3 * self.ratio))
            self.lab_fjl.setObjectName('分解炉')

        if tvalue[1][28][hour]=='null':
            pass
        elif tvalue[1][28][hour]>300:
            self.lab_yao.setPixmap(
                self.yao_d.scaled(self.xft_dl.width() * 9 * self.ratio, self.yao.height() * self.ratio))
            self.lab_yao.setObjectName('窑')


        if tvalue[1][33][hour]=='null':
            pass
        elif tvalue[1][33][hour]>0:
            self.lab_blj.setPixmap(self.blj_d.scaled(self.blj.width() * self.ratio, self.blj.height() * self.ratio))
            self.lab_blj.setObjectName('篦冷机')
        self.initPic()

    def initBtn(self):
        con.setValue_flag_Time(0)  # 初始化选择时间标志
        self.click_flag = 0  # 初始化选择图片标志
        self.flag_timeBtn = 0  # 初始化点击时间选择按钮标志，避免重复单击按钮出现的bug
        self.timeBtn = QPushButton('双击确定', self.widget)
        self.hourBo = QComboBox(self.widget)  # 声明一个组合框hourBo

        for i in range(24):  # 循环添加组合框的元素0-23
            self.hourBo.addItem(str(i))

        self.timeBtn.move(self.width * 0.5, self.height * 0.05)
        self.hourBo.move(self.width * 0.5 + 100, self.height * 0.05)  # 组合框位置
        self.timeBtn.clicked.connect(self.on_click)
        self.hourBo.activated[str].connect(self.getHour)  # 点击时间响应

        self.timeBtn.show()
        self.hourBo.show()

        self.timeLabel = QLabel(self.widget)
        self.timeLabel.move(self.width * 0.5 - 30, self.height * 0.05 + 5)
        self.timeLabel.resize(30, 20)
        self.timeLabel.setText('日期')

        self.timeLabel.show()

    def getHour(self):
        hour = con.getValue_hour()
        flag_Time = con.getValue_flagTime()
        if flag_Time == 0:  # 判断在选择小时前选择日期没，若没显示先选日期
            QMessageBox.information(self, '提示', '请先选择日期', QMessageBox.Yes | QMessageBox.No)
            self.hourBo.setCurrentText('0')
        else:
            hour = int(self.hourBo.currentText())  # 获得用户在组合框选择的数据
            print('组合框的数据%i' % hour)
            self.judgePic()
            self.updateInfor()

    def setTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.operate)  # 触发事件
        self.timer.start(1000)  # 触发间隔

    def operate(self):  # 刷新一天的部件信息
        '''global hour
        print(hour)
        hour = (hour + 1) % 24
        if hour == 0:
            self.timer.stop()'''
        pass

    # 菜单项的实现
    # 数据可视化
    def dataVisual(self):
        print("窑系统数据可视化")

    # 窑系统设备配置
    def deviceSet(self):
        self.set_window.show()

    # 窑系统热耗可视化
    def heatVisual(self):
        con.setValue_flag_Visual(1)

        self.updateInfor()

    # 窑系统设备热耗可视化
    def deviceVisual(self):
        con.setValue_flag_Visual(0)

        self.updateInfor()

    # 文件导入
    def leadIn(self):
        filepath = con.getValue_filepath()
        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取文件", filepath,
                                                          "Excel Files (*.xlsx);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔
        filedir = os.path.split(fileName1)  # 获取文件所在的文件夹
        filepath = filedir[0]  # 文件路径信息
        filename = filedir[1]  # 文件名
        con.setValue_filepath(filepath)

        # print(filepath + '/' + filename)
        if filename and filepath:
            reshape_data(filepath + '/' + filename)  # 后台处理传入文件格式

    # 菜单栏
    def initMenu(self):

        # 数据模块
        dataInputAct = QAction('数据输入', self)

        openFileAct = QAction('打开数据文件', self)

        saveFileAct = QAction('数据保存', self)

        saveasFileAct = QAction('数据另存为', self)

        changeDataAct = QAction('数据修改', self)

        simulateDataAct = QAction('数据模拟', self)

        leadInAct = QAction('数据导入', self)
        leadInAct.setStatusTip('将用户选择的文件变为符合本系统格式的文件')
        leadInAct.triggered.connect(self.leadIn)

        leadOutAct = QAction('数据导出', self)

        # 可视化模块
        dataVisualAct = QAction('窑系统数据可视化', self)
        dataVisualAct.setStatusTip('数据可视化')
        dataVisualAct.triggered.connect(self.dataVisual)

        singleVisualAct = QAction('独立因素热耗分析可视化', self)

        mulVisualAct = QAction('联合因素热耗分析可视化', self)

        heatVisualAct = QAction('窑系统热耗可视化', self)
        heatVisualAct.setStatusTip('窑系统10小时热耗可视化')
        heatVisualAct.triggered.connect(self.heatVisual)

        deviceVisualAct = QAction('窑系统设备热耗可视化', self)
        deviceVisualAct.setStatusTip('窑系统整日热耗可视化')
        deviceVisualAct.triggered.connect(self.deviceVisual)

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

    def change_table(self, index1, index2):  # 单击部件时刷新表格数据
        day = con.getValue_day()
        col1, col2 = get_by_day(day)  # 返回值为[[],[[],[],[],[]]],col1为名称，col2为参数
        if con.getValue_flag_Visual() == 0:
            self.table.setRowCount(len(col2[index1]))
            self.table.setHorizontalHeaderLabels([col1[index1], col1[index2]])
            for i in range(len(col2[index1])):
                newItem = QTableWidgetItem(str(col2[index1][i]))
                self.table.setItem(i, 0, newItem)
                newItem = QTableWidgetItem(str(col2[index2][i]))
                self.table.setItem(i, 1, newItem)
        else:
            self.table.setRowCount(len(col1))
            self.table.setHorizontalHeaderLabels(['名称', '数值'])

            hour = 10
            # 以后会改

            for i in range(len(col1)):
                newItem = QTableWidgetItem(col1[i])
                self.table.setItem(i, 0, newItem)
                newItem = QTableWidgetItem(str(col2[i][hour]))
                self.table.setItem(i, 1, newItem)

    def change_pic(self, index1, index2):  # 接收从标签传过来的温度和压强的下标

        if self.click_flag == 0:
            self.fp1 = MyTempMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.fp2 = MyPressMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.pic1.addWidget(self.fp1)
            self.pic2.addWidget(self.fp2)
            self.change_table(index1, index2)
            self.click_flag = 1
            self.updateInfor()
        elif self.click_flag == 1:
            self.sp1 = MyTempMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.sp2 = MyPressMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.pic1.replaceWidget(self.fp1, self.sp1)
            self.pic2.replaceWidget(self.fp2, self.sp2)
            self.change_table(index1, index2)
            self.click_flag = 2
            self.updateInfor()
        elif self.click_flag == 2:
            self.fp1 = MyTempMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.fp2 = MyPressMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.pic1.replaceWidget(self.sp1, self.fp1)
            self.pic2.replaceWidget(self.sp2, self.fp2)
            self.change_table(index1, index2)
            self.click_flag = 1
            self.updateInfor()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            '''settings = QSettings()
            settings.setValue("MainWindow/Size", QVariant(self.size()))
            settings.setValue("MainWindow/Position", QVariant(self.pos()))
            settings.setValue("mainSplitter", QVariant(self.mainSplitter.saveState()))
            settings.setValue("messageSplitter", QVariant(self.messageSplitter.saveState()))'''
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
        self.num = ['2', '3', '4', '5', '6', '7', '8', '9']
        for i in self.num:
            self.xft_num.addItem(i)

        self.buttonBox.accepted.connect(self.Accept)
        self.buttonBox.rejected.connect(self.Reject)

    def Accept(self):
        if self.serial_sin.isChecked():
            flag = 1
            # con.setValue_flag_Ser(1)
        else:
            flag = 2
            # con.setValue_flag_Ser(2)
        # con.setValue_number(int(self.xft_num.currentText()))
        self.yao_par_signal.emit(flag, self.xft_num.currentText())
        self.close()

    def Reject(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWindow()
    form.show()
    app.exec_()
