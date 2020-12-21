from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
import sys
from Approval import *
from TeacherQueryAsk import *


class ApprovalInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('ApprovalInterface.ui', self)

    # 点击“查询”关联动作
    def query(self):
        # 更新device_id
        if(self.lineEdit.text() == ""):
            self.device_id = "*"
        else:
            self.device_id = self.lineEdit.text()
        # 更新user_student
        if(self.lineEdit_2.text() == ""):
            self.user_student = "*"
        else:
            self.user_student = self.lineEdit_2.text()
        # 检查合理性
        [result, reason] = self.check()
        if(result):
            # 显示查询结果
            # print("传递参数给TeacherQueryAsk：%s, %s, %s" % (self.device_id, self.user_student, self.user))
            D = TeacherQueryAsk.queryAskReq([self.device_id, self.user_student, self.user])
            self.updateTable(D)
        else:
            QMessageBox.information(self, "错误", reason, QMessageBox.Yes)

    # 检查参数合理性
    def check(self):
        # 检查id是否合理
        if(self.device_id != "*"):
            try:
                int(self.device_id)
            except:
                return [False, "设备id应该是数字！"]
        # 检查无误
        return [True, "检查无误！"]

    # 同意请求
    def agree(self):
        self.query()
        # print("传递参数给Approval：%s, %s, %s" % (self.user_student, self.device_id, True))
        if(Approval.approvalReq(self.user_student, self.device_id, True)):
            QMessageBox.information(self, "成功", "操作成功！", QMessageBox.Yes)
        else:
            QMessageBox.information(self, "错误", "无效操作！", QMessageBox.Yes)
        self.query()

    # 拒绝请求
    def reject(self):
        self.query()
        # print("传递参数给Approval：%s, %s, %s" % (self.user_student, self.device_id, False))
        if(Approval.approvalReq(self.user_student, self.device_id, False)):
            QMessageBox.information(self, "成功", "操作成功！", QMessageBox.Yes)
        else:
            QMessageBox.information(self, "错误", "无效操作！", QMessageBox.Yes)
        self.query()

    # 更新查询结果
    def updateTable(self, D):
        row = len(D) - 1
        column = len(D[0])
        model = QStandardItemModel(row, column)
        

        if(np.array(D).ndim == 1): # 如果搜索结果为空，只返回了属性列
            model.setHorizontalHeaderLabels(D)
        else:
            model.setHorizontalHeaderLabels(D[0, :])
            for i in range(row):
                for j in range(column):
                    item=QStandardItem(str(D[i + 1, j]))
                    model.setItem(i, j, item)

        self.tableView.setModel(model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # 填充边界


    '''
        方法：openWindow(str user)
        描述：教师审批界面的mainloop
        输入：用户账号
        外部输入：申请的各种筛选条件
        输出：无
        返回：无
        协作类：TeacherInterface、Approval、TeacherQueryAsk
        负责人：zzr
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
        self.query()

        self.pushButton.clicked.connect(self.query)
        self.pushButton_2.clicked.connect(self.agree)
        self.pushButton_3.clicked.connect(self.reject)

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