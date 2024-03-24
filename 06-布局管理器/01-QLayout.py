
import sys
from PyQt5.Qt import *

'''
### 布局管理器  
1. 创建一个布局管理器
2. 把布局管理器设置给需要布局的父控件
3. 把需要布局的子控件添加到布局管理器

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

    label1 = QLabel("标签1")
    label2 = QLabel("标签2")
    label3 = QLabel("标签3")
    label1.setStyleSheet("border: 1px solid red")
    label2.setStyleSheet("border: 1px solid green")
    label3.setStyleSheet("border: 1px solid pink")

    layout = QVBoxLayout()
    layout.addWidget(label1)
    layout.addWidget(label2)
    layout.addWidget(label3)

    # layout.setContentsMargins(0, 0 ,10,20)
    layout.setSpacing(10)

    window.setStyleSheet("background-color: #aaa")
    window.setLayout(layout)

    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
