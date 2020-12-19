from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from AddDevInterface import *
from FixDevInterface import *
from ApprovalInterface import *


class TeacherInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('TeacherInterface.ui', self)

    def click_test(self):
        print("按钮点击！传递参数：" + self.user)

    def openAddDevInterface(self):
        self.AddDevInterfaceWindow = AddDevInterface()
        self.AddDevInterfaceWindow.openWindow(self.user)

    def openFixDevInterface(self):
        self.FixDevInterfaceWindow = FixDevInterface()
        self.FixDevInterfaceWindow.openWindow(self.user)

    def openApprovalInterface(self):
        self.ApprovalInterfaceWindow = ApprovalInterface()
        self.ApprovalInterfaceWindow.openWindow(self.user)

    '''
        方法：openWindow(str user)
        描述：教师图形界面的mainloop
        输入：用户账号
        外部输入：无
        输出：无
        返回：无
        协作类：LoginInterface、AddDevInerface、FixDevInerface、ApprovalInerface、TeacherQueryDevInerface    
        负责人：caimx
    '''
    def openWindow(self, user):
        self.user = user
        self.setWindowTitle("教师用户界面-" + self.user)
        self.pushButton.clicked.connect(self.openAddDevInterface) # click(添加设备)
        self.pushButton_2.clicked.connect(self.openFixDevInterface) # click(维修/报废设备)
        self.pushButton_3.clicked.connect(self.openApprovalInterface) # click(申请审批)
        self.pushButton_4.clicked.connect(self.click_test) # click(我管理的设备)
        '''if(click(添加设备))
            AddDevInterface.openWindow(self.user)
        if(click(维修/报废设备))
            FixDevInterface.openWindow(self.user)
        if(click(申请审批))
            ApprovalInterface.openWindow(self.user)
        if(click(我管理的设备))
            TeacherQueryDevInterface.openWindow(self.user)
        if(click(close))
            system.close()'''
        self.show()