import sys
from PyQt5.Qt import *


def main():
    app = QApplication(sys.argv)

    window = QWidget()

    window.setWindowTitle("晴天的pyqt学习")
    window.resize(500, 500)
    window.move(300, 200)

    label = QLabel(window)
    label.move(200, 200)
    label.setText("hello world")

    btn1 = QPushButton(window)
    btn1.setText('猜数字')
    btn1.move(230, 300)

    window.show()
    sys.exit(app.exec_())




if __name__ == '__main__':
    main()
