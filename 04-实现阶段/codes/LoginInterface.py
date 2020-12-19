from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import sys

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
        self.pushButton.clicked.connect(self.test_pushButton)
        self.show()
