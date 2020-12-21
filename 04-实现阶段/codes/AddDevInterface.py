from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
import re
import time
from AddDev import *

class AddDevInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('AddDevInterface.ui', self)

    def button_click(self):
        device_id = self.lineEdit.text()
        name = self.lineEdit_2.text()
        deviceType = self.lineEdit_3.text()
        parameter = self.lineEdit_4.text()
        date_buy = self.lineEdit_5.text()
        price = self.lineEdit_6.text()
        manufactor = self.lineEdit_7.text()
        warranty_period = self.lineEdit_8.text()
        bought_by = self.lineEdit_9.text()
        manager_user = self.lineEdit_10.text()
        state = "空闲"
        result, reason = self.check_para([device_id, name, deviceType, parameter, date_buy, price, manufactor, warranty_period, bought_by, manager_user])
        if(result):
            '''在这里调用AddDev'''
            # print("参数传递到AddDev：%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (device_id, name, deviceType, parameter, date_buy, price, manufactor, warranty_period, bought_by, manager_user, state))

            if(AddDev.addDevReq([device_id, name, deviceType, parameter, date_buy, price, manufactor, warranty_period, bought_by, manager_user, state])):
                QMessageBox.information(self, "成功", "添加成功！", QMessageBox.Yes)
            else:
                QMessageBox.information(self, "错误", "操作失败！", QMessageBox.Yes)


            '''if(click(添加)) # 输入信息后确认添加
            if(Device中除了state外的任何一个属性未被指定)
                msgbox("Please enter full info!")
            else
                Device.state = "空闲"
                if(AddDev.addDevReq(input.Device))
                    msgbox("Success!")
                else
                    msgbox("Fail!")
            if(click(close))
                system.close()'''
        else:
            QMessageBox.information(self, "错误", reason, QMessageBox.Yes)

    def check_para(self, deviceInfo):
        for eachInfo in deviceInfo:
            if(eachInfo == ""):
                return [False, "请填写完整的信息！"]
        # 设备id合法性检测
        try:
            int(deviceInfo[0])
        except:
            return [False, "设备id必须是数字！"]
        # 设备参数合法性检测
        try:
            float(deviceInfo[3])
        except:
            return [False, "设备参数必须是数字！"]
        # 合法日期检测
        try:
            time.strptime(deviceInfo[4], "%Y-%m-%d")
        except:
            return [False, "日期非法！"]
        # 合法价格检测
        try:
            float(deviceInfo[5])
        except:
            return [False, "价格必须是数字！"]
        # 合法保修期检测
        try:
            float(deviceInfo[7])
        except:
            return [False, "保修期必须是数字！"]
        # 检查无误
        return [True, "检查无误"]


    '''
        方法：openWindow(str user)
        描述：教师添加设备界面的mainloop
        输入：用户账号
        外部输入：仪器的各种信息
        输出：无
        返回：无
        协作类：TeacherInerface、AddDev
        负责人：caimx
    '''
    def openWindow(self, user):
        self.user = user
        self.setWindowTitle("添加设备-" + self.user)
        self.pushButton.clicked.connect(self.button_click)
        
        self.show()