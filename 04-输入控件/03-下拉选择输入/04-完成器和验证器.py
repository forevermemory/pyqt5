
import sys
from PyQt5.Qt import *

'''
QComboBox 下拉选择框

# 设置完成起
self.t.setEditable(True)

c = QCompleter(('hello', 'hewwo'))
self.t.setCompleter(c)

# 验证器参考其它
self.t.setValidator(QValidator())

# 主动弹出
self.t.showPopup()

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

    def btn_click(self):

        self.t.setEditable(True)

        c = QCompleter(('hello', 'hewwo'))
        self.t.setCompleter(c)

        # self.t.setValidator(QValidator())

        self.t.showPopup()

        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())