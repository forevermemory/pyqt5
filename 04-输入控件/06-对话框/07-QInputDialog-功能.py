import sys
from PyQt5.Qt import *

'''
QInputDialog 输入对话框

### 功能作用
QInputDialog.getText(window, "text1", "text2") --> ('txt', bool)
支持: 整型 浮点型 文本(支持下拉输入框) 

### 输入模式
dlg = QInputDialog(window)
DoubleInput = 2
IntInput = 1
TextInput = 0 # 支持下拉列表
dlg.setInputMode(QInputDialog.TextInput)

### 信号
dlg.intValueChanged
dlg.intValueSelected
dlg.doubleValueChanged
dlg.doubleValueSelected
dlg.textValueChanged
dlg.textValueSelected


'''


def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    # code
    def dlg_open_slot():
        # dlg = QInputDialog.getText(window, "text1", "text2")
        # print(dlg)

        dlg = QInputDialog(window)
        DoubleInput = 2
        IntInput = 1
        TextInput = 0 # 支持下拉列表
        dlg.setInputMode(QInputDialog.TextInput)


        # dlg.intValueChanged
        # dlg.intValueSelected
        # dlg.doubleValueChanged
        # dlg.doubleValueSelected
        # dlg.textValueChanged
        # dlg.textValueSelected

        # dlg.accepted.connect()

    btn1 = QPushButton('输入对话框', window)
    btn1.move(50, 50)
    btn1.clicked.connect(dlg_open_slot)

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
