
import sys
from PyQt5.Qt import *

'''
QComboBox 下拉选择框

# 信号
# 某个条目被选中 必须是用户交互才会发射这个信号
self.t.activated[str].connect(lambda tx :print('用户交互才会发射这个信号', tx))
self.t.activated[int]

# 某个条目被选中 用户交互或者代码控制
self.t.currentIndexChanged[str].connect(lambda tx :print('用户交互或者代码控制', tx))
self.t.currentIndexChanged[int]

# 高亮
self.t.highlighted[str].connect(lambda tx:print('高亮', tx))
self.t.highlighted[int

]
'''


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.btn = QPushButton('button', self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.btn_click)

        self.btn = QPushButton('clear', self)
        self.btn.move(150, 20)
        self.btn.clicked.connect(lambda: self.t.clear())

        self.t = QComboBox(self)
        self.t.move(50, 100)
        self.t.resize(300, 50)

        self.t.addItem("hello", [1, 2])
        self.t.addItem("hewwo", [1, 2])
        self.t.addItems(["2", "3"])
        self.t.addItems(("4", "5"))

        self.t.insertItem(2, "insertItem")
        self.t.setItemText(3, "setItemText")
        self.t.setItemIcon(3, QIcon('../../images/web.png'))

        # self.t.setModel()

        # 某个条目被选中 必须是用户交互才会发射这个信号
        # self.t.activated[int]
        self.t.activated[str].connect(lambda tx :print('用户交互才会发射这个信号', tx))

        # 某个条目被选中 用户交互或者代码控制
        self.t.currentIndexChanged[str].connect(lambda tx :print('用户交互或者代码控制', tx))

        # 高亮
        self.t.highlighted[str].connect(lambda tx:print('高亮', tx))

    def btn_click(self):
        self.t.setCurrentIndex(2)
        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())