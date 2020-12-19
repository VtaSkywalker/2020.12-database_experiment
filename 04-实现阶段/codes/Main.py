import sys
from LoginInterface import *
from PyQt5 import QtCore

# 自适应缩放
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

app = QApplication(sys.argv)
# 创建窗口
window = LoginInterface()

# 显示窗口
window.init()

# 运行应用，并监听事件
sys.exit(app.exec_())
