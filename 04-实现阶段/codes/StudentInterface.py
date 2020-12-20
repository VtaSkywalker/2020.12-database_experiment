from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from StudentQueryDevInterface import *


class StudentInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('StudentInterface.ui', self)

    def push_test(self):
        print("按钮触发！传递参数：" + self.user)

    def openStudentQueryDevInterface(self):
        self.StudentQueryDevInterfaceWindow = StudentQueryDevInterface()
        self.StudentQueryDevInterfaceWindow.openWindow(self.user)

    '''
        方法：openWindow(str user)
        描述：学生图形界面的mainloop
        输入：用户账号
        外部输入：无
        输出：无
        返回：无
        协作类：LoginInterface、StudentQueryDevInerface、StudentQueryAskInerface
        负责人：caimx
    '''
    def openWindow(self, user):
        self.user = user
        self.setWindowTitle("学生用户界面-" + self.user)
        self.pushButton_2.clicked.connect(self.openStudentQueryDevInterface) # click(设备查询)
        self.pushButton.clicked.connect(self.push_test)
        '''if(click(设备查询))
            AddDevInterface.openWindow(self.user)
        if(click(我的申请))
            FixDevInterface.openWindow(self.user)
        if(click(close))
            system.close()'''
        self.show()