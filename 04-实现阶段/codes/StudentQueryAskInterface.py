from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys


class StudentQueryAskInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('StudentQueryAskInterface.ui', self)

    def query(self):
        self.devId = "*" if (self.lineEdit.text() == "") else self.lineEdit.text()
        [result, reason] = self.check()
        if(reason):
            # 送至后端StudentQueryAsk查询
            print("传送给StudentQueryAsk的参数：%s, %s" % (self.user, self.devId))
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
        # if(选中的仪器是在使用中) then 释放 else 报错
        print("传送选中的记录给ReleaseDev，释放选中的仪器")
        # 刷新查询

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

        '''
            if(click(查询)) # 按条件查询
                for eachX in input # 默认没有筛选条件
                    if(eachX为空)
                        input.eachX = "*"
                D = StudentQueryAsk.queryAskReq(self.user, input.devId)
                update(table, D) # 刷新查询结果'''

        self.pushButton_2.clicked.connect(self.release) # click(释放)

        '''if(click(释放)) # 释放仪器
                if(AskDev.releaseDevReq(select.devId))
                    msgbox("Success!")
                else
                    msgbox("Fail!")
            if(click(close))
                system.close()'''
        self.show()