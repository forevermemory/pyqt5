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
    btn = QPushButton(window)
    btn.move(100, 100)
    btn.setText("btn")

    # 被点过了之后才会更改样式
    btn.setAutoDefault(True)
    print(btn.autoDefault())

    # 没有点过会更改样式
    # btn.setDefault(True)

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
