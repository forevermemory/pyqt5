
import sys
from PyQt5.Qt import *

'''
QDial 类似于仪表盘速度等

# 是否显示刻度
self.t.setNotchesVisible(True)

# 刻度之间的间隔
self.t.setNotchTarget(0.5)

# 步长
self.t.setPageStep(10)

# 最大值和最小值之间是否有缺口 默认有缺口
self.t.setWrapping(True)


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

        self.t = QDial(self)
        self.t.move(50, 100)
        self.t.resize(200, 200)
        self.t.setRange(0, 220)

        self.t.setNotchesVisible(True)
        self.t.setPageStep(10)
        self.t.setWrapping(True)
        self.t.setNotchTarget(1)

        self.t.valueChanged.connect(lambda val: print('val:', val))



    def btn_click(self):


        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())