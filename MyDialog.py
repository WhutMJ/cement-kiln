from Production_warning import *
from provide_data_for_gui import *
from Connect_to_Database import *
from Model import *
import config as con
import sys
import sip
import os
from MyPic import *
from youlg_predict import *
from rexiaolv_model import *
from cent_svm_predict import *
from rehao_predict import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from numpy import arange
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
import re
import matplotlib.font_manager as fm
import copy

myfont = fm.FontProperties(fname="C:\\Windows\\Fonts\\simsun.ttc", size=14)  # 设置字体，实现显示中文
matplotlib.rcParams["axes.unicode_minus"] = False


class MyAddUserDlg(QDialog):
    AddUser_Sig = pyqtSignal(bool)

    def __init__(self):
        super(MyAddUserDlg, self).__init__()

        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768

        self.setFixedSize(422 * ratio_width, 322 * ratio_height)
        self.okBtn = QtWidgets.QPushButton('确认', self)
        self.okBtn.setGeometry(QtCore.QRect(150 * ratio_width, 240 * ratio_height, 75 * ratio_width, 23 * ratio_height))
        self.EditWidget = QtWidgets.QWidget(self)
        self.EditWidget.setGeometry(
            QtCore.QRect(170 * ratio_width, 50 * ratio_height, 160 * ratio_width, 141 * ratio_height))
        self.labelVerLay = QtWidgets.QVBoxLayout(self.EditWidget)
        self.labelVerLay.setContentsMargins(0, 0, 0, 0)
        self.username = QtWidgets.QLineEdit(self.EditWidget)
        self.labelVerLay.addWidget(self.username)
        self.password = QtWidgets.QLineEdit(self.EditWidget)
        self.labelVerLay.addWidget(self.password)
        self.level = QtWidgets.QComboBox(self.EditWidget)
        self.level.addItems(['Top_administrator', 'vip'])
        self.labelVerLay.addWidget(self.level)
        self.LabelWidget = QtWidgets.QWidget(self)
        self.LabelWidget.setGeometry(
            QtCore.QRect(100 * ratio_width, 60 * ratio_height, 50 * ratio_width, 121 * ratio_height))
        self.editVerLay = QtWidgets.QVBoxLayout(self.LabelWidget)
        self.editVerLay.setContentsMargins(0, 0, 0, 0)
        self.username_lab = QtWidgets.QLabel(self.LabelWidget)
        self.editVerLay.addWidget(self.username_lab)
        self.password_lab = QtWidgets.QLabel(self.LabelWidget)
        self.editVerLay.addWidget(self.password_lab)
        self.level_lab = QtWidgets.QLabel(self.LabelWidget)
        self.editVerLay.addWidget(self.level_lab)

        self.label = QtWidgets.QLabel(self)
        self.label.move(30 * ratio_width, 30 * ratio_height)

        self.setWindowTitle("添加用户")
        self.username_lab.setText('用户名')
        self.password_lab.setText('密码')
        self.level_lab.setText('权限')
        self.label.setText("添加用户")
        self.label.setFont(QFont("Roman times", 15, QFont.Bold))

        self.username.setFocus()
        self.okBtn.clicked.connect(self.Accept)
        self.show()

    def Accept(self):
        try:
            result = Add_User(self.username.text(), self.password.text(), self.level.currentText())
            operation = '添加用户:'
            operation = operation + self.username.text()
            if operation_record([con.getValue_username(), operation]):
                if result == True:
                    QMessageBox.information(self, '提示', '添加成功', QMessageBox.Yes)
                    self.AddUser_Sig.emit(True)
                    self.close()
                else:
                    operation = operation + '失败!!!'
                    operation_record([con.getValue_username(), operation])
                    self.AddUser_Sig.emit(False)
            else:
                QMessageBox.information(self, '提示', result, QMessageBox.Yes)
        except Exception:
            QMessageBox.information(self, '提示', '异常终止', QMessageBox.Yes)


class MyUserSettingDlg(QDialog):
    def __init__(self):
        super(MyUserSettingDlg, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768
        self.setFixedSize(422 * ratio_width, 322 * ratio_height)
        self.okBtn = QtWidgets.QPushButton('确认修改', self)
        self.okBtn.move(150 * ratio_width, 240 * ratio_height)
        self.EditWidget = QtWidgets.QWidget(self)
        self.EditWidget.setGeometry(
            QtCore.QRect(170 * ratio_width, 50 * ratio_height, 130 * ratio_width, 141 * ratio_height))
        self.labelVerLay = QtWidgets.QVBoxLayout(self.EditWidget)
        self.labelVerLay.setContentsMargins(0, 0, 0, 0)
        self.oldPassword = QtWidgets.QLineEdit(self.EditWidget)
        self.labelVerLay.addWidget(self.oldPassword)
        self.newPassword = QtWidgets.QLineEdit(self.EditWidget)
        self.labelVerLay.addWidget(self.newPassword)
        self.newPassword2 = QtWidgets.QLineEdit(self.EditWidget)
        self.labelVerLay.addWidget(self.newPassword2)
        self.LabelWidget = QtWidgets.QWidget(self)
        self.LabelWidget.setGeometry(
            QtCore.QRect(70 * ratio_width, 60 * ratio_height, 100 * ratio_width, 121 * ratio_height))
        self.editVerLay = QtWidgets.QVBoxLayout(self.LabelWidget)
        self.editVerLay.setContentsMargins(0, 0, 0, 0)
        self.oldPassword_lab = QtWidgets.QLabel(self.LabelWidget)
        self.editVerLay.addWidget(self.oldPassword_lab)
        self.newPassword_lab = QtWidgets.QLabel(self.LabelWidget)
        self.editVerLay.addWidget(self.newPassword_lab)
        self.newPassword2_lab = QtWidgets.QLabel(self.LabelWidget)
        self.editVerLay.addWidget(self.newPassword2_lab)

        self.oldPassword.setFocus()
        self.label = QtWidgets.QLabel(self)
        self.label.move(30 * ratio_width, 30 * ratio_height)

        self.setWindowTitle("修改密码:" + con.getValue_username())
        self.oldPassword_lab.setText('    原密码')
        self.newPassword_lab.setText('    新密码')
        self.newPassword2_lab.setText('再次输入新密码')
        self.label.setText("用户修改")
        self.label.setFont(QFont("Roman times", 15, QFont.Bold))

        self.okBtn.clicked.connect(self.Accept)
        self.show()

    def Accept(self):
        try:
            if self.newPassword.text() == self.newPassword2.text():
                operation = '修改密码'
                result = Update_User(con.getValue_username(), self.oldPassword.text(), self.newPassword.text())
                if result == True:
                    if operation_record([con.getValue_username(), operation]):
                        QMessageBox.information(self, '提示', '修改成功', QMessageBox.Yes)
                        self.close()
                    else:
                        QMessageBox.information(self, '提示', '修改成功但操作记录失败!', QMessageBox.Yes)
                else:
                    QMessageBox.information(self, '提示', result, QMessageBox.Yes)
            else:
                QMessageBox.information(self, '提示', '两次输入的密码不一样', QMessageBox.Yes)
        except Exception:
            self.close()


class MyUserManageDlg(QDialog):
    def __init__(self):
        super(MyUserManageDlg, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768
        self.setFixedSize(465 * ratio_width, 499 * ratio_height)
        self.addUserBtn = QtWidgets.QPushButton('添加用户', self)
        self.addUserBtn.setGeometry(
            QtCore.QRect(60 * ratio_width, 420 * ratio_height, 75 * ratio_width, 23 * ratio_height))
        self.deleteUserBtn = QtWidgets.QPushButton('删除用户', self)
        self.deleteUserBtn.setGeometry(
            QtCore.QRect(190 * ratio_width, 420 * ratio_height, 75 * ratio_width, 23 * ratio_height))
        self.okBtn = QtWidgets.QPushButton('退出', self)
        self.okBtn.setGeometry(QtCore.QRect(320 * ratio_width, 420 * ratio_height, 75 * ratio_width, 23 * ratio_height))
        self.initUser()
        self.label = QtWidgets.QLabel(self)
        self.label.move(50 * ratio_width, 30 * ratio_height)
        self.label.setObjectName("label")

        self.setWindowTitle("用户管理")
        self.label.setText("用户管理")
        self.label.setFont(QFont("Roman times", 15, QFont.Bold))
        self.tip = QLabel(self)
        self.addUserBtn.clicked.connect(self.AddUser)
        self.deleteUserBtn.clicked.connect(self.DeleteUser)
        self.okBtn.clicked.connect(self.Accept)
        self.show()

    def initUser(self):
        state, data = show_all_user('moujun')
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768
        if state:
            self.tableWidget = QtWidgets.QTableWidget(self)
            self.tableWidget.setGeometry(
                QtCore.QRect(50 * ratio_width, 70 * ratio_height, 371 * ratio_width, 311 * ratio_height))
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setHorizontalHeaderLabels(['用户名', '权限'])
            self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
            for i in range(len(data)):
                for j in range(2):
                    newItem = QTableWidgetItem(str(data[i][j]))
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(i, j, newItem)
                    self.tableWidget.item(i, 0).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                    self.tableWidget.item(i, j).setToolTip(str(data[i][j]))
            self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 单击选中一行
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.itemChanged[QTableWidgetItem].connect(self.tableItemChanged)  # 编辑单元格后字体会显示红色
        else:
            QMessageBox.information(self, '提示', data, QMessageBox.Yes)

    def updateUser(self):
        self.tableWidget.itemChanged[QTableWidgetItem].disconnect(self.tableItemChanged)
        state, data = show_all_user('moujun')
        if state:
            self.tableWidget.setRowCount(len(data))
            for i in range(len(data)):
                for j in range(2):
                    newItem = QTableWidgetItem(str(data[i][j]))
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(i, j, newItem)
                    self.tableWidget.item(i, 0).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

            self.tableWidget.itemChanged[QTableWidgetItem].connect(self.tableItemChanged)  # 编辑单元格后字体会显示红色
        else:
            QMessageBox.information(self, '提示', data, QMessageBox.Yes)

    def AddUser(self):
        self.adduserDlg = MyAddUserDlg()
        self.adduserDlg.AddUser_Sig.connect(self.adduser)

    def adduser(self, sig):
        if sig:
            self.tableWidget.itemChanged[QTableWidgetItem].disconnect(self.tableItemChanged)
            state, data = show_all_user('moujun')
            if state:
                self.tableWidget.setRowCount(len(data))
                for i in range(len(data)):
                    for j in range(2):
                        newItem = QTableWidgetItem(str(data[i][j]))
                        newItem.setTextAlignment(Qt.AlignCenter)
                        self.tableWidget.setItem(i, j, newItem)
                        self.tableWidget.item(i, 0).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

                self.tableWidget.itemChanged[QTableWidgetItem].connect(self.tableItemChanged)  # 编辑单元格后字体会显示红色
            else:
                QMessageBox.information(self, '提示', data, QMessageBox.Yes)

    def tableItemChanged(self):
        try:
            self.tableWidget.currentItem().setForeground(QBrush(QColor(255, 0, 0)))
            row = self.tableWidget.currentRow()
            result = Update_Identity('moujun', self.tableWidget.item(row, 0).text(),
                                     self.tableWidget.item(row, 1).text())
            self.tip.setFont(QFont('Microsoft YaHei'))
            self.tip.setStyleSheet("color:red")
            self.tip.setAlignment(Qt.AlignCenter)
            self.tip.setGeometry(QtCore.QRect(0, self.height() * 0.76, self.width(), 23))
            if result == True:
                self.tip.setText('Succeed!')
            else:
                self.tip.setText(result)
            self.updateUser()
        except Exception:
            self.close()

    def DeleteUser(self):
        reply = QMessageBox.information(self, '提示', '是否确认删除该用户？', QMessageBox.Yes | QMessageBox.No)
        if reply:
            try:
                row = self.tableWidget.currentRow()
                operation = '删除用户:'
                operation = operation + self.tableWidget.item(row, 0).text() + ';'
                if operation_record([con.getValue_username(), operation]):
                    result = Delete_User('moujun', self.tableWidget.item(row, 0).text())
                    if result == True:
                        self.tableWidget.removeRow(row)
                        QMessageBox.information(self, '提示', '删除成功', QMessageBox.Yes)
                    else:
                        QMessageBox.information(self, '提示', result, QMessageBox.Yes)
            except Exception:
                self.close()

    def Accept(self):
        self.close()


class MySysLogDlg(QDialog):
    def __init__(self):
        super(MySysLogDlg, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768
        self.resize(500 * ratio_width, 404 * ratio_height)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(
            QtCore.QRect(30 * ratio_width, 50 * ratio_height, 440 * ratio_width, 321 * ratio_height))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['操作时间', '用户名', '操作', '具体内容'])
        # self.tableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.label = QtWidgets.QLabel(self)
        self.label.move(30 * ratio_width, 20 * ratio_height)
        self.label.setObjectName("label")
        self.setWindowTitle("系统日志")
        self.label.setText("操作记录")
        self.label.setFont(QFont("Roman times", 15, QFont.Bold))
        self.show()


class MyTimeDlg(QDialog):  # 选择10小时的
    time_signal = pyqtSignal(str)

    def __init__(self):
        super(MyTimeDlg, self).__init__()
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768
        self.setFixedSize(260 * ratio_width, 330 * ratio_height)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(
            QtCore.QRect(90 * ratio_width, 280 * ratio_height, 75 * ratio_width, 23 * ratio_height))
        self.pushButton.setObjectName("pushButton")
        date = get_all_date()

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(
            QtCore.QRect(20 * ratio_width, 50 * ratio_height, 211 * ratio_width, 211 * ratio_height))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(len(date))
        self.tableWidget.setHorizontalHeaderLabels(['日期', '小时'])
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        for i in range(len(date)):
            for j in range(2):
                newItem = QTableWidgetItem(str(date[i][j]))
                self.tableWidget.setItem(i, j, newItem)
                self.tableWidget.item(i, j).setToolTip(str(date[i][j]))
                self.tableWidget.item(i, j).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 单击选中一行
        # self.tableWidget.horizontalHeader().setDefaultSectionSize(75)  # 列宽
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20 * ratio_width, 20 * ratio_height, 54 * ratio_width, 12 * ratio_height))
        self.label.setObjectName("label")

        if con.getValue_flag_Visual() == -1:
            self.setWindowTitle("选择窑系统数据可视化的初始时间")
        else:
            self.setWindowTitle("选择时间")
        self.pushButton.setText("OK")
        self.label.setText("选择时间")

        self.pushButton.clicked.connect(self.Accept)
        self.show()

    def Accept(self):
        try:
            row = self.tableWidget.currentRow()
            # print(self.tableWidget.item(row, 0).text() + self.tableWidget.item(row, 1).text())
            self.time_signal.emit(self.tableWidget.item(row, 0).text() + self.tableWidget.item(row, 1).text())
            self.close()
        except Exception:
            self.close()


# 以后此类可以被MyTimeDlg替换掉
class MyDayDlg(QDialog):  # 选择24小时的
    time_signal = pyqtSignal(str)

    def __init__(self):
        super(MyDayDlg, self).__init__()
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768
        self.setFixedSize(260 * ratio_width, 330 * ratio_height)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(
            QtCore.QRect(90 * ratio_width, 280 * ratio_height, 75 * ratio_width, 23 * ratio_height))
        self.pushButton.setObjectName("pushButton")
        date = get_all_date()

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(
            QtCore.QRect(20 * ratio_width, 50 * ratio_height, 211 * ratio_width, 211 * ratio_height))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(len(date))
        self.tableWidget.setHorizontalHeaderLabels(['日期', '小时'])
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        for i in range(len(date)):
            for j in range(2):
                newItem = QTableWidgetItem(str(date[i][j]))
                self.tableWidget.setItem(i, j, newItem)
                self.tableWidget.item(i, j).setToolTip(str(date[i][j]))
                self.tableWidget.item(i, j).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 单击选中一行
        # self.tableWidget.horizontalHeader().setDefaultSectionSize(75)  # 列宽
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20 * ratio_width, 20 * ratio_height, 54 * ratio_width, 12 * ratio_height))

        self.setWindowTitle("选择时间(24小时的数据）")
        self.pushButton.setText("OK")
        self.label.setText("选择时间")

        self.pushButton.clicked.connect(self.Accept)
        self.show()
        '''data = get_all_date()
        date = []
        for i in range(len(data)):
            date.append(data[i][0])
        data = date
        date = list(set(date))
        date.sort(key=data.index)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(
            QtCore.QRect(20 * ratio_width, 50 * ratio_height, 211 * ratio_width, 211 * ratio_height))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(len(date))
        self.tableWidget.setHorizontalHeaderLabels(['日期'])
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        for i in range(len(date)):
            newItem = QTableWidgetItem(str(date[i]))
            newItem.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(i, 0, newItem)
            self.tableWidget.item(i, 0).setToolTip(str(date[i]))
            self.tableWidget.item(i, 0).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 单击选中一行
        # self.tableWidget.horizontalHeader().setDefaultSectionSize(75)  # 列宽
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20 * ratio_width, 20 * ratio_height, 54 * ratio_width, 12 * ratio_height))
        self.label.setObjectName("label")

        self.setWindowTitle("选择时间")
        self.pushButton.setText("OK")
        self.label.setText("选择时间")

        self.pushButton.clicked.connect(self.Accept)
        self.show()'''

    def Accept(self):
        try:
            row = self.tableWidget.currentRow()
            # print(self.tableWidget.item(row, 0).text() + self.tableWidget.item(row, 1).text())
            self.time_signal.emit(self.tableWidget.item(row, 0).text() + self.tableWidget.item(row, 1).text())
            self.close()
        except Exception:
            self.close()


class MyDataSimDlg(QDialog):
    def __init__(self, time):
        super(MyDataSimDlg, self).__init__()
        name, value = get_by_hour(time)

        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768

        self.setFixedSize(800 * ratio_width, 600 * ratio_height)

        self.label = QtWidgets.QLabel(self)
        self.label.move(20 * ratio_width, 30 * ratio_height)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(
            QtCore.QRect(20 * ratio_width, 70 * ratio_height, 321 * ratio_width, 471 * ratio_height))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(len(name))
        self.tableWidget.setHorizontalHeaderLabels(['表头', '原数据', '模拟数据(可修改)'])
        # self.tableWidget.horizontalHeader().setDefaultSectionSize(90)  # 列宽
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i in range(len(name)):
            newItem = QTableWidgetItem(name[i])
            self.tableWidget.setItem(i, 0, newItem)
            self.tableWidget.item(i, 0).setToolTip(str(name[i]))
            if value[i] == None:
                newItem = QTableWidgetItem('')
                newItem2 = QTableWidgetItem('')
            else:
                newItem = QTableWidgetItem(str(value[i]))
                newItem2 = QTableWidgetItem(str(value[i]))
            self.tableWidget.setItem(i, 1, newItem)
            self.tableWidget.setItem(i, 2, newItem2)
            self.tableWidget.item(i, 1).setToolTip(str(value[i]))
            self.tableWidget.item(i, 2).setToolTip(str(value[i]))
            self.tableWidget.item(i, 0).setFlags(Qt.ItemIsEnabled)
            self.tableWidget.item(i, 1).setFlags(Qt.ItemIsEnabled)
        if get_target_data(time) != False:
            name2, value2 = get_target_data(time)
        else:
            name2, value = '', ''
        self.tableWidget_2 = QtWidgets.QTableWidget(self)
        self.tableWidget_2.setGeometry(
            QtCore.QRect(430 * ratio_width, 70 * ratio_height, 321 * ratio_width, 471 * ratio_height))
        self.tableWidget_2.setAlternatingRowColors(False)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setRowCount(len(name2))
        # self.tableWidget_2.horizontalHeader().setDefaultSectionSize(70)  # 列宽
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.setHorizontalHeaderLabels(['表头', '原结果', '模拟结果', '变化幅度'])

        for i in range(len(name2)):
            newItem = QTableWidgetItem(name2[i])
            self.tableWidget_2.setItem(i, 0, newItem)
            self.tableWidget_2.item(i, 0).setToolTip(str(name2[i]))
            if value2[i] == None:
                newItem = QTableWidgetItem('')
            else:
                newItem = QTableWidgetItem(str(value2[i]))
            self.tableWidget_2.setItem(i, 1, newItem)
            self.tableWidget_2.item(i, 1).setToolTip(str(value2[i]))
            self.tableWidget_2.item(i, 0).setFlags(Qt.ItemIsEnabled)
            self.tableWidget_2.item(i, 1).setFlags(Qt.ItemIsEnabled)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(
            QtCore.QRect(360 * ratio_width, 270 * ratio_height, 61 * ratio_width, 41 * ratio_height))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)

        self.label_3.move(430 * ratio_width, 31 * ratio_height)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(
            QtCore.QRect(670 * ratio_width, 550 * ratio_height, 75 * ratio_width, 23 * ratio_height))
        self.pushButton.setObjectName("pushButton")

        self.setWindowTitle("Dialog")
        self.label.setText("模拟数据")
        self.label.setFont(QFont("Roman times", 15, QFont.Bold))

        self.statePic = QPixmap('picture\\white.png')
        self.label_2.setPixmap(self.statePic.scaled(50, 30))
        self.label_3.setText("生产预警变化")
        self.label_3.setFont(QFont("Roman times", 15, QFont.Bold))
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.Accept)

        self.show()

    def Accept(self):
        self.statePic = QPixmap('picture\\red.png')
        self.label_2.setPixmap(self.statePic.scaled(50, 30))
        col_data = []
        for i in range(self.tableWidget.rowCount()):
            try:
                col_data.append(self.tableWidget.item(i, 2).text())
            except Exception:
                col_data.append('')


class MyDataLeadInDlg(QDialog):  # 数据导入
    def __init__(self):
        super(MyDataLeadInDlg, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768
        self.setFixedSize(600 * ratio_width, 390 * ratio_height)

        self.tableWidget = QtWidgets.QTableWidget(self)

        self.tableWidget.setGeometry(
            QtCore.QRect(10 * ratio_width, 70 * ratio_height, 580 * ratio_width, 250 * ratio_height))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(3)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.resizeColumnsToContents()  # 不能放在后面，否则不起作用
        # self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.label = QtWidgets.QLabel(self)
        self.label.move(20 * ratio_width, 20 * ratio_height)
        # self.label.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.label.setObjectName("label")

        self.setWindowTitle("设置标准表头")
        self.label.setText("从左至右，自上而下按顺序添加表头，一行不够请点击添加按钮")
        self.label.setFont(QFont("Roman times", 15, QFont.Bold))
        self.lay = QHBoxLayout()
        self.pushButton = QtWidgets.QPushButton(self)
        # self.pushButton.setGeometry(QtCore.QRect(90, 280, 75, 23))
        self.pushButton.setText("另存为")
        self.pushButton.clicked.connect(self.Accept)
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setText('添加')
        self.pushButton_2.clicked.connect(self.Add)
        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setText('选择标准表头文件')
        self.pushButton_3.clicked.connect(self.OpenStandardFile)
        self.lay.addWidget(self.pushButton_2)
        self.lay.addWidget(self.pushButton)
        self.lay.addWidget(self.pushButton_3)

        self.lay.setGeometry(QtCore.QRect(150 * ratio_width, 350 * ratio_height, 300 * ratio_width, 23 * ratio_height))
        self.initTable()
        self.show()

    def initTable(self):
        name = get_table_name()

        for i in range(len(name)):
            if i >= self.tableWidget.rowCount() * 5:
                self.Add()
            newItem = QTableWidgetItem(name[i])
            self.tableWidget.setItem(i / 5, i % 5, newItem)
        if self.tableWidget.rowCount() * 5 == len(name):
            self.Add()

    def Add(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.scrollToBottom()

    def Accept(self):
        try:
            data = []
            for row in range(self.tableWidget.rowCount()):
                for col in range(self.tableWidget.columnCount()):
                    if self.tableWidget.item(row, col):
                        data.append(self.tableWidget.item(row, col).text())

            filepath = con.getValue_filepath()
            fileName, filetype = QFileDialog.getSaveFileName(self,
                                                             "文件保存", filepath,
                                                             "Excel Files (*.xlsx);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔

            filedir = os.path.split(fileName)  # 获取文件所在的文件夹
            filepath = filedir[0]  # 文件路径信息
            con.setValue_filepath(filepath)
            Build_table(data, fileName)  # 创建新的表头文件

            self.close()
        except Exception:
            reply = QMessageBox.information(self, '提示', '创建失败', QMessageBox.Yes | QMessageBox.No)
            self.close()

    def OpenStandardFile(self):
        filepath = con.getValue_filepath()
        fileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "文件选择", filepath,
                                                         "Excel Files (*.xlsx);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔
        # print(fileName)
        filedir = os.path.split(fileName)  # 获取文件所在的文件夹
        filepath = filedir[0]  # 文件路径信息
        con.setValue_filepath(filepath)


class MyOpenFileWnd(QMainWindow):
    def __init__(self):
        super(MyOpenFileWnd, self).__init__()
        filepath = con.getValue_filepath()
        fileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "选取文件", filepath,
                                                         "Excel Files (*.xlsx);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔

        try:
            filedir = os.path.split(fileName)  # 获取文件所在的文件夹
            filepath = filedir[0]  # 文件路径信息
            self.filename = filedir[1]  # 文件名
            con.setValue_filepath(filepath)
            self.name, self.data = Read_file(fileName)
            self.initUI()
            self.initTable()
        except Exception:
            print('未选择')

    def initUI(self):
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(
            QtCore.QRect(10 * ratio_width, 40 * ratio_height, (width - 20) * ratio_width, height * 0.8 * ratio_height))
        self.tableWidget.setRowCount(len(self.data[0]))
        self.tableWidget.setColumnCount(len(self.name))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText(self.filename)
        self.label.setFont(QFont("Roman times", 15, QFont.Bold))
        self.label.move(width * 0.5 - self.label.width() / 2, 10 * ratio_height)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menu = QtWidgets.QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(self)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(self)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        self.setWindowTitle("打开文件")
        self.menu.setTitle("数据")
        self.action.setText("数据保存")
        self.action_2.setText("数据另存为")
        self.action_2.triggered.connect(self.Save_As)

        self.showMaximized()

    def initTable(self):
        value = list(map(list, zip(*self.data)))
        self.tableWidget.setHorizontalHeaderLabels(self.name)

        try:
            dateIndex = self.name.index('date')
        except Exception:
            dateIndex = -1
        if dateIndex != -1:
            for i in range(len(value)):
                value[i][dateIndex] = int(value[i][dateIndex])
        try:
            timeIndex = self.name.index('time')
        except Exception:
            timeIndex = -1
        if timeIndex != -1:
            for i in range(len(value)):
                value[i][timeIndex] = int(value[i][timeIndex])
        # 以上两个循环将float变为int
        for i in range(len(value)):
            for j in range(len(self.name)):
                try:
                    newItem = QTableWidgetItem(str(value[i][j]))
                    self.tableWidget.setItem(i, j, newItem)
                    self.tableWidget.item(i, j).setToolTip(str(value[i][j]))
                except Exception:
                    newItem = QTableWidgetItem('')
                    self.tableWidget.setItem(i, j, newItem)

    def Save_As(self):
        pass  # 另存为


class MyStandardValueDlg(QDialog):  # 生产数据标准设置窗口
    def __init__(self):
        super(MyStandardValueDlg, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768
        self.setFixedSize(320 * ratio_width, 521 * ratio_height)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(
            QtCore.QRect(120 * ratio_width, 480 * ratio_height, 75 * ratio_width, 23 * ratio_height))
        self.pushButton.setObjectName("pushButton")

        self.name = get_table_name()
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(
            QtCore.QRect(20 * ratio_width, 50 * ratio_height, 270 * ratio_width, 400 * ratio_height))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(len(self.name))
        self.tableWidget.setHorizontalHeaderLabels(['名称', '最小值', '最大值'])

        for i in range(len(self.name)):
            newItem = QTableWidgetItem(str(self.name[i]))
            self.tableWidget.setItem(i, 0, newItem)
            self.tableWidget.item(i, 0).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            self.tableWidget.item(i, 0).setToolTip(str(self.name[i]))
        # self.tableWidget.horizontalHeader().setDefaultSectionSize(80)  # 列宽
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.label = QtWidgets.QLabel(self)
        self.label.move(20 * ratio_width, 10 * ratio_height)
        self.setWindowTitle("生产数据标准设置")
        self.pushButton.setText("确定")
        self.label.setText("生产数据标准设置")
        self.label.setFont(QFont("Roman times", 15, QFont.Bold))
        self.pushButton.clicked.connect(self.Accept)

        self.show()

    def Accept(self):
        try:
            min = []
            max = []
            for i in range(len(self.name)):
                if self.tableWidget.item(i, 1) == None:
                    min.append('')
                else:
                    min.append(self.tableWidget.item(i, 1).text())
                if self.tableWidget.item(i, 2) == None:
                    max.append('')
                else:
                    max.append(self.tableWidget.item(i, 2).text())
            print(min)
            print(max)
            self.close()
        except Exception:
            print('异常')
            self.close()


class MyRadioWnd(QMainWindow):
    check_signal = pyqtSignal(list)

    def __init__(self):
        super(MyRadioWnd, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        self.Width = metric.width()
        self.Height = metric.height()
        self.flag = 0
        self.setFixedSize(self.Width * 0.368, self.Height * 0.618)
        self.lay = QGridLayout()  # 初始化布局

        number = con.getValue_number()  # 旋风筒个数
        flag_Ser = con.getValue_flag_Ser()  # 窑系统系列
        self.xft = {}
        for i in range(number):
            self.xft[i] = QRadioButton('%d级筒A' % (i + 1), self)
            self.xft[i].setObjectName('%d级筒A' % (i + 1))
            self.lay.addWidget(self.xft[i], i / 3, i % 3)
        if flag_Ser == 2:
            for i in range(number):
                self.xft[i + number] = QRadioButton('%d级筒B' % (i + 1), self)
                self.xft[i + number].setObjectName('%d级筒B' % (i + 1))
                self.lay.addWidget(self.xft[i + number], (i + number) / 3, (i + number) % 3)

        self.fjl = QRadioButton('分解炉')
        self.fjl.setObjectName('分解炉')
        self.lay.addWidget(self.fjl)
        self.yao1 = QRadioButton('窑1')
        self.yao1.setObjectName('窑1')
        self.lay.addWidget(self.yao1)
        self.yao2 = QRadioButton('窑2')
        self.yao2.setObjectName('窑2')
        self.lay.addWidget(self.yao2)
        self.yao3 = QRadioButton('窑3')
        self.yao3.setObjectName('窑3')
        self.lay.addWidget(self.yao3)
        self.blj1 = QRadioButton('篦冷机1')
        self.blj1.setObjectName('篦冷机1')
        self.lay.addWidget(self.blj1)
        self.blj2 = QRadioButton('篦冷机2')
        self.blj2.setObjectName('篦冷机2')
        self.lay.addWidget(self.blj2)
        self.blj3 = QRadioButton('篦冷机3')
        self.blj3.setObjectName('篦冷机3')
        self.lay.addWidget(self.blj3)

        self.lay.setSpacing(40)
        self.lay.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.widget = QWidget(self)
        self.widget.setGeometry(QtCore.QRect(20, 40, self.Width * 0.36, self.Height * 0.5))
        self.widget.setLayout(self.lay)

        self.mainWidget = QWidget()
        self.mainLay = QHBoxLayout()
        self.mainLay.addWidget(self.widget)
        self.mainWidget.setLayout(self.mainLay)
        self.setCentralWidget(self.mainWidget)

        self.okBtn = QPushButton('确定', self.mainWidget)
        self.okBtn.move(self.width() * 0.7, self.height() * 0.9)

        self.okBtn.clicked.connect(self.Accept)
        self.setWindowTitle('请选择您想要的部件')

        self.show()

    def Accept(self):
        children = self.findChildren(QRadioButton, )
        check_name = []  # 被选中的部件名称
        for child in children:
            if child.isChecked():
                check_name.append(child.objectName())
                print(child.objectName())
        self.addDock()
        self.check_signal.emit(check_name)

    def addDock(self):
        print(777)
        if self.flag == 0:
            dock1 = MyDockWidget('')
            dock1.setFeatures(QDockWidget.DockWidgetClosable)
            dock1.setAllowedAreas(Qt.RightDockWidgetArea)
            print(8888)
            # self.bar = MyHeatCanvas()  # 此处应该有value
            # dock1.setFixedWidth(400)
            # dock1.setWidget(self.bar)
            print(789)
            dock1.dock_signal.connect(self.change)
            self.addDockWidget(Qt.RightDockWidgetArea, dock1)
            self.setFixedSize(self.Width * 0.368 + 400, self.Height * 0.618)
            self.flag = 1
            print(789)
        else:
            pass

    def change(self, str):
        self.setFixedSize(self.Width * 0.368, self.Height * 0.618)
        self.flag = 0


class MyCheckWnd(QMainWindow):
    check_signal = pyqtSignal(list)

    def __init__(self):
        super(MyCheckWnd, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        self.Width = metric.width()
        self.Height = metric.height()
        self.flag = 0
        self.setFixedSize(self.Width * 0.618, self.Height * 0.618)
        self.move(50, (self.Height - self.height()) / 2)
        self.mainlay = QGridLayout()  # 选项主布局

        tablename = get_table_name()  # 获取所有因素
        tablename.remove('date')
        tablename.remove('time')
        tablename.remove('youlig')
        tablename.remove('rehao')  # 去除不需要的
        # print(tablename)

        class1 = ['ruyaomfhf', 'ruyaomfsf', 'ruyaomfhff', 'reyaomfrz', 'ruyaomfgdt']
        class2 = ['chumoslKH', 'chumoslSM', 'chumoslIM', 'ruyaoslCaO', 'ruyaoslFe2O3', 'ruyaoslKH', 'ruyaoslSM',
                  'ruyaoslIM', 'CaO', 'Fe2O3']
        class3 = ['weiliaoc', 'yaotouc', 'yaoweic']
        class4 = ['yijitwdA', 'yijityqA', 'yijitwdB', 'yijityqB', 'erjitwdA', 'erjityqA', 'erjitwdB', 'erjityqB',
                  'sanjitwdA', 'sanjityqA', 'sanjitwdB', 'sanjityqB', 'sijitwdA', 'sijityqA', 'sijitwdB', 'sijityqB',
                  'wujitwdA', 'wujityqA', 'wujitwdB', 'wujityqB']
        class5 = ['yaos', 'yaoweiwd', 'yicifj', 'yaotouyl']
        class6 = ['bilengjydyl', 'bilengjydS1', 'bilengjydI1', 'bilengjedS1', 'bilengjedI1', 'bilengjsdS1',
                  'bilengjsdI1', 'sancifyl', 'fengjizs', 'fengjidl']
        class7 = ['shuliaoKH', 'shuliaoSM', 'shuliaoIM', 'shuliaoK2O', 'shuliaoNa2O', 'shuliaoSO3']
        # print(len(tablename))
        # print(len(class1)+len(class2)+len(class3)+len(class4)+len(class5)+len(class6)+len(class7))
        self.element = {}
        count = 0
        groupBox1 = QGroupBox('煤粉制备:')
        groupBox1.setFlat(False)
        layout1 = QGridLayout()
        for i in range(len(class1)):
            x = class1[i]
            self.element[count] = QCheckBox(get_chinese(x))
            self.element[count].setObjectName(x)
            layout1.addWidget(self.element[count], i % 10, i / 10)
            count = count + 1
        groupBox1.setLayout(layout1)
        self.mainlay.addWidget(groupBox1)

        groupBox2 = QGroupBox('生料制备')
        groupBox2.setFlat(False)
        layout2 = QGridLayout()
        for i in range(len(class2)):
            x = class2[i]
            self.element[count] = QCheckBox(get_chinese(x))
            self.element[count].setObjectName(x)
            layout2.addWidget(self.element[count], i % 10, i / 10)
            count = count + 1
        groupBox2.setLayout(layout2)
        self.mainlay.addWidget(groupBox2, 0, 1)

        groupBox3 = QGroupBox('计量喂料:')
        groupBox3.setFlat(False)
        layout3 = QGridLayout()
        for i in range(len(class3)):
            x = class3[i]
            self.element[count] = QCheckBox(get_chinese(x))
            self.element[count].setObjectName(x)
            layout3.addWidget(self.element[count], i % 10, i / 10)
            count = count + 1
        groupBox3.setLayout(layout3)
        self.mainlay.addWidget(groupBox3, 0, 2)

        groupBox4 = QGroupBox('预热预分解:')
        groupBox4.setFlat(False)
        layout4 = QGridLayout()
        for i in range(len(class4)):
            x = class4[i]
            self.element[count] = QCheckBox(get_chinese(x))
            self.element[count].setObjectName(x)
            layout4.addWidget(self.element[count], i % 10, i / 10)
            count = count + 1
        groupBox4.setLayout(layout4)
        self.mainlay.addWidget(groupBox4, 0, 3)

        groupBox5 = QGroupBox('回转窑煅烧:')
        groupBox5.setFlat(False)
        layout5 = QGridLayout()
        for i in range(len(class5)):
            x = class5[i]
            self.element[count] = QCheckBox(get_chinese(x))
            self.element[count].setObjectName(x)
            layout5.addWidget(self.element[count], i % 10, i / 10)
            count = count + 1
        groupBox5.setLayout(layout5)
        self.mainlay.addWidget(groupBox5)

        groupBox6 = QGroupBox('冷却熟料:')
        groupBox6.setFlat(False)
        layout6 = QGridLayout()
        for i in range(len(class6)):
            x = class6[i]
            self.element[count] = QCheckBox(get_chinese(x))
            self.element[count].setObjectName(x)
            layout6.addWidget(self.element[count], i % 10, i / 10)
            count = count + 1
        groupBox6.setLayout(layout6)
        self.mainlay.addWidget(groupBox6)

        groupBox7 = QGroupBox('熟料输送:')
        groupBox7.setFlat(False)
        layout7 = QGridLayout()
        for i in range(len(class7)):
            x = class7[i]
            self.element[count] = QCheckBox(get_chinese(x))
            self.element[count].setObjectName(x)
            layout7.addWidget(self.element[count], i % 10, i / 10)
            count = count + 1
        groupBox7.setLayout(layout7)
        self.mainlay.addWidget(groupBox7)

        '''row = (len(tablename) + 1) / 3
        self.element = {}
        self.lay.addWidget(QLabel('勾选你需要的因素'), 0, 0)
        defaultElement = []
        for i in range(1, len(tablename) + 1):
            self.element[i] = QCheckBox(get_chinese(tablename[i - 1]), self)
            self.element[i].setObjectName(tablename[i - 1])
            self.lay.addWidget(self.element[i], (i - 1) % row + 1, (i - 1) / row)'''

        self.mainlay.setSpacing(5)
        self.mainlay.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.widget = QWidget(self)
        self.widget.setGeometry(QtCore.QRect(20, 20, self.Width * 0.36, self.Height * 0.5))
        self.widget.setLayout(self.mainlay)

        self.mainWidget = QWidget()
        self.mainLay = QHBoxLayout()
        self.mainLay.addWidget(self.widget)
        # self.mainLay.addWidget(self.btnWidget)
        self.mainWidget.setLayout(self.mainLay)
        self.setCentralWidget(self.mainWidget)
        self.btnWidget = QWidget(self.mainWidget)
        # self.btnLay = QVBoxLayout()

        self.checkAllBtn = QPushButton('全选')
        self.invertBtn = QPushButton('反选')
        self.okBtn = QPushButton('确定')
        self.timeBox = QComboBox()
        date = get_all_date()
        for i in range(len(date)):
            self.timeBox.addItem(date[i][0] + ' ' + date[i][1])
        self.timeBox.setCurrentIndex(6)
        buttonBox = QGroupBox('')
        buttonBox.setFlat(False)
        layoutBtn = QVBoxLayout()
        layoutBtn.addWidget(self.timeBox)
        layoutBtn.addWidget(self.checkAllBtn)
        layoutBtn.addWidget(self.invertBtn)
        layoutBtn.addWidget(self.okBtn)
        buttonBox.setLayout(layoutBtn)
        # buttonBox.setGeometry(QtCore.QRect(self.width()*0.7,self.height()*0.418,self.width()*0.1,self.height()*0.3))
        self.mainlay.addWidget(buttonBox, 0, 4, 2, 1)
        '''self.timeBox.move(self.width() * 0.7, self.height() * 0.418 - 40)
        self.checkAllBtn.move(self.width() * 0.7, self.height() * 0.418)
        self.invertBtn.move(self.width() * 0.7, self.height() * 0.418 + 40)
        self.okBtn.move(self.width() * 0.7, self.height() * 0.418 + 80)'''

        # self.btnWidget.move(self.width() * 0.8, self.height() * 0.418)
        # self.btnLay.setGeometry(QtCore.QRect(self.width() * 0.8, self.height() * 0.418,100,60))
        # self.btnWidget.setLayout(self.btnLay)

        self.checkAllBtn.clicked.connect(self.checkAll)
        self.invertBtn.clicked.connect(self.Invert)
        self.okBtn.clicked.connect(self.Accept)
        self.setWindowTitle('请勾选您想要的部件')

        self.show()

    def checkAll(self):
        children = self.findChildren(QCheckBox, )
        for child in children:
            child.setChecked(True)

    def Invert(self):  # 反选
        children = self.findChildren(QCheckBox, )
        for child in children:
            child.setChecked(not child.checkState())

    def Accept(self):
        children = self.findChildren(QCheckBox, )
        check_name = []  # 被选中的部件名称
        for child in children:
            if child.isChecked():
                check_name.append(child.objectName())
        self.addDock()
        self.check_signal.emit(check_name)

    def addDock(self):
        if self.flag == 0:
            dock1 = MyDockWidget('DockWidget')
            dock1.setFeatures(QDockWidget.DockWidgetClosable)
            dock1.setAllowedAreas(Qt.RightDockWidgetArea)

            value = []
            time = self.timeBox.currentText()
            time = time[:8] + time[9:]
            data = get_by_hour(time)
            value.append(Production_warning_rehao(data[1]))
            value.append(Production_warning_fenjielu(data[1]))
            value.append(value[0] - value[1])
            value.append(Production_warning_rexiaolv(data[1]))
            self.bar = MyHeatCanvas(value)
            dock1.setFixedWidth(400)
            dock1.setWidget(self.bar)
            dock1.dock_signal.connect(self.change)
            self.addDockWidget(Qt.RightDockWidgetArea, dock1)
            self.setFixedSize(self.Width * 0.618 + 400, self.Height * 0.618)
            self.flag = 1
        else:
            pass

    def change(self, str):
        self.setFixedSize(self.Width * 0.368, self.Height * 0.618)
        self.flag = 0


class MyDockWidget(QDockWidget):
    dock_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyDockWidget, self).__init__(parent)

    def closeEvent(self, QCloseEvent):
        self.dock_signal.emit('close')


class MyYaoDlg(QDialog):
    def __init__(self):
        super(MyYaoDlg, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        self.ratio_width = width / 1366
        self.ratio_height = height / 768
        self.setFixedSize(width * 0.6, height * 0.6)

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, width * 0.58, height * 0.55))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(5)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(['设备', '名称', '描述', '数据'])
        # self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setDefaultSectionSize(120)
        self.loadPic()
        self.loadTable()
        self.setWindowTitle("窑系统数据")
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.show()

    def loadPic(self):
        self.xft = QPixmap('picture\\xft_dl.png')
        self.blj = QPixmap('picture\\blj.png')
        self.yao = QPixmap('picture\\yao.png')
        self.fjl = QPixmap('picture\\fjl.png')
        self.fjl_yao = QPixmap('picture\\fjl_yao.png')

    def loadTable(self):
        self.lay1 = QHBoxLayout()
        self.item1 = QLabel()
        self.item1.setPixmap(
            self.xft.scaled(120 * self.ratio_width, 120 * self.ratio_height, aspectRatioMode=Qt.KeepAspectRatio))
        self.lay1.addWidget(self.item1)
        self.lay1.setAlignment(Qt.AlignCenter)
        widget = QWidget()
        widget.setLayout(self.lay1)
        self.tableWidget.setCellWidget(0, 0, widget)

        self.lay2 = QHBoxLayout()
        self.item2 = QLabel()
        self.item2.setPixmap(
            self.blj.scaled(120 * self.ratio_width, 120 * self.ratio_height, aspectRatioMode=Qt.KeepAspectRatio))
        self.lay2.addWidget(self.item2)
        self.lay2.setAlignment(Qt.AlignCenter)
        widget2 = QWidget()
        widget2.setLayout(self.lay2)
        self.tableWidget.setCellWidget(1, 0, widget2)

        self.lay3 = QHBoxLayout()
        self.item3 = QLabel()
        self.item3.setPixmap(
            self.yao.scaled(120 * self.ratio_width, 120 * self.ratio_height, aspectRatioMode=Qt.KeepAspectRatio))
        self.lay3.addWidget(self.item3)
        self.lay3.setAlignment(Qt.AlignCenter)
        widget3 = QWidget()
        widget3.setLayout(self.lay3)
        self.tableWidget.setCellWidget(2, 0, widget3)

        self.lay4 = QHBoxLayout()
        self.item4 = QLabel()
        self.item4.setPixmap(
            self.fjl.scaled(120 * self.ratio_width, 120 * self.ratio_height, aspectRatioMode=Qt.KeepAspectRatio))
        self.lay4.addWidget(self.item4)
        self.lay4.setAlignment(Qt.AlignCenter)
        widget4 = QWidget()
        widget4.setLayout(self.lay4)
        self.tableWidget.setCellWidget(3, 0, widget4)

        self.lay5 = QHBoxLayout()
        self.item5 = QLabel()
        self.item5.setPixmap(
            self.fjl_yao.scaled(120 * self.ratio_width, 120 * self.ratio_height, aspectRatioMode=Qt.KeepAspectRatio))
        self.lay5.addWidget(self.item5)
        self.lay5.setAlignment(Qt.AlignCenter)
        widget5 = QWidget()
        widget5.setLayout(self.lay5)
        self.tableWidget.setCellWidget(4, 0, widget5)


class MyVisualDlg(QDialog):  # 可视化对象设置窗口，目前还未完成，还需要将文件路径保存至全局变量config文件中
    def __init__(self):
        super(MyVisualDlg, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        self.ratio_width = width / 1366
        self.ratio_height = height / 768
        self.setFixedSize(width * 0.6, height * 0.6)
        self.mainWidget = QWidget(self)
        self.mainWidget.setGeometry(50, 50, width * 0.4, height * 0.4)
        self.loadPic()
        self.loadLable()
        self.loadLayout()

        self.setWindowTitle("可视化对象设置")
        self.show()

    def loadPic(self):
        self.xft = QPixmap('picture\\xft_dl.png')
        self.blj = QPixmap('picture\\blj.png')
        self.yao = QPixmap('picture\\yao.png')
        self.fjl = QPixmap('picture\\fjl.png')
        self.fjl_yao = QPixmap('picture\\fjl_yao.png')

    def loadLable(self):
        self.lab_xft = MyVisualLabel()
        self.lab_xft.setToolTip('旋风筒')
        self.lab_xft.setObjectName('旋风筒')
        self.lab_xft.setPixmap(self.xft.scaled(231 * self.ratio_width, 50 * self.ratio_height,
                                               aspectRatioMode=Qt.KeepAspectRatio))
        self.lab_xft.index.connect(self.change_pic)
        self.lab_xft.setStyleSheet('border:1px solid red;')
        self.lab_xft.setAlignment(Qt.AlignCenter)

        self.lab_blj = MyVisualLabel()
        self.lab_blj.setToolTip('篦冷机')
        self.lab_blj.setObjectName('篦冷机')
        self.lab_blj.setPixmap(self.blj.scaled(231 * self.ratio_width, 50 * self.ratio_height,
                                               aspectRatioMode=Qt.KeepAspectRatio))
        self.lab_blj.index.connect(self.change_pic)
        self.lab_blj.setStyleSheet('border:1px solid red;')
        self.lab_blj.setAlignment(Qt.AlignCenter)

        self.lab_yao = MyVisualLabel()
        self.lab_yao.setToolTip('窑')
        self.lab_yao.setObjectName('窑')
        self.lab_yao.setPixmap(self.yao.scaled(231 * self.ratio_width, 50 * self.ratio_height,
                                               aspectRatioMode=Qt.KeepAspectRatio))
        self.lab_yao.index.connect(self.change_pic)
        self.lab_yao.setStyleSheet('border:1px solid red;')
        self.lab_yao.setAlignment(Qt.AlignCenter)

        self.lab_fjl = MyVisualLabel()
        self.lab_fjl.setToolTip('分解炉')
        self.lab_fjl.setObjectName('分解炉')
        self.lab_fjl.setPixmap(self.fjl.scaled(231 * self.ratio_width, 50 * self.ratio_height,
                                               aspectRatioMode=Qt.KeepAspectRatio))
        self.lab_fjl.index.connect(self.change_pic)
        self.lab_fjl.setStyleSheet('border:1px solid red;')
        self.lab_fjl.setAlignment(Qt.AlignCenter)

        self.lab_fjl_yao = MyVisualLabel()
        self.lab_fjl_yao.setToolTip('分解炉--窑')
        self.lab_fjl_yao.setObjectName('分解炉--窑')
        self.lab_fjl_yao.setPixmap(self.fjl_yao.scaled(231 * self.ratio_width, 50 * self.ratio_height,
                                                       aspectRatioMode=Qt.KeepAspectRatio))
        self.lab_fjl_yao.index.connect(self.change_pic)
        self.lab_fjl_yao.setStyleSheet('border:1px solid red;')
        self.lab_fjl_yao.setAlignment(Qt.AlignCenter)

    def loadLayout(self):

        self.mainLay = QGridLayout(self.mainWidget)
        self.mainLay.addWidget(self.lab_xft, 0, 0)
        self.mainLay.addWidget(self.lab_blj, 0, 1)
        self.mainLay.addWidget(self.lab_yao, 0, 2)
        self.mainLay.addWidget(self.lab_fjl, 1, 0)
        self.mainLay.addWidget(self.lab_fjl_yao, 1, 1)

        self.mainWidget.setLayout(self.mainLay)

    def change_pic(self, objName, filepath):
        print(objName)
        print(filepath)
        if filepath != '':
            if objName == '旋风筒':
                self.xft = QPixmap(filepath)
                self.lab_xft.setPixmap(self.xft.scaled(231 * self.ratio_width, 50 * self.ratio_height,
                                                       aspectRatioMode=Qt.KeepAspectRatio))
            elif objName == '篦冷机':
                self.blj = QPixmap(filepath)
                self.lab_blj.setPixmap(self.blj.scaled(231 * self.ratio_width, 50 * self.ratio_height,
                                                       aspectRatioMode=Qt.KeepAspectRatio))
            elif objName == '窑':
                self.yao = QPixmap(filepath)
                self.lab_yao.setPixmap(self.yao.scaled(231 * self.ratio_width, 50 * self.ratio_height,
                                                       aspectRatioMode=Qt.KeepAspectRatio))
            elif objName == '分解炉':
                self.fjl = QPixmap(filepath)
                self.lab_fjl.setPixmap(self.fjl.scaled(231 * self.ratio_width, 50 * self.ratio_height,
                                                       aspectRatioMode=Qt.KeepAspectRatio))
            elif objName == '分解炉--窑':
                self.fjl_yao = QPixmap(filepath)
                self.lab_fjl_yao.setPixmap(self.fjl_yao.scaled(231 * self.ratio_width, 50 * self.ratio_height,
                                                               aspectRatioMode=Qt.KeepAspectRatio))


class MyLoginDlg(QDialog):
    login_signal = pyqtSignal(str, str)

    def __init__(self):
        super(MyLoginDlg, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768
        self.setFixedSize(400 * ratio_width, 300 * ratio_height)
        self.setWindowTitle('Login')
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(
            QtCore.QRect(-60 * ratio_width, 240 * ratio_height, 341 * ratio_width, 32 * ratio_height))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        # self.buttonBox.setObjectName("buttonBox")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(80 * ratio_width, 90 * ratio_height, 260 * ratio_width, 81 * ratio_height))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_username = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_username.setFixedWidth(60 * ratio_width)
        self.horizontalLayout.addWidget(self.label_username)
        self.Edt_username = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.Edt_username.setFocus()
        self.Edt_username.setFixedWidth(90 * ratio_width)
        self.horizontalLayout.addWidget(self.Edt_username)
        self.registBtn = QPushButton()
        self.registBtn.setText('注册用户')
        self.registBtn.setFixedWidth(80 * ratio_width)
        self.horizontalLayout.addWidget(self.registBtn)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(80 * ratio_width, 140 * ratio_height, 170 * ratio_width, 81 * ratio_height))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_pwd = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_pwd.setFixedWidth(60 * ratio_width)
        self.horizontalLayout_2.addWidget(self.label_pwd)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setFixedWidth(90 * ratio_width)
        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.label_brand = QtWidgets.QLabel(self)  # 商标
        self.label_brand.setGeometry(
            QtCore.QRect(80 * ratio_width, 20 * ratio_height, 231 * ratio_width, 50 * ratio_height))
        self.label_brand.setPixmap(QPixmap('picture\\logo.png').scaled(231 * ratio_width, 50 * ratio_height,
                                                                       aspectRatioMode=Qt.KeepAspectRatio))

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.registBtn.clicked.connect(self.registe)
        self.label_username.setText("用户名：")
        self.label_pwd.setText("密码：  ")
        self.Edt_username.setText('moujun')
        self.lineEdit_2.setText('123456')

    def registe(self):
        print('123')

    def accept(self):
        self.login_signal.emit(self.Edt_username.text(), self.lineEdit_2.text())

    def reject(self):
        qApp.quit()


class MyDeviceDlg(QDialog):  # 初始化设备参数窗口
    yao_par_signal = pyqtSignal(int, str)

    def __init__(self):
        super(MyDeviceDlg, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768
        self.setWindowTitle('配置设备')
        self.resize(400 * ratio_width, 300 * ratio_height)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)  # 禁止窗口最大化
        self.setFixedSize(self.width(), self.height())  # 禁止拉伸窗口
        self.lay_ser = QHBoxLayout()
        self.lay_xft = QHBoxLayout()
        self.lay_main = QVBoxLayout()
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(
            QtCore.QRect(30 * ratio_width, 240 * ratio_height, 341 * ratio_width, 32 * ratio_height))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(
            QtCore.QRect(30 * ratio_width, 20 * ratio_height, 291 * ratio_width, 78 * ratio_height))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle('窑系统类型')

        self.serial_sin = QRadioButton('单系列', self.groupBox)
        self.serial_sin.setGeometry(
            QtCore.QRect(50 * ratio_width, 30 * ratio_height, 106 * ratio_width, 16 * ratio_height))
        self.serial_dou = QRadioButton('双系列', self.groupBox)
        self.serial_dou.setGeometry(
            QtCore.QRect(170 * ratio_width, 30 * ratio_height, 161 * ratio_width, 16 * ratio_height))
        self.serial_dou.setChecked(True)

        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(
            QtCore.QRect(30 * ratio_width, 110 * ratio_height, 291 * ratio_width, 101 * ratio_height))
        self.groupBox_2.setTitle('旋风筒参数')
        self.xft_num = QtWidgets.QComboBox(self.groupBox_2)
        self.xft_num.setGeometry(
            QtCore.QRect(150 * ratio_width, 40 * ratio_height, 69 * ratio_width, 22 * ratio_height))
        self.xft_num.setObjectName("comboBox")
        self.label_xft = QLabel('旋风筒个数', self.groupBox_2)
        self.label_xft.setGeometry(
            QtCore.QRect(63 * ratio_width, 42 * ratio_height, 61 * ratio_width, 20 * ratio_height))
        self.num = ['2', '3', '4', '5', '6', '7', '8', '9']
        for i in self.num:
            self.xft_num.addItem(i)
        self.xft_num.setCurrentIndex(3)
        self.buttonBox.accepted.connect(self.Accept)
        self.buttonBox.rejected.connect(self.Reject)

        self.setModal(True)

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


class MyDataInputWnd(QMainWindow):  # 数据输入功能窗口
    def __init__(self):
        super(MyDataInputWnd, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768
        self.setObjectName("数据输入")
        self.BtnAddData = QPushButton('录入一行', self)
        self.BtnOk = QPushButton('确认', self)
        self.BtnCancle = QPushButton('取消', self)
        self.BtnAddData.clicked.connect(self.addRowData)
        self.BtnOk.clicked.connect(self.accept)
        self.BtnCancle.clicked.connect(self.reject)
        self.Btn_layout = QHBoxLayout()
        self.Btn_layout.addWidget(self.BtnAddData)
        self.Btn_layout.addWidget(self.BtnOk)
        self.Btn_layout.addWidget(self.BtnCancle)
        self.Btn_layout.setGeometry(QtCore.QRect(width * 0.7, height * 0.85, 341 * ratio_width, 32 * ratio_height))
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(0, height * 0.73, width * ratio_width, 16 * ratio_height))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(width * 0.01, height * 0.04, width * 0.98, height * 0.69))
        self.tableWidget.setObjectName("dataInputWidget")
        '''
        day = str(con.getValue_day())
        hour = str(con.getValue_hour())
        print(123)
        '''
        date = get_time_now()
        day = date[:8]
        hour = date[8:]
        value, name = get_by_fragment()
        self.col_num = len(value[0]) - 3
        self.row_num = len(value)
        self.tableWidget.setColumnCount(self.col_num)
        self.tableWidget.setRowCount(len(value) + 1)
        col_label = []
        for i in range(self.col_num):
            col_label.append(get_chinese(name[i]))
        self.new_data = []

        self.tableWidget.setHorizontalHeaderLabels(col_label)
        for i in range(len(value)):
            for j in range(self.col_num):
                newItem = QTableWidgetItem((str(value[i][j])))
                self.tableWidget.setItem(i, j, newItem)
                self.tableWidget.item(i, j).setFlags(Qt.ItemIsEnabled)
                self.tableWidget.item(i, j).setToolTip(str(value[i][j]))

        newItem = QTableWidgetItem(str(day))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, newItem)
        self.tableWidget.item(self.tableWidget.rowCount() - 1, 0).setToolTip(str(day))
        newItem = QTableWidgetItem(str(hour))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, newItem)
        self.tableWidget.item(self.tableWidget.rowCount() - 1, 1).setToolTip(str(hour))

        '''date = int(self.tableWidget.item(self.row_num - 1, 0).text())
        hour = int(self.tableWidget.item(self.row_num - 1, 1).text())

        if hour < 24:
            newItem = QTableWidgetItem(str(day))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, newItem)
            newItem = QTableWidgetItem(str(hour + 1))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, newItem)

        else:
            newItem = QTableWidgetItem(str(date + 1))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, newItem)
            newItem = QTableWidgetItem(str(0))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, newItem)'''

        self.red = 180
        self.green = 180
        self.blue = 180
        self.tableWidget.item(self.tableWidget.rowCount() - 1, 0).setBackground(
            QBrush(QColor(self.red, self.green, self.blue)))
        self.tableWidget.item(self.tableWidget.rowCount() - 1, 1).setBackground(
            QBrush(QColor(self.red, self.green, self.blue)))
        for i in arange(2, self.col_num):
            newItem = QTableWidgetItem('')
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, i, newItem)
            self.tableWidget.item(self.tableWidget.rowCount() - 1, i).setBackground(
                QBrush(QColor(self.red, self.green, self.blue)))
        self.tableWidget.scrollToBottom()
        self.tableWidget.itemDoubleClicked[QTableWidgetItem].connect(self.tableItemDoubleClicked)
        self.showMaximized()

    def delFirstRow(self):  # 删除第一行
        self.tableWidget.removeRow(0)

    def addRow(self):  # 在最后一行的下面新增一行
        self.tableWidget.insertRow(self.tableWidget.rowCount())

    # 以上两个函数是为了实现保持行数不变

    def addRowData(self):
        self.delFirstRow()
        new_row = []
        for col in range(2):
            item = self.tableWidget.item(self.tableWidget.rowCount() - 1, col)
            item.setBackground(QBrush(QColor(255, 255, 255)))
            try:
                new_row.append(int(item.text()))
            except Exception:
                new_row.append(None)
        for col in range(2, self.tableWidget.columnCount()):
            item = self.tableWidget.item(self.tableWidget.rowCount() - 1, col)
            item.setBackground(QBrush(QColor(255, 255, 255)))
            try:
                new_row.append(float(item.text()))
            except Exception:
                new_row.append(None)
                self.tableWidget.setItem(self.row_num - 1, col, QTableWidgetItem(''))  # 单元格为None无法设置不可编辑
            self.tableWidget.item(self.row_num - 1, col).setFlags(Qt.ItemIsEnabled)

        self.addRow()

        date = int(self.tableWidget.item(self.row_num - 1, 0).text())
        hour = int(self.tableWidget.item(self.row_num - 1, 1).text())

        if hour < 23:
            newItem = QTableWidgetItem(str(date))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, newItem)
            self.tableWidget.item(self.tableWidget.rowCount() - 1, 0).setToolTip(str(date))
            newItem = QTableWidgetItem(str(hour + 1))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, newItem)
            self.tableWidget.item(self.tableWidget.rowCount() - 1, 1).setToolTip(str(hour + 1))
        else:
            newItem = QTableWidgetItem(str(date + 1))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, newItem)
            self.tableWidget.item(self.tableWidget.rowCount() - 1, 0).setToolTip(str(date + 1))
            newItem = QTableWidgetItem(str(0))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, newItem)
            self.tableWidget.item(self.tableWidget.rowCount() - 1, 1).setToolTip(str(0))

        self.tableWidget.item(self.tableWidget.rowCount() - 1, 0).setBackground(
            QBrush(QColor(self.red, self.green, self.blue)))
        self.tableWidget.item(self.tableWidget.rowCount() - 1, 1).setBackground(
            QBrush(QColor(self.red, self.green, self.blue)))
        for i in arange(2, self.col_num):
            newItem = QTableWidgetItem('')
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, i, newItem)
            self.tableWidget.item(self.tableWidget.rowCount() - 1, i).setBackground(
                QBrush(QColor(self.red, self.green, self.blue)))
        self.new_data.append(new_row)

    def accept(self):
        self.addRowData()
        operation = '数据输入:'
        for x in self.new_data:
            operation = operation + str(x[0]) + ',' + str(x[1]) + ';'
        if operation_record([con.getValue_username(), operation]) and save_data(self.new_data):
            reply = QMessageBox.information(self, '提示', '最新数据已经导入，是否自动生成生产预警', QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.warningDlg = MyProduceWarWnd(con.getValue_day(), con.getValue_hour(), 1)
                self.close()
            else:
                self.close()
        else:
            QMessageBox.information(self, '提示', '上传失败', QMessageBox.Yes)

    def reject(self):
        reply = QMessageBox.information(self, '提示', '确认放弃上传？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:

            self.close()
        else:
            pass

    def tableItemDoubleClicked(self):
        if self.tableWidget.currentRow() == self.tableWidget.rowCount() - 1:
            new_row = []
            for col in range(2):
                item = self.tableWidget.item(self.tableWidget.rowCount() - 1, col)
                try:
                    new_row.append(int(item.text()))
                except Exception:
                    new_row.append(None)
            for col in range(2, self.tableWidget.columnCount()):
                item = self.tableWidget.item(self.tableWidget.rowCount() - 1, col)
                try:
                    new_row.append(float(item.text()))
                except Exception:
                    new_row.append(None)
            self.rowdataDlg = MyRowdataInput(new_row)
            self.rowdataDlg.row_data_signal.connect(self.updateRowData)

    def updateRowData(self, value):
        for i in range(len(value)):
            newItem = QTableWidgetItem(value[i])
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, i, newItem)
            self.tableWidget.item(self.tableWidget.rowCount() - 1, i).setBackground(
                QBrush(QColor(self.red, self.green, self.blue)))


class MyRowdataInput(QDialog):  # 双击单元格时弹出来的对话框
    row_data_signal = pyqtSignal(list)

    def __init__(self, row_data):
        super(MyRowdataInput, self).__init__()
        # print(row_data)#上一行的单元格数据
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768
        self.setFixedSize(260 * ratio_width, 330 * ratio_height)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(
            QtCore.QRect(90 * ratio_width, 280 * ratio_height, 75 * ratio_width, 23 * ratio_height))
        self.pushButton.setObjectName("pushButton")

        self.name = get_table_name()
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(
            QtCore.QRect(20 * ratio_width, 50 * ratio_height, 211 * ratio_width, 211 * ratio_height))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(self.name) - 3)
        self.tableWidget.setHorizontalHeaderLabels(['名称', '输入值'])
        for i in range(len(self.name) - 3):
            newItem = QTableWidgetItem(get_chinese(str(self.name[i])))
            self.tableWidget.setItem(i, 0, newItem)
            self.tableWidget.item(i, 0).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            self.tableWidget.item(i, 0).setToolTip(str(self.name[i]))
            if row_data[i] == None:
                newItem = QTableWidgetItem('')
            else:
                newItem = QTableWidgetItem(str(row_data[i]))
            self.tableWidget.setItem(i, 1, newItem)
        # self.tableWidget.horizontalHeader().setDefaultSectionSize(80)  # 列宽
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.label = QtWidgets.QLabel(self)
        self.label.move(20 * ratio_width, 10 * ratio_height)
        self.setWindowTitle("单行数据输入")
        self.pushButton.setText("OK")
        self.label.setText("单行数据输入")
        self.label.setFont(QFont("Roman times", 15, QFont.Bold))
        self.pushButton.clicked.connect(self.Accept)

        self.setModal(True)
        self.show()

    def Accept(self):

        try:
            value = []
            flag = True  # 如果数据都合法，则传数据给下一层，否则提示
            for i in range(len(self.name) - 3):
                if self.tableWidget.item(i, 1) == None:
                    value.append('')
                elif self.tableWidget.item(i, 1).text() == '':
                    value.append('')
                elif re.compile(r'^[-+]?[0-9]+\.?[0-9]*$').match(self.tableWidget.item(i, 1).text()):
                    value.append(self.tableWidget.item(i, 1).text())
                else:
                    # print(i)
                    flag = False
            if flag:
                self.row_data_signal.emit(value)
                self.close()
            else:
                QMessageBox.information(self, '提示', '有数据包含非法字符,请修改', QMessageBox.Yes)
        except Exception:
            QMessageBox.information(self, '提示', '程序出错', QMessageBox.Yes)


class MyDataReviseWnd(QMainWindow):  # 数据修改功能窗口
    def __init__(self):
        super(MyDataReviseWnd, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
        ratio_width = width / 1366
        ratio_height = height / 768
        self.revise_flag = 0  # 数据修改标志
        self.setObjectName("数据修改")
        self.BtnOk = QPushButton('确认', self)
        self.BtnCancle = QPushButton('取消', self)
        self.BtnOk.clicked.connect(self.accept)
        self.BtnCancle.clicked.connect(self.reject)
        self.Btn_layout = QHBoxLayout()
        self.Btn_layout.addWidget(self.BtnOk)
        self.Btn_layout.addWidget(self.BtnCancle)

        self.Btndelete = QPushButton('删除选中行数据', self)
        self.Btndelete.clicked.connect(self.Delete)
        self.Btn_layout.addWidget(self.Btndelete)

        self.Btn_layout.setGeometry(QtCore.QRect(width * 0.7, height * 0.85, 341 * ratio_width, 32 * ratio_height))

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(0, height * 0.73, width, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(width * 0.01, height * 0.04, width * 0.98, height * 0.69))
        self.tableWidget.setObjectName("dataShowWidget")

        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        value, name = get_by_fragment()

        self.col_num = len(value[0]) - 3  # 最后三列不要
        self.row_num = len(value)
        self.tableWidget.setColumnCount(self.col_num)
        self.tableWidget.setRowCount(len(value))
        col_label = []

        for i in range(self.col_num):
            col_label.append(name[i])

        self.new_data = []  # 修改过的数据
        self.row_changed = []  # 修改过的数据的行下标

        self.tableWidget.setHorizontalHeaderLabels(col_label)
        for i in range(len(value)):
            for j in range(2):
                newItem = QTableWidgetItem(str(value[i][j]))
                self.tableWidget.setItem(i, j, newItem)
                self.tableWidget.item(i, j).setToolTip(str(value[i][j]))
                self.tableWidget.item(i, j).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)  # 不可双击编辑但可单击选中

            for j in range(2, self.col_num):
                newItem = QTableWidgetItem(str(value[i][j]))
                self.tableWidget.setItem(i, j, newItem)
                self.tableWidget.item(i, j).setToolTip(str(value[i][j]))

        self.tableWidget.itemChanged[QTableWidgetItem].connect(self.tableItemChanged)  # 编辑单元格后字体会显示红色
        self.tableWidget.scrollToBottom()
        self.showMaximized()

    def tableItemChanged(self):
        self.revise_flag = 1
        self.tableWidget.currentItem().setForeground(QBrush(QColor(255, 0, 0)))
        self.row_changed.append(self.tableWidget.currentRow())

    def Delete(self):
        selected = self.tableWidget.selectedItems()
        Rows = set()
        for item in selected:
            Rows.add(item.row())
        # print(Rows)
        rows = list(Rows)
        rows.sort()
        # print(rows)
        reply = QMessageBox.information(self, '提示', '是否确认删除%d条数据' % len(rows), QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            rows_data = []
            for row in rows:
                row_data = []
                for col in range(2):
                    item = self.tableWidget.item(row, col)
                    print(item.text())
                    row_data.append(str(item.text()))
                rows_data.append(row_data)
            operation = '删除数据:'
            for x in rows_data:
                operation = operation + x[0] + ',' + x[1] + ';'
            if operation_record([con.getValue_username(), operation]):
                try:
                    delete_data(rows_data)
                    for i in rows:
                        self.tableWidget.removeRow(i)
                    reply = QMessageBox.information(self, '提示', '删除成功，是否继续操作?', QMessageBox.Yes | QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        pass
                    else:
                        self.close()
                except Exception:
                    QMessageBox.information(self, '提示', '删除失败', QMessageBox.Yes)
            else:
                QMessageBox.information(self, '提示', '删除失败', QMessageBox.Yes)
        else:
            pass

    def accept(self):
        reply = QMessageBox.information(self, '提示', '是否确认保存修改', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.save()

    def reject(self):
        reply = QMessageBox.information(self, '提示', '确认放弃修改？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.revise_flag = 0
            self.close()
        else:
            pass

    def save(self):
        for row in list(set(self.row_changed)):
            row_data = []
            for col in range(2):
                item = self.tableWidget.item(row, col)
                try:
                    row_data.append(int(item.text()))
                except Exception:
                    row_data.append('')
            for col in arange(2, self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                try:
                    row_data.append(float(item.text()))
                except Exception:
                    row_data.append(None)
            self.new_data.append(row_data)
        operation = '数据修改:'
        for x in self.new_data:
            operation = operation + str(x[0]) + ',' + str(x[1]) + ';'
        if operation_record([con.getValue_username(), operation]):
            try:
                update_data(self.new_data)
                reply = QMessageBox.information(self, '提示', '修改成功', QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    self.revise_flag = 0
                    self.close()
            except Exception:
                QMessageBox.information(self, '提示', '修改失败', QMessageBox.Yes)
        else:
            QMessageBox.information(self, '提示', '修改失败', QMessageBox.Yes)

    def closeEvent(self, *args, **kwargs):
        if self.revise_flag == 1:
            reply = QMessageBox.information(self, '提示', '您尚未保存数据，是否保存修改', QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.revise_flag = 0
                self.save()
            elif reply == QMessageBox.No:
                self.revise_flag = 0
                self.close()
        else:
            self.close()


class MyProduceSimWnd(QMainWindow):
    def __init__(self, day, hour):
        super(MyProduceSimWnd, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        self.Width = metric.width()
        self.Height = metric.height()
        self.setWindowTitle('生产预警')
        self.ratio_w = 0.6
        self.ratio_h = 0.78

        self.output, self.real = production_warning(str(day), str(hour))
        data, self.name = get_by_fragment2(str(day) + str(hour), 5)
        time = ['']
        for element in data:
            time.append(element[0][4:6] + '/' + element[0][6:] + ' ' + element[1])
        data = get_by_hour(str(day) + str(hour))

        left = -9  # 为了使窗口能够位于左上角
        self.move(left, 0)
        self.setFixedSize(self.Width, self.Height - 72 * self.Height / 768)  # 72为win10任务栏高度

        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        self.scroll = QScrollArea()
        self.filler = QWidget()
        self.fillLay = QGridLayout()
        self.filler.setFixedWidth(self.Width - 40)  # 为了不让水平方向上出现滚轮，需要固定填充控件的宽度不超过分辨率的宽度

        list_time = ['20170220-11', '20170220-12']
        list_table = ['窑头压力']
        list_model = ['SVM-ADaboost', 'RNN', 'RNN-LSTM', 'NN']

        self.time_box = QComboBox(self.filler)
        self.time_box.setObjectName('time_box')
        self.time_box.activated.connect(self.timeEvent)
        self.time_box.addItem('请选择时间点')
        for item in list_time:
            self.time_box.addItem(item)
        self.fillLay.addWidget(self.time_box, 0, 0)

        self.model_box = QComboBox(self.filler)
        self.model_box.setObjectName('model_box')
        self.model_box.activated.connect(self.modelEvent)
        self.model_box.addItem('请选择模型')
        for item in list_model:
            self.model_box.addItem(item)
        self.fillLay.addWidget(self.model_box, 0, 1)



        tableVCombox = QWidget(self.filler)
        tableVComLay = QVBoxLayout()
        tableVCombox.setLayout(tableVComLay)
        tableHWidget = QWidget(self.filler)
        tableHLay = QHBoxLayout()
        tableHWidget.setLayout(tableHLay)

        self.table_box = QComboBox(self.filler)
        self.table_box.setObjectName('table_box')
        self.table_box.activated.connect(self.tableEvent)
        self.table_box.addItem('请选择')
        for item in list_table:
            self.table_box.addItem(item)
        tableVComLay.addWidget(self.table_box)

        limit_min = 0.6
        limit_max = 0.9
        self.limit_lab = QLabel('(' + str(limit_min) + ' ～ ' + str(limit_max) + ')')
        self.limit_lab.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.limit_lab.setFont(QFont('Timers', 10, QFont.Times))
        tableVComLay.addWidget(self.limit_lab)
        tableHLay.addWidget(tableVCombox)#为了居中显示，外面嵌套一层水平布局
        self.fillLay.addWidget(tableHWidget, 1, 0,2,1)

        percentWidget = QWidget(self.filler)#标签控件应与值控件分开布局,为了以后替换方便
        percentWidget.setObjectName('percentWidget')
        # percentWidget.setStyleSheet('border:1px solid red;')
        percentWidget.setFixedHeight(self.model_box.height()*2)
        percentLay = QHBoxLayout()
        percentWidget.setLayout(percentLay)
        startValueLab = QLabel('初始值')
        startValueLab.setFont(QFont('Timers', 10, QFont.Times))
        controlValueLab = QLabel('调控值')
        controlValueLab.setFont(QFont('Timers', 10, QFont.Times))
        percentLay.addWidget(startValueLab)
        percentLay.addWidget(controlValueLab)
        self.percentEdt = QLineEdit(self.filler)
        self.percentEdt.setObjectName('percentEdt')
        self.percentEdt.setText('99')
        self.percentEdt.setValidator(QRegExpValidator(QRegExp("^(([1-9]{1}\\d*)|([0]{1}))(\\.(\\d){0,2})?$")))
        # self.percentEdt.textChanged.connect(self.percentEvent)
        self.percentEdt.returnPressed.connect(self.percentEvent)
        percentLay.addWidget(self.percentEdt)
        baifenhao = QLabel('%')
        baifenhao.setFont(QFont('Timers', 10, QFont.Times))
        percentLay.addWidget(baifenhao)
        self.fillLay.addWidget(percentWidget,1,1,1,3)

        valueWidget = QWidget(self.filler)
        valueWidget.setObjectName('valueWidget')
        # valueWidget.setStyleSheet('border:1px solid red;')
        valueLay = QGridLayout()
        valueWidget.setLayout(valueLay)
        startValue = {}
        controlValue = {}
        for i in range(8):
            startValue[i] = QLabel(str(i))
            startValue[i].setFont(QFont('Timers', 12, QFont.Times))
            startValue[i].setAlignment(Qt.AlignHCenter|Qt.AlignTop)
            controlValue[i] = QLabel(str(i + 1))
            controlValue[i].setFont(QFont('Timers', 12, QFont.Times))
            controlValue[i].setAlignment(Qt.AlignHCenter|Qt.AlignTop)
            valueLay.addWidget(startValue[i], i, 0)
            valueLay.addWidget(controlValue[i], i, 1)
        self.fillLay.addWidget(valueWidget, 2, 1)

        self.line0 = QtWidgets.QFrame(self)
        self.line0.setGeometry(QtCore.QRect(self.Width * 0.5, 0, 16, self.Height))
        self.line0.setFrameShape(QtWidgets.QFrame.VLine)
        self.line0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fillLay.addWidget(self.line0, 0, 4, 3, 1)

        yaotouWidget = QWidget(self.filler)
        yaotouWidget.setObjectName('yaotouWidget')
        yaotouLay = QGridLayout()
        yaotouWidget.setLayout(yaotouLay)
        yaotouLab = QLabel('窑头秤')
        yaotouLab.setFont(QFont('Timers', 15, QFont.Times))
        yaotouLab.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        yaotouStartLab = QLabel('初始值')
        yaotouStartLab.setFont(QFont('Timers', 10, QFont.Times))
        yaotouControlLab = QLabel('调控值')
        yaotouControlLab.setFont(QFont('Timers', 10, QFont.Times))
        yaotouPercent = QLabel('变化幅度')
        yaotouPercent.setFont(QFont('Timers', 10, QFont.Times))
        yaotouLay.addWidget(yaotouLab, 0, 0, 1, 3)
        yaotouLay.addWidget(yaotouStartLab, 1, 0)
        yaotouLay.addWidget(yaotouControlLab, 1, 1)
        yaotouLay.addWidget(yaotouPercent, 1, 2)
        self.yaotouStartValue = {}
        self.yaotouControlValue = {}
        self.yaotouChangePercent = {}
        for i in range(8):
            self.yaotouStartValue[i] = QLabel(str(i))
            self.yaotouStartValue[i].setFont(QFont('Timers', 12, QFont.Times))
            self.yaotouStartValue[i].setAlignment(Qt.AlignCenter)
            self.yaotouControlValue[i] = QLabel(str(i + 1))
            self.yaotouControlValue[i].setFont(QFont('Timers', 12, QFont.Times))
            self.yaotouControlValue[i].setAlignment(Qt.AlignCenter)
            self.yaotouChangePercent[i] = QLabel('↑↓' + str(i + 2))
            self.yaotouChangePercent[i].setFont(QFont('Timers', 12, QFont.Times))
            self.yaotouChangePercent[i].setAlignment(Qt.AlignCenter)
            yaotouLay.addWidget(self.yaotouStartValue[i], i + 2, 0)
            yaotouLay.addWidget(self.yaotouControlValue[i], i + 2, 1)
            yaotouLay.addWidget(self.yaotouChangePercent[i], i + 2, 2)
        self.fillLay.addWidget(yaotouWidget, 0, 5, 3, 3)

        self.line1 = QtWidgets.QFrame(self)
        self.line1.setGeometry(QtCore.QRect(self.Width * 0.5, 0, 16, self.Height))
        self.line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fillLay.addWidget(self.line1, 0, 8, 3, 1)

        yaoweiWidget = QWidget(self.filler)
        yaoweiWidget.setObjectName('yaoweiWidget')
        yaoweiLay = QGridLayout()
        yaoweiWidget.setLayout(yaoweiLay)
        yaoweiLab = QLabel('窑尾秤')
        yaoweiLab.setFont(QFont('Timers', 15, QFont.Times))
        yaoweiLab.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        yaoweiStartLab = QLabel('初始值')
        yaoweiStartLab.setFont(QFont('Timers', 10, QFont.Times))
        yaoweiControlLab = QLabel('调控值')
        yaoweiControlLab.setFont(QFont('Timers', 10, QFont.Times))
        yaoweiPercent = QLabel('变化幅度')
        yaoweiPercent.setFont(QFont('Timers', 10, QFont.Times))
        yaoweiLay.addWidget(yaoweiLab, 0, 0, 1, 3)
        yaoweiLay.addWidget(yaoweiStartLab, 1, 0)
        yaoweiLay.addWidget(yaoweiControlLab, 1, 1)
        yaoweiLay.addWidget(yaoweiPercent, 1, 2)
        self.yaoweiStartValue = {}
        self.yaoweiControlValue = {}
        self.yaoweiChangePercent = {}
        for i in range(8):
            self.yaoweiStartValue[i] = QLabel(str(i))
            self.yaoweiStartValue[i].setFont(QFont('Timers', 12, QFont.Times))
            self.yaoweiStartValue[i].setAlignment(Qt.AlignCenter)
            self.yaoweiControlValue[i] = QLabel(str(i + 1))
            self.yaoweiControlValue[i].setFont(QFont('Timers', 12, QFont.Times))
            self.yaoweiControlValue[i].setAlignment(Qt.AlignCenter)
            self.yaoweiChangePercent[i] = QLabel('↑↓' + str(i + 2))
            self.yaoweiChangePercent[i].setFont(QFont('Timers', 12, QFont.Times))
            self.yaoweiChangePercent[i].setAlignment(Qt.AlignCenter)
            yaoweiLay.addWidget(self.yaoweiStartValue[i], i + 2, 0)
            yaoweiLay.addWidget(self.yaoweiControlValue[i], i + 2, 1)
            yaoweiLay.addWidget(self.yaoweiChangePercent[i], i + 2, 2)
        # self.fillLay.addWidget(yaoweiLab, 1, 10)
        self.fillLay.addWidget(yaoweiWidget, 0, 9, 3, 3)

        self.line2 = QtWidgets.QFrame(self)
        self.line2.setGeometry(QtCore.QRect(self.Width * 0.5, 0, 16, self.Height))
        self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fillLay.addWidget(self.line2, 0, 12, 3, 1)

        rehaoWidget = QWidget(self.filler)
        rehaoWidget.setObjectName('rehaoWidget')
        rehaoLay = QVBoxLayout()
        rehaoWidget.setLayout(rehaoLay)
        rehaoLab = QLabel('热耗')
        rehaoLab.setFont(QFont('Timers', 15, QFont.Times))
        rehaoLab.setAlignment(Qt.AlignCenter)
        rehaoLay.addWidget(rehaoLab)
        rehaoValueLab = {}
        for i in range(8):
            rehaoValueLab[i] = QLabel(str(i))
            rehaoValueLab[i].setFont(QFont('Timers', 12, QFont.Times))
            rehaoValueLab[i].setAlignment(Qt.AlignCenter)
            rehaoLay.addWidget(rehaoValueLab[i])
        self.fillLay.addWidget(rehaoWidget, 0, 13, 3, 1)

        self.line3 = QtWidgets.QFrame(self)
        self.line3.setGeometry(QtCore.QRect(self.Width * 0.5, 0, 16, self.Height))
        self.line3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fillLay.addWidget(self.line3, 0, 14, 3, 1)

        Ca_Widget = QWidget(self.filler)
        Ca_Widget.setObjectName('CaWidget')
        Ca_VLayout = QVBoxLayout()
        Ca_Widget.setLayout(Ca_VLayout)

        try:
            # value = self.output['youlig']['youlig']
            old = []
            new = []
            Ca = MyCaLineGraph(old, new, time)
            fangcha = QLabel('方差同比缩小：--%')
            fangcha.setFont(QFont('Timers', 12, QFont.Times))
            fangcha.setAlignment(Qt.AlignCenter)
            yuanhegelv = QLabel('原始合格率：--%')
            yuanhegelv.setFont(QFont('Timers', 12, QFont.Times))
            yuanhegelv.setAlignment(Qt.AlignCenter)
            houhegelv = QLabel('调控后合格率：--%')
            houhegelv.setFont(QFont('Timers', 12, QFont.Times))
            houhegelv.setAlignment(Qt.AlignCenter)
            Ca_VLayout.addWidget(Ca)
            Ca_VLayout.addWidget(fangcha)
            Ca_VLayout.addWidget(yuanhegelv)
            Ca_VLayout.addWidget(houhegelv)
            self.fillLay.addWidget(Ca_Widget, 0, 15, 3, 1)
        except Exception:
            QMessageBox.information(self, '提示', '游离钙数据出错', QMessageBox.Yes)

        # self.line4 = QtWidgets.QFrame(self)
        # self.line4.setGeometry(QtCore.QRect(self.Width * 0.5, 0, 16, self.Height))
        # self.line4.setFrameShape(QtWidgets.QFrame.VLine)
        # self.line4.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.fillLay.addWidget(self.line4, 0, 18, 2, 1)

        self.line4 = QtWidgets.QFrame(self)
        self.line4.setGeometry(QtCore.QRect(self.Width * 0.5, 0, 16, self.Height))
        self.line4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fillLay.addWidget(self.line4, 3, 0, 1, 20)

        ThreeValueWidget = QWidget(self.filler)
        ThreeValueWidget.setObjectName('ThreeValueWidget')
        ThreeValueHLayout = QHBoxLayout()
        ThreeValueWidget.setLayout(ThreeValueHLayout)
        KHVWidget = QWidget()
        KHVLay = QVBoxLayout()
        KHVWidget.setLayout(KHVLay)
        SMVWidget = QWidget()
        SMVLay = QVBoxLayout()
        SMVWidget.setLayout(SMVLay)
        IMVWidget = QWidget()
        IMVLay = QVBoxLayout()
        IMVWidget.setLayout(IMVLay)

        try:
            # value = self.output['youlig']['youlig']
            old = []
            new = []
            KH = MyThreeValueLineGraph(old, new, time, 0)
            SM = MyThreeValueLineGraph(old, new, time, 1)
            IM = MyThreeValueLineGraph(old, new, time, 2)
            KH_Label1 = QLabel('方差同比缩小：--%')
            KH_Label1.setFont(QFont('Timers', 12, QFont.Times))
            KH_Label1.setAlignment(Qt.AlignCenter)
            KH_Label2 = QLabel('原始合格率：--%')
            KH_Label2.setFont(QFont('Timers', 12, QFont.Times))
            KH_Label2.setAlignment(Qt.AlignCenter)
            KH_Label3 = QLabel('调控后合格率：--%')
            KH_Label3.setFont(QFont('Timers', 12, QFont.Times))
            KH_Label3.setAlignment(Qt.AlignCenter)
            SM_Label1 = QLabel('方差同比缩小：--%')
            SM_Label1.setFont(QFont('Timers', 12, QFont.Times))
            SM_Label1.setAlignment(Qt.AlignCenter)
            SM_Label2 = QLabel('原始合格率：--%')
            SM_Label2.setFont(QFont('Timers', 12, QFont.Times))
            SM_Label2.setAlignment(Qt.AlignCenter)
            SM_Label3 = QLabel('调控后合格率：--%')
            SM_Label3.setFont(QFont('Timers', 12, QFont.Times))
            SM_Label3.setAlignment(Qt.AlignCenter)
            IM_Label1 = QLabel('方差同比缩小：--%')
            IM_Label1.setFont(QFont('Timers', 12, QFont.Times))
            IM_Label1.setAlignment(Qt.AlignCenter)
            IM_Label2 = QLabel('原始合格率：--%')
            IM_Label2.setFont(QFont('Timers', 12, QFont.Times))
            IM_Label2.setAlignment(Qt.AlignCenter)
            IM_Label3 = QLabel('调控后合格率：--%')
            IM_Label3.setFont(QFont('Timers', 12, QFont.Times))
            IM_Label3.setAlignment(Qt.AlignCenter)
            KHVLay.addWidget(KH)
            KHVLay.addWidget(KH_Label1)
            KHVLay.addWidget(KH_Label2)
            KHVLay.addWidget(KH_Label3)
            SMVLay.addWidget(SM)
            SMVLay.addWidget(SM_Label1)
            SMVLay.addWidget(SM_Label2)
            SMVLay.addWidget(SM_Label3)
            IMVLay.addWidget(IM)
            IMVLay.addWidget(IM_Label1)
            IMVLay.addWidget(IM_Label2)
            IMVLay.addWidget(IM_Label3)
            ThreeValueHLayout.addWidget(KHVWidget)
            ThreeValueHLayout.addWidget(SMVWidget)
            ThreeValueHLayout.addWidget(IMVWidget)
            ThreeValueWidget.setFixedHeight(self.Height * 0.618)  # 调整三率值的页面高度
            self.fillLay.addWidget(ThreeValueWidget, 4, 0, 2, 16)
        except Exception:
            QMessageBox.information(self, '提示', '三率值数据出错', QMessageBox.Yes)

        self.line5 = QtWidgets.QFrame(self)
        self.line5.setGeometry(QtCore.QRect(self.Width * 0.5, 0, 16, self.Height))
        self.line5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fillLay.addWidget(self.line5, 6, 0, 1, 20)

        yijitong_VWidget = QWidget(self.filler)
        yijitong_VWidget.setObjectName('yijitongWidget')
        yijitong_VLayout = QVBoxLayout()
        yijitong_VWidget.setLayout(yijitong_VLayout)
        yijitong_HWidget = QWidget(self.filler)
        yijitong_HLayout = QHBoxLayout()
        yijitong_HWidget.setLayout(yijitong_HLayout)

        try:
            # value = self.output['yijit']
            old = []
            new = []
            yijitwdA = MyYijitongMplCanvas(old, new, 0, time)
            yijityqA = MyYijitongMplCanvas(old, new, 1, time)
            yijitwdB = MyYijitongMplCanvas(old, new, 2, time)
            yijityqB = MyYijitongMplCanvas(old, new, 3, time)
            # yijitong_title = QLabel('一级筒指标预测')
            # yijitong_title.setAlignment(Qt.AlignLeft)
            # yijitong_VLayout.addWidget(yijitong_title)
            yijitong_HLayout.addWidget(yijitwdA)
            yijitong_HLayout.addWidget(yijityqA)
            yijitong_HLayout.addWidget(yijitwdB)
            yijitong_HLayout.addWidget(yijityqB)
            yijitong_VLayout.addWidget(yijitong_HWidget)
            yijitong_VWidget.setFixedHeight(self.Height * 0.618)  # 调整一级筒数据的页面高度
            self.fillLay.addWidget(yijitong_VWidget, 7, 0, 1, 16)
        except Exception:
            QMessageBox.information(self, '提示', '一级筒指标数据出错', QMessageBox.Yes)

        self.line6 = QtWidgets.QFrame(self)
        self.line6.setGeometry(QtCore.QRect(self.Width * 0.5, 0, 16, self.Height))
        self.line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fillLay.addWidget(self.line6, 8, 0, 1, 20)

        fjlWidget = QWidget(self.filler)
        fjlWidget.setObjectName('fjlWidget')
        fjlHLayout = QHBoxLayout()
        fjlWidget.setLayout(fjlHLayout)

        try:
            # value = self.output['youlig']['youlig']
            old = []
            new = []
            wd = MyFjlLineGraph(old, new, time, 0)
            yq = MyFjlLineGraph(old, new, time, 1)
            Label1 = QLabel('温度：--%')
            Label1.setFont(QFont('Timers', 12, QFont.Times))
            Label1.setAlignment(Qt.AlignCenter)
            Label2 = QLabel('压强--%')
            Label2.setFont(QFont('Timers', 12, QFont.Times))
            Label2.setAlignment(Qt.AlignCenter)
            fjlHLayout.addWidget(wd)
            fjlHLayout.addWidget(Label1)
            fjlHLayout.addWidget(yq)
            fjlHLayout.addWidget(Label2)
            fjlWidget.setFixedHeight(self.Height * 0.618)  # 调整分解炉的页面高度
            self.fillLay.addWidget(fjlWidget, 9, 0, 1, 16)
        except Exception:
            QMessageBox.information(self, '提示', '分解炉数据出错', QMessageBox.Yes)

        self.line7 = QtWidgets.QFrame(self)
        self.line7.setGeometry(QtCore.QRect(self.Width * 0.5, 0, 16, self.Height))
        self.line7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fillLay.addWidget(self.line7, 10, 0, 1, 20)

        # bljHWidget = QWidget(self.filler)
        # bljHWidget
        # bljHLayout = QHBoxLayout()
        # bljHWidget.setLayout(bljHLayout)
        # bljVWidget =QWidget(self.filler)
        # bljVLayout=QVBoxLayout()
        # bljVWidget.setLayout(bljVLayout)
        # bljGraph=QWidget(self.filler)
        # bljGLayout =QGridLayout()
        # bljGraph.setLayout(bljGLayout)
        #
        # try:
        #     value = output['youlig']['youlig']
        #     blj1 = MyBljLineGraph(value, time, 0)
        #     blj2 = MyBljLineGraph(value, time, 0)
        #     blj3 = MyBljLineGraph(value, time, 0)
        #     blj4 = MyBljLineGraph(value, time, 0)
        #     blj5 = MyBljLineGraph(value, time, 0)
        #     blj6 = MyBljLineGraph(value, time, 0)
        #     bljGLayout.addWidget(blj1,0,0)
        #     bljGLayout.addWidget(blj2,0,1)
        #     bljGLayout.addWidget(blj3,0,2)
        #     bljGLayout.addWidget(blj4,1,0)
        #     bljGLayout.addWidget(blj5,1,1)
        #     bljGLayout.addWidget(blj6,1,2)
        #
        #     Label1 = QLabel('温度：--%')
        #     Label1.setFont(QFont('Timers', 12, QFont.Times))
        #     Label1.setAlignment(Qt.AlignCenter)
        #     Label2 = QLabel('压强--%')
        #     Label2.setFont(QFont('Timers', 12, QFont.Times))
        #     Label2.setAlignment(Qt.AlignCenter)
        #     bljVLayout.addWidget(Label1)
        #     bljVLayout.addWidget(Label2)
        #     bljHLayout.addWidget(bljGraph)
        #     bljHLayout.addWidget(bljVWidget)
        #
        #     bljHWidget.setFixedHeight(self.Height*0.618)#调整篦冷机的页面高度
        #     self.fillLay.addWidget(bljHWidget, 10, 0, 1, 16)
        # except Exception:
        #     QMessageBox.information(self, '提示', '分解炉数据出错', QMessageBox.Yes)
        #
        # self.line8 = QtWidgets.QFrame(self)
        # self.line8.setGeometry(QtCore.QRect(self.Width * 0.5, 0, 16, self.Height))
        # self.line8.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line8.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.fillLay.addWidget(self.line8, 11, 0, 1, 20)

        hzyWidget = QWidget(self.filler)
        hzyWidget.setObjectName('hzyWidget')
        hzyHLayout = QHBoxLayout()
        hzyWidget.setLayout(hzyHLayout)

        try:
            # value = self.output['youlig']['youlig']
            old = []
            new = []
            wd = MyHzyLineGraph(old, new, time, 0)
            yq = MyHzyLineGraph(old, new, time, 1)
            Label1 = QLabel('温度：--%')
            Label1.setFont(QFont('Timers', 12, QFont.Times))
            Label1.setAlignment(Qt.AlignCenter)
            Label2 = QLabel('压强--%')
            Label2.setFont(QFont('Timers', 12, QFont.Times))
            Label2.setAlignment(Qt.AlignCenter)
            hzyHLayout.addWidget(wd)
            hzyHLayout.addWidget(Label1)
            hzyHLayout.addWidget(yq)
            hzyHLayout.addWidget(Label2)
            hzyWidget.setFixedHeight(self.Height * 0.618)  # 调整回转窑的页面高度
            self.fillLay.addWidget(hzyWidget, 13, 0, 1, 16)
        except Exception:
            QMessageBox.information(self, '提示', '回转窑数据出错', QMessageBox.Yes)

        # 确定布局
        self.filler.setLayout(self.fillLay)
        ##创建一个滚动条
        # self.filler.setMinimumSize(self.Width * self.ratio_w-48, self.Height+200)  #######设置滚动条区域的尺寸
        self.scroll.setWidget(self.filler)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        self.mainWidget.setLayout(self.vbox)

        # self.statusBar().showMessage("底部信息栏")
        self.show()

    def timeEvent(self):
        if (self.time_box.currentIndex() != 0):
            time = self.time_box.currentText()
            # print(time[:8]+time[9:])
            self.deadline = time[:8] + time[9:]
            print(self.deadline)
            try:
                self.model1 = Model_rehao(self.deadline)
                print(self.deadline)
                # ModelData = self.model1.use_model()
                # print(ModelData)
                print(self.deadline)
                # self.model2 = Model_detection(Model_rehao('2017022011'))
                # Model2Data = self.model2.detection()
                # print(Model2Data)
                print(222)
            except Exception as e:
                QMessageBox.information(self, '提示', '模型数据出错', QMessageBox.Yes)
                print(e)
            table_data, table_name = get_by_fragment2(self.deadline, 8)  # 返回deadline的前8小时
            self.timeLabel = ['']
            print(table_data)
            for element in table_data:
                self.timeLabel.append(element[0][4:6] + '/' + element[0][6:] + ' ' + element[1])
            print(self.timeLabel)
            # print(Model2Data['rehao']['new']['rehao'])
            # self.replaceYaotouWidget(ModelData['old']['yaotouc'], ModelData['new']['yaotouc'])
            # self.replaceYaoweiWidget(ModelData['old']['yaoweic'], ModelData['new']['yaoweic'])
            # self.replaceCaWidget(ModelData['old']['youlig'], ModelData['new']['youlig'], self.timeLabel)
            # self.replaceRehaoWidget(Model2Data['rehao']['new']['rehao'])
            # self.replaceThreeValueWidget(Model2Data['sanlvz']['old'],Model2Data['sanlvz']['new'])
            # self.replaceYijitongWidget(Model2Data['yijit']['old'],Model2Data['yijit']['new'])
            # self.replaceFjlWidget(Model2Data['fenjiel_huizhuany']['old'],Model2Data['fenjiel_huizhuany']['new'])
            # self.replaceHzyWidget(Model2Data['fenjiel_huizhuany']['old'],Model2Data['fenjiel_huizhuany']['new'])

    def modelEvent(self):
        if (self.model_box.currentIndex() != 0):
            pass
        print(self.model_box.currentText())

    def tableEvent(self):
        if (self.table_box.currentIndex() != 0):
            pass
        print(self.table_box.currentText())

    def percentEvent(self):
        if self.time_box.currentIndex() == 0:
            QMessageBox.information(self, '提示', '请先选择时间点', QMessageBox.Yes)
            self.percentEdt.setText('99')
        elif self.percentEdt.text() != None:
            percent = float(self.percentEdt.text()) / 100
            print(percent)
            # self.model1.set_radio(percent)
            # ModelData = self.model1.use_model()
            # print(ModelData)
            # self.replaceYaotouWidget(ModelData['old']['yaotouc'], ModelData['new']['yaotouc'])
            # self.replaceYaoweiWidget(ModelData['old']['yaoweic'], ModelData['new']['yaoweic'])
            # self.replaceCaWidget(ModelData['old']['youlig'], ModelData['new']['youlig'], self.timeLabel)
            old=[100,100,100,100,100,100,100,100]
            new=[x*percent for x in old]
            print(new)
            self.replacePercentWidget(old,new)
        print(self.percentEdt.text())

    def replacePercentWidget(self,old,new):
        valueWidget = QWidget(self.filler)
        valueWidget.setObjectName('valueWidget')
        # valueWidget.setStyleSheet('border:1px solid red;')
        valueLay = QGridLayout()
        valueWidget.setLayout(valueLay)
        startValue = {}
        controlValue = {}
        for i in range(8):
            startValue[i] = QLabel(str(round(old[i],2)))
            startValue[i].setFont(QFont('Timers', 12, QFont.Times))
            startValue[i].setAlignment(Qt.AlignHCenter | Qt.AlignTop)
            controlValue[i] = QLabel(str(round(new[i],2)))
            controlValue[i].setFont(QFont('Timers', 12, QFont.Times))
            controlValue[i].setAlignment(Qt.AlignHCenter | Qt.AlignTop)
            valueLay.addWidget(startValue[i], i, 0)
            valueLay.addWidget(controlValue[i], i, 1)
        oldWidget = self.findChild(QWidget, 'valueWidget')
        if oldWidget != None:
            self.fillLay.removeWidget(oldWidget)
            sip.delete(oldWidget)
        valueWidget.setObjectName('valueWidget')
        self.fillLay.addWidget(valueWidget, 2, 1)

    def replaceYaotouWidget(self, old, new):
        yaotouWidget = QWidget(self.filler)
        yaotouLay = QGridLayout()
        yaotouWidget.setLayout(yaotouLay)
        yaotouLab = QLabel('窑头秤')
        yaotouLab.setFont(QFont('Timers', 15, QFont.Times))
        yaotouLab.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        yaotouStartLab = QLabel('初始值')
        yaotouStartLab.setFont(QFont('Timers', 10, QFont.Times))
        yaotouControlLab = QLabel('调控值')
        yaotouControlLab.setFont(QFont('Timers', 10, QFont.Times))
        yaotouPercent = QLabel('变化幅度')
        yaotouPercent.setFont(QFont('Timers', 10, QFont.Times))
        yaotouLay.addWidget(yaotouLab, 0, 0, 1, 3)
        yaotouLay.addWidget(yaotouStartLab, 1, 0)
        yaotouLay.addWidget(yaotouControlLab, 1, 1)
        yaotouLay.addWidget(yaotouPercent, 1, 2)
        for i in range(8):
            self.yaotouStartValue[i] = QLabel(str(round(old[i], 2)))
            self.yaotouStartValue[i].setFont(QFont('Timers', 12, QFont.Times))
            self.yaotouStartValue[i].setAlignment(Qt.AlignCenter)
            self.yaotouControlValue[i] = QLabel(str(round(new[i], 2)))
            self.yaotouControlValue[i].setFont(QFont('Timers', 12, QFont.Times))
            self.yaotouControlValue[i].setAlignment(Qt.AlignCenter)
            percent = (new[i] - old[i]) / old[i]
            if percent > 0:
                self.yaotouChangePercent[i] = QLabel('↑' + str(round(percent * 100, 2)) + '%')
                self.yaotouChangePercent[i].setFont(QFont('Timers', 12, QFont.Times))
                self.yaotouChangePercent[i].setStyleSheet("QLabel{color:rgb(255,0,0)}")
                self.yaotouChangePercent[i].setAlignment(Qt.AlignCenter)
            else:
                self.yaotouChangePercent[i] = QLabel('↓' + str(round(-percent * 100, 2)) + '%')
                self.yaotouChangePercent[i].setFont(QFont('Timers', 12, QFont.Times))
                self.yaotouChangePercent[i].setStyleSheet("QLabel{color:rgb(0,255,0)}")
                self.yaotouChangePercent[i].setAlignment(Qt.AlignCenter)
            yaotouLay.addWidget(self.yaotouStartValue[i], i + 2, 0)
            yaotouLay.addWidget(self.yaotouControlValue[i], i + 2, 1)
            yaotouLay.addWidget(self.yaotouChangePercent[i], i + 2, 2)

        oldWidget = self.findChild(QWidget, 'yaotouWidget')
        if oldWidget != None:
            self.fillLay.removeWidget(oldWidget)
            sip.delete(oldWidget)
        yaotouWidget.setObjectName('yaotouWidget')
        self.fillLay.addWidget(yaotouWidget, 0, 5, 2, 3)

    def replaceYaoweiWidget(self, old, new):
        yaoweiWidget = QWidget(self.filler)
        yaoweiLay = QGridLayout()
        yaoweiWidget.setLayout(yaoweiLay)
        yaoweiLab = QLabel('窑尾秤')
        yaoweiLab.setFont(QFont('Timers', 15, QFont.Times))
        yaoweiLab.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        yaoweiStartLab = QLabel('初始值')
        yaoweiStartLab.setFont(QFont('Timers', 10, QFont.Times))
        yaoweiControlLab = QLabel('调控值')
        yaoweiControlLab.setFont(QFont('Timers', 10, QFont.Times))
        yaoweiPercent = QLabel('变化幅度')
        yaoweiPercent.setFont(QFont('Timers', 10, QFont.Times))
        yaoweiLay.addWidget(yaoweiLab, 0, 0, 1, 3)
        yaoweiLay.addWidget(yaoweiStartLab, 1, 0)
        yaoweiLay.addWidget(yaoweiControlLab, 1, 1)
        yaoweiLay.addWidget(yaoweiPercent, 1, 2)
        self.yaoweiStartValue = {}
        self.yaoweiControlValue = {}
        self.yaoweiChangePercent = {}
        for i in range(8):
            self.yaoweiStartValue[i] = QLabel(str(round(old[i], 2)))
            self.yaoweiStartValue[i].setFont(QFont('Timers', 12, QFont.Times))
            self.yaoweiStartValue[i].setAlignment(Qt.AlignCenter)
            self.yaoweiControlValue[i] = QLabel(str(round(new[i], 2)))
            self.yaoweiControlValue[i].setFont(QFont('Timers', 12, QFont.Times))
            self.yaoweiControlValue[i].setAlignment(Qt.AlignCenter)
            percent = (new[i] - old[i]) / old[i]
            if percent > 0:
                self.yaoweiChangePercent[i] = QLabel('↑' + str(round(percent * 100, 2)) + '%')
                self.yaoweiChangePercent[i].setFont(QFont('Timers', 12, QFont.Times))
                self.yaoweiChangePercent[i].setStyleSheet("QLabel{color:rgb(255,0,0)}")
                self.yaoweiChangePercent[i].setAlignment(Qt.AlignCenter)
            else:
                self.yaoweiChangePercent[i] = QLabel('↓' + str(round(-percent * 100, 2)) + '%')
                self.yaoweiChangePercent[i].setFont(QFont('Timers', 12, QFont.Times))
                self.yaoweiChangePercent[i].setStyleSheet("QLabel{color:rgb(0,255,0)}")
                self.yaoweiChangePercent[i].setAlignment(Qt.AlignCenter)

            yaoweiLay.addWidget(self.yaoweiStartValue[i], i + 2, 0)
            yaoweiLay.addWidget(self.yaoweiControlValue[i], i + 2, 1)
            yaoweiLay.addWidget(self.yaoweiChangePercent[i], i + 2, 2)

        oldWidget = self.findChild(QWidget, 'yaoweiWidget')
        if oldWidget != None:
            self.fillLay.removeWidget(oldWidget)
            sip.delete(oldWidget)
        yaoweiWidget.setObjectName('yaoweiWidget')
        self.fillLay.addWidget(yaoweiWidget, 0, 9, 2, 3)

    def replaceRehaoWidget(self, newValue):
        rehaoWidget = QWidget(self.filler)
        rehaoLay = QVBoxLayout()
        rehaoWidget.setLayout(rehaoLay)
        rehaoLab = QLabel('热耗')
        rehaoLab.setFont(QFont('Timers', 15, QFont.Times))
        rehaoLab.setAlignment(Qt.AlignCenter)
        rehaoLay.addWidget(rehaoLab)
        print(123)
        for i in range(len(newValue)):
            newValue[i] = round(newValue[i], 2)
        print(newValue)
        rehaoValue = newValue
        rehaoValueLab = {}
        for i in range(8):
            rehaoValueLab[i] = QLabel(str(rehaoValue))
            rehaoValueLab[i].setFont(QFont('Timers', 12, QFont.Times))
            rehaoValueLab[i].setAlignment(Qt.AlignCenter)
            rehaoLay.addWidget(rehaoValueLab[i])

        oldWidget = self.findChild(QWidget, 'rehaoWidget')
        if oldWidget != None:
            self.fillLay.removeWidget(oldWidget)
            sip.delete(oldWidget)
        rehaoWidget.setObjectName('rehaoWidget')
        self.fillLay.addWidget(rehaoWidget, 0, 13, 2, 1)

    def replaceCaWidget(self, old, new, time):
        Ca_Widget = QWidget(self.filler)
        Ca_VLayout = QVBoxLayout()
        Ca_Widget.setLayout(Ca_VLayout)

        try:
            # value = self.output['youlig']['youlig']
            Ca = MyCaLineGraph(old, new, time)
            VarChange,oldRate,newRate=self.calculate(old,new)
            if VarChange < 0:
                fangcha = QLabel('方差同比缩小：' + str(-VarChange) + '%')
            else:
                fangcha = QLabel('方差同比增长：' + str(VarChange) + '%')
            fangcha.setFont(QFont('Timers', 12, QFont.Times))
            fangcha.setAlignment(Qt.AlignCenter)
            yuanhegelv = QLabel('原始合格率：' + str(oldRate) + '%')
            yuanhegelv.setFont(QFont('Timers', 12, QFont.Times))
            yuanhegelv.setAlignment(Qt.AlignCenter)
            houhegelv = QLabel('调控后合格率：' + str(newRate) + '%')
            houhegelv.setFont(QFont('Timers', 12, QFont.Times))
            houhegelv.setAlignment(Qt.AlignCenter)
            Ca_VLayout.addWidget(Ca)
            Ca_VLayout.addWidget(fangcha)
            Ca_VLayout.addWidget(yuanhegelv)
            Ca_VLayout.addWidget(houhegelv)
        except Exception:
            QMessageBox.information(self, '提示', '游离钙数据出错', QMessageBox.Yes)

        oldWidget = self.findChild(QWidget, 'CaWidget')
        if oldWidget != None:
            self.fillLay.removeWidget(oldWidget)
            sip.delete(oldWidget)
        Ca_Widget.setObjectName('CaWidget')
        self.fillLay.addWidget(Ca_Widget, 0, 15, 2, 1)

    def calculate(self,old,new):
        oldPass = 0
        newPass = 0
        for element in old:
            if element <= 2:
                oldPass += 1
        for element in new:
            if element <= 2:
                newPass += 1
        oldRate = round((oldPass / len(old)) * 100, 2)
        newRate = round((newPass / len(new)) * 100, 2)
        oldVar = np.var(old)  # 求原方差
        newVar = np.var(new)  # 求调控后方差
        VarChange = round(((newVar - oldVar) / oldVar) * 100, 2)
        return VarChange,oldRate,newRate
    def replaceThreeValueWidget(self, old, new):
        ThreeValueWidget = QWidget(self.filler)
        ThreeValueHLayout = QHBoxLayout()
        ThreeValueWidget.setLayout(ThreeValueHLayout)
        KHVWidget = QWidget()
        KHVLay = QVBoxLayout()
        KHVWidget.setLayout(KHVLay)
        SMVWidget = QWidget()
        SMVLay = QVBoxLayout()
        SMVWidget.setLayout(SMVLay)
        IMVWidget = QWidget()
        IMVLay = QVBoxLayout()
        IMVWidget.setLayout(IMVLay)

        try:
            # value = self.output['youlig']['youlig']
            KH = MyThreeValueLineGraph(old['shuliaoKH'], new['shuliaoKH'], self.timeLabel, 0)
            SM = MyThreeValueLineGraph(old['shuliaoSM'], new['shuliaoSM'], self.timeLabel, 1)
            IM = MyThreeValueLineGraph(old['shuliaoIM'], new['shuliaoIM'], self.timeLabel, 2)

            VarChange, oldRate, newRate = self.calculate(old['shuliaoKH'], new['shuliaoKH'])
            if VarChange < 0:
                KH_Label1 = QLabel('方差同比缩小：' + str(-VarChange) + '%')
            else:
                KH_Label1 = QLabel('方差同比增长：' + str(VarChange) + '%')
            KH_Label1.setFont(QFont('Timers', 12, QFont.Times))
            KH_Label1.setAlignment(Qt.AlignCenter)
            KH_Label2 = QLabel('原始合格率：' + str(oldRate) + '%')
            KH_Label2.setFont(QFont('Timers', 12, QFont.Times))
            KH_Label2.setAlignment(Qt.AlignCenter)
            KH_Label3 = QLabel('调控后合格率：' + str(newRate) + '%')
            KH_Label3.setFont(QFont('Timers', 12, QFont.Times))
            KH_Label3.setAlignment(Qt.AlignCenter)

            VarChange, oldRate, newRate = self.calculate(old['shuliaoSM'], new['shuliaoSM'])
            if VarChange < 0:
                SM_Label1 = QLabel('方差同比缩小：' + str(-VarChange) + '%')
            else:
                SM_Label1 = QLabel('方差同比增长：' + str(VarChange) + '%')
            SM_Label1.setFont(QFont('Timers', 12, QFont.Times))
            SM_Label1.setAlignment(Qt.AlignCenter)
            SM_Label2 = QLabel('原始合格率：' + str(oldRate) + '%')
            SM_Label2.setFont(QFont('Timers', 12, QFont.Times))
            SM_Label2.setAlignment(Qt.AlignCenter)
            SM_Label3 = QLabel('调控后合格率：' + str(newRate) + '%')
            SM_Label3.setFont(QFont('Timers', 12, QFont.Times))
            SM_Label3.setAlignment(Qt.AlignCenter)

            VarChange, oldRate, newRate = self.calculate(old['shuliaoIM'], new['shuliaoIM'])
            if VarChange < 0:
                IM_Label1 = QLabel('方差同比缩小：' + str(-VarChange) + '%')
            else:
                IM_Label1 = QLabel('方差同比增长：' + str(VarChange) + '%')
            IM_Label1.setFont(QFont('Timers', 12, QFont.Times))
            IM_Label1.setAlignment(Qt.AlignCenter)
            IM_Label2 = QLabel('原始合格率：' + str(oldRate) + '%')
            IM_Label2.setFont(QFont('Timers', 12, QFont.Times))
            IM_Label2.setAlignment(Qt.AlignCenter)
            IM_Label3 = QLabel('调控后合格率：' + str(newRate) + '%')
            IM_Label3.setFont(QFont('Timers', 12, QFont.Times))
            IM_Label3.setAlignment(Qt.AlignCenter)

            KHVLay.addWidget(KH)
            KHVLay.addWidget(KH_Label1)
            KHVLay.addWidget(KH_Label2)
            KHVLay.addWidget(KH_Label3)
            SMVLay.addWidget(SM)
            SMVLay.addWidget(SM_Label1)
            SMVLay.addWidget(SM_Label2)
            SMVLay.addWidget(SM_Label3)
            IMVLay.addWidget(IM)
            IMVLay.addWidget(IM_Label1)
            IMVLay.addWidget(IM_Label2)
            IMVLay.addWidget(IM_Label3)
            ThreeValueHLayout.addWidget(KHVWidget)
            ThreeValueHLayout.addWidget(SMVWidget)
            ThreeValueHLayout.addWidget(IMVWidget)
            ThreeValueWidget.setFixedHeight(self.Height * 0.618)  # 调整三率值的页面高度
        except Exception:
            QMessageBox.information(self, '提示', '三率值数据出错', QMessageBox.Yes)

        oldWidget = self.findChild(QWidget, 'ThreeValueWidget')
        if oldWidget != None:
            self.fillLay.removeWidget(oldWidget)
            sip.delete(oldWidget)
        ThreeValueWidget.setObjectName('ThreeValueWidget')
        self.fillLay.addWidget(ThreeValueWidget, 3, 0, 2, 16)

    def replaceYijitongWidget(self, old,new):
        yijitong_VWidget = QWidget(self.filler)
        yijitong_VLayout = QVBoxLayout()
        yijitong_VWidget.setLayout(yijitong_VLayout)
        yijitong_HWidget = QWidget(self.filler)
        yijitong_HLayout = QHBoxLayout()
        yijitong_HWidget.setLayout(yijitong_HLayout)

        try:
            # value = self.output['yijit']
            yijitwdA = MyYijitongMplCanvas(old['yijitwdA'],new['yijitwdA'], 0, self.timeLabel)
            yijityqA = MyYijitongMplCanvas(old['yijityqA'],new['yijityqA'], 1, self.timeLabel)
            yijitwdB = MyYijitongMplCanvas(old['yijitwdB'],new['yijitwdB'], 2, self.timeLabel)
            yijityqB = MyYijitongMplCanvas(old['yijityqB'],new['yijityqB'], 3, self.timeLabel)
            # yijitong_title = QLabel('一级筒指标预测')
            # yijitong_title.setAlignment(Qt.AlignLeft)
            # yijitong_VLayout.addWidget(yijitong_title)
            yijitong_HLayout.addWidget(yijitwdA)
            yijitong_HLayout.addWidget(yijityqA)
            yijitong_HLayout.addWidget(yijitwdB)
            yijitong_HLayout.addWidget(yijityqB)
            yijitong_VLayout.addWidget(yijitong_HWidget)
            yijitong_VWidget.setFixedHeight(self.Height * 0.618)  # 调整一级筒数据的页面高度
        except Exception:
            QMessageBox.information(self, '提示', '一级筒指标数据出错', QMessageBox.Yes)

        oldWidget = self.findChild(QWidget, 'yijitongWidget')
        if oldWidget != None:
            self.fillLay.removeWidget(oldWidget)
            sip.delete(oldWidget)
        yijitong_VWidget.setObjectName('yijitongWidget')
        self.fillLay.addWidget(yijitong_VWidget, 6, 0, 1, 16)

    def replaceFjlWidget(self, old,new):
        fjlWidget = QWidget(self.filler)
        fjlHLayout = QHBoxLayout()
        fjlWidget.setLayout(fjlHLayout)

        try:
            # value = self.output['youlig']['youlig']
            wd = MyFjlLineGraph(old['fenjielwd'],new['fenjielwd'],self.timeLabel,0)
            yq = MyFjlLineGraph(old['fenjielyq'],new['fenjielyq'],self.timeLabel,1)
            Label1 = QLabel('温度：--%')
            Label1.setFont(QFont('Timers', 12, QFont.Times))
            Label1.setAlignment(Qt.AlignCenter)
            Label2 = QLabel('压强--%')
            Label2.setFont(QFont('Timers', 12, QFont.Times))
            Label2.setAlignment(Qt.AlignCenter)
            fjlHLayout.addWidget(wd)
            fjlHLayout.addWidget(Label1)
            fjlHLayout.addWidget(yq)
            fjlHLayout.addWidget(Label2)
            fjlWidget.setFixedHeight(self.Height * 0.618)  # 调整分解炉的页面高度
        except Exception:
            QMessageBox.information(self, '提示', '分解炉数据出错', QMessageBox.Yes)

        oldWidget = self.findChild(QWidget, 'fjlWidget')
        if oldWidget != None:
            self.fillLay.removeWidget(oldWidget)
            sip.delete(oldWidget)
        fjlWidget.setObjectName('fjlWidget')
        self.fillLay.addWidget(fjlWidget, 8, 0, 1, 16)

    #
    def replaceBljWidget(self, data):

        oldWidget = self.findChild(QWidget, 'bljWidget')
        # if oldWidget != None:
        #     self.fillLay.removeWidget(oldWidget)
        #     sip.delete(oldWidget)
        # bljHWidget.setObjectName('bljWidget')
        # self.fillLay.addWidget(Ca_Widget, 0, 15, 2, 1)

    def replaceHzyWidget(self, old,new):
        hzyWidget = QWidget(self.filler)
        hzyHLayout = QHBoxLayout()
        hzyWidget.setLayout(hzyHLayout)

        try:
            # value = self.output['youlig']['youlig']
            wd = MyHzyLineGraph(old['yaoweiwd'], new['yaoweiwd'], 0)
            # yq = MyHzyLineGraph(, , 1)
            Label1 = QLabel('温度：--%')
            Label1.setFont(QFont('Timers', 12, QFont.Times))
            Label1.setAlignment(Qt.AlignCenter)
            # Label2 = QLabel('压强--%')
            # Label2.setFont(QFont('Timers', 12, QFont.Times))
            # Label2.setAlignment(Qt.AlignCenter)
            hzyHLayout.addWidget(wd)
            hzyHLayout.addWidget(Label1)
            # hzyHLayout.addWidget(yq)
            # hzyHLayout.addWidget(Label2)
            hzyWidget.setFixedHeight(self.Height * 0.618)  # 调整回转窑的页面高度
        except Exception:
            QMessageBox.information(self, '提示', '回转窑数据出错', QMessageBox.Yes)

        oldWidget = self.findChild(QWidget, 'hzyWidget')
        if oldWidget != None:
            self.fillLay.removeWidget(oldWidget)
            sip.delete(oldWidget)
        hzyWidget.setObjectName('hzyWidget')
        self.fillLay.addWidget(hzyWidget, 12, 0, 1, 16)


class MyProduceWarWnd(QMainWindow):
    def __init__(self, day, hour, number=1):  # number为条数，暂且只预测一个时间点
        super(MyProduceWarWnd, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        self.Width = metric.width()
        self.Height = metric.height()
        self.setWindowTitle('生产预警')
        self.ratio_w = 0.6
        self.ratio_h = 0.78
        self.flag = 0
        # self.setStyleSheet("background-color: rgb(225,255,255)")
        output, real = production_warning(str(day), str(hour))
        data, name = get_by_fragment2(str(day) + str(hour), 5)
        # print(data)
        time = ['']
        for element in data:
            time.append(element[0][4:6] + '/' + element[0][6:] + ' ' + element[1])
        print(time)
        # self.move(50, 50)
        # # 调整窗口显示时的大小
        # self.setFixedWidth(self.Width * self.ratio_w)
        # self.setMinimumHeight(self.Height * self.ratio_h)

        left = -9  # 为了使窗口能够位于左上角
        self.move(left, 0)
        self.setFixedSize(self.Width, self.Height - 72 * self.Height / 768)  # 72为win10任务栏高度

        self.pageView = QTabWidget()
        self.tab = {}
        self.pic = {}
        for i in range(number):
            self.tab[i] = QLabel()
            self.pageView.addTab(self.tab[i], '%d小时' % (hour + i))
            self.pic[i] = QGridLayout(self.tab[i])
            data = get_by_hour(str(day) + str(hour))

            three_VWidget = QWidget()
            three_VLayout = QVBoxLayout(three_VWidget)
            three_VWidget.setLayout(three_VLayout)

            title = QLabel('熟料三率值预测')
            title.setAlignment(Qt.AlignCenter)
            title.setFont(QFont('Timers', 15, QFont.Fantasy))
            three_VLayout.addWidget(title)

            three_HWidget = QWidget()
            three_HLayout = QHBoxLayout(three_HWidget)
            three_HWidget.setLayout(three_HLayout)
            three_VLayout.addWidget(three_HWidget)

            one = QWidget()
            one_Layout = QHBoxLayout()
            one.setLayout(one_Layout)
            KH = QLabel(str(output['sanlvz']['KH']))
            KH.setAlignment(Qt.AlignCenter)
            KH.setFixedSize(100, 100)
            if output['sanlvz']['KH'] <= 0.92 and output['sanlvz']['KH'] >= 0.88:
                KH.setStyleSheet(
                    "border-color: rgb(0,255,0);font-size: 20px;border-width: 3px 3px 3px 3px;border-style: solid;border-radius:50px; ")
            elif output['sanlvz']['KH'] > 0.96 and output['sanlvz']['KH'] < 0.87:
                KH.setStyleSheet(
                    "border-color: rgb(255,0,0);font-size: 20px;border-width: 3px 3px 3px 3px;border-style: solid;border-radius:50px; ")
            else:
                KH.setStyleSheet(
                    "border-color: rgb(238,118,33);font-size: 20px;border-width: 3px 3px 3px 3px;border-style: solid;border-radius:50px; ")
            KH_VLayout = QVBoxLayout()
            KH_title = QLabel('KH')
            KH_title.setAlignment(Qt.AlignHCenter)
            KH_title.setFont(QFont('Timers', 10, QFont.Fantasy))
            KH_VLayout.addWidget(KH_title)
            one_Layout.addWidget(KH)
            KH_VLayout.addWidget(one)
            KH_des = QLabel('KH表示熟料中SiO₂被CaO饱和成A矿\n的程度')
            KH_VLayout.addWidget(KH_des)
            KH_VWidget = QWidget()
            KH_VWidget.setLayout(KH_VLayout)
            three_HLayout.addWidget(KH_VWidget)

            two = QWidget()
            two_Layout = QHBoxLayout()
            two.setLayout(two_Layout)
            IM = QLabel(str(output['sanlvz']['IM']))
            IM.setAlignment(Qt.AlignCenter)
            IM.setFixedSize(100, 100)
            if output['sanlvz']['IM'] <= 1.5 and output['sanlvz']['IM'] >= 1.1:
                IM.setStyleSheet(
                    "border-color: rgb(0,255,0);font-size: 20px;border-width: 3px 3px 3px 3px;border-style: solid;border-radius:50px; ")
            elif output['sanlvz']['IM'] < 0.9 and output['sanlvz']['IM'] > 1.7:
                IM.setStyleSheet(
                    "border-color: rgb(255,0,0);font-size: 20px;border-width: 3px 3px 3px 3px;border-style: solid;border-radius:50px; ")
            else:
                IM.setStyleSheet(
                    "border-color: rgb(238,118,33);font-size: 20px;border-width: 3px 3px 3px 3px;border-style: solid;border-radius:50px; ")
            IM_VLayout = QVBoxLayout()
            IM_title = QLabel('IM')
            IM_title.setAlignment(Qt.AlignHCenter)
            IM_title.setFont(QFont('Timers', 10, QFont.Fantasy))
            IM_VLayout.addWidget(IM_title)
            two_Layout.addWidget(IM)
            IM_VLayout.addWidget(two)
            IM_des = QLabel('IM表示熟料中Al₂O₃与Fe₂O₃含量\n之比')
            IM_VLayout.addWidget(IM_des)
            IM_VWidget = QWidget()
            IM_VWidget.setLayout(IM_VLayout)
            three_HLayout.addWidget(IM_VWidget)

            three = QWidget()
            three_Layout = QHBoxLayout()
            three.setLayout(three_Layout)
            SM = QLabel(str(output['sanlvz']['SM']))
            SM.setAlignment(Qt.AlignCenter)
            SM.setFixedSize(100, 100)
            if output['sanlvz']['SM'] <= 2.2 and output['sanlvz']['SM'] >= 1.8:
                SM.setStyleSheet(
                    "border-color: rgb(0,255,0);font-size: 20px;border-width: 3px 3px 3px 3px;border-style: solid;border-radius:50px; ")
            elif output['sanlvz']['SM'] < 1.7 and output['sanlvz']['SM'] > 2.5:
                SM.setStyleSheet(
                    "border-color: rgb(255,0,0);font-size: 20px;border-width: 3px 3px 3px 3px;border-style: solid;border-radius:50px; ")
            else:
                SM.setStyleSheet(
                    "border-color: rgb(238,118,33);font-size: 20px;border-width: 3px 3px 3px 3px;border-style: solid;border-radius:50px; ")
            SM_VLayout = QVBoxLayout()
            SM_title = QLabel('SM')
            SM_title.setAlignment(Qt.AlignHCenter)
            SM_title.setFont(QFont('Timers', 10, QFont.Fantasy))
            SM_VLayout.addWidget(SM_title)
            three_Layout.addWidget(SM)
            SM_VLayout.addWidget(three)
            SM_des = QLabel('IM表示熟料中SiO₂含量与Al₂O₃、\nFe₂O₃之和的比')
            SM_VLayout.addWidget(SM_des)
            SM_VWidget = QWidget()
            SM_VWidget.setLayout(SM_VLayout)
            three_HLayout.addWidget(SM_VWidget)
            three_HLayout.setSpacing(0)
            self.pic[i].addWidget(three_VWidget, 0, 0, 1, 2)

            self.line0 = QtWidgets.QFrame(self)
            self.line0.setGeometry(QtCore.QRect(self.Width * 0.5, 0, 16, self.Height))
            self.line0.setFrameShape(QtWidgets.QFrame.VLine)
            self.line0.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.pic[i].addWidget(self.line0, 0, 1)

            Effic_Widget = QWidget()
            Effic_VLayout = QVBoxLayout()
            Effic_Widget.setLayout(Effic_VLayout)

            try:
                value = Production_warning_rexiaolv(data[1])
                Effic_title = QLabel('分解炉热效率')
                Effic_title.setFixedWidth(250)
                Effic_title.setFont(QFont('Timers', 15, QFont.Fantasy))
                Effic_title.setAlignment(Qt.AlignCenter)
                Effic_VLayout.addWidget(Effic_title)
                rexiaol_Widget = QWidget()
                rexiaol_Layout = QHBoxLayout()
                rexiaol_Widget.setLayout(rexiaol_Layout)
                Effic = QLabel(str(output['rexfiaol']['rexiaol'] * 100)[:4] + '%')
                Effic.setAlignment(Qt.AlignCenter)
                Effic.setFixedSize(100, 100)
                Effic.setStyleSheet(
                    "font-size: 20px;border-width: 3px 3px 3px 3px;border-style: solid;border-color: rgb(0,255,0);border-radius:50px; ")
                rexiaol_Layout.addWidget(Effic)
                Effic_VLayout.addWidget(rexiaol_Widget)
                Effic_VLayout.addWidget(QLabel('热效率表示有效输出的能量与输入的能量之比'))
                self.pic[i].addWidget(Effic_Widget, 0, 2)
            except Exception:
                QMessageBox.information(self, '提示', '热效率数据出错', QMessageBox.Yes)

            self.line1 = QtWidgets.QFrame(self)
            self.line1.setGeometry(QtCore.QRect(self.Width * 0.5, 0, 16, self.Height))
            self.line1.setFrameShape(QtWidgets.QFrame.VLine)
            self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.pic[i].addWidget(self.line1, 0, 3)

            Ca_Widget = QWidget()
            Ca_VLayout = QVBoxLayout()
            Ca_Widget.setLayout(Ca_VLayout)

            try:
                value = output['youlig']['youlig']
                Ca = MyCaMplCanvas(value)
                Ca_title = QLabel('熟料游离钙合格预测')
                Ca_title.setAlignment(Qt.AlignCenter)
                Ca_title.setFont(QFont('Timers', 15, QFont.Fantasy))
                Ca_VLayout.addWidget(Ca_title)
                Ca_VLayout.addWidget(Ca)
                self.pic[i].addWidget(Ca_Widget, 0, 4)
            except Exception:
                QMessageBox.information(self, '提示', '游离钙数据出错', QMessageBox.Yes)

            self.line2 = QtWidgets.QFrame(self)
            self.line2.setGeometry(QtCore.QRect(self.Width * 0.5, 0, 16, self.Height))
            self.line2.setFrameShape(QtWidgets.QFrame.HLine)
            self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.pic[i].addWidget(self.line2, 1, 0, 1, 5)

            yijitong_VWidget = QWidget()
            yijitong_VLayout = QVBoxLayout()
            yijitong_VWidget.setLayout(yijitong_VLayout)
            yijitong_HWidget = QWidget()
            yijitong_HLayout = QHBoxLayout()
            yijitong_HWidget.setLayout(yijitong_HLayout)

            try:
                # value = output['yijit']
                old = []
                new = []
                yijitwdA = MyYijitongMplCanvas(old, new, 0, time)
                yijityqA = MyYijitongMplCanvas(old, new, 1, time)
                yijitwdB = MyYijitongMplCanvas(old, new, 2, time)
                yijityqB = MyYijitongMplCanvas(old, new, 3, time)
                # yijitong_title = QLabel('一级筒指标预测')
                # yijitong_title.setAlignment(Qt.AlignLeft)
                # yijitong_VLayout.addWidget(yijitong_title)
                yijitong_HLayout.addWidget(yijitwdA)
                yijitong_HLayout.addWidget(yijityqA)
                yijitong_HLayout.addWidget(yijitwdB)
                yijitong_HLayout.addWidget(yijityqB)
                yijitong_VLayout.addWidget(yijitong_HWidget)
                self.pic[i].addWidget(yijitong_VWidget, 2, 0, 1, 5)
            except Exception:
                QMessageBox.information(self, '提示', '一级筒指标数据出错', QMessageBox.Yes)

            self.line3 = QtWidgets.QFrame(self)
            self.line3.setGeometry(QtCore.QRect(0, self.Height * 0.73, self.Width, 16))
            self.line3.setFrameShape(QtWidgets.QFrame.HLine)
            self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.pic[i].addWidget(self.line3, 3, 0, 1, 5)

            yao_HWidget = QWidget()
            yao_HLayout = QHBoxLayout()
            yao_HWidget.setLayout(yao_HLayout)

            try:
                value_yaotouc = output['yaotou_yaoweic']['yaotouc']
                value_yaoweic = output['yaotou_yaoweic']['yaoweic']
                yao_touc = MyYaoMplCanvas(value_yaotouc, real['yaotou_yaoweic']['yaotouc'], 0, time)
                yao_weic = MyYaoMplCanvas(value_yaoweic, real['yaotou_yaoweic']['yaoweic'], 1, time)
                yao_HLayout.addWidget(yao_touc)
                yao_HLayout.addWidget(yao_weic)
                self.pic[i].addWidget(yao_HWidget, 4, 0)
            except Exception:
                QMessageBox.information(self, '提示', '窑指标数据出错', QMessageBox.Yes)

            try:
                value = real['rehao'][:4]
                # print(123)
                # print(value)
                value.append(output['rehao']['rehao'])
                # print(value)
                heat = MyHeatCanvas(value, time)  # 柱状图
                self.pic[i].addWidget(heat, 4, 2, 1, 3)
            except Exception:
                QMessageBox.information(self, '提示', '分解炉热耗数据出错', QMessageBox.Yes)

            # self.guide = '生产预警指导'
            # self.okBtn = QPushButton('ok', self.tab[i])#这里注释掉后记得把相关函数也注释掉，否则会闪退
            # self.okBtn.move(self.width() * 0.85, self.height() * 0.9)
            # self.okBtn.clicked.connect(self.Accept)

        # 设置将self.pageView为中心Widget
        self.setCentralWidget(self.pageView)
        self.show()

    #
    # def Accept(self):
    #     self.addDock()
    #
    # def addDock(self):
    #     if self.flag == 0:
    #         self.flag = 1
    #         dock1 = MyDockWidget('DockWidget')
    #         dock1.setFeatures(QDockWidget.DockWidgetClosable)
    #         dock1.setAllowedAreas(Qt.RightDockWidgetArea)
    #         # try:
    #         #     self.bar = MyHeatCanvas()  # 柱状图
    #         # except Exception:
    #         #     QMessageBox.information(self,'提示','添加柱状图失败',QMessageBox.Yes)
    #
    #         self.label = QLabel(self.guide)
    #         dock1.setFixedWidth(400)
    #         dock1.setWidget(self.label)
    #         dock1.dock_signal.connect(self.change)
    #         self.addDockWidget(Qt.RightDockWidgetArea, dock1)
    #         self.setFixedWidth(self.Width)
    #     else:
    #         pass
    #
    # def change(self, str):  # 关闭浮动窗口时重新改变窗口大小
    #     self.flag = 0
    #     self.setFixedWidth(self.Width)

    # def resizeEvent(self, *args, **kwargs):
    #     if self.flag == 0:
    #         self.okBtn.move(self.width() * 0.85, self.height() * 0.9)
    #     else:
    #         self.okBtn.move((self.width() - 400) * 0.85, self.height() * 0.9)
    def getHeat(self):
        pass


class MyMplCanvas(FigureCanvas):
    """这是一个窗口部件，即QWidget（当然也是FigureCanvasAgg）"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # 每次plot()调用的时候，我们希望原来的坐标轴被清除(所以False)
        # self.axes.hold(False)
        fig.set_tight_layout(True)
        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyCaMplCanvas(MyMplCanvas):
    def __init__(self, value):
        self.value = value
        super(MyCaMplCanvas, self).__init__()

    def compute_initial_figure(self):
        # data = MyMplCanvas.find_data(self.day, self.hour)

        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False

        # data是选中的那一行的数据，利用data来将合格、不合格的数据求出来，存在Percentage的列表中

        # Percentage
        Percentage = self.value  # 前者为不合格，后者为合格
        Percentage[0] = self.value[0] * 100
        Percentage[1] = self.value[1] * 100

        label_list = ['不合格', '合格']
        color = ['red', 'yellow']
        explode = [0, 0]
        self.axes.pie(Percentage, explode=explode, colors=color, labels=label_list, labeldistance=1.1,
                      autopct="%1.2f%%", shadow=False, startangle=90, pctdistance=0.6)
        self.axes.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
        self.axes.set_title('游离钙')
        self.axes.legend()
        # self.axes.barh(range(2), Percentage, height=0.7, color='steelblue', alpha=0.8)
        # self.axes.set_yticks(range(2))
        # self.axes.set_yticklabels(['合格', '不合格'])
        # self.axes.set_xlim(0, 100)
        # self.axes.set_xlabel('百分比 %')
        # self.axes.set_title('游离钙是否合格的百分比')

        # for x, y, in zip(Percentage, range(2)):
        #     self.axes.text(x + 5, y, '%.2f' % x, ha='right', va='center', fontsize=10)


class MyCaLineGraph(MyMplCanvas):
    def __init__(self, old, new, time):
        for i in range(len(old)):
            old[i] = round(old[i], 2)
        for i in range(len(new)):
            new[i] = round(new[i], 2)
        self.oldValue = old
        self.newValue = new
        self.x_ticklabels = time
        super(MyCaLineGraph, self).__init__()

    def compute_initial_figure(self):
        # data = MyMplCanvas.find_data(self.day, self.hour)

        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
        # x = [0, 1, 2, 3, 4, 5, 6, 7]
        # y = [0.6, 0.7, 0.8, 0.9, 0.8, 0.9, 0.8, 0.6]
        # y1 = [0.5, 0.6, 0.7, 0.8, 0.9, 0.8, 0.9, 0.7]
        y = self.oldValue
        y1 = self.newValue
        x = range(len(y))
        self.axes.plot(x, y, label='weight changes', linewidth=1, color='r', marker='o',
                       markerfacecolor='blue', markersize=5)
        self.axes.plot(x, y1, label='weight changes', linewidth=1, color='r', marker='^',
                       markerfacecolor='green', markersize=5, linestyle="--")

        self.axes.set_xticklabels(self.x_ticklabels, rotation=15, fontsize=9)

        self.axes.set_title('游离钙趋势图')
        self.axes.set_ylabel('游离钙', verticalalignment='center', fontproperties=labelfont)

        # self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
        for a, b in zip(x, y):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)
        for a, b in zip(x, y1):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)


class MyThreeValueLineGraph(MyMplCanvas):
    def __init__(self, old, new, time, flag):
        for i in range(len(old)):
            old[i] = round(old[i], 2)
        for i in range(len(new)):
            new[i] = round(new[i], 2)
        self.oldValue = old
        self.newValue = new
        self.x_ticklabels = time
        self.flag = flag
        super(MyThreeValueLineGraph, self).__init__()

    def compute_initial_figure(self):
        # data = MyMplCanvas.find_data(self.day, self.hour)
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
        # x = [0, 1, 2, 3, 4, 5, 6, 7]
        # y = [0.6, 0.7, 0.8, 0.9, 0.8, 0.9, 0.8, 0.6]
        # y1 = [0.5, 0.6, 0.7, 0.8, 0.9, 0.8, 0.9, 0.7]
        y = self.oldValue
        y1 = self.newValue
        x = range(len(y))
        self.axes.plot(x, y, label='weight changes', linewidth=1, color='r', marker='o',
                       markerfacecolor='blue', markersize=5)
        self.axes.plot(x, y1, label='weight changes', linewidth=1, color='r', marker='^',
                       markerfacecolor='green', markersize=5, linestyle="--")

        self.axes.set_xticklabels(self.x_ticklabels, rotation=15, fontsize=9)

        self.axes.set_ylabel('单位/%', verticalalignment='center', fontproperties=labelfont)

        if self.flag == 0:
            self.axes.set_title('KH')
        elif self.flag == 1:
            self.axes.set_title('SM')
        elif self.flag == 2:
            self.axes.set_title('IM')
        else:
            QMessageBox.information(self, '提示', '三率值标志位设置错误', QMessageBox.Yes)

        # self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
        for a, b in zip(x, y):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)
        for a, b in zip(x, y1):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)


class MyFjlLineGraph(MyMplCanvas):
    def __init__(self, old, new, time, flag):
        for i in range(len(old)):
            old[i] = round(old[i], 2)
        for i in range(len(new)):
            new[i] = round(new[i], 2)
        self.oldValue = old
        self.newValue = new
        self.x_ticklabels = time
        self.flag = flag
        super(MyFjlLineGraph, self).__init__()

    def compute_initial_figure(self):
        # data = MyMplCanvas.find_data(self.day, self.hour)
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
        # x = [0, 1, 2, 3, 4, 5, 6, 7]
        # y = [0.6, 0.7, 0.8, 0.9, 0.8, 0.9, 0.8, 0.6]
        # y1 = [0.5, 0.6, 0.7, 0.8, 0.9, 0.8, 0.9, 0.7]
        y = self.oldValue
        y1 = self.newValue
        x = range(len(y))
        self.axes.plot(x, y, label='weight changes', linewidth=1, color='r', marker='o',
                       markerfacecolor='blue', markersize=5)
        self.axes.plot(x, y1, label='weight changes', linewidth=1, color='r', marker='^',
                       markerfacecolor='green', markersize=5, linestyle="--")

        self.axes.set_xticklabels(self.x_ticklabels, rotation=15, fontsize=9)

        self.axes.set_ylabel('单位/%', verticalalignment='center', fontproperties=labelfont)

        if self.flag == 0:
            self.axes.set_title('分解炉温度')
        elif self.flag == 1:
            self.axes.set_title('分解炉压强')
        else:
            QMessageBox.information(self, '提示', '分解炉标志位设置错误', QMessageBox.Yes)

        # self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
        for a, b in zip(x, y):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)
        for a, b in zip(x, y1):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)


class MyHzyLineGraph(MyMplCanvas):
    def __init__(self, old, new, time, flag):
        for i in range(len(old)):
            old[i] = round(old[i], 2)
        for i in range(len(new)):
            new[i] = round(new[i], 2)
        self.oldValue = old
        self.newValue = new
        self.x_ticklabels = time
        self.flag = flag
        super(MyHzyLineGraph, self).__init__()

    def compute_initial_figure(self):
        # data = MyMplCanvas.find_data(self.day, self.hour)
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
        # x = [0, 1, 2, 3, 4, 5, 6, 7]
        # y = [0.6, 0.7, 0.8, 0.9, 0.8, 0.9, 0.8, 0.6]
        # y1 = [0.5, 0.6, 0.7, 0.8, 0.9, 0.8, 0.9, 0.7]
        y = self.oldValue
        y1 = self.newValue
        x = range(len(y))
        self.axes.plot(x, y, label='weight changes', linewidth=1, color='r', marker='o',
                       markerfacecolor='blue', markersize=5)
        self.axes.plot(x, y1, label='weight changes', linewidth=1, color='r', marker='^',
                       markerfacecolor='green', markersize=5, linestyle="--")

        self.axes.set_xticklabels(self.x_ticklabels, rotation=15, fontsize=9)

        self.axes.set_ylabel('单位/%', verticalalignment='center', fontproperties=labelfont)

        if self.flag == 0:
            self.axes.set_title('回转窑温度')
        elif self.flag == 1:
            self.axes.set_title('回转窑压强')
        else:
            QMessageBox.information(self, '提示', '回转窑标志位设置错误', QMessageBox.Yes)

        # self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
        for a, b in zip(x, y):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)
        for a, b in zip(x, y1):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)


class MyBljLineGraph(MyMplCanvas):
    def __init__(self, old, new, time, flag):
        for i in range(len(old)):
            old[i] = round(old[i], 2)
        for i in range(len(new)):
            new[i] = round(new[i], 2)
        self.oldValue = old
        self.newValue = new
        self.x_ticklabels = time
        self.flag = flag
        super(MyBljLineGraph, self).__init__()

    def compute_initial_figure(self):
        # data = MyMplCanvas.find_data(self.day, self.hour)
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
        # x = [0, 1, 2, 3, 4, 5, 6, 7]
        # y = [0.6, 0.7, 0.8, 0.9, 0.8, 0.9, 0.8, 0.6]
        # y1 = [0.5, 0.6, 0.7, 0.8, 0.9, 0.8, 0.9, 0.7]
        y = self.oldValue
        y1 = self.newValue
        x = range(len(y))
        self.axes.plot(x, y, label='weight changes', linewidth=1, color='r', marker='o',
                       markerfacecolor='blue', markersize=5)
        self.axes.plot(x, y1, label='weight changes', linewidth=1, color='r', marker='^',
                       markerfacecolor='green', markersize=5, linestyle="--")

        self.axes.set_xticklabels(self.x_ticklabels, rotation=15, fontsize=9)

        self.axes.set_ylabel('单位/%', verticalalignment='center', fontproperties=labelfont)

        if self.flag == 0:
            self.axes.set_title('篦冷机')
        elif self.flag == 1:
            self.axes.set_title('篦冷机')
        elif self.flag == 2:
            self.axes.set_title('篦冷机')
        else:
            QMessageBox.information(self, '提示', '篦冷机标志位设置错误', QMessageBox.Yes)

        # self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
        for a, b in zip(x, y):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)
        for a, b in zip(x, y1):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)


class MyEfficMpCanvas(MyMplCanvas):
    def __init__(self, value):
        self.value = value
        super(MyEfficMpCanvas, self).__init__()

    def compute_initial_figure(self):
        #        data = MyMplCanvas.find_data(self.day, self.hour)  # data是选中那天的输入的所有数据

        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False

        # 利用data算出热耗，以及1减去热耗剩余的值，放在size列表中，后面一个是热耗
        size = [100 - self.value * 100, self.value * 100]  # 测试用
        label_list = ['', '热效率']
        color = ['yellow', 'red']
        explode = [0, 0]
        self.axes.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1,
                      autopct="%1.2f%%", shadow=False, startangle=90, pctdistance=0.6)
        self.axes.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
        self.axes.set_title('回转窑的热效率')
        self.axes.legend()


class MyCoalMpCanvas(QWidget):
    def __init__(self, value):
        self.value = value
        super(MyCoalMpCanvas, self).__init__()
        self.compute_initial_figure()

    def compute_initial_figure(self):
        consumption = self.value

        self.Label = QLabel()
        self.lay = QVBoxLayout()

        self.Label.setText('分解炉的标煤耗：  %d   kJ/kg' % consumption)
        ft = QFont()
        ft.setPointSize(12)
        self.Label.setFont(ft)
        # self.Label.show()

        for i in range(2):
            self.lay.addWidget(QLabel(''))
        self.lay.addWidget(self.Label)
        for i in range(3):
            self.lay.addWidget(QLabel(''))

        self.setLayout(self.lay)


class MyHeatCanvas(MyMplCanvas):

    def __init__(self, value, time):
        self.value = value
        self.x_ticklabels = time
        super(MyHeatCanvas, self).__init__()

    def compute_initial_figure(self):
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
        x1 = range(5)
        y1 = self.value[:5]
        self.axes.bar(x1[:-1], y1[:-1], color='blue')
        self.axes.bar(x1[-1], y1[-1], color='red')
        for a, b in zip(x1, y1):
            self.axes.text(a, b + 0.05, '%.2f' % b, ha='center', va='bottom', fontsize=11)
        self.axes.set_ylabel('标煤耗 (kJ/kg)')
        self.axes.set_xticklabels(self.x_ticklabels, rotation=15, fontsize=9)
        # y2 = self.value[3] * 100
        # self.axes2 = self.axes.twinx()
        # self.axes2.set_ylim(0, 100)
        # self.axes2.bar(3, y2, color='red')
        # self.axes2.text(3, y2 + 0.05, '%.2f' % y2, ha='center', va='bottom', fontsize=11)
        # self.axes2.set_xticklabels(['', '热耗', '分解炉', '窑头', '热效率'])
        # self.axes2.set_ylabel('百分比%')


class MyYijitongMplCanvas(MyMplCanvas):
    def __init__(self, old, new, flag, x_ticklabels):
        for i in range(len(old)):
            old[i] = round(old[i], 2)
        for i in range(len(new)):
            new[i] = round(new[i], 2)
        self.oldValue = old
        self.newValue = new
        self.flag = flag
        self.x_ticklabels = x_ticklabels

        super(MyYijitongMplCanvas, self).__init__()

    def compute_initial_figure(self):
        # data = MyMplCanvas.find_data(self.day, self.hour)

        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
        #
        # x = [0, 1, 2, 3, 4]
        # y = self.real
        # y1 = self.value
        y = self.oldValue
        y1 = self.newValue
        x = range(len(y))
        self.axes.plot(x, y, label='weight changes', linewidth=1, color='r', marker='o',
                       markerfacecolor='blue', markersize=5)
        self.axes.plot(x, y1, label='weight changes', linewidth=1, color='r', marker='^',
                       markerfacecolor='green', markersize=5, linestyle="--")

        self.axes.set_xticklabels(self.x_ticklabels, rotation=15, fontsize=9)
        if self.flag == 0:
            self.axes.set_title('一级筒A温度')
            self.axes.set_ylabel('温度/℃', verticalalignment='center', fontproperties=labelfont)
        elif self.flag == 1:
            self.axes.set_title('一级筒A压强')
            self.axes.set_ylabel('压强/kPa', verticalalignment='center', fontproperties=labelfont)
        elif self.flag == 2:
            self.axes.set_title('一级筒B温度')
            self.axes.set_ylabel('温度/℃', verticalalignment='center', fontproperties=labelfont)
        elif self.flag == 3:
            self.axes.set_title('一级筒B压强')
            self.axes.set_ylabel('压强/kPa', verticalalignment='center', fontproperties=labelfont)

        # self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
        for a, b in zip(x, y):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)
        for a, b in zip(x, y1):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)


class MyYaoMplCanvas(MyMplCanvas):
    def __init__(self, value, real, flag, x_ticklabels):
        self.value = value
        self.real = real
        self.flag = flag
        self.x_ticklabels = x_ticklabels
        super(MyYaoMplCanvas, self).__init__()

    def compute_initial_figure(self):
        # data = MyMplCanvas.find_data(self.day, self.hour)

        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False

        x = [0, 1, 2, 3, 4]
        y = self.real
        y1 = self.value
        self.axes.plot(x, y, label='weight changes', linewidth=1, color='r', marker='o',
                       markerfacecolor='blue', markersize=5)
        self.axes.plot(x, y1, label='weight changes', linewidth=1, color='r', marker='^',
                       markerfacecolor='green', markersize=5, linestyle="--")

        self.axes.set_xticklabels(self.x_ticklabels, rotation=15, fontsize=9)
        if self.flag == 0:
            self.axes.set_title('窑头秤')
        elif self.flag == 1:
            self.axes.set_title('窑尾秤')
        self.axes.set_ylabel('t/h', verticalalignment='center', fontproperties=labelfont)
        # self.axes.set_xlabel('时间/h', verticalalignment='center', fontproperties=labelfont)
        for a, b in zip(x, y):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)
        for a, b in zip(x, y1):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # form = MyVisualDlg()
    # form = MyDataSimDlg('2017012310')
    # form = MyDataInputWnd()
    # form = MyDataLeadInDlg()
    # form = MySysLogDlg()
    # print(filepath + '/' + filename)
    # form = MyStandardDlg()
    # form=MyTimeDlg()
    # form = MyDataReviseWnd()
    # form =MyOpenFileWnd()
    # form2 = MyYaoDlg()
    # form = MyOpenFileWnd()
    # form = MyCheckWnd()
    # form = MyRadioWnd()
    # form = MyProduceWarWnd(20170223, 10)
    form = MyProduceSimWnd(20170223, 10)
    # form=MyDataReviseWnd()
    # form = MyUserManageDlg()
    # form = MyUserSettingDlg()
    # form = MyAddUserDlg()
    app.exec_()
