from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from StudentQueryDev import *
from PyQt5.QtGui import *
import time
from AskDev import *


class StudentQueryDevInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('StudentQueryDevInterface.ui', self)

    def query(self):
        self.device_id = "*" if (self.lineEdit.text() == "") else self.lineEdit.text()
        self.name = "*" if (self.lineEdit_2.text() == "") else self.lineEdit_2.text()
        self.deviceType = "*" if (self.lineEdit_3.text() == "") else self.lineEdit_3.text()
        self.parameter = "*" if (self.lineEdit_4.text() == "") else self.lineEdit_4.text()
        self.date_buy = "*" if (self.lineEdit_5.text() == "") else self.lineEdit_5.text()
        self.price = "*" if (self.lineEdit_6.text() == "") else self.lineEdit_6.text()
        self.manufactor = "*" if (self.lineEdit_7.text() == "") else self.lineEdit_7.text()
        self.warranty_period =  "*" if (self.lineEdit_8.text() == "") else self.lineEdit_8.text()
        self.bought_by = "*" if (self.lineEdit_9.text() == "") else self.lineEdit_9.text()
        self.manager_user = "*" if (self.lineEdit_10.text() == "") else self.lineEdit_10.text()
        self.state = self.comboBox.currentText()
        [result, reason] = self.check_para()
        if(result):
            '''显示查询结果'''
            # print("传送到StudentQueryDev的参数：%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.device_id, self.name, self.deviceType, self.parameter, self.date_buy, self.price, self.manufactor, self.warranty_period, self.bought_by, self.manager_user, self.state))
            D = StudentQueryDev.queryDevReq([self.device_id, self.name, self.deviceType, self.parameter, self.date_buy, self.price, self.manufactor, self.warranty_period, self.bought_by, self.manager_user, self.state])
            self.updateTable(D)
        else:
            QMessageBox.information(self, "错误", reason, QMessageBox.Yes)

    def check_para(self):
        # 设备id合法性检测
        if(self.device_id != "*"):
            try:
                int(self.device_id)
            except:
                return [False, "设备id必须是数字！"]
        # 设备参数合法性检测
        if(self.parameter != "*"):
            try:
                float(self.parameter)
            except:
                return [False, "设备参数必须是数字！"]
        # 合法日期检测
        if(self.date_buy != "*"):
            try:
                time.strptime(self.date_buy, "%Y-%m-%d")
            except:
                return [False, "日期非法！"]
        # 合法价格检测
        if(self.price != "*"):
            try:
                float(self.price)
            except:
                return [False, "价格必须是数字！"]
        # 合法保修期检测
        if(self.warranty_period != "*"):
            try:
                float(self.warranty_period)
            except:
                return [False, "保修期必须是数字！"]
        # 检查无误
        return [True, "检查无误"]

    def ask(self):
        self.days = self.spinBox.value() # 申请天数
        '''
        if(click(申请)){ # 申请使用仪器
            if(AskDev.askDevReq(self.user, select.devId, input.days))
                msgbox("Success!")
            else
                msgbox("Fail!")
        if(click(close))
            system.close()'''
        # 检查状态是否有效，先暂定在后端处理
        # print("传递到AskDev的参数：%s, input.devId, %s" % (self.user, self.days))
        self.query()
        if(AskDev.askDevReq(self.user, self.device_id, self.days)):
            QMessageBox.information(self, "成功", "申请成功！请等待处理", QMessageBox.Yes)
        else:
            QMessageBox.information(self, "错误", "操作失败！", QMessageBox.Yes)
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
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # 填充边界


    '''
        方法：openWindow(str user)
        描述：学生查询设备界面的mainloop
        输入：用户账号
        外部输入：
            1、设备筛选条件
            2、借用天数
        输出：无
        返回：无
        协作类：StudentInterface、StudentQueryDev、AskDev
        负责人：caimx
    '''
    def openWindow(self, user):
        self.user = user
        self.setWindowTitle("设备查询-" + self.user)

        '''
            初始化查询，并显示表格
        '''
        self.query()

        '''筛选条件全部默认为"*"
        StudentQueryDev.queryAskReq(input.Device)'''

        self.pushButton.clicked.connect(self.query) # click(查询)

        '''
        if(click(查询)) # 按条件查询
            for eachX in input.Device中的所有属性 # 默认没有筛选条件
                if(eachX为空)
                    input.Device.eachX = "*"
            StudentQueryDev.queryAskReq(input.Device)
            update(table) # 刷新查询结果'''

        self.pushButton_2.clicked.connect(self.ask) # click(申请)

        
        self.show()