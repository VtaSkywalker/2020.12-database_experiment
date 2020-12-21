
class AddDev():
"""
    方法：addDevReq(Device newDev)
    描述：尝试向数据库中添加设备
    输入：设备信息
    外部输入：无
    输出：无
    返回：添加是否成功
    协作类：AddDevInterface、DB
    负责人： zzr
"""
    @staticmethod
    def addDevReq(devlist):
        sql ="insert into device (device_id, name, deviceType, parameter, date_buy, price, manufactor, warranty_period, bought_by, manager_user, state) value(%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)" % (devlist[0],devlist[1],devlist[2],devlist[3],devlist[4],devlist[5],devlist[6],devlist[7],devlist[8],devlist[9],devlist[10])
        try:
            with db.cursor() as cursor:
                cursor.execute(sql)
                db.commit()
                db.close()
                return True
        except:
            return False

