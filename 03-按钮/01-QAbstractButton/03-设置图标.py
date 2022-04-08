
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
        btn.move(200, 200)
        btn.resize(200, 100)
        btn.setText("&abc更新时间")

        label = QLabel(self)
        label.setText("label")
        label.move(200, 100)



        ##########
        # 设置图标
        btn.setIcon(QIcon('../images/web.png'))
        btn.setIconSize(QSize(30, 30))




if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())