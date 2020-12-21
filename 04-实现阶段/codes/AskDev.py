import pymysql
import time

class AskDev():
    """
        方法：askDevReq(str user, int devId, int days)
        描述：处理学生申请设备的请求
        输入：查询设备时所输入的筛选条件
        外部输入：
            1、学生用户名
            2、设备id
            3、申请使用天数
        输出：无
        返回：申请是否有效
        协作类：StudentQueryDevInerface、DB
        负责人：zzr
    """
    @staticmethod
    def askDevReq(user,devId,days):
        db = pymysql.connect("localhost", "root", "root", "device_manage")
        with db.cursor() as cursor:
            try:
                sql ="select state from device   where  id = %s " % (devId)
                cursor.execute(sql)
                state = cursor.fetchone()
                if(state[0] == "空闲"):
                    addAskRecordSql = "insert into ask_record(student_user, device_id, date_ask, days) values('%s', %s, '%s', %s)" % (user, devId, time.strftime("%Y-%m-%d", time.localtime()), str(days)) # 增加一条申请
                    cursor.execute(addAskRecordSql)
                    db.commit()
                    db.close()
                    return True
                else:
                    return False
            except:
                db.close()
                return False