
import sys
from PyQt5.Qt import *

'''
QTextEdit 软换行模式 用户输入的内容过多时候 是否换行 以及什么模式换行

# 设置软换行模式
QTextEdit.NoWrap # 无软换行 内容超过宽度 会产生水平滚动条
QTextEdit.WidgetWidth # 以控件宽度为限制 但会保持单词完整性
QTextEdit.FixedPixelWidth # 固定像素宽度 配合 setLineWrapColumnOrWidth()
QTextEdit.FixedColumnWidth # 固定列宽度 配合  setLineWrapColumnOrWidth()

self.t.setLineWrapMode(QTextEdit.WidgetWidth)
self.t.lineWrapMode() # 获取


# # 设置单词换行模式
QTextEdit.NoWrap # 无换行
QTextEdit.WordWrap # 单词保持完整性
QTextEdit.ManualWrap # 同NoWrap
QTextEdit.WrapAnywhere # 宽度够了之后 随意在任何位置换行
QTextEdit.WrapAtWordBoundaryOrAnywhere # 尽可能赶在单词的边界

self.t.setWordWrapMode(QTextEdit.WordWrap)
self.t.wordWrapMode()  # 获取

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

        # # 设置软换行模式
        # QTextEdit.NoWrap # 无软换行 内容超过宽度 会产生水平滚动条
        # QTextEdit.WidgetWidth # 以控件宽度为限制 但会保持单词完整性
        # QTextEdit.FixedPixelWidth # 固定像素宽度 配合 setLineWrapColumnOrWidth()
        # QTextEdit.FixedColumnWidth # 固定列宽度 配合  setLineWrapColumnOrWidth()
        #
        self.t.setLineWrapMode(QTextEdit.FixedPixelWidth)
        self.t.setLineWrapColumnOrWidth(100)
        self.t.lineWrapMode() # 获取

        # # 设置单词换行模式
        QTextEdit.NoWrap # 无换行
        QTextEdit.WordWrap # 单词保持完整性
        QTextEdit.ManualWrap # 同NoWrap
        QTextEdit.WrapAnywhere # 宽度够了之后 随意在任何位置换行
        QTextEdit.WrapAtWordBoundaryOrAnywhere # 尽可能赶在单词的边界

        self.t.setWordWrapMode(QTextEdit.WordWrap)
        self.t.wordWrapMode()  # 获取
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