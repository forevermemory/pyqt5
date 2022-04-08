
import sys
from PyQt5.Qt import *

'''
QRubberBand 一般结合鼠标操作 按下选中区域


setGeometry 设置大小

'''


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.btn = QPushButton('button', self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.btn_click)

        self.btn = QPushButton('clear', self)
        self.btn.move(150, 20)
        self.btn.clicked.connect(lambda: self.t.clear())


        for i in range(18):
            cb = QCheckBox(self)
            cb.setText('{}'.format(i+1))
            cb.move(i % 4 * 50 + 100, i // 4 * 60 + 100)

        # 创建橡皮
        self.rb = QRubberBand(QRubberBand.Rectangle, self)


    def mousePressEvent(self, a0: QMouseEvent) -> None:
        # print('mousePressEvent')

        self.origin_pos = a0.pos()
        self.rb.setGeometry(QRect(self.origin_pos, QSize()))
        self.rb.setVisible(True)

        return super(Window, self).mousePressEvent(a0)

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        # print('mouseMoveEvent')

        # 保证无负数
        self.rb.setGeometry(QRect(self.origin_pos, a0.pos()).normalized())

        return super(Window, self).mouseMoveEvent(a0)

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        # 查找元素

        rect = self.rb.geometry()
        for child in self.children():
            if rect.contains(child.geometry()) and child.inherits("QCheckBox"):
                child.toggle()

        self.rb.setVisible(False)
        return super(Window, self).mouseReleaseEvent(a0)


    def btn_click(self):


        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())