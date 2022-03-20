
import sys
from PyQt5.Qt import *
from PyQt5 import  QtGui
from PyQt5 import  QtCore

# 如果某个控件相关事件没有处理, 会传给改控件的 父对象
# evt.accept() 接收了事件 不会继续向父对象传递
# evt.ignore() 忽略事件, 会继续向父对象传递

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):

        pass

    ##############各种事件###################
    # 窗口显示和关闭
    def showEvent(self, a0: QShowEvent) -> None:
        print('窗口显示')

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        print('窗口关闭')

    # 移动事件
    def moveEvent(self, a0: QtGui.QMoveEvent) -> None:
        print('移动事件')

    # 调整大小
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        print('调整大小')

    # 鼠标事件
    def enterEvent(self, a0: QtCore.QEvent) -> None:
        print('鼠标 enterEvent')

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        print('鼠标 leaveEvent')

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        print('鼠标 mousePressEvent')

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        print('鼠标 mouseReleaseEvent')

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        print('鼠标 mouseDoubleClickEvent')

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        # 鼠标按下后移动事件
        # 设置鼠标追踪后 鼠标移动也会触发
        print('鼠标 mouseMoveEvent')
        # def setMouseTracking(self, enable: bool) -> None:
        #     pass

    # 键盘事件
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        print('键盘 keyPressEvent')

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        print('键盘 keyReleaseEvent')

    # 焦点事件

    def focusOutEvent(self, a0: QtGui.QFocusEvent) -> None:
        print('焦点 focusOutEvent')

    def focusInEvent(self, a0: QtGui.QFocusEvent) -> None:
        print('焦点 focusInEvent')

    # 拖拽事件
    def dragEnterEvent(self, a0: QtGui.QDragEnterEvent) -> None:
        print('拖拽事件 dragEnterEvent')

    def dragLeaveEvent(self, a0: QtGui.QDragLeaveEvent) -> None:
        print('拖拽事件 dragLeaveEvent')

    def dragMoveEvent(self, a0: QtGui.QDragMoveEvent) -> None:
        print('拖拽事件 dragMoveEvent')

    def dropEvent(self, a0: QtGui.QDropEvent) -> None:
        print('拖拽事件 拖拽放下')

    # 绘制事件
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        print('paintEvent 显示控件更新控件时候调用')

    # 改变事件
    def changeEvent(self, a0: QtCore.QEvent) -> None:
        print('changeEvent 窗体改变 字体改变时候调用')

    # 右键菜单
    def contextMenuEvent(self, a0: QtGui.QContextMenuEvent) -> None:
        print('contextMenuEvent 右键菜单')

    # 输入法
    def inputMethodEvent(self, a0: QtGui.QInputMethodEvent) -> None:
        print('inputMethodEvent 输入法')



if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())