import pymysql
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
            with db.cursor() as cursor:
                sql ="update device set state = ‘空闲’ where id=%s" % (devId)
                cursor.execute(sql)
                db.commit()
                return flag
        except:
            flag= False
            return flag

            
        

