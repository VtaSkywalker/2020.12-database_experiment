import pymysql
class Approval():
    """
        方法：approvalReq(str user, int devId, boolean op)
        描述：审批请求，同意或拒绝。将相应更改写入到数据库
        输入：
            1、学生用户名
            2、设备id
            3、审核结果
        外部输入：无
        输出：无
        返回：审批操作是否成功
        协作类：ApprovalInterface、DB
        负责人：zzr
    """
    @staticmethod
    def approvalReq(user,devId,op):
        db = pymysql.connect("localhost","root","root","device_manage" )
        cursor = db.cursor()
        #教师拒绝更新的情况
        if op == False:
            try:
                sql="update ask_record set is_pass ='N' where student_user = '%s' and device_id = %s" % (user, devId)
                cursor.execute(sql)
                db.commit()
                db.close()
                return True
            except:
                db.close()
                return False
                #教师同意更新的情况
        elif op == True:
            agreeSql = "update ask_record set is_pass = 'Y' where student_user = '%s' and device_id = %s" % (user, devId) #修改相应的请求记录为同意
            rejectSql = "update ask_record set is_pass = 'N' where student_user <> '%s' and device_id = %s and is_pass = 'P'" % (user, devId) # 拒绝其他人对这个设备的请求
            updateStateSql = "update device set state = '使用中' where id = %s" % (devId) # 更新设备使用状态
            try:
                cursor.execute(agreeSql)
                cursor.execute(rejectSql)
                cursor.execute(updateStateSql)
                db.commit()
                db.close()
                return True
            except:
                db.close()
                return False
