
import sys
from PyQt5.Qt import *

'''
### QGridLayout 网格布局

### 元素操作
layout.addWidget(widget, 2, 1)
layout.addLayout(layout)

### 拉伸系数
layout.setColumnStretch(1, 2)
layout.setColumnMinimumWidth(1, 100)
layout.setRowStretch(2, 3)
layout.setRowMinimumHeight(2, 100)

### 间距
layout.setVerticalSpacing(30)
layout.setHorizontalSpacing(30)


'''

import sys
from PyQt5.Qt import *


def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("title-")
    window.resize(500, 500)
    window.move(300, 200)
    # label1 = QLabel("标签1", window)

    # 1. 创建一个布局管理器
    layout = QGridLayout()

    # 2. 把布局管理器设置给需要布局的父控件
    window.setLayout(layout)

    # 3. 把需要布局的子控件添加到布局管理器
    label1 = QLabel("标签1")
    label2 = QLabel("标签2")
    label3 = QLabel("标签3")
    label1.setStyleSheet("background-color: #abc")
    label2.setStyleSheet("background-color: green")
    label3.setStyleSheet("background-color: pink")

    label4 = QLabel("标签4")
    label4.setStyleSheet("background-color: #aaa")

    label5 = QLabel("标签5")
    label5.setStyleSheet("background-color: #555")
    label6 = QLabel("标签6")
    label6.setStyleSheet("background-color: #333")
    label7 = QLabel("标签7")
    label7.setStyleSheet("background-color: #535")


    ### 此时是4*3
    layout.addWidget(label1, 0, 0)
    layout.addWidget(label2, 1, 1)
    layout.addWidget(label3, 2, 1)
    layout.addWidget(label4, 3, 1)
    layout.addWidget(label5, 3, 2)
    layout.addWidget(label6, 2, 0)
    layout.addWidget(label7, 2, 1)

    layout.setColumnStretch(1, 2)
    layout.setColumnMinimumWidth(1, 100)
    layout.setRowStretch(2, 3)
    layout.setRowMinimumHeight(2, 100)

    # layout.setVerticalSpacing(50)


    window.show()
    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
