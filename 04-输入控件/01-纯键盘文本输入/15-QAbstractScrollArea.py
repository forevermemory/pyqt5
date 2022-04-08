import sys
from PyQt5.Qt import *

# 设置水平垂直滚动条 待定

# # 设置滚动策略
# Qt.ScrollBarAsNeeded  # 默认值
# Qt.ScrollBarAlwaysOn  # 一直显示
# Qt.ScrollBarAlwaysOff  # 一直关闭
# t.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # mac没有显示出来
# # t.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#
# # 右下角按钮
# btn = QPushButton(window)
# btn.setIcon(QIcon("../../images/web.png"))
# t.setCornerWidget(btn)

def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    # code
    t = QTextEdit('hello world, china', window)
    # 设置水平垂直滚动条 待定

    # 设置滚动策略
    Qt.ScrollBarAsNeeded # 默认值
    Qt.ScrollBarAlwaysOn # 一直显示
    Qt.ScrollBarAlwaysOff # 一直关闭
    t.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn) # mac没有显示出来
    # t.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    # 右下角按钮
    btn = QPushButton(window)
    btn.setIcon(QIcon("../../images/web.png"))
    t.setCornerWidget(btn)

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
