
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
        # 1. 设置鼠标样式
        self.cursor_01_设置鼠标样式()



    def cursor_01_设置鼠标样式(self):
        # self.setCursor(Qt.BusyCursor)
        # Qt.ArrowCursor
        # Qt.UpArrowCursor
        # Qt.CrossCursor
        # Qt.IBeamCursor
        # Qt.WaitCursor
        # Qt.BusyCursor
        # Qt.ForbiddenCursor
        # Qt.WhatsThisCursor
        # Qt.SizeVerCursor
        # Qt.SizeAllCursor
        # Qt.SizeHorCursor
        # Qt.SizeBDiagCursor
        # Qt.SizeFDiagCursor
        # Qt.SplitHCursor
        # Qt.SplitVCursor
        # Qt.OpenHandCursor
        # Qt.ClosedHandCursor

        self.setCursor(Qt.CrossCursor)



if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())