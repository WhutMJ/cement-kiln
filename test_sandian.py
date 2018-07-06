# -*- coding: utf-8 -*--
import matplotlib.pyplot as plt
import numpy as np
from Relation_test import *
from Tools import *

if __name__ == "__main__":
    filename = '三线窑操作记录总表.xlsx'
    Namefile = xlrd.open_workbook(filename)
    namesheet = Namefile.sheet_by_name('Sheet1')
    name = namesheet.row_values(0, 2)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示坐标轴负号
    '''
    输出仅有均值和散点的图
    for i in range(44):
        data_y = Get_Date(filename, i+2)
        print(data_y)
        average = tongjl().Average(data_y)
        Fangc = tongjl().Fangc(data_y)
        data_y = blank_to_zero(data_y)          #数据显示时空白数据清零
        data_x = [i for i in range(len(data_y))]
        plt.scatter(data_x, data_y)
        plt.plot(data_x, [average for i in range(len(data_y))], color='r')
        #plt.plot(data_x, [average-Fangc for i in range(len(data_y))])
        #plt.plot(data_x, [average+Fangc for i in range(len(data_y))])
        #plt.savefig('%s'%i + '.jpg')
        plt.title(name[i])
        plt.show()
    '''

    '''
    输出有均值，以及正太分布区间的三点图
    '''
    for i in range(44):
        data_y = Get_Date(filename, i+2)
        print(data_y)
        average = tongjl().Average(data_y)
        biaozc = tongjl().Biaozc(data_y)
        print(biaozc)
        data_y = blank_to_zero(data_y)
        data_x = [i for i in range(len(data_y))]
        plt.scatter(data_x, data_y)
        plt.plot(data_x, [average for i in range(len(data_y))], color='r')
        plt.plot(data_x, [average - biaozc for i in range(len(data_y))], color='y')
        plt.plot(data_x, [average + biaozc for i in range(len(data_y))], color='y')
        plt.title(name[i])
        plt.show()