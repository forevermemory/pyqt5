import sys
from PyQt5.Qt import *

'''
QDoubleSpinBox 浮点型步长调节

# 使用和QSpinBox基本类似
self.t.setMaximum(2)
self.t.setMinimum(0.5)
self.t.setWrapping(True)
self.t.setDecimals(1)
self.t.setSingleStep(0.5)

信号
valueChanged[str]
valueChanged[float]

'''

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.t = QDoubleSpinBox(self)
        self.t.move(50, 100)
        self.t.resize(300, 50)

        self.t.editingFinished.connect(lambda: print("end edit"))

        self.btn = QPushButton('button', self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.btn_click)

        QDateTimeEdit

        self.btn = QPushButton('clear', self)
        self.btn.move(150, 20)
        self.btn.clicked.connect(lambda: self.t.clear())

    def btn_click(self):

        self.t.setMaximum(2)
        self.t.setMinimum(0.5)
        self.t.setWrapping(True)
        self.t.setDecimals(1)
        self.t.setSingleStep(0.5)

        self.t.setSuffix("倍速")
        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())