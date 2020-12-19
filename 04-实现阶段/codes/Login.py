import pymysql

class Login:
    '''
        方法：loginVerify(str user, str password, str type)
        描述：尝试进行登录操作，若成功，返回true，否则返回false
        输入：
            1、用户账号
            2、用户密码
            3、用户类型
        外部输入：无
        输出：无
        返回：登录是否成功
        协作类：LoginInterface、DB
        负责人：caimx
    '''
    @staticmethod
    def loginVerify(user, password, loginType):
        user = "'" + user + "'"
        password = "'" + password + "'"
        try:
            db = pymysql.connect("localhost", "root", "root", "device_manage")
            cursor = db.cursor()
            if(loginType == "Teacher"):
                sql = "select user from teacher where (user = %s) and (password = %s);" % (user, password)
                cursor.execute(sql)
                result = cursor.fetchall()
                if(len(result) == 0):
                    return False
                else:
                    return True
            
            elif(loginType == "Student"):
                sql = "select user from student where (user = %s) and (password = %s);" % (user, password)
                cursor.execute(sql)
                result = cursor.fetchall()
                if(len(result) == 0):
                    return False
                else:
                    return True
            else:
                return False
        except:
            return False