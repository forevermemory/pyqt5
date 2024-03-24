
import sys
from PyQt5.Qt import *

'''
### 自定义信号 例如按钮的右击



'''


class Btn(QPushButton):

    # 自定义信号

    # 传递一个参数
    # rightClicked = pyqtSignal(str)

    # 可变类型参数
    # rightClicked = pyqtSignal([str], [int])

    # 可变类型参数2
    rightClicked = pyqtSignal([str], [int, str])

    def mousePressEvent(self, e: QMouseEvent) -> None:
        print("鼠标按下", e.button())
        if e.button() == Qt.RightButton:
            # 发射右击信号
            # self.rightClicked[str].emit(self.text())
            self.rightClicked[int, str].emit(1, "hello")

        return super().mousePressEvent(e)


def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("title-")
    window.resize(500, 500)
    window.move(300, 200)
    # label1 = QLabel("标签1", window)

    btn = Btn("按钮", window)
    btn.pressed.connect(lambda: print("btn--presed"))
    # btn.rightClicked[str].connect(lambda x: print("btn--右击", x))
    # btn.rightClicked[int].connect(lambda x: print("btn--右击", x))
    btn.rightClicked[int, str].connect(lambda x, y : print("btn--右击", x, y))




    window.show()
    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
