from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys


class ApprovalInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('ApprovalInterface.ui', self)

    '''
        方法：openWindow(str user)
        描述：教师审批界面的mainloop
        输入：用户账号
        外部输入：申请的各种筛选条件
        输出：无
        返回：无
        协作类：TeacherInterface、Approval、TeacherQueryAsk
    '''
    def openWindow(self, user):
        self.user = user
        self.setWindowTitle("申请审批-" + self.user)
        # 初始化筛选条件
        self.device_id = "*"
        self.user_student = "*"
        self.user_teacher = self.user

        '''
            初始化查询，并显示表格
        '''

        # self.pushButton.clicked.connect()

        '''TeacherQueryAsk.queryAskReq(input.Ask)
        if(click(查询)) # 按条件查询
            for eachX in input.Ask中的所有属性{ # 默认没有筛选条件
                if(eachX为空)
                    input.Ask.eachX = "*"
            D = TeacherQueryAsk.queryAskReq(input.Ask)
            update(table, D) # 刷新查询结果
        if(click(同意)) # 申请通过
            if(Approval.approvalReq(select.user_student, select.devId, true))
                msgbox("Success!")
            else
                msgbox("Fail!")
        if(click(拒绝)) # 申请不通过
            if(Approval.approvalReq(select.user_student, select.devId, false))
                msgbox("Success!")
            else
                msgbox("Fail!")
        if(click(close))
            system.close()'''
        self.show()