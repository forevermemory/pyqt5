
import sys
from PyQt5.Qt import *

'''
QLabel
label.linkHovered
label.linkActivated

'''


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法



    def btn_click(self):
       pass

    def init_ui(self):

        label = QLabel("Qlabel-hello(&s)", self)
        label.move(100, 100)
        # label.resize(300, 300)
        label.setStyleSheet("border: 1px solid pink")


        label.linkHovered
        label.linkActivated





if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())