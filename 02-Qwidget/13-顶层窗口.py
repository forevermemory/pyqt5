

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

        # 窗口标题
        self.setWindowTitle("setWindowTitle")
        print(self.windowTitle())

        # 窗口图标
        self.setWindowIcon(QIcon("../images/web.png"))
        print(self.windowIcon())

        # 透明度
        self.setWindowOpacity(0.5)
        print(self.windowOpacity())

        # 窗口状态
        # Qt.WindowNoState # 无状态
        # Qt.WindowMinimized
        # Qt.WindowMaximized
        # Qt.WindowFullScreen
        # Qt.WindowActive # 活动窗口 展示在第一个的窗口

        # 方法一
        # self.setWindowState(Qt.WindowNoState)

        # 方法二
        # self.showMaximized()
        # self.showMinimized()
        # self.showNormal()
        # self.showFullScreen()

        # self.isMaximized()
        # self.isMinimized()
        # self.isFullScreen()


        #####################
        # windowFlag 窗口标志
        # flags 枚举值
        Qt.Widget
        Qt.Sheet
        Qt.Drawer
        Qt.Window
        Qt.Dialog
        Qt.Popup
        Qt.Tool
        Qt.Desktop
        Qt.ToolTip
        Qt.SplashScreen
        Qt.SubWindow

        # Hint
        Qt.MSWindowsFixedSizeDialogHint
        Qt.FramelessWindowHint
        Qt.CustomizeWindowHint
        Qt.WindowTitleHint
        Qt.WindowSystemMenuHint
        Qt.WindowMaximizeButtonHint
        Qt.WindowMinimizeButtonHint
        Qt.WindowMinMaxButtonsHint
        Qt.WindowCloseButtonHint
        Qt.WindowContextHelpButtonHint
        Qt.WindowStaysOnTopHint
        Qt.WindowStaysOnBottomHint
        self.setWindowFlags()


        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())