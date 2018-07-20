import xlrd
import xlwt
from Relation_test import *
import numpy as np
import matplotlib.pyplot as plt


def meihao(rezhi, yaotc, yaowc, shuliao):   #每公斤燃煤产生的熟料量
    results = []
    for i in range(len(rezhi)):
        result = (rezhi[i]/7000)*29307*(yaotc[i]+yaowc[i])/shuliao[i]
        results.append(result)
    return results

def count_meihao():
    filename = '三线总表.xlsx'
    readfile = xlrd.open_workbook(filename)
    readsheet = readfile.sheet_by_name('Sheet3')
    yaotc = readsheet.col_values(7, 1)
    yaowc = readsheet.col_values(8, 1)
    rezhi = readsheet.col_values(62, 1)
    shuliao = readsheet.col_values(64, 1)
    '''
    print(yaotc)
    print(yaowc)
    print(rezhi)
    print(shuliao)
    '''
    biaomeihao = meihao(rezhi, yaotc, yaowc, shuliao)       #每公斤熟料的耗煤量
    print(biaomeihao)
    writefile = xlwt.Workbook()
    writesheet = writefile.add_sheet('Sheet1')
    for i in range(len(biaomeihao)):
        writesheet.write(i, 0, biaomeihao[i])
    writefile.save('biaomeihao.xls')


def meihao_to_youligai():           #计算煤耗和游离钙之间的相关性
    filename = '三线总表.xlsx'
    readfile = xlrd.open_workbook(filename)
    readsheet = readfile.sheet_by_name('Sheet3')
    meihao = readsheet.col_values(6, 1)
    youligai = readsheet.col_values(5, 1)
    for i in range(len(youligai)):
        if youligai[i] != '':
            if youligai[i] > 100:
                youligai[i] = ''
    youligai, meihao = Delete_blank(youligai, meihao)
    cov = np.corrcoef(np.array(meihao), np.array(youligai))
    print(cov)
    #0.08935404
    data_x = [i for i in range(len(youligai))]
    for i in range(len(youligai)):
        if youligai[i]<1.5:
            plt.scatter(data_x[i], meihao[i], color='b')
        else:
            plt.scatter(data_x[i], meihao[i], color='r')
    plt.show()


def youlg_relation():
    filename = '三线总表.xlsx'
    readfile = xlrd.open_workbook(filename)
    readsheet = readfile.sheet_by_name('Sheet3')
    youligai = readsheet.col_values(5, 1)
    for i in range(len(youligai)):
        if youligai[i] != '':
            if youligai[i] > 100:
                youligai[i] = ''
    for j in range(50, 56):
        y = readsheet.col_values(j, 1)
        print(len(y))
        for i in range(len(y)):
            if i == 0:
                continue
            if i == len(y)-1:
                y[i] = y[i-1]
                continue
            if y[i-1] != '' and y[i+1] != '':
                y[i] = y[i-1]

        print(y)
        youligai, y = Delete_blank(youligai, y)
        cov = np.corrcoef(np.array(y), np.array(youligai))
        print(cov)
        # 0.08935404
        data_x = [i for i in range(len(youligai))]
        for i in range(len(youligai)):
            if youligai[i] < 1.5:
                plt.scatter(data_x[i], y[i], color='b')
            else:
                plt.scatter(data_x[i], y[i], color='r')
        plt.show()


def rexiaolv(yaotc, yaowc, shuliao, rezhi, SiO2, Al2O3, Fe2O3 , CaO, MgO):
    result = []
    for i in range(len(yaotc)):
        Mr = (yaotc[i] + yaowc[i]) / shuliao[i]  # 窑头称和窑尾称燃料量(Kg/h)
        Q_netar = (rezhi[i] * 29307) / 7000  # 转化为标煤耗
        Q_rR = Mr * Q_netar

        j = int(i/24)
        Q_sh = 17.19 * Al2O3[j] + 27.1 * MgO[j] + 32.01 * CaO[j] - 21.4 * SiO2[j] - 2.47 * Fe2O3[j]
        print(Q_rR)
        yita_y = Q_sh / Q_rR  # 计算回转窑的热效率
        result.append(yita_y)
    return result


def huizhuanyao_rexiaolv():     #计算回转窑热效率
    filename = '三线总表.xlsx'
    readfile = xlrd.open_workbook(filename)
    readsheet1 = readfile.sheet_by_name('Sheet3')
    readsheet2 = readfile.sheet_by_name('Sheet2')
    '''数据获取'''
    yaotc = readsheet1.col_values(7, 1)
    yaowc = readsheet1.col_values(8, 1)
    rezhi = readsheet1.col_values(62, 1)
    shuliao = readsheet1.col_values(64, 1)
    SiO2, Al2O3, Fe2O3 , CaO, MgO = [readsheet2.col_values(i, 26, 37) for i in range(1, 6)]
    yita_y = rexiaolv(yaotc, yaowc, shuliao, rezhi, SiO2, Al2O3, Fe2O3 , CaO, MgO)
    print(yita_y)
    writefile = xlwt.Workbook()
    writesheet = writefile.add_sheet('Sheet1')
    for i in range(len(yita_y)):
        writesheet.write(i, 0, yita_y[i])
    writefile.save('rexiaolv.xls')


def relation_to_rexiaolv():   #热效率与其他因素的影响
    filename = '三线总表.xlsx'
    readfile = xlrd.open_workbook(filename)
    readsheet = readfile.sheet_by_name('Sheet3')
    rexiaolv = readsheet.col_values(66, 1)          #读取热效率
    yaotc = readsheet.col_values(7, 1)              #读取窑头称
    yaowc = readsheet.col_values(8, 1)              #读取窑尾称
    cov1 = np.corrcoef(np.array(yaotc), np.array(rexiaolv))
    cov2 = np.corrcoef(np.array(yaowc), np.array(rexiaolv))
    Add = []
    for i in range(len(yaotc)):
        Add.append(yaotc[i] + yaowc[i])

    cov3 = np.corrcoef(np.array(Add), np.array(rexiaolv))


    print(cov1)
    print(cov2)
    print(cov3)


    yijitong = readsheet.col_values(10, 1)


    '''画图'''
    x = [i for i in range(len(yaotc))]
    '''
    plt.plot(x, yaotc, color='b')
    plt.plot(x, yaowc, color='g')
    plt.plot(x, Add, color='y')
    '''
    for i in range(len(rexiaolv)):
        rexiaolv[i] = rexiaolv[i] * 100

    plt.plot(x, rexiaolv, color='r')
    yijitong = blank_to_zero(yijitong)
    plt.plot(x, yijitong, color='b')
    plt.show()


def all_relation():     #计算热效率和所有特征的相关性
    filename = '三线总表.xlsx'
    readfile = xlrd.open_workbook(filename)
    readsheet = readfile.sheet_by_name('Sheet3')
    rexiaolv = readsheet.col_values(66, 1)

    name = readsheet.row_values(0, 0)
    length = len(name)
    covs = []
    y = 0
    for i in range(7, length - 1):     #外层循环，遍历每一个特征(除开最后一个特征)
        Others = readsheet.col_values(i, 1)
        print(Others)
        y, Others = Delete_blank(rexiaolv, Others)
        if len(Others) < 10:
            cov = 0
            covs.append(cov)
            continue
        cov = np.corrcoef(y, Others)
        covs.append(cov[0][1])

    writefile = xlwt.Workbook()
    writesheet = writefile.add_sheet('Sheet1')
    for i in range(len(covs)):
        writesheet.write(0, i, abs(covs[i]))

    writefile.save('all_relation_to_rexiaolv.xls')

    return covs


def show_question():        #针对20170302部分数据的异常进行可视化
    filename = '三线总表.xlsx'
    readfile = xlrd.open_workbook(filename)
    readsheet = readfile.sheet_by_name('Sheet4')
    length = len(readsheet.row_values(0, 0))
    for i in range(length):
        data = readsheet.col_values(i, 0)
        x = [i for i in range(len(data))]
        data = standard(data)
        plt.plot(x, data)
    plt.show()


if __name__ == '__main__':
    show_question()

