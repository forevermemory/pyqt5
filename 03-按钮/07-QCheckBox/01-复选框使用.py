import sys
from PyQt5.Qt import *


def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    # code
    c1 = QCheckBox("&python", window)
    c2 = QCheckBox("Java", window)
    c3 = QCheckBox("Golang", window)
    c2.move(0, 30)
    c3.move(0, 60)

    group = QButtonGroup(window)
    group.addButton(c1)
    group.addButton(c2)
    group.addButton(c3)
    group.setExclusive(False)

    # 是否设置为三态
    c1.setTristate(True)
    print(c1.isTristate())

    # 设置复选框的状态
    # Qt.CheckState # 选中
    # Qt.Unchecked # 未选中
    # Qt.PartiallyChecked # 部分选中
    c1.setCheckState(Qt.CheckState)

    # 事件
    c1.stateChanged.connect(lambda state: print(state))

    # 这个选中和部分选中都会触发True
    # c1.toggled.connect(lambda is_check: print(is_check))

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
