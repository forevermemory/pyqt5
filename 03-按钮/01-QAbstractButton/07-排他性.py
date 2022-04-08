
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

        for i in range(0, 3):
            # btn = QPushButton(self)
            # btn = QRadioButton(self)
            btn = QCheckBox(self)
            btn.move(100, 30+i*30)
            btn.setText("btn-"+str(i))

            btn.setAutoExclusive(True)
            # btn.setChecked(True)
            print(btn.autoExclusive(), btn.isCheckable(), "---", end="\n")




if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())