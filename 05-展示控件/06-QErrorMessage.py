
import sys
from PyQt5.Qt import *

'''
QErrorMessage 错误消息对话框 
box = QErrorMessage(self)

### 如果在checkbox上勾选 就不会继续弹出同样的内容
box.showMessage("okok")
box.showMessage("okok")
box.showMessage("okok2")

### 显示调试信息
box.qtHandler()
qDebug("qtHandler")
        
'''

import sys
from PyQt5.Qt import *


def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    btn = QPushButton('button', window)
    btn.move(50, 20)


    # code
    box = QErrorMessage(window)
    box.setWindowTitle("setWindowTitle")

    box.qtHandler()
    qDebug("qtHandler")


    def btn_click():
        # box.show()
        # box.showMessage("okok")
        # box.showMessage("okok")
        # box.showMessage("okok2")
        pass

    btn.clicked.connect(btn_click)
    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
