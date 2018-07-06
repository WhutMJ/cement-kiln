import pymysql
import xlrd
import numpy as np
from Tools import *
mport xlwt


def Get_Date(filename, n):                  #纵向获取数据
    ReadFile = xlrd.open_workbook(filename)
    FileSheet = ReadFile.sheet_by_name("Sheet1")
    Column = FileSheet.col_values(n, 3)     #除去表头开始
    #print(Column)
    return Column


def blank_to_zero(source):
    result = source
    for i in range(len(source)):
        if source[i] == '':
            result[i] = 0
    return result


def Delete_blank(source1, source2):           #去掉每一列中的空缺值
    '''
    :param source1: the first list
    :param source2: the second list
    :return: the lists that have been dealed with
    '''
    result1 = []
    result2 = []
    for index in range(len(source1)):
        if source1[index] == '' or source2[index] == '':
            continue
        elif source1[index] == 'Y' or source2[index] == 'N':
            continue
        else:
            result1.append(source1[index])
            result2.append(source2[index])

    return result1, result2


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
        test = Get_Date('一线窑操作记录总表.xlsx', i+2)
        test_x.append(test)
    for x in test_x[4]:
        if x != '':
            if x > 100:
                x = ''
    print(test_x[4])
    for i in test_x:
        y, i = Delete_blank(test_x[4], i)
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
        test.append(Get_Date(filename, i))
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
        test.append(Get_Date(filename, i))
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



if __name__ == "__main__":
    Count_relation()
