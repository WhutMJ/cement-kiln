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
    sql = "SELECT * FROM all_data WHERE date = '%s' and time = '%s'" % (date, hour)
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
    result = list(map(list, zip(*result)))
    return name, result[2:]


def get_by_fragment(time_now):
    cursor = Connect()
    date = time_now[:8]
    hour = int(time_now[8:]) - 1
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
        # print(result)
        i += 1
        # print(i)
    length = len(result)
    T_result = [[] for i in range(length)]
    for i in range(length):
        T_result[length - i - 1] = result[i]
    return T_result, name
    # print(result)


def update_data(data):
    db = connect(host='localhost', user="root", password="123456", db="Program", charset="utf8")
    cursor = db.cursor()
    try:
        for x in data:
            date = x[0]
            hour = x[1]
            name, raw_data = get_by_hour(str(date) + str(hour))
            for i in range(len(x)):
                if x[i] != raw_data[i]:
                    sql = "UPDATE all_data SET %s = '%lf' WHERE date = '%s' and time = '%s'" \
                          % (name[i], x[i], date, hour)
                    cursor.execute(sql)
                    db.commit()
        return True
    except Exception as msg:
        print(msg)
        return False


def save_data(data):
    db = connect(host='localhost', user="root", password="123456", db="Program", charset="utf8")
    cursor = db.cursor()
    try:
        sql1 = "SELECT * FROM all_data WHERE ID = 1"
        cursor.execute(sql1)
        information = cursor.description
        name = []
        for x in information:
            name.append(x[0])
        Name = name[1:]
        # print(name)
        for i in range(len(data)):
            # Data = Name + data[i]
            # print(data[i])
            sql = "INSERT INTO all_data(date, time) VALUE('%s', '%s')" % (data[i][0], data[i][1])
            cursor.execute(sql)
            db.commit()
            for j in range(2, len(data[0])):
                if data[i][j] == None:
                    data[i][j] = 0
                sql = "UPDATE all_data SET %s = '%lf' WHERE date = '%s' and time = '%s'"\
                        % (Name[j], data[i][j], data[i][0], data[i][1])
                cursor.execute(sql)
                db.commit()
            '''
            sql = "INSERT INTO all_data(%s for i in range(len(Name))) VALUE('%s' for i in range(len(data[0])))"\
                  % (Data[j] for j in range(len(Data)))
                  '''
        return True
    except Exception as msg:
        print(msg)
        return False

'''
if __name__ == "__main__":

    name, data = get_by_hour('2017031507')
    data = list(data)
    # data[3] = 400
    if save_data([data]):
        print('OK')
    else:
        print('FALSE')
        '''
