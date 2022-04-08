import sys
from PyQt5.Qt import *


# QLineEdit 单行文本输入框
# 提前定义好或者放在数据库中的
# com = QCompleter(["liu", "lixxxxx", "wzzzzz"], parent)
# line1.setCompleter(com)

def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    # code
    line1 = QLineEdit("", window)
    line1.move(100, 100)
    line1.setPlaceholderText("请输入用户名")

    line2 = QLineEdit("", window)
    line2.move(100, 200)
    line2.setPlaceholderText("请输入密码")
    line2.setEchoMode(QLineEdit.Password)

    # 提前定义好或者放在数据库中的 设置自动补全
    com = QCompleter(["liu", "lixxxxx", "wzzzzz"], line1)
    line1.setCompleter(com)

    btn = QPushButton("按钮", window)
    btn.move(100, 300)

    def cao():
        pass
    btn.clicked.connect(cao)

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
