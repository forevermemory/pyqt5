

import sys
import time

from PyQt5.Qt import *
#
# adjustSize 自动调整大小
# setFixedSize 不可以最大化


def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)

    # window.setFixedSize(500,500) # 不可以最大化
    # window.move(300, 200)

    # code
    # setGeometry 设置用户区域距离左上角的距离
    # window.setGeometry(0,0, 100,100)
    print(window.geometry())

    label = QLabel(window)
    label.setText("晴天晴天")
    label.move(100,100)
    label.setStyleSheet("background-color:pink")

    def btn_click():
        label.setText(label.text() + str(time.time()))
        label.adjustSize() # 自动调整大小


    btn = QPushButton(window)
    btn.setText("变大")
    btn.clicked.connect(btn_click)

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
