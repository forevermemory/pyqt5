

import sys
from PyQt5.Qt import *



class MyButton(QAbstractButton):
    # NotImplementedError: QAbstractButton.paintEvent() is abstract and must be overridden

    def paintEvent(self, e: QPaintEvent) -> None:
        # 1.创建画家
        painter = QPainter(self)

        # 2. 设置画笔
        pen = QPen(QColor(200, 100, 30), 3)
        painter.setPen(pen)

        # 3. 画画
        painter.drawText(20, 30 ,self.text())
        painter.drawEllipse(0, 0, 100, 80)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        btn = MyButton(self)
        btn.setText("QAbstractButton")
        btn.resize(100, 100)
        btn.clicked.connect(lambda:print("aaa"))
        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())