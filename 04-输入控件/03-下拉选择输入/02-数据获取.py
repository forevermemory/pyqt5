
import sys
from PyQt5.Qt import *

'''
QComboBox 下拉选择框
# 数据获取
total = self.t.count()
        
print(self.t.itemIcon(i))
print(self.t.itemText(i))
print(self.t.itemData(i))
print(self.t.currentText())
print(self.t.currentData())
print(self.t.currentIndex())

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

        total = self.t.count()
        print(total)

        for i in range(total):
            pass
            # print(self.t.itemIcon(i))
            # print(self.t.itemText(i))
            # print(self.t.itemData(i))
        print(self.t.currentText())
        print(self.t.currentData())
        print(self.t.currentIndex())


        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())