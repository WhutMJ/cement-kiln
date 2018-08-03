from pymysql import *

'''
if __name__ == '__main__':
    db = connect(host='localhost', user="root", password="", db="sys", charset="utf8")
    cursor = db.cursor()
    sql = "SELECT * FROM sys_config "
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    '''


def Login_test(username, password):
    db = connect(host='localhost', user="root", password="123456", db="Program", charset="utf8")
    cursor = db.cursor()
    sql1 = "SELECT Username FROM User_info"
    cursor.execute(sql1)
    result = cursor.fetchall()
    for x in result:
        if x[0] == username:
            sql2 = "SELECT Password FROM User_info WHERE Username = '%s'"%(username)
            cursor.execute(sql2)
            real_password = cursor.fetchall()[0][0]
            if password == real_password:
                return True
    return False
    #print(result)

'''
if __name__ == "__main__":
    if Login_test('moujun', '12346'):
        print('登录成功')
    else:
        print('登录失败')
        '''
