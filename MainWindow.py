import sys
from MyPic import *
import MyDialog as dlg
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from Connect_to_Database import *


class MyWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.loginDlg = dlg.MyLoginDlg()
        self.loginDlg.show()
        self.loginDlg.login_signal.connect(self.login)
        self.Flag_login = 0

    def login(self, user, password):
        if Login_test(user, password):
            self.loginDlg.hide()
            con.setValue_username(user)
            if self.Flag_login == 0:
                self.Flag_login = 1
                self.initWindow()
            else:
                self.setWindowTitle("Cement Kiln--%s" % con.getValue_username())  # 设置主窗口标题
                self.show()
        else:
            QMessageBox.information(self, '提示', '用户名或密码错误', QMessageBox.Yes)

    def initWindow(self):
        metric = QDesktopWidget().screenGeometry()
        self.width = metric.width()  # 图片宽度
        self.height = metric.height()  # 图片高度
        self.setFixedSize(self.width, self.height - 72 * self.height / 768)  # 72为win10任务栏高度
        left = -9
        self.move(left, 0)
        self.show()
        # self.showMaximized()

        self.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(46, 139, 130))  # 更改背景色
        self.setPalette(palette)
        self.setWindowTitle("Cement Kiln--%s" % con.getValue_username())  # 设置主窗口标题
        self.initMenu()  # 初始化菜单栏
        self.updatePic()  # 加载图片资源
        self.setTimer()  # 设定计时器，稍后会摆在正确位置
        self.xft = {}  # 旋风筒初始化

        self.deviceDlg = dlg.MyDeviceDlg()  # 初始化对话框
        self.deviceDlg.show()
        self.deviceDlg.yao_par_signal.connect(self.initDevice)

    def initInfor(self):  # 信息栏
        self.lab_infor = QLabel(self.mainWidget)
        self.lab_infor.setStyleSheet('background-color:white')
        self.lab_infor.resize(self.width * 0.65, self.lab_infor.height())
        if con.getValue_flag_Visual() == 0:
            self.lab_infor.setText('\t窑系统设备数据可视化\t选择时间：未选择\t热耗：无数据')
        else:
            self.lab_infor.setText('\t窑系统数据可视化\t选择时间：未选择\t热耗：无数据')

    def updateInfor(self):

        day = con.getValue_day()
        # print(con.getValue_flag_Visual())
        if con.getValue_number() != 0:  # 判断用户是否完成了窑系统配置信息
            if con.getValue_flag_Visual() == 1:  # 显示小时

                hour = str(con.getValue_hour())
                if self.click_flag == 0:  # 判断是否点击了部件
                    day_str = str(day)
                    self.lab_infor.setText(
                        '\t窑系统数据可视化\t选择时间：%s-%s-%s %s:00\t热耗：无数据' % (day_str[0:4], day_str[4:6], day_str[6:8], hour))
                else:
                    day_str = str(day)
                    value = get_by_day(str(day))
                    self.lab_infor.setText(
                        '\t窑系统数据可视化\t选择时间：%s-%s-%s %s:00\t热耗：' % (
                            day_str[0:4], day_str[4:6], day_str[6:8], hour))
            else:

                if self.click_flag == 0:  # 判断是否点击了部件
                    day_str = str(day)
                    self.lab_infor.setText(
                        '\t窑系统设备数据可视化\t选择时间：%s-%s-%s\t热耗：无数据' % (day_str[0:4], day_str[4:6], day_str[6:8]))
                else:
                    value = get_by_day(str(day))
                    day_str = str(day)
                    self.lab_infor.setText(
                        '\t窑系统设备数据可视化\t选择时间：%s-%s-%s\t热耗：' % (
                            day_str[0:4], day_str[4:6], day_str[6:8]))

    def initDevice(self, flag_Seri, num):
        con.setValue_flag_Visual(0)
        self.hideIndex = 0
        self.lay = QGridLayout()  # 重置布局，否则上次的部件不会消失
        self.click_flag = 0  # 折线图的切换图片标志
        con.setValue_flag_Ser(flag_Seri)
        con.setValue_number(int(num))
        # 设置信息显示区域
        self.widget = QWidget()
        self.table = QTableWidget(0, 2)  # 以表格形式显示数据
        self.table.setMinimumHeight(100)
        self.table.horizontalHeader().setDefaultSectionSize(120)  # 列宽

        self.messageView = QTabWidget()
        self.messageView.setMinimumHeight(100)
        self.messageView.setMinimumWidth(self.width * 0.25)  # 设置右边信息栏的最小宽度

        self.messageLay = QVBoxLayout()
        self.messageLay.addWidget(self.table)
        self.messageLay.addWidget(self.messageView)
        self.messageWidget = QWidget()
        self.messageWidget.setLayout(self.messageLay)
        self.hidewidget = QWidget()
        self.btn = QPushButton(self.hidewidget)
        self.btn.setFlat(True)
        self.btn.setIcon(QIcon('picture\\jiantou_you.png'))
        self.btn.setToolTip('展开或折叠信息窗口')
        self.btn.move(0, self.height * 0.5 - 90)
        self.btn.show()
        self.btn.clicked.connect(self.hideW)

        self.hideLay = QHBoxLayout()

        self.hideLay.addStretch(1)

        self.hideLay.addWidget(self.btn)
        self.cblLay = QHBoxLayout()

        self.cblLay.addWidget(self.hidewidget)
        self.cblLay.addWidget(self.messageWidget)
        self.hidewidget.setLayout(self.hideLay)

        self.main_lay = QHBoxLayout()
        self.main_lay.addWidget(self.widget)
        self.information = QWidget()
        self.infor_lay = QVBoxLayout()
        self.information.setLayout(self.infor_lay)
        self.main_lay.addWidget(self.information)
        self.main_lay.addLayout(self.cblLay)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.main_lay)
        self.setCentralWidget(self.mainWidget)
        self.initInfor()  # 初始化信息栏
        self.update_normal_Pic()  # 重置为正常图片
        self.initPic()  # 初始化窑系统各部件
        # self.initBtn()  # 初始化时间选择控件
        self.refresh()

    def hideW(self):
        if self.hideIndex == 0:
            self.hideIndex = 1
            self.messageWidget.hide()
            self.infor_lab = QLabel('13fasdfaaaaaaaaaaaaaaaaaaaaaaaaaaafasdfasdfasdfasdfasdfads')
            self.infor_lay.addWidget(self.infor_lab)
            self.btn.setIcon(QIcon('picture\\jiantou_zuo.png'))
            self.btn.move(20, self.height * 0.5 - 90)
        else:
            self.hideIndex = 0
            self.messageWidget.show()
            self.btn.setIcon(QIcon('picture\\jiantou_you.png'))

            self.infor_lay.removeWidget(self.infor_lab)
            # self.btn.move(0, self.height * 0.5 - 90)

    '''def initTime(self):
        con.setValue_flag_Time(1)

        self.update_normal_Pic()
        self.initPic()
        date = get_time_now()
        date_input = '12345678'
        date_input = date[:4] + date[5:7] + date[8:10]

        con.setValue_day(int(date_input))

        self.updateInfor()'''

    '''def double_click(self):  # 双击确认时间
        con.setValue_flag_Time(1)
        

        self.update_normal_Pic()
        self.initPic()
        self.calendar.hide()
        date = self.calendar.selectedDate().toString('yyyy-MM-dd')  # 日期显示格式 例:2017-01-02
        date_input = '12345678'
        date_input = date[:4] + date[5:7] + date[8:10]
        self.timeBtn.setText(date)

        con.setValue_day(int(date_input))

        self.updateInfor()'''

    def initPic(self):  # 初始化布局

        # self.widget.autoFillBackground()
        # print(con.getValue_flag_Time())
        '''if con.getValue_flag_Time() == 0:
            self.lay = QGridLayout()  # 初始化布局'''
        xft_row = 1  # 旋风筒所占行数
        xft_col = 2  # 旋风筒所占列数
        fjl_row = 3  # 分解炉所占行数
        fjl_col = 5  # 分解炉所占列数
        number = con.getValue_number()
        flag_Ser = con.getValue_flag_Ser()

        if number % 2 == 0:
            self.lay.addWidget(self.jt[0], number - 1, 1, 2, 3)
            self.lay.addWidget(self.jt[1], number, 2, 2, 2)
            self.lay.addWidget(self.lab_fjl, number - 2, 2, fjl_row, fjl_col)  # 分解炉
            self.lay.addWidget(self.xft[number], number - 1, 2)  # A系列旋风筒最后一级

            self.lay.addWidget(self.fjl_yao, number - 2 + fjl_row, (fjl_col - 1) / 2 + 2)  # 连接件
            if flag_Ser == 1:
                self.lay.addWidget(self.lab_yao_1, number - 2 + fjl_row, (fjl_col - 1) / 2 + 3, 1, 3)
            self.lay.addWidget(self.lab_yao_2, number - 2 + fjl_row, (fjl_col - 1) / 2 + 6, 1, 3)
            self.lay.addWidget(self.lab_yao_3, number - 2 + fjl_row, (fjl_col - 1) / 2 + 9, 1, 3)
            # self.lay.addWidget(self.lab_yao, number - 2 + fjl_row, (fjl_col - 1) / 2 + 3, 2, 9)  # 窑
            self.lay.addWidget(self.lab_blj_1, number - 2 + fjl_row, 16)  # 篦冷机1段
            self.lay.addWidget(self.lab_blj_2, number - 2 + fjl_row, 17)  # 篦冷机2段
            self.lay.addWidget(self.lab_blj_3, number - 2 + fjl_row, 18)  # 篦冷机3段
            # self.lay.addWidget(self.lab_blj, number - 2 + fjl_row, 16, 2, 3)  # 篦冷机
        else:
            self.lay.addWidget(self.jt[0], number, 1, 2, 3)
            self.lay.addWidget(self.jt[1], number - 1, 2, 2, 2)
            self.lay.addWidget(self.lab_fjl, number - 2, 1, fjl_row, fjl_col + 2)  # 分解炉
            self.lay.addWidget(self.xft[number], number - 1, 1)

            self.lay.addWidget(self.fjl_yao, number - 2 + fjl_row, (fjl_col - 1) / 2 + 2)  # 连接件
            if flag_Ser == 1:
                self.lay.addWidget(self.lab_yao_1, number - 2 + fjl_row, (fjl_col - 1) / 2 + 3, 1, 3)
            self.lay.addWidget(self.lab_yao_2, number - 2 + fjl_row, (fjl_col - 1) / 2 + 6, 1, 3)
            self.lay.addWidget(self.lab_yao_3, number - 2 + fjl_row, (fjl_col - 1) / 2 + 9, 1, 3)
            # self.lay.addWidget(self.lab_yao, number - 2 + fjl_row, (fjl_col - 1) / 2 + 3, 2, 9)  # 窑
            self.lay.addWidget(self.lab_blj_1, number - 2 + fjl_row, 16)  # 篦冷机1段
            self.lay.addWidget(self.lab_blj_2, number - 2 + fjl_row, 17)  # 篦冷机2段
            self.lay.addWidget(self.lab_blj_3, number - 2 + fjl_row, 18)  # 篦冷机3段
            # self.lay.addWidget(self.lab_blj, number - 2 + fjl_row, 16, 2, 3)  # 篦冷机

        self.lay.addWidget(self.xft[0], 0, 0)
        for i in arange(1, number):
            self.lay.addWidget(self.xft[i], i - 1, 1, xft_row, xft_col)
            if i % 2 == 0:
                self.lay.addWidget(self.jt[i + 5], i - 1, 1)
            else:
                self.lay.addWidget(self.jt[i + 5], i - 1, 2)

        if flag_Ser == 2:
            self.lay.addWidget(self.xft[number + 1], 0, 10 - flag_Ser)
            for i in arange(number + 2, 2 * number + 1):
                self.lay.addWidget(self.xft[i], (i - 2) % number, 8 - flag_Ser, xft_row, xft_col)
                if number % 2 == 0:
                    if i % 2 == 0:
                        self.lay.addWidget(self.jt[i + 3], (i - 2) % number, 8 - flag_Ser)
                    else:
                        self.lay.addWidget(self.jt[i + 3], (i - 2) % number, 9 - flag_Ser)
                else:
                    if i % 2 == 0:
                        self.lay.addWidget(self.jt[i + 3], (i - 2) % number, 9 - flag_Ser)
                    else:
                        self.lay.addWidget(self.jt[i + 3], (i - 2) % number, 8 - flag_Ser)
            if number % 2 == 0:
                self.lay.addWidget(self.jt[4], number - 1, 7 - flag_Ser, 2, 3)
                self.lay.addWidget(self.jt[5], number, 7 - flag_Ser, 2, 2)
                self.lay.addWidget(self.xft[number * 2 + 1], number - 1, 8 - flag_Ser)
            else:
                self.lay.addWidget(self.jt[2], number - 1, 7 - flag_Ser, 2, 2)
                self.lay.addWidget(self.jt[3], number, 7 - flag_Ser, 2, 3)
                self.lay.addWidget(self.xft[number * 2 + 1], number - 1, 9 - flag_Ser)
            self.lay.addWidget(self.lab_yao_1, number - 2 + fjl_row, (fjl_col - 1) / 2 + 3, 1, 3)  # 放到此处避免窑尾被覆盖
        self.lay.setSpacing(0)
        self.lay.setAlignment(Qt.AlignLeft | Qt.AlignBottom)

        self.widget.setLayout(self.lay)

    def updatePic(self):
        # 加载正常状态下的图片
        self.xft_dl = QPixmap('picture\\xft_dl.png')  # 旋风筒
        self.xft_zuo = QPixmap('picture\\xft_zuo.png')  # 旋风筒左管
        self.xft_you = QPixmap('picture\\xft_you.png')  # 旋风筒右管
        self.fjl = QPixmap('picture\\fjl.png')  # 分解炉
        self.jt_you1 = QPixmap('picture\\jt_you1.png')
        self.jt_you2 = QPixmap('picture\\jt_you2.png')
        self.jt_zuo1 = QPixmap('picture\\jt_zuo1.png')
        self.jt_zuo2 = QPixmap('picture\\jt_zuo2.png')
        self.jt_zuo3 = QPixmap('picture\\jt_zuo3.png')
        self.jt_zuo4 = QPixmap('picture\\jt_zuo4.png')
        self.jt_xia = QPixmap('picture\\jt_xia.png')
        self.mfc = QPixmap('picture\\mfc.png')  # 煤粉仓
        self.fjl_yao1 = QPixmap('picture\\fjl_yao.png')
        self.gwfj = QPixmap('picture\\gwfj.png')  # 高温风机
        # self.blj = QPixmap('picture\\blj.png')
        self.blj_1 = QPixmap('picture\\blj_1.png')  # 篦冷机
        self.blj_2 = QPixmap('picture\\blj_2.png')
        self.blj_3 = QPixmap('picture\\blj_3.png')
        # self.yao = QPixmap('picture\\yao.png')
        self.yao_1 = QPixmap('picture\\yao_1.png')
        self.yao_2 = QPixmap('picture\\yao_2.png')
        self.yao_3 = QPixmap('picture\\yao_3.png')

        # 加载警告状态下的图片
        self.xft_dl_d = QPixmap('picture\\xft_dl_d.png')
        self.xft_zuo_d = QPixmap('picture\\xft_zuo_d.png')  # 旋风筒左管
        self.xft_you_d = QPixmap('picture\\xft_you_d.png')  # 旋风筒右管
        self.fjl_d = QPixmap('picture\\fjl_d.png')  # 分解炉
        self.mfc_d = QPixmap('picture\\mfc_d.png')  # 煤粉仓
        self.gwfj_d = QPixmap('picture\\gwfj_d.png')  # 高温风机
        # self.blj_d = QPixmap('picture\\blj_d.png')  # 篦冷机
        self.blj_1_d = QPixmap('picture\\blj_1_d.png')  # 篦冷机
        self.blj_2_d = QPixmap('picture\\blj_2_d.png')
        self.blj_3_d = QPixmap('picture\\blj_3_d.png')
        # self.yao_d = QPixmap('picture\\yao_d.png')
        self.yao_1_d = QPixmap('picture\\yao_1_d.png')
        self.yao_2_d = QPixmap('picture\\yao_2_d.png')
        self.yao_3_d = QPixmap('picture\\yao_3_d.png')

        # 加载危险状态下的图片
        self.xft_dl_r = QPixmap('picture\\xft_dl_r.png')
        self.xft_zuo_r = QPixmap('picture\\xft_zuo_r.png')  # 旋风筒左管
        self.xft_you_r = QPixmap('picture\\xft_you_r.png')  # 旋风筒右管
        self.fjl_r = QPixmap('picture\\fjl_r.png')  # 分解炉
        self.mfc_r = QPixmap('picture\\mfc_r.png')  # 煤粉仓
        self.gwfj_r = QPixmap('picture\\gwfj_r.png')  # 高温风机
        self.blj_1_r = QPixmap('picture\\blj_1_r.png')  # 篦冷机
        self.blj_2_r = QPixmap('picture\\blj_2_r.png')
        self.blj_3_r = QPixmap('picture\\blj_3_r.png')
        self.yao_1_r = QPixmap('picture\\yao_1_r.png')
        self.yao_2_r = QPixmap('picture\\yao_2_r.png')
        self.yao_3_r = QPixmap('picture\\yao_3_r.png')

    def update_normal_Pic(self):

        QToolTip.setFont(QFont('SansSerif', 10))  # 设置tooltip的字体类型和字体的大小

        number = con.getValue_number()
        flag_Ser = con.getValue_flag_Ser()

        self.ratio = 0.27 * self.width / 1366  # 图片放大倍数
        self.jt = {}
        self.jt[0] = QLabel()
        self.jt[0].setPixmap(
            self.jt_you1.scaled(self.xft_dl.width() * self.ratio * 3, self.xft_dl.height() * self.ratio * 2))

        self.jt[1] = QLabel()
        self.jt[1].setPixmap(
            self.jt_you2.scaled(self.xft_dl.width() * self.ratio * 2, self.xft_dl.height() * self.ratio * 2))

        self.jt[2] = QLabel()
        self.jt[2].setPixmap(
            self.jt_zuo2.scaled(self.xft_dl.width() * self.ratio * 2, self.xft_dl.height() * self.ratio * 2))
        self.jt[3] = QLabel()
        self.jt[3].setPixmap(
            self.jt_zuo1.scaled(self.xft_dl.width() * self.ratio * 3, self.xft_dl.height() * self.ratio * 2))
        self.jt[4] = QLabel()
        self.jt[4].setPixmap(
            self.jt_zuo3.scaled(self.xft_dl.width() * self.ratio * 3, self.xft_dl.height() * self.ratio * 2))
        self.jt[5] = QLabel()
        self.jt[5].setPixmap(
            self.jt_zuo4.scaled(self.xft_dl.width() * self.ratio * 2, self.xft_dl.height() * self.ratio * 2))
        for i in range((number - 1) * 2):
            self.jt[6 + i] = QLabel()
            self.jt[6 + i].setPixmap(
                self.jt_xia.scaled(self.xft_dl.width() * self.ratio, self.xft_dl.height() * self.ratio))
        self.xft[0] = MyLabel()
        self.xft[0].setPixmap(self.xft_dl.scaled(self.xft_dl.width() * self.ratio, self.xft_dl.height() * self.ratio))
        self.xft[0].setToolTip('%d级筒A0' % 1)
        self.xft[0].setObjectName('%d级筒A0' % 1)
        self.xft[0].changeindex.connect(self.change_pic)
        # print(self.xft[0].objectName())
        self.xft[number] = MyLabel()
        self.xft[number].setPixmap(
            self.xft_dl.scaled(self.xft_dl.width() * self.ratio, self.xft_dl.height() * self.ratio))
        self.xft[number].setToolTip('%d级筒A' % number)
        self.xft[number].setObjectName('%d级筒A' % number)
        self.xft[number].changeindex.connect(self.change_pic)

        for i in arange(1, number, 2):  # 不会取到number,奇数旋风筒为右管
            self.xft[i] = MyLabel()
            self.xft[i].setPixmap(
                self.xft_you.scaled(self.xft_you.width() * self.ratio, self.xft_you.height() * self.ratio))
            self.xft[i].setToolTip('%d级筒A' % i)
            self.xft[i].setObjectName('%d级筒A' % i)
            self.xft[i].changeindex.connect(self.change_pic)
        for i in arange(2, number, 2):  # 偶数旋风筒为左管
            self.xft[i] = MyLabel()
            self.xft[i].setPixmap(
                self.xft_zuo.scaled(self.xft_zuo.width() * self.ratio, self.xft_zuo.height() * self.ratio))
            self.xft[i].setToolTip('%d级筒A' % i)
            self.xft[i].setObjectName('%d级筒A' % i)
            self.xft[i].changeindex.connect(self.change_pic)

        if flag_Ser == 2:  # 双系列
            self.xft[number + 1] = MyLabel()
            self.xft[number + 1].setPixmap(
                self.xft_dl.scaled(self.xft_dl.width() * self.ratio, self.xft_dl.height() * self.ratio))
            self.xft[number + 1].setToolTip('%d级筒B0' % 1)
            self.xft[number + 1].setObjectName('%d级筒B0' % 1)
            self.xft[number + 1].changeindex.connect(self.change_pic)
            # print(self.xft[0].objectName())
            self.xft[2 * number + 1] = MyLabel()
            self.xft[2 * number + 1].setPixmap(
                self.xft_dl.scaled(self.xft_dl.width() * self.ratio, self.xft_dl.height() * self.ratio))
            self.xft[2 * number + 1].setToolTip('%d级筒B' % number)
            self.xft[2 * number + 1].setObjectName('%d级筒B' % number)
            self.xft[2 * number + 1].changeindex.connect(self.change_pic)

            for i in arange(number + 2, 2 * number + 1, 2):  # 不会取到2*number,奇数旋风筒为左管
                # print(i)
                self.xft[i] = MyLabel()
                self.xft[i].setPixmap(
                    self.xft_zuo.scaled(self.xft_zuo.width() * self.ratio, self.xft_zuo.height() * self.ratio))
                self.xft[i].setToolTip('%d级筒B' % (i % (number + 1)))
                self.xft[i].setObjectName('%d级筒B' % (i % (number + 1)))
                self.xft[i].changeindex.connect(self.change_pic)

            for i in arange(number + 3, 2 * number + 1, 2):  # 偶数旋风筒为右管
                # print(i)
                self.xft[i] = MyLabel()
                self.xft[i].setPixmap(
                    self.xft_you.scaled(self.xft_you.width() * self.ratio, self.xft_you.height() * self.ratio))
                self.xft[i].setToolTip('%d级筒B' % (i % (number + 1)))
                self.xft[i].setObjectName('%d级筒B' % (i % (number + 1)))
                self.xft[i].changeindex.connect(self.change_pic)

        self.lab_fjl = MyLabel()
        if number % 2 == 0:
            self.lab_fjl.setPixmap(
                self.fjl.scaled(self.xft_dl.width() * 5 * self.ratio, self.xft_dl.height() * 3 * self.ratio))
        else:
            self.lab_fjl.setPixmap(
                self.fjl.scaled(self.xft_dl.width() * 7 * self.ratio, self.xft_dl.height() * 3 * self.ratio))
        self.lab_fjl.setToolTip('分解炉')
        self.lab_fjl.setObjectName('分解炉')
        self.lab_fjl.changeindex.connect(self.change_pic)

        self.lab_yao_1 = MyLabel()
        self.lab_yao_1.setPixmap(
            self.yao_1.scaled(self.xft_dl.width() * 3 * self.ratio, self.yao_1.height() * self.ratio))
        self.lab_yao_1.setToolTip('窑')
        self.lab_yao_1.setObjectName('窑1')
        self.lab_yao_1.changeindex.connect(self.change_pic)
        self.lab_yao_2 = MyLabel()
        self.lab_yao_2.setPixmap(
            self.yao_2.scaled(self.xft_dl.width() * 3 * self.ratio, self.yao_2.height() * self.ratio))
        self.lab_yao_2.setToolTip('窑')
        self.lab_yao_2.setObjectName('窑2')
        self.lab_yao_2.changeindex.connect(self.change_pic)
        self.lab_yao_3 = MyLabel()
        self.lab_yao_3.setPixmap(
            self.yao_3.scaled(self.xft_dl.width() * 3 * self.ratio, self.yao_3.height() * self.ratio))
        self.lab_yao_3.setToolTip('窑')
        self.lab_yao_3.setObjectName('窑3')
        self.lab_yao_3.changeindex.connect(self.change_pic)

        self.lab_blj_1 = MyLabel()
        self.lab_blj_1.setPixmap(self.blj_1.scaled(self.blj_1.width() * self.ratio, self.blj_1.height() * self.ratio))
        self.lab_blj_1.setToolTip('篦冷机1段')
        self.lab_blj_1.setObjectName('篦冷机1段')
        self.lab_blj_1.changeindex.connect(self.change_pic)
        self.lab_blj_2 = MyLabel()
        self.lab_blj_2.setPixmap(self.blj_2.scaled(self.blj_2.width() * self.ratio, self.blj_2.height() * self.ratio))
        self.lab_blj_2.setToolTip('篦冷机2段')
        self.lab_blj_2.setObjectName('篦冷机2段')
        self.lab_blj_2.changeindex.connect(self.change_pic)
        self.lab_blj_3 = MyLabel()
        self.lab_blj_3.setPixmap(self.blj_3.scaled(self.blj_3.width() * self.ratio, self.blj_3.height() * self.ratio))
        self.lab_blj_3.setToolTip('篦冷机3段')
        self.lab_blj_3.setObjectName('篦冷机3段')
        self.lab_blj_3.changeindex.connect(self.change_pic)

        self.fjl_yao = MyLabel()
        self.fjl_yao.setPixmap(
            self.fjl_yao1.scaled(self.xft_dl.width() * self.ratio, self.fjl_yao1.height() * self.ratio))
        self.fjl_yao.setToolTip('分解炉--窑连接部分')
        self.fjl_yao.setObjectName('分解炉--窑')
        self.fjl_yao.changeindex.connect(self.change_pic)

    def judgePic(self):
        day = str(con.getValue_day())
        tvalue = get_by_day(day)
        hour = con.getValue_hour()
        number = con.getValue_number()
        flag_Ser = con.getValue_flag_Ser()
        if tvalue[1][8][hour] == None:
            pass
        elif tvalue[1][8][hour] > 300:
            self.xft[0].setPixmap(
                self.xft_dl_d.scaled(self.xft_dl_d.width() * self.ratio, self.xft_dl_d.height() * self.ratio))
            # self.xft[0].setObjectName('%d级筒A' % 1)

        if tvalue[1][(number - 1) * 4 + 8][hour] == None:
            pass
        elif tvalue[1][(number - 1) * 4 + 8][hour] > 300:
            self.xft[number].setPixmap(
                self.xft_dl_d.scaled(self.xft_dl_d.width() * self.ratio, self.xft_dl_d.height() * self.ratio))
            # self.xft[number].setObjectName('%d级筒A' % number)

        for i in arange(1, number, 2):  # 不会取到number,奇数旋风筒为右管
            if tvalue[1][(i - 1) * 4 + 8][hour] == None:
                pass
            elif tvalue[1][(i - 1) * 4 + 8][hour] > 300:
                self.xft[i].setPixmap(
                    self.xft_you_d.scaled(self.xft_you.width() * self.ratio, self.xft_you.height() * self.ratio))
                # self.xft[i].setObjectName('%d级筒A' % i)
        for i in arange(2, number, 2):  # 偶数旋风筒为左管
            if tvalue[1][(i - 1) * 4 + 8][hour] == None:
                pass
            elif tvalue[1][(i - 1) * 4 + 8][hour] > 300:
                self.xft[i].setPixmap(
                    self.xft_zuo_d.scaled(self.xft_zuo.width() * self.ratio, self.xft_zuo.height() * self.ratio))
                # self.xft[i].setObjectName('%d级筒A' % i)
        if flag_Ser == 2:
            if tvalue[1][10][hour] == None:
                pass
            elif tvalue[1][10][hour] > 300:
                self.xft[number + 1].setPixmap(
                    self.xft_dl_d.scaled(self.xft_dl.width() * self.ratio, self.xft_dl.height() * self.ratio))
                # self.xft[number + 1].setObjectName('%d级筒B' % 1)
            if tvalue[1][(number - 1) * 4 + 10][hour] == None:
                pass
            elif tvalue[1][(number - 1) * 4 + 10][hour] > 300:
                self.xft[2 * number + 1].setPixmap(
                    self.xft_dl_d.scaled(self.xft_dl.width() * self.ratio, self.xft_dl.height() * self.ratio))
                # self.xft[2 * number + 1].setObjectName('%d级筒B' % number)
            for i in arange(number + 2, 2 * number + 1, 2):  # 不会取到2*number,奇数旋风筒为左管
                if tvalue[1][(i - number - 1) * 4 + 10][hour] == None:
                    pass
                elif tvalue[1][(i - number - 1) * 4 + 10][hour] > 300:
                    self.xft[i].setPixmap(
                        self.xft_zuo_d.scaled(self.xft_zuo.width() * self.ratio, self.xft_zuo.height() * self.ratio))
                    # self.xft[i].setObjectName('%d级筒B' % (i % (number + 1)))

            for i in arange(number + 3, 2 * number + 1, 2):  # 偶数旋风筒为右管
                if tvalue[1][(i - number - 1) * 4 + 10][hour] == None:
                    pass
                elif tvalue[1][(i - number - 1) * 4 + 10][hour] > 300:
                    self.xft[i].setPixmap(
                        self.xft_you_d.scaled(self.xft_you.width() * self.ratio, self.xft_you.height() * self.ratio))
                    # self.xft[i].setObjectName('%d级筒B' % (i % (number + 1)))

        if tvalue[1][29][hour] == None:
            pass
        elif tvalue[1][29][hour] > 300:
            if number % 2 == 0:
                self.lab_fjl.setPixmap(
                    self.fjl_d.scaled(self.xft_dl.width() * 5 * self.ratio, self.xft_dl.height() * 3 * self.ratio))
            else:
                self.lab_fjl.setPixmap(
                    self.fjl_d.scaled(self.xft_dl.width() * 7 * self.ratio, self.xft_dl.height() * 3 * self.ratio))
            # self.lab_fjl.setObjectName('分解炉')

        if tvalue[1][28][hour] == None:
            pass
        elif tvalue[1][28][hour] > 300:
            self.lab_yao_1.setPixmap(
                self.yao_1_d.scaled(self.xft_dl.width() * 3 * self.ratio, self.yao_1.height() * self.ratio))
            self.lab_yao_2.setPixmap(
                self.yao_2_d.scaled(self.xft_dl.width() * 3 * self.ratio, self.yao_2.height() * self.ratio))
            self.lab_yao_3.setPixmap(
                self.yao_3_d.scaled(self.xft_dl.width() * 3 * self.ratio, self.yao_3.height() * self.ratio))

            '''self.lab_yao.setPixmap(
                self.yao_d.scaled(self.xft_dl.width() * 9 * self.ratio, self.yao.height() * self.ratio))
            self.lab_yao.setObjectName('窑')'''

        if tvalue[1][33][hour] == None:
            pass
        elif tvalue[1][33][hour] > 0:
            self.lab_blj_1.setPixmap(
                self.blj_1_d.scaled(self.blj_1.width() * self.ratio, self.blj_1.height() * self.ratio))
            self.lab_blj_2.setPixmap(
                self.blj_2_d.scaled(self.blj_2.width() * self.ratio, self.blj_2.height() * self.ratio))
            self.lab_blj_3.setPixmap(
                self.blj_3_d.scaled(self.blj_3.width() * self.ratio, self.blj_3.height() * self.ratio))
            '''self.lab_blj.setPixmap(self.blj_d.scaled(self.blj.width() * self.ratio, self.blj.height() * self.ratio))
            self.lab_blj.setObjectName('篦冷机')'''
        # self.initPic()

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

    def keyPressEvent(self, event):
        # 这里event.key（）显示的是按键的编码
        # print("按下：" + str(event.key()))
        # 举例，这里Qt.Key_A注意虽然字母大写，但按键事件对大小写不敏感
        if (event.key() == Qt.Key_Control):
            con.setValue_flag_Ctrl(1)

    def keyReleaseEvent(self, event):
        # 这里event.key（）显示的是按键的编码
        # 举例，这里Qt.Key_A注意虽然字母大写，但按键事件对大小写不敏感
        if (event.key() == Qt.Key_Control):
            con.setValue_flag_Ctrl(0)

    # 菜单项的实现
    def warning(self):
        self.timeDlg_war = dlg.MyTimeDlg()
        self.timeDlg_war.time_signal.connect(self.time_war)

    def time_war(self, time):
        self.warningWnd = dlg.MyProduceWarWnd(int(time[:8]), int(time[8:]), 1)

    # 数据可视化
    def dataVisual(self):
        con.setValue_flag_Visual(1)
        self.timeDlg_data = dlg.MyTimeDlg()
        self.timeDlg_data.time_signal.connect(self.time_data)

    def time_data(self, time):
        con.setValue_day(int(time[:8]))
        con.setValue_hour(int(time[8:]))
        self.judgePic()  # 更换图片资源
        self.initPic()  # 显示图片
        self.updateInfor()

    def dataDeviceVisual(self):
        con.setValue_flag_Visual(0)
        self.timeDlg_dataDevice = dlg.MyDayDlg()
        self.timeDlg_dataDevice.time_signal.connect(self.time_dataDevice)

    def time_dataDevice(self, time):
        con.setValue_day(int(time))
        self.judgePic()  # 更换图片资源
        self.initPic()  # 显示图片
        self.updateInfor()

    def singleVisual(self):
        self.singleWnd = dlg.MyRadioWnd()

    def mulVisual(self):

        self.mulWnd = dlg.MyCheckWnd()

    # 窑系统设备配置
    def deviceSet(self):
        self.deviceDlg.show()

    # 窑系统热耗可视化
    def heatVisual(self):
        pass

    # 窑系统设备热耗可视化
    def deviceVisual(self):
        pass

    # 数据导入
    def leadIn(self):
        self.dataLeadInDlg = dlg.MyDataLeadInDlg()

    def dataInput(self):

        self.datainputWnd = dlg.MyDataInputWnd()
        '''if con.getValue_flag_Hour() == 1:
            self.datainputDlg = dlg.MyDataInputWnd()
        else:
            QMessageBox.information(self, '提示', '请先选择日期和小时!', QMessageBox.Yes | QMessageBox.No)'''

    def openFile(self):
        self.openFileWnd = dlg.MyOpenFileWnd()

    def changeData(self):
        self.changeDataWnd = dlg.MyDataReviseWnd()

    def simulateData(self):
        self.timeDlg_sim = dlg.MyTimeDlg()
        self.timeDlg_sim.time_signal.connect(self.time_sim)

    def time_sim(self, time):
        # print(time)
        self.dataSimDlg = dlg.MyDataSimDlg(time)

    def userManage(self):
        self.userManageDlg = dlg.MyUserManageDlg()

    def sysLog(self):
        self.sysLogDlg = dlg.MySysLogDlg()

    def userChange(self):
        self.hide()
        self.loginDlg.show()

    def dataSet(self):
        self.YaoDlg = dlg.MyYaoDlg()

    def userSet(self):
        self.userSetDlg = dlg.MyUserSettingDlg()

    def standardSet(self):
        self.standardValueDlg = dlg.MyStandardValueDlg()

    def refresh(self):
        data = get_all_date()
        index = len(data)
        date = data[index - 1][0]
        hour = data[index - 1][1]
        con.setValue_day(int(date))
        con.setValue_hour(int(hour))
        con.setValue_flag_Hour(1)
        self.judgePic()  # 更换图片资源
        self.initPic()  # 显示图片
        self.updateInfor()

    # 菜单栏
    def initMenu(self):

        # 数据模块
        dataInputAct = QAction('数据输入', self)
        dataInputAct.setStatusTip('用户手动输入数据')
        dataInputAct.triggered.connect(self.dataInput)

        openFileAct = QAction('打开数据文件', self)
        openFileAct.setStatusTip('用户手动输入数据')
        openFileAct.triggered.connect(self.openFile)

        changeDataAct = QAction('数据修改', self)
        changeDataAct.setStatusTip('用户手动输入数据')
        changeDataAct.triggered.connect(self.changeData)

        simulateDataAct = QAction('数据模拟', self)
        simulateDataAct.setStatusTip('用户修改某些数据以模拟窑系统状况')
        simulateDataAct.triggered.connect(self.simulateData)

        leadInAct = QAction('数据导入', self)
        leadInAct.setStatusTip('将用户选择的文件变为符合本系统格式的文件')
        leadInAct.triggered.connect(self.leadIn)

        leadOutAct = QAction('数据导出', self)

        # 可视化模块
        dataVisualAct = QAction('窑系统数据可视化', self)
        dataVisualAct.setStatusTip('实时数据可视化')
        dataVisualAct.triggered.connect(self.dataVisual)

        dataDeviceVisualAct = QAction('窑系统设备数据可视化', self)
        dataDeviceVisualAct.setStatusTip('单日数据可视化')
        dataDeviceVisualAct.triggered.connect(self.dataDeviceVisual)

        singleVisualAct = QAction('独立因素热耗分析可视化', self)
        singleVisualAct.setStatusTip('单因素分析')
        singleVisualAct.triggered.connect(self.singleVisual)

        mulVisualAct = QAction('联合因素热耗分析可视化', self)
        mulVisualAct.setStatusTip('多因素分析')
        mulVisualAct.triggered.connect(self.mulVisual)

        heatVisualAct = QAction('窑系统热耗可视化', self)
        heatVisualAct.setStatusTip('窑系统10小时热耗可视化')
        heatVisualAct.triggered.connect(self.heatVisual)

        deviceVisualAct = QAction('窑系统设备热耗可视化', self)
        deviceVisualAct.setStatusTip('窑系统整日热耗可视化')
        deviceVisualAct.triggered.connect(self.deviceVisual)

        # 生产指导模块
        warningAct = QAction('生产预警', self)
        warningAct.setStatusTip('窑系统单日数据分析结果')
        warningAct.triggered.connect(self.warning)

        warningGuideAct = QAction('生产预警指导', self)

        errorAct = QAction('生产异常报警', self)

        errorGuideAct = QAction('生产异常指导', self)

        # 设置模块
        deviceSetAct = QAction('窑系统设备', self)
        deviceSetAct.setStatusTip('窑系统设备设置')
        deviceSetAct.triggered.connect(self.deviceSet)

        dataSetAct = QAction('窑系统数据', self)
        dataSetAct.setStatusTip('窑系统数据展示')
        dataSetAct.triggered.connect(self.dataSet)

        userSetAct = QAction('用户设置', self)
        userSetAct.setStatusTip('修改密码')
        userSetAct.triggered.connect(self.userSet)

        standardSetAct = QAction('生产数据标准设置', self)
        standardSetAct.setStatusTip('窑系统数据展示')
        standardSetAct.triggered.connect(self.standardSet)

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
        userManageAct.setStatusTip('系统操作日志')
        userManageAct.triggered.connect(self.userManage)

        dataBackupAct = QAction('数据备份', self)

        dataRecAct = QAction('数据恢复', self)

        knowBackupAct = QAction('知识库备份', self)

        sysLogAct = QAction('系统日志', self)
        sysLogAct.setStatusTip('系统操作日志')
        sysLogAct.triggered.connect(self.sysLog)

        sysHelpAct = QAction('系统帮助', self)

        # 退出模块
        userChangeAct = QAction('用户切换', self)
        userChangeAct.setStatusTip('切换用户')
        userChangeAct.triggered.connect(self.userChange)

        userLoginAct = QAction('用户登陆', self)

        exitAct = QAction('系统退出', self)  # exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出系统')
        exitAct.triggered.connect(qApp.exit)

        refreshAct = QAction('刷新', self)  # exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        refreshAct.setShortcut('F5')
        refreshAct.setStatusTip('刷新时间')
        refreshAct.triggered.connect(self.refresh)

        self.menubar = self.menuBar()
        self.status = self.statusBar()

        dataMenu = self.menubar.addMenu('数据')
        dataMenu.addAction(dataInputAct)
        dataMenu.addAction(openFileAct)
        dataMenu.addSeparator()
        dataMenu.addAction(changeDataAct)
        dataMenu.addAction(simulateDataAct)
        dataMenu.addSeparator()
        dataMenu.addAction(leadInAct)
        dataMenu.addAction(leadOutAct)

        visualMenu = self.menubar.addMenu('窑系统热耗分析可视化')
        visualMenu.addAction(dataVisualAct)
        visualMenu.addAction(dataDeviceVisualAct)
        visualMenu.addSeparator()
        visualMenu.addAction(singleVisualAct)
        visualMenu.addAction(mulVisualAct)
        visualMenu.addSeparator()
        visualMenu.addAction(heatVisualAct)
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

        nullAction = QAction('                                                    ', self)
        nullAction.setEnabled(False)
        self.menubar.addAction(nullAction)

        self.menubar.addAction(refreshAct)

    def change_table(self, index1, index2):  # 单击部件时刷新表格数据
        day = str(con.getValue_day())
        col1, col2 = get_by_day(day)  # 返回值为[[],[[],[],[],[]]],col1为名称，col2为参数
        col1 = col1[2:]
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
            hour = con.getValue_hour()

            for i in range(len(col1)):
                newItem = QTableWidgetItem(col1[i])
                self.table.setItem(i, 0, newItem)
                newItem = QTableWidgetItem(str(col2[i][hour]))
                self.table.setItem(i, 1, newItem)

    def selectLab(self, name):
        children = self.findChildren(MyLabel, )
        for child in children:
            child.setStyleSheet('border:0px solid red;')
        child = self.findChild(MyLabel, name)
        child.setStyleSheet('border:1px solid red;')

        if self.messageView.count() == 0:
            self.tab1 = QLabel()  # 这里以后可以修改成不定数量的标签页，以实现不同部件的折线图显示
            self.tab2 = QLabel()
            self.messageView.addTab(self.tab1, '温度')
            self.messageView.addTab(self.tab2, '压强')
            self.pic1 = QVBoxLayout(self.tab1)
            self.pic2 = QVBoxLayout(self.tab2)

    def change_pic(self, index1, index2, name):  # 接收从标签传过来的温度和压强的下标及部件名称
        self.selectLab(name)
        if self.click_flag == 0:
            self.fp1 = MyTempMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.fp2 = MyPressMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.pic1.addWidget(self.fp1)
            self.pic2.addWidget(self.fp2)
            self.change_table(index1[len(index1) - 1] - 2, index2[len(index2) - 1] - 2)
            self.click_flag = 1
            self.updateInfor()
        elif self.click_flag == 1:
            self.sp1 = MyTempMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.sp2 = MyPressMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.pic1.replaceWidget(self.fp1, self.sp1)
            self.pic2.replaceWidget(self.fp2, self.sp2)
            self.change_table(index1[len(index1) - 1] - 2, index2[len(index2) - 1] - 2)
            self.click_flag = 2
            self.updateInfor()
        elif self.click_flag == 2:
            self.fp1 = MyTempMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.fp2 = MyPressMplCanvas(self.messageView, width=4, height=3, dpi=100)
            self.pic1.replaceWidget(self.sp1, self.fp1)
            self.pic2.replaceWidget(self.sp2, self.fp2)
            self.change_table(index1[len(index1) - 1] - 2, index2[len(index2) - 1] - 2)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWindow()
    app.exec_()
