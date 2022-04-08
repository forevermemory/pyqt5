import sys
from PyQt5.Qt import *

# btn = QCommandLinkButton("title", "description", window)
# print(btn.description())
# btn.setDescription("description-description")

def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    # code
    btn = QCommandLinkButton("title", "description", window)
    print(btn.description())
    btn.setDescription("description-description")

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
