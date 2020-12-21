import pymysql
import numpy as np

class StudentQueryAsk:
    """
    方法：queryAskReq(str user, int devId, str state)
    描述：学生查询的申请记录，根据条件，筛选并打印查询结果
    输入：
        1、学生账号
        2、设备id
    外部输入：无
    输出：无
    返回：查询结果
    协作类：StudentQueryAskInerface、DB
    负责人：zzr
    """
    @staticmethod
    def queryAskReq(user,devId,state):
        querySqlUserPart = "" if (user == "*") else  "ask_record.user = %s and" % user
        querySqlIdPart   = "" if(devId=="*")else  "ask_record.id = %s" % str(id)
        
        db =pymysql.connect(host="localhost", 
                        user="root", 
                        password="root", 
                        db="device_manage",
                        charset="utf-8")
        with db.cursor() as cursor:
            sql ="select ask_record.device_id, ask_record.date_ask, ask_record.days, ask_record.date_start, ask_record.is_pass from (ask_record join device) where %s %s ask_record.id = device.id" % (querySqlUserPart, querySqlIdPart)
            cursor.execute(sql)
            data = cursor.fetchall()
        db.close()
        attribute = np.array(['设备id', '申请日期', '申请天数','开始使用日期','审核状态'])
        data = np.array(data)
        data = np.row_stack((attribute, data))
        return data

