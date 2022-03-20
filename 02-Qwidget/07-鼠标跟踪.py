import sys
from PyQt5.Qt import *


class MyWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(MyWidget, self).__init__(*args, **kwargs)

        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        # code
        # 设置为True之后 鼠标移动就会出发mouseMoveEvent事件
        self.setMouseTracking(True)

        self.label = QLabel(self)
        self.label.setText("qingtian")



    # 默认情况只有鼠标按下后 在移动才会出发这个事件
    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        print("mouse move", a0.pos())
        self.label.move(a0.pos().x(), a0.pos().y())



def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = MyWidget()





    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
