
import sys
from PyQt5.Qt import *

'''
### QBoxLayout 垂直或者水平布局管理器 一般使用其两个子类

## 构造函数
layout = QBoxLayout(QBoxLayout.LeftToRight)
    BottomToTop = 3
    LeftToRight = 0
    RightToLeft = 1
    TopToBottom = 2

## 调整方向
layout.setDirection((layout.direction() + 1) % 4)

## 添加元素
# 添加控件
layout.addWidget()
layout.insertLayout()

# 添加子布局
layout.addLayout()
layout.insertLayout()

# 替换控件
layout.replaceWidget()

# 移除控件
layout.removeWidget() # 但是还是会显示

# 添加空白
layout.addSpacing()
layout.insertSpacing()

# 添加伸缩 类似于前端的flex布局

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
    layout2 = QBoxLayout(QBoxLayout.LeftToRight)
    layout2.addWidget(label5)
    layout2.addWidget(label6)
    layout2.addWidget(label7)

    # 1. 创建一个布局管理器
    layout = QBoxLayout(QBoxLayout.TopToBottom)

    # 2. 把布局管理器设置给需要布局的父控件
    window.setLayout(layout)

    # 3. 把需要布局的子控件添加到布局管理器
    layout.addWidget(label1)
    layout.addWidget(label2)
    layout.addLayout(layout2)
    layout.addWidget(label3)
    layout.addWidget(label4)

    ## 添加元素
    # # 添加控件
    # layout.addWidget()
    # layout.insertLayout()
    # # 添加子布局
    # layout.addLayout()
    # layout.insertLayout()
    #
    # # 替换控件
    # layout.replaceWidget()
    # # 移除控件
    # layout.removeWidget() # 但是还是会显示
    #
    # # 添加空白
    # layout.addSpacing()
    # layout.insertSpacing()
    #
    # 添加伸缩
    # layout.addStretch()

    # timer = QTimer(window)
    # def test_():
    #     layout.setDirection((layout.direction() + 1) % 4)
    # timer.timeout.connect(test_)
    # timer.start(1000)



    window.show()


    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
