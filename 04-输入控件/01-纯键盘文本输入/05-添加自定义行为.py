import sys
from PyQt5.Qt import *


# QLineEdit 单行文本输入框
# 例如: 密码输入框有个小眼睛 显示和加密
# addAction
#     LeadingPosition = 0 显示在左边
#     TrailingPosition = 1

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

    # 添加行为
    action = QAction(line2)
    action.setIcon(QIcon("../../images/icons/show.png"))

    def cao():
        mode = line2.echoMode()
        if mode == QLineEdit.Password:
            action.setIcon(QIcon("../../images/icons/ico-hidden.png"))
            line2.setEchoMode(QLineEdit.Normal)
        elif mode == QLineEdit.Normal:
            action.setIcon(QIcon("../../images/icons/show.png"))
            line2.setEchoMode(QLineEdit.Password)
    action.triggered.connect(cao)

    # line2.addAction(action, QLineEdit.LeadingPosition)
    line2.addAction(action, QLineEdit.TrailingPosition)


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
