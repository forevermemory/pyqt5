import sys
from PyQt5.Qt import *

'''
QAbstractSpinBox 整数步长调节

# 设置数值范围
self.t.setMaximum(10)
self.t.setMinimum(1)

self.t.setRange(1, 10) 闭区间


# 数值循环 到最大或者最小循环
self.t.setWrapping(True)
print(self.t.wrapping())

# 设置步长
self.t.setSingleStep(2)

# 设置前缀后者后缀
self.t.setPrefix("前缀-")
self.t.setSuffix("-后缀")

# 最小值设置特殊文本
self.t.setSpecialValueText("我是最小值")

# 进制控制
self.t.setDisplayIntegerBase(2)

# 内容获取
self.t.value() # 只获取值 和前后缀没关系
self.t.text()
self.t.lineEdit().text()

# 自定义展示格式
重写 textFormValue

# 信号
valueChanged[str]
valueChanged[int]

'''



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.t = QSpinBox(self)
        self.t.move(50, 100)
        self.t.resize(300, 50)

        self.t.editingFinished.connect(lambda: print("end edit"))

        self.btn = QPushButton('button', self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.btn_click)

        self.btn = QPushButton('clear', self)
        self.btn.move(150, 20)
        self.btn.clicked.connect(lambda: self.t.clear())

    def btn_click(self):

        # 设置数值范围
        # self.t.setMaximum(10)
        # self.t.setMinimum(1)
        self.t.setRange(1, 10)

        # 数值循环 到最大或者最小循环
        self.t.setWrapping(True)
        print(self.t.wrapping())

        # 设置步长
        self.t.setSingleStep(2)

        # 设置前缀后者后缀
        self.t.setPrefix("前缀-")
        self.t.setSuffix("-后缀")

        # 最小值设置特殊文本
        self.t.setSpecialValueText("我是最小值")

        #
        self.t.setDisplayIntegerBase(2)

        print(self.t.value())
        self.t.text()
        self.t.lineEdit().text()

        self.t.valueChanged

        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())