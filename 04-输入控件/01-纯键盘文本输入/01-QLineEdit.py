import sys
from PyQt5.Qt import *


# QLineEdit 单行文本输入框
# QLineEdit.NoEcho  # 不输出
# QLineEdit.Normal  # 正常输出
# QLineEdit.Password  # 密文模式
# QLineEdit.PasswordEchoOnEdit  # 编辑时明文, 结束后密文
#
# line.setEchoMode(QLineEdit.PasswordEchoOnEdit)
# line.echoMode()

def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    # code
    line = QLineEdit("默认文本", window)
    line2 = QLineEdit("默认文本", window)
    line2.move(0, 30)

    # QLineEdit.NoEcho # 不输出
    # QLineEdit.Normal # 正常输出
    # QLineEdit.Password # 密文模式
    # QLineEdit.PasswordEchoOnEdit # 编辑时明文, 结束后密文

    line.setEchoMode(QLineEdit.PasswordEchoOnEdit)
    line.echoMode()

    btn = QPushButton("按钮", window)
    btn.move(100,100)

    def cao():
        print(line.text())
        line.setText("btn-click")
        line.insert("xxx") # 在光标之后插入
    btn.clicked.connect(cao)

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
