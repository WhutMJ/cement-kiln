import xlrd
import xlwt
from xlutils.copy import copy
import numpy as np


def reshape_data(source_filename):
    source_readfile = xlrd.open_workbook(source_filename)
    sourcesheet = source_readfile.sheet_by_index(0)
    source_table_name = sourcesheet.row_values(0, 0)        #获取用户文件的表头

    standard_file = xlrd.open_workbook('总数据.xlsx')
    standardsheet = standard_file.sheet_by_name('Sheet1')
    standard_table_name = standardsheet.row_values(0, 0)

    new_table_value = [[] for i in range(len(standard_table_name))]

    for i in range(len(standard_table_name)):
        lable = 0
        for j in range(len(source_table_name)):
            if standard_table_name[i] == source_table_name[j]:
                table_value = sourcesheet.col_values(j, 1)
                new_table_value[i] = table_value
                lable = 1
                break
        if lable == 0:
            new_table_value[i] = ['' for x in range(len(standardsheet.col_values(0, 1)))]

    new_file = xlwt.Workbook()
    newsheet = new_file.add_sheet('Sheet1')
    for i in range(len(standard_table_name)):
        newsheet.write(0, i, standard_table_name[i])
    for i in range(len(standard_table_name)):
        for j in range(len(new_table_value[i])):
            newsheet.write(j+1, i, new_table_value[i][j])
    new_file.save('Datafile_From_C\\test_table.xls')

def get_by_hour(time):          #获取具体一小时的横向数据
    '''
    :param time: 输入的时间
    :return: 两个数值，变量名和对应数值
    '''
    filename = '总数据.xlsx'
    readfile = xlrd.open_workbook(filename)
    read_sheet = readfile.sheet_by_name('Sheet1')
    table_data = read_sheet.col_values(0, 1)
    index = 0
    for data in table_data:
        if data == time:
            index = table_data.index(data)
            break
    table_value = read_sheet.row_values(index+2, 2)
    table_name = read_sheet.row_values(0, 2)
    for i in range(len(table_value)):
        if table_value[i] == '':
            table_value[i] = 'null'
    return table_name, table_value


def get_by_day(time):              #获取一天的二维数组的数据
    filename = '三线窑操作记录总表.xlsx'
    readfile = xlrd.open_workbook(filename)
    read_sheet = readfile.sheet_by_name('Sheet1')
    table_data = read_sheet.col_values(0, 1)
    index = 0
    for data in table_data:
        if data == time:
            index = table_data.index(data)
            break
    table_name = read_sheet.row_values(0, 2)
    table_value = []
    for i in range(len(table_name)):
        x = read_sheet.col_values(i+2, index+1, index+25)
        for j in range(len(x)):
            if x[j] == '':
                x[j] = 'null'
        table_value.append(x)
    return table_name, table_value


def get_by_fragment(time_now):  # 按片段获取
    filename = '总数据.xlsx'
    readfile = xlrd.open_workbook(filename)
    read_sheet = readfile.sheet_by_name('Sheet1')

    data_name = read_sheet.row_values(0, 0)
    #data_length = len(data_name)
    date = int(time_now[:8])
    hour = int(time_now[8:])
    '''date=20170123
    hour=9'''
    raw_date = read_sheet.col_values(0, 0)
    index = 1
    while raw_date[index] != date:
        index += 1
    index += hour - 1
    time_limit = 72
    if index < 71:
        time_limit = index
    result_data = [0 for i in range(time_limit)]

    for i in range(time_limit):
        result_data[time_limit - i - 1] = read_sheet.row_values(index, 0)
        result_data[time_limit - i - 1][:2] = [int(result_data[time_limit - i - 1][j]) for j in range(2)]
        index -= 1

    return result_data,data_name


def save_data(data):
    '''
    :param data: [[a1, b1, c1, ...], [a2, b2, c2, ...], ...]
    '''
    number = len(data)              #获取数据的条数

    filename = '总数据.xls'
    readfile = xlrd.open_workbook(filename)
    read_sheet = readfile.sheet_by_name('Sheet1')
    newb = copy(readfile)
    write_sheet = newb.get_sheet(0)
    date_value = read_sheet.col_values(0, 0)
    length = len(date_value)
    try:
        data_length = len(data[0])
    except Exception:
        return '输入格式有误'
    for i in range(number):
        for j in range(data_length):
            write_sheet.write(length+i, j, data[i][j])
    try:
        newb.save('总数据.xls')
        return True
    except Exception:
        return False

def update_data(data):
    filename = '总数据.xls'
    readfile = xlrd.open_workbook(filename)
    read_sheet = readfile.sheet_by_name('Sheet1')
    newb = copy(readfile)
    write_sheet = newb.get_sheet(0)
    date = data[0][0]
    hour = data[0][1]
    date_value = read_sheet.col_values(0, 0)
    index = 1
    while date_value[index] != date:
        index += 1
    index += hour           #获得现在更改的起始位置

    length = len(data)
    data_length = len(data[0])
    for i in range(length):
        for j in range(data_length):
            write_sheet.write(index+i, j, data[i][j])
    newb.save('总数据.xls')

if __name__ == "__main__":
    data = get_by_hour('20170223')[1]
    print(data)
    date = [20170316, 0]
    data = date + data
    save_data(data)