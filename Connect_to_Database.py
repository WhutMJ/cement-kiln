from pymysql import *
import config as con

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
    db = connect(host='localhost', user="root", password=con.password, db="Program", charset="utf8")
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

def Update_User(username, old_password, new_password):
    '''
    :param username: 用户名
    :param old_password: 旧密码
    :param new_password: 新密码
    :return:
    '''
    db = connect(host='localhost', user="root", password=con.password, db="Program", charset="utf8")
    cursor = db.cursor()
    sql = "SELECT password FROM user_info WHERE username = '%s'" % (username)
    if cursor.execute(sql):
        password = cursor.fetchone()[0]
        # print(password)
        if password == old_password:
            try:
                sql = "UPDATE user_info SET password = '%s' WHERE username = '%s'" % (new_password, username)
                cursor.execute(sql)
                db.commit()
                return True
            except Exception:
                return 'MySQL_ERROR!'
        else:
            return 'Old_Password_ERROR!'
    else:
        return 'Not_Found__'+username


def Add_User(username, password, Identity):
    '''
    :param username: 用户名
    :param password: 密码
    :param Identity: 身份
    :return:
    '''
    db = connect(host='localhost', user="root", password=con.password, db="Program", charset="utf8")
    cursor = db.cursor()
    sql = "SELECT ID FROM user_info WHERE username = '%s'" % (username)
    if not cursor.execute(sql):
        try:
            sql = "SELECT ID FROM user_info"
            cursor.execute(sql)
            ID = cursor.fetchall()[-1][0] + 1      # 获取最后一个ID，并加一
            sql = "INSERT INTO user_info(ID, username, password, Identity) VALUE('%d', '%s', '%s', '%s')"\
                        % (ID, username, password, Identity)
            cursor.execute(sql)
            db.commit()
            return True
        except Exception as msg:
            print(msg)
            return 'MySQL_ERROR!'
    else:
        return 'Username_Existed!'
def Delete_User(operator, username):
    db = connect(host='localhost', user="root", password=con.password, db="Program", charset="utf8")
    cursor = db.cursor()
    sql = "SELECT Identity FROM user_info WHERE username = '%s'" % (operator)
    cursor.execute(sql)
    identity_1 = cursor.fetchone()[0]
    if identity_1 == 'Top_administrator':
        sql = "SELECT Identity From user_info WHERE username = '%s'" % (username)
        cursor.execute(sql)
        identity_2 = cursor.fetchone()[0]
        if not identity_2 == 'Top_administrator':
            sql = "DELETE FROM user_info WHERE username = '%s'" % (username)
            cursor.execute(sql)
            db.commit()
            return True
        else:
            return "Sorry, you don't have permission!"
    else:
        return "Can't delete!"


def show_all_user(operator):
    db = connect(host='localhost', user="root", password=con.password, db="Program", charset="utf8")
    cursor = db.cursor()
    sql = "SELECT Identity FROM user_info WHERE username = '%s'" % (operator)
    cursor.execute(sql)
    identity = cursor.fetchone()[0]
    if identity == 'Top_administrator':
        sql = "SELECT username, Identity FROM user_info"
        cursor.execute(sql)
        result = cursor.fetchall()
        return True, result
    else:
        return False, "Sorry, you don't have permission!"
def Update_Identity(operator, username, Identity):
    '''
    :param operator: 操作者
    :param username: 被操作者的用户名
    :param Identity: 新的身份
    :return:
    '''
    db = connect(host='localhost', user="root", password=con.password, db="Program", charset="utf8")
    cursor = db.cursor()
    sql = "SELECT Identity FROM user_info WHERE username = '%s'" % (operator)
    cursor.execute(sql)
    identity_1 = cursor.fetchone()[0]
    if identity_1 == 'Top_administrator':
        sql = "SELECT Identity From user_info WHERE username = '%s'" % (username)
        cursor.execute(sql)
        identity_2 = cursor.fetchone()[0]
        if not identity_2 == 'Top_administrator':
            sql = "UPDATE user_info SET Identity = '%s' WHERE username = '%s'"\
                    % (Identity, username)
            try:
                cursor.execute(sql)
                db.commit()
                return True
            except Exception:
                return 'MySQL_ERROR!'
        else:
            return "Sorry, you don't have permission!"
    else:
        return "You can't Update!"

'''
if __name__ == "__main__":
    if Login_test('moujun', '12346'):
        print('登录成功')
    else:
        print('登录失败')
        '''
