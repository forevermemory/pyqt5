import sys
from PyQt5.Qt import *


# QToolButton 一般为带图标的小按钮 多用于快捷方式

def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    # code
    # 如果图标和文本同时设置 只会显示图标
    btn = QToolButton(window)
    btn.setText("我是按钮")
    btn.setIcon(QIcon("../../images/web.png"))
    btn.setIconSize(QSize(60, 60))

    # 设置tool提示
    btn.setToolTip("这是tooltip")

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
