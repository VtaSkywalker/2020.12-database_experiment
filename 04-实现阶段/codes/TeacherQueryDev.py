import pymysql
import time
import numpy as np

class TeacherQueryDev():    
    """    
        方法：queryDevReq(Device dev)
        描述：教师查询自己管理的仪器情况，根据条件，筛选并打印查询结果
        输入：查询设备时所输入的筛选条件
        外部输入：无
        输出：无
        返回：查询结果
        协作类：TeacherQueryDevInterface、DB
        负责人：he_pai
    """
    @staticmethod
    def queryDevReq(devlist):
        querySqlDeviceIdPart = "" if ( devlist[0] == "*") else  "device.id = %s and" %devlist[0]
        querySqlNamePart = "" if ( devlist[1] == "*") else  "device.name = '%s' and" %devlist[1]
        querySqlTypePart = "" if ( devlist[2] == "*") else  "device.type = '%s' and" %devlist[2]
        querySqlParameterPart = "" if ( devlist[3] == "*") else  "device.parameter = %s and" %devlist[3]
        querySqlDateBuyPart = "" if ( devlist[4] == "*") else  "device.date_buy = '%s' and" %devlist[4]
        querySqlPricePart = "" if ( devlist[5] == "*") else  "device.price = %s and" %devlist[5]
        querySqlManufactorPart = "" if ( devlist[6] == "*") else  "device.manufactor = '%s' and" %devlist[6]
        querySqlWPPart = "" if ( devlist[7] == "*") else  "device.warranty_period = %s and" %devlist[7]
        querySqlBBPart = "" if ( devlist[8] == "*") else  "device.bought_by = '%s' and" %devlist[8]
        querySqlStatePart = "" if ( devlist[10] == "*") else  "device.state = '%s' and" %devlist[10]
        
        querySqlMUPart =   "device.manager_user = '%s' and" %devlist[9]

        db =pymysql.connect(host="localhost", 
                        user="root", 
                        password="root", 
                        db="device_manage")
        with db.cursor() as cursor:
            sql = "select device.id, device.name, device.type, device.parameter, device.date_buy,device.price,device.manufactor,device.warranty_period,device.bought_by,device.manager_user,device.state from device where %s %s %s %s %s %s %s %s %s %s %s device.state like '%%';" % (querySqlDeviceIdPart, querySqlNamePart, querySqlTypePart, querySqlParameterPart, querySqlDateBuyPart, querySqlPricePart, querySqlManufactorPart, querySqlWPPart, querySqlBBPart, querySqlMUPart, querySqlStatePart)
            cursor.execute(sql)
            data = cursor.fetchall()
        db.close()
        attribute = np.array(['设备id', '设备名称', '设备类型','设备参数','购买日期','价格','生产厂家','保修日期','经办人','管理者编号','设备状态'])
        data = np.array(data)
        if(len(data) == 0):
            return attribute
        else:
            data = np.row_stack((attribute, data))
            return data