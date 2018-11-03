'''以下为窑系统所需的全局变量的获取与设置'''
from PyQt5.QtWidgets import QDesktopWidget

global day, index_T, index_P, flag_Ser, number, filepath, flag_Visual
#     日期， 温度，压强，  单双系列标志，旋风筒数,文件路径,热耗可视化标志
global hour, flag_Hour, password, username, flag_Ctrl, metric, hours
#                                           判断是否按住了Ctrl键

day = 0
index_T = []
index_P = []
flag_Ser = 0
number = 0
filepath = ''
flag_Visual = 0  # 为 0 则表示以天显示，为 1 则以小时显示
hour = 0
hours = []      #存储一天所有有数据的hour的集合
flag_Hour = 0
password = '123456'
flag_Ctrl = 0  # 没有按下


def getValue_flag_Ctrl():
    return flag_Ctrl


def setValue_flag_Ctrl(value):
    global flag_Ctrl
    flag_Ctrl = value


def getValue_username():
    return username


def setValue_username(value):
    global username
    username = value


def getValue_filepath():
    return filepath


def setValue_filepath(value):
    global filepath
    filepath = value


def getValue_day():
    return day


def setValue_day(value):
    global day
    day = value


'''def getValue_flag_Time():
    return flag_Time


def setValue_flag_Time(value):
    global flag_Time
    flag_Time = value'''


def getValue_flag_Hour():
    return flag_Hour


def setValue_flag_Hour(value):
    global flag_Hour
    flag_Hour = value


def getValue_index_T():
    return index_T


def setValue_index_T(value):
    global index_T
    if getValue_flag_Ctrl() == 0:
        index_T = []
        index_T.append(value)
    else:
        if value in index_T:
            index_T.remove(value)
        else:
            index_T.append(value)


def getValue_index_P():
    return index_P


def setValue_index_P(value):
    global index_P
    if getValue_flag_Ctrl() == 0:
        index_P = []
        index_P.append(value)
    else:
        if value in index_P:
            index_P.remove(value)
        else:
            index_P.append(value)


def getValue_flag_Ser():
    return flag_Ser


def setValue_flag_Ser(value):
    global flag_Ser
    flag_Ser = value


def getValue_number():
    return number


def setValue_number(value):
    global number
    number = value


def getValue_flag_Visual():
    return flag_Visual


def setValue_flag_Visual(value):
    global flag_Visual
    flag_Visual = value


def getValue_hour():
    return hour


def setValue_hour(value):
    global hour
    hour = value

def getValue_hours():
    return hours


def setValue_hours(value):
    global hours
    hours = value