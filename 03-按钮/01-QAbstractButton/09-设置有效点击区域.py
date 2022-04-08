
import sys
from datetime import  datetime

from PyQt5.Qt import *



class MyButton(QPushButton):
    def hitButton(self, pos: QPoint) -> bool:
        # 返回True才会触发点击的事件
        print(pos)
        if pos.x() > 100:
            return True

        return False

    def paintEvent(self, e: QPaintEvent) -> None:
        super().paintEvent(e)
        # 1.创建画家
        painter = QPainter(self)

        # 2. 设置画笔
        pen = QPen(QColor(200, 100, 30), 3)
        painter.setPen(pen)

        # 3. 画画
        painter.drawEllipse(self.x()/2, self.y()/2, self.x(), self.x())


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):

        btn = MyButton(self)
        btn.move(100, 30)
        btn.resize(200, 200)
        btn.setText("btn-")




        def cao():
            print("点击")
            
        btn.clicked.connect(cao)


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())