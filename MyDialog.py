from provide_data_for_gui import *
import config as con
import sys
from youlg_predict import *
from rexiaolv_model import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from numpy import arange
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib


class MyLoginDlg(QDialog):
    login_signal = pyqtSignal(str, str)

    def __init__(self):
        super(MyLoginDlg, self).__init__()
        self.setFixedSize(400,300)  # 72为win10任务栏高度
        self.setWindowTitle('Login')
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(-60, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 90, 192, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFocus()
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(100, 140, 191, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self)

        self.label_3.setGeometry(QtCore.QRect(80, 20, 231, 51))
        self.label_3.setPixmap(QPixmap('picture\\logo.png').scaled(231, 50, aspectRatioMode=Qt.KeepAspectRatio))
        self.label_3.setObjectName("label_3")

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.label.setText("用户名：")
        self.label_2.setText("密码：  ")

    def accept(self):
        self.login_signal.emit(self.lineEdit.text(), self.lineEdit_2.text())

    def reject(self):
        qApp.quit()


class MyDeviceDlg(QDialog):
    yao_par_signal = pyqtSignal(int, str)

    def __init__(self):
        super(MyDeviceDlg, self).__init__()

        self.setWindowTitle('配置设备')
        self.resize(400, 300)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)  # 禁止窗口最大化
        self.setFixedSize(self.width(), self.height())  # 禁止拉伸窗口
        self.lay_ser = QHBoxLayout()
        self.lay_xft = QHBoxLayout()
        self.lay_main = QVBoxLayout()
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
        self.serial_dou.setChecked(True)

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


class MyDataInputDlg(QMainWindow):  # 数据输入功能窗口
    def __init__(self):
        super(MyDataInputDlg, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()
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
        self.Btn_layout.setGeometry(QtCore.QRect(width * 0.7, height * 0.85, 341, 32))
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(0, height * 0.73, width, 16))
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
            col_label.append(name[i])
        self.new_data = []

        self.tableWidget.setHorizontalHeaderLabels(col_label)
        for i in range(len(value)):
            for j in range(self.col_num):
                newItem = QTableWidgetItem(str(value[i][j]))
                self.tableWidget.setItem(i, j, newItem)
                self.tableWidget.item(i, j).setFlags(Qt.ItemIsEnabled)

        newItem = QTableWidgetItem(str(day))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, newItem)
        newItem = QTableWidgetItem(str(hour))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, newItem)

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
                new_row.append('')
        for col in range(2, self.tableWidget.columnCount()):
            item = self.tableWidget.item(self.tableWidget.rowCount() - 1, col)
            item.setBackground(QBrush(QColor(255, 255, 255)))
            try:
                new_row.append(float(item.text()))
            except Exception:
                new_row.append('')
                self.tableWidget.setItem(self.row_num - 1, col, QTableWidgetItem(''))  # 单元格为None无法设置不可编辑

            self.tableWidget.item(self.row_num - 1, col).setFlags(Qt.ItemIsEnabled)

        self.addRow()

        date = int(self.tableWidget.item(self.row_num - 1, 0).text())
        hour = int(self.tableWidget.item(self.row_num - 1, 1).text())

        if hour < 23:
            newItem = QTableWidgetItem(str(date))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, newItem)
            newItem = QTableWidgetItem(str(hour + 1))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, newItem)
        else:
            newItem = QTableWidgetItem(str(date + 1))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, newItem)
            newItem = QTableWidgetItem(str(0))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, newItem)

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
        if save_data(self.new_data):
            reply = QMessageBox.information(self, '提示', '最新数据已经导入，是否自动生成生产预警', QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.warningDlg = MyProduceWarDlg(con.getValue_day(), con.getValue_hour(), 1)

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


class MyDataReviseDlg(QMainWindow):  # 数据修改功能窗口
    def __init__(self):
        super(MyDataReviseDlg, self).__init__()
        metric = QDesktopWidget().screenGeometry()
        width = metric.width()
        height = metric.height()

        self.setObjectName("数据修改")
        self.BtnOk = QPushButton('确认', self)
        self.BtnCancle = QPushButton('取消', self)
        self.BtnOk.clicked.connect(self.accept)
        self.BtnCancle.clicked.connect(self.reject)
        self.Btn_layout = QHBoxLayout()
        self.Btn_layout.addWidget(self.BtnOk)
        self.Btn_layout.addWidget(self.BtnCancle)
        self.Btn_layout.setGeometry(QtCore.QRect(width * 0.7, height * 0.85, 341, 32))

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

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

        day = str(con.getValue_day())
        hour = str(con.getValue_hour())

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
                self.tableWidget.item(i, j).setFlags(Qt.ItemIsEnabled)
            for j in range(2, self.col_num):
                newItem = QTableWidgetItem(str(value[i][j]))
                self.tableWidget.setItem(i, j, newItem)

        self.tableWidget.itemChanged[QTableWidgetItem].connect(self.tableItemChanged)  # 编辑单元格后字体会显示红色
        self.tableWidget.scrollToBottom()
        self.showMaximized()

    def tableItemChanged(self):
        self.tableWidget.currentItem().setForeground(QBrush(QColor(255, 0, 0)))
        self.row_changed.append(self.tableWidget.currentRow())

    def accept(self):

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
        if update_data(self.new_data):
            reply = QMessageBox.information(self, '提示', '修改成功', QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.close()
        else:
            QMessageBox.information(self, '提示', '修改失败', QMessageBox.Yes)

    def reject(self):
        reply = QMessageBox.information(self, '提示', '确认放弃修改？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            pass


class MyProduceWarDlg(QMainWindow):
    def __init__(self, day, hour, number=1):
        super(MyProduceWarDlg, self).__init__()

        self.setWindowTitle('生产预警')
        # 调整窗口显示时的大小
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.pageView = QTabWidget()
        self.tab = {}
        self.pic = {}

        for i in range(number):
            self.tab[i] = QLabel()
            self.pageView.addTab(self.tab[i], '%d小时' % (hour+i))
            self.pic[i] = QVBoxLayout(self.tab[i])
            data = get_by_hour(str(day) + str(hour))
            value = Production_warning_youligai(data[1])
            Ca = MyCaMplCanvas(value)
            self.pic[i].addWidget(QLabel('游离钙合格比'))
            self.pic[i].addWidget(Ca)

            self.line = QtWidgets.QFrame(self)
            self.line.setGeometry(QtCore.QRect(0, QDesktopWidget().screenGeometry().height() * 0.73,
                                               QDesktopWidget().screenGeometry().width(), 16))
            self.line.setFrameShape(QtWidgets.QFrame.HLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.pic[i].addWidget(self.line)

            value = Production_warning_rexiaolv(data[1])
            Effic = MyEfficMpCanvas(value)
            self.pic[i].addWidget(QLabel('热效率分析'))
            self.pic[i].addWidget(Effic)
            self.line2 = QtWidgets.QFrame(self)
            self.line2.setGeometry(QtCore.QRect(0, QDesktopWidget().screenGeometry().height() * 0.73,
                                               QDesktopWidget().screenGeometry().width(), 16))
            self.line2.setFrameShape(QtWidgets.QFrame.HLine)
            self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.pic[i].addWidget(self.line2)
            Coal = MyCoalMpCanvas(value)
            self.pic[i].addWidget(Coal)

        # 设置将self.pageView为中心Widget
        self.setCentralWidget(self.pageView)
        self.show()


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
        Percentage = [30, 70]  # 前者为合格，后者为不合格
        Percentage[0] = self.value[1] * 100
        Percentage[1] = self.value[0] * 100
        self.axes.barh(range(2), Percentage, height=0.7, color='steelblue', alpha=0.8)
        self.axes.set_yticks(range(2))
        self.axes.set_yticklabels(['合格', '不合格'])
        self.axes.set_xlim(0, 100)
        self.axes.set_xlabel('百分比 %')
        self.axes.set_title('游离钙是否合格的百分比')

        for x, y, in zip(Percentage, range(2)):
            self.axes.text(x + 5, y, '%.2f' % x, ha='right', va='center', fontsize=10)


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
    def __init__(self, date):
        super(MyCoalMpCanvas, self).__init__()
        self.compute_initial_figure()

    def compute_initial_figure(self):
        #        data = self.find_data(self.day, self.hour)  # 和上面的data相同

        # consumption       利用data求出煤耗
        consumption = 60

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # form = MyDataReviseDlg()
    form = MyProduceWarDlg(20170315, 2)
    form.show()
    app.exec_()
