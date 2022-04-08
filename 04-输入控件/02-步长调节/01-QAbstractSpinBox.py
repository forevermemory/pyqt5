
import sys
from PyQt5.Qt import *

'''
QAbstractSpinBox 可以直接使用 

子类化的化 可以重写 stepEnabled stepBy

# 设置加速
self.t.setAccelerated(True)

# 设置只读
self.t.setReadOnly(True)

# 设置内容
self.t.lineEdit().xxx
self.t.text() 获取内容

# 对齐方式
self.t.setAlignment(Qt.AlignCenter)

# 是否有边框
self.t.setFrame(False)


# 验证内容 
# 重写 validate fixup

# 信号
editingFinished

'''

class MyQAbstractSpinBox(QAbstractSpinBox):

    # def validate(self, input: str, pos: int) -> typing.Tuple[QtGui.QValidator.State, str, int]:
    #     pass
    #
    # def fixup(self, input: str) -> str:
    #     return  input

    def stepEnabled(self):
        # StepDownEnabled = 2
        # StepNone = 0
        # StepUpEnabled = 1

        return QAbstractSpinBox.StepDownEnabled | QAbstractSpinBox.StepUpEnabled

    def stepBy(self, steps: int) -> None:
        val = int(self.text())
        self.lineEdit().setText(str(val+steps))


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.t = MyQAbstractSpinBox(self)
        self.t.move(50, 100)
        self.t.resize(300, 50)

        self.t.editingFinished.connect(lambda:print("end edit"))

        self.btn = QPushButton('button', self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.btn_click)

        self.btn = QPushButton('clear', self)
        self.btn.move(150, 20)
        self.btn.clicked.connect(lambda: self.t.clear())



    def btn_click(self):
        self.t.setAccelerated(True)
        self.t.lineEdit().setText('1')
        self.t.setReadOnly(True)
        self.t.setAlignment(Qt.AlignCenter)
        self.t.setFrame(False)
        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())