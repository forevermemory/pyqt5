
import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.origin_x = 0
        self.origin_y = 0

        self.global_x = 0
        self.global_y = 0

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        
        pass

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        print("鼠标按下")

        self.origin_x = a0.x()
        self.origin_y = a0.y()

        self.global_x = a0.globalX()
        self.global_y = a0.globalY()

        print(self.origin_x, self.origin_y, '-', self.global_x, self.global_y)

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        # 没有捕获移动 默认是按下移动
        # print("鼠标移动")

        self.move(self.origin_x + a0.globalX() - self.global_x, self.origin_y + a0.globalY() - self.global_y)

        pass

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        print("鼠标离开")

if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())