
import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        t1 = QLineEdit(self)
        t1.move(100,100)

        t2 = QLineEdit(self)
        t2.move(100,200)

        t3 = QLineEdit(self)
        t3.move(100,300)

        # 指定控件获取焦点
        # t3.setFocus()

        # 设置获取焦点策略
        # Qt.TabFocus # 只能通过tab切换
        # Qt.ClickFocus # 只能通过click
        # Qt.StrongFocus # 上面两个都可以
        # Qt.NoFocus # 不可以通过上面两种方式 但是setFocus可用
        t3.setFocusPolicy(Qt.StrongFocus)
        t3.clearFocus()

        #################
        # 通过父控件设置子控件的焦点
        # self.focusNextChild()
        # self.focusPreviousChild()

        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())