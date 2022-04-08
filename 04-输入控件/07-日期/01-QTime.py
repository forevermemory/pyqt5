
import sys
from PyQt5.Qt import *

'''
QTime
QTime.currentTime()
# 计时器 
start()
elapsed()


QDate
QDateTime

'''


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

        self.t = QTime.currentTime()

        # 计时器
        self.t.start()
        # QTime
        # QDate
        # QDateTime

        self.btn = QPushButton('button', self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.btn_click)

    def btn_click(self):
        print(self.t.elapsed())
        # self.t.addSecs(1)
        # self.t.fromString()

    def init_ui(self):


        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())