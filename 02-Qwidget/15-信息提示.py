
import sys
from PyQt5.Qt import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        # 手动加载
        self.statusBar()

        btn = QPushButton(self)
        btn.setText("click me")

        # 当鼠标悬停在某个控件上面 在状态栏提示的文本信息
        btn.setStatusTip("这是信息提示-btn")
        self.setStatusTip("这是信息提示-QMainWindow")

        # 工具提示 鼠标放上后在旁边显示的提示信息
        btn.setToolTip("这是工具提示")
        btn.setToolTipDuration(1000)


        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())