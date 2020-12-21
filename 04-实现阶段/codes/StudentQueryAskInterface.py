from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
import sys
from StudentQueryAsk import *
import numpy as np
from ReleaseDev import *


class StudentQueryAskInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('StudentQueryAskInterface.ui', self)

    def query(self):
        self.devId = "*" if (self.lineEdit.text() == "") else self.lineEdit.text()
        [result, reason] = self.check()
        if(reason):
            # 送至后端StudentQueryAsk查询
            D = StudentQueryAsk.queryAskReq(self.user, self.devId)
            self.updateTable(D)

            '''
            if(click(查询)) # 按条件查询
                for eachX in input # 默认没有筛选条件
                    if(eachX为空)
                        input.eachX = "*"
                D = StudentQueryAsk.queryAskReq(self.user, input.devId)
                update(table, D) # 刷新查询结果'''
            # print("传送给StudentQueryAsk的参数：%s, %s" % (self.user, self.devId))
        else:
            QMessageBox.information(self, "错误", reason, QMessageBox.Yes)
    def check(self):
        if(self.devId != "*"):
            try:
                int(self.devId)
            except:
                return [False, "设备id必须是数字！"]
        return [True, "检查无误"]

    def release(self):
        # print("传送输入的记录给ReleaseDev，释放选中的仪器")
        self.query() # 刷新查询结果
        if(ReleaseDev.releaseDevReq(self.devId)):
            QMessageBox.information(self, "成功", "释放成功！", QMessageBox.Yes)
        else:
            QMessageBox.information(self, "错误", "操作失败！", QMessageBox.Yes)
        '''if(click(释放)) # 释放仪器
                if(AskDev.releaseDevReq(input.devId))
                    msgbox("Success!")
                else
                    msgbox("Fail!")
            if(click(close))
                system.close()'''
        self.query() # 刷新查询结果

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
        描述：学生查询申请界面的mainloop
        输入：用户账号
        外部输入：设备id
        输出：无
        返回：无
        协作类：StudentInterface、StudentQueryAsk、ReleaseDev
    '''
    def openWindow(self, user):
        self.user = user
        self.setWindowTitle("查询申请-" + self.user)
        '''筛选条件全部默认为"*"
        StudentQueryAsk.queryAskReq(self.user, input.devId)
        while(loop){'''

        '''
            初始时期，显示所有结果
        '''

        self.pushButton.clicked.connect(self.query) # click(查询)
        self.pushButton_2.clicked.connect(self.release) # click(释放)

        self.show()