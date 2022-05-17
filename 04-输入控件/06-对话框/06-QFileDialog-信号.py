
import sys
from PyQt5.Qt import *

'''
QFileDialog  信号

dlg.currentChanged[str].connect(lambda _p:print("currentChanged:",_p))
dlg.currentUrlChanged[QUrl].connect(lambda _p:print("currentChanged:",_p))

dlg.directoryEntered
dlg.directoryUrlEntered

dlg.filterSelected
dlg.fileSelected
dlg.filesSelected

dlg.urlSelected
dlg.urlsSelected
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
        dlg = QFileDialog(window, "caption", "../../", "")

        dlg.currentChanged[str].connect(lambda _p:print("currentChanged:",_p))
        dlg.currentUrlChanged[QUrl].connect(lambda _p:print("currentChanged:",_p))

        dlg.directoryEntered
        dlg.directoryUrlEntered

        dlg.filterSelected
        dlg.fileSelected
        dlg.filesSelected

        dlg.urlSelected
        dlg.urlsSelected
        dlg.open()

        # dlg.accepted.connect()

    btn1 = QPushButton('文件对话框', window)
    btn1.move(50, 50)
    btn1.clicked.connect(dlg_open_slot)

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
