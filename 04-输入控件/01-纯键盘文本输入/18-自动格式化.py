
import sys
from PyQt5.Qt import *

'''
QTextEdit 自动格式化

self.t.autoFormatting()
# AutoAll = -1
# AutoBulletList = 1 自动创建符号列表
# AutoNone = 0 不格式化
self.t.setAutoFormatting(QTextEdit.AutoBulletList)


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
        self.t.autoFormatting()
        # AutoAll = -1
        # AutoBulletList = 1 自动创建符号列表
        # AutoNone = 0 不格式化
        self.t.setAutoFormatting(QTextEdit.AutoBulletList)

    def init_ui(self):
        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())