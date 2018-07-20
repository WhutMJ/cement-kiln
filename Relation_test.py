import pymysql
import xlrd
import numpy as np
from Tools import *
import xlwt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import *
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange


def Get_Data(filename, n):                  #纵向获取数据
    ReadFile = xlrd.open_workbook(filename)
    FileSheet = ReadFile.sheet_by_name("Sheet1")
    Column = FileSheet.col_values(n, 1)     #除去表头开始
    #print(Column)
    return Column


def standard(data):                     #标准化
    average = tongjl().Average(data)
    s = tongjl().Biaozc(data)
    result = []
    for x in data:
        y = (x-average)/s
        result.append(y)
    return result


def Count_relation():                   #计算相关性
    test_x = []
    cov = []
    for i in range(43):
        test = Get_Data('三线窑操作记录总表.xlsx', i+2)
        test_x.append(test)
    for x in test_x[3]:
        if x != '':
            if x > 100:
                x = ''
    print(test_x[3])
    for i in test_x:
        y, i = Delete_blank(test_x[3], i)
        if(len(i) < 10):
            continue
        #y = standard(y)
        #i = standard(i)
        try:
            covs = np.corrcoef(np.array(y), np.array(i))
            cov.append(covs)
            print(covs)
        except Exception:
            print('error')

    WriteFile = xlwt.Workbook()
    Sheet1 = WriteFile.add_sheet('Sheet1')
    cov_value = []
    for x in cov:
        cov_value.append(abs(x[0][1]))
    Sort_value = sort(cov_value)
    i = 0
    for x in cov:
        Sheet1.write(0, i, abs(x[0][1]))
        Sheet1.write(1, i, Sort_value[i])
        i += 1
    WriteFile.save('relation2.xls')


def Count_Hurt1():                      #计算三线窑中每一行的温度

    #存储最后温度列表的文件创建操作
    WriteFile = xlwt.Workbook()
    Sheet1 = WriteFile.add_sheet('Sheet1')


    index = [9, 10, 12, 14, 16, 20, 26, 28, 30, 31]      #三线窑中对应有温度的下标、
    filename = '三线窑操作记录总表.xlsx'
    test = []
    Average = []                       #存放每一个时间点对应的温度均值
    length = len(index)             #列数
    print(length)
    for i in index:
        test.append(Get_Data(filename, i))
    for i in range(len(test[0])):
        number = length                 #设置初始每一个时间点可计算的温度的个数
        sum = 0                         #初始化温度总和为0
        for j in range(length):
            if test[j][i] == '':        #如果横向某个温度点为空
                number -= 1
            else:
                sum += test[j][i]
        if number > 0:
            average = sum/number
        else:
            average = 0
        Average.append(average)
        Sheet1.write(i, 0, average)
    WriteFile.save('heat.xls')
    print(Average)


def Count_Hurt2():              #计算一线窑每行对应的温度

    #存储最后温度列表的文件创建操作
    WriteFile = xlwt.Workbook()
    Sheet1 = WriteFile.add_sheet('Sheet1')
    index = [10, 12, 15, 18, 21, 23, 25, 26, 29]      #一线窑中对应有温度的下标、
    filename = '一线窑操作记录总表.xlsx'
    test = []
    Average = []                       #存放每一个时间点对应的温度均值
    length = len(index)             #列数
    for i in index:
        test.append(Get_Data(filename, i))
    for i in range(len(test[0])):
        number = length                 #设置初始每一个时间点可计算的温度的个数
        sum = 0                         #初始化温度总和为0
        for j in range(length):
            if test[j][i] == '':        #如果横向某个温度点为空
                number -= 1
            else:
                sum += test[j][i]
        if number > 0:
            average = sum/number
        else:
            average = 0
        Average.append(average)
        Sheet1.write(i, 0, average)
    WriteFile.save('heat2.xls')
    print(Average)


def sort(data):                     #为列表中的每个数据根据排序编号
    length = len(data)
    result = [-1 for i in range(length)]
    bVisit = [-1 for i in range(length)]
    for j in range(length):
        Max = 0
        Max_index = 0
        for i in range(length):
            if data[i] > Max and bVisit[i] == -1:
                Max_index = i
                Max = data[i]
        bVisit[Max_index] = 0
        result[Max_index] = j+1
    return result


def Line_regression():
    filename = '三线窑操作记录总表.xlsx'
    work = xlrd.open_workbook(filename)
    sheet1 = work.sheet_by_name('Sheet1')

    x_train = sheet1.col_values(10, 1)
    y_train = sheet1.col_values(11, 1)
    x_test = sheet1.col_values(12, 1)
    y_test = sheet1.col_values(13, 1)
    x_train, y_train = Delete_blank(x_train, y_train)
    x_test, y_test = Delete_blank(x_test, y_test)

    x_train = np.array(x_train)[:, np.newaxis]
    x_test = np.array(x_test)[:, np.newaxis]
    y_train = np.array(y_train)
    lr = LinearRegression()
    pr = LinearRegression()
    quadratic = PolynomialFeatures(degree=2)
    #X_quad = quadratic.fit_transform(x)

    lr.fit(x_train, y_train)
    y_fit = lr.predict(x_test)
    score = lr.score(x_test, y_test)
    print(score)

    return y_test, y_fit


def all_relation():
    test_x = []
    for i in range(44):
        test = Get_Data('三线窑操作记录总表.xlsx', i + 2)
        test_x.append(test)
    cov_value = []
    for n in range(44):
        cov = []
        if n == 3:                      #若被分析列为游离钙
            for x in test_x[n]:
                if x != '':
                    if x > 100:
                        x = ''
        #print(test_x[n])
        if len(test_x[n]) < 10:
            cov = [0 for i in range(len(test_x))]
            continue
        for i in test_x:
            y, x = Delete_blank(test_x[n], i)
            if len(x) < 10:
                covs = 0
                cov.append(covs)
                continue
            # y = standard(y)
            # i = standard(i)
            try:
                covs = np.corrcoef(np.array(y), np.array(x))
                cov.append(covs)
                #print(covs)
            except Exception:
                print('error')
        cov_value.append(cov)
        #print(cov)
    WriteFile = xlwt.Workbook()
    Sheet1 = WriteFile.add_sheet('Sheet1')
    for n in range(45):
        print(n)
        i = 0
        print(cov_value[n])
        for x in cov_value[n]:
            try:
                Sheet1.write(n, i, abs(x[0][1]))
            except TypeError:
                Sheet1.write(n, i, 0)
            i += 1
    WriteFile.save('relation2.xls')


if __name__ == "__main__":
    all_relation()
    '''
    y1, y2 = Line_regression()
    x = [i for i in range(len(y1))]
    plt.plot(x, y1, color='r')
    plt.plot(x, y2, color='b')
    plt.show()
    '''
