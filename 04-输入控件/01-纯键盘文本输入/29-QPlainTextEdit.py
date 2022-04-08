
import sys
from PyQt5.Qt import *


'''
QPlainTextEdit 和QTextEdit类似 
对处理纯文本做了优化，性能优于QTextEdit
不支持插入表格和框架
采用逐行滚动, QTextEdit采用像素滚动

# 支持放大和缩小
self.t.zoomIn(1)
self.t.zoomOut(1)

'''

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

        self.t = QPlainTextEdit('hello world, china', self)
        self.t.move(50, 100)
        self.t.resize(300, 300)

        self.btn = QPushButton('button', self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.btn_click)

        self.btn = QPushButton('clear', self)
        self.btn.move(150, 20)
        self.btn.clicked.connect(lambda: self.t.clear())

    def init_ui(self):

        pass

    def btn_click(self):
        self.t.zoomIn(1)
        self.t.zoomOut(1)
        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())