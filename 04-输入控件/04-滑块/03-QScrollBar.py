
import sys
from PyQt5.Qt import *

'''
QScrollBar 滚动条

# 不会单独使用


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

        self.label = QLabel('0', self)
        self.label.move(150, 200)
        self.label.resize(300, 50)

        # self.t = QAbstractSlider(self)

        self.t = QScrollBar(self)
        self.t.move(50, 100)
        self.t.resize(300, 50)



    def btn_click(self):


        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())