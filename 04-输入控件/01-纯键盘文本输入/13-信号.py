import sys
from PyQt5.Qt import *


# QLineEdit 单行文本输入框
# 信号
# line1.textEdited.connect(lambda: print('文本被用户编辑时'))
# line1.textChanged.connect(lambda: print('文本内容改变时'))  # 用户改变和代码改变都会触发
# line1.returnPressed.connect(lambda: print('按下回车键'))
# line1.editingFinished.connect(lambda: print('回车键、tab、失去焦点会触发'))
# line1.cursorPositionChanged.connect(lambda old_pos, new_pos: print('光标位置发生改变', old_pos, new_pos))
# line1.selectionChanged.connect(lambda: print('选中文本内容发生改变'))


def main():
    # 1. 创建应用程序对象
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

    btn = QPushButton("按钮", window)
    btn.move(100, 300)

    # 文本内边距
    line1.resize(200, 60)
    # 模拟鼠标点击
    line1.setText('hello world, china')

    # 信号
    line1.textEdited.connect(lambda: print('文本被用户编辑时'))
    line1.textChanged.connect(lambda: print('文本内容改变时')) # 用户改变和代码改变都会触发
    line1.returnPressed.connect(lambda: print('按下回车键'))
    line1.editingFinished.connect(lambda: print('回车键、tab、失去焦点会触发'))
    line1.cursorPositionChanged.connect(lambda old_pos,new_pos: print('光标位置发生改变',old_pos,new_pos))
    line1.selectionChanged.connect(lambda: print('选中文本内容发生改变'))

    def cao():
        pass

    btn.clicked.connect(cao)

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
