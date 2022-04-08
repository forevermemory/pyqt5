
import sys
from PyQt5.Qt import *

'''
QComboBox 下拉选择框
# 添加条目
self.t.addItem("1", [1, 2])
self.t.addItem("2", [1, 2])
self.t.addItems(["2", "3"])
self.t.addItems(("4", "5"))

self.t.insertItem(2, "insertItem")
self.t.setItemText(3, "setItemText")
self.t.setItemIcon(3, QIcon('../../images/web.png'))

# 设置model
self.t.setModel() # 待定 可以为树形结构或者表格样式


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

        self.t.addItem("1", [1, 2])
        self.t.addItem("2", [1, 2])
        self.t.addItems(["2", "3"])
        self.t.addItems(("4", "5"))

        self.t.insertItem(2, "insertItem")
        self.t.setItemText(3, "setItemText")
        self.t.setItemIcon(3, QIcon('../../images/web.png'))

        # self.t.setModel()

    def btn_click(self):


        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())