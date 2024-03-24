
import sys
from PyQt5.Qt import *

'''
### QStackedLayout 类似于编辑器的代码界面 由上面的标签控制显示哪个内容



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
    layout = QVBoxLayout()

    # 2. 把布局管理器设置给需要布局的父控件
    window.setLayout(layout)

    # 3. 把需要布局的子控件添加到布局管理器
    label1 = QPushButton("标签1")
    label2 = QPushButton("标签2")
    label3 = QPushButton("标签3")
    # label1.setStyleSheet("background-color: #abc")
    # label2.setStyleSheet("background-color: green")
    # label3.setStyleSheet("background-color: pink")

    vb = QHBoxLayout()

    vb.addWidget(label1)
    vb.addWidget(label2)
    vb.addWidget(label3)

    layout.addLayout(vb)

    #####
    qs = QStackedLayout()
    middle1 = QLabel("label1", window)
    middle1.setStyleSheet("background-color: #aaa")
    middle2 = QLabel("label2", window)
    middle2.setStyleSheet("background-color: #bbb")
    middle3 = QLabel("label3", window)
    middle3.setStyleSheet("background-color: #ccc")
    qs.addWidget(middle1)
    qs.addWidget(middle2)
    qs.addWidget(middle3)

    layout.addLayout(qs)

    label1.clicked.connect(lambda: qs.setCurrentIndex(0))
    label2.clicked.connect(lambda: qs.setCurrentIndex(1))
    label3.clicked.connect(lambda: qs.setCurrentIndex(2))

    window.show()
    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
