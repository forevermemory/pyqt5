import sys
from PyQt5.Qt import *


# QLineEdit 单行文本输入框
#
#         line1.setCursorPosition(3)
#         # line1.backspace() # 删除选中文本/光标左侧一个字符
#         # line1.del_() # 删除选中文本/光标右侧一个字符
#
#         line1.clear() # 清空
#         line1.copy()
#         line1.cut()
#         line1.paste()
#         line1.isUndoAvailable()
#         line1.undo()
#         line1.isRedoAvailable()
#         line1.redo()
#
#         # 拖拽 选中的文本允许拖拽
#         line1.setDragEnabled(True)

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


    def cao():
        # line1.setSelection(3, 5)

        line1.setCursorPosition(3)
        # line1.backspace() # 删除选中文本/光标左侧一个字符
        # line1.del_() # 删除选中文本/光标右侧一个字符

        line1.clear() # 清空
        line1.copy()
        line1.cut()
        line1.paste()
        line1.isUndoAvailable()
        line1.undo()
        line1.isRedoAvailable()
        line1.redo()

        # 拖拽 选中的文本允许拖拽
        line1.setDragEnabled(True)

    btn.clicked.connect(cao)

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
