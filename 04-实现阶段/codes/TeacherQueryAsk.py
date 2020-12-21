import pymysql
import numpy as np

class TeacherQueryAsk():
    """
        方法：queryAskReq(Asklist[id, user_student, user ])
        描述：教师查询学生的申请记录，根据条件，筛选并打印查询结果
        输入：查询申请时所输入的筛选条件
        外部输入：无
        输出：无
        返回：查询结果
        协作类：ApprovalInterface、DB
    """
    @staticmethod
    def queryAskReq(Asklist):
        db = pymysql.connect("localhost","root","root","device_manage" )
        cursor  = db.cursor()
        if(Asklist[0]== '*'):
            querySqlDeviceIdPart = ""
        else:
            querySqlDeviceIdPart = "ask_record.id = %s" % Asklist[0]
        # 学生账号
        if  Asklist[1] == '*'：
            querySqlUserStudentPart = ""
        else：
            querySqlUserStudentPart = "ask_record.user = '%s'" % Asklist[1]
        querySql = "select ask_record.user, ask_record.id, ask_record.date_ask, ask_record.days from (ask_record join device) where '%s' and '%s' and device.manager_user = '%s' and ask_record.id = device.id and is_pass = 'P'" % (querySqlDeviceIdPart, querySqlUserStudentPart, Asklist[2]) # 只选出待处理的进行显示
        data = cursor.fetchall(querySql)
        db.close()
        attribute = np.array(['申请人', '申请设备id','申请日期','审请时间'])
        data = np.array(data)
        if(len(data) == 0):
            return attribute
        else:
            data = np.row_stack((attribute, data))
            return data

