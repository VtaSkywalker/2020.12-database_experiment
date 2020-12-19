from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import sys


class LoginInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('LoginInterface.ui', self)

    def test_pushButton(self):
        print("pushButton clicked!")

    def init(self):
        self.lineEdit_2.setEchoMode(2)
        self.pushButton.clicked.connect(self.test_pushButton)
        self.show()
