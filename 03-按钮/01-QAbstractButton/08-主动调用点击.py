
import sys
from datetime import  datetime

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):

        btn = QPushButton(self)
        btn.move(100, 30)
        btn.resize(100,100)
        btn.setText("btn-1")


        btn2 = QPushButton(self)
        btn2.move(220, 30)
        btn2.resize(100,100)
        btn2.setText("btn-2")
        btn2.clicked.connect(lambda:print("btn2 被电击了"))


        def cao():
            # 触发点击
            # btn2.click()

            # 点击后模拟被按下几秒
            btn2.animateClick(1000)

        btn.clicked.connect(cao)


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())