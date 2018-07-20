import xlrd
import xlwt
from Tools import *

def count_shuliao():
    filename = '三线总表.xlsx'
    readfile = xlrd.open_workbook(filename)
    readsheet = readfile.sheet_by_name('Sheet1')
    shengliao = readsheet.col_values(2, 1)
    shengliao = blank_to_zero(shengliao)
    shuliao = []
    for x in shengliao:
        shuliao.append(x/1.578)
    writefile = xlwt.Workbook()
    sheet1 = writefile.add_sheet('Sheet1')
    for i in range(len(shuliao)):
        sheet1.write(i, 0, shuliao[i])
    writefile.save('shuliao.xls')
    print(shuliao)

if __name__ == '__main__':
    count_shuliao()