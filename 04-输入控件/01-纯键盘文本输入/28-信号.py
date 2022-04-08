
import sys
from PyQt5.Qt import *

'''
QTextEdit 信号

# 文本内容发生改变
self.t.textChanged.connect(self.text_change)

# 选中文本发生改变
self.t.selectionChanged.connect(self.select_change)

# 光标位置发生改变
self.t.cursorPositionChanged.connect(self.cursor_pos_change)

# 当前字符格式发生改变
self.t.currentCharFormatChanged

# 复制可用时候
self.t.copyAvailable

# 重做可用
self.t.redoAvailable

# 撤销可用
self.t.undoAvailable

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

        self.t.setText("hello world, a "*100 +'<a name="_name" href="https://www.baidu.com">锚点</a>'+'pyqt5'*100)


        # 文本内容发生改变
        self.t.textChanged.connect(self.text_change)

        # 选中文本发生改变
        self.t.selectionChanged.connect(self.select_change)

        # 光标位置发生改变
        self.t.cursorPositionChanged.connect(self.cursor_pos_change)
        #
        # # 当前字符格式发生改变
        # self.t.currentCharFormatChanged
        #
        # # 复制可用时候
        # self.t.copyAvailable
        #
        # # 重做可用
        # self.t.redoAvailable
        #
        # # 撤销可用
        # self.t.undoAvailable
        #

    def text_change(self,):
        print('文本内容发生改变')

    def select_change(self):
        print('选中文本发生改变')

    def btn_click(self):



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