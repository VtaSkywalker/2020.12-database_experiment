import pymysql
import numpy as np
class StudentQueryDev():
"""
    方法：queryDevReq(Device dev)
    描述：学生查询自己全部仪器情况，根据条件，筛选并打印查询结果
    输入：查询设备时所输入的筛选条件
    外部输入：无
    输出：无
    返回：查询结果
    协作类：StudentQueryDevInterface、DB
    负责人：zzr
"""
    @staticmethod
    def queryDevReq(devlist):
        querySqlDeviceIdPart = "" if ( device[0] == "*") else  "device.id = %d and" %device[0]
        querySqlNamePart = "" if ( devlist[1] == "*") else  "device.name = %s and" %device[1]
        querySqlTypePart = "" if ( devlist[2] == "*") else  "device.type = %s and" %device[2]
        querySqlParameterPart = "" if ( devlist[3] == "*") else  "device.parameter = %f and" %device[3]
        querySqlDateBuyPart = "" if ( devlist[4] == "*") else  "device.data_buy = %s and" %device[4]
        querySqlPricePart = "" if ( devlist[5] == "*") else  "device.price = %f and" %device[5]
        querySqlManufactorPart = "" if ( devlist[6] == "*") else  "device.manufactor = %s and" %device[6]
        querySqlWPPart = "" if ( devlist[7] == "*") else  "device.warranty_period = %d and" %device[7]
        querySqlBBPart = "" if ( devlist[8] == "*") else  "device.bought_by = %s and" %device[8]
        querySqlMUPart = "" if ( devlist[9] == "*") else  "device.manage_user = %s and" %device[9]
        querySqlStatePart = "" if ( devlist[10] == "*") else  "device.state = %s " %device[10]
        
        db =pymysql.connect(host="localhost", 
                        user="root", 
                        password="root", 
                        db="device_manage")
        with db.cursor() as cursor:
            sql ="select device.id, device.name, device.type, device.parameter, device.data_buy,device.price,device.manufactor,device.warranty_period,device.bought_by,device.manage_user,device.state  from device where %s %s %s %s %s %s %s %s %s %s %s" % (querySqlDeviceIdPart,querySqlNamePart,querySqlTypePart,querySqlParameterPart,querySqlDateBuyPart,querySqlPricePart,querySqlManufactorPart,querySqlWPPart,querySqlBBPart,querySqlMUPart,querySqlStatePart)
            cursor.execute(sql)
            data = cursor.fetchall()
        db.close()
        attribute = np.array(['设备id', '设备名称', '设备类型','设备参数','购买日期','价格','生产厂家','保修日期','经办人','管理者编号','设备状态'])
        data = np.array(data)
        data = np.row_stack((attribute, data))
        return data

