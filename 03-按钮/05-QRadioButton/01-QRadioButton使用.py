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

    # code
    w1 = QWidget(window)
    w1.resize(500, 100)
    w1.setStyleSheet("background-color: #bbb")
    r1 = QRadioButton("男", w1)
    r1.move(10, 10)
    r1.setChecked(True)
    r2 = QRadioButton("女", w1)
    r2.move(50, 10)
    
    # 两组互斥
    w2 = QWidget(window)
    w2.resize(500, 100)
    w2.move(0, 150)
    w2.setStyleSheet("background-color: pink")
    r3 = QRadioButton("是", w2)
    r3.move(10, 10)
    r4 = QRadioButton("否", w2)
    r4.move(50, 10)



    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
