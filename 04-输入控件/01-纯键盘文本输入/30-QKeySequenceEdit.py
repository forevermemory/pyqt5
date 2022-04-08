
import sys
from PyQt5.Qt import *


'''
QKeySequenceEdit 适用于获取组合键

当控件收到焦点时开始录制, 并在用户释放最后一个关键字后一秒钟结束录制

# 设置组合键 MAC的control为Qt.META
se = QKeySequence(Qt.CTRL+Qt.Key_C, Qt.META+Qt.Key_1)
self.t.setKeySequence(se)

# 获取组合键
se = self.t.keySequence()
print(se.count())
print(se.toString())

# 信号
self.t.editingFinished.connect(lambda: print('finished'))
self.t.keySequenceChanged.connect(lambda se: print('changed', se))

'''

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

        self.t = QKeySequenceEdit('hello world, china', self)
        self.t.move(50, 100)
        self.t.resize(300, 300)

        self.btn = QPushButton('button', self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.btn_click)

        self.btn = QPushButton('clear', self)
        self.btn.move(150, 20)
        self.btn.clicked.connect(lambda: self.t.clear())


        se = QKeySequence(Qt.CTRL+Qt.Key_C, Qt.META+Qt.Key_1)
        self.t.setKeySequence(se)

        self.t.editingFinished.connect(lambda: print('finished'))
        self.t.keySequenceChanged.connect(lambda se: print('changed', se))

    def init_ui(self):

        pass

    def btn_click(self):
        se = self.t.keySequence()
        print(se.count())
        print(se.toString())
        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())