from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
import sys
import time
from TeacherQueryDev import *


class TeacherQueryDevInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('TeacherQueryDevInterface.ui', self)

    def query(self):
        '''if(click(查询)) # 按条件查询
            for eachX in input.Device中的所有属性 # 默认没有筛选条件
                if(eachX为空)
                    input.Device.eachX = "*"
            
            D = TeacherQueryDev.queryAskReq(input.Device)
            update(table, D) # 刷新查询结果
        
        if(click(close))
            system.close()'''
        self.device_id = "*" if (self.lineEdit.text() == "") else self.lineEdit.text()
        self.name = "*" if (self.lineEdit_2.text() == "") else self.lineEdit_2.text()
        self.deviceType = "*" if (self.lineEdit_3.text() == "") else self.lineEdit_3.text()
        self.parameter = "*" if (self.lineEdit_4.text() == "") else self.lineEdit_4.text()
        self.date_buy = "*" if (self.lineEdit_5.text() == "") else self.lineEdit_5.text()
        self.price = "*" if (self.lineEdit_6.text() == "") else self.lineEdit_6.text()
        self.manufactor = "*" if (self.lineEdit_7.text() == "") else self.lineEdit_7.text()
        self.warranty_period =  "*" if (self.lineEdit_8.text() == "") else self.lineEdit_8.text()
        self.bought_by = "*" if (self.lineEdit_9.text() == "") else self.lineEdit_9.text()
        self.manager_user = self.user
        self.state = self.comboBox.currentText()
        [result, reason] = self.check_para()
        if(result):
            '''显示查询结果'''
            # print("传送到TeacherQueryDev的参数：%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.device_id, self.name, self.deviceType, self.parameter, self.date_buy, self.price, self.manufactor, self.warranty_period, self.bought_by, self.manager_user, self.state))
            D = TeacherQueryDev.queryDevReq([self.device_id, self.name, self.deviceType, self.parameter, self.date_buy, self.price, self.manufactor, self.warranty_period, self.bought_by, self.manager_user, self.state])
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

    '''
        方法：openWindow(str user)
        描述：教师查询设备界面的mainloop
        输入：用户账号
        外部输入：设备筛选条件
        输出：无
        返回：无
        协作类：TeacherInterface、TeacherQueryDev
        负责人：caimx
    '''
    def openWindow(self, user):
        self.user = user
        self.setWindowTitle("设备查询-" + self.user)
        self.pushButton.clicked.connect(self.query)

        '''
            初始化查询，并显示表格
        '''
        self.query()

        '''Device.manager_user = self.user # 初始化Device的筛选条件
        其余筛选条件全部默认为"*"
        TeacherQueryDev.queryAskReq(input.Device)'''
        
        self.show()