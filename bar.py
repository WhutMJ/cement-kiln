## 条形图

# coding=gbk
import matplotlib.pyplot as plt
import xlrd
import numpy as np

# data = xlrd.open_workbook('一线窑操作记录总表 .xlsx')#打开excel文件
data = xlrd.open_workbook('三线窑操作记录总表.xlsx')#打开excel文件
table = data.sheets()[0]
ncols = table.ncols-1               #列数
nrows = table.nrows-3               #行数
dates = table.col_values(0,3)       #读取所有的日期数据

# 一线表头
#names =['CaO','Fe2O3','立升重','游离钙','w01S01rpm','v72s01','v82f01','窑体温度','预热器1顶部压强','预热器1温度','预热器1底部压强','预热器2顶部压强', '预热器2温度', '预热器2底部压强',  '预热器3顶部压强', '预热器3温度', '预热器3底部压强',  '预热器4顶部压强', '预热器4温度', '预热器4底部压强',  '预热器5顶部压强', '预热器5温度', '预热器6温度','烟室W01P01', '烟室W01A01','烟室W01T01','v91','w1','电收进口阀门','篦冷机k02', '篦冷机k01', '篦冷机k11', '篦冷机k12', '篦冷机k13','三次风管','高温风机J01','高温风管J02','温度']

#三线表头
names =['喂料秤', '入窑生料CaO', '入窑生料Fe2O3', '游离钙', '窑速', '窑头秤', '窑尾秤', '筒体温度', '一级桶140C1AT1', '一级桶140C1AP1', '一级桶140C1BT1', '一级桶140C1BP1',  '二级桶140C2AT1', '二级桶140C2AP1', '二级桶140C2BT1', '二级桶140C2BP1',  '三级桶140C3AT1', '三级桶140C3AP1', '三级桶140C3BT1', '三级桶140C3BP1',  '四级桶140C4AT1', '四级桶140C4AP1', '四级桶140C4BT1', '四级桶140C4BP1',  '五级桶140C5AT1', '五级桶140C5AP1', '五级桶140C5BT1', '五级桶140C5BP1',  '窑尾温度', '篦冷机一段压力', '篦冷机一段S1', '篦冷机一段I1',  '篦冷机二段S1', '篦冷机二段I1',  '篦冷机三段S1', '篦冷机三段I1',  '三次风压力', '高温风机转速', '高温风机电流']

for i in range(2,ncols):
    y1 = table.col_values(i, 3)
    plt.figure(i-2)
    #plt.title(table.cell(i,2).value)
    plt.bar(dates, y1, alpha=0.5)
    plt.savefig(names[i-2]+'.jpg')


y1 = table.col_values(3, 3)
plt.bar(dates, y1, alpha=0.5)

print(dates)
plt.show()
