
import sys
from PyQt5.Qt import *


# childAt(x, y)
# childrenRect()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        for i in range(1,11):
            label = QLabel(self)
            label.setText("标签-"+str(i))
            label.move(10+i*30, 10+i*30)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        print("鼠标按下了")
        #
        label = self.childAt(a0.x(), a0.y())
        print(label)
        if label is not None:
            label.setStyleSheet("background-color: pink")

if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())