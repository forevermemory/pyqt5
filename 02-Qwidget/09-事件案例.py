
import sys
from PyQt5.Qt import *
from PyQt5 import  QtGui

class Mylabel(QLabel):

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        print('键盘按下')
        if a0.key() == Qt.Key_S and a0.modifiers() == Qt.ControlModifier:
            print("按下了 command + s")

        if a0.key() == Qt.Key_S and a0.modifiers() == Qt.ControlModifier | Qt.ShiftModifier:
            print("按下了 command + shift + s")

        # 修饰键
        # Qt.ControlModifier # command按键
        # Qt.NoModifier # 没有修饰键
        # Qt.ShiftModifier # shift 按键按下
        # Qt.AltModifier # alt被按下


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        self.label = Mylabel(self)
        self.label.setText("ooooo")
        self.label.resize(100, 100)
        self.label.move(100, 100)
        self.label.setStyleSheet('background-color:pink')
        # 捕获键盘按下事件
        self.label.grabKeyboard()
        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())