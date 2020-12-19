from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
import time


class FixDevInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('FixDevInterface.ui', self)

    def button_click(self):
        # mode检查
        if(self.radioButton.isChecked()):
            self.mode = 0 # 维修
        elif(self.radioButton_2.isChecked()):
            self.mode = 1 # 报废

        device_id = self.lineEdit.text()
        fix_reason = self.plainTextEdit.toPlainText()
        [result, reason] = self.check([device_id, fix_reason])
        date = time.strftime("%Y-%m-%d", time.localtime())
        if(result):
            # 留作传递
            print("传递到fixDevReq的参数：%s, %d, %s, %s, %s" % (self.user, int(device_id), self.mode, date, fix_reason))
            '''if(FixDev.fixDevReq(input.user, input.devId, self.mode, date(), input.reason))
                msgbox("Success!")
            else
                msgbox("Fail!")'''
        else:
            QMessageBox.information(self, "错误", reason, QMessageBox.Yes)

    def check(self, deviceList):
        # 检查填入信息是否完整
        for eachEle in deviceList:
            if(eachEle == ""):
                return [False, "信息需要填写完整！"]
        # 检查id是否合法
        try:
            int(deviceList[0])
        except:
            return [False, "设备id应该是数字！"]
        # 检查无误
        return[True, "无误"]

    '''
        方法：openWindow(str user)
        描述：教师维修/报废界面的mainloop
        输入：用户账号
        外部输入：
            1、仪器id
            2、维修/报废原因
        输出：无
        返回：无
        协作类：TeacherInterface、FixDev
        负责人：caimx
    '''
    def openWindow(self, user):
        self.user = user
        self.setWindowTitle("维修/报废设备-" + self.user)
        self.pushButton.clicked.connect(self.button_click)
        # self.mode = 0 # 默认0表示维修，1表示报废
        '''if(click(维修)) # 维修选项
            self.mode = 0
        if(click(报废)) # 报废选项
            self.mode = 1
        if(click(确认)) # 输入信息后确认维修/报废
            if(id未被指定)
                msgbox("Please enter device id!")
            else
                if(FixDev.fixDevReq(input.user, input.devId, self.mode, date(), input.reason))
                    msgbox("Success!")
                else
                    msgbox("Fail!")
        if(click(close))
            system.close()'''
        self.show()