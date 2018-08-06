from pymysql import *


def Connect():      # 连接数据库
    db = connect(host='localhost', user="root", password="123456", db="Program", charset="utf8")
    cursor = db.cursor()
    return cursor


def get_by_hour(time):      # 具体一个小时的数据
    '''
    :param time: 传入数据为字符串形式
    :return:
    '''
    cursor = Connect()
    date = time[:8]
    hour = int(time[8:])
    sql = "SELECT * FROM all_data WHERE date = '%s' and time = '%d'" % (date, hour)
    cursor.execute(sql)
    result = cursor.fetchall()[0]
    result = result[1:]
    name = []
    for x in cursor.description[1:]:
        name.append(x[0])
    # print(name)
    # print(result)
    return name, result


def get_by_day(time):       # 数据库中有ID栏
    cursor = Connect()
    sql = "SELECT * FROM all_data WHERE date = '%s'" % (time)
    cursor.execute(sql)
    data = cursor.fetchall()
    result = []
    for x in data:
        result.append(x[1:])
    name = []
    for x in cursor.description[1:]:
        name.append(x[0])
    return name, result


def get_by_fragment(time_now):
    cursor = Connect()
    '''date = time_now[:8]
    hour = int(time_now[8:]) - 1'''
    date= time_now[:8]
    hour= int(time_now[8:]) - 1
    sql = "SELECT * FROM all_data WHERE date = '%s' and time = '%s'" % (date, hour)
    cursor.execute(sql)
    result = []
    name = []
    for x in cursor.description[1:]:
        name.append(x[0])
    data_now = cursor.fetchall()[0]
    id = data_now[0]
    # print(id)
    result.append(data_now[1:])
    i = 1
    while i != 71 and id - i != 0:
        sql = "SELECT * FROM all_data WHERE ID = '%d'" % (id - i)
        cursor.execute(sql)
        result.append(cursor.fetchall()[0][1:])
        # print(id - i)
        i += 1
    length = len(result)
    T_result = [[] for i in range(length)]
    for i in range(length):
        T_result[length - i - 1] = result[i]
    return T_result, name
    # print(result)


if __name__ == "__main__":
    result, name = get_by_fragment('2017031510')
    print(result)
    print(name)
