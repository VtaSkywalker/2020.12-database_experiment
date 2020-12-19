from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import sys
from Login import *
from TeacherInterface import *
from StudentInterface import *

'''
    LoginInterface Class
'''
class LoginInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('LoginInterface.ui', self)
        self.type = "Student"

    def test_pushButton(self):
        print("账号：" + self.lineEdit.text())
        print("密码：" + self.lineEdit_2.text())
        if(self.radioButton.isChecked()):
            self.type = "Student"
        else:
            self.type = "Teacher"
        print("类型：" + self.type)

    def button_push(self):
        # 获取用户名等基本登录信息
        self.user = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        if(self.radioButton.isChecked()):
            self.loginType = "Student"
        else:
            self.loginType = "Teacher"

        # 登录
        if(Login.loginVerify(self.user, self.password, self.loginType)): # 密码正确
            
            # 自适应缩放
            QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
            
            if(self.loginType == "Teacher"):
                print("打开教师界面")
                # 创建窗口
                self.TeacherInterfaceWindow = TeacherInterface()
                self.TeacherInterfaceWindow.openWindow(self.user)
            elif(self.loginType == "Student"):
                print("打开学生界面")
                # 创建窗口
                self.StudentInterfaceWindow = StudentInterface()
                self.StudentInterfaceWindow.openWindow(self.user)
            
            self.close()

        else:
            QMessageBox.information(self, "错误", "No such account or password incorrect!", QMessageBox.Yes)

    '''
        方法：init()
        描述：登录界面的mainloop
        输入：无
        外部输入：
            1、用户名
            2、密码
        输出：无
        返回：无
        协作类：Login、TeacherInterface、StudentInterface
        负责人：caimx
    '''
    def init(self):
        self.setWindowTitle("登录")
        self.lineEdit_2.setEchoMode(2)
        self.pushButton.clicked.connect(self.button_push)
        self.show()
