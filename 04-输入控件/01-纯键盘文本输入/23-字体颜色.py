
import sys
from PyQt5.Qt import *

'''
QTextEdit 字体颜色

# 背景色
self.t.setTextBackgroundColor(QColor(222, 10, 10))

# 字体颜色
self.t.setTextColor(QColor(10, 10, 233))

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


        self.t.setTextBackgroundColor(QColor(222, 10, 10))
        self.t.setTextColor(QColor(10, 10, 233))
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