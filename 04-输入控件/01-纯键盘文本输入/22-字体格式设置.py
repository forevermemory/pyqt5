
import sys
from PyQt5.Qt import *

'''
QTextEdit 字体设置

# QFontDialog().getFont() # 展示对话框 查看字体

self.t.setFontFamily("华文黑体")
self.t.setFontItalic(True)
self.t.setFontUnderline(True)
self.t.setFontWeight(60) 
self.t.setFontPointSize(28) # 字号大小

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

        # QFontDialog().getFont() # 展示对话框 查看字体

        self.t.setFontFamily("华文黑体")
        self.t.setFontItalic(True)
        self.t.setFontUnderline(True)
        self.t.setFontWeight(60)
        self.t.setFontPointSize(28) # 字号大小
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