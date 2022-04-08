
import sys
from PyQt5.Qt import *

'''
QSlider 滑块

# 特有的功能

# 在两边画刻度线
self.t.setTickPosition(QSlider.TicksBothSides)

# 刻度间隔
# self.t.setTickInterval()


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
        self.t = QSlider(self)
        self.t.move(50, 100)
        self.t.resize(300, 50)

        # self.t.setTickInterval()
        self.t.setOrientation(Qt.Horizontal)

        # 在两边画刻度线
        self.t.setTickPosition(QSlider.TicksBothSides)


    def btn_click(self):


        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())