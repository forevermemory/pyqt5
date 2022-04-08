
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

        # btn = QPushButton(self)
        btn = QCheckBox(self)
        btn.move(100, 30)
        btn.resize(200, 200)
        btn.setText("btn-aaaa")

        # 按下后会触发pressed 正常松开会触发released 如果不松开移到按钮之外的区域也会触发released
        # btn.pressed.connect(lambda: print("按钮被按下了"))
        # btn.released.connect(lambda: print("按钮被松开了"))

        #  如果不松开移到按钮之外的区域 不会 触发 clicked
        # btn.clicked.connect(lambda: print("按钮被点击了"))

        # btn.setCheckable(True)
        btn.toggled.connect(lambda: print("按钮被切换了"))


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())