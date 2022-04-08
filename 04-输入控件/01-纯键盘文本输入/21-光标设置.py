
import sys
from PyQt5.Qt import *

'''
QTextEdit 光标设置

# 获取光标的矩形
self.t.cursorRect(self.t.textCursor())

# 设置光标宽度
self.t.setCursorWidth(10)

'''

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.t = QTextEdit('hello world, china', self)
        self.t.move(50, 100)
        self.t.resize(300, 300)

        self.btn = QPushButton('button', self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.btn_click)

        self.btn = QPushButton('clear', self)
        self.btn.move(150, 20)
        self.btn.clicked.connect(lambda: self.t.clear())

        self.init_ui()  # 界面绘制交给InitUi方法

    def btn_click(self):

        print(self.t.cursorWidth())

        if self.t.overwriteMode():
            self.t.setOverwriteMode(False)
            self.t.setCursorWidth(1)
        else:
            self.t.setOverwriteMode(True)
            self.t.setCursorWidth(10)
        pass

    def init_ui(self):
        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())