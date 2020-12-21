import pymysql
import numpy as np

class FixDev():    
    """    
        方法：fixDevReq(fixlist[str user, int devId, int mode, Date date, str reason])
        描述：更改数据库中的仪器的状态为维修/报废
        输入：
            1、教师用户名
            2、设备id
            3、报修模式（0：维修，1：报废）
            4、报修日期
            5、原因
        外部输入：无
        输出：无
        返回：修改数据库是否成功
        协作类：FixDevInterface、DB
        负责人：zzr
    """
    @staticmethod
    def fixDevReq(fixlist):
        db = pymysql.connect("localhost","root","root","device_manage" )
        sql="select state from device where id = %s" % fixlist[1]
        cursor = db.cursor()
        if fixlist[2] == 0:
            fixMode = "维修"
        elif fixlist[2]  == 1:
            fixMode = "报废"
        cursor.execute(sql) # 如果原来的状态已经是维修或报废，则无法再报修一次
        orgState = cursor.fetchone()
        orgState = np.array(orgState)
        if(len(orgState) == 0): # 没有找到相关记录
            return False
        if orgState[0] == "维修" or orgState[0] == "报废":
            return False
        deviceSql = "update device set state = '%s' where id = %s" % (fixMode, fixlist[1])
        fixRecordSql = "insert into fix_record value('%s', %s, '%s', '%s')" % (fixlist[0], fixlist[1], fixlist[3], fixlist[4])
        try:
            cursor.execute(deviceSql)
            db.commit()
            cursor.execute(fixRecordSql)
            db.commit()
            db.close()
            return True
        except:
            db.close()
            return False
