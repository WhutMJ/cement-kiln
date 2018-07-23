import xlrd


def get_by_hour(time):
    '''
    :param time: 输入的时间
    :return: 两个数值，变量名和对应数值
    '''
    filename = '三线窑操作记录总表.xlsx'
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

def get_by_day(time):
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


if __name__ == "__main__":
    x, y = get_by_day(20170123)
    for i in range(len(x)):
        print(i)
        print(x[i])

