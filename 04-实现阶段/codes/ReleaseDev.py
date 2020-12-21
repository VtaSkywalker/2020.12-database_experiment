import pymysql
import numpy as np

class ReleaseDev():

    """
     方法：releaseDevReq(int devId)
        描述：学生释放设备，使设备状态回到"空闲"
        输入：设备id
        外部输入：无
        输出：无
        返回：释放是否成功
        协作类：StudentQueryAskInerface、DB
        负责人：zzr
    """
    @staticmethod
    def releaseDevReq(devId):
        flag= True
        try:
            db = pymysql.connect("localhost", "root", "root", "device_manage")
            with db.cursor() as cursor:
                cursor.execute("select state from device where id = %s;" % devId)
                state = cursor.fetchall()
                state = np.array(state)
                if(len(state) == 0): # 如果未搜索到
                    return False
                if(state[0][0] != '使用中'):
                    return False
                sql ="update device set state = '空闲' where id = %s;" % (devId)
                cursor.execute(sql)
                db.commit()
                return flag
        except:
            flag= False
            return flag
