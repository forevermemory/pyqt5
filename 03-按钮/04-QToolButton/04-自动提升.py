import sys
from PyQt5.Qt import *


# 箭头  箭头的优先级比Qicon高 如果同时设置 会显示箭头
# Qt.NoArrow
# Qt.UpArrow
# Qt.DownArrow
# Qt.LeftArrow
# Qt.RightArrow

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
    btn.setIconSize(QSize(30, 30))

    # 设置tool提示
    btn.setToolTip("这是tooltip")

    btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
    print(btn.toolButtonStyle())

    # 自动提升 类似于QPushButton 的 setFlat
    btn.setAutoRaise(True)

    btn2 = QToolButton(window)
    btn2.move(100,100)
    btn2.setArrowType(Qt.UpArrow)
    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
